# Contributing to Native AI Core

Thank you for improving the public contract layer of Native AI Engineering.

Native AI Core owns runtime-agnostic domain language, architecture boundaries, ports, contracts, rules, templates, schemas, conformance semantics, and quality standards. Contributions should make those agreements clearer, more reusable, and more verifiable without importing private product context or provider-specific implementation.

## Before changing the core

1. Identify the issue, objective, and acceptance criteria.
2. Confirm that the change is universal enough to belong in `ai-native-core`.
3. Inspect existing contracts, schemas, docs, validators, and consumers before creating a new concept.
4. Determine compatibility impact and affected adapters.
5. Preserve useful existing behavior unless the accepted change explicitly supersedes it.
6. Define the validation evidence required before claiming completion.

Repository responsibility:

```text
ai-native-core    canonical domain, contracts, ports, boundaries, terminology, schemas, and quality standards
ai-native-skills  executable reusable skills, workflows, declarations, references, and behavioral evaluation
native-ai-fw      orchestration, discovery, control-plane behavior, runtime adapters, and runtime evidence
product repos     product-specific implementation, policy, data, acceptance, and real-world validation
```

Change the correct layer:

- update `ai-native-core` when a universal contract, principle, port, boundary, term, schema, validator rule, or quality standard changes;
- update `ai-native-skills` when executable behavior or adapter declarations change;
- update `native-ai-fw` when orchestration, binding, control-plane, or runtime behavior changes;
- update product repositories for product implementation and validation.

## Contribution paths

### Add or refine a skill contract

Place reusable capability contracts under:

```text
contracts/skills/<category>/<contract-id>.contract.yaml
```

A skill contract should define:

- a unique ID and semantic version;
- category, type, capability, and description;
- roles that consume the contract;
- required and optional inputs;
- required or allowed outputs;
- quality gates;
- explicit `covers` and `does_not_cover` boundaries;
- adapter requirements when product or runtime decisions must remain external.

Do not encode provider names, framework-specific code, private product policy, credentials, or customer context in a reusable contract.

### Add or refine a workflow contract

Use `contracts/workflows/` when the stable agreement is an ordered lifecycle.

A workflow contract uses the `workflow_contract` root under `contracts/workflows/` and makes phases, gates, ownership, evidence, handoffs, and exit conditions explicit. Specialist methodology remains in executable skills or supporting documentation; the contract owns lifecycle expectations. A skill with internal procedure phases remains a skill unless it owns a separately coordinated lifecycle.

### Add or refine a runtime contract

Use `contracts/runtime/` for runtime-facing agreements that must remain implementation-agnostic, such as context files, execution loops, memory, hooks, tool registration, or operating procedures.

Runtime contracts define required capabilities and constraints. They must not own an ordered phase-transition workflow lifecycle. Provider commands, infrastructure policy, deployment credentials, and installed runtime state belong in adapters or product repositories.

### Add a behavioral test contract

Behavioral evaluation contracts live in:

```text
contracts/tests/<skill-id>.test.yaml
```

A useful case defines:

- a realistic trigger;
- required behavior;
- prohibited behavior;
- sequence constraints when order matters;
- quality gates under evaluation.

Use behavioral cases to protect reusable learning and prevent known regressions. Do not add cases that only restate a contract description.

### Add or refine framework documentation

Use `docs/` for public architecture, port specifications, glossary terms, domain models, integration guidance, migration records, and acceptance evidence.

Documentation may explain rationale and examples, but it must not silently redefine a machine-readable contract or schema. Update the governing artifact and documentation together when the actual interface changes.

### Add or refine rules

Use `rules/` for reusable mandatory constraints. A rule should be broadly applicable, testable where possible, and clearly separated from optional methodology.

### Add or refine templates

Use `templates/` for generic artifact starting points such as ADRs, blueprints, specifications, declarations, or review records.

Templates must remain product-neutral. Product-specific defaults, branding, environments, and private workflow policy belong in product adapters.

### Add or evolve a schema

`schemas/` is the canonical registry for contract-family schemas, conformance schemas, report schemas, and shared serialization primitives.

When introducing or changing a schema:

- declare whether the change affects schema version, contract version, declaration version, report version, or more than one;
- preserve family-owned domain meaning and avoid semantic normalization by field name alone;
- connect it to active artifacts or an explicit fixture-backed future boundary;
- add positive and negative fixtures;
- add repository and semantic regression tests;
- define compatibility and migration behavior;
- regenerate governed generated artifacts when applicable;
- document what structural validation proves and what remains unverified.

Do not add an unused schema as aspirational documentation or weaken a family schema merely to make incompatible artifacts pass.

## Contract format

A typical skill contract follows this envelope. Schema version and contract version are independent:

```yaml
contract_schema:
  kind: skill_contract
  version: "1.0.0"
  path: schemas/skill-contract.schema.yaml

skill_contract:
  id: example-capability
  category: engineering
  type: skill
  version: "1.0.0"
  capability: example_capability
  description: >
    Runtime-agnostic capability description.
  roles:
    - example_role
  inputs:
    required: []
    optional: []
  outputs:
    allowed: []
  quality_gates: []
  boundary:
    covers: []
    does_not_cover: []
```

Use snake_case for machine-readable capabilities and gates. Use kebab-case for contract IDs and filenames. Keep IDs, filenames, manifest entries, aliases, and adapter references aligned.

## Structured adapter declarations

Executable methodology remains in:

```text
skills/<adapter-id>/SKILL.md
```

A contract-backed adapter declares static conformance beside it:

```text
skills/<adapter-id>/adapter.conformance.yaml
```

Canonical declaration:

```yaml
contract_schema:
  kind: adapter_conformance
  version: 1.0.0
  path: schemas/adapter-conformance.schema.yaml

adapter_conformance:
  adapter:
    id: example-adapter
    kind: skill
    patterns:
      - skill-adapter
    entrypoint: skills/example-adapter/SKILL.md

  implements:
    contract_id: example-capability
    contract_kind: skill_contract
    contract_path: contracts/skills/engineering/example-capability.contract.yaml
    contract_version: "^1.0.0"

  capability: example_capability

  interface:
    inputs: []
    outputs: []
    gates: []

  boundary:
    covers: []
    delegates: []

  dependencies: []
  handoffs: []
  unsupported_claims: []
  adapter_requirements: []
  evidence_refs: []
```

Official executable kinds:

```text
skill
workflow
meta-skill
```

Every contract-backed declaration includes the `skill-adapter` pattern. Additional accepted declaration patterns are `facade`, `runtime-adapter`, and `port-adapter`. Patterns do not replace the executable kind.

Rules:

- use exact contract IDs for interfaces, gates, boundaries, dependencies, handoffs, and adapter requirement keys;
- declare every required input, required output, and contract gate;
- treat optional inputs and allowed outputs as permitted universes rather than mandatory complete coverage;
- do not list a delegated responsibility under `covers`;
- do not delegate an item the contract assigns to the adapter unless the declaration intentionally records a `PARTIAL` limitation;
- record unsupported contract responsibilities honestly;
- preserve adapter-specific dependencies and handoffs as adapter evidence rather than pretending they are core-owned;
- do not bulk-copy declarations without inspecting actual executable responsibility;
- treat declaration validation as one evidence layer, not proof of executable behavior.

Structural result meanings:

```text
CONFORMANT     required checkable structure matches the resolved contract
PARTIAL        declaration exists but required coverage or support is incomplete
ERROR          malformed, contradictory, incompatible, unresolved, unknown, or out-of-bound declaration
NOT_CHECKABLE  structured declaration is absent or required static evidence cannot be evaluated
```

Legacy frontmatter such as `ai-native-skills.implements`, contract-version pins, and dotted boundary metadata remains migration evidence only. It does not establish v2 `CONFORMANT` status.

See [`docs/adapter-conformance.md`](docs/adapter-conformance.md) for canonical declaration, report, result, exit-code, and evidence semantics.

## Versioning and compatibility

Version each contract independently according to behavioral compatibility.

### Patch

Use a patch bump for corrections or clarifications that do not change required adapter behavior, such as wording, examples, or non-semantic metadata.

### Minor

For contracts at `1.x` or later, use a minor bump only for backward-compatible additions, such as optional inputs or additive metadata that existing compliant adapters do not need to change to satisfy.

### Major

Use a major bump when existing adapters may need changes, including:

- adding or changing required inputs;
- adding required outputs or quality gates;
- renaming or removing inputs, outputs, IDs, or gates;
- changing output meaning;
- changing contract ownership or delegation boundaries;
- moving a contract path used by adapters.

For `0.x` contracts, a minor bump may represent a breaking pre-stable change. The current resolver treats `^0.y.z` as compatible only within the same `0.y` line.

Adapter pins currently support:

```text
^1.2.0  compatible versions in major line 1
^0.2.0  compatible patches in the 0.2 line
~1.2    versions in the 1.2 line
exact   exact version only
```

See [`scripts/validate-implements.sh`](scripts/validate-implements.sh) and [`scripts/contract_resolution.py`](scripts/contract_resolution.py) for implemented pin and alias semantics.

Do not claim compatibility from version numbers alone. Validate dependent adapters and disclose migrations that remain outstanding.

## Manifest governance

[`contracts/manifest.yaml`](contracts/manifest.yaml) is generated and must not be edited manually.

Regenerate it after any governed contract content, path, filename, addition, deletion, or version change:

```bash
./scripts/generate-manifest.sh
```

Then inspect and commit the resulting manifest changes. Verify:

- contract ID and kind;
- schema version and schema path;
- canonical artifact path and contract version;
- checksum change;
- total artifact count;
- removed or moved entries;
- unexpected unrelated drift.

Documentation-only and adapter-conformance tooling changes do not alter the core contract manifest unless a governed contract artifact also changes.

## Validation

Install Python dependencies required by the scripts, including PyYAML and jsonschema, before running Python validation.

### Validate all contract families and generated metadata

```bash
python3 scripts/validate-contract-schemas.py
python3 scripts/validate-contract-identity.py
./scripts/generate-manifest.sh
python3 scripts/inventory-contract-schemas.py --check
```

### Validate behavioral test contracts

```bash
python3 scripts/run-eval.py --all --validate-tests
```

### Validate script and test syntax

```bash
python3 -m py_compile \
  scripts/run-eval.py \
  scripts/conformance_validation.py \
  scripts/conformance_semantics.py \
  scripts/conformance_taxonomy.py \
  scripts/validate-conformance.py \
  tests/test_validate_conformance.py \
  tests/test_conformance_semantics.py
```

### Run validator unit and CLI regression tests

```bash
python3 -m unittest discover -s tests -v
```

Conformance fixtures cover complete, partial, missing, malformed, explicit overclaim, unknown interface IDs, version and identity mismatch, required versus allowed outputs, dependencies, handoffs, adapter requirements, executable kinds, adapter patterns, evidence-layer separation, machine reports, and exit codes.

### Validate adapter paths and pinned versions

From an adapter repository containing `SKILL.md` implementations:

```bash
../ai-native-core/scripts/validate-implements.sh ../ai-native-core
```

### Validate adapter conformance

From `ai-native-core` or another location with both repositories available:

```bash
python3 scripts/validate-conformance.py \
  ../ai-native-core \
  ../ai-native-skills \
  --mode migration \
  --output-dir conformance-reports
```

Use `--mode strict` only when the checked migration slice is expected to contain no `PARTIAL` or `NOT_CHECKABLE` result.

Path/version resolution and structured conformance are different checks. Textual matching is supplemental migration diagnostics only and cannot promote a missing declaration to `CONFORMANT`.

A zero migration-mode exit code means there is no explicit structural `ERROR`; it does not prove behavior, runtime execution, product acceptance, review, or approval.

### Validate documentation-only changes

For documentation-only changes, inspect:

- rendered Markdown structure;
- relative links and anchors;
- commands against current scripts;
- terminology against the glossary and architecture docs;
- source-of-truth boundaries;
- claims about current inventory against generated or validated sources.

## Documentation responsibilities

Update public documentation when a change affects:

- architecture layers or repository boundaries;
- contract identity, location, or versioning rules;
- port taxonomy;
- adapter declarations, report shapes, result semantics, or validation commands;
- templates, rules, schemas, or workflows;
- glossary terms;
- the visitor or contributor path.

Use [`docs/contract-catalog.md`](docs/contract-catalog.md) to explain inventory navigation. Use [`docs/adapter-conformance.md`](docs/adapter-conformance.md) for adapter declaration and validation semantics. Keep generated manifests and machine reports authoritative instead of maintaining duplicate exhaustive tables.

## Pull request checklist

Before requesting review:

- [ ] The issue objective and acceptance criteria are satisfied.
- [ ] The change belongs in the public core rather than a skill, framework, or product adapter.
- [ ] Existing contracts, schemas, validators, and consumers were inspected.
- [ ] Contract kind, schema version/path, ID, canonical path, contract version, boundaries, and terminology are consistent.
- [ ] Compatibility impact is classified honestly.
- [ ] Affected adapters and migration needs are disclosed.
- [ ] The manifest and schema discovery report were regenerated when governed contracts changed.
- [ ] Behavioral test contracts validate when affected.
- [ ] Validator unit and CLI regression tests pass when tooling changes.
- [ ] Adapter path/version and structured conformance checks were run when adapter repositories were available.
- [ ] Adapter kinds, patterns, interface IDs, and boundaries were reviewed against actual executable responsibility.
- [ ] Machine reports validate against their schema.
- [ ] Documentation and relative links were reviewed.
- [ ] Known gaps remain labeled `PARTIAL`, `NOT_CHECKABLE`, `BEHAVIOR_NOT_VERIFIED`, or `NOT_APPLICABLE` at the correct evidence layer.
- [ ] No credentials, private product context, customer data, or runtime-specific installed state were committed.

Use focused commits and a PR description that explains the contract change, compatibility impact, validation evidence, affected consumers, and known limitations.
