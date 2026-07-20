# Native AI Engineering Bounded Contexts

Status: Proposed canonical context map for issue `#6`

Entry point: [`README.md`](README.md)

These contexts define language and ownership boundaries. They are not mandatory microservices, packages, teams, databases, or repositories.

A concrete system may combine contexts physically while preserving their semantic boundaries and dependency direction.

---

## Context map

```text
Intent & Specification
        ↓
Capability & Agreement
        ↓
Method & Workflow ───────────────┐
        ↓                        │
Integration & Binding            │
        ↓                        │
Runtime & Execution              │
        ↓                        │
Evidence, Evaluation & Review ◀──┘
        ↓
Governance, Risk & Authority
        ↓
Product, Delivery & Registry
        ↓
Learning & Evolution
        ↘ governed proposals to the smallest correct upstream context

Context, Knowledge & Memory supports every context through attributable,
scoped, current information without owning their decisions.
```

The arrows show primary dependency and evidence flow. They do not imply that every context is always invoked or that downstream work may mutate upstream meaning.

---

## 1. Intent & Specification

### Owns

```text
IntentSpecification
Intent
Requirement
AcceptanceCriterion
Constraint
NonGoal
SuccessMeasure
RiskStatement
```

### Responsibilities

- preserve attributable requested intent;
- label inferred intent and unresolved ambiguity;
- define scope, constraints, non-goals, and desired outcomes;
- convert accepted intent into verifiable requirements and acceptance criteria;
- track requirement supersession without erasing decision history.

### Provides

```text
accepted intent
requirements
acceptance criteria
scope and exclusions
success and risk framing
```

### Consumes

- attributable user, product, repository, policy, or authority sources;
- research and evidence where intent or need is not yet established.

### Must not own

- implementation method;
- runtime execution state;
- technical verification results;
- approval merely because the requester expressed intent.

### Anti-corruption boundary

A prompt, ticket, conversation, or model-generated brief is an input source. It is not automatically the accepted intent specification.

---

## 2. Capability & Agreement

### Owns

```text
CapabilityAgreement
DomainCapability
UseCase
ContractIdentity
ContractVersion
ContractBoundary
InputRequirement
OutputAllowance
QualityGateDefinition
CompatibilityExpectation
```

### Responsibilities

- define stable domain capabilities independent of providers;
- define goal-oriented use cases;
- register governed contracts and versions;
- preserve required inputs, allowed outputs, gates, owned boundary, and delegated boundary;
- expose compatibility expectations and breaking-change impact;
- distinguish contract identity from implementation and conformance.

### Provides

```text
capability meaning
use-case requirements
stable agreement
contract identity and compatibility
quality and boundary expectations
```

### Consumes

- accepted requirements and acceptance criteria;
- philosophy and canonical domain terminology;
- governed evolution decisions.

### Must not own

- executable methodology;
- provider or framework selection;
- runtime process state;
- product-specific acceptance.

### Anti-corruption boundary

A contract file, manifest row, or version pin cannot be translated into “implemented,” “conformant,” or “production-ready” without separate evidence.

---

## 3. Method & Workflow

### Owns

```text
SkillDefinition
WorkflowDefinition
PhaseDefinition
TransitionRule
HandoffDefinition
ExitCondition
MethodSelection
EvidenceRequirement
```

### Responsibilities

- define reusable executable procedures;
- distinguish one bounded method from an ordered workflow;
- compose capabilities, skills, phases, gates, handoffs, and exit conditions;
- define what evidence is expected from each phase;
- route specialist ownership rather than absorbing all methodology;
- preserve the distinction between workflow, Development Loop, and Epistemic Loop.

### Provides

```text
method selection
skill requirements
workflow phase order
transition and handoff expectations
execution-ready procedure definition
```

### Consumes

- capability agreements;
- accepted intent and constraints;
- context and knowledge;
- governance policy for applicable gates.

### Must not own

- concrete runtime invocation;
- technical permission or authority;
- provider credentials;
- final review or approval.

### Anti-corruption boundary

A workflow definition is not an execution run. A skill installation is not evidence that the method was applied.

---

## 4. Integration & Binding

### Owns

```text
PortReference
AdapterBinding
ProviderBinding
ProductBinding
FrameworkBinding
ImplementationRequirement
BindingCompatibility
BindingLimitation
DelegatedResponsibility
```

### Responsibilities

- translate abstract capability requirements into replaceable implementation bindings;
- preserve upstream contract and domain meaning;
- declare adapter limitations and delegated responsibilities;
- validate binding compatibility;
- allow product and runtime specialization without upstream leakage.

### Provides

```text
selected binding
implementation requirements
compatibility and limitation record
delegation and handoff record
```

### Consumes

- capability and contract requirements;
- product policy and runtime constraints;
- provider and framework capabilities;
- authority and permission constraints.

### Must not own

- canonical domain meaning;
- authority inferred from tool access;
- product policy merely because a provider supports an option;
- the exhaustive port taxonomy owned by issue `#7`.

### Base adapter specializations

```text
SkillAdapter
RuntimeAdapter
ProviderAdapter
ProductAdapter
FrameworkAdapter
```

These names establish ownership direction. Issue `#7` may refine the exhaustive taxonomy.

### Anti-corruption boundary

Provider names, SDK types, framework components, and deployment commands must remain behind the binding boundary unless a product contract explicitly owns them.

---

## 5. Runtime & Execution

### Owns

```text
RuntimeEnvironment
Actor
Agent
ToolRegistration
ExecutionRun
ExecutionStep
ToolInvocation
ExecutionArtifact
RuntimeEvent
ExecutionStatus
CapacityAssessment
ExecutionAuthorizationReference
```

### Responsibilities

- execute or route authorized work;
- preserve requested, planned, authorized, running, and completed states separately;
- record actual tool invocations and outcomes;
- produce attributable execution artifacts and events;
- disclose blocked, failed, cancelled, partial, and limited outcomes;
- assess current capacity before material execution.

### Provides

```text
actual execution record
runtime events
execution artifacts
observations and evidence candidates
operational outcome
```

### Consumes

- workflow and method definitions;
- adapter bindings;
- context packs;
- permission and authority references;
- risk controls and recovery constraints.

### Must not own

- canonical contracts;
- approval inferred from successful execution;
- product acceptance;
- facts broader than observed runtime scope.

### Anti-corruption boundary

A plan, code generation request, tool call proposal, or model response is not an execution event until the host mechanism actually executes or records it.

---

## 6. Context, Knowledge & Memory

### Owns

```text
ContextRequest
ContextPack
SourceReference
KnowledgeItem
MemoryReference
ContextGap
StalenessAssessment
ContextValidationResult
```

### Responsibilities

- gather relevant attributable context;
- preserve source, scope, time, version, recency, and authority;
- distinguish accepted knowledge from memory, inference, and assumption;
- identify missing, stale, conflicting, or inaccessible context;
- provide context to other contexts without taking their decisions.

### Provides

```text
context pack
source references
knowledge references
memory references
missing or stale context report
```

### Consumes

- designated sources of truth;
- repository state;
- product and runtime references;
- accepted domain definitions.

### Must not own

- the authoritative source merely because it copied or summarized it;
- current state without observation;
- approval or effective decision;
- silent replacement of knowledge with memory.

### Anti-corruption boundary

A context pack is a scoped handoff, not a new canonical source for every included fact.

---

## 7. Evidence, Evaluation & Review

### Owns

```text
EvidenceCase
Claim
EvidenceItem
EvidenceScope
Coverage
VerificationResult
ValidationResult
EvaluationResult
ReviewRequest
ReviewResult
Finding
GateResult
CompletionClaim
```

### Responsibilities

- relate explicit claims to typed, attributable evidence;
- preserve scope and coverage;
- perform verification, validation, evaluation, and review as distinct activities;
- evaluate gates against declared criteria and evidence;
- record findings, verdicts, limitations, and unsupported claims;
- represent completion as a bounded claim with evidence and limitations.

### Provides

```text
claim support or challenge
evidence references
verification and validation results
evaluation and review results
gate outcomes
completion disposition
```

### Consumes

- requirements and acceptance criteria;
- contract quality gates;
- execution observations and artifacts;
- product acceptance criteria;
- governance review requirements.

### Must not own

- authority-bearing approval unless governance explicitly assigns it;
- runtime execution;
- evidence-free confidence or recommendation.

### Anti-corruption boundary

A build, test, screenshot, static declaration, review comment, or model judgment supports only the claim and coverage appropriate to its method.

---

## 8. Governance, Risk & Authority

### Owns

```text
Policy
Rule
AuthorityGrant
PermissionGrant
Decision
EffectiveDecisionAssessment
Approval
RiskAssessment
RiskAcceptance
Exception
Delegation
ApprovalCondition
```

### Responsibilities

- define who may bind, approve, reject, delegate, supersede, or accept risk;
- distinguish technical permission from decision authority;
- determine whether a decision is effective;
- apply proportionate review, approval, exception, and escalation policy;
- govern canonical changes and risk acceptance;
- preserve approval conditions, expiry, revocation, and scope.

### Provides

```text
policy and rule constraints
permission and authority references
effective decision result
approval or rejection
risk and exception decisions
```

### Consumes

- risk and reversibility information;
- review findings and evidence;
- affected scope and consumers;
- designated authority sources.

### Must not own

- evidence production;
- implementation merely because it constrains implementation;
- authority inferred from repository ownership, access, or capability alone.

### Anti-corruption boundary

A recommendation, review approval emoji, technical merge permission, or lack of objection is not an approval unless the governing process assigns that authority.

---

## 9. Product, Delivery & Registry

### Owns the runtime-agnostic base model for

```text
ProductInstance
ProductIntentReference
ProductPolicyReference
ProductBindingRegistry
DeliveryCandidate
DeliveryRecord
ReleaseAcceptance
ConsumerImpact
ProductValidationReference
```

### Responsibilities

- bind reusable core capabilities to product-owned policy and implementation;
- identify product-specific source-of-truth boundaries;
- register product and provider bindings;
- record delivery into a target branch, environment, registry, or consumer boundary;
- distinguish technical delivery from product acceptance and business outcomes;
- identify affected consumers and product acceptance authority.

### Provides

```text
product binding and policy references
delivery target and record
release acceptance reference
consumer-impact record
field-validation reference
```

### Consumes

- intent and capability agreements;
- workflows and adapter bindings;
- evidence, review, and approval results;
- product repository implementation and policy.

### Must not own in core

- private customer data;
- product secrets;
- one product’s domain as universal Native AI Engineering meaning;
- provider-specific deployment configuration.

### Anti-corruption boundary

The core context defines the relationship. Product repositories own concrete product policy, business rules, implementation, and acceptance.

---

## 10. Learning & Evolution

### Owns

```text
LearningEvolutionCase
FeedbackItem
AffectedLayer
UpdateRecord
LearningRecord
LearningCandidate
TransferabilityAssessment
CounterexampleSet
CompatibilityImpact
EvolutionProposal
EvolutionDecision
```

### Responsibilities

- route feedback to the smallest correct layer;
- distinguish local update from learning and shared promotion;
- require transferability and counterexample review;
- identify affected consumers and compatibility impact;
- govern promotion to knowledge, skill, workflow, contract, port, domain, or philosophy layers;
- prevent field evidence from directly redefining core.

### Provides

```text
local update record
learning record
learning candidate
transferability result
evolution proposal and decision
```

### Consumes

- execution, product, evaluation, and review feedback;
- current target-layer authority and compatibility rules;
- counterexamples from multiple contexts.

### Must not own

- automatic promotion from one successful case;
- silent mutation of canonical contracts or terms;
- product-specific behavior generalized without evidence.

### Anti-corruption boundary

A verified local fix may become a learning candidate. It becomes core evolution only after the core owner accepts a compatible, transferable proposal.

---

## Collaboration rules

### Shared identifiers, not shared ownership

Contexts may reference objects owned elsewhere through stable identifiers and snapshots. They must not duplicate and independently mutate another context’s aggregate.

### Evidence crosses boundaries by reference

Evidence retains its source, method, scope, coverage, and claim relation when consumed by governance, delivery, or evolution contexts.

### Product specialization remains downstream

Product contexts may specialize capability, policy, workflow, and binding. They must not present product-specific meaning as universal core without governed evolution.

### Context boundaries survive physical co-location

A monolith or one repository may implement several contexts. Co-location does not erase ownership, language, or invariant boundaries.

---

## Context ownership summary

| Context | Primary question |
|---|---|
| Intent & Specification | What outcome and conditions are accepted? |
| Capability & Agreement | What stable ability and agreement must remain true? |
| Method & Workflow | How is reusable work performed and composed? |
| Integration & Binding | Which replaceable implementation binds the agreement? |
| Runtime & Execution | What actually ran, where, by whom, and with what outcome? |
| Context, Knowledge & Memory | What attributable information is available and current? |
| Evidence, Evaluation & Review | What claims are supported, challenged, or limited? |
| Governance, Risk & Authority | Who may decide, approve, reject, delegate, or accept risk? |
| Product, Delivery & Registry | How is core specialized, delivered, and accepted by a product? |
| Learning & Evolution | What should update locally or be proposed for shared evolution? |
