# Native AI Engineering Port Retention And Alias Matrix

Status: Final migration decision ledger for issue `#7`

Canonical domain authority: [`domain-model/README.md`](domain-model/README.md)

Canonical taxonomy: [`port-taxonomy.md`](port-taxonomy.md)

Executable inventory: [`port-inventory.yaml`](port-inventory.yaml)

Machine contracts: [`../contracts/ports/`](../contracts/ports/)

## 1. Decision rule

A first-class port requires:

```text
a real consumer context
a coherent required capability boundary
replaceable implementations or translations
explicit request, response, failure, compatibility, and observability semantics
one semantic owner
Integration & Binding ownership of adapter selection
runtime-agnostic versioning
references only to canonical domain objects and status families
```

A name is not retained merely because it ends in `Port`.

Decision values:

```text
MIGRATE     preserve an active source boundary as a first-class contract
RENAME      preserve meaning under a clearer identity
SPLIT       separate independent boundaries or status families
RECLASSIFY  move to skill, workflow, policy, adapter, binding, aggregate, or product
RETIRE      remove an incoherent boundary name
DEFER       wait for sufficient reusable evidence
```

## 2. Canonical first-class contracts

### IntegrationPort

```text
model-inference@0.1.0
code-operation-execution@0.1.0
database@0.1.0
```

### ControlPort

```text
agent-runtime@0.1.0
workflow-coordination@0.1.0
execution-run-management@0.1.0
context-resolution@0.1.0
skill-resolution@0.1.0
rule-resolution@0.1.0
rule-evaluation@0.1.0
review-management@0.1.0
approval-decision@0.1.0
authorization-assessment@0.1.0
```

### CapabilityCompositionPort

```text
visual-direction-composition@0.1.0
layout-composition@0.1.0
design-strategy-composition@0.1.0
interaction-composition@0.1.0
```

### ProductSurfacePort

```text
no accepted active contracts
```

The family is retained in the taxonomy, but no contract is created solely for symmetry.

## 3. Active dedicated specification migration

| Source | Decision | Canonical result |
|---|---|---|
| `AgentRuntimePort` | RENAME/NARROW/MIGRATE | `agent-runtime` |
| `WorkflowOrchestrationPort` | RENAME/NARROW/MIGRATE | `workflow-coordination` |
| `ExecutionRunPort` | RENAME/MIGRATE | `execution-run-management` |
| `ContextManagementPort` | RENAME/MIGRATE | `context-resolution` |
| `SkillManagementPort` | RENAME/MIGRATE | `skill-resolution` |
| `RuleManagementPort` | SPLIT/MIGRATE | `rule-resolution` + `rule-evaluation` |
| `ReviewApprovalPort` | SPLIT/MIGRATE | review + approval decision + authorization assessment |
| `ToolIntegrationPort` | RETIRE UMBRELLA | narrower candidates version independently when evidenced |

The combined `ReviewApprovalPort` has no compatibility alias. One alias cannot safely resolve to three independently versioned contracts.

The legacy name `workflow-orchestration` is a one-to-one migration alias for the narrower `workflow-coordination` boundary only. It does not authorize workflow-engine execution or introduce a `WorkflowRun` lifecycle.

`ToolIntegrationPort` has no alias or replacement god port. Its former gateway, API, authentication, execution, registry, permission, review, and approval concerns are independently owned.

## 4. Active capability-composition migration

| Legacy skill contract | Canonical port |
|---|---|
| `design-visual` | `visual-direction-composition` |
| `design-layout` | `layout-composition` |
| `design-strategy` | `design-strategy-composition` |
| `design-interaction` | `interaction-composition` |

Legacy `skill_contract.type: port` artifacts remain active for executable consumers during migration. Their first-class port contracts use `compatibility.legacy_contract_refs` to preserve traceability without claiming that registration proves adapter conformance.

Capability-composition ports select and synthesize reusable methods. They are not provider integrations, final implementations, review authorities, or product-acceptance records.

## 5. General documented examples

| Current name | Final classification |
|---|---|
| `ModelInferencePort` | MIGRATED to `model-inference` |
| `CodeExecutionPort` | SPLIT/NARROW to `code-operation-execution` + external ExecutionRun management |
| `DatabasePort` | MIGRATED to `database` |
| `DesignReviewPort` | RECLASSIFY as review capability by default |
| `WebAppPort` | RETIRE as one boundary; use narrower ports and framework/product bindings |
| `EvaluationPort` | RECLASSIFY generic evaluation; DEFER scoped execution port pending evidence |
| `DesignGenerationPort` | SPLIT/RECLASSIFY; DEFER rendering/product-surface contracts pending evidence |
| `KnowledgeRetrievalPort` | DEFER candidate |
| `RepositoryPort` | DEFER candidate |
| `FileSystemPort` | DEFER candidate |
| `BrowserResearchPort` | DEFER candidate |
| `StoragePort` | DEFER candidate |
| `PublishingPort` | DEFER product-surface/integration candidate |
| `ObservabilityPort` | DEFER candidate |

These general names were examples, not accepted active machine contracts. Their classification is complete in `port-inventory.yaml`; future acceptance requires separate ownership, consumer, compatibility, and evidence review.

## 6. Runtime and workflow non-collapses

### Agent runtime

```text
existing ExecutionRun
+ Agent
+ RuntimeEnvironment
+ CapacityAssessment
+ AuthorizationAssessment
+ AdapterBinding
→ start or control a bounded runtime instance
→ emit attributable runtime observations
```

Mandatory exclusions:

```text
ExecutionStatus ownership
model inference
tool execution
workflow coordination
review
approval
completion
product acceptance
```

A runtime start request cannot create `running`; only an actual host observation plus the owning ExecutionRun transition can.

### Workflow coordination

```text
WorkflowDefinition
+ trigger
+ ContextPack
+ external GateResult, ExecutionRun, ReviewResult, and Approval references
→ phase and transition selection
→ handoff records
→ exit-condition results
```

The canonical domain model defines `WorkflowDefinition` and `ExecutionRun`, but not a separate `WorkflowRun` aggregate or status family. Concrete workflow-engine scheduling, transport, provider state, start, pause, resume, retry, and cancellation remain future integration or adapter concerns.

## 7. Code and database boundaries

```text
actual code operation
≠ generated plan or model output
≠ ExecutionStatus
≠ architecture decision
≠ review
≠ approval
≠ completion or delivery
```

`code-operation-execution` requires explicit operation, repository revision, adapter binding, and authorization references and returns attributable changed artifacts and command results.

```text
database operation result
≠ canonical domain meaning
≠ aggregate authority
≠ product data policy
≠ approval or product acceptance
```

`database` preserves query, mutation, transaction, migration, schema, rollback, and failure evidence while keeping domain ownership external.

## 8. Tool-integration subtype candidates

The retired umbrella formerly listed:

```text
MCPGatewayPort
APIConnectorPort
AuthBrokerPort
ToolExecutionPort
ToolRegistryPort
```

Each remains `DEFER` until it has a real consumer, coherent operations, accepted mutation and authorization semantics, replaceable adapter evidence, and a stable version path.

Required distinction:

```text
external OAuth or tool permission
≠ Native AI Engineering authority
≠ review
≠ approval
≠ AuthorizationAssessment
≠ actual execution
```

See [`tool-integration-port.md`](tool-integration-port.md) for migration guidance.

## 9. Product-surface status

Candidate names include assistant, content, creative rendering, media, learning, template, publishing, and product output.

Final decision for issue `#7`:

```text
DEFER
```

No `ProductSurfacePort` contract should be created without a proven reusable consumer boundary, source artifact, semantic owner, compatibility path, and separation from provider integration, delivery authorization, and product acceptance.

## 10. Adapter reference compatibility

A port adapter reference declares:

```yaml
port_adapter_reference:
  adapter_id: example-adapter
  port_id: model-inference
  port_path: contracts/ports/integration/model-inference.port.yaml
  port_version: ^0.1.0
```

Validate with:

```bash
python3 scripts/validate-port-adapter-reference.py <reference.yaml>
```

The validator checks stable ID, canonical path, and compatible exact, caret, or tilde version pin. This proves intended compatibility only, not implementation, runtime behavior, review, approval, completion, or product acceptance.

## 11. Machine authority and documentation

```text
contracts/ports/**/*.port.yaml
→ canonical machine semantics

docs/port-inventory.yaml
→ executable discovery and migration classification

docs/port-retention-matrix.md
→ human-readable decision rationale

legacy docs/*-port.md
→ navigation and migration records only
```

The inventory regression verifies all eight dedicated source documents and all `skill_contract.type: port` artifacts. Migrated entries must point to existing first-class contracts; retired, reclassified, and deferred entries require explicit rationale.

## 12. Downstream ownership

Issue `#7` does not implement provider adapters or build downstream registries.

Known legacy downstream declarations are migration evidence and follow-up work:

```text
ai-native-skills issue #26
ai-native-fw adapter manifests and registry
product-specific bindings
```

They must adopt stable port ID, path, and version references only after the relevant core contract is accepted. Their static presence is not a blocker to this core taxonomy issue and does not prove conformance.

## 13. Final status

```text
canonical kinds defined: yes
active schema and semantic validator: yes
active file-backed source inventory complete: yes
dedicated port documents resolved: 8 of 8
contract-declared composition ports migrated: 4 of 4
first-class contracts: 17
adapter path/version compatibility fixture: yes
manifest registration and checksum generation: yes
legacy Markdown competing authority removed: yes
tool-integration umbrella retired: yes
product-surface candidate family classified: yes, deferred
provider adapters implemented: out of scope
downstream registries migrated: follow-up owner work
ready for issue acceptance: yes, subject to final CI and review
```
