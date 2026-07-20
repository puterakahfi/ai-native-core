# Native AI Engineering Port Taxonomy

Status: Canonical

Canonical domain meanings: [`domain-model/README.md`](domain-model/README.md)

Machine contracts: [`../contracts/ports/`](../contracts/ports/)

Executable inventory: [`port-inventory.yaml`](port-inventory.yaml)

Migration decisions: [`port-retention-matrix.md`](port-retention-matrix.md)

Discovery history: [`port-taxonomy-discovery.md`](port-taxonomy-discovery.md)

## 1. Canonical relationship

```text
DomainCapability
→ stable ability required by the domain

Port
→ abstract boundary through which a consumer requests that ability

Contract
→ stable governed agreement for the boundary

Adapter
→ replaceable implementation or translation

AdapterBinding
→ selected adapter for a runtime, provider, framework, or product context

ExecutionRun
→ actual bounded execution attempt
```

Therefore:

```text
capability ≠ port
port ≠ contract
contract ≠ adapter
adapter ≠ binding
binding ≠ execution
```

The shorthand `Port = capability contract` is retired.

## 2. Canonical port kinds

### IntegrationPort

Boundary from a core, application, runtime, method, or product context to an external provider, infrastructure surface, persistence system, protocol, framework service, tool, repository, or external application.

Accepted contracts:

```text
ModelInferencePort
CodeOperationExecutionPort
DatabasePort
```

Integration ports normalize external semantics without allowing providers, SDKs, storage schemas, credentials, or technical permissions to redefine upstream domain meaning or authority.

### ControlPort

Boundary for coordinating, resolving, assessing, recording, or controlling domain work without becoming the external execution provider or acquiring another context's aggregate or authority.

Accepted contracts:

```text
AgentRuntimePort
WorkflowCoordinationPort
ExecutionRunManagementPort
ContextResolutionPort
SkillResolutionPort
RuleResolutionPort
RuleEvaluationPort
ReviewManagementPort
ApprovalDecisionPort
AuthorizationAssessmentPort
```

A control port may coordinate a canonical aggregate, workflow definition, runtime request, rule, review, or decision process. It does not become the aggregate, provider, review method, authority source, execution provider, completion owner, or product-acceptance owner.

### ProductSurfacePort

Boundary exposing a reusable product-owned capability, interaction, output, rendering, delivery, assistant, content, media, or publication surface.

```text
accepted active contracts: none
```

Assistant, content, creative-rendering, media, learning, template, publishing, and product-output names remain deferred. No ProductSurfacePort is accepted merely to populate the taxonomy; a real reusable consumer boundary, semantic owner, compatibility path, and separation from provider integration, delivery authorization, and product acceptance must be demonstrated first.

### CapabilityCompositionPort

Boundary selecting, ordering, routing, and synthesizing specialist capabilities behind one stable method-facing facade.

Accepted contracts:

```text
VisualDirectionCompositionPort
LayoutCompositionPort
DesignStrategyCompositionPort
InteractionCompositionPort
```

Composition owns concern selection, method routing, synthesis, handoff, and verification planning. It does not own provider integration, every specialist method, final implementation, review authority, release authorization, or product acceptance.

## 3. Direction

Port kind and communication direction are independent.

```text
inbound
→ a consumer drives a capability owned by the semantic context

outbound
→ the semantic context requests capability from another boundary

bidirectional
→ the agreement includes commands and observations in both directions
```

Direction does not imply authority, mutation permission, lifecycle ownership, or adapter technology.

## 4. Ownership

Every first-class port declares:

```text
semantic_owner_context
→ owns capability meaning and invariants

binding_owner_context
→ Integration & Binding owns adapter selection and compatibility

consumer_contexts
→ contexts allowed to request or observe the boundary
```

```text
capability
≠ permission
≠ authority
```

Provider access, credentials, tool availability, runtime control, or technical permission cannot create Native AI Engineering authority.

## 5. Contract identity and structure

Canonical paths:

```text
contracts/ports/integration/<id>.port.yaml
contracts/ports/control/<id>.port.yaml
contracts/ports/product-surface/<id>.port.yaml
contracts/ports/capability-composition/<id>.port.yaml
```

Identity rules:

```text
ID and filename use kebab-case
ID omits the redundant -port suffix
capability and machine fields use snake_case
display type uses PascalCase plus Port
version follows semantic compatibility policy
```

Every `port_contract` declares:

```text
identity, kind, version, and capability
direction and context ownership
purpose
owned, delegated, and excluded boundaries
requests, responses, events, and streams
structured failures and partial-result policy
typed state transitions
authorization boundary
idempotency
observability and sensitive fields
adapter ID/path/version requirements
compatibility, aliases, supersession, and legacy references
quality gates
```

Schema authority:

```text
schemas/port-contract.schema.yaml
```

Validate:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
python3 -m unittest discover -s tests -p 'test_port_inventory.py' -v
```

## 6. Typed lifecycle rule

One port contract may own transitions from at most one canonical status family.

```text
ExecutionRunManagementPort → ExecutionStatus
ReviewManagementPort       → ReviewDisposition
ApprovalDecisionPort       → ApprovalStatus
```

`AgentRuntimePort`, `WorkflowCoordinationPort`, `AuthorizationAssessmentPort`, IntegrationPorts, and CapabilityCompositionPorts own no competing status family.

```text
runtime control outcome
≠ ExecutionStatus

workflow transition selection
≠ WorkflowRun status

AuthorizationAssessment
≠ ApprovalStatus

UI state representation
≠ canonical domain status
```

Ports may reference results from other families, but they do not mutate those states unless that family is their explicit owned boundary.

## 7. Runtime and workflow boundaries

### Agent runtime

```text
ExecutionRun
+ CapacityAssessment
+ AuthorizationAssessment
+ Agent
+ RuntimeEnvironment
+ AdapterBinding
→ AgentRuntimePort start/control request
→ attributable runtime observations
→ external ExecutionRun recording
```

A request, plan, model response, or runtime-provider checkpoint cannot become `running` or `succeeded` without actual host evidence and the owning ExecutionRun transition.

### Workflow coordination

```text
WorkflowDefinition
+ trigger
+ ContextPack
+ external GateResult, ExecutionRun, ReviewResult, and Approval references
→ WorkflowCoordinationPort
→ phase and transition selection
→ handoff records
→ exit-condition results
```

The canonical domain model defines `WorkflowDefinition` and `ExecutionRun`, not a separate `WorkflowRun` aggregate or status family. Concrete workflow-engine scheduling, transport, provider state, start, pause, resume, retry, and cancellation remain external integration or adapter concerns.

## 8. Review, evaluation, and authority

```text
GateOutcome
≠ EvaluationResult
≠ ReviewDisposition
≠ ApprovalStatus
≠ AuthorizationAssessment
≠ ExecutionStatus
```

```text
RuleResolutionPort
→ resolves applicable governed rules

RuleEvaluationPort
→ evaluates a subject against resolved rules

ReviewManagementPort
→ preserves review requests, findings, results, and disposition

ApprovalDecisionPort
→ records authority-bearing approval decisions

AuthorizationAssessmentPort
→ assesses whether one concrete action may proceed now
```

Rule availability does not prove conformance. A passing evaluation or positive review is not approval. Approval alone does not prove an action is currently authorized, executed, completed, delivered, or accepted.

The combined name `ReviewApprovalPort` has no canonical alias because preserving it would recreate the retired semantic collapse.

## 9. Integration boundary locks

### Code operations

```text
actual code operation
≠ generated plan or model output
≠ ExecutionStatus
≠ architecture decision
≠ review
≠ approval
≠ completion or delivery
```

`CodeOperationExecutionPort` returns attributable changed artifacts, commands, tests, failures, conflicts, and limitations. ExecutionRun management, architecture, review, approval, completion, delivery, and product acceptance remain external.

### Database operations

```text
database operation result
≠ canonical domain meaning
≠ aggregate authority
≠ product data policy
≠ approval or product acceptance
```

`DatabasePort` preserves query, mutation, transaction, migration, schema, rollback, conflict, and failure evidence while keeping domain ownership external.

### Retired tool-integration umbrella

```text
ToolIntegrationPort
→ retired as one umbrella contract
```

Gateway translation, direct APIs, authentication, external operation execution, tool discovery, permission, review, and approval are independently owned concerns. Historical subtype names remain deferred until separately evidenced.

```text
external OAuth or tool permission
≠ Native AI Engineering authority
≠ review
≠ approval
≠ AuthorizationAssessment
≠ actual execution
```

## 10. Capability-composition boundaries

```text
DesignStrategyCompositionPort
→ experience, information, collection, content, copy, and conditional conversion strategy

LayoutCompositionPort
→ macrostructure, component roles, adaptive substitutions, and responsive behavior

VisualDirectionCompositionPort
→ visual concerns, specialist selection, synthesis, and verification planning

InteractionCompositionPort
→ interaction patterns, UI states, accessibility behavior, recovery, and verification planning
```

Each first-class composition contract links to its legacy `skill_contract.type: port` source through `compatibility.legacy_contract_refs`. Static registration does not prove an executable skill conforms or that the composed output is accepted.

## 11. Adapter references

A compatible adapter declaration references:

```text
stable port ID
canonical contract path
compatible version pin
```

Example:

```yaml
port_adapter_reference:
  adapter_id: example-adapter
  port_id: model-inference
  port_path: contracts/ports/integration/model-inference.port.yaml
  port_version: ^0.1.0
```

Validate:

```bash
python3 scripts/validate-port-adapter-reference.py <reference.yaml>
```

Supported pin semantics include exact, caret, and tilde ranges. For a `0.x` contract, a caret pin remains within the same minor compatibility line.

A valid reference proves intended identity and version compatibility only. It does not prove adapter implementation, conformance, runtime behavior, authority, review, approval, completion, or product acceptance.

## 12. Inventory and migration policy

`docs/port-inventory.yaml` is the executable classification ledger. Regression tests verify:

```text
all eight dedicated port source documents are classified
all skill_contract.type: port artifacts are discovered and classified
migrated sources point to existing first-class contracts
retired, reclassified, and deferred sources carry explicit rationale
the tool-integration umbrella remains retired
product-surface candidates remain deferred without fake contracts
```

Migration sequence:

```text
1. inventory the existing source or name
2. migrate, rename, split, reclassify, retire, or defer
3. review the semantic boundary independently
4. verify every domain object and status family is canonical
5. create a first-class contract only for an accepted boundary
6. register it in the generated manifest
7. preserve explicit legacy references where valid
8. migrate downstream adapter ID/path/version declarations in their owning repositories
9. gather conformance and runtime evidence separately
10. remove competing Markdown machine authority
```

Do not bulk-generate every name ending in `Port`. Do not invent aggregates, status families, providers, or product boundaries to make the taxonomy look complete.

## 13. Current first-class contracts

```text
IntegrationPort
  code-operation-execution@0.1.0
  database@0.1.0
  model-inference@0.1.0

ControlPort
  agent-runtime@0.1.0
  approval-decision@0.1.0
  authorization-assessment@0.1.0
  context-resolution@0.1.0
  execution-run-management@0.1.0
  review-management@0.1.0
  rule-evaluation@0.1.0
  rule-resolution@0.1.0
  skill-resolution@0.1.0
  workflow-coordination@0.1.0

CapabilityCompositionPort
  design-strategy-composition@0.1.0
  interaction-composition@0.1.0
  layout-composition@0.1.0
  visual-direction-composition@0.1.0
```

`ProductSurfacePort` remains intentionally uninstantiated.

## 14. Evidence boundary

Schema, inventory, and manifest validation prove only that an artifact is structurally valid, aligned to its identity and kind, explicitly classified, and registered at a version and checksum.

They do not prove:

```text
an adapter exists
an adapter conforms
the port was exercised
runtime behavior is correct
authority or approval exists
completion or delivery occurred
a product accepted the result
```
