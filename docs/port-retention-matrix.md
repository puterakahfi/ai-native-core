# Native AI Engineering Port Retention And Alias Matrix

Status: Candidate migration authority for issue `#7`

Canonical domain authority: [`domain-model/README.md`](domain-model/README.md)

Canonical taxonomy: [`port-taxonomy.md`](port-taxonomy.md)

Discovery record: [`port-taxonomy-discovery.md`](port-taxonomy-discovery.md)

This record classifies documented or contract-declared names before they become first-class port contracts. Machine authority belongs to accepted artifacts under `contracts/ports/`.

---

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
```

A name is not retained merely because it ends in `Port`.

Decision values:

```text
RETAIN      preserve the boundary
RENAME      preserve meaning under a clearer identity
SPLIT       separate independent boundaries or status families
RECLASSIFY  move to skill, workflow, policy, adapter, binding, aggregate, or product
RETIRE      remove an incoherent boundary name
DEFER       wait for sufficient reusable evidence
```

---

## 2. Accepted first-class contracts in this branch

| Legacy or source concept | Decision | Canonical contract | Kind |
|---|---|---|---|
| `ModelInferencePort` | RETAIN | `model-inference@0.1.0` | integration |
| `ExecutionRunPort` | RENAME | `execution-run-management@0.1.0` | control |
| `ContextManagementPort` | RENAME | `context-resolution@0.1.0` | control |
| `SkillManagementPort` | RENAME | `skill-resolution@0.1.0` | control |
| rule discovery part of `RuleManagementPort` | SPLIT | `rule-resolution@0.1.0` | control |
| rule checking part of `RuleManagementPort` | SPLIT | `rule-evaluation@0.1.0` | control |
| review part of `ReviewApprovalPort` | SPLIT | `review-management@0.1.0` | control |
| approval part of `ReviewApprovalPort` | SPLIT | `approval-decision@0.1.0` | control |
| action authorization part of `ReviewApprovalPort` | SPLIT | `authorization-assessment@0.1.0` | control |
| `design-visual` composition facade | RENAME/MIGRATE | `visual-direction-composition@0.1.0` | capability composition |

The retired combined name `ReviewApprovalPort` has no alias. One alias cannot safely resolve to three independently versioned contracts.

---

## 3. General port decisions

| Current name | Decision | Candidate boundary | Reason |
|---|---|---|---|
| `CodeExecutionPort` | SPLIT | code/tool operation integration plus execution-run management | actual operation, run record, review, risk, and approval are independent |
| `DesignGenerationPort` | SPLIT | visual composition plus rendering/product output | reasoning, generation, rendering, and delivery are independent |
| `DesignReviewPort` | RECLASSIFY by default | design-review capability agreement | a review method is not automatically an integration boundary |
| `KnowledgeRetrievalPort` | RETAIN | `knowledge-retrieval` | coherent attributable retrieval boundary |
| `RepositoryPort` | RETAIN | `repository` | coherent provider-neutral repository boundary |
| `FileSystemPort` | RETAIN | `file-system` | distinct host file-system semantics |
| `BrowserResearchPort` | RETAIN | `browser-research` | coherent attributable web retrieval boundary |
| `WebAppPort` | RETIRE | narrower ports plus framework/product bindings | routes, pages, components, APIs, state, and rendering are not one capability |
| `DatabasePort` | RETAIN | `database` | coherent structured persistence boundary |
| `StoragePort` | RENAME candidate | `object-storage` | distinguishes product object lifecycle from host files |
| `PublishingPort` | RETAIN | `publishing` | coherent external mutation boundary |
| `EvaluationPort` | SPLIT/RECLASSIFY | evaluation capability or scoped evaluation execution boundary | generic outputs formerly collapsed evaluation, review, and approval |
| `ObservabilityPort` | RETAIN | `observability` | coherent telemetry boundary |

`CodeExecutionPort` is not accepted as one god port. The retained model is:

```text
operation execution integration
+ ExecutionRunManagementPort
+ external review, approval, completion, and product acceptance
```

---

## 4. Control-plane decisions

| Current name | Decision | Canonical direction |
|---|---|---|
| `AgentRuntimePort` | RETAIN candidate | control boundary using canonical execution and authorization references |
| `WorkflowOrchestrationPort` | RETAIN candidate | WorkflowDefinition, WorkflowRun, and ExecutionRun remain separate |
| `ExecutionRunPort` | MIGRATED | `execution-run-management` |
| `ContextManagementPort` | MIGRATED | `context-resolution` |
| `SkillManagementPort` | MIGRATED | `skill-resolution` |
| `RuleManagementPort` | MIGRATED/SPLIT | `rule-resolution` + `rule-evaluation` |
| `ReviewApprovalPort` | MIGRATED/SPLIT | review + approval + authorization contracts |
| `ToolIntegrationPort` | RETIRE AS UMBRELLA CONTRACT | narrower integration contracts version independently |

---

## 5. Tool-integration subtypes

| Name | Decision | Boundary |
|---|---|---|
| `MCPGatewayPort` | RETAIN candidate | MCP protocol and gateway translation |
| `APIConnectorPort` | RETAIN candidate | direct external API translation |
| `AuthBrokerPort` | RETAIN candidate | external authentication and token lifecycle |
| `ToolExecutionPort` | RETAIN WITH NARROWING | authorized external operation execution |
| `ToolRegistryPort` | RETAIN candidate | discover external tool schemas and capabilities |

Mandatory distinction:

```text
external OAuth or tool permission
≠ Native AI Engineering authority
≠ Approval
≠ AuthorizationAssessment
```

---

## 6. Capability-composition migration

| Legacy skill-contract ID | Decision | Candidate port |
|---|---|---|
| `design-visual` | MIGRATED REPRESENTATIVE | `visual-direction-composition` |
| `design-layout` | RETAIN FOR MIGRATION | `layout-composition` |
| `design-strategy` | RETAIN FOR MIGRATION | `design-strategy-composition` |
| `design-interaction` | RETAIN FOR MIGRATION | `interaction-composition` |

A legacy `skill_contract.type: port` remains active until consumers migrate. It may be referenced through `compatibility.legacy_contract_refs`, but static presence does not prove the existing adapter implements the new first-class port contract.

---

## 7. Product-surface status

Candidate names mentioned by issue scope include assistant, content, creative rendering, media, learning, template, and product output.

Current decision:

```text
DEFER
```

No ProductSurfacePort should be created solely for taxonomy symmetry. Acceptance requires a real reusable consumer boundary, source artifact, ownership, and compatibility path.

---

## 8. Adapter reference migration

A port adapter reference must declare:

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

The validator checks stable ID, canonical path, and compatible version. This proves intended compatibility only, not implementation or runtime behavior.

---

## 9. Markdown authority reconciliation

The following legacy documents are navigation and migration records only:

```text
docs/context-management-port.md
docs/skill-management-port.md
docs/rule-management-port.md
docs/review-approval-port.md
```

Their machine semantics are superseded by the corresponding first-class contracts.

---

## 10. Remaining migration work

```text
retain or reject AgentRuntimePort
retain or reject WorkflowOrchestrationPort
migrate selected integration ports individually
migrate remaining design composition facades
resolve whether a scoped EvaluationExecutionPort is needed
confirm or reject real ProductSurfacePort boundaries
migrate downstream adapter declarations
add conformance and runtime evidence
complete final contradiction and acceptance review
```

Bulk generation from a single generic template is prohibited. Each boundary must be reviewed independently against ownership, failure, authorization, lifecycle, and consumer semantics.

---

## 11. Current status

```text
canonical kinds defined: yes
active schema and validator: yes
first-class contracts: 10
adapter reference validation: yes
legacy review/approval collapse removed: yes
legacy context/skill/rule docs reconciled: yes
all active ports migrated: no
product-surface boundary proven: no
ready for final issue acceptance: no
```
