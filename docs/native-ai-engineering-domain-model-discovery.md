# Native AI Engineering Domain Model Discovery

Status: Discovery input for issue `#6`

Canonical philosophy authority: [`philosophy/README.md`](philosophy/README.md)

Accepted atomic vocabulary: [`philosophy/term-authority.md`](philosophy/term-authority.md)

This document inventories the current Native AI Engineering domain signals, identifies contradictions and ownership gaps, and proposes candidate modeling boundaries for review.

It is not yet the canonical domain model. It does not redefine the accepted philosophy, finalize the port taxonomy owned by `#7`, select schemas owned by `#8`, or specify validator-v2 behavior owned by `#9`.

---

## 1. Discovery objective

Issue `#6` requires one runtime-agnostic domain model that lets core contracts, executable skills, control-plane runtime, and product repositories share the same language without sharing the same ownership.

The model must explain the relationship between:

```text
intent
requirement and acceptance
capability and use case
contract and boundary
workflow and method
port and adapter
runtime execution
evidence and gates
review and approval
delivery and product acceptance
feedback, learning, and governed evolution
```

The model must also preserve the philosophy-level distinctions accepted by issue `#13`:

```text
state ≠ observation
observation ≠ interpretation
interpretation ≠ inference
assumption ≠ fact
claim ≠ evidence
capability ≠ permission ≠ authority
decision ≠ effective decision ≠ approval
verification ≠ validation ≠ evaluation ≠ review
feedback ≠ learning candidate ≠ accepted evolution
partial / blocked / not-verified ≠ complete
```

---

## 2. Sources inspected

### Philosophy and term authority

- `docs/philosophy/README.md`
- `docs/philosophy/laws.md`
- `docs/philosophy/principles-and-guardrails.md`
- `docs/philosophy/term-authority.md`
- `docs/philosophy/epistemic-loop.md`
- `docs/philosophy/traceability-and-usefulness.md`
- `docs/philosophy/reconciliation-and-pruning.md`

### Architecture and modeling

- `README.md`
- `docs/architecture-v0.2.md`
- `docs/domain-driven-model.md`
- `docs/engineering-contract.md`
- `docs/ports-and-adapters.md`
- `docs/port-taxonomy.md`
- `docs/adapter-registry.md`
- `docs/glossary.md`
- `docs/memory-vs-knowledge.md`

### Lifecycle and executable agreement

- `docs/development-loop.md`
- `docs/contract-catalog.md`
- `docs/adapter-conformance.md`
- `contracts/skills/**`
- `contracts/workflows/**`
- `contracts/runtime/**`
- `contracts/tests/**`
- `contracts/manifest.yaml`

### Downstream ownership signals

- `ai-native-skills` executable skill, workflow, reviewer, and eval adapters
- `native-ai-fw` orchestration and control-plane responsibility
- product repositories as product policy, implementation, and field-validation owners

The generated manifest remains the contract inventory authority. This report uses contract families and categories as domain signals; it does not duplicate every manifest row.

---

## 3. Current strengths

### 3.1 Stable upstream/downstream direction already exists

The repository consistently expresses:

```text
domain meaning and stable agreement
→ port or capability boundary
→ replaceable adapter
→ runtime or product specialization
```

This is a strong dependency rule even though the domain objects and bounded contexts are not yet canonical.

### 3.2 Philosophy now supplies the missing epistemic and authority boundaries

The accepted philosophy provides stable distinctions for:

- attributable observation and explicit unknowns;
- state–representation separation;
- claim and typed evidence;
- capability, permission, authority, decision, and approval;
- scope, coverage, and contextual capacity;
- completion and embodiment;
- feedback, learning candidates, and governed core evolution;
- source-of-truth knowledge and memory.

These terms are domain-model constraints, not optional explanatory prose.

### 3.3 Contract families expose real capability and lifecycle boundaries

Current contract families distinguish:

```text
skill contracts       reusable capability interfaces
workflow contracts    ordered lifecycle agreements
runtime contracts     runtime-facing implementation-agnostic agreements
behavioral tests      executable behavior expectations
```

The distinction is useful and should survive the domain model even if issue `#8` later unifies their schemas.

### 3.4 Execution, review, and evolution loops already exist

The repository has usable concepts for:

- Development Loop execution phases;
- workflow phases and transitions;
- adapter conformance evidence layers;
- decision provenance;
- skill evaluation;
- feedback and skill evolution.

The gap is not absence of concepts. The gap is one canonical relationship and ownership model across them.

---

## 4. Current conflicts and ambiguity

### 4.1 Operational layers are being used where bounded contexts are needed

`architecture-v0.2.md` lists eleven operational layers:

```text
Intent
Domain
Application
Contract
Port
Adapter
Agent
Rule
Skill
Knowledge
Evaluation
```

These are useful dependency or responsibility views, but they are not automatically bounded contexts.

Examples:

- `Rule`, `Skill`, and `Contract` are artifact or behavior kinds that may participate in several bounded contexts.
- `Agent` is an actor type inside runtime execution, not necessarily a domain context.
- `Evaluation` spans evidence production, criteria, review, and governance rather than one simple layer.
- `Adapter` is an implementation role whose subtype and owner depend on the boundary being bound.

The canonical model should preserve the architecture view as an operational map while refusing to treat layer numbering as domain ownership.

### 4.2 The existing domain-driven document is a modeling guide, not the Native AI Engineering domain model

`docs/domain-driven-model.md` correctly teaches core domain, bounded context, entity, value object, aggregate, and domain event. However, its concrete model is product-oriented and dominated by an illustrative creative product.

It does not yet define Native AI Engineering objects such as:

```text
Intent
Requirement
AcceptanceCriterion
Capability
UseCase
Contract
WorkflowRun
ExecutionRun
Claim
Evidence
GateResult
Review
Approval
Delivery
LearningCandidate
EvolutionProposal
```

The document should remain a modeling guide or be reconciled to point to the accepted canonical domain model. Product examples must remain explicitly illustrative.

### 4.3 Several different lifecycle maps coexist

Current sources contain:

```text
Architecture v0.1 lifecycle
Intent → Blueprint → Engineering Contract → ... → Continuous Improvement

Architecture v0.2 core flow
Intent → Domain Model → Use Case → Contract → ... → Governed Improvement

Domain modeling flow
Product Intent → Business Capability → ... → Ports → Adapters

Development Loop
Explore → Plan → Implement → Verify → Review → Document → Deliver

Issue #6 required relation
Intent → Requirement → Capability → Use Case → Contract → ... → Evolution
```

These maps answer different questions, but the distinction is currently implicit.

The canonical model must classify them as:

- domain relationship map;
- delivery or execution lifecycle;
- modeling method;
- historical architecture view.

No one map should silently replace all others.

### 4.4 `Engineering Contract` mixes universal contract meaning with product policy

`docs/engineering-contract.md` describes a product-specific stack, security, test, and review agreement. It is useful, but it is not the parent type for every core contract.

Candidate interpretation:

```text
Contract
  stable governed agreement

Product Engineering Contract
  product-owned policy and implementation agreement
  specializing core rules and contracts without redefining them
```

The canonical model should preserve both without allowing a product engineering contract to become universal core.

### 4.5 Port and adapter meanings are directionally correct but not fully typed

Current documentation uses `port` for:

- external provider integration;
- repository and storage capability;
- control-plane capability;
- product-surface capability;
- skill-composition capability.

It uses `adapter` for:

- provider integration;
- runtime implementation;
- product implementation;
- executable skill specialization;
- framework or UI technology mapping.

Issue `#6` should define the base relationship and ownership rules. Issue `#7` should define the final port and adapter subtype taxonomy and machine-readable port contracts.

### 4.6 Evidence and completion are still distributed across many artifacts

Current documents correctly warn that one check does not prove complete behavior, but no shared domain relation currently binds:

```text
Claim
Evidence item
Evidence method
Scope
Coverage
Verification result
Validation result
Evaluation result
Review finding
Gate result
Approval
Completion claim
```

Without this relation, downstream implementations can still collapse evidence into an output blob, review into a boolean, or one green check into completion.

### 4.7 Learning and core evolution need an explicit promotion boundary

The philosophy defines:

```text
feedback
→ affected-layer update
→ learning
→ learning candidate
→ transferability and compatibility review
→ accepted target-layer change
```

The domain model must make this a governed relationship. A product result, adapter fix, runtime observation, or single field test may create a learning candidate; it may not directly mutate canonical core meaning.

---

## 5. Modeling rules derived from philosophy

The canonical domain model must satisfy these rules.

### D1 — Observation and representation remain separate

A source record, repository inspection, command result, screenshot, model response, or runtime event becomes an `Observation` with attributable source, method, time, environment, and coverage.

It does not become `State`, `Fact`, `Decision`, or `Evidence` merely because it exists.

### D2 — Claims and evidence are separate related objects

A `Claim` expresses a proposition.

An `EvidenceItem` has:

```text
source
method
time or version
environment
scope
coverage
integrity or reliability notes
supported or challenged claim relation
```

Evidence does not own approval or complete truth.

### D3 — Capability, permission, authority, and capacity are not one field

An actor may have capability without permission, permission without authority, and both without enough capacity for safe execution.

`CapacityAssessment` is contextual and may include:

```text
context availability
capability
required tools
permission
authority
risk controls
time and scope budget
verification path
review coverage
reversibility and recovery
```

### D4 — Decision, effective decision, review, and approval remain separate

A `Decision` records a selected or rejected option.

A policy determines whether it becomes effective based on source, authority, scope, conflicts, required approvals, and conditions.

A `ReviewResult` produces findings or a verdict.

An `Approval` is an authority-bearing decision permitting a named action, transition, claim, release, risk acceptance, or canonical change.

### D5 — Status is typed by domain concern

The canonical model must not use one generic status for epistemic, execution, gate, review, approval, delivery, and completion state.

Candidate status families include:

```text
EpistemicStatus
ExecutionStatus
GateOutcome
ReviewDisposition
ApprovalStatus
DeliveryStatus
CompletionStatus
EvolutionStatus
```

The exact enum values may remain documentation-level until issue `#8` defines schemas.

### D6 — Completion is a bounded claim

A `CompletionClaim` must identify:

```text
objective and accepted criteria
scope and exclusions
supporting evidence references
verification and validation coverage
required review and approval state
known limitations
completion disposition
```

Candidate dispositions must preserve at least:

```text
incomplete
partial
blocked
not_verified
complete_with_limitations
complete
```

### D7 — Feedback updates the smallest correct layer

A feedback item may update a local plan, implementation, product policy, adapter, skill, workflow, knowledge artifact, or canonical proposal depending on ownership.

Promotion to shared core requires a distinct `LearningCandidate` and governed `EvolutionProposal` with transferability, counterexample, compatibility, consumer-impact, and authority review.

---

## 6. Candidate bounded contexts

The following candidate contexts reduce overlap while preserving the concepts required by issue `#6`.

They are discovery candidates, not yet accepted canonical contexts.

### 6.1 Intent & Specification

Owns:

```text
Intent
Requirement
AcceptanceCriterion
Constraint
NonGoal
RiskStatement
SuccessMeasure
```

Responsibilities:

- preserve attributable requested intent separately from inferred intent;
- define accepted scope and non-goals;
- translate intent into verifiable requirements and acceptance criteria;
- avoid treating a plan or implementation as evidence that intent was satisfied.

Does not own:

- implementation method;
- runtime execution;
- final approval or delivery evidence.

### 6.2 Capability & Agreement

Owns:

```text
DomainCapability
UseCase
ContractIdentity
ContractVersion
ContractBoundary
QualityGateDefinition
CompatibilityExpectation
```

Responsibilities:

- define stable capability meaning and governed agreements;
- connect use cases to required capabilities;
- define required inputs, allowed outputs, gates, boundaries, and compatibility;
- keep contract presence separate from implementation and conformance.

Does not own:

- executable methodology;
- concrete providers;
- product-specific adapter selection.

### 6.3 Method & Workflow

Owns:

```text
SkillDefinition
WorkflowDefinition
PhaseDefinition
TransitionRule
HandoffDefinition
ExitCondition
MethodSelection
```

Responsibilities:

- define reusable executable methods and ordered lifecycle composition;
- distinguish atomic capability method from multi-phase workflow;
- coordinate gates, handoffs, and evidence expectations;
- keep the Epistemic Loop distinct from delivery workflows and the Development Loop.

Does not own:

- provider binding;
- runtime process state;
- approval authority.

### 6.4 Integration & Binding

Owns the base concepts:

```text
PortReference
AdapterBinding
ProviderBinding
ProductBinding
ImplementationRequirement
BindingCompatibility
```

Responsibilities:

- bind abstract capability requirements to replaceable implementation;
- preserve upstream domain and contract meaning;
- declare limitations, delegated responsibilities, and compatibility;
- prevent implementation access from implying authority.

Issue `#7` owns the final port kinds, adapter kinds, dependency rules, and first-class port contract shape.

### 6.5 Runtime & Execution

Owns:

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
```

Responsibilities:

- execute or route authorized work;
- record actual state transitions and tool outcomes;
- preserve plan, execution, and result as distinct concepts;
- produce attributable execution evidence;
- represent blocked, failed, cancelled, partial, and successful outcomes honestly.

Does not own:

- canonical domain meaning;
- approval merely because execution is technically possible;
- product acceptance.

### 6.6 Context, Knowledge & Memory

Owns:

```text
ContextRequest
ContextPack
SourceReference
KnowledgeItem
MemoryReference
ContextGap
StalenessAssessment
```

Responsibilities:

- provide relevant attributable context;
- preserve source, recency, scope, and authority;
- distinguish accepted knowledge from memory and inference;
- report missing or stale context rather than inventing facts.

Does not own:

- the upstream authoritative source itself;
- approval or current state without verification.

### 6.7 Evidence, Evaluation & Review

Owns:

```text
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

Responsibilities:

- relate claims to typed and scoped evidence;
- evaluate against declared criteria;
- separate verification, validation, evaluation, review, gate outcome, and completion;
- preserve limitations and evidence coverage;
- provide findings without silently granting approval.

Does not own:

- authority-bearing approval unless explicitly delegated by governance policy;
- runtime execution itself.

### 6.8 Governance, Risk & Authority

Owns:

```text
Policy
Rule
AuthorityGrant
PermissionGrant
Decision
Approval
RiskAssessment
RiskAcceptance
Exception
Delegation
```

Responsibilities:

- define who may bind, approve, reject, delegate, supersede, or accept risk;
- determine whether a decision is effective;
- apply proportionate review and approval requirements;
- distinguish technical permission from authority;
- govern exceptions and canonical changes.

Does not own:

- evidence production;
- implementation merely because it governs it.

### 6.9 Product, Delivery & Registry

Owns the runtime-agnostic base relation for:

```text
ProductInstance
ProductIntentReference
ProductPolicyReference
ProductBindingRegistry
DeliveryCandidate
DeliveryRecord
ReleaseAcceptance
ConsumerImpact
```

Responsibilities:

- bind reusable core capabilities to product-owned policy and implementation;
- keep private product context and customer data outside universal core;
- record delivery and product acceptance separately from technical execution;
- identify affected consumers and product-specific acceptance authority.

Product repositories own concrete business policy, implementation, configuration, and validation.

### 6.10 Learning & Evolution

Owns:

```text
FeedbackItem
AffectedLayer
UpdateRecord
LearningRecord
LearningCandidate
EvolutionProposal
TransferabilityAssessment
CompatibilityImpact
EvolutionDecision
```

Responsibilities:

- route feedback to the smallest correct layer;
- distinguish local update from reusable learning;
- require multiple contexts and counterexamples before broad promotion;
- preserve compatibility and consumer-impact review;
- prevent local adapters, runtimes, products, or field tests from silently redefining core.

---

## 7. Candidate aggregate boundaries

These are candidate consistency boundaries for the canonical model.

### IntentSpecification aggregate

Root candidate: `IntentSpecification`

Contains or references:

```text
Intent
Requirement
AcceptanceCriterion
Constraint
NonGoal
SuccessMeasure
```

Key invariants:

- every acceptance criterion traces to a requirement or accepted intent;
- inferred intent is labeled and cannot silently replace attributable intent;
- non-goals remain explicit when scope changes.

### CapabilityAgreement aggregate

Root candidate: `CapabilityAgreement`

Contains or references:

```text
DomainCapability
UseCase
ContractIdentity
ContractVersion
Boundary
GateDefinition
CompatibilityExpectation
```

Key invariants:

- contract identity is stable and versioned;
- inputs, outputs, gates, and boundary remain distinguishable;
- contract presence does not mark implementation or conformance complete.

### WorkflowDefinition aggregate

Root candidate: `WorkflowDefinition`

Contains or references:

```text
PhaseDefinition
TransitionRule
HandoffDefinition
ExitCondition
SkillRequirement
EvidenceRequirement
```

Key invariants:

- transitions identify applicable gates;
- handoffs identify ownership and required artifacts;
- workflow and Development Loop semantics are not silently collapsed.

### ExecutionRun aggregate

Root candidate: `ExecutionRun`

Contains or references:

```text
ExecutionStep
Actor
RuntimeEnvironment
ToolInvocation
ExecutionArtifact
RuntimeEvent
ExecutionStatus
CapacityAssessment
```

Key invariants:

- planned work is not recorded as executed;
- actual tool outcomes remain attributable;
- completion is not derived from execution status alone;
- capability or permission does not imply authority.

### EvidenceCase aggregate

Root candidate: `EvidenceCase`

Contains or references:

```text
Claim
EvidenceItem
Scope
Coverage
VerificationResult
ValidationResult
EvaluationResult
ReviewResult
GateResult
CompletionClaim
```

Key invariants:

- evidence references a claim and bounded scope;
- review remains separate from approval;
- one evidence layer does not imply all other layers;
- completion preserves limitations and missing coverage.

### AuthorityDecision aggregate

Root candidate: `AuthorityDecision`

Contains or references:

```text
Decision
AuthorityGrant
Approval
RiskAcceptance
Condition
Scope
ConflictReference
```

Key invariants:

- newest or most convenient decision is not automatically effective;
- approval requires verified authority and applicable scope;
- review verdict is not approval unless governance explicitly assigns that meaning.

### LearningEvolution aggregate

Root candidate: `LearningEvolutionCase`

Contains or references:

```text
FeedbackItem
LearningRecord
LearningCandidate
TransferabilityAssessment
CompatibilityImpact
EvolutionProposal
EvolutionDecision
```

Key invariants:

- feedback does not directly mutate shared agreements;
- one success is insufficient for shared promotion;
- core evolution requires core authority and compatibility handling.

Other contexts may use smaller aggregates or references rather than creating one large cross-context aggregate.

---

## 8. Candidate commands and events

### Commands

```text
RecordIntent
DefineRequirement
AcceptAcceptanceCriterion
RegisterCapabilityAgreement
SelectMethod
StartWorkflow
BindAdapter
AssessCapacity
AuthorizeExecution
StartExecutionRun
RecordObservation
SubmitClaim
AttachEvidence
VerifyClaim
ValidateUse
EvaluateArtifact
RequestReview
RecordReviewFinding
IssueApproval
RecordDelivery
SubmitFeedback
CreateLearningCandidate
ProposeEvolution
AcceptEvolution
```

### Events

```text
IntentRecorded
RequirementAccepted
CapabilityAgreementRegistered
WorkflowStarted
AdapterBound
CapacityAssessed
ExecutionAuthorized
ExecutionRunStarted
ExecutionStepCompleted
ExecutionBlocked
EvidenceAttached
ClaimVerified
ValidationCompleted
EvaluationCompleted
ReviewCompleted
ApprovalIssued
DeliveryRecorded
FeedbackReceived
LearningCandidateCreated
EvolutionProposed
EvolutionAccepted
CanonicalAgreementSuperseded
```

Event naming should describe completed domain facts. Issue `#8` will own canonical event serialization and schema rules where applicable.

---

## 9. Candidate policies

```text
IntentTraceabilityPolicy
ContractCompatibilityPolicy
BindingSelectionPolicy
CapacityPolicy
ExecutionAuthorizationPolicy
EvidenceSufficiencyPolicy
GateEvaluationPolicy
ReviewRequirementPolicy
ApprovalAuthorityPolicy
CompletionPolicy
DeliveryAcceptancePolicy
LearningPromotionPolicy
CoreEvolutionPolicy
```

Policies own decisions that depend on several objects or contexts. They must not become miscellaneous containers for unresolved ownership.

---

## 10. Canonical lifecycle relationship candidate

The required issue lifecycle can be represented as related records rather than one monolithic state machine:

```text
IntentSpecification
→ Requirement and AcceptanceCriterion
→ DomainCapability and UseCase
→ CapabilityAgreement / Contract
→ Port requirement and AdapterBinding
→ WorkflowDefinition and SkillDefinition
→ CapacityAssessment and ExecutionAuthorization
→ ExecutionRun
→ Claim and EvidenceCase
→ GateResult, ReviewResult, and Approval where required
→ DeliveryRecord and Product Acceptance
→ FeedbackItem
→ LearningCandidate
→ accepted target-layer update or governed EvolutionProposal
```

Important transition boundaries:

```text
intent acceptance does not authorize execution;
contract presence does not prove implementation;
adapter binding does not prove runtime readiness;
execution success does not prove product validity;
review does not grant approval by default;
delivery does not prove business outcome;
feedback does not equal accepted evolution.
```

The Development Loop remains an execution-cycle method used within delivery work. The Epistemic Loop remains a reasoning discipline used inside domain activities. Neither becomes the whole canonical domain lifecycle.

---

## 11. Ownership and dependency direction candidate

```text
Philosophy and atomic terms
  constrain domain meaning
        ↓
Canonical domain model
  owns objects, relationships, contexts, lifecycle, and invariants
        ↓
Contracts and ports
  serialize stable agreements and capability boundaries
        ↓
Skills, workflows, and adapters
  implement or compose reusable behavior
        ↓
Runtime and control plane
  orchestrate authorized execution and evidence capture
        ↓
Product repositories
  own product policy, implementation, bindings, and acceptance
        ↓
Field evidence
  may create affected-layer updates and learning candidates
        ↘ governed proposal only
Canonical evolution
```

Prohibited direction:

```text
provider → universal domain meaning
adapter → canonical term redefinition
runtime access → authority
product policy → universal core by default
single test → shared contract mutation
memory → current source of truth
review result → approval without authority
```

---

## 12. Existing document role reconciliation

### `docs/philosophy/**`

Role: accepted philosophy, atomic vocabulary, laws, principles, guardrails, epistemic loop, and source-role governance.

Action: referenced by the canonical domain model; not rewritten by issue `#6`.

### `docs/domain-driven-model.md`

Role candidate: general domain-driven modeling guide with product examples.

Action: mark it as a guide and point it to the canonical Native AI Engineering domain model. Do not treat its illustrative product model as universal.

### `docs/architecture-v0.2.md`

Role: operational architecture and dependency view.

Action: preserve the layer view but point domain ownership and canonical terminology to the accepted domain model. Layer numbering is not bounded-context authority.

### `docs/engineering-contract.md`

Role candidate: product engineering agreement guidance.

Action: qualify it as product- or repository-owned specialization of stable core agreements, not the universal root contract type.

### `docs/ports-and-adapters.md`

Role: architecture pattern and examples.

Action: point base definitions to the canonical domain model and final taxonomy to issue `#7`.

### `docs/development-loop.md`

Role: execution-cycle method.

Action: preserve it as distinct from workflow definitions, domain lifecycle, and the Epistemic Loop.

### `docs/glossary.md`

Role: navigation and short labels.

Action: point philosophy terms to term authority and domain objects to the canonical model. It must not become a competing atomic or object-definition authority.

---

## 13. Deferred decisions

Issue `#6` should not decide:

```text
final port kinds and adapter subtype taxonomy           #7
canonical machine schemas and workflow root shape       #8
structured validator-v2 result and evidence semantics   #9
repository-wide downstream contract migration           skills #26
reference runtime behavior harness                       skills #27
provider, framework, or product implementation choices
```

It should provide stable names, ownership, relationships, and invariants that those issues consume.

---

## 14. Discovery verdict

```text
Accepted philosophy input:                  READY
Existing domain concepts:                   STRONG BUT DISTRIBUTED
Canonical bounded contexts:                 MISSING
Canonical aggregate relationships:          MISSING
Evidence and authority distinctions:        AVAILABLE FROM PHILOSOPHY
Current lifecycle maps:                      USEFUL BUT UNCLASSIFIED
Operational layer view:                     USEFUL BUT NOT DOMAIN AUTHORITY
Port/adapter base relationship:              READY FOR DOMAIN DEFINITION
Final port taxonomy:                         DEFER TO #7
Contract schema changes:                     NOT REQUIRED FOR DISCOVERY
Ready to implement canonical domain model:  YES
```

The smallest next slice should create one canonical domain-model entry point that:

1. accepts a reviewed bounded-context set;
2. defines core object meanings and relationships;
3. records aggregates, invariants, policies, commands, and events;
4. defines the canonical lifecycle and typed status families;
5. supplies philosophy-to-domain traceability;
6. reconciles architecture and glossary navigation without rewriting all contracts.

No contract path, version, manifest entry, validator, or runtime behavior should change until a separately owned downstream issue requires it.
