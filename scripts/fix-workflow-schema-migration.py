#!/usr/bin/env python3
"""Apply bounded workflow data corrections discovered by unified schema validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "contracts" / "workflows"


def load(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: document root must be a mapping")
    return payload


def write(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120))


def merge_unique(values: list[Any], additions: list[Any]) -> list[Any]:
    result = list(values)
    for value in additions:
        if value not in result:
            result.append(value)
    return result


def fix_product_development() -> None:
    path = WORKFLOWS / "product-development.contract.yaml"
    payload = load(path)
    workflow = payload.get("workflow_contract")
    if not isinstance(workflow, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: missing workflow_contract")

    load_order = workflow.get("skill_load_order")
    if not isinstance(load_order, list):
        raise ValueError(f"{path.relative_to(ROOT)}: skill_load_order must be a list")

    target: dict[str, Any] | None = None
    orphan: dict[str, Any] | None = None
    retained: list[Any] = []
    for entry in load_order:
        if isinstance(entry, dict) and entry.get("phase") == "acceptance_verification":
            target = entry
            retained.append(entry)
        elif isinstance(entry, dict) and entry.get("phase") == "acceptance_domain_review":
            orphan = entry
        else:
            retained.append(entry)

    if target is None:
        raise ValueError("product-development: acceptance_verification load entry is missing")
    if orphan is not None:
        target_load = target.get("load")
        orphan_load = orphan.get("load")
        if not isinstance(target_load, list) or not isinstance(orphan_load, list):
            raise ValueError("product-development: acceptance load entries must use lists")
        target["load"] = merge_unique(target_load, orphan_load)
        workflow["skill_load_order"] = retained

    phase_ids = {
        str(phase.get("id"))
        for phase in workflow.get("phases", [])
        if isinstance(phase, dict) and phase.get("id")
    }
    unresolved = [
        entry.get("phase")
        for entry in workflow["skill_load_order"]
        if isinstance(entry, dict) and entry.get("phase") not in phase_ids
    ]
    if unresolved:
        raise ValueError(f"product-development: unresolved phase load entries: {unresolved}")

    write(path, payload)


def fix_redesign_workflow() -> None:
    path = WORKFLOWS / "redesign-workflow.contract.yaml"
    payload = load(path)
    workflow = payload.get("workflow_contract")
    if not isinstance(workflow, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: missing workflow_contract")

    workflow.setdefault(
        "adapter_requirements",
        {
            "must_preserve_declared_lifecycle_and_phase_ids": True,
            "must_preserve_single_design_owner_and_repository_write_owner": True,
            "must_support_expected_head_write_lease_and_drift_detection": True,
            "must_preserve_scope_diff_concurrency_and_verification_evidence": True,
            "must_route_review_through_design_review_facade": True,
            "must_not_claim_pass_when_blocked_or_not_verified": True,
        },
    )
    write(path, payload)


def main() -> int:
    fix_product_development()
    fix_redesign_workflow()
    print("Applied bounded workflow schema migration corrections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
