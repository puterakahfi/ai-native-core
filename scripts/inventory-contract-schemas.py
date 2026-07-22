#!/usr/bin/env python3
"""Inventory Native AI contract and manifest shapes without changing semantics."""

from __future__ import annotations

import argparse
import collections
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_ROOT = ROOT / "contracts"
MANIFEST_PATH = CONTRACTS_ROOT / "manifest.yaml"
DEFAULT_OUTPUT = ROOT / "docs" / "contract-schema-discovery.yaml"

EXPECTED_ROOT_BY_FAMILY = {
    "skill": "skill_contract",
    "workflow": "workflow_contract",
    "runtime": "runtime_contract",
    "port": "port_contract",
    "behavioral_test": "skill_test",
}

COMMON_FIELDS_BY_FAMILY = {
    "skill": [
        "id",
        "category",
        "type",
        "version",
        "capability",
        "roles",
        "inputs",
        "outputs",
        "quality_gates",
        "adapter_requirements",
    ],
    "workflow": [
        "id",
        "type",
        "version",
        "category",
        "purpose",
        "required_phases",
        "skill_load_order",
        "quality_gates",
        "adapter_requirements",
    ],
    "runtime": [
        "id",
        "version",
        "purpose",
        "description",
        "quality_gates",
        "adapter_requirements",
    ],
    "port": [
        "id",
        "kind",
        "version",
        "capability",
        "direction",
        "boundary",
        "interactions",
        "failures",
        "authorization",
        "adapter_requirements",
        "compatibility",
        "quality_gates",
    ],
    "behavioral_test": ["skill", "version", "description", "cases"],
}

TARGET_EXTENSION_KEYS = {
    "adapter_requirements",
    "aliases",
    "approval",
    "approvals",
    "compatibility",
    "concurrency",
    "delegation",
    "dependencies",
    "evidence",
    "facade",
    "gates",
    "handoffs",
    "lifecycle",
    "scope_diff",
    "state_transitions",
    "transitions",
}

LIFECYCLE_MARKERS = {
    "phases",
    "required_phases",
    "phase_order",
    "transitions",
    "state_transitions",
    "handoffs",
    "exit_conditions",
    "lifecycle",
    "steps",
}


def contract_paths() -> list[Path]:
    paths: list[Path] = []
    for path in CONTRACTS_ROOT.rglob("*.yaml"):
        if path.name == "manifest.yaml":
            continue
        if path.name.endswith((".contract.yaml", ".port.yaml", ".test.yaml")):
            paths.append(path)
    return sorted(paths)


def family_for(path: Path) -> str:
    rel = path.relative_to(CONTRACTS_ROOT)
    first = rel.parts[0]
    return {
        "skills": "skill",
        "workflows": "workflow",
        "runtime": "runtime",
        "ports": "port",
        "tests": "behavioral_test",
    }.get(first, "unclassified")


def expected_id(path: Path) -> str:
    for suffix in (".contract.yaml", ".port.yaml", ".test.yaml"):
        if path.name.endswith(suffix):
            return path.name[: -len(suffix)]
    return path.stem


def node_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, dict):
        return "mapping"
    if isinstance(value, list):
        return "sequence"
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    return type(value).__name__


def collect_key_paths(value: Any, *, prefix: str = "") -> Iterable[str]:
    if isinstance(value, dict):
        for key, nested in value.items():
            key_text = str(key)
            path = f"{prefix}.{key_text}" if prefix else key_text
            if key_text in TARGET_EXTENSION_KEYS:
                yield path
            yield from collect_key_paths(nested, prefix=path)
    elif isinstance(value, list):
        for nested in value:
            yield from collect_key_paths(nested, prefix=f"{prefix}[]")


def ordered_counts(counter: collections.Counter[str]) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def normalize_scalar(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def root_candidates(payload: dict[str, Any]) -> list[str]:
    return sorted(
        str(key)
        for key in payload
        if str(key).endswith(("_contract", "_test"))
    )


def nested_shape(value: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"value_type": node_type(value)}
    if isinstance(value, dict):
        result["mapping_keys"] = sorted(str(key) for key in value)
    elif isinstance(value, list):
        item_types = collections.Counter(node_type(item) for item in value)
        result["item_type_counts"] = ordered_counts(item_types)
        item_keys: collections.Counter[str] = collections.Counter()
        mapping_items = 0
        for item in value:
            if isinstance(item, dict):
                mapping_items += 1
                item_keys.update(str(key) for key in item)
        if mapping_items:
            result["mapping_item_count"] = mapping_items
            result["mapping_item_field_counts"] = ordered_counts(item_keys)
    return result


def inspect_contract(path: Path) -> dict[str, Any]:
    rel = path.relative_to(ROOT).as_posix()
    family = family_for(path)
    record: dict[str, Any] = {
        "path": rel,
        "path_family": family,
        "expected_id": expected_id(path),
    }

    try:
        payload = yaml.safe_load(path.read_text())
    except Exception as exc:  # pragma: no cover - repository discovery path
        record.update({"parse_status": "invalid_yaml", "parse_error": str(exc)})
        return record

    if not isinstance(payload, dict):
        record.update(
            {
                "parse_status": "non_mapping_root",
                "document_type": type(payload).__name__,
            }
        )
        return record

    root_keys = sorted(str(key) for key in payload)
    record["document_root_keys"] = root_keys
    candidates = root_candidates(payload)

    if len(candidates) == 1 and isinstance(payload[candidates[0]], dict):
        root_key = candidates[0]
        contract = payload[root_key]
        identifier_field = "skill" if root_key == "skill_test" else "id"
        record["parse_status"] = "parsed"
        record["contract_root"] = root_key
        record["identifier_field"] = identifier_field
        record["contract_id"] = normalize_scalar(contract.get(identifier_field))
        record["contract_version"] = normalize_scalar(contract.get("version"))
        record["declared_type"] = normalize_scalar(contract.get("type"))
        record["declared_kind"] = normalize_scalar(contract.get("kind"))
        record["root_fields"] = sorted(str(key) for key in contract)
        record["root_field_shapes"] = {
            str(key): nested_shape(value) for key, value in sorted(contract.items())
        }
        record["extension_key_paths"] = sorted(set(collect_key_paths(contract)))
    else:
        record["parse_status"] = "ambiguous_contract_root"
        record["candidate_contract_roots"] = candidates

    expected_root = EXPECTED_ROOT_BY_FAMILY.get(family)
    if expected_root:
        record["expected_contract_root"] = expected_root
        record["root_matches_path_family"] = record.get("contract_root") == expected_root

    return record


def manifest_entries() -> list[dict[str, Any]]:
    payload = yaml.safe_load(MANIFEST_PATH.read_text())
    contracts = payload.get("contracts", {}) if isinstance(payload, dict) else {}
    entries: list[dict[str, Any]] = []

    def visit(value: Any, family_path: list[str]) -> None:
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and "path" in item:
                    entries.append(
                        {
                            "family_path": "/".join(family_path),
                            "metadata_fields": sorted(str(key) for key in item),
                            **{str(key): normalize_scalar(val) for key, val in item.items()},
                        }
                    )
                else:
                    visit(item, family_path)
        elif isinstance(value, dict):
            for key, nested in sorted(value.items()):
                visit(nested, [*family_path, str(key)])

    visit(contracts, [])
    return sorted(entries, key=lambda item: str(item.get("path", "")))


def summarize_manifest(entries: list[dict[str, Any]]) -> dict[str, Any]:
    field_counts: collections.Counter[str] = collections.Counter()
    family_counts: collections.Counter[str] = collections.Counter()
    missing_kind: list[str] = []
    missing_schema_version: list[str] = []
    missing_contract_version: list[str] = []

    for entry in entries:
        field_counts.update(entry.get("metadata_fields", []))
        family_counts[str(entry.get("family_path", ""))] += 1
        path = str(entry.get("path", ""))
        if not entry.get("kind"):
            missing_kind.append(path)
        if not entry.get("schema_version"):
            missing_schema_version.append(path)
        if not entry.get("version"):
            missing_contract_version.append(path)

    return {
        "entry_count": len(entries),
        "family_path_counts": ordered_counts(family_counts),
        "metadata_field_coverage": {
            field: {
                "count": count,
                "coverage": round(count / len(entries), 4) if entries else 0.0,
            }
            for field, count in sorted(field_counts.items())
        },
        "missing_kind_paths": missing_kind,
        "missing_schema_version_paths": missing_schema_version,
        "missing_contract_version_paths": missing_contract_version,
        "entries": entries,
    }


def build_report(records: list[dict[str, Any]]) -> dict[str, Any]:
    path_family_counts: collections.Counter[str] = collections.Counter()
    root_counts: collections.Counter[str] = collections.Counter()
    parse_counts: collections.Counter[str] = collections.Counter()
    declared_type_counts: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    declared_kind_counts: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    root_field_counts: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    root_field_type_counts: dict[
        str, dict[str, collections.Counter[str]]
    ] = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    extension_path_counts: collections.Counter[str] = collections.Counter()
    ids_by_family: dict[str, dict[str, list[str]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    ids_global: dict[str, list[dict[str, str]]] = collections.defaultdict(list)

    anomalies: dict[str, list[Any]] = {
        "invalid_or_ambiguous_documents": [],
        "path_root_mismatches": [],
        "missing_contract_ids": [],
        "missing_contract_versions": [],
        "filename_id_mismatches": [],
        "duplicate_ids_within_family": [],
        "cross_family_id_collisions": [],
    }

    field_presence_gaps: dict[str, dict[str, list[str]]] = {
        family: {field: [] for field in fields}
        for family, fields in COMMON_FIELDS_BY_FAMILY.items()
    }

    workflow_contracts: list[str] = []
    declared_skill_workflows: list[dict[str, Any]] = []
    skill_internal_phase_procedures: list[dict[str, Any]] = []
    runtime_lifecycle_candidates: list[dict[str, Any]] = []

    for record in records:
        family = record["path_family"]
        path_family_counts[family] += 1
        parse_status = record.get("parse_status", "unknown")
        parse_counts[parse_status] += 1

        root = record.get("contract_root")
        if root:
            root_counts[root] += 1
            for field in record.get("root_fields", []):
                root_field_counts[root][field] += 1
                value_type = record.get("root_field_shapes", {}).get(field, {}).get("value_type")
                if value_type:
                    root_field_type_counts[root][field][str(value_type)] += 1
            for extension_path in record.get("extension_key_paths", []):
                extension_path_counts[extension_path] += 1

            declared_type = record.get("declared_type")
            if declared_type is not None:
                declared_type_counts[root][str(declared_type)] += 1
            declared_kind = record.get("declared_kind")
            if declared_kind is not None:
                declared_kind_counts[root][str(declared_kind)] += 1

        if parse_status != "parsed":
            anomalies["invalid_or_ambiguous_documents"].append(
                {
                    "path": record["path"],
                    "status": parse_status,
                    "detail": record.get("parse_error")
                    or record.get("candidate_contract_roots")
                    or record.get("document_type"),
                }
            )
            continue

        fields = set(record.get("root_fields", []))
        for field in COMMON_FIELDS_BY_FAMILY.get(family, []):
            if field not in fields:
                field_presence_gaps[family][field].append(record["path"])

        if record.get("expected_contract_root") and not record.get("root_matches_path_family"):
            anomalies["path_root_mismatches"].append(
                {
                    "path": record["path"],
                    "expected": record["expected_contract_root"],
                    "actual": root,
                }
            )

        contract_id = record.get("contract_id")
        if not contract_id:
            anomalies["missing_contract_ids"].append(record["path"])
        else:
            contract_id_text = str(contract_id)
            ids_by_family[family][contract_id_text].append(record["path"])
            ids_global[contract_id_text].append({"family": family, "path": record["path"]})
            if contract_id_text != record["expected_id"]:
                anomalies["filename_id_mismatches"].append(
                    {
                        "path": record["path"],
                        "expected": record["expected_id"],
                        "actual": contract_id_text,
                    }
                )

        if not record.get("contract_version"):
            anomalies["missing_contract_versions"].append(record["path"])

        lifecycle_fields = sorted(fields & LIFECYCLE_MARKERS)
        if family == "workflow" and root == "workflow_contract":
            workflow_contracts.append(record["path"])
        elif family == "skill" and root == "skill_contract":
            candidate = {
                "path": record["path"],
                "contract_id": contract_id,
                "contract_version": record.get("contract_version"),
                "lifecycle_fields": lifecycle_fields,
            }
            if record.get("declared_type") == "workflow":
                declared_skill_workflows.append(candidate)
            elif lifecycle_fields:
                skill_internal_phase_procedures.append(candidate)
        elif family == "runtime" and lifecycle_fields:
            runtime_lifecycle_candidates.append(
                {
                    "path": record["path"],
                    "contract_id": contract_id,
                    "contract_version": record.get("contract_version"),
                    "lifecycle_fields": lifecycle_fields,
                }
            )

    for family, ids in sorted(ids_by_family.items()):
        for contract_id, paths in sorted(ids.items()):
            if len(paths) > 1:
                anomalies["duplicate_ids_within_family"].append(
                    {"family": family, "contract_id": contract_id, "paths": sorted(paths)}
                )

    for contract_id, occurrences in sorted(ids_global.items()):
        families = {item["family"] for item in occurrences}
        if len(families) > 1:
            anomalies["cross_family_id_collisions"].append(
                {"contract_id": contract_id, "occurrences": occurrences}
            )

    root_shapes: dict[str, Any] = {}
    for root, count in sorted(root_counts.items()):
        root_shapes[root] = {
            "artifact_count": count,
            "field_coverage": {
                field: {
                    "count": field_count,
                    "coverage": round(field_count / count, 4),
                    "value_type_counts": ordered_counts(root_field_type_counts[root][field]),
                }
                for field, field_count in sorted(root_field_counts[root].items())
            },
            "declared_type_values": ordered_counts(declared_type_counts[root]),
            "declared_kind_values": ordered_counts(declared_kind_counts[root]),
        }

    manifest = summarize_manifest(manifest_entries())

    return {
        "contract_schema_discovery": {
            "version": "0.2.0",
            "source_root": "contracts",
            "artifact_count": len(records),
            "path_family_counts": ordered_counts(path_family_counts),
            "parse_status_counts": ordered_counts(parse_counts),
            "contract_root_counts": ordered_counts(root_counts),
            "root_shapes": root_shapes,
            "field_presence_gaps": field_presence_gaps,
            "extension_key_path_counts": ordered_counts(extension_path_counts),
            "workflow_representation_inventory": {
                "canonical_workflow_contract_paths": sorted(workflow_contracts),
                "declared_skill_workflow_candidates": sorted(
                    declared_skill_workflows, key=lambda item: item["path"]
                ),
                "skill_internal_phase_procedures": sorted(
                    skill_internal_phase_procedures, key=lambda item: item["path"]
                ),
                "runtime_lifecycle_candidates": sorted(
                    runtime_lifecycle_candidates, key=lambda item: item["path"]
                ),
            },
            "manifest_inventory": manifest,
            "anomalies": anomalies,
            "artifacts": records,
            "evidence_boundary": [
                "inventory proves observed YAML shape only",
                "field presence does not establish that a field is universally required",
                "declared type does not prove executable behavior",
                "lifecycle markers do not automatically make an expert procedure a workflow",
                "workflow candidacy requires reviewed ownership and migration decisions",
                "schema validity will not prove adapter conformance or product acceptance",
            ],
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    records = [inspect_contract(path) for path in contract_paths()]
    report = build_report(records)
    rendered = yaml.safe_dump(report, sort_keys=False, allow_unicode=True, width=120)

    output = args.output if args.output.is_absolute() else ROOT / args.output
    if args.check:
        if not output.exists() or output.read_text() != rendered:
            print(f"FAIL — schema discovery report is stale: {output.relative_to(ROOT)}")
            return 1
        print(f"PASS — schema discovery report is current ({len(records)} artifacts).")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered)
    print(f"Generated {output.relative_to(ROOT)} ({len(records)} artifacts).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
