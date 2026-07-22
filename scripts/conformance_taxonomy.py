#!/usr/bin/env python3
"""Executable taxonomy checks layered on structured conformance results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

import yaml


def _strings(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except Exception:
            try:
                parsed = yaml.safe_load(value)
            except Exception:
                parsed = value
        if isinstance(parsed, list):
            return [str(item) for item in parsed if str(item).strip()]
        if parsed is not None and str(parsed).strip():
            return [str(parsed)]
    return []


def _metadata(skill: dict[str, Any]) -> dict[str, Any]:
    value = skill.get("frontmatter", {}).get("metadata") or {}
    return value if isinstance(value, dict) else {}


def _legacy_patterns(metadata: dict[str, Any], *, contract_backed: bool) -> list[str]:
    patterns: list[str] = []
    if contract_backed:
        patterns.append("skill-adapter")
    patterns.extend(_strings(metadata.get("ai-native-skills.pattern")))
    result: list[str] = []
    for pattern in patterns:
        normalized = pattern.strip().lower().replace("_", "-")
        if normalized and normalized not in result:
            result.append(normalized)
    return result


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
        result.setdefault("adapter_patterns", [])

        try:
            declaration = engine.load_yaml(declaration_path)["adapter_conformance"]
            adapter = declaration["adapter"]
        except Exception:
            return result

        skill = engine.parse_skill(skill_path)
        metadata = _metadata(skill)
        declared_kind = str(adapter.get("kind", ""))
        declared_patterns = [str(item) for item in adapter.get("patterns") or []]
        expected_kind = str(metadata.get("ai-native-skills.type", "")).strip()
        expected_patterns = _legacy_patterns(metadata, contract_backed=True)

        if expected_kind and declared_kind != expected_kind:
            result["findings"].append(
                engine.issue(
                    "ADAPTER_KIND_MISMATCH",
                    "ERROR",
                    "adapter_identity",
                    "declaration adapter kind does not match executable metadata type",
                    [expected_kind],
                    [declared_kind],
                )
            )

        missing_patterns = [
            pattern for pattern in expected_patterns if pattern not in declared_patterns
        ]
        if missing_patterns:
            result["findings"].append(
                engine.issue(
                    "ADAPTER_PATTERN_MISSING",
                    "PARTIAL",
                    "adapter_identity",
                    "declaration does not preserve executable adapter patterns",
                    expected_patterns,
                    declared_patterns,
                )
            )

        result["adapter_kind"] = declared_kind
        result["adapter_patterns"] = declared_patterns
        result["structural_status"] = engine.status(result["findings"])
        return result

    return validate


def enhance_legacy(
    engine: Any,
    base: Callable[[Path, Path, Path], dict[str, Any] | None],
) -> Callable[[Path, Path, Path], dict[str, Any] | None]:
    def validate(
        core: Path,
        adapters: Path,
        skill_path: Path,
    ) -> dict[str, Any] | None:
        result = base(core, adapters, skill_path)
        if result is None:
            return None
        skill = engine.parse_skill(skill_path)
        metadata = _metadata(skill)
        result["adapter_kind"] = str(
            metadata.get("ai-native-skills.type", result.get("adapter_kind", "unknown"))
        )
        result["adapter_patterns"] = _legacy_patterns(
            metadata,
            contract_backed=True,
        )
        return result

    return validate
