#!/usr/bin/env python3
"""One-time navigation patch for schema v1 contributor and visitor guidance."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise SystemExit(f"documentation patch anchor not found: {label}")


readme = README.read_text()
readme = replace_once(
    readme,
    "| Looking for a capability or lifecycle contract | [Contract catalog](docs/contract-catalog.md) |\n",
    "| Looking for a capability or lifecycle contract | [Contract catalog](docs/contract-catalog.md) |\n"
    "| Understanding contract kinds, schema versions, and workflow migration | [Contract schema architecture](docs/contract-schema-architecture.md) |\n",
    "readme start table",
)
readme = replace_once(
    readme,
    "A skill contract is a YAML interface, not executable methodology:\n\n```yaml\nskill_contract:\n",
    "A skill contract is a YAML interface, not executable methodology. Every artifact declares schema identity separately from contract version:\n\n"
    "```yaml\ncontract_schema:\n  kind: skill_contract\n  version: \"1.0.0\"\n  path: schemas/skill-contract.schema.yaml\n\nskill_contract:\n",
    "readme contract envelope",
)
readme = replace_once(
    readme,
    "Workflow contracts use the same principles but emphasize ordered phases, gates, ownership, evidence, handoffs, and exit conditions.\n",
    "Workflow contracts use `workflow_contract` under `contracts/workflows/` and emphasize ordered phases, gates, ownership, evidence, handoffs, and exit conditions. Internal skill procedure phases do not automatically create a workflow contract.\n",
    "readme workflow classification",
)
readme = replace_once(
    readme,
    "  generated registry of IDs, paths, checksums, and skill-contract versions where recorded\n",
    "  schema-aware registry of IDs, kinds, schema versions, canonical paths, contract versions, and checksums\n",
    "readme manifest map",
)
readme = replace_once(
    readme,
    "  reserved validation schemas; only add with a real artifact and validator path\n",
    "  canonical family schemas, shared primitives, manifest schemas, and fixture-backed future boundaries\n",
    "readme schema map",
)
readme = replace_once(
    readme,
    "Review and commit the resulting ID, path, checksum, skill-contract version where recorded, and total changes. Do not hand-edit the manifest.\n",
    "Review and commit the resulting ID, kind, schema version, schema path, canonical artifact path, contract version, checksum, and total changes. Do not hand-edit the manifest.\n",
    "readme manifest governance",
)
readme = replace_once(
    readme,
    "| [`generate-manifest.sh`](scripts/generate-manifest.sh) | regenerate contract registry and checksums |\n",
    "| [`validate-contract-schemas.py`](scripts/validate-contract-schemas.py) | validate all contract families, workflow references, compatibility aliases, and manifest parity |\n"
    "| [`generate-manifest.sh`](scripts/generate-manifest.sh) | regenerate schema-aware contract registry and checksums |\n",
    "readme validation tools",
)
readme = replace_once(
    readme,
    "- [Contract catalog](docs/contract-catalog.md)\n",
    "- [Contract catalog](docs/contract-catalog.md)\n- [Contract schema architecture](docs/contract-schema-architecture.md)\n- [Schema registry](schemas/README.md)\n",
    "readme canonical docs",
)
README.write_text(readme)

contributing = CONTRIBUTING.read_text()
contributing = replace_once(
    contributing,
    "A workflow contract should make phases, gates, ownership, evidence, handoffs, and exit conditions explicit. Specialist methodology remains in executable skills or supporting documentation; the contract owns lifecycle expectations.\n",
    "A workflow contract uses the `workflow_contract` root under `contracts/workflows/` and makes phases, gates, ownership, evidence, handoffs, and exit conditions explicit. Specialist methodology remains in executable skills or supporting documentation; the contract owns lifecycle expectations. A skill with internal procedure phases remains a skill unless it owns a separately coordinated lifecycle.\n",
    "contributing workflow classification",
)
contributing = replace_once(
    contributing,
    "Runtime contracts define required capabilities and constraints. Provider commands, infrastructure policy, deployment credentials, and installed runtime state belong in adapters or product repositories.\n",
    "Runtime contracts define required capabilities and constraints. They must not own an ordered phase-transition workflow lifecycle. Provider commands, infrastructure policy, deployment credentials, and installed runtime state belong in adapters or product repositories.\n",
    "contributing runtime boundary",
)
old_schema = """### Add a schema

`schemas/` is reserved for reusable validation schemas and may not yet contain a validator for every artifact family.

When introducing a schema:

- connect it to a real artifact and validation path;
- document what it validates and what it does not validate;
- add fixtures or tests where applicable;
- avoid introducing an unused schema as aspirational documentation;
- update the README or relevant architecture document.
"""
new_schema = """### Add or evolve a schema

`schemas/` is the canonical registry for contract-family schemas and shared serialization primitives.

When introducing or changing a schema:

- declare whether the change affects schema version, contract version, or both;
- preserve family-owned domain meaning and avoid semantic normalization by field name alone;
- connect it to active artifacts or an explicit fixture-backed future boundary;
- add positive and negative fixtures;
- add repository and semantic regression tests;
- define compatibility and migration behavior;
- regenerate the manifest and schema discovery report;
- document what structural validation proves and what remains unverified.

Do not add an unused schema as aspirational documentation or weaken a family schema merely to make incompatible artifacts pass.
"""
contributing = replace_once(contributing, old_schema, new_schema, "contributing schema guidance")
contributing = replace_once(
    contributing,
    "A typical skill contract follows this shape:\n\n```yaml\nskill_contract:\n",
    "A typical skill contract follows this envelope. Schema version and contract version are independent:\n\n"
    "```yaml\ncontract_schema:\n  kind: skill_contract\n  version: \"1.0.0\"\n  path: schemas/skill-contract.schema.yaml\n\nskill_contract:\n",
    "contributing contract envelope",
)
contributing = replace_once(
    contributing,
    "- contract ID and path;\n- version where recorded;\n- checksum change;\n",
    "- contract ID and kind;\n- schema version and schema path;\n- canonical artifact path and contract version;\n- checksum change;\n",
    "contributing manifest metadata",
)
contributing = replace_once(
    contributing,
    "Install Python dependencies required by the scripts, including PyYAML, before running Python validation.\n",
    "Install Python dependencies required by the scripts, including PyYAML and jsonschema, before running Python validation.\n\n"
    "### Validate all contract families and generated metadata\n\n"
    "```bash\npython3 scripts/validate-contract-schemas.py\npython3 scripts/validate-contract-identity.py\n./scripts/generate-manifest.sh\npython3 scripts/inventory-contract-schemas.py --check\n```\n",
    "contributing unified validation",
)
contributing = replace_once(
    contributing,
    "- [ ] IDs, paths, versions, boundaries, and terminology are consistent.\n",
    "- [ ] Contract kind, schema version/path, ID, canonical path, contract version, boundaries, and terminology are consistent.\n",
    "contributing checklist identity",
)
contributing = replace_once(
    contributing,
    "- [ ] The manifest was regenerated for contract changes.\n",
    "- [ ] The manifest and schema discovery report were regenerated for contract changes.\n",
    "contributing checklist generated",
)
CONTRIBUTING.write_text(contributing)

print("Patched README and CONTRIBUTING for contract schema v1 navigation.")
