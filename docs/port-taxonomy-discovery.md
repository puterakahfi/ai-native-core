# Native AI Engineering Port Taxonomy Discovery

Status: Discovery — non-canonical

Issue: `#7 — Formalize port taxonomy and first-class port contracts`

Branch: `7-formalize-port-taxonomy-and-first-class-port-contracts`

Canonical domain model: [`domain-model/README.md`](domain-model/README.md)

Canonical integration ownership: [`domain-model/bounded-contexts.md`](domain-model/bounded-contexts.md)

This document inventories current port declarations, records semantic conflicts, and proposes a candidate classification model for issue `#7`.

It is not a first-class port contract, final taxonomy, schema authority, adapter migration, or authorization to change runtime or product behavior.

---

## 1. Objective

Issue `#7` must turn ports from mixed Markdown descriptions and embedded contract labels into explicit, versioned, machine-validatable agreements.

The result must make these questions answerable:

```text
what required capability boundary is being requested;
which bounded context owns the port meaning;
which kind of port it is;
which direction communication flows;
what requests, responses, failures, events, and transitions are allowed;
which responsibilities the port owns and delegates;
which authorization, risk, idempotency, and observability rules apply;
which adapters may implement the port;
which version and compatibility line an adapter consumes;
which evidence proves registration, compatibility, conformance, and behavior.
```

A taxonomy that only groups names without changing these decisions is insufficient.

---

## 2. Acceptance Boundary

Issue `#7` owns:

```text
canonical port kinds;
port direction and naming rules;
first-class port contract semantics;
port ownership and dependency direction;
requests, responses, failures, events, and transition declarations;
authorization, idempotency, observability, and adapter requirements;
port compatibility and breaking-change rules;
inventory and migration of active port specifications;
manifest registration and validation of port contracts;
relationship between capability-composition ports and application or integration ports.
```

Issue `#7` does not own:

```text
redefining the canonical domain model accepted through #6;
redefining capability, contract, adapter, binding, execution, evidence, review, or approval;
implementing provider or runtime adapters;
choosing default providers for products;
moving product credentials or configuration into core;
rewriting executable skill methodology;
building the native-ai-fw control plane or adapter registry;
proving product acceptance from static port declarations.
```

---

## 3. Canonical Constraints From Issue #6

The canonical model defines:

```text
DomainCapability
→ stable ability required by the domain;

Contract
→ stable governed agreement defining what must remain true;

Port
→ abstract required capability and boundary through which a context requests behavior;

Adapter
→ replaceable implementation or translation preserving upstream meaning;

AdapterBinding
→ governed selection of an adapter for a port or contract under runtime,
  provider, product, framework, compatibility, limitation, and delegation constraints;

ExecutionRun
→ actual bounded execution attempt using an authorized binding.
```

Required non-collapses:

```text
Port ≠ DomainCapability
Port ≠ Contract
Port ≠ Adapter
Port ≠ AdapterBinding
Port ≠ provider or framework
Port ≠ WorkflowDefinition
Port ≠ ExecutionRun
Port ≠ review or approval authority
contract registration ≠ implementation
compatible adapter pin ≠ behavioral conformance
tool permission ≠ authority
successful execution ≠ product acceptance
```

The legacy shorthand:

```text
Port = capability contract
```

must not remain the canonical definition because it collapses three distinct concepts.

The corrected relationship is:

```text
Domain defines capability.
Port exposes a required capability boundary.
Contract defines the stable agreement for that boundary.
Adapter implements or translates the agreement.
AdapterBinding selects the concrete implementation for a context.
ExecutionRun records actual authorized work.
```

---

## 4. Source Inventory Inspected

### Canonical sources

```text
docs/domain-model/README.md
docs/domain-model/bounded-contexts.md
docs/domain-model/domain-objects.md
docs/domain-model/ownership-and-dependencies.md
docs/domain-model/reconciliation.md
```

### General port and adapter documents

```text
docs/port-taxonomy.md
docs/ports-and-adapters.md
docs/adapter-registry.md
README.md
```

### Dedicated control and integration port specifications

```text
docs/agent-runtime-port.md
docs/workflow-orchestration-port.md
docs/execution-run-port.md
docs/review-approval-port.md
docs/context-management-port.md
docs/skill-management-port.md
docs/rule-management-port.md
docs/tool-integration-port.md
```

### Contract-declared composition ports

```text
contracts/skills/design/design-visual.contract.yaml
contracts/skills/design/design-layout.contract.yaml
contracts/skills/design/design-strategy.contract.yaml
contracts/skills/design/design-interaction.contract.yaml
```

### Contract inventory

```text
contracts/manifest.yaml
```

The manifest currently registers skill, workflow, runtime, and behavioral-test contracts. It does not yet contain a first-class `ports` family.

---

## 5. Current Representation Classes

Port meaning currently appears in at least three forms.

### A. General Markdown examples

`docs/port-taxonomy.md`, `docs/ports-and-adapters.md`, and `docs/adapter-registry.md` list common ports and broad input/output examples.

These documents are useful discovery material but are not versioned machine authority.

### B. Dedicated Markdown specifications

Files such as `agent-runtime-port.md` and `tool-integration-port.md` define:

```text
purpose;
position;
responsibilities;
non-responsibilities;
candidate adapters;
input and output examples;
status flows;
quality gates;
dashboard usage.
```

They contain substantial contract-like meaning but are not registered, versioned port artifacts.

### C. Skill contracts marked `type: port`

The four design composition contracts use:

```yaml
skill_contract:
  type: port
```

They are registered and versioned, but their top-level artifact kind remains `skill_contract`.

This creates ambiguity between:

```text
first-class port agreement;
reusable skill capability agreement;
composition facade selecting specialist skills;
executable adapter contract.
```

Issue `#7` must preserve current consumers while making artifact identity explicit.

---

## 6. Candidate Taxonomy Model

Port kind and communication direction must be separate dimensions.

### 6.1 Port Kind

Candidate retained kinds:

```text
IntegrationPort
ControlPort
ProductSurfacePort
CapabilityCompositionPort
```

The issue body uses `ProductPort`. Discovery proposes `ProductSurfacePort` because `ProductPort` is broad enough to be mistaken for every port used by a product.

The final name remains under review.

### 6.2 Direction

```text
inbound
outbound
bidirectional
```

Direction describes communication relative to the owning context.

It does not define port kind, authority, or implementation technology.

### 6.3 Interaction Shape

A port may declare one or more interaction shapes:

```text
command
query
event
stream
subscription
callback
```

Interaction shape must not be inferred only from an operation name.

### 6.4 Mutation And Authority Profile

A port must declare whether it supports:

```text
read-only behavior;
reversible mutation;
destructive mutation;
external communication;
publishing or delivery;
security-sensitive access;
authority-bearing decision recording.
```

Technical support for mutation does not authorize a mutation.

---

## 7. Candidate Port Kind Definitions

## 7.1 IntegrationPort

Purpose:

```text
Connect a core, application, runtime, or product context to an external system,
provider, repository, persistence surface, framework, tool gateway, or infrastructure
capability through a replaceable adapter and anti-corruption boundary.
```

Typical examples:

```text
ModelInferencePort
RepositoryPort
FileSystemPort
BrowserResearchPort
DatabasePort or PersistencePort
StoragePort
ObservabilityPort
APIConnectorPort
MCPGatewayPort
AuthBrokerPort
ToolRegistryPort
```

Primary constraints:

```text
provider and SDK types stay behind the adapter boundary;
external permission does not become domain authority;
external errors and limitations remain explicit;
request and response normalization preserves source provenance;
credentials and private configuration remain outside core;
provider capability does not redefine product policy.
```

## 7.2 ControlPort

Purpose:

```text
Expose application or control-plane operations that coordinate, resolve, route,
record, or govern domain work without becoming the concrete execution provider or
owning another context's aggregate.
```

Typical examples:

```text
AgentRuntimePort
WorkflowOrchestrationPort
ExecutionRun management boundary
ContextManagementPort
SkillManagementPort
RuleManagementPort
Review request boundary
Approval or authorization request boundary
```

Primary constraints:

```text
control operations reference canonical aggregates rather than duplicating them;
workflow or runtime control does not self-authorize execution;
recording execution does not perform execution;
review requests and approval decisions remain separate;
control status cannot collapse domain status families;
control-plane convenience does not override context ownership.
```

## 7.3 ProductSurfacePort

Purpose:

```text
Expose stable product-facing input, output, delivery, rendering, assistant,
content, media, or publication capabilities while preserving product ownership
and keeping provider integrations replaceable.
```

Candidate examples from current documentation and issue scope:

```text
PublishingPort
DesignGenerationPort or a future CreativeRenderingPort
assistant capability boundary
content capability boundary
media capability boundary
template capability boundary
product-output capability boundary
```

Primary constraints:

```text
product-surface meaning is owned by product or accepted cross-product agreement;
provider APIs remain behind IntegrationPorts and adapters;
generation is not acceptance;
publishing capability is not publishing authorization;
technical delivery is not product acceptance;
one product's surface model does not become universal core by default.
```

Issue-declared assistant, content, creative-rendering, media, learning, template, and product-output candidates require exact active-artifact confirmation before acceptance.

## 7.4 CapabilityCompositionPort

Purpose:

```text
Expose a stable facade that selects, routes, orders, or composes reusable capability
contracts or skill adapters without pretending to be an infrastructure integration port.
```

Confirmed current examples:

```text
design-visual
design-layout
design-strategy
design-interaction
```

Primary constraints:

```text
composition owns routing and synthesis boundaries, not every specialist method;
the facade declares owned and delegated responsibilities;
selected skill contracts retain their own identity and version;
loading a skill does not prove correct application;
composition output does not become review or approval automatically;
composition ports remain distinguishable from hexagonal integration ports.
```

---

## 8. Confirmed General Port Inventory

The following names are explicitly present in general port documentation.

| Existing name | Source | Candidate classification | Current decision |
|---|---|---|---|
| `ModelInferencePort` | port taxonomy, ports/adapters | IntegrationPort, outbound | Retain candidate; provider-neutral request/response and error semantics required |
| `CodeExecutionPort` | port taxonomy, ports/adapters, adapter registry | ControlPort with execution-plane adapter | Retain candidate; must reference authorization and ExecutionRun rather than own approval |
| `DesignGenerationPort` | port taxonomy, ports/adapters, adapter registry | ProductSurfacePort and/or CapabilityCompositionPort | Split or narrow; current name mixes design reasoning, rendering, and product output |
| `DesignReviewPort` | port taxonomy, ports/adapters, adapter registry | CapabilityCompositionPort or ControlPort | Retain only as review capability boundary; must not own approval |
| `KnowledgeRetrievalPort` | port taxonomy, ports/adapters | IntegrationPort | Retain candidate as source retrieval; ContextManagementPort owns assembly and readiness |
| `RepositoryPort` | port taxonomy, ports/adapters, adapter registry | IntegrationPort | Retain candidate; operations, mutation risk, idempotency, and repository authority required |
| `FileSystemPort` | ports/adapters | IntegrationPort | Retain candidate; distinguish local filesystem from repository semantics |
| `BrowserResearchPort` | ports/adapters | IntegrationPort | Retain candidate; source, coverage, rate-limit, and retrieval evidence required |
| `WebAppPort` | port taxonomy, ports/adapters, adapter registry | Framework binding rather than one stable port | Reject as currently broad; decompose by required capability or model as FrameworkAdapter binding |
| `DatabasePort` | port taxonomy, ports/adapters, adapter registry | IntegrationPort | Retain or rename as PersistencePort specialization; schema and transaction boundaries required |
| `StoragePort` | port taxonomy, ports/adapters, adapter registry | IntegrationPort | Retain candidate; object/file lifecycle and destructive operations required |
| `PublishingPort` | port taxonomy, ports/adapters, adapter registry | ProductSurfacePort backed by IntegrationPorts | Retain candidate; publishing readiness and authorization remain external governance inputs |
| `EvaluationPort` | port taxonomy, ports/adapters, adapter registry | ControlPort or CapabilityCompositionPort | Narrow; current approved/rejected outputs collapse evaluation, review, and approval |
| `ObservabilityPort` | port taxonomy, ports/adapters, adapter registry | IntegrationPort | Retain candidate; write telemetry and query telemetry may require distinct operations |

---

## 9. Dedicated Control And Integration Port Inventory

## 9.1 AgentRuntimePort

Source: `docs/agent-runtime-port.md`

Candidate kind: `ControlPort`

Retainable responsibilities:

```text
start, pause, resume, stop, and inspect agent runs;
resolve allowed tools, skills, rules, and runtime constraints;
route external actions through tool integration;
reference ExecutionRun records;
pause or route when approval is required.
```

Required corrections:

```text
agent runtime does not own approval;
runtime status uses canonical execution semantics;
reasoning-safe summary does not imply private chain-of-thought exposure;
ExecutionRun remains Runtime & Execution aggregate authority;
allowed tools and permission do not imply authority.
```

## 9.2 WorkflowOrchestrationPort

Source: `docs/workflow-orchestration-port.md`

Candidate kind: `ControlPort`

Retainable responsibilities:

```text
trigger and coordinate WorkflowRuns;
manage step handoffs, retry policy, pause, cancellation, and visibility;
route external operations;
record execution references and failures.
```

Required corrections:

```text
WorkflowDefinition ≠ WorkflowRun;
WorkflowRun ≠ ExecutionRun;
workflow completion ≠ product or criterion completion;
waiting for approval is not approval ownership;
retry does not bypass idempotency or authorization requirements.
```

## 9.3 ExecutionRunPort

Source: `docs/execution-run-port.md`

Candidate kind: `ControlPort`

Current conflict:

```text
queued → running → completed → failed → needs_review → approved
```

This collapses `ExecutionStatus`, `ReviewDisposition`, and `ApprovalStatus`.

Candidate correction:

```text
ExecutionRun recording and retrieval boundary
→ owns creation, append, transition, and retrieval operations over ExecutionRun;

Review request
→ separate review capability;

Approval or authorization
→ separate governance capability.
```

The final name may need to become `ExecutionRunManagementPort`, `ExecutionRecordPort`, or another operation-specific name so the port is not confused with the aggregate itself.

## 9.4 ReviewApprovalPort

Source: `docs/review-approval-port.md`

Candidate classification: split required.

Current responsibilities combine:

```text
review request;
review findings and verdict;
authority-bearing approval or rejection;
workflow blocking and unblocking;
revision control.
```

Canonical split candidate:

```text
ReviewPort or ReviewManagementPort
→ create review request, assign reviewer, preserve evidence and findings,
  record ReviewResult;

Decision or ApprovalPort
→ record authority-bearing decision, approval, rejection, waiver,
  or risk acceptance under DecisionCase semantics;

AuthorizationPort
→ assess whether a concrete action may proceed now.
```

One adapter may implement multiple ports. One port contract must not collapse their meanings.

## 9.5 ContextManagementPort

Source: `docs/context-management-port.md`

Candidate kind: `ControlPort`

Retainable responsibilities:

```text
resolve ContextRequests;
assemble ContextPacks;
validate source, freshness, availability, and gaps;
produce a bounded handoff checkpoint.
```

Required corrections:

```text
ContextPack ≠ source of truth;
context completeness ≠ execution authorization;
ready_for_handoff ≠ capability, permission, authority, or successful execution;
retrieval adapters remain IntegrationPorts.
```

## 9.6 SkillManagementPort

Source: `docs/skill-management-port.md`

Candidate kind: `ControlPort`

Retainable responsibilities:

```text
list and resolve SkillDefinitions;
check contract and adapter compatibility;
attach selected skill references to a method or workflow handoff;
report missing or incompatible skills.
```

Required corrections:

```text
skill discovery ≠ skill application;
installation ≠ embodiment;
SkillManagementPort must not own ExecutionRun;
creating or evolving skills routes through Learning & Evolution governance.
```

The final model may separate catalog, resolution, and application operations without requiring three port kinds.

## 9.7 RuleManagementPort

Source: `docs/rule-management-port.md`

Candidate kind: `ControlPort`

Retainable responsibilities:

```text
resolve applicable rules and policy references;
evaluate planned action against declared constraints;
report violations, warnings, blocks, and routes.
```

Required corrections:

```text
rule resolution ≠ approval;
rule evaluation result ≠ technical execution authorization by itself;
product policy stays product-owned;
canonical core rules cannot be silently rewritten by product adapters.
```

A more precise final name may be `RuleResolutionPort`, `PolicyEvaluationPort`, or a split between retrieval and evaluation.

## 9.8 ToolIntegrationPort

Source: `docs/tool-integration-port.md`

Candidate kind: `IntegrationPort` umbrella or family.

Current subtype candidates:

| Existing subtype | Candidate kind | Note |
|---|---|---|
| `MCPGatewayPort` | IntegrationPort | protocol/gateway specialization |
| `APIConnectorPort` | IntegrationPort | direct external API specialization |
| `AuthBrokerPort` | IntegrationPort | external identity, token, and scope integration; authority remains external governance reference |
| `ToolExecutionPort` | IntegrationPort or ControlPort specialization | must separate approved request from actual ToolInvocation and ExecutionRun |
| `ToolRegistryPort` | IntegrationPort | discovers external tool schemas, capability, and permission metadata |

Required corrections:

```text
adapter lifecycle ≠ port lifecycle;
external OAuth permission ≠ Native AI authority;
tool request ≠ ToolInvocation;
tool invocation ≠ successful domain outcome;
mutation capability ≠ approval;
tool result normalization preserves external source and limitations.
```

---

## 10. Contract-Declared Capability Composition Ports

The manifest registers four `skill_contract` artifacts with `type: port`.

| Contract ID | Version | Current role | Candidate kind |
|---|---:|---|---|
| `design-visual` | `1.1.0` | routes visual direction concerns to specialist design contracts | CapabilityCompositionPort |
| `design-layout` | `2.0.1` | composes macrostructure, components, adaptive selection, responsiveness | CapabilityCompositionPort |
| `design-strategy` | `1.1.0` | composes UX strategy, IA, collection discovery, CRO, copy, content | CapabilityCompositionPort |
| `design-interaction` | `1.0.0` | composes interaction and UX pattern capabilities | CapabilityCompositionPort |

Current strengths:

```text
versioned identity;
manifest registration;
explicit capability;
quality gates;
adapter or specialist catalogs;
consumer use through executable skills.
```

Current ambiguity:

```text
top-level artifact is skill_contract;
type is port;
port ownership and direction are implicit;
request, response, failure, authority, idempotency, observability,
and compatibility fields are inconsistent or absent;
"adapter" sometimes means specialist skill rather than Integration & Binding adapter.
```

Migration constraints:

```text
Do not duplicate the same agreement independently as skill_contract and port_contract.
Do not break existing adapter pins without a compatibility plan.
Do not rename specialist skill adapters only to satisfy a taxonomy label.
Do not treat composition facade success as final design review or product acceptance.
```

Candidate migration patterns under review:

### Pattern A — Port contract becomes canonical

```text
port_contract/design-visual
→ stable composition boundary;

skill contract or executable adapter
→ implements the port contract;

legacy skill_contract path
→ compatibility alias or deprecated lineage.
```

### Pattern B — Skill contract remains canonical with explicit port profile

```text
skill_contract
→ remains capability agreement;

port profile
→ adds explicit kind, direction, request/response, failure, and adapter-binding semantics.
```

Pattern B reduces path churn but weakens the goal of one first-class `port_contract` family.

The final decision requires schema, manifest, validator, and adapter-pin analysis.

---

## 11. Issue-Declared Candidates Not Yet Confirmed As Active Artifacts

The issue body asks the inventory to evaluate:

```text
browser;
persistence;
infrastructure;
assistant;
content;
creative rendering;
media;
learning;
template;
product output.
```

Some concepts overlap confirmed ports or registered skill contracts, but exact first-class active port artifacts have not yet been confirmed for every name.

Until inspected, they remain:

```text
issue-declared candidates;
not accepted inventory rows;
not evidence of an existing port contract;
not authorization to create duplicate artifacts.
```

---

## 12. Rejected Or Split Candidates

### WebAppPort as one broad port

Current meaning includes routing, pages, components, server actions, APIs, state, and rendering.

This is a framework/application implementation bundle rather than one coherent required capability boundary.

Candidate replacement:

```text
FrameworkAdapter or ProductBinding
→ selects Next.js, Nuxt, Remix, SvelteKit, or another framework;

specific ports
→ expose required HTTP, UI rendering, persistence, publishing, or product capabilities.
```

### ReviewApprovalPort as one port

Rejected because review and approval have different owners, evidence, authority, and status families.

### EvaluationPort returning approved/rejected

Rejected in current form because evaluation result and authority-bearing approval are distinct.

### ExecutionRunPort owning approved state

Rejected because ExecutionStatus cannot contain review or approval state.

### DesignGenerationPort as universal design boundary

Requires split or narrowing because design reasoning, composition, rendering, generation, review, and product output are different capabilities.

---

## 13. Candidate First-Class Port Contract Shape

This shape is a discovery proposal, not an accepted schema.

```yaml
port_contract:
  id: stable-kebab-case-id
  kind: integration | control | product_surface | capability_composition
  version: "1.0.0"
  capability: stable_capability_identifier
  direction: inbound | outbound | bidirectional
  owner_context: integration_and_binding
  consumer_contexts: []
  purpose: >
    Stable required capability boundary.

  boundary:
    owns: []
    delegates: []
    does_not_own: []

  interactions:
    requests: []
    responses: []
    events: []
    streams: []

  failures:
    errors: []
    retryability: explicit
    partial_result_policy: explicit
    unknown_or_not_checkable_policy: explicit

  state_transitions: []

  authorization:
    required_for: []
    authority_source: external_reference
    permission_is_not_authority: true

  idempotency:
    mode: required | supported | not_applicable
    key_scope: explicit

  observability:
    required_events: []
    correlation_fields: []
    sensitive_fields: []

  adapter_requirements: []

  compatibility:
    policy: semantic_version
    breaking_changes: []
    aliases: []
    supersedes: []

  quality_gates: []
```

Required-field profiles may differ by kind, but omissions must be explicit rather than silently accepted.

---

## 14. Compatibility And Breaking-Change Candidates

A port contract change is potentially breaking when it:

```text
removes or renames a request, response, event, or error;
changes operation meaning or ownership;
changes direction;
changes mutation or authorization requirements;
changes idempotency guarantees;
weakens or strengthens required evidence or quality gates;
changes failure or partial-result semantics;
changes state-transition rules;
changes delegated responsibility into owned responsibility or the reverse;
changes adapter requirements;
changes privacy, security, or observability obligations;
changes product-surface meaning consumed downstream.
```

A new optional field is not automatically non-breaking if its semantic requirement changes adapter behavior.

Compatibility evidence remains layered:

```text
path and identity resolve;
version pin is compatible;
required contract fields validate;
owned and delegated boundaries are consistent;
adapter behavior passes representative cases;
runtime integration works;
product acceptance is demonstrated where claimed.
```

---

## 15. Migration Principles

```text
Inventory before renaming.
Classify before creating schema.
Stabilize taxonomy before bulk migration.
Preserve stable IDs or provide explicit aliases and supersession.
Do not copy Markdown prose blindly into YAML.
Do not duplicate one agreement across two canonical artifact kinds.
Do not treat manifest registration as runtime implementation.
Do not migrate product/provider configuration into core.
Do not use port migration to rename executable skills without a consumer plan.
Keep documentation explanatory and link it to machine authority.
```

Candidate migration order:

```text
1. complete active port inventory;
2. accept port kinds, directions, names, and ownership rules;
3. define schema and positive/negative fixtures;
4. create a small representative first-class port set;
5. update manifest generation and validation;
6. migrate remaining active port specs with aliases and compatibility notes;
7. update Markdown docs to navigation and explanatory roles;
8. validate adapter pins and downstream consumer migration;
9. add behavioral and architecture evidence;
10. request owner acceptance.
```

---

## 16. Open Questions

1. Should the final fourth kind be named `ProductPort` or `ProductSurfacePort`?
2. Is `ControlPort` sufficiently precise, or should application/control-plane operations use `ApplicationPort` with a separate control-plane profile?
3. Should direction be relative to the owning bounded context, the application core, or the product boundary?
4. Should one port contract allow multiple interaction shapes or require separate command/query/event ports?
5. Should `ExecutionRunPort` be renamed to avoid identity collision with the `ExecutionRun` aggregate?
6. Should review, decision recording, approval, and authorization be separate ports?
7. Should `ToolIntegrationPort` remain an umbrella contract or become only a documentation family over subtype contracts?
8. Should database and storage ports share a `PersistencePort` parent profile or remain independent?
9. How should product-surface ports reference product-owned semantics without encoding one product in universal core?
10. Should the four design composition artifacts migrate to `port_contract`, or retain `skill_contract` with an explicit composition-port profile?
11. Which current adapter metadata key should pin a port contract without conflating it with `ai-native-skills.implements`?
12. Which port fields belong in issue `#7` versus unified schema mechanics owned by issue `#8`?
13. Which compatibility checks belong in current tooling versus validator v2 owned by issue `#9`?
14. Which issue-declared product and infrastructure candidates already exist under different names?
15. Which Markdown port specs are active, historical, duplicated, or unreferenced?

---

## 17. Validation Gates For Discovery

Before taxonomy may be frozen:

- [ ] every active Markdown port specification is enumerated;
- [ ] every contract declaring itself as a port is enumerated;
- [ ] every README and architecture port name is mapped;
- [ ] aliases, duplicates, umbrella names, and obsolete names are explicit;
- [ ] each retained port has one kind and one primary owner;
- [ ] direction is declared separately from kind;
- [ ] Port, Contract, Adapter, and AdapterBinding remain distinct;
- [ ] review and approval remain separate;
- [ ] execution and execution recording remain separate;
- [ ] evaluation results do not become approvals;
- [ ] product-surface semantics do not leak provider details;
- [ ] composition ports do not masquerade as infrastructure ports;
- [ ] no existing adapter pin is broken without migration evidence;
- [ ] issue `#8` can consume the artifact shape;
- [ ] issue `#9` can consume static conformance semantics;
- [ ] `native-ai-fw` can bind adapters without importing provider semantics into core;
- [ ] representative product repositories can specialize ports without redefining them.

---

## 18. Current Verdict

```text
Canonical domain dependency: SATISFIED
General port documents inspected: YES
Dedicated control/integration specs inspected: 8
Contract-declared composition ports inspected: 4
Manifest port family present: NO
Legacy Port = capability contract collapse: REJECTED
Candidate port kinds: 4
Direction modeled separately: YES
Review/approval split required: YES
Execution/review/approval status collapse found: YES
WebAppPort retained as-is: NO
First-class port schema accepted: NO
Complete repository-wide inventory: NOT YET
Contract migration authorized: NO
Ready to freeze taxonomy: NO
Ready for complete inventory matrix and representative schema design: YES
```
