#!/usr/bin/env python3
"""Stable CLI entry point for structured adapter conformance validation v2."""

from pathlib import Path
from typing import Any, Optional

from conformance_validation import *  # noqa: F401,F403
from conformance_validation import cli, interface
from contract_resolution import load_contract_document


def parse_contract(path: Path) -> Optional[dict[str, Any]]:
    """Compatibility facade for consumers that inspect a contract family."""
    try:
        kind, body, _document = load_contract_document(path)
        return interface(kind, body)
    except Exception:
        return None


if __name__ == "__main__":
    raise SystemExit(cli())
