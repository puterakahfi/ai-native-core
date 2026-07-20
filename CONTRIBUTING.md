# Contributing to Native AI Core

Thank you for improving the public contract layer of Native AI Engineering.

Native AI Core owns runtime-agnostic domain language, architecture boundaries, ports, contracts, rules, templates, and quality standards. Contributions should make those agreements clearer, more reusable, and more verifiable without importing private product context or provider-specific implementation.

## Before changing the core

1. Identify the issue, objective, and acceptance criteria.
2. Confirm that the change is universal enough to belong in `ai-native-core`.
3. Inspect existing contracts, docs, and consumers before creating a new concept.
4. Determine compatibility impact and affected adapters.
5. Preserve useful existing behavior unless the accepted change explicitly supersedes it.
6. Define the validation evidence required before claiming completion.

Repository responsibility:

```text
ai-native-core    canonical domain, contracts, ports, boundaries, terminology, and quality standards
ai-native-skills  executable reusable skills, workflows, references, and behavioral evaluation
native-ai-fw      orchestration, discovery, control-plane behavior, and runtime adapters
product repos     product-specific implementation, policy, data, and real-world validation
```

Change the correct layer:

- update `ai-native-core` when a universal contract, principle, port, boundary, term, or quality standard changes;
- update `ai-native-skills` when executable agent behavior changes;
- update `native-ai-fw` when orchestration or control-plane behavior changes;
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
- allowed outputs;
- quality gates;
- explicit `covers` and `does_not_cover` boundaries;
- adapter requirements when product or runtime decisions must remain external.

Do not encode provider names, framework-specific code, private product policy, credentials, or customer context in a reusable contract.

### Add or refine a workflow contract

Use `contracts/workflows/` when the stable agreement is an ordered lifecycle.

A workflow contract should make phases, gates, ownership, evidence, handoffs, and exit conditions explicit. Specialist methodology remains in executable skills or supporting documentation; the contract owns lifecycle expectations.

### Add or refine a runtime contract

Use `contracts/runtime/` for runtime-facing agreements that must remain implementation-agnostic, such as context files, execution loops, memory, hooks, tool registration, or operating procedures.

Runtime contracts define required capabilities and constraints. Provider commands, infrastructure policy, deployment credentials, and installed runtime state belong in adapters or product repositories.

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

Use `docs/` for public architecture, port specifications, glossary terms, domain models, and integration guidance.

Documentation may explain rationale and examples, but it must not silently redefine a machine-readable contract. Update the contract and documentation together when the actual interface changes.

### Add or refine rules

Use `rules/` for reusable mandatory constraints. A rule should be broadly applicable, testable where possible, and clearly separated from optional methodology.

### Add or refine templates

Use `templates/` for generic artifact starting points such as ADRs, blueprints, specifications, or review records.

Templates must remain product-neutral. Product-specific defaults, branding, environments, and private workflow policy belong in product adapters.

### Add a schema

`schemas/` is reserved for reusable validation schemas and may not yet contain a validator for every artifact family.

When introducing a schema:

- connect it to a real artifact and validation path;
- document what it validates and what it does not validate;
- add fixtures or tests where applicable;
- avoid introducing an unused schema as aspirational documentation;
- update the README or relevant architecture document.

## Contract format

A typical skill contract follows this shape:

```yaml
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

Use snake_case for machine-readable capabilities and gates. Use kebab-case for contract IDs and filenames. Keep IDs, filenames, manifest entries, and adapter references aligned.

## Versioning and compatibility

Version each contract independently according to behavioral compatibility.

### Patch

Use a patch bump for corrections or clarifications that do not change required adapter behavior, such as wording, examples, or non-semantic metadata.

### Minor

For contracts at `1.x` or later, use a minor bump only for backward-compatible additions, such as optional inputs or additive metadata that existing compliant adapters do not need to change to satisfy.

### Major

Use a major bump when existing adapters may need changes, including:

- adding or changing required inputs;
- adding required quality gates;
- renaming or removing inputs, outputs, IDs, or gates;
- changing output meaning;
- changing contract ownership or delegation boundaries;
- moving a contract path used by adapters.

For `0.x` contracts, a minor bump may represent a breaking pre-stable change. The current validator treats `^0.y.z` as compatible only within the same `0.y` line.

Adapter pins currently support:

```text
^1.2.0  compatible versions in major line 1
^0.2.0  compatible patches in the 0.2 line
~1.2    versions in the 1.2 line
exact   exact version only
```

See [`scripts/validate-implements.sh`](scripts/validate-implements.sh) for the implemented pin semantics.

Do not claim compatibility from version numbers alone. Validate dependent adapters and disclose migrations that remain outstanding.

## Manifest governance

[`contracts/manifest.yaml`](contracts/manifest.yaml) is generated and must not be edited manually.

Regenerate it after any contract content, path, filename, addition, deletion, or version change:

```bash
./scripts/generate-manifest.sh
```

Then inspect and commit the resulting manifest changes. Verify:

- contract ID and path;
- version where recorded;
- checksum change;
- total artifact count;
- removed or moved entries;
- unexpected unrelated drift.

Documentation-only changes do not require manifest regeneration.

## Validation

Install Python dependencies required by the scripts, including PyYAML, before running Python validation.

### Validate behavioral test contracts

```bash
python3 scripts/run-eval.py --all --validate-tests
```

### Validate script syntax

```bash
python3 -m py_compile \
  scripts/run-eval.py \
  scripts/validate-conformance.py
```

### Validate adapter paths and pinned versions

From an adapter repository containing `SKILL.md` implementations:

```bash
../ai-native-core/scripts/validate-implements.sh ../ai-native-core
```

### Validate adapter conformance

From an adapter repository:

```bash
python3 ../ai-native-core/scripts/validate-conformance.py \
  ../ai-native-core \
  .
```

Path/version validation and conformance validation are different checks. A valid path and compatible pin do not prove that the adapter covers all required gates, inputs, outputs, or boundaries.

### Validate documentation-only changes

For documentation-only changes, inspect:

- rendered Markdown structure;
- relative links and anchors;
- commands against current scripts;
- terminology against the glossary and architecture docs;
- source-of-truth boundaries;
- claims about current inventory against `contracts/manifest.yaml`.

## Documentation responsibilities

Update public documentation when a change affects:

- architecture layers or repository boundaries;
- contract identity, location, or versioning rules;
- port taxonomy;
- adapter metadata or validation commands;
- templates, rules, schemas, or workflows;
- glossary terms;
- the visitor or contributor path.

Use [`docs/contract-catalog.md`](docs/contract-catalog.md) to explain inventory navigation. Keep the generated manifest authoritative instead of maintaining duplicate exhaustive tables.

## Pull request checklist

Before requesting review:

- [ ] The issue objective and acceptance criteria are satisfied.
- [ ] The change belongs in the public core rather than a skill, framework, or product adapter.
- [ ] Existing contracts and consumers were inspected.
- [ ] IDs, paths, versions, boundaries, and terminology are consistent.
- [ ] Compatibility impact is classified honestly.
- [ ] Affected adapters and migration needs are disclosed.
- [ ] The manifest was regenerated for contract changes.
- [ ] Behavioral test contracts validate when affected.
- [ ] Adapter path/version and conformance checks were run when adapter repositories were available.
- [ ] Documentation and relative links were reviewed.
- [ ] Known gaps remain labeled `PARTIAL`, `NOT_VERIFIED`, or `NOT_APPLICABLE`.
- [ ] No credentials, private product context, customer data, or runtime-specific installed state were committed.

Use focused commits and a PR description that explains the contract change, compatibility impact, validation evidence, affected consumers, and known limitations.