#!/usr/bin/env python3
"""Validate first-class Native AI Engineering port contracts."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PORTS_ROOT = ROOT / "contracts" / "ports"
SCHEMA_PATH = ROOT / "schemas" / "port-contract.schema.yaml"

KIND_BY_DIRECTORY = {
    "integration": "integration_port",
    "control": "control_port",
    "product-surface": "product_surface_port",
    "capability-composition": "capability_composition_port",
}


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError("document root must be a mapping")
    return payload


def format_schema_error(error: Any) -> str:
    location = ".".join(str(part) for part in error.absolute_path)
    if not location:
        location = "<root>"
    return f"{location}: {error.message}"


def validate_contract(
    path: Path,
    schema_validator: Draft202012Validator,
    *,
    root: Path = ROOT,
) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []

    try:
        payload = load_yaml(path)
    except Exception as exc:
        return None, [f"invalid YAML: {exc}"]

    schema_errors = sorted(
        schema_validator.iter_errors(payload),
        key=lambda error: [str(item) for item in error.absolute_path],
    )
    errors.extend(format_schema_error(error) for error in schema_errors)

    contract = payload.get("port_contract")
    if not isinstance(contract, dict):
        return None, errors

    contract_id = str(contract.get("id", "")).strip()
    expected_id = path.name.removesuffix(".port.yaml")
    if contract_id and contract_id != expected_id:
        errors.append(
            f"filename/id mismatch: expected '{expected_id}', got '{contract_id}'"
        )
    if contract_id.endswith("-port"):
        errors.append("id must omit the redundant '-port' suffix")

    try:
        relative = path.relative_to(root / "contracts" / "ports")
        directory = relative.parts[0]
    except ValueError:
        directory = ""

    expected_kind = KIND_BY_DIRECTORY.get(directory)
    actual_kind = contract.get("kind")
    if expected_kind and actual_kind != expected_kind:
        errors.append(
            f"directory/kind mismatch: directory '{directory}' requires '{expected_kind}'"
        )
    elif not expected_kind:
        errors.append(f"unknown port kind directory '{directory or '<none>'}'")

    boundary = contract.get("boundary")
    if isinstance(boundary, dict):
        owns = set(boundary.get("owns") or [])
        delegates = set(boundary.get("delegates") or [])
        does_not_own = set(boundary.get("does_not_own") or [])
        overlap = {
            "owns/delegates": owns & delegates,
            "owns/does_not_own": owns & does_not_own,
            "delegates/does_not_own": delegates & does_not_own,
        }
        for label, values in overlap.items():
            if values:
                errors.append(
                    f"boundary overlap in {label}: {', '.join(sorted(values))}"
                )

    transitions = contract.get("state_transitions")
    if isinstance(transitions, list):
        families = {
            transition.get("status_family")
            for transition in transitions
            if isinstance(transition, dict) and transition.get("status_family")
        }
        if len(families) > 1:
            errors.append(
                "one port contract may own transitions from only one typed status family"
            )

    authorization = contract.get("authorization")
    if isinstance(authorization, dict):
        mode = authorization.get("mode")
        required_for = authorization.get("required_for")
        authority_ref = authorization.get("authority_reference_required")
        if mode == "none" and required_for:
            errors.append("authorization mode 'none' requires an empty required_for list")
        if mode == "none" and authority_ref is True:
            errors.append(
                "authorization mode 'none' cannot require an authority reference"
            )
        if mode == "required" and not required_for:
            errors.append(
                "authorization mode 'required' requires at least one governed action"
            )
        if mode == "required" and authority_ref is not True:
            errors.append(
                "authorization mode 'required' requires authority_reference_required=true"
            )

    interactions = contract.get("interactions")
    if isinstance(interactions, dict):
        for group in ("requests", "responses", "events", "streams"):
            identifiers: list[str] = []
            for item in interactions.get(group) or []:
                if isinstance(item, dict) and item.get("id"):
                    identifiers.append(str(item["id"]))
            duplicates = sorted(
                identifier
                for identifier in set(identifiers)
                if identifiers.count(identifier) > 1
            )
            if duplicates:
                errors.append(f"duplicate {group} ids: {', '.join(duplicates)}")

    compatibility = contract.get("compatibility")
    if isinstance(compatibility, dict):
        for legacy_ref in compatibility.get("legacy_contract_refs") or []:
            legacy_path = root / str(legacy_ref)
            if not legacy_path.exists():
                errors.append(f"legacy contract reference does not exist: {legacy_ref}")

    return contract, errors


def validate_paths(
    paths: list[Path],
    *,
    schema_path: Path = SCHEMA_PATH,
    root: Path = ROOT,
) -> list[str]:
    try:
        schema = load_yaml(schema_path)
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"{schema_path}: invalid schema: {exc}"]

    schema_validator = Draft202012Validator(schema)
    errors: list[str] = []
    ids: dict[str, Path] = {}
    capabilities: dict[str, Path] = {}
    aliases: defaultdict[str, list[Path]] = defaultdict(list)

    for path in sorted(paths):
        contract, contract_errors = validate_contract(path, schema_validator, root=root)
        relative = path
        try:
            relative = path.relative_to(root)
        except ValueError:
            pass

        for error in contract_errors:
            errors.append(f"{relative}: {error}")

        if not contract:
            continue

        contract_id = str(contract.get("id", "")).strip()
        capability = str(contract.get("capability", "")).strip()

        if contract_id:
            if contract_id in ids:
                errors.append(
                    f"{relative}: duplicate id '{contract_id}', already owned by "
                    f"{ids[contract_id].relative_to(root)}"
                )
            else:
                ids[contract_id] = path

        if capability:
            if capability in capabilities:
                errors.append(
                    f"{relative}: duplicate capability '{capability}', already owned by "
                    f"{capabilities[capability].relative_to(root)}"
                )
            else:
                capabilities[capability] = path

        compatibility = contract.get("compatibility")
        if isinstance(compatibility, dict):
            for alias in compatibility.get("aliases") or []:
                aliases[str(alias)].append(path)

    for alias, owners in sorted(aliases.items()):
        if len(owners) > 1:
            owner_list = ", ".join(str(path.relative_to(root)) for path in owners)
            errors.append(
                f"port alias '{alias}' is claimed by multiple contracts: {owner_list}"
            )
        if alias in ids:
            alias_owner = owners[0].relative_to(root)
            canonical_owner = ids[alias].relative_to(root)
            errors.append(
                f"port alias '{alias}' on {alias_owner} collides with canonical id "
                f"owned by {canonical_owner}"
            )

    return errors


def discover_paths(ports_root: Path) -> list[Path]:
    return sorted(ports_root.rglob("*.port.yaml"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate first-class Native AI Engineering port contracts."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional port contract paths. Defaults to contracts/ports/**/*.port.yaml.",
    )
    parser.add_argument(
        "--schema",
        default=str(SCHEMA_PATH),
        help="Port contract schema path.",
    )
    args = parser.parse_args()

    paths = [Path(path).resolve() for path in args.paths]
    if not paths:
        paths = discover_paths(PORTS_ROOT)

    if not paths:
        print("ERROR: no port contracts found")
        return 1

    errors = validate_paths(
        paths,
        schema_path=Path(args.schema).resolve(),
        root=ROOT,
    )
    if errors:
        print("Port contract validation failed:\n")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} port contract violation(s).")
        return 1

    print(
        f"PASS — {len(paths)} port contract(s) satisfy schema, identity, kind, "
        "boundary, lifecycle, authorization, alias, and migration-reference checks."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
