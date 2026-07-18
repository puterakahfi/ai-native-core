#!/usr/bin/env python3
"""Validate canonical identity and migration safety for Native AI contracts."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_ROOT = ROOT / "contracts" / "skills"


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def main() -> int:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    capabilities: dict[str, Path] = {}
    aliases: defaultdict[str, list[Path]] = defaultdict(list)
    capability_aliases: defaultdict[str, list[Path]] = defaultdict(list)

    contract_paths = sorted(CONTRACTS_ROOT.rglob("*.contract.yaml"))
    if not contract_paths:
        print("ERROR: no skill contracts found")
        return 1

    records: list[tuple[Path, dict]] = []

    for path in contract_paths:
        rel = path.relative_to(ROOT)
        try:
            payload = yaml.safe_load(path.read_text()) or {}
        except Exception as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue

        contract = payload.get("skill_contract")
        if not isinstance(contract, dict):
            errors.append(f"{rel}: missing skill_contract mapping")
            continue

        records.append((path, contract))
        contract_id = str(contract.get("id", "")).strip()
        capability = str(contract.get("capability", "")).strip()
        expected_id = path.name.removesuffix(".contract.yaml")

        if not contract_id:
            errors.append(f"{rel}: missing id")
        elif contract_id != expected_id:
            errors.append(
                f"{rel}: filename/id mismatch: expected id '{expected_id}', got '{contract_id}'"
            )
        elif contract_id in ids:
            errors.append(
                f"{rel}: duplicate id '{contract_id}', already owned by {ids[contract_id].relative_to(ROOT)}"
            )
        else:
            ids[contract_id] = path

        if not capability:
            errors.append(f"{rel}: missing capability")
        elif capability in capabilities:
            errors.append(
                f"{rel}: duplicate capability '{capability}', already owned by "
                f"{capabilities[capability].relative_to(ROOT)}"
            )
        else:
            capabilities[capability] = path

        for alias in as_list(contract.get("aliases")):
            aliases[alias].append(path)

        for alias in as_list(contract.get("capability_aliases")):
            capability_aliases[alias].append(path)

        for superseded in as_list(contract.get("supersedes")):
            superseded_path = ROOT / superseded
            if superseded_path.exists():
                errors.append(
                    f"{rel}: superseded contract still exists: {superseded}"
                )

    for alias, owners in sorted(aliases.items()):
        if len(owners) > 1:
            owner_list = ", ".join(str(path.relative_to(ROOT)) for path in owners)
            errors.append(f"alias '{alias}' is claimed by multiple contracts: {owner_list}")
        if alias in ids:
            alias_owner = owners[0].relative_to(ROOT)
            canonical_owner = ids[alias].relative_to(ROOT)
            errors.append(
                f"alias '{alias}' on {alias_owner} collides with canonical id owned by {canonical_owner}"
            )

    for alias, owners in sorted(capability_aliases.items()):
        if len(owners) > 1:
            owner_list = ", ".join(str(path.relative_to(ROOT)) for path in owners)
            errors.append(
                f"capability alias '{alias}' is claimed by multiple contracts: {owner_list}"
            )
        if alias in capabilities:
            alias_owner = owners[0].relative_to(ROOT)
            canonical_owner = capabilities[alias].relative_to(ROOT)
            errors.append(
                f"capability alias '{alias}' on {alias_owner} collides with canonical capability "
                f"owned by {canonical_owner}"
            )

    if errors:
        print("Contract identity validation failed:\n")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} identity violation(s).")
        return 1

    print(
        f"PASS — {len(records)} skill contracts have unique ids, capabilities, aliases, "
        "and clean supersession paths."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
