# Structured Adapter Conformance V2 — Discovery And Decisions

Status: implementation discovery for issue `#9`

Base: `main@2fdc5529eb44762580430012917147f8648f8608`

## Objective

Replace prose-first interface inference with a structured, deterministic declaration and report model while preserving executable methodology in `SKILL.md` and keeping behavioral, runtime, product, and approval evidence separate.

## Current baseline

The existing validator already provides useful behavior:

- schema-aware canonical and legacy contract path resolution;
- compatible version-pin resolution through the manifest and path aliases;
- explicit boundary `covers` and `delegates` checks;
- `ERROR`, `WARN`, and `NOT_CHECKABLE` boundary findings;
- legacy fuzzy text diagnostics for inputs, outputs, and gates.

The remaining problem is that gate/input/output coverage is inferred from copied vocabulary in prose. A skill can mention contract terms without declaring that it supports the interface or without actually performing the responsibility.

## Source ownership

```text
ai-native-core
→ declaration schema
→ report schema
→ validator semantics
→ compatibility and evidence boundaries

ai-native-skills
→ adapter declarations
→ executable methodology
→ migration inventory
→ behavioral evaluation

native-ai-fw
→ runtime observations and execution evidence

product repositories
→ product acceptance and field evidence
```

Core issue `#9` must not bulk-edit `ai-native-skills`. Consumer migration remains owned by `ai-native-skills#26`.

## Canonical declaration location

Preferred adapter declaration:

```text
skills/<adapter-id>/adapter.conformance.yaml
```

The declaration is separate from `SKILL.md` because Agent Skills frontmatter currently uses namespaced scalar metadata and should remain a portable executable entry point rather than becoming a deeply nested conformance document.

Legacy frontmatter fields remain migration inputs:

```text
ai-native-skills.implements
ai-native-skills.contract-version
ai-native-skills.boundary.covers
ai-native-skills.boundary.delegates
```

They do not produce full v2 conformance by themselves.

## Declaration model

```yaml
contract_schema:
  kind: adapter_conformance
  version: 1.0.0
  path: schemas/adapter-conformance.schema.yaml

adapter_conformance:
  adapter:
    id: example-adapter
    kind: skill
    entrypoint: skills/example-adapter/SKILL.md

  implements:
    contract_id: example-contract
    contract_kind: skill_contract
    contract_path: contracts/skills/example/example-contract.contract.yaml
    contract_version: ^1.0.0

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

## Structural checks

The validator must check deterministically:

1. declaration schema and adapter path identity;
2. canonical or aliased contract path resolution;
3. contract ID, kind, and version-pin compatibility;
4. exact capability identity;
5. required and optional input declarations;
6. required and allowed output declarations;
7. quality or safety gate declarations;
8. owned and delegated boundary declarations;
9. dependencies and handoffs when represented by stable IDs;
10. adapter requirement keys;
11. unsupported or out-of-bound claims;
12. evidence references without treating references as verified evidence.

Unknown interface or boundary IDs are errors. Missing required coverage is partial. Explicit ownership of a delegated responsibility is an error.

## Result dimensions

Static conformance is not one boolean and is not runtime proof.

```text
structural_status
→ CONFORMANT | PARTIAL | ERROR | NOT_CHECKABLE

behavioral_status
→ BEHAVIOR_NOT_VERIFIED | EVIDENCE_REFERENCED

runtime_status
→ NOT_CHECKABLE | EVIDENCE_REFERENCED

product_status
→ NOT_CHECKABLE | EVIDENCE_REFERENCED
```

An evidence reference proves only that a reference was declared and resolved when checkable. It does not prove the referenced evidence is sufficient, accepted, or applicable.

## Exit semantics

Migration mode preserves current downstream compatibility:

```text
0 → no ERROR findings
1 → one or more ERROR findings
```

Strict mode exposes incomplete migration to CI:

```text
0 → all checked declarations structurally CONFORMANT
1 → ERROR
2 → PARTIAL
3 → NOT_CHECKABLE
```

`BEHAVIOR_NOT_VERIFIED` does not fail static conformance because behavioral evaluation is a separate evidence layer. It remains explicit in every per-adapter report.

## Report outputs

The validator will write:

```text
per-adapter JSON or YAML report
repository summary JSON or YAML
```

The report records contract identity, declaration identity, result dimensions, findings, evidence references, and migration diagnostics.

## Textual diagnostics

Textual gate/input/output matching remains available only as supplemental migration diagnostics. It must never upgrade a missing structured declaration to `CONFORMANT`.

## Compatibility boundary

Existing adapters without `adapter.conformance.yaml` are classified `NOT_CHECKABLE`, not silently conformant. Existing path/version and boundary metadata are preserved in the report as migration observations.

## Evidence boundary

```text
structured declaration
≠ behavioral execution
≠ runtime execution
≠ product acceptance
≠ approval
```

The validator must not emit claims stronger than the evidence layer it actually inspected.
