#!/usr/bin/env python3
"""Semantic corrections layered over the core structured validator engine."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable


def enhance_structured(
    engine: Any,
    base: Callable[[Path, Path, Path, Path], dict[str, Any]],
) -> Callable[[Path, Path, Path, Path], dict[str, Any]]:
    def validate(
        core: Path,
        adapters: Path,
        skill_path: Path,
        declaration_path: Path,
    ) -> dict[str, Any]:
        result = base(core, adapters, skill_path, declaration_path)
        contract_ref = result.get("contract")
        schema_failed = any(
            finding.get("code")
            in {"DECLARATION_YAML_INVALID", "DECLARATION_SCHEMA_INVALID"}
            for finding in result.get("findings", [])
        )
        if schema_failed or not isinstance(contract_ref, dict):
            return result

        try:
            declaration = engine.load_yaml(declaration_path)["adapter_conformance"]
            contract_path = core / contract_ref["canonical_path"]
            kind, body, _document = engine.load_contract_document(contract_path)
            contract = engine.interface(kind, body)
        except Exception:
            return result

        declared_outputs = declaration["interface"]["outputs"]
        required_outputs = contract["required_outputs"]
        allowed_outputs = engine.unique(required_outputs + contract["allowed_outputs"])

        findings = [
            finding
            for finding in result.get("findings", [])
            if finding.get("code") != "OUTPUT_COVERAGE_MISSING"
        ]

        required_map = engine.maps(required_outputs)
        declared_map = engine.maps(declared_outputs)
        missing_required = sorted(set(required_map) - set(declared_map))
        if missing_required:
            findings.append(
                engine.issue(
                    "REQUIRED_OUTPUT_MISSING",
                    "PARTIAL",
                    "outputs",
                    "adapter declaration is missing required contract outputs",
                    [required_map[key] for key in missing_required],
                    declared_outputs,
                )
            )

        allowed_only = set(engine.maps(allowed_outputs)) - set(required_map)
        filtered: list[dict[str, Any]] = []
        for finding in findings:
            if finding.get("code") != "REQUIRED_CLAIM_UNSUPPORTED":
                filtered.append(finding)
                continue
            actual = {
                engine.norm(value)
                for value in finding.get("actual", [])
                if engine.norm(value)
            }
            if actual and actual.issubset(allowed_only):
                continue
            filtered.append(finding)

        result["findings"] = filtered
        result["structural_status"] = engine.status(filtered)
        return result

    return validate
