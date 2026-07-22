#!/usr/bin/env python3
"""One-time controlled materialization for issue #8 schema v1 migration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"
SCHEMAS = ROOT / "schemas"

SCHEMA_META = {
    "skill_contract": "schemas/skill-contract.schema.yaml",
    "workflow_contract": "schemas/workflow-contract.schema.yaml",
    "runtime_contract": "schemas/runtime-contract.schema.yaml",
    "port_contract": "schemas/port-contract.schema.yaml",
    "behavioral_test_contract": "schemas/behavioral-test-contract.schema.yaml",
    "compatibility_manifest": "schemas/compatibility-manifest.schema.yaml",
}

WORKFLOW_KIND = {
    "bugfix": "engineering_lifecycle",
    "code-review": "review_lifecycle",
    "deployment": "deployment_lifecycle",
    "new-feature": "engineering_lifecycle",
    "product-development": "product_lifecycle",
    "spec-driven": "engineering_lifecycle",
    "design-refinement": "quality_lifecycle",
    "redesign-workflow": "quality_lifecycle",
    "skill-evolution": "learning_lifecycle",
    "development-loop": "execution_method",
}

MOVED = {
    "design-refinement": (
        CONTRACTS / "skills" / "quality" / "design-refinement.contract.yaml",
        CONTRACTS / "workflows" / "design-refinement.contract.yaml",
        "skill_contract",
    ),
    "redesign-workflow": (
        CONTRACTS / "skills" / "quality" / "redesign-workflow.contract.yaml",
        CONTRACTS / "workflows" / "redesign-workflow.contract.yaml",
        "skill_contract",
    ),
    "skill-evolution": (
        CONTRACTS / "skills" / "quality" / "skill-evolution.contract.yaml",
        CONTRACTS / "workflows" / "skill-evolution.contract.yaml",
        "skill_contract",
    ),
    "development-loop": (
        CONTRACTS / "runtime" / "development-loop.contract.yaml",
        CONTRACTS / "workflows" / "development-loop.contract.yaml",
        "runtime_contract",
    ),
}


def load(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: root must be a mapping")
    return payload


def write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120))


def header(kind: str) -> dict[str, str]:
    return {
        "kind": kind,
        "version": "1.0.0",
        "path": SCHEMA_META[kind],
    }


def prepend_header(path: Path, kind: str) -> None:
    text = path.read_text()
    if text.startswith("contract_schema:"):
        return
    rendered = yaml.safe_dump(
        {"contract_schema": header(kind)}, sort_keys=False, allow_unicode=True
    )
    path.write_text(rendered + text)


def normalize_phase_list(phases: list[Any]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, raw in enumerate(phases, start=1):
        if not isinstance(raw, dict):
            raise ValueError("workflow phase must be a mapping")
        phase = dict(raw)
        phase.setdefault("order", index)
        result.append(phase)
    return result


def normalize_redesign_phases(raw: Any) -> list[dict[str, Any]]:
    if not isinstance(raw, dict):
        raise ValueError("redesign phases must be a mapping")
    required = raw.get("required", [])
    definitions = raw.get("definitions", {})
    if not isinstance(required, list) or not isinstance(definitions, dict):
        raise ValueError("redesign phases require ordered ids and definitions")

    phases: list[dict[str, Any]] = []
    for order, phase_id in enumerate(required, start=1):
        phase_id = str(phase_id)
        definition = definitions.get(phase_id, {})
        if not isinstance(definition, dict):
            raise ValueError(f"phase definition must be a mapping: {phase_id}")
        phase: dict[str, Any] = {"id": phase_id, "order": order}
        phase.update(definition)
        if "produces" in phase and "outputs" not in phase:
            phase["outputs"] = phase.pop("produces")
        phases.append(phase)
    return phases


def workflow_document(body: dict[str, Any], contract_id: str) -> dict[str, Any]:
    workflow = dict(body)
    workflow["type"] = "workflow"
    workflow.setdefault("category", "quality")
    workflow["workflow_kind"] = WORKFLOW_KIND[contract_id]

    if "required_phases" in workflow:
        workflow["phases"] = normalize_phase_list(workflow.pop("required_phases"))
    elif contract_id == "redesign-workflow":
        workflow["phases"] = normalize_redesign_phases(workflow.get("phases"))
    else:
        phases = workflow.get("phases")
        if isinstance(phases, list):
            workflow["phases"] = normalize_phase_list(phases)
        else:
            raise ValueError(f"{contract_id}: workflow phases are missing")

    if not workflow.get("purpose"):
        description = workflow.get("description")
        if not description:
            raise ValueError(f"{contract_id}: workflow purpose is missing")
        workflow["purpose"] = description

    workflow.setdefault("skill_load_order", [])
    return {
        "contract_schema": header("workflow_contract"),
        "workflow_contract": workflow,
    }


def migrate_existing_workflows() -> None:
    for path in sorted((CONTRACTS / "workflows").glob("*.contract.yaml")):
        payload = load(path)
        body = payload.get("workflow_contract")
        if not isinstance(body, dict):
            raise ValueError(f"{path.relative_to(ROOT)}: missing workflow_contract")
        contract_id = str(body.get("id", ""))
        if contract_id not in WORKFLOW_KIND:
            raise ValueError(f"{path.relative_to(ROOT)}: workflow_kind decision missing")
        write(path, workflow_document(body, contract_id))


def migrate_moved_workflows() -> None:
    for contract_id, (source, target, root_key) in MOVED.items():
        if target.exists() and not source.exists():
            continue
        payload = load(source)
        body = payload.get(root_key)
        if not isinstance(body, dict):
            raise ValueError(f"{source.relative_to(ROOT)}: missing {root_key}")
        document = workflow_document(body, contract_id)
        if contract_id == "development-loop":
            document["workflow_contract"]["category"] = "runtime"
        write(target, document)
        source.unlink()


def add_headers_to_remaining_contracts() -> None:
    for path in sorted((CONTRACTS / "skills").rglob("*.contract.yaml")):
        prepend_header(path, "skill_contract")
    for path in sorted((CONTRACTS / "workflows").glob("*.contract.yaml")):
        prepend_header(path, "workflow_contract")
    for path in sorted((CONTRACTS / "runtime").glob("*.contract.yaml")):
        prepend_header(path, "runtime_contract")
    for path in sorted((CONTRACTS / "ports").rglob("*.port.yaml")):
        prepend_header(path, "port_contract")
    for path in sorted((CONTRACTS / "tests").glob("*.test.yaml")):
        prepend_header(path, "behavioral_test_contract")


def upgrade_port_schema() -> None:
    path = SCHEMAS / "port-contract.schema.yaml"
    schema = load(path)
    if schema.get("$id") == "https://native-ai.engineering/schemas/port-contract.schema.yaml":
        return

    schema["$id"] = "https://native-ai.engineering/schemas/port-contract.schema.yaml"
    required = list(schema.get("required", []))
    if "contract_schema" not in required:
        required.insert(0, "contract_schema")
    schema["required"] = required

    properties = dict(schema.get("properties", {}))
    properties = {
        "contract_schema": {
            "allOf": [
                {
                    "$ref": "https://native-ai.engineering/schemas/common.schema.yaml#/$defs/contract_schema_identity"
                },
                {
                    "type": "object",
                    "properties": {
                        "kind": {"const": "port_contract"},
                        "version": {"const": "1.0.0"},
                        "path": {"const": "schemas/port-contract.schema.yaml"},
                    },
                },
            ]
        },
        **properties,
    }
    schema["properties"] = properties
    write(path, schema)


def create_compatibility_manifest() -> None:
    path = CONTRACTS / "compatibility" / "contract-path-aliases.contract.yaml"
    aliases = []
    for contract_id, (source, target, _root_key) in MOVED.items():
        version = load(target)["workflow_contract"]["version"]
        aliases.append(
            {
                "from_path": source.relative_to(ROOT).as_posix(),
                "to_path": target.relative_to(ROOT).as_posix(),
                "contract_id": contract_id,
                "contract_kind": "workflow_contract",
                "version_constraint": f"^{version}",
                "status": "active",
                "rationale": "Canonical workflow root and location migration under issue #8.",
            }
        )
    payload = {
        "contract_schema": header("compatibility_manifest"),
        "compatibility_manifest": {
            "id": "contract-path-aliases",
            "version": "1.0.0",
            "aliases": aliases,
            "evidence_boundary": [
                "path_alias_preserves_resolution_not_behavioral_conformance",
                "canonical_target_remains_the_only_machine_authority",
                "downstream_consumers_still_require_explicit_migration",
            ],
        },
    }
    write(path, payload)


def main() -> int:
    migrate_existing_workflows()
    migrate_moved_workflows()
    add_headers_to_remaining_contracts()
    upgrade_port_schema()
    create_compatibility_manifest()
    print("Materialized contract schema v1 envelope and workflow migration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
