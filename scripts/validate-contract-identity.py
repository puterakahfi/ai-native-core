#!/usr/bin/env python3
"""Validate canonical identity and migration safety across Native AI contracts."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_ROOT = ROOT / "contracts"
SUFFIXES = (".contract.yaml", ".port.yaml", ".test.yaml")

ROOT_BY_KIND = {
    "skill_contract": "skill_contract",
    "workflow_contract": "workflow_contract",
    "runtime_contract": "runtime_contract",
    "port_contract": "port_contract",
    "behavioral_test_contract": "skill_test",
    "compatibility_manifest": "compatibility_manifest",
    "adapter_manifest": "port_adapter_reference",
    "domain_contract": "domain_contract",
}

SCHEMA_BY_KIND = {
    kind: f"schemas/{kind.replace('_', '-')}.schema.yaml"
    for kind in ROOT_BY_KIND
}
SCHEMA_BY_KIND["behavioral_test_contract"] = "schemas/behavioral-test-contract.schema.yaml"
SCHEMA_BY_KIND["compatibility_manifest"] = "schemas/compatibility-manifest.schema.yaml"
SCHEMA_BY_KIND["adapter_manifest"] = "schemas/adapter-manifest.schema.yaml"
SCHEMA_BY_KIND["domain_contract"] = "schemas/domain-contract.schema.yaml"

KIND_BY_DIRECTORY = {
    "skills": "skill_contract",
    "workflows": "workflow_contract",
    "runtime": "runtime_contract",
    "ports": "port_contract",
    "tests": "behavioral_test_contract",
    "compatibility": "compatibility_manifest",
    "adapters": "adapter_manifest",
    "domains": "domain_contract",
}


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def artifact_paths() -> list[Path]:
    return sorted(
        path
        for path in CONTRACTS_ROOT.rglob("*.yaml")
        if path.name != "manifest.yaml" and path.name.endswith(SUFFIXES)
    )


def filename_id(path: Path) -> str:
    for suffix in SUFFIXES:
        if path.name.endswith(suffix):
            return path.name[: -len(suffix)]
    return path.stem


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError("document root must be a mapping")
    return payload


def contract_id(kind: str, body: dict[str, Any], path: Path) -> str:
    if kind == "behavioral_test_contract":
        return filename_id(path)
    if kind == "adapter_manifest":
        return str(body.get("adapter_id", "")).strip()
    return str(body.get("id", "")).strip()


def main() -> int:
    errors: list[str] = []
    identities: dict[tuple[str, str], Path] = {}
    skill_capabilities: dict[str, Path] = {}
    skill_aliases: defaultdict[str, list[Path]] = defaultdict(list)
    capability_aliases: defaultdict[str, list[Path]] = defaultdict(list)
    compatibility_sources: dict[str, Path] = {}
    records = 0

    paths = artifact_paths()
    if not paths:
        print("ERROR: no contract artifacts found")
        return 1

    for path in paths:
        rel = path.relative_to(ROOT)
        try:
            payload = load_yaml(path)
        except Exception as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue

        schema_identity = payload.get("contract_schema")
        if not isinstance(schema_identity, dict):
            errors.append(f"{rel}: missing contract_schema mapping")
            continue

        kind = str(schema_identity.get("kind", "")).strip()
        root_key = ROOT_BY_KIND.get(kind)
        if not root_key:
            errors.append(f"{rel}: unsupported contract kind '{kind}'")
            continue

        expected_kind = KIND_BY_DIRECTORY.get(rel.parts[1] if len(rel.parts) > 1 else "")
        if expected_kind != kind:
            errors.append(
                f"{rel}: directory requires kind '{expected_kind}', got '{kind}'"
            )

        expected_schema = SCHEMA_BY_KIND[kind]
        actual_schema = str(schema_identity.get("path", "")).strip()
        if actual_schema != expected_schema:
            errors.append(
                f"{rel}: kind '{kind}' requires schema path '{expected_schema}', got '{actual_schema}'"
            )
        if not schema_identity.get("version"):
            errors.append(f"{rel}: missing schema version")

        body = payload.get(root_key)
        if not isinstance(body, dict):
            errors.append(f"{rel}: missing {root_key} mapping")
            continue

        records += 1
        identity = contract_id(kind, body, path)
        if not identity:
            errors.append(f"{rel}: missing contract identity")
        elif identity != filename_id(path):
            errors.append(
                f"{rel}: filename/id mismatch: expected '{filename_id(path)}', got '{identity}'"
            )
        elif (kind, identity) in identities:
            errors.append(
                f"{rel}: duplicate identity '{kind}:{identity}', already owned by "
                f"{identities[(kind, identity)].relative_to(ROOT)}"
            )
        else:
            identities[(kind, identity)] = path

        if kind == "skill_contract":
            capability = str(body.get("capability", "")).strip()
            if not capability:
                errors.append(f"{rel}: missing capability")
            elif capability in skill_capabilities:
                errors.append(
                    f"{rel}: duplicate skill capability '{capability}', already owned by "
                    f"{skill_capabilities[capability].relative_to(ROOT)}"
                )
            else:
                skill_capabilities[capability] = path

            for alias in as_list(body.get("aliases")):
                skill_aliases[alias].append(path)
            for alias in as_list(body.get("capability_aliases")):
                capability_aliases[alias].append(path)
            for superseded in as_list(body.get("supersedes")):
                if (ROOT / superseded).exists():
                    errors.append(f"{rel}: superseded contract still exists: {superseded}")

        if kind == "compatibility_manifest":
            for alias in body.get("aliases") or []:
                if not isinstance(alias, dict):
                    continue
                source = str(alias.get("from_path", ""))
                target = str(alias.get("to_path", ""))
                if source in compatibility_sources:
                    errors.append(
                        f"{rel}: legacy path '{source}' is already owned by "
                        f"{compatibility_sources[source].relative_to(ROOT)}"
                    )
                else:
                    compatibility_sources[source] = path
                if (ROOT / source).exists():
                    errors.append(f"{rel}: legacy alias source still exists: {source}")
                if not (ROOT / target).exists():
                    errors.append(f"{rel}: canonical alias target does not exist: {target}")

    for alias, owners in sorted(skill_aliases.items()):
        if len(owners) > 1:
            owner_list = ", ".join(str(path.relative_to(ROOT)) for path in owners)
            errors.append(f"skill alias '{alias}' is claimed by multiple contracts: {owner_list}")
        if ("skill_contract", alias) in identities:
            errors.append(
                f"skill alias '{alias}' collides with canonical skill identity owned by "
                f"{identities[('skill_contract', alias)].relative_to(ROOT)}"
            )

    for alias, owners in sorted(capability_aliases.items()):
        if len(owners) > 1:
            owner_list = ", ".join(str(path.relative_to(ROOT)) for path in owners)
            errors.append(
                f"capability alias '{alias}' is claimed by multiple contracts: {owner_list}"
            )
        if alias in skill_capabilities:
            errors.append(
                f"capability alias '{alias}' collides with canonical capability owned by "
                f"{skill_capabilities[alias].relative_to(ROOT)}"
            )

    if errors:
        print("Contract identity validation failed:\n")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} identity violation(s).")
        return 1

    print(
        f"PASS — {records} contract artifacts have declared schema identity, canonical "
        "filename ownership, unique family IDs, and clean migration aliases."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
