#!/usr/bin/env python3
"""Generate the Native AI contract manifest from declared schema identities."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_ROOT = ROOT / "contracts"
MANIFEST_PATH = CONTRACTS_ROOT / "manifest.yaml"

ARTIFACT_SUFFIXES = (".contract.yaml", ".port.yaml", ".test.yaml")
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


def artifact_paths() -> list[Path]:
    return sorted(
        path
        for path in CONTRACTS_ROOT.rglob("*.yaml")
        if path != MANIFEST_PATH and path.name.endswith(ARTIFACT_SUFFIXES)
    )


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: document root must be a mapping")
    return payload


def checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def expected_filename_id(path: Path) -> str:
    for suffix in ARTIFACT_SUFFIXES:
        if path.name.endswith(suffix):
            return path.name[: -len(suffix)]
    raise ValueError(f"unsupported artifact path: {path}")


def inspect(path: Path) -> tuple[str, dict[str, Any], dict[str, Any]]:
    document = load_yaml(path)
    schema_identity = document.get("contract_schema")
    if not isinstance(schema_identity, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: missing contract_schema mapping")

    kind = str(schema_identity.get("kind", "")).strip()
    schema_version = str(schema_identity.get("version", "")).strip()
    schema_path = str(schema_identity.get("path", "")).strip()
    root_key = ROOT_BY_KIND.get(kind)
    if not root_key:
        raise ValueError(f"{path.relative_to(ROOT)}: unsupported contract_schema.kind '{kind}'")

    body = document.get(root_key)
    if not isinstance(body, dict):
        raise ValueError(
            f"{path.relative_to(ROOT)}: kind '{kind}' requires root mapping '{root_key}'"
        )

    if kind == "behavioral_test_contract":
        contract_id = expected_filename_id(path)
    elif kind == "adapter_manifest":
        contract_id = str(body.get("adapter_id", "")).strip()
    else:
        contract_id = str(body.get("id", "")).strip()
    version = str(body.get("version", "")).strip()

    if not contract_id:
        raise ValueError(f"{path.relative_to(ROOT)}: missing contract identity")
    if not version:
        raise ValueError(f"{path.relative_to(ROOT)}: missing contract version")
    if not schema_version or not schema_path:
        raise ValueError(f"{path.relative_to(ROOT)}: incomplete schema identity")

    entry = {
        "id": contract_id,
        "kind": kind,
        "schema_version": schema_version,
        "schema_path": schema_path,
        "path": path.relative_to(ROOT).as_posix(),
        "version": version,
        "sha256": checksum(path),
    }
    return kind, body, entry


def empty_groups() -> dict[str, Any]:
    return {
        "skills": {},
        "ports": {},
        "workflows": [],
        "tests": [],
        "runtime": [],
        "compatibility": [],
        "adapters": [],
        "domains": [],
    }


def add_entry(groups: dict[str, Any], path: Path, kind: str, body: dict[str, Any], entry: dict[str, Any]) -> None:
    if kind == "skill_contract":
        category = str(body.get("category", "uncategorized"))
        groups["skills"].setdefault(category, []).append(entry)
    elif kind == "port_contract":
        port_kind = path.parent.name
        groups["ports"].setdefault(port_kind, []).append(entry)
    elif kind == "workflow_contract":
        groups["workflows"].append(entry)
    elif kind == "behavioral_test_contract":
        groups["tests"].append(entry)
    elif kind == "runtime_contract":
        groups["runtime"].append(entry)
    elif kind == "compatibility_manifest":
        groups["compatibility"].append(entry)
    elif kind == "adapter_manifest":
        groups["adapters"].append(entry)
    elif kind == "domain_contract":
        groups["domains"].append(entry)
    else:  # pragma: no cover - guarded by ROOT_BY_KIND
        raise ValueError(f"unsupported contract kind: {kind}")


def sort_groups(groups: dict[str, Any]) -> None:
    groups["skills"] = {
        category: sorted(entries, key=lambda item: item["id"])
        for category, entries in sorted(groups["skills"].items())
    }
    groups["ports"] = {
        kind: sorted(entries, key=lambda item: item["id"])
        for kind, entries in sorted(groups["ports"].items())
    }
    for name in ("workflows", "tests", "runtime", "compatibility", "adapters", "domains"):
        groups[name] = sorted(groups[name], key=lambda item: item["id"])


def normalized(payload: dict[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result["generated_at"] = "<normalized>"
    return result


def generate() -> dict[str, Any]:
    groups = empty_groups()
    paths = artifact_paths()
    for path in paths:
        kind, body, entry = inspect(path)
        add_entry(groups, path, kind, body, entry)
    sort_groups(groups)

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload = {
        "contract_schema": {
            "kind": "contract_manifest",
            "version": "1.0.0",
            "path": "schemas/contract-manifest.schema.yaml",
        },
        "version": "2.0.0",
        "generated_at": timestamp,
        "description": "Auto-generated schema-aware contract manifest. Regenerate with: scripts/generate-manifest.sh",
        "total_contracts": len(paths),
        "contracts": groups,
    }

    if MANIFEST_PATH.exists():
        try:
            existing = load_yaml(MANIFEST_PATH)
        except Exception:
            existing = {}
        if existing and normalized(existing) == normalized(payload):
            payload["generated_at"] = existing.get("generated_at", timestamp)

    return payload


def main() -> int:
    try:
        payload = generate()
    except Exception as exc:
        print(f"Manifest generation failed: {exc}")
        return 1

    rendered = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120)
    MANIFEST_PATH.write_text(rendered)
    print(f"Generated {MANIFEST_PATH.relative_to(ROOT)} ({payload['total_contracts']} contracts).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
