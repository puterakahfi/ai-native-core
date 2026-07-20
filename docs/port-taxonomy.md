# Native AI Engineering Port Taxonomy

Status: Candidate taxonomy under issue `#7`

Canonical domain meanings: [`domain-model/README.md`](domain-model/README.md)

Retention and migration decisions: [`port-retention-matrix.md`](port-retention-matrix.md)

Discovery record: [`port-taxonomy-discovery.md`](port-taxonomy-discovery.md)

Machine-readable representative contracts: [`../contracts/ports/`](../contracts/ports/)

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

Examples:

```text
ModelInferencePort
RepositoryPort
KnowledgeRetrievalPort
FileSystemPort
BrowserResearchPort
DatabasePort
StoragePort
PublishingPort
ObservabilityPort
MCPGatewayPort
APIConnectorPort
AuthBrokerPort
ToolExecutionPort
ToolRegistryPort
```

Integration ports translate external semantics without allowing provider models to redefine upstream domain meaning.

### ControlPort

Boundary for coordinating, routing, or recording lifecycle operations.

Examples:

```text
AgentRuntimePort
WorkflowOrchestrationPort
ExecutionRunManagementPort
ContextResolutionPort
SkillResolutionPort
RuleResolutionPort
ReviewManagementPort
AuthorizationAssessmentPort
```

A control port does not acquire the aggregate, review, approval, or product authority of the context it coordinates.

### ProductSurfacePort

Boundary exposing a product-owned capability, interaction, or output to a consumer surface.

Examples remain candidate-only until active reusable source boundaries are confirmed:

```text
AssistantPort
CreativeRenderingPort
ProductOutputPort
```

Do not create a product-surface port solely to mirror a UI page, component, provider endpoint, or private product feature.

### CapabilityCompositionPort

Boundary composing specialist capabilities behind one stable method-facing facade.

Examples:

```text
VisualDirectionCompositionPort
LayoutCompositionPort
DesignStrategyCompositionPort
InteractionCompositionPort
```

A composition port selects and coordinates capabilities. It does not become an infrastructure port, a workflow run, or proof that specialist methods were executed.

---

## 3. Direction

Port kind and direction are independent.

```text
inbound
→ external or downstream consumer drives a capability owned by the semantic context;

outbound
→ the semantic context requests capability from an external or downstream boundary;

bidirectional
→ the agreement includes commands and observations in both directions.
```

Examples:

```text
ModelInferencePort
kind: integration_port
direction: outbound

ExecutionRunManagementPort
kind: control_port
direction: bidirectional

VisualDirectionCompositionPort
kind: capability_composition_port
direction: inbound
```

---

## 4. Ownership

Every first-class port contract declares:

```text
semantic_owner_context
→ owns the capability meaning and invariants;

binding_owner_context
→ Integration & Binding, which owns adapter selection and compatibility;

consumer_contexts
→ contexts allowed to request or observe the boundary.
```

A port contract must not infer authority from technical access.

```text
capability
≠ permission
≠ authority
```

---

## 5. Contract location and identity

```text
contracts/ports/integration/<id>.port.yaml
contracts/ports/control/<id>.port.yaml
contracts/ports/product-surface/<id>.port.yaml
contracts/ports/capability-composition/<id>.port.yaml
```

Rules:

```text
ID and filename use kebab-case;
ID omits the redundant "-port" suffix;
capability and machine fields use snake_case;
display type uses PascalCase plus Port;
version follows repository compatibility policy.
```

Example:

```text
contracts/ports/control/execution-run-management.port.yaml

id: execution-run-management
display type: ExecutionRunManagementPort
```

---

## 6. Required contract dimensions

Every `port_contract` declares:

```text
identity, kind, version, and capability;
direction and context ownership;
purpose;
owned, delegated, and excluded boundary;
requests, responses, events, and streams;
structured errors and partial-result behavior;
typed state transitions;
authorization boundary;
idempotency;
observability and sensitive fields;
adapter ID/path/version reference requirements;
compatibility, aliases, supersession, and legacy references;
quality gates.
```

The canonical schema is:

```text
schemas/port-contract.schema.yaml
```

Validate with:

```bash
python3 scripts/validate-port-contracts.py
```

---

## 7. Typed lifecycle rule

One port contract may own transitions from at most one canonical status family.

Examples:

```text
ExecutionRunManagementPort
→ ExecutionStatus

ReviewManagementPort
→ ReviewDisposition

ApprovalDecisionPort
→ ApprovalStatus
```

Invalid:

```text
queued
→ running
→ completed
→ needs_review
→ approved
```

because it collapses execution, review, and approval.

Ports may reference results from other families, but they do not mutate those states unless that family is their explicit owned boundary.

---

## 8. Review and authority rule

```text
GateOutcome
≠ ReviewDisposition
≠ ApprovalStatus
≠ AuthorizationAssessment
```

A review port may preserve review findings and disposition.

An approval or decision port must preserve authority, scope, subject, conditions, and provenance.

An authorization assessment evaluates whether one concrete action may proceed now.

No positive review or passing gate becomes approval automatically.

---

## 9. Adapter contract references

A compatible adapter declaration must reference the port contract by:

```text
stable ID;
canonical path;
compatible version pin.
```

The declaration is evidence of intended compatibility, not proof of executable behavior.

Adapter conformance, runtime evidence, and product acceptance remain separate evidence layers.

---

## 10. Representative contracts

```text
IntegrationPort
→ model-inference@0.1.0

ControlPort
→ execution-run-management@0.1.0

CapabilityCompositionPort
→ visual-direction-composition@0.1.0
```

ProductSurfacePort remains uninstantiated until inventory confirms a reusable source boundary.

---

## 11. Migration policy

```text
1. classify the existing name;
2. retain, rename, split, reclassify, retire, or defer;
3. create the first-class port contract;
4. register it in the generated manifest;
5. preserve explicit legacy contract references;
6. migrate adapter declarations;
7. gather conformance and runtime evidence;
8. retire competing Markdown or legacy authority only after consumers migrate.
```

Do not bulk-convert every name ending in `Port`.

---

## 12. Evidence boundary

Schema and manifest validation prove only that:

```text
the port artifact is structurally valid;
identity and path align;
required boundary dimensions are declared;
the artifact is registered at a version and checksum.
```

They do not prove:

```text
an adapter exists;
an adapter conforms;
the port was exercised;
runtime behavior is correct;
approval exists;
a product accepted the result.
```
