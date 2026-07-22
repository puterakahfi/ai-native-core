#!/usr/bin/env python3
"""Resolve canonical and legacy Native AI contract references."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

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


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: document root must be a mapping")
    return payload


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


def manifest_index(core_root: Path) -> dict[str, dict[str, Any]]:
    manifest = load_yaml(core_root / "contracts" / "manifest.yaml")
    return {
        str(entry["path"]): entry
        for entry in flatten_manifest_entries(manifest.get("contracts", {}))
        if entry.get("path")
    }


def path_alias_index(core_root: Path) -> dict[str, dict[str, Any]]:
    aliases: dict[str, dict[str, Any]] = {}
    compatibility_root = core_root / "contracts" / "compatibility"
    if not compatibility_root.exists():
        return aliases

    for path in sorted(compatibility_root.glob("*.contract.yaml")):
        document = load_yaml(path)
        schema_identity = document.get("contract_schema") or {}
        if schema_identity.get("kind") != "compatibility_manifest":
            continue
        body = document.get("compatibility_manifest") or {}
        for alias in body.get("aliases") or []:
            if not isinstance(alias, dict):
                continue
            source = str(alias.get("from_path", "")).strip()
            if source:
                aliases[source] = {**alias, "manifest_path": path}
    return aliases


def normalize_reference(reference: str) -> str:
    normalized = reference.strip()
    prefix = "ai-native-core/"
    if normalized.startswith(prefix):
        normalized = normalized[len(prefix) :]
    return normalized.lstrip("./")


def resolve_contract_reference(
    core_root: Path,
    reference: str,
) -> dict[str, Any] | None:
    declared = normalize_reference(reference)
    manifest = manifest_index(core_root)
    aliases = path_alias_index(core_root)

    canonical = declared
    alias = aliases.get(declared)
    if alias:
        if alias.get("status") == "retired":
            return None
        canonical = str(alias.get("to_path", "")).strip()

    entry = manifest.get(canonical)
    path = core_root / canonical
    if not entry or not path.is_file():
        return None

    return {
        "declared_path": declared,
        "canonical_path": canonical,
        "path": path,
        "entry": entry,
        "alias": alias,
    }


def load_contract_document(path: Path) -> tuple[str, dict[str, Any], dict[str, Any]]:
    document = load_yaml(path)
    schema_identity = document.get("contract_schema")
    if not isinstance(schema_identity, dict):
        raise ValueError(f"{path}: missing contract_schema mapping")
    kind = str(schema_identity.get("kind", "")).strip()
    root_key = KIND_TO_ROOT.get(kind)
    if not root_key:
        raise ValueError(f"{path}: unsupported contract kind '{kind}'")
    body = document.get(root_key)
    if not isinstance(body, dict):
        raise ValueError(f"{path}: missing {root_key} mapping")
    return kind, body, document


def parse_version(value: str) -> tuple[int, int, int]:
    core = value.split("-", 1)[0]
    parts = core.split(".")
    if len(parts) not in (2, 3) or not all(part.isdigit() for part in parts):
        raise ValueError(f"invalid semantic version '{value}'")
    return int(parts[0]), int(parts[1]), int(parts[2]) if len(parts) == 3 else 0


def pin_accepts(pin: str, version: str) -> bool:
    cleaned = pin.strip().strip('"').strip("'")
    prefix = cleaned[0] if cleaned and cleaned[0] in "^~" else ""
    requested = parse_version(cleaned[1:] if prefix else cleaned)
    actual = parse_version(version.strip().strip('"').strip("'"))
    if prefix == "":
        return actual == requested
    if actual < requested:
        return False
    if prefix == "~":
        return actual[:2] == requested[:2]
    if requested[0] == 0:
        return actual[0] == 0 and actual[1] == requested[1]
    return actual[0] == requested[0]
