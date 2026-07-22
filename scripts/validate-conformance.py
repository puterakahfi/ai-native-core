#!/usr/bin/env python3
"""Stable CLI entry point for structured adapter conformance validation v2."""

from pathlib import Path
from typing import Any, Optional

import conformance_validation as engine
from conformance_taxonomy import enhance_legacy, enhance_structured
from contract_resolution import load_contract_document

engine.validate_structured = enhance_structured(engine, engine.validate_structured)
engine.validate_legacy = enhance_legacy(engine, engine.validate_legacy)

from conformance_validation import *  # noqa: E402,F401,F403

cli = engine.cli
interface = engine.interface
validate_structured = engine.validate_structured
validate_legacy = engine.validate_legacy


def parse_contract(path: Path) -> Optional[dict[str, Any]]:
    """Compatibility facade for consumers that inspect a contract family."""
    try:
        kind, body, _document = load_contract_document(path)
        parsed = interface(kind, body)
        parsed["quality_gates"] = parsed["gates"]
        parsed["inputs"] = {
            "required": parsed["required_inputs"],
            "optional": parsed["optional_inputs"],
        }
        parsed["outputs"] = {
            "required": parsed["required_outputs"],
            "allowed": parsed["allowed_outputs"],
        }
        parsed["boundary"] = {
            "covers": parsed["covers"],
            "does_not_cover": parsed["delegates"],
        }
        return parsed
    except Exception:
        return None


if __name__ == "__main__":
    raise SystemExit(cli())
