# Contract Schema And Workflow Canonicalization Acceptance Review

Status: Candidate acceptance record for issue `#8`

Branch:

```text
8-unify-contract-schemas-and-workflow-contracts
```

Draft pull request:

```text
#39 — feat(schemas): unify contract schemas and canonicalize workflows
```

Upstream authority:

```text
#13 philosophy and source-role authority
→ #6 canonical domain model and ownership
→ #7 first-class port taxonomy and contracts
→ #8 contract schemas and workflow canonicalization
```

## 1. Acceptance conclusion

The issue `#8` objective and acceptance criteria are satisfied at the core contract layer.

The candidate establishes:

```text
one declared schema identity envelope
one canonical schema registry
one canonical workflow root and location
one schema-aware generated manifest
one unified repository validation pipeline
one explicit compatibility path for moved contracts
```

No runtime execution, executable skill behavior, provider implementation, product adapter, or product acceptance is claimed.

## 2. Final active inventory

Deterministic discovery records:

```text
129 active contract artifacts

85 skill contracts
17 port contracts
10 workflow contracts
10 behavioral-test contracts
6 runtime contracts
1 compatibility manifest
```

Result:

```text
129 parsed
0 ambiguous roots
0 unclassified artifacts
```

Every active artifact declares:

```text
contract kind
schema version
schema path
family-owned body root
contract identity
contract version
```

Generated manifest version `2.0.0` records for every artifact:

```text
id
kind
schema_version
schema_path
canonical path
contract version
checksum
```

## 3. Canonical schema registry

Active schemas:

```text
common.schema.yaml
skill-contract.schema.yaml
workflow-contract.schema.yaml
runtime-contract.schema.yaml
port-contract.schema.yaml
behavioral-test-contract.schema.yaml
compatibility-manifest.schema.yaml
contract-manifest.schema.yaml
```

Fixture-backed future boundaries:

```text
adapter-manifest.schema.yaml
domain-contract.schema.yaml
```

The future-boundary schemas have positive and negative fixtures but do not imply that first-class adapter or domain contract artifacts are currently implemented.

## 4. Shared primitive review

Shared serialization primitives are defined once for:

```text
contract and machine identifiers
workflow phase identifiers
semantic versions
schema and contract paths
schema identity
lists and gate identifiers
workflow phase, transition, and load references
compatibility path aliases
```

Domain meanings are not collapsed by serialization reuse:

```text
observation ≠ model ≠ assumption
claim ≠ evidence
review ≠ approval
permission ≠ authority
feedback ≠ learning
```

Family schemas retain family invariants. Existing domain-specific extension structures remain visible and compatible rather than being rewritten into one generic field by name similarity.

## 5. Workflow canonicalization review

Canonical location and root:

```text
contracts/workflows/<id>.contract.yaml
workflow_contract
```

Migrated while preserving stable IDs and contract versions:

```text
design-refinement
redesign-workflow
skill-evolution
development-loop
```

`development-loop` is serialized as:

```text
workflow_kind: execution_method
```

This preserves its domain role as an engineering execution method. It does not turn the Development Loop into a product workflow or the canonical domain lifecycle. Issue `#26` retains its separate wording and review/approval refinement responsibility.

Retained as skill contracts:

```text
design-review
systematic-debugging
```

Their phases are internal expert-procedure steps, not separately coordinated lifecycle ownership.

Required negative states are regression-tested:

```text
skill_contract type: workflow after migration
runtime contract owning phases or transitions
unknown workflow phase references
orphan skill-load phase references
duplicate workflow phase IDs
non-contiguous phase ordering
```

## 6. Compatibility review

Moved paths are governed by:

```text
contracts/compatibility/contract-path-aliases.contract.yaml
```

Each alias records:

```text
legacy path
canonical target path
contract identity
contract kind
compatible version range
migration status
```

The old files do not remain as competing machine authority.

Shared resolution tooling proves that:

```text
direct canonical paths resolve
all four legacy workflow paths resolve to canonical targets
adapter version pins are evaluated against canonical targets
conformance parsing follows the declared contract family root
```

Existing executable adapters may continue to declare a legacy path during the migration window. Direct metadata migration in `ai-native-skills` remains downstream work, not a blocker to the core compatibility agreement.

## 7. Unified validation review

Permanent `Contract integrity` validates:

```text
schema registry validity
all active contract documents
schema kind, version, and path identity
family path and root alignment
contract and alias uniqueness
workflow lifecycle references
runtime/workflow separation
compatibility target identity and version
port semantic invariants
behavioral-test contracts
manifest parity and checksums
deterministic manifest regeneration
schema discovery drift
positive and negative fixtures
```

Permanent `Validate Conformance Tooling` validates:

```text
canonical and legacy contract resolution
version-pin compatibility
schema-aware conformance parsing
boundary overclaim, partial declaration, and not-checkable behavior
```

Negative fixtures cover:

```text
malformed versions
missing gates
missing ownership boundaries
invalid adapter pins
incomplete compatibility aliases
incomplete manifest metadata
behavioral cases without assertions
runtime contracts owning workflow phases
```

Repository-level regressions additionally cover:

```text
duplicate IDs
filename/identity drift
kind/path-family drift
unknown workflow phases
broken alias targets
manifest checksum drift
canonical workflow movement
retained internal-phase skills
```

## 8. Compatibility with issue #7

The accepted first-class port schema and semantic validator remain active.

Issue `#8` adds the shared schema envelope and registry resolution without weakening:

```text
port kind and directory alignment
ownership boundaries
one typed status family
permission/authority separation
review/approval separation
adapter reference semantics
port alias uniqueness
```

Four legacy design `skill_contract type: port` artifacts remain compatibility sources:

```text
design-interaction
design-layout
design-strategy
design-visual
```

Their first-class port contracts from issue `#7` remain authoritative. The unified validator reports these as migration warnings rather than creating duplicate port authority.

## 9. Acceptance-criteria traceability

| Acceptance criterion | Result | Evidence |
|---|---|---|
| Canonical schemas for active families | PASS | schema registry, envelopes, unified validation |
| Shared primitives defined once | PASS | `schemas/common.schema.yaml` |
| Every current contract validates or has explicit migration rationale | PASS | 129/129 parsed and validated; workflow migration map |
| One workflow root and location | PASS | `workflow_contract` under `contracts/workflows/` |
| Lifecycle-as-skill migration reviewed | PASS | four migrations and two retained-skill decisions |
| Complete manifest metadata | PASS | schema-aware manifest v2 with 129 entries |
| Schema validation blocks malformed contracts in CI | PASS | permanent Contract Integrity and negative fixtures |
| Manifest identity and drift validation | PASS | YAML parser generator, parity checks, deterministic regeneration |
| Positive and negative fixtures | PASS | skill, workflow, runtime, port, behavioral test, adapter, compatibility, domain, manifest |
| Existing adapters receive compatibility path | PASS | active path aliases and resolver/conformance regressions |
| README, contribution guide, catalog use schemas as authority | PASS | navigation and contribution documentation updated |

## 10. Known limitations and downstream work

The following are intentionally not claimed as completed by issue `#8`:

```text
executable adapter behavior
runtime orchestration implementation
product-specific bindings
field or production validation
direct rewrite of ai-native-skills metadata to canonical workflow paths
semantic refinement owned by issue #26
promotion of fixture-backed adapter/domain schema into active artifacts
```

Schema presence and validation are not embodiment evidence.

## 11. Final acceptance boundary

Issue `#8` may be accepted when the owner confirms the canonical schema architecture, workflow classification, compatibility strategy, and validation evidence in PR `#39`.

Acceptance permits the core schema and migration contracts to become canonical. It does not approve downstream runtime or product behavior automatically.
