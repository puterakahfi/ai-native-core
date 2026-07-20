# Port Taxonomy And Contract Architecture Review

Issue: `#7 — Formalize port taxonomy and first-class port contracts`

Review type: final architecture and acceptance review

Decision: `PASS FOR ISSUE SCOPE`, subject to Contract Integrity passing on the final PR head

## 1. Review scope

This review verifies that the issue delivers a runtime-agnostic core contract system rather than provider adapters, product bindings, or a downstream registry.

Reviewed surfaces:

```text
docs/domain-model/**
docs/port-taxonomy.md
docs/port-inventory.yaml
docs/port-retention-matrix.md
docs/*-port.md
contracts/ports/**/*.port.yaml
schemas/port-contract.schema.yaml
scripts/validate-port-contracts.py
scripts/validate-port-adapter-reference.py
scripts/generate-manifest.sh
tests/test_validate_port_contracts.py
tests/test_port_inventory.py
tests/test_validate_port_adapter_reference.py
contracts/manifest.yaml
```

## 2. Canonical model alignment

The implementation preserves:

```text
DomainCapability
≠ Port
≠ Contract
≠ Adapter
≠ AdapterBinding
≠ ExecutionRun
```

Ownership remains aligned to the canonical bounded contexts:

```text
semantic owner
→ owns port meaning and invariants

Integration & Binding
→ owns adapter identity, compatibility, and binding selection

Runtime & Execution
→ owns actual ExecutionRun lifecycle and ExecutionStatus

Evidence, Evaluation & Review
→ owns evaluation and review semantics

Governance, Risk & Authority
→ owns approval and action authorization semantics
```

No provider, SDK, framework, product, or storage schema becomes canonical domain authority.

## 3. Taxonomy review

Canonical kinds are independently defined from communication direction:

```text
IntegrationPort
ControlPort
ProductSurfacePort
CapabilityCompositionPort
```

```text
inbound | outbound | bidirectional
```

The taxonomy does not require every kind to contain a contract. `ProductSurfacePort` remains empty because no universal reusable source boundary is proven.

Result: `PASS`

## 4. Active inventory completeness

The executable inventory covers:

```text
8 dedicated port documents
4 skill_contract.type: port composition sources
14 named general-document examples
5 former ToolIntegration subtype candidates
ProductSurface candidate family
```

Active file-backed sources resolve as:

```text
7 dedicated documents → migrated through rename, narrowing, or split
1 dedicated document  → retired as an incoherent umbrella
4 composition sources → migrated to first-class CapabilityCompositionPorts
```

Regression tests discover `skill_contract.type: port` sources automatically and exact-match the dedicated document set. Migrated records must point to existing contracts; retired, reclassified, and deferred records require rationale.

Result: `PASS`

## 5. Contract structure review

Every accepted port contract declares:

```text
stable ID, path, kind, version, and capability
direction and context ownership
owned, delegated, and excluded boundaries
requests, responses, events, and streams
structured failures and partial-result behavior
typed lifecycle transitions
authorization and authority semantics
idempotency
observability and sensitive fields
adapter contract-reference requirements
compatibility and breaking changes
quality gates
```

Schema and semantic validation reject:

```text
invalid roots or missing required structure
filename, ID, or kind-directory mismatch
duplicate IDs, capabilities, or aliases
overlapping owned/delegated/excluded boundaries
more than one owned typed status family
inconsistent authorization declarations
invalid legacy references
```

Result: `PASS`

## 6. Replaceability review

Adapters remain replaceable because port contracts:

```text
use provider-neutral requests and results
keep provider credentials and private configuration outside core
require stable ID, canonical path, and compatible version pin
assign binding selection to Integration & Binding
return structured external failures and limitations
avoid default-provider decisions
avoid SDK, framework, or product-specific types
```

The compatibility fixture proves that an adapter can reference a port contract by stable ID, path, and exact/caret/tilde version line.

A valid pin proves intended compatibility only. It does not prove implementation conformance or runtime behavior.

Result: `PASS`

## 7. Lifecycle and authority review

Required non-collapses are explicit and regression-protected:

```text
runtime control outcome ≠ ExecutionStatus
workflow coordination ≠ WorkflowRun lifecycle
rule availability ≠ rule evaluation
evaluation ≠ review
review ≠ approval
approval ≠ AuthorizationAssessment
authorization ≠ execution
execution ≠ completion
completion or delivery ≠ product acceptance
UI state representation ≠ canonical domain status
```

Only the owning contract may mutate its typed status family:

```text
ExecutionRunManagementPort → ExecutionStatus
ReviewManagementPort       → ReviewDisposition
ApprovalDecisionPort       → ApprovalStatus
```

Result: `PASS`

## 8. Specific migration decisions

### Agent runtime

Retained only as runtime control above existing `ExecutionRun`, `CapacityAssessment`, `AuthorizationAssessment`, `RuntimeEnvironment`, `Agent`, and `AdapterBinding` references. It owns no `ExecutionStatus`.

### Workflow orchestration

Renamed and narrowed to `WorkflowCoordinationPort`. The rejected draft introduced an unmodeled `WorkflowRun` aggregate; the accepted contract coordinates `WorkflowDefinition` phases, gates, transitions, handoffs, and exits without owning engine execution.

### Review and approval

`ReviewApprovalPort` is split into review management, approval decision, and authorization assessment. No combined alias is retained.

### Tool integration

`ToolIntegrationPort` is retired as one umbrella. Gateway translation, APIs, authentication, external operation execution, registry, permission, review, and approval require independent contracts and evidence.

### Code execution

The broad name is split. `CodeOperationExecutionPort` owns bounded actual operation requests and results; ExecutionRun recording, architecture, review, approval, completion, and delivery remain external.

### Database

`DatabasePort` owns provider-neutral structured persistence operations and evidence. Database schema does not define canonical domain meaning.

### Design composition

Visual direction, strategy, layout, and interaction have separate composition contracts. They compose methods and handoffs but do not own final implementation, review authority, release authorization, or product acceptance.

Result: `PASS`

## 9. Markdown authority review

Canonical machine meaning belongs only to:

```text
contracts/ports/**/*.port.yaml
```

Supporting roles are explicit:

```text
docs/port-inventory.yaml
→ executable source classification and migration status

docs/port-retention-matrix.md
→ human-readable decision rationale

legacy docs/*-port.md
→ explanation, navigation, and migration guidance
```

The former `ToolIntegrationPort` specification has been converted into a migration record. Other migrated dedicated documents link to or defer to first-class contracts.

Result: `PASS`

## 10. Manifest and breaking-change review

The generator registers every `*.port.yaml` by canonical kind with:

```text
ID
path
version
SHA-256 checksum prefix
```

Contract compatibility follows semantic versioning. Breaking changes include required input changes, changed result or failure meaning, removed evidence, weakened authority or observability semantics, and ownership expansion across bounded contexts.

The final Contract Integrity run must regenerate the manifest and produce no diff.

Result: `PASS`, pending final-head CI evidence

## 11. Acceptance criteria mapping

| Acceptance criterion | Review result |
|---|---|
| Canonical taxonomy uses issue #6 terminology | PASS |
| Every active port is inventoried and classified | PASS |
| Schema-valid `port_contract` exists | PASS |
| Canonical `contracts/ports/` structure exists | PASS |
| Manifest contains version and checksum | PASS, pending final generated sync |
| Requests, responses, failures, boundary, authority, observability, and adapter requirements are explicit | PASS |
| Adapter compatibility references stable ID, path, and version | PASS |
| Breaking-change semantics are defined | PASS |
| Markdown is not a competing machine source | PASS |
| Capability composition is distinct from integration, control, and product surface | PASS |
| Manifest generation, schema validation, and tests pass | PASS, pending final-head CI evidence |

## 12. Out-of-scope follow-up evidence

The issue explicitly does not implement provider adapters or build downstream registries. Therefore these remain follow-up owner work:

```text
ai-native-skills issue #26
ai-native-fw legacy adapter manifest migration
product-specific AdapterBinding declarations
adapter conformance evidence
runtime execution evidence
product acceptance evidence
```

Known downstream legacy names are evidence for future migration, not a reason to move product/runtime configuration into core.

## 13. Residual risks

```text
Static contracts can drift from downstream implementations.
A compatible version pin can be declared by an adapter that does not conform.
ProductSurfacePort may be over-generalized by future work without reusable evidence.
Deferred integration names may be bulk-created without independent ownership review.
Legacy Markdown or downstream manifests may continue using retired names.
```

Mitigations:

```text
executable inventory regression
schema and semantic validator
manifest drift check
stable adapter reference validator
explicit evidence limits
follow-up compatibility and conformance work in owning repositories
```

## 14. Final disposition

The architecture is internally consistent with the canonical domain model and issue scope. It provides a reviewable taxonomy, active-source inventory, versioned contract tree, compatibility semantics, generated registry, and permanent quality gates while preserving adapter replaceability and evidence boundaries.

```text
Architecture review: PASS FOR ISSUE SCOPE
Merge gate: Contract Integrity must pass on the final PR head
```
