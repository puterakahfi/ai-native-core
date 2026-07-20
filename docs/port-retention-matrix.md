# Native AI Engineering Port Retention And Alias Matrix

Status: Candidate migration record for issue `#7`

Branch: `7-formalize-port-taxonomy-and-first-class-port-contracts`

Canonical domain authority: [`domain-model/README.md`](domain-model/README.md)

Discovery input: [`port-taxonomy-discovery.md`](port-taxonomy-discovery.md)

This record decides whether currently documented or contract-declared port names should be retained, renamed, split, reclassified, or retired before bulk migration into first-class `port_contract` artifacts.

It is not yet the final canonical taxonomy. Machine authority begins only with accepted contracts under `contracts/ports/`.

---

## 1. Decision rules

A first-class port must satisfy all of these conditions:

```text
a consumer context requires a capability through an explicit boundary;
the capability can have more than one replaceable implementation or translation;
the boundary owns request, response, failure, compatibility, and observability semantics;
the port does not merely rename a workflow, skill, framework, aggregate, status, or product feature;
the port has one semantic owner and one Integration & Binding owner;
the port can be versioned without importing provider, runtime, or product implementation details.
```

A name is not retained as a port merely because it ends with `Port`.

### Decision values

```text
RETAIN
→ keep the semantic boundary and migrate it into a first-class port contract;

RENAME
→ keep the boundary but replace an ambiguous or aggregate-colliding name;

SPLIT
→ the existing name owns multiple independent boundaries or status families;

RECLASSIFY
→ the concept is useful but belongs to a contract, skill, workflow, adapter,
  binding, aggregate, policy, or product surface rather than a port;

RETIRE
→ the name does not represent one coherent reusable boundary;

DEFER
→ evidence is insufficient to accept a first-class port.
```

---

## 2. Canonical port kinds under evaluation

| Kind | Semantic responsibility | Typical examples |
|---|---|---|
| `integration_port` | translates or requests capability from an external system, provider, framework, persistence surface, or infrastructure boundary | model inference, repository, storage, external tools |
| `control_port` | coordinates or records lifecycle operations without owning the implementation target or another context's decisions | runtime orchestration, execution-run management, context resolution |
| `product_surface_port` | exposes a product-owned capability or output boundary to a consumer surface | assistant response, creative rendering, product output |
| `capability_composition_port` | composes reusable specialist capabilities behind one stable method-facing boundary | visual direction, layout, design strategy, interaction composition |

Port kind and communication direction are independent:

```text
kind: integration_port
direction: outbound

kind: product_surface_port
direction: inbound

kind: control_port
direction: bidirectional
```

---

## 3. Naming and identity rules

Machine identity:

```text
contracts/ports/<kind-directory>/<id>.port.yaml

id:
  kebab-case;
  omits the redundant "-port" suffix;

capability:
  snake_case;

display type:
  PascalCase identifier plus "Port".
```

Examples:

```text
id: model-inference
display type: ModelInferencePort

id: execution-run-management
display type: ExecutionRunManagementPort
```

A legacy name is recorded in one of two ways:

```text
compatibility.aliases
→ prior port identity that resolves to the same semantic boundary;

compatibility.legacy_contract_refs
→ an existing skill, runtime, or other contract that remains active during migration
  but does not become the canonical port contract.
```

Legacy skill IDs must not be copied blindly into port aliases when doing so would create ambiguous cross-family identity.

---

## 4. General port list decisions

| Current name | Decision | Candidate canonical boundary | Kind | Reason |
|---|---|---|---|---|
| `ModelInferencePort` | RETAIN | `model-inference` | integration | coherent provider-neutral inference boundary |
| `CodeExecutionPort` | SPLIT | code-operation execution plus execution-run management | control + integration/runtime binding | currently mixes actual code execution, run records, testing, risk, and review |
| `DesignGenerationPort` | SPLIT | visual direction composition plus creative rendering/output | composition + product surface | reasoning, generation, rendering, and delivery are independent |
| `DesignReviewPort` | RECLASSIFY | design-review capability agreement by default | skill/capability contract | review method is not automatically a replaceable integration boundary |
| `KnowledgeRetrievalPort` | RETAIN | `knowledge-retrieval` | integration | coherent retrieval boundary, consumed by context management |
| `RepositoryPort` | RETAIN | `repository` | integration | coherent repository-provider boundary |
| `FileSystemPort` | RETAIN | `file-system` | integration | coherent host file-system boundary when distinct from repository semantics |
| `BrowserResearchPort` | RETAIN | `browser-research` | integration | coherent external browsing and source-retrieval boundary |
| `WebAppPort` | RETIRE | framework and product bindings plus narrower ports | binding/product | routes, pages, components, server actions, APIs, state, and rendering are not one capability |
| `DatabasePort` | RETAIN | `database` | integration | coherent structured-persistence boundary |
| `StoragePort` | RETAIN | `object-storage` or `storage` | integration | coherent file/media storage boundary; final name requires inventory review |
| `PublishingPort` | RETAIN | `publishing` | integration | coherent external mutation boundary with policy-dependent authorization |
| `EvaluationPort` | SPLIT | evaluation execution, gate evaluation, review, and decision boundaries | control + capability agreements | current output values collapse evaluation, review, and approval |
| `ObservabilityPort` | RETAIN | `observability` | integration | coherent telemetry export and query boundary |

### Confirmed representative

```text
ModelInferencePort
→ contracts/ports/integration/model-inference.port.yaml
```

---

## 5. Dedicated control-plane port decisions

| Current name | Decision | Candidate canonical boundary | Kind | Required correction |
|---|---|---|---|---|
| `AgentRuntimePort` | RETAIN | `agent-runtime` | control | use canonical ExecutionStatus and external authorization references |
| `WorkflowOrchestrationPort` | RETAIN | `workflow-orchestration` | control | WorkflowDefinition, WorkflowRun, and ExecutionRun remain separate |
| `ExecutionRunPort` | RENAME | `execution-run-management` | control | avoid collision with the `ExecutionRun` aggregate and remove review/approval statuses |
| `ReviewApprovalPort` | SPLIT | review management, approval decision, authorization assessment | control | ReviewDisposition, ApprovalStatus, and authorization are independent |
| `ContextManagementPort` | RENAME | `context-resolution` or `context-pack-management` | control | clarify whether it resolves sources, assembles packs, or owns both operations |
| `SkillManagementPort` | RENAME | `skill-resolution` | control | discovery/resolution is distinct from skill definition and application |
| `RuleManagementPort` | RENAME | `rule-resolution-and-evaluation` | control | rule storage, rule applicability, evaluation, and authority must not collapse |
| `ToolIntegrationPort` | RETIRE AS UMBRELLA PORT | integration taxonomy and narrower contracts | integration facade | registry, authentication, execution, and connector semantics version independently |

### Confirmed representative

```text
ExecutionRunPort
→ ExecutionRunManagementPort
→ contracts/ports/control/execution-run-management.port.yaml
```

The old lifecycle:

```text
queued → running → completed → needs_review → approved
```

is rejected because it crosses:

```text
ExecutionStatus
→ ReviewDisposition
→ ApprovalStatus
```

The representative contract owns only canonical `ExecutionStatus` transitions and carries review, approval, completion, and delivery as external references.

---

## 6. Tool integration subtype decisions

| Current name | Decision | Candidate kind | Notes |
|---|---|---|---|
| `MCPGatewayPort` | RETAIN | integration | protocol/gateway translation boundary |
| `APIConnectorPort` | RETAIN | integration | direct external API translation boundary |
| `AuthBrokerPort` | RETAIN | integration | external authorization flow and token-management boundary; does not own domain authority |
| `ToolExecutionPort` | RETAIN WITH NARROWING | integration | executes authorized external operations; does not own approval or workflow state |
| `ToolRegistryPort` | RETAIN | integration | lists available external tool capabilities and operation schemas |

The following distinction is mandatory:

```text
external OAuth authorization
≠ Native AI Engineering authority
≠ approval
≠ authorization assessment for a domain action.
```

---

## 7. Capability-composition decisions

The current artifacts are registered under `contracts/skills/design/` with:

```yaml
skill_contract:
  type: port
```

This proves active composition behavior but not a first-class port artifact family.

| Current skill-contract ID | Decision | Candidate canonical port | Migration rule |
|---|---|---|---|
| `design-visual` | RENAME/MIGRATE | `visual-direction-composition` | keep legacy skill contract active until adapter migration |
| `design-layout` | RENAME/MIGRATE | `layout-composition` | preserve ordered specialist adapter behavior |
| `design-strategy` | RENAME/MIGRATE | `design-strategy-composition` | preserve conditional capability selection |
| `design-interaction` | RENAME/MIGRATE | `interaction-composition` | preserve behavior and accessibility ownership boundaries |

### Confirmed representative

```text
design-visual skill contract
→ legacy executable/capability agreement during migration

visual-direction-composition port contract
→ canonical composition boundary
```

The port contract references the legacy artifact through:

```yaml
compatibility:
  legacy_contract_refs:
    - contracts/skills/design/design-visual.contract.yaml
```

This is not a claim that the legacy skill contract already implements the new first-class port contract. Adapter migration and evidence remain downstream work.

---

## 8. Review, evaluation, approval, and authorization split

The following ports or capabilities must remain independently versionable:

```text
ReviewManagementPort
→ creates review requests and preserves ReviewResult / ReviewDisposition;

EvaluationExecutionPort
→ executes an evaluation method against declared criteria and evidence;

ApprovalDecisionPort
→ records authority-bearing ApprovalStatus and decision provenance;

AuthorizationAssessmentPort
→ evaluates whether one concrete action may proceed now.
```

No contract may expose one generic response such as:

```text
approved
approved_with_comments
needs_revision
rejected
```

without naming the semantic family and authority boundary.

A positive evaluation or completed review is not an approval.

---

## 9. Product-surface candidate status

Issue `#7` mentions product-surface examples such as:

```text
assistant;
content;
creative rendering;
media;
learning;
template;
product output.
```

No first-class source artifacts for these names have yet been confirmed in the inspected repository inventory.

Decision:

```text
DEFER
```

A ProductSurfacePort may be created only when a real reusable consumer boundary, active document or contract, and compatibility path are identified.

Do not create product-surface contracts solely to make all four taxonomy kinds appear populated.

---

## 10. Representative contract set

This slice introduces three contracts:

```text
IntegrationPort
→ model-inference@0.1.0

ControlPort
→ execution-run-management@0.1.0

CapabilityCompositionPort
→ visual-direction-composition@0.1.0
```

A ProductSurfacePort is intentionally absent until inventory proves a universal boundary.

Each representative must prove:

```text
schema validation;
ID and filename alignment;
kind and directory alignment;
one semantic owner;
Integration & Binding ownership;
request and response semantics;
structured failures;
typed state-family ownership;
authorization boundaries;
idempotency;
observability;
adapter ID/path/version references;
breaking-change semantics;
manifest registration.
```

---

## 11. Migration order

```text
1. accept taxonomy and machine shape;
2. validate three representative contracts;
3. prove manifest and CI support;
4. complete inventory against all active docs and contracts;
5. migrate retained integration and control ports;
6. migrate composition facades with explicit legacy references;
7. introduce product-surface ports only from confirmed reusable boundaries;
8. update adapter declarations and compatibility checks;
9. retire or redirect Markdown sources that compete with accepted contracts.
```

Bulk conversion before representative validation is prohibited.

---

## 12. Remaining decisions

1. Whether `StoragePort` should be named `storage` or `object-storage`.
2. Whether context resolution and context-pack persistence require separate ports.
3. Whether review management is a port or remains an application use case over review contracts.
4. Whether approval recording and authorization assessment need separate first-class ports.
5. Whether code execution is one control port plus runtime bindings or multiple operation-specific ports.
6. Which product-surface boundaries have active reusable consumers.
7. How legacy `skill_contract.type: port` artifacts declare migration without creating duplicate authority.
8. Whether the eventual unified schema in issue `#8` absorbs or references the dedicated port schema.

---

## 13. Acceptance status for this record

```text
canonical domain terminology consumed: yes;
legacy port inventory partially classified: yes;
representative stable names selected: yes;
all active ports inventoried: no;
product-surface source confirmed: no;
bulk migration authorized: no;
taxonomy ready for final acceptance: no.
```
