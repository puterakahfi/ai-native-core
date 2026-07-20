#!/usr/bin/env python3
"""Validate stable adapter references to first-class Native AI port contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PORTS_ROOT = ROOT / "contracts" / "ports"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PIN_PATTERN = re.compile(r"^(?:\^|~)?\d+\.\d+(?:\.\d+)?(?:-[0-9A-Za-z.-]+)?$")


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError("document root must be a mapping")
    return payload


def parse_version(value: str) -> tuple[int, int, int]:
    core = value.split("-", 1)[0]
    parts = core.split(".")
    if len(parts) not in (2, 3) or not all(part.isdigit() for part in parts):
        raise ValueError(f"invalid semantic version '{value}'")
    major, minor = int(parts[0]), int(parts[1])
    patch = int(parts[2]) if len(parts) == 3 else 0
    return major, minor, patch


def pin_accepts(pin: str, version: str) -> bool:
    if not PIN_PATTERN.fullmatch(pin):
        raise ValueError(f"unsupported version pin '{pin}'")

    prefix = pin[0] if pin[0] in "^~" else ""
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


def validate_reference(path: Path, *, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        payload = load_yaml(path)
    except Exception as exc:
        return [f"invalid YAML: {exc}"]

    reference = payload.get("port_adapter_reference")
    if not isinstance(reference, dict):
        return ["missing port_adapter_reference mapping"]

    allowed = {"adapter_id", "port_id", "port_path", "port_version"}
    unknown = sorted(set(reference) - allowed)
    if unknown:
        errors.append(f"unknown fields: {', '.join(unknown)}")

    adapter_id = str(reference.get("adapter_id", "")).strip()
    port_id = str(reference.get("port_id", "")).strip()
    port_path_value = str(reference.get("port_path", "")).strip()
    port_version = str(reference.get("port_version", "")).strip()

    if not ID_PATTERN.fullmatch(adapter_id):
        errors.append("adapter_id must be a non-empty kebab-case identifier")
    if not ID_PATTERN.fullmatch(port_id):
        errors.append("port_id must be a non-empty kebab-case identifier")
    if not port_path_value:
        errors.append("port_path is required")
    if not port_version:
        errors.append("port_version is required")

    if errors:
        return errors

    candidate = (root / port_path_value).resolve()
    try:
        candidate.relative_to((root / "contracts" / "ports").resolve())
    except ValueError:
        errors.append("port_path must resolve under contracts/ports")
        return errors

    if not candidate.exists():
        errors.append(f"port_path does not exist: {port_path_value}")
        return errors

    try:
        contract_payload = load_yaml(candidate)
    except Exception as exc:
        errors.append(f"referenced port contract is invalid YAML: {exc}")
        return errors

    contract = contract_payload.get("port_contract")
    if not isinstance(contract, dict):
        errors.append("referenced file does not contain port_contract")
        return errors

    actual_id = str(contract.get("id", "")).strip()
    actual_version = str(contract.get("version", "")).strip()

    if actual_id != port_id:
        errors.append(
            f"port_id mismatch: reference declares '{port_id}', contract declares '{actual_id}'"
        )

    try:
        compatible = pin_accepts(port_version, actual_version)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if not compatible:
            errors.append(
                f"port_version '{port_version}' is incompatible with contract version '{actual_version}'"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate adapter ID/path/version references to first-class port contracts."
    )
    parser.add_argument("references", nargs="+", help="Port adapter reference YAML files.")
    args = parser.parse_args()

    errors: list[str] = []
    for value in args.references:
        path = Path(value).resolve()
        for error in validate_reference(path):
            errors.append(f"{path}: {error}")

    if errors:
        print("Port adapter reference validation failed:\n")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} adapter reference violation(s).")
        return 1

    print(
        f"PASS — {len(args.references)} adapter reference(s) resolve by stable ID, "
        "canonical path, and compatible version pin."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
