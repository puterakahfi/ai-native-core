#!/usr/bin/env python3
"""Shared JSON Schema loading utilities for Native AI contract validators."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_ROOT = ROOT / "schemas"


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError("document root must be a mapping")
    return payload


def schema_store(schemas_root: Path = SCHEMAS_ROOT) -> dict[str, dict[str, Any]]:
    effective_root = schemas_root if schemas_root.exists() else SCHEMAS_ROOT
    store: dict[str, dict[str, Any]] = {}
    for path in sorted(effective_root.glob("*.schema.yaml")):
        schema = load_yaml(path)
        Draft202012Validator.check_schema(schema)
        schema_id = schema.get("$id")
        if schema_id:
            store[str(schema_id)] = schema
    return store


def validator_for(
    schema_path: Path,
    *,
    schemas_root: Path = SCHEMAS_ROOT,
) -> Draft202012Validator:
    schema = load_yaml(schema_path)
    Draft202012Validator.check_schema(schema)
    store = schema_store(schemas_root)
    resolver = RefResolver.from_schema(schema, store=store)
    return Draft202012Validator(
        schema,
        resolver=resolver,
        format_checker=FormatChecker(),
    )


def format_schema_error(error: Any) -> str:
    location = ".".join(str(part) for part in error.absolute_path) or "<root>"
    return f"{location}: {error.message}"
