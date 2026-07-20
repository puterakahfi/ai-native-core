# Native AI Engineering Port Taxonomy

Status: Candidate canonical taxonomy under issue `#7`

Canonical domain meanings: [`domain-model/README.md`](domain-model/README.md)

Migration decisions: [`port-retention-matrix.md`](port-retention-matrix.md)

Discovery record: [`port-taxonomy-discovery.md`](port-taxonomy-discovery.md)

Machine-readable contracts: [`../contracts/ports/`](../contracts/ports/)

---

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
→ actual performed work
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

---

## 2. Port kinds

### IntegrationPort

Boundary to an external provider, infrastructure surface, persistence system, protocol, framework service, or external application.

Examples include model inference, repositories, knowledge retrieval, file systems, browsing, databases, object storage, publishing, observability, tool gateways, APIs, external authentication, and provider-specific workflow engines.

Integration ports translate external semantics without allowing provider models to redefine upstream domain meaning.

### ControlPort

Boundary for coordinating, resolving, assessing, recording, or controlling domain lifecycle operations without implementing the external target or acquiring another context's authority.

Current examples:

```text
ExecutionRunManagementPort
AgentRuntimePort
WorkflowCoordinationPort
ContextResolutionPort
SkillResolutionPort
RuleResolutionPort
RuleEvaluationPort
ReviewManagementPort
ApprovalDecisionPort
AuthorizationAssessmentPort
```

A control port may coordinate an aggregate, runtime control request, workflow definition, or decision process. It does not become the aggregate, runtime provider, review method, authority source, execution provider, or product acceptance owner.

### ProductSurfacePort

Boundary exposing a product-owned capability, interaction, or output to a consumer surface.

Candidate examples include assistant response, creative rendering, and product output. No ProductSurfacePort is accepted merely to populate the taxonomy. A real reusable consumer boundary and compatibility path must be demonstrated first.

### CapabilityCompositionPort

Boundary composing specialist capabilities behind one stable method-facing facade.

Current example:

```text
VisualDirectionCompositionPort
```

Future candidates include layout, design-strategy, and interaction composition. Composition owns routing and synthesis boundaries, not every specialist method, runtime execution, or proof of correct application.

---

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

---

## 4. Ownership

Every first-class port contract declares:

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

---

## 5. Contract identity

```text
contracts/ports/integration/<id>.port.yaml
contracts/ports/control/<id>.port.yaml
contracts/ports/product-surface/<id>.port.yaml
contracts/ports/capability-composition/<id>.port.yaml
```

Rules:

```text
ID and filename use kebab-case
ID omits the redundant "-port" suffix
capability and machine fields use snake_case
display type uses PascalCase plus Port
version follows semantic compatibility policy
```

---

## 6. Required dimensions

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

Schema and validation:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
```

Schema authority:

```text
schemas/port-contract.schema.yaml
```

---

## 7. Typed lifecycle rule

One port contract may own transitions from at most one canonical status family.

```text
ExecutionRunManagementPort → ExecutionStatus
ReviewManagementPort       → ReviewDisposition
ApprovalDecisionPort       → ApprovalStatus
```

`AgentRuntimePort`, `WorkflowCoordinationPort`, and `AuthorizationAssessmentPort` own no competing status family.

```text
runtime control outcome
≠ ExecutionStatus

workflow transition selection
≠ WorkflowRun status

AuthorizationAssessment
≠ ApprovalStatus
```

Invalid collapse:

```text
queued
→ running
→ completed
→ needs_review
→ approved
```

Ports may reference results from other families, but they do not mutate those states unless that family is their explicit owned boundary.

---

## 8. Runtime and workflow rule

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

Agent runtime control does not own `ExecutionStatus`. A request, plan, model response, or runtime-provider checkpoint cannot become `running` or `succeeded` without the owning ExecutionRun transition and evidence.

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

The canonical domain model currently defines `WorkflowDefinition` and `ExecutionRun`, not a separate `WorkflowRun` aggregate or status family. A port contract may not introduce that lifecycle without governed upstream domain evolution.

Concrete workflow-engine start, pause, resume, retry, cancellation, and provider-state semantics remain external integration concerns.

---

## 9. Review, evaluation, and authority

```text
GateOutcome
≠ EvaluationResult
≠ ReviewDisposition
≠ ApprovalStatus
≠ AuthorizationAssessment
≠ ExecutionStatus
```

Required boundaries:

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

Rule availability does not prove conformance. A passing evaluation or positive review is not approval. Approval alone does not prove the action is currently authorized, executed, completed, delivered, or accepted.

The legacy combined name `ReviewApprovalPort` has no canonical alias because preserving it would recreate the retired semantic collapse.

---

## 10. Adapter references

A compatible adapter declaration references the port by:

```text
stable port ID
canonical contract path
compatible version pin
```

Validate a declaration with:

```bash
python3 scripts/validate-port-adapter-reference.py <reference.yaml>
```

Supported pin semantics include exact, caret, and tilde ranges. For a `0.x` contract, a caret pin remains within the same minor compatibility line.

A valid reference proves intended identity and version compatibility only. It does not prove adapter conformance, runtime behavior, or product acceptance.

---

## 11. Current first-class contracts

```text
IntegrationPort
  model-inference@0.1.0

ControlPort
  execution-run-management@0.1.0
  agent-runtime@0.1.0
  workflow-coordination@0.1.0
  context-resolution@0.1.0
  skill-resolution@0.1.0
  rule-resolution@0.1.0
  rule-evaluation@0.1.0
  review-management@0.1.0
  approval-decision@0.1.0
  authorization-assessment@0.1.0

CapabilityCompositionPort
  visual-direction-composition@0.1.0
```

ProductSurfacePort remains intentionally uninstantiated.

---

## 12. Migration policy

```text
1. classify the existing name
2. retain, rename, split, reclassify, retire, or defer
3. review the semantic boundary independently
4. verify every referenced domain object and status family is canonical
5. create a first-class contract
6. register it in the generated manifest
7. preserve explicit legacy references where valid
8. migrate adapter ID/path/version declarations
9. gather conformance and runtime evidence
10. retire competing Markdown authority only after consumers migrate
```

Do not bulk-generate every name ending in `Port` from one generic template. Do not invent an aggregate or status family inside a port merely because an adapter exposes one.

---

## 13. Evidence boundary

Schema and manifest validation prove only that the artifact is structurally valid, aligned to its ID/path/kind, declares required boundary dimensions, and is registered at a version and checksum.

They do not prove:

```text
an adapter exists
an adapter conforms
the port was exercised
runtime behavior is correct
approval exists
a product accepted the result
```
