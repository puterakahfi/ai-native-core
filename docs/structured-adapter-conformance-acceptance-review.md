# Structured Adapter Conformance V2 — Acceptance Review

Status: candidate acceptance evidence for issue `#9`

Pull request: `#42`

Canonical declaration and result semantics:

```text
docs/adapter-conformance.md
```

Discovery and design decisions:

```text
docs/structured-adapter-conformance-discovery.md
```

## 1. Objective review

Issue `#9` requires structured, deterministic adapter conformance to replace prose-first interface inference while preserving behavioral evaluation and stronger evidence layers as separate concerns.

Candidate verdict:

```text
structured declaration: IMPLEMENTED
schema validation: IMPLEMENTED
deterministic contract resolution: IMPLEMENTED
machine reports: IMPLEMENTED
legacy migration mode: IMPLEMENTED
strict mode: IMPLEMENTED
textual matching as primary proof: REJECTED
behavior/runtime/product/approval collapse: REJECTED
consumer bulk mutation from core: NOT PERFORMED
```

## 2. Canonical artifacts

### Declaration

```text
schemas/adapter-conformance.schema.yaml
skills/<adapter-id>/adapter.conformance.yaml
```

The executable method remains in `SKILL.md`. The adjacent declaration owns static interface claims.

### Reports

```text
schemas/conformance-report.schema.yaml
conformance-reports/repository-summary.json
conformance-reports/<adapter-id>.json
```

### Validator

```text
scripts/conformance_validation.py
scripts/conformance_semantics.py
scripts/conformance_taxonomy.py
scripts/validate-conformance.py
```

### Permanent validation

```text
.github/workflows/validate-conformance.yml
```

## 3. Acceptance matrix

| Acceptance criterion | Evidence | Result |
|---|---|---|
| Canonical structured declaration is documented and schema-valid | declaration schema, canonical docs, complete/malformed fixtures | PASS |
| Contract ID, path, kind, and version are checked deterministically | manifest/path-alias resolver, identity/version regressions | PASS |
| Inputs, outputs, gates, boundaries, dependencies, handoffs, unsupported claims, and adapter requirements are checked from structured IDs | engine and semantic regression suites | PASS |
| Delegated-responsibility ownership fails non-zero | overclaim fixture and migration/strict CLI tests | PASS |
| Missing declarations differ from contradiction and partial coverage | `NOT_CHECKABLE`, `ERROR`, and `PARTIAL` fixtures | PASS |
| Text matching is not primary proof | text diagnostics are migration-only `INFO`; missing declaration remains `NOT_CHECKABLE` | PASS |
| Legacy adapters have a documented migration path | adjacent declaration guidance, migration mode, path/version compatibility | PASS |
| Machine-readable repository and per-adapter reports are generated | JSON/YAML writer and report schema tests | PASS |
| Static, behavioral, runtime, product, and approval evidence remain separate | distinct report fields and evidence-boundary statements | PASS |
| Previous boundary behavior remains regression-covered | covers/delegates, partial, missing, unknown, overclaim fixtures | PASS |
| Positive and negative fixtures run in CI | permanent conformance workflow | PASS |
| Consumer migration is tracked in `ai-native-skills` | `ai-native-skills#26`; core changed no consumer declaration | PASS |

## 4. Result semantics

### Structural

```text
CONFORMANT
PARTIAL
ERROR
NOT_CHECKABLE
```

### Evidence layers

```text
behavioral_status
runtime_status
product_status
approval_status
```

A structurally conformant declaration does not prove executable behavior. An evidence reference does not prove evidence sufficiency, applicability, acceptance, or authority.

## 5. Executable taxonomy

Official executable kinds:

```text
skill
workflow
meta-skill
```

Every contract-backed declaration includes:

```text
skill-adapter
```

Additional accepted declaration patterns:

```text
facade
runtime-adapter
port-adapter
```

Migration reports preserve additional legacy pattern strings without automatically accepting them as v2 declaration patterns.

## 6. Interface and boundary decisions

```text
required input omitted
→ PARTIAL

optional input omitted
→ allowed

required output omitted
→ PARTIAL

allowed output omitted
→ allowed

contract output explicitly marked unsupported
→ PARTIAL limitation

unknown interface or gate ID
→ ERROR

contract-owned boundary omitted
→ PARTIAL

contract-delegated boundary omitted
→ PARTIAL

contract-delegated responsibility claimed as covered
→ ERROR
```

Adapter-specific dependencies, handoffs, and requirements remain visible migration diagnostics when they exceed the reusable core agreement.

## 7. Exit semantics

Migration mode:

```text
0 → no ERROR
1 → one or more ERROR results
```

Strict mode:

```text
0 → all checked results CONFORMANT
1 → ERROR
2 → PARTIAL without ERROR
3 → NOT_CHECKABLE without ERROR
```

Behavioral, runtime, product, review, and approval evidence do not silently alter static structural exit codes.

## 8. Real consumer inventory

The permanent CI pipeline checks out `puterakahfi/ai-native-skills` and runs migration mode against the current executable adapter repository.

Observed migration state:

```text
contract-backed adapters discovered: 91
checked: 91
CONFORMANT: 0
PARTIAL: 0
ERROR: 0
NOT_CHECKABLE: 91
BEHAVIOR_NOT_VERIFIED: 91
```

Interpretation:

- legacy contract paths and version pins remain resolvable;
- no explicit v2 contradiction was found;
- no adapter is promoted to `CONFORMANT` without a reviewed adjacent declaration;
- consumer migration remains outstanding and is owned by `ai-native-skills#26`;
- `NOT_CHECKABLE` is a migration state, not proof of behavioral failure.

## 9. Regression coverage

The permanent gate executes:

```text
test_validate_conformance.py
test_conformance_semantics.py
test_contract_resolution.py
```

Covered scenarios include:

```text
complete declaration
partial declaration
missing declaration
malformed declaration
explicit delegated overclaim
contract ID/kind/version/capability mismatch
adapter kind/pattern mismatch
unknown interface IDs
required versus allowed outputs
dependencies and handoffs
adapter requirements
unsupported claims
legacy pattern preservation
behavioral evidence reference separation
migration and strict exit codes
per-adapter and repository reports
canonical and aliased path resolution
```

## 10. Compatibility

Retained compatibility surfaces:

```text
active contract-path aliases
exact, caret, and tilde version pins
validate-implements.sh path/version validation
validate-conformance.py parse_contract compatibility facade
legacy frontmatter migration observations
```

Compatibility does not convert legacy metadata into structured conformance.

## 11. Known limitations and downstream ownership

Not claimed by this change:

```text
consumer declarations completed in ai-native-skills
behavioral correctness
runtime execution correctness
product acceptance
review verdict
approval or authorization
production adoption
semantic quality of every adapter declaration
```

Downstream work:

```text
ai-native-skills#26
→ review and add declarations adapter by adapter
→ preserve actual executable responsibility
→ run strict migration slices
→ collect behavioral evidence separately
```

`native-ai-fw` and product repositories remain responsible for runtime and product evidence respectively.

## 12. Repository hygiene

Acceptance requires:

```text
no temporary conformance workflow
no one-time bulk declaration generator
no tracked Python bytecode
no consumer repository mutation from core
branch synchronized with main
```

Bulk declaration generation is intentionally rejected because copying contract lists cannot establish executable ownership.

## 13. Exact-head validation

Final exact-head commit and workflow run IDs are recorded in PR `#42` after this acceptance artifact passes both permanent gates.

Required final state:

```text
Contract Integrity            PASS
Validate Conformance Tooling  PASS
branch behind main            0
PR mergeable                  yes
PR draft                      false only after final evidence
```

## 14. Candidate acceptance verdict

```text
canonical declaration: PASS
structured structural checks: PASS
result and exit semantics: PASS
machine reports: PASS
legacy migration safety: PASS
evidence-layer separation: PASS
consumer bulk mutation avoided: PASS
real repository inventory: PASS
final exact-head CI: PENDING
ready for merge: NO — owner review required
```
