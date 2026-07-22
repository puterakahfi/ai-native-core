#!/usr/bin/env python3
"""One-time patch for compatibility-manifest discovery classification."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "inventory-contract-schemas.py"
DOC = ROOT / "docs" / "contract-schema-architecture.md"

text = SCRIPT.read_text()

replacements = {
    '    "behavioral_test": "skill_test",\n}':
        '    "behavioral_test": "skill_test",\n    "compatibility": "compatibility_manifest",\n    "adapter": "port_adapter_reference",\n    "domain": "domain_contract",\n}',
    '    "behavioral_test": ["skill", "version", "description", "cases"],\n}':
        '    "behavioral_test": ["skill", "version", "description", "cases"],\n    "compatibility": ["id", "version", "aliases"],\n}',
    '        "tests": "behavioral_test",\n    }.get(first, "unclassified")':
        '        "tests": "behavioral_test",\n        "compatibility": "compatibility",\n        "adapters": "adapter",\n        "domains": "domain",\n    }.get(first, "unclassified")',
    '        if str(key).endswith(("_contract", "_test"))':
        '        if str(key).endswith(("_contract", "_test", "_manifest"))',
}

for old, new in replacements.items():
    if old not in text:
        if new not in text:
            raise SystemExit(f"inventory patch anchor not found: {old!r}")
    else:
        text = text.replace(old, new, 1)

SCRIPT.write_text(text)

architecture = DOC.read_text()
architecture = architecture.replace(
    "contracts/compatibility/contract-path-aliases.yaml",
    "contracts/compatibility/contract-path-aliases.contract.yaml",
)
DOC.write_text(architecture)

print("Patched discovery family classification and canonical compatibility path.")
