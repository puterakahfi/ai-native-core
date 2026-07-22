#!/usr/bin/env python3
"""Validate all Native AI contract families, migrations, and manifest parity."""

from __future__ import annotations

import hashlib
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from schema_validation import format_schema_error, load_yaml, schema_store, validator_for

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"
SCHEMAS = ROOT / "schemas"
MANIFEST = CONTRACTS / "manifest.yaml"

KIND_TO_SCHEMA = {
    "skill_contract": "schemas/skill-contract.schema.yaml",
    "workflow_contract": "schemas/workflow-contract.schema.yaml",
    "runtime_contract": "schemas/runtime-contract.schema.yaml",
    "port_contract": "schemas/port-contract.schema.yaml",
    "behavioral_test_contract": "schemas/behavioral-test-contract.schema.yaml",
    "compatibility_manifest": "schemas/compatibility-manifest.schema.yaml",
    "adapter_manifest": "schemas/adapter-manifest.schema.yaml",
    "domain_contract": "schemas/domain-contract.schema.yaml",
}

KIND_TO_ROOT = {
    "skill_contract": "skill_contract",
    "workflow_contract": "workflow_contract",
    "runtime_contract": "runtime_contract",
    "port_contract": "port_contract",
    "behavioral_test_contract": "skill_test",
    "compatibility_manifest": "compatibility_manifest",
    "adapter_manifest": "port_adapter_reference",
    "domain_contract": "domain_contract",
}

PATH_KIND = {
    "skills": "skill_contract",
    "workflows": "workflow_contract",
    "runtime": "runtime_contract",
    "ports": "port_contract",
    "tests": "behavioral_test_contract",
    "compatibility": "compatibility_manifest",
    "adapters": "adapter_manifest",
    "domains": "domain_contract",
}

SUFFIXES = (".contract.yaml", ".port.yaml", ".test.yaml")


def artifact_paths(root: Path = ROOT) -> list[Path]:
    contracts = root / "contracts"
    return sorted(
        path
        for path in contracts.rglob("*.yaml")
        if path.name != "manifest.yaml" and path.name.endswith(SUFFIXES)
    )


def filename_id(path: Path) -> str:
    for suffix in SUFFIXES:
        if path.name.endswith(suffix):
            return path.name[: -len(suffix)]
    return path.stem


def checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def parse_version(value: str) -> tuple[int, int, int]:
    core = value.split("-", 1)[0]
    parts = core.split(".")
    if len(parts) not in (2, 3) or not all(part.isdigit() for part in parts):
        raise ValueError(f"invalid semantic version '{value}'")
    return int(parts[0]), int(parts[1]), int(parts[2]) if len(parts) == 3 else 0


def pin_accepts(pin: str, version: str) -> bool:
    prefix = pin[0] if pin and pin[0] in "^~" else ""
    requested = parse_version(pin[1:] if prefix else pin)
    actual = parse_version(version)
    if prefix == "":
        return actual == requested
    if actual < requested:
        return False
    if prefix == "~":
        return actual[:2] == requested[:2]
    if requested[0] == 0:
        return actual[0] == 0 and actual[1] == requested[1]
    return actual[0] == requested[0]


def expected_kind_for_path(path: Path, root: Path = ROOT) -> str | None:
    try:
        first = path.relative_to(root / "contracts").parts[0]
    except ValueError:
        return None
    return PATH_KIND.get(first)


def contract_identity(kind: str, body: dict[str, Any], path: Path) -> tuple[str, str]:
    if kind == "behavioral_test_contract":
        return filename_id(path), str(body.get("version", "")).strip()
    if kind == "adapter_manifest":
        return str(body.get("adapter_id", "")).strip(), "1.0.0"
    return str(body.get("id", "")).strip(), str(body.get("version", "")).strip()


def validate_workflow(path: Path, workflow: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    phases = workflow.get("phases")
    if not isinstance(phases, list):
        return errors

    phase_ids: list[str] = []
    orders: list[int] = []
    for phase in phases:
        if isinstance(phase, dict):
            if phase.get("id"):
                phase_ids.append(str(phase["id"]))
            if isinstance(phase.get("order"), int):
                orders.append(phase["order"])

    duplicates = sorted({item for item in phase_ids if phase_ids.count(item) > 1})
    if duplicates:
        errors.append(f"duplicate workflow phase ids: {', '.join(duplicates)}")
    if orders and sorted(orders) != list(range(1, len(phases) + 1)):
        errors.append(
            f"workflow phase order must be contiguous 1..{len(phases)}, got {sorted(orders)}"
        )

    known = set(phase_ids)
    for index, transition in enumerate(workflow.get("transitions") or []):
        if not isinstance(transition, dict):
            continue
        for field in ("from", "to"):
            value = transition.get(field)
            if value and value not in known:
                errors.append(
                    f"transitions[{index}].{field} references unknown phase '{value}'"
                )

    for index, entry in enumerate(workflow.get("skill_load_order") or []):
        if isinstance(entry, dict):
            phase = entry.get("phase")
            if phase and phase not in known:
                errors.append(
                    f"skill_load_order[{index}].phase references unknown phase '{phase}'"
                )

    if "required_phases" in workflow:
        errors.append("legacy required_phases field is prohibited; use phases")
    return errors


def validate_compatibility(
    path: Path,
    manifest: dict[str, Any],
    documents_by_path: dict[str, dict[str, Any]],
    root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    seen_sources: set[str] = set()
    aliases = manifest.get("aliases") or []
    for index, alias in enumerate(aliases):
        if not isinstance(alias, dict):
            continue
        source = str(alias.get("from_path", ""))
        target = str(alias.get("to_path", ""))
        contract_id = str(alias.get("contract_id", ""))
        contract_kind = str(alias.get("contract_kind", ""))
        pin = str(alias.get("version_constraint", ""))
        label = f"aliases[{index}]"

        if source in seen_sources:
            errors.append(f"{label}: duplicate legacy path '{source}'")
        seen_sources.add(source)
        if (root / source).exists():
            errors.append(f"{label}: legacy path still exists: {source}")

        target_doc = documents_by_path.get(target)
        if not target_doc:
            errors.append(f"{label}: canonical target does not exist: {target}")
            continue
        target_schema = target_doc.get("contract_schema") or {}
        if target_schema.get("kind") != contract_kind:
            errors.append(
                f"{label}: target kind '{target_schema.get('kind')}' does not match '{contract_kind}'"
            )
            continue
        root_key = KIND_TO_ROOT.get(contract_kind)
        target_body = target_doc.get(root_key, {}) if root_key else {}
        if target_body.get("id") != contract_id:
            errors.append(
                f"{label}: target id '{target_body.get('id')}' does not match '{contract_id}'"
            )
        try:
            compatible = pin_accepts(pin, str(target_body.get("version", "")))
        except ValueError as exc:
            errors.append(f"{label}: {exc}")
        else:
            if not compatible:
                errors.append(
                    f"{label}: version pin '{pin}' is incompatible with target version "
                    f"'{target_body.get('version')}'"
                )
    return errors


def flatten_manifest_entries(value: Any) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict) and "path" in item:
                entries.append(item)
            else:
                entries.extend(flatten_manifest_entries(item))
    elif isinstance(value, dict):
        for nested in value.values():
            entries.extend(flatten_manifest_entries(nested))
    return entries


def expected_manifest_entry(path: Path, document: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    schema_identity = document["contract_schema"]
    kind = str(schema_identity["kind"])
    body = document[KIND_TO_ROOT[kind]]
    contract_id, version = contract_identity(kind, body, path)
    return {
        "id": contract_id,
        "kind": kind,
        "schema_version": str(schema_identity["version"]),
        "schema_path": str(schema_identity["path"]),
        "path": path.relative_to(root).as_posix(),
        "version": version,
        "sha256": checksum(path),
    }


def validate_manifest(
    documents_by_path: dict[str, dict[str, Any]],
    *,
    root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "contracts" / "manifest.yaml"
    try:
        manifest = load_yaml(manifest_path)
        validator = validator_for(
            root / "schemas" / "contract-manifest.schema.yaml",
            schemas_root=root / "schemas",
        )
    except Exception as exc:
        return [f"contracts/manifest.yaml: invalid manifest/schema: {exc}"]

    for error in sorted(
        validator.iter_errors(manifest),
        key=lambda item: [str(part) for part in item.absolute_path],
    ):
        errors.append(f"contracts/manifest.yaml: {format_schema_error(error)}")

    entries = flatten_manifest_entries(manifest.get("contracts", {}))
    by_path: dict[str, dict[str, Any]] = {}
    for entry in entries:
        path = str(entry.get("path", ""))
        if path in by_path:
            errors.append(f"contracts/manifest.yaml: duplicate path entry '{path}'")
        by_path[path] = entry

    expected_paths = set(documents_by_path)
    actual_paths = set(by_path)
    for missing in sorted(expected_paths - actual_paths):
        errors.append(f"contracts/manifest.yaml: missing artifact '{missing}'")
    for stale in sorted(actual_paths - expected_paths):
        errors.append(f"contracts/manifest.yaml: stale artifact '{stale}'")

    for relative in sorted(expected_paths & actual_paths):
        path = root / relative
        expected = expected_manifest_entry(path, documents_by_path[relative], root)
        actual = by_path[relative]
        if actual != expected:
            errors.append(
                f"contracts/manifest.yaml: metadata drift for '{relative}': "
                f"expected {expected}, got {actual}"
            )

    if manifest.get("total_contracts") != len(expected_paths):
        errors.append(
            "contracts/manifest.yaml: total_contracts does not match active artifact count"
        )
    return errors


def validate_repository(root: Path = ROOT) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        schema_store(root / "schemas")
    except Exception as exc:
        return [f"schema registry is invalid: {exc}"], warnings

    documents_by_path: dict[str, dict[str, Any]] = {}
    identities: defaultdict[tuple[str, str], list[str]] = defaultdict(list)

    for path in artifact_paths(root):
        relative = path.relative_to(root).as_posix()
        try:
            document = load_yaml(path)
        except Exception as exc:
            errors.append(f"{relative}: invalid YAML: {exc}")
            continue
        documents_by_path[relative] = document

        schema_identity = document.get("contract_schema")
        if not isinstance(schema_identity, dict):
            errors.append(f"{relative}: missing contract_schema mapping")
            continue
        kind = str(schema_identity.get("kind", ""))
        declared_schema_path = str(schema_identity.get("path", ""))
        expected_schema_path = KIND_TO_SCHEMA.get(kind)
        if not expected_schema_path:
            errors.append(f"{relative}: unsupported schema kind '{kind}'")
            continue
        if declared_schema_path != expected_schema_path:
            errors.append(
                f"{relative}: schema path mismatch: kind '{kind}' requires "
                f"'{expected_schema_path}', got '{declared_schema_path}'"
            )

        expected_kind = expected_kind_for_path(path, root)
        if expected_kind != kind:
            errors.append(
                f"{relative}: path family requires '{expected_kind}', got '{kind}'"
            )

        schema_path = root / expected_schema_path
        try:
            validator = validator_for(schema_path, schemas_root=root / "schemas")
        except Exception as exc:
            errors.append(f"{relative}: invalid schema '{expected_schema_path}': {exc}")
            continue
        for error in sorted(
            validator.iter_errors(document),
            key=lambda item: [str(part) for part in item.absolute_path],
        ):
            errors.append(f"{relative}: {format_schema_error(error)}")

        root_key = KIND_TO_ROOT[kind]
        body = document.get(root_key)
        if not isinstance(body, dict):
            continue
        contract_id, version = contract_identity(kind, body, path)
        if not contract_id:
            errors.append(f"{relative}: missing contract identity")
            continue
        if not version:
            errors.append(f"{relative}: missing contract version")
        if contract_id != filename_id(path):
            errors.append(
                f"{relative}: filename/id mismatch: expected '{filename_id(path)}', got '{contract_id}'"
            )
        identities[(kind, contract_id)].append(relative)

        if kind == "skill_contract":
            if body.get("type") == "workflow":
                errors.append(
                    f"{relative}: lifecycle workflow must use workflow_contract in contracts/workflows"
                )
            if body.get("type") == "port":
                warnings.append(
                    f"{relative}: legacy type 'port' remains a compatibility source; first-class port is authoritative"
                )
        elif kind == "workflow_contract":
            errors.extend(f"{relative}: {item}" for item in validate_workflow(path, body))

    for (kind, contract_id), paths in sorted(identities.items()):
        if len(paths) > 1:
            errors.append(
                f"duplicate identity '{kind}:{contract_id}' owned by {', '.join(paths)}"
            )

    for relative, document in sorted(documents_by_path.items()):
        schema_identity = document.get("contract_schema") or {}
        if schema_identity.get("kind") == "compatibility_manifest":
            body = document.get("compatibility_manifest")
            if isinstance(body, dict):
                errors.extend(
                    f"{relative}: {item}"
                    for item in validate_compatibility(
                        root / relative, body, documents_by_path, root
                    )
                )

    errors.extend(validate_manifest(documents_by_path, root=root))
    return errors, warnings


def main() -> int:
    errors, warnings = validate_repository(ROOT)
    for warning in warnings:
        print(f"WARN — {warning}")
    if errors:
        print("Unified contract schema validation failed:\n")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} violation(s), {len(warnings)} warning(s).")
        return 1

    print(
        f"PASS — {len(artifact_paths(ROOT))} contract artifacts satisfy declared schemas, "
        f"family identity, workflow, compatibility, and manifest parity checks "
        f"({len(warnings)} migration warning(s))."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
