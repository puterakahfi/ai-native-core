# Native AI Engineering Domain Objects

Status: Proposed canonical object model for issue `#6`

Entry point: [`README.md`](README.md)

Bounded contexts: [`bounded-contexts.md`](bounded-contexts.md)

This document defines the first-class entities, value objects, aggregates, policies, commands, events, and invariants of Native AI Engineering.

The model is runtime-agnostic and product-agnostic. Issue `#8` owns future machine-readable schemas.

---

## 1. Modeling conventions

### Entity

An object with stable identity and lifecycle.

### Value object

An immutable value defined by its content rather than identity.

### Aggregate

A consistency boundary with one aggregate root controlling invariant-preserving changes.

### Policy

A named decision rule spanning several objects or contexts.

### Command

A request to perform a domain action.

### Event

A completed domain-relevant occurrence stated in past tense.

### Reference

A stable identifier or snapshot pointing to an object owned by another context. A reference does not transfer ownership.

---

## 2. Shared value objects

These values are reused across contexts.

### ObjectId

Stable identity for a domain object.

### Scope

Explicit boundary of subjects, actions, claims, environments, time, consumers, risks, and responsibilities.

### Coverage

Portion of declared scope actually observed, executed, evaluated, reviewed, or supported by evidence.

### SourceReference

Attributable origin with source kind, location or identifier, observed version or time, authority notes, and retrieval method.

### TimeRange

Bounded point or interval relevant to observation, validity, execution, approval, or delivery.

### VersionReference

Artifact identity plus version, revision, commit, checksum, or compatibility range.

### Limitation

Known boundary, uncertainty, unsupported claim, missing coverage, or residual risk.

### ActorReference

Reference to a person, agent, team, organization, runtime process, or system actor.

### AuthorityReference

Reference to the source and scope of recognized decision authority.

### EvidenceReference

Reference to an evidence item without copying or re-owning it.

### ProductReference

Reference to a product instance and its source-of-truth boundary.

---

## 3. Intent & Specification objects

### Intent — entity

Identity-bearing record of an attributable desired outcome, problem, need, constraint, or direction.

Required relations:

```text
source
scope
requested outcome or problem
known constraints
recorded time or version
```

An inferred interpretation of intent is recorded separately.

### Requirement — entity

A condition that must be satisfied.

Required relations:

```text
source intent or governing policy
scope
priority or criticality
verification expectation
supersession history
```

### AcceptanceCriterion — entity

A checkable condition determining whether a requirement or objective is satisfied within scope.

Required relations:

```text
requirement reference
criterion
verification or validation method
required evidence kind
```

### Constraint — value object

A bounded restriction on solution, method, environment, risk, time, budget, compatibility, or policy.

### NonGoal — value object

An explicitly excluded outcome or adjacent concern.

### SuccessMeasure — value object

A named measure with definition, method, target, time window, and guardrail where applicable.

### IntentSpecification — aggregate root

Controls:

```text
Intent
Requirement
AcceptanceCriterion
Constraint
NonGoal
SuccessMeasure
RiskStatement
```

Invariants:

1. Each acceptance criterion traces to a requirement or accepted intent.
2. Inferred intent is labeled and cannot overwrite attributable intent silently.
3. Scope changes preserve prior decision and supersession history.
4. Non-goals remain visible when requirements evolve.
5. A requirement is not marked satisfied without the required evidence relation.

---

## 4. Capability & Agreement objects

### DomainCapability — entity

A stable ability required by the domain, independent of concrete provider, runtime, tool, or framework.

### UseCase — entity

Goal-oriented application of capabilities for a named actor or system boundary.

Required relations:

```text
intent or requirement
actor
preconditions
capability references
outcome
acceptance references
```

### ContractIdentity — entity

Stable identifier of a governed agreement.

### ContractVersion — entity

Versioned revision of a contract identity with compatibility meaning.

### ContractBoundary — value object

Owned responsibility and explicitly delegated or excluded responsibility.

### InputRequirement — value object

Required or optional input with meaning and constraints.

### OutputAllowance — value object

Allowed result kind and its semantic boundary.

### QualityGateDefinition — entity

Stable gate identity, criterion, evidence expectation, and failure meaning.

### CompatibilityExpectation — value object

Accepted consumer range, breaking-change boundary, and migration expectation.

### CapabilityAgreement — aggregate root

Controls:

```text
DomainCapability
UseCase references
ContractIdentity
ContractVersion
InputRequirement
OutputAllowance
QualityGateDefinition
ContractBoundary
CompatibilityExpectation
```

Invariants:

1. Contract identity and version are explicit.
2. Required inputs, allowed outputs, gates, and boundaries remain separately inspectable.
3. A delegated responsibility cannot be claimed as owned by the same agreement.
4. Breaking semantic change requires compatible versioning and migration handling.
5. Contract registration does not set implementation, conformance, embodiment, or product maturity state.

---

## 5. Method & Workflow objects

### SkillDefinition — entity

Definition of a reusable executable procedure or specialist method for a bounded capability.

Required relations:

```text
capability agreement
method boundary
required context
steps or procedure reference
quality and evidence expectations
handoffs
```

### WorkflowDefinition — aggregate root

Controls:

```text
PhaseDefinition
TransitionRule
HandoffDefinition
ExitCondition
SkillRequirement
EvidenceRequirement
```

### PhaseDefinition — entity

Named lifecycle segment with purpose, expected outputs, ownership, gates, and allowed transitions.

### TransitionRule — value object

Source phase, target phase, preconditions, gates, and failure or return path.

### HandoffDefinition — value object

Sender, receiver, artifact or state transferred, required context, acceptance condition, and ownership change if any.

### ExitCondition — value object

Checkable condition required to leave a phase or workflow.

### MethodSelection — entity

Decision record selecting a skill, workflow, or method for a use case under constraints.

Workflow invariants:

1. Every transition names its applicable gate or explicit no-gate rationale.
2. Handoffs identify receiver and required artifact or evidence.
3. A workflow definition is not an execution run.
4. A skill or workflow does not acquire approval authority merely by being selected.
5. Epistemic Loop and Development Loop references remain supporting mechanisms, not competing workflow definitions.

---

## 6. Integration & Binding objects

### PortReference — entity

Reference to an abstract capability boundary requested by a consumer context.

The exhaustive port taxonomy is deferred to issue `#7`.

### AdapterBinding — aggregate root

Controls:

```text
port or contract reference
adapter identity and kind
runtime, provider, product, or framework target
compatibility record
limitations
delegated responsibilities
implementation requirements
```

### AdapterKind — value object

Minimum accepted base kinds:

```text
skill_adapter
runtime_adapter
provider_adapter
product_adapter
framework_adapter
```

Issue `#7` may add or refine subtypes.

### BindingCompatibility — value object

Compatibility between adapter, contract or port, runtime, provider, and product constraints.

### BindingLimitation — value object

Unsupported operation, risk, missing capability, environmental restriction, or required handoff.

Binding invariants:

1. Adapter binding preserves upstream meaning and boundary.
2. Provider or framework capability does not imply product authorization.
3. Concrete credentials and private configuration remain outside core.
4. Binding incompatibility or limitation is disclosed rather than hidden by translation.
5. Adapter access does not imply authority.

---

## 7. Runtime & Execution objects

### RuntimeEnvironment — entity

Execution surface with identity, version, configuration reference, supported capabilities, registered tools, and operational constraints.

### Actor — entity

Person, team, agent, service, or runtime process participating in domain action.

### Agent — entity specialization

AI actor with assigned responsibilities, capabilities, and runtime identity.

### ToolRegistration — entity

Runtime registration of a tool, operation surface, permission boundary, and adapter reference.

### CapacityAssessment — entity

Contextual assessment of whether a bounded action can be performed responsibly.

Required dimensions:

```text
context availability
capability
tool availability
permission
authority
risk controls
time and scope budget
verification path
review coverage
reversibility and recovery
```

### ExecutionRun — aggregate root

Controls:

```text
ExecutionStep
ExecutionStatus
ToolInvocation
ExecutionArtifact
RuntimeEvent
CapacityAssessment reference
ExecutionAuthorizationReference
workflow and method references
```

### ExecutionStep — entity

One actual step with actor, start/end, inputs or references, action, result, and evidence references.

### ToolInvocation — entity

Actual request to a registered tool plus returned outcome, error, and environment information.

### ExecutionArtifact — entity

Artifact produced, modified, or consumed by execution with path or identifier, version, and provenance.

### RuntimeEvent — event record

Runtime-relevant occurrence such as start, block, retry, tool result, failure, cancellation, or completion of an execution step.

Execution invariants:

1. Requested, planned, authorized, running, and completed are distinct states.
2. A tool proposal is not a tool invocation.
3. Tool invocation outcome is recorded, including failure and uncertainty.
4. Successful execution does not automatically create product validation or complete delivery.
5. Execution cannot claim authority absent an authority reference.
6. Execution status cannot substitute for completion disposition.

---

## 8. Context, Knowledge & Memory objects

### ContextRequest — entity

Request for context needed by a task, workflow, decision, or execution run.

### ContextPack — aggregate root

Controls:

```text
SourceReference
KnowledgeItem reference
MemoryReference
ContextGap
StalenessAssessment
ContextValidationResult
```

### KnowledgeItem — entity

Explicit reviewable information accepted for use within scope and maintained in a source-of-truth artifact or system.

### MemoryReference — entity

Reference to retained context, history, preference, pattern, or prior outcome used for retrieval or reasoning.

### ContextGap — entity

Relevant missing, inaccessible, contradictory, stale, or insufficient context.

### StalenessAssessment — value object

Assessment of currentness with observed version or time, expected freshness, and consequence.

Context invariants:

1. Every material item preserves its source reference.
2. Memory does not silently supersede knowledge.
3. Missing or stale context is represented explicitly.
4. Context-pack inclusion does not transfer source ownership.
5. Unattributed summaries cannot become accepted knowledge by convenience.

---

## 9. Evidence, Evaluation & Review objects

### Claim — entity

Explicit proposition about state, behavior, meaning, quality, causality, authority, completion, or result.

### EvidenceItem — entity

Typed attributable information related to one or more claims.

Required values:

```text
source
method
time or version
environment
scope
coverage
integrity or reliability notes
supports, weakens, distinguishes, or challenges relation
```

### EvidenceCase — aggregate root

Controls:

```text
Claim
EvidenceItem reference
EvidenceScope
Coverage
VerificationResult
ValidationResult
EvaluationResult
ReviewResult
GateResult
CompletionClaim
```

### VerificationResult — entity

Result of determining whether a specified claim, requirement, property, contract, or result is supported by appropriate evidence.

### ValidationResult — entity

Result of determining fitness for intended use, context, need, and acceptance scope.

### EvaluationResult — entity

Assessment against declared criteria with findings, measurements, evidence, and optional verdict.

### ReviewRequest — entity

Request for qualified examination with subject, criteria, scope, reviewer requirement, and expected output.

### ReviewResult — entity

Findings or verdict produced by review. It is not approval unless linked to an explicit authority-bearing policy.

### Finding — entity

Observed issue, strength, uncertainty, contradiction, or recommendation with severity and evidence references.

### GateResult — entity

Outcome of one declared gate for one subject and scope with criterion, evidence, result, and limitations.

### CompletionClaim — entity

Bounded claim that accepted objectives and in-scope criteria are satisfied.

Required relations:

```text
objective and criteria
scope and exclusions
evidence references
verification and validation coverage
required review and approval state
known limitations
completion disposition
```

Evidence invariants:

1. Claim and evidence remain separate objects.
2. Evidence names scope and coverage.
3. Verification, validation, evaluation, review, and approval are not interchangeable.
4. One evidence layer cannot imply untested layers.
5. Completion requires limitations and unmet coverage to remain visible.
6. Review result does not create authority by itself.

---

## 10. Governance, Risk & Authority objects

### Policy — entity

Governed decision rule applying to a named scope.

### Rule — entity

Mandatory constraint stating what must or must not happen in scope.

### PermissionGrant — entity

Technical, policy, or access-control allowance to attempt a named operation.

### AuthorityGrant — entity

Recognized decision right to bind, approve, reject, delegate, supersede, or constrain action, risk, claim, or canonical meaning.

### Decision — entity

Recorded selection, rejection, commitment, or constraint among alternatives.

### EffectiveDecisionAssessment — entity

Assessment of whether a decision has verified source, applicable authority, covered scope, required approvals, and resolved conflicts.

### Approval — entity

Authority-bearing positive decision permitting a named action, transition, release, claim, risk acceptance, or canonical change under conditions.

### RiskAssessment — entity

Assessment of likelihood, impact, reversibility, controls, exposure, and residual risk.

### RiskAcceptance — entity

Authority-bearing decision accepting a named risk within scope and conditions.

### Exception — entity

Governed deviation from a rule, contract, gate, or policy with authority, scope, rationale, conditions, and expiry.

### Delegation — entity

Transfer of a bounded responsibility or decision right without transferring upstream ownership by default.

### AuthorityDecision — aggregate root

Controls:

```text
Decision
AuthorityGrant reference
EffectiveDecisionAssessment
Approval
RiskAcceptance
Exception
Condition
Scope
ConflictReference
```

Governance invariants:

1. Capability, permission, and authority remain separate.
2. Newest or easiest decision is not automatically effective.
3. Approval identifies authority, scope, subject, conditions, and validity.
4. Review is not approval absent explicit governing policy.
5. Risk acceptance requires applicable authority.
6. Exceptions are explicit and time- or condition-bounded.

---

## 11. Product, Delivery & Registry objects

### ProductInstance — entity

Product-specific source-of-truth boundary for product intent, policy, configuration, implementation, bindings, and validation.

### ProductBindingRegistry — aggregate root

Controls product references to:

```text
capability agreements
workflow and skill selections
adapter bindings
provider and runtime bindings
product policy
implementation location
acceptance authority
```

Core owns only the runtime-agnostic relation. Product repositories own concrete data.

### DeliveryCandidate — entity

Artifact or change proposed for delivery with target, version, evidence, and required gates.

### DeliveryRecord — entity

Recorded delivery to a branch, environment, registry, release, or consumer boundary.

### ReleaseAcceptance — entity

Product- or organization-owned acceptance result for a delivery candidate.

### ConsumerImpact — value object

Affected consumers, compatibility effect, migration need, risk, and communication requirement.

### ProductDeliveryCase — aggregate root

Controls or references:

```text
ProductInstance
DeliveryCandidate
DeliveryRecord
ReleaseAcceptance
ConsumerImpact
ProductValidationReference
```

Delivery invariants:

1. Technical delivery remains separate from release acceptance and business outcome.
2. Product policy and private context remain outside universal core.
3. A product binding cannot redefine core meaning silently.
4. A delivery record identifies actual target and version.
5. Consumer impact is assessed for shared or breaking changes.

---

## 12. Learning & Evolution objects

### FeedbackItem — entity

Attributable information from observation, execution, evaluation, review, use, measurement, or consequence.

### AffectedLayer — value object

Smallest layer or artifact class whose model, behavior, implementation, knowledge, agreement, or policy may need change.

### UpdateRecord — entity

Traceable local or shared change in response to accepted feedback, evidence, or authority.

### LearningRecord — entity

Evaluated change in future interpretation, decision, or repeatable behavior.

### LearningCandidate — entity

Proposal that a verified lesson may transfer beyond the source case.

### TransferabilityAssessment — entity

Assessment across multiple contexts, counterexamples, scope boundaries, and failure conditions.

### CompatibilityImpact — entity

Affected consumers, semantic change, version or migration need, and risk.

### EvolutionProposal — entity

Proposal for governed change to knowledge, skill, workflow, contract, port, domain, philosophy, or another shared layer.

### EvolutionDecision — entity

Authority-bearing acceptance, rejection, narrowing, or deferral of an evolution proposal.

### LearningEvolutionCase — aggregate root

Controls:

```text
FeedbackItem
AffectedLayer
UpdateRecord
LearningRecord
LearningCandidate
TransferabilityAssessment
CompatibilityImpact
EvolutionProposal
EvolutionDecision
```

Evolution invariants:

1. Feedback is not learning automatically.
2. One local success is not transferable proof.
3. A learning candidate identifies the smallest correct target layer.
4. Shared promotion requires counterexamples and compatibility impact.
5. Core evolution requires core authority.
6. Rejected or narrowed proposals preserve rationale and evidence.

---

## 13. Canonical policies

### IntentTraceabilityPolicy

Determines whether requirements and acceptance criteria remain attributable to accepted intent.

### ContractCompatibilityPolicy

Determines compatibility impact, versioning, and migration requirement for contract change.

### MethodSelectionPolicy

Selects an appropriate skill or workflow based on use case, constraints, and risk.

### BindingSelectionPolicy

Selects a compatible adapter or provider binding without leaking implementation meaning upstream.

### CapacityPolicy

Determines whether current context, capability, tools, permission, authority, controls, evidence path, review, reversibility, and recovery are sufficient for action.

### ExecutionAuthorizationPolicy

Determines whether a named execution run may begin.

### EvidenceSufficiencyPolicy

Determines whether evidence type, scope, coverage, integrity, and method support a claim or gate.

### GateEvaluationPolicy

Evaluates one declared gate and records its bounded outcome.

### ReviewRequirementPolicy

Determines required review based on subject, contract, risk, reversibility, affected consumers, and claim scope.

### ApprovalAuthorityPolicy

Determines who may approve which action or transition under which conditions.

### CompletionPolicy

Determines completion disposition from accepted criteria, evidence, validation, review, approval, and disclosed limitations.

### DeliveryAcceptancePolicy

Determines whether a delivery candidate may move into a target consumer boundary.

### LearningPromotionPolicy

Determines whether a lesson remains local, updates knowledge, or becomes a shared evolution proposal.

### CoreEvolutionPolicy

Determines whether a core-owned agreement may change and what compatibility, validation, and authority are required.

---

## 14. Canonical commands

```text
RecordIntent
ClarifyIntent
DefineRequirement
AcceptAcceptanceCriterion
RegisterCapabilityAgreement
ReviseContractVersion
SelectMethod
StartWorkflow
BindAdapter
AssembleContextPack
AssessCapacity
AuthorizeExecution
StartExecutionRun
RecordToolInvocation
RecordObservation
SubmitClaim
AttachEvidence
VerifyClaim
ValidateUse
EvaluateSubject
RequestReview
RecordReviewResult
EvaluateGate
IssueApproval
AcceptRisk
DeclareCompletion
RegisterDeliveryCandidate
RecordDelivery
AcceptRelease
SubmitFeedback
RecordLearning
CreateLearningCandidate
ProposeEvolution
AcceptEvolution
RejectEvolution
```

Commands are requests. They do not prove that the action occurred.

---

## 15. Canonical events

```text
IntentRecorded
IntentClarified
RequirementDefined
AcceptanceCriterionAccepted
CapabilityAgreementRegistered
ContractVersionRevised
MethodSelected
WorkflowStarted
AdapterBound
ContextPackAssembled
CapacityAssessed
ExecutionAuthorized
ExecutionRunStarted
ToolInvoked
ObservationRecorded
ExecutionBlocked
ExecutionFailed
ExecutionRunCompleted
ClaimSubmitted
EvidenceAttached
ClaimVerified
ValidationCompleted
EvaluationCompleted
ReviewCompleted
GateEvaluated
ApprovalIssued
RiskAccepted
CompletionDeclared
DeliveryCandidateRegistered
DeliveryRecorded
ReleaseAccepted
FeedbackReceived
LearningRecorded
LearningCandidateCreated
EvolutionProposed
EvolutionAccepted
EvolutionRejected
CanonicalAgreementSuperseded
```

Events describe completed occurrences and use past-tense names.

---

## 16. Cross-aggregate invariants

1. No material claim or action begins from invented state when relevant observation or explicit unknown is required.
2. Intent, requirement, capability, agreement, method, binding, execution, evidence, review, approval, delivery, and evolution remain traceable but separately owned.
3. No generic status field represents all epistemic, execution, gate, review, approval, delivery, completion, and evolution concerns.
4. No adapter, provider, runtime, or product silently redefines an upstream term or contract.
5. No execution success creates approval, product validation, or core evolution by implication.
6. No review result is treated as approval without verified authority and governing policy.
7. No evidence item supports a claim beyond its scope and coverage.
8. No local feedback directly mutates shared core.
9. No product-specific example becomes universal domain ownership.
10. Every shared breaking change identifies affected consumers, compatibility impact, migration, validation, and authority.
