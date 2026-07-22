# Structured Adapter Conformance V2 — Discovery And Decisions

Status: implementation discovery for issue `#9`

Base: `main@2fdc5529eb44762580430012917147f8648f8608`

## Objective

Replace prose-first interface inference with a structured, deterministic declaration and report model while preserving executable methodology in `SKILL.md` and keeping behavioral, runtime, product, and approval evidence separate.

## Current baseline

The previous validator already provided useful behavior:

- schema-aware canonical and legacy contract path resolution;
- compatible version-pin resolution through the manifest and path aliases;
- explicit boundary `covers` and `delegates` checks;
- `ERROR`, `WARN`, and `NOT_CHECKABLE` boundary findings;
- fuzzy textual diagnostics for inputs, outputs, and gates.

The remaining problem was that interface coverage could be inferred from copied vocabulary in prose. A skill could mention contract terms without declaring that it supports the interface or without actually performing the responsibility.

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

The declaration is separate from `SKILL.md` because Agent Skills frontmatter uses namespaced scalar metadata and should remain a portable executable entry point rather than becoming a deeply nested conformance document.

Legacy frontmatter fields remain migration inputs:

```text
ai-native-skills.implements
ai-native-skills.contract-version
ai-native-skills.boundary.covers
ai-native-skills.boundary.delegates
ai-native-skills.pattern
```

They do not produce full v2 conformance by themselves.

## Executable taxonomy decision

`ai-native-skills` has three official executable types:

```text
skill
workflow
meta-skill
```

Adapter and composition semantics are patterns, not new types.

Every contract-backed v2 declaration includes:

```text
skill-adapter
```

Additional accepted declaration patterns:

```text
facade
runtime-adapter
port-adapter
```

Legacy reports may preserve additional downstream values, such as `domain-reviewer`, without making those values accepted declaration patterns.

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
    patterns:
      - skill-adapter
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

The validator checks deterministically:

1. declaration schema and adapter entrypoint identity;
2. executable kind and adapter patterns;
3. canonical or aliased contract path resolution;
4. contract ID, kind, and version-pin compatibility;
5. exact capability identity;
6. required and optional input declarations;
7. required and allowed output declarations;
8. quality or safety gate declarations;
9. owned and delegated boundary declarations;
10. dependencies and handoffs when represented by stable IDs;
11. adapter requirement keys;
12. unsupported or out-of-bound claims;
13. evidence references without treating references as verified evidence.

Unknown interface or boundary IDs are errors. Missing required coverage is partial. Explicit ownership of a delegated responsibility is an error.

## Output semantics decision

```text
required output omitted
→ PARTIAL

allowed output omitted
→ no coverage failure

contract output explicitly marked unsupported
→ PARTIAL limitation

unknown output declared
→ ERROR
```

The allowed-output list defines a permitted universe, not a requirement that every adapter support every possible result.

## Adapter-specific extensions

Dependencies, handoffs, or adapter requirements not represented by the reusable core contract may still be valid adapter-level constraints. They are preserved as migration diagnostics rather than automatically treated as core contract claims.

## Result dimensions

Static conformance is not one Boolean and is not runtime proof.

```text
structural_status
→ CONFORMANT | PARTIAL | ERROR | NOT_CHECKABLE

behavioral_status
→ BEHAVIOR_NOT_VERIFIED | EVIDENCE_REFERENCED

runtime_status
→ NOT_CHECKABLE | EVIDENCE_REFERENCED

product_status
→ NOT_CHECKABLE | EVIDENCE_REFERENCED

approval_status
→ NOT_EVALUATED
```

An evidence reference proves only that a reference was declared. It does not prove that the referenced evidence is sufficient, accepted, applicable, or authority-bearing.

## Exit semantics

Migration mode preserves downstream compatibility:

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

The validator writes:

```text
per-adapter JSON or YAML report
repository summary JSON or YAML
```

The report records contract identity, declaration identity, executable kind, adapter patterns, result dimensions, findings, evidence references, and migration diagnostics.

Report serialization intentionally preserves unknown legacy pattern strings so consumer migration evidence is not lost.

## Textual diagnostics

Textual gate/input/output matching remains available only as supplemental migration diagnostics. It must never upgrade a missing structured declaration to `CONFORMANT`.

## Compatibility boundary

Existing adapters without `adapter.conformance.yaml` are classified `NOT_CHECKABLE`, not silently conformant. Existing path/version, boundary, type, and pattern metadata are preserved in the report as migration observations.

Real inventory against `ai-native-skills` found:

```text
91 contract-backed adapters
0 CONFORMANT
0 PARTIAL
0 ERROR
91 NOT_CHECKABLE
91 BEHAVIOR_NOT_VERIFIED
```

This is an expected migration state, not a claim that the adapters fail behaviorally.

## Evidence boundary

```text
structured declaration
≠ behavioral execution
≠ runtime execution
≠ product acceptance
≠ approval
```

The validator must not emit claims stronger than the evidence layer it actually inspected.
