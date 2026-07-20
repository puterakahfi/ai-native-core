# Native AI Engineering Lifecycle And Status Semantics

Status: Proposed canonical lifecycle model for issue `#6`

Entry point: [`README.md`](README.md)

Objects: [`domain-objects.md`](domain-objects.md)

The canonical lifecycle is a relationship model between separately owned records. It is not one giant state machine and does not replace delivery workflows, the Development Loop, or the Epistemic Loop.

---

## 1. Canonical lifecycle relationship

```text
IntentSpecification
→ Requirement and AcceptanceCriterion
→ DomainCapability and UseCase
→ CapabilityAgreement / Contract
→ Port requirement and AdapterBinding
→ WorkflowDefinition and SkillDefinition
→ ContextPack and CapacityAssessment
→ ExecutionAuthorization
→ ExecutionRun
→ Claim and EvidenceCase
→ GateResult
→ ReviewResult
→ Approval where required
→ CompletionClaim
→ DeliveryCandidate and DeliveryRecord
→ ReleaseAcceptance or ProductValidation
→ FeedbackItem
→ LearningRecord or LearningCandidate
→ accepted target-layer update or governed EvolutionProposal
```

The relationship is traceable, but each object keeps its own owner, invariant, status, and evidence.

---

## 2. Transition rules

### Intent to requirement

Requires:

- attributable intent or explicit inferred-intent label;
- accepted scope and non-goals;
- ambiguity resolved or preserved as explicit unknown;
- governing source and authority identified where material.

Does not imply:

- approval to implement;
- chosen solution;
- product validation.

### Requirement to capability and use case

Requires:

- requirement and acceptance criteria;
- domain meaning independent of one implementation;
- actor or system boundary;
- expected outcome.

Does not imply:

- contract exists;
- method or adapter chosen.

### Capability to agreement

Requires:

- stable capability identity;
- inputs, outputs, gates, and boundary;
- version and compatibility expectation;
- ownership and delegated responsibility.

Does not imply:

- executable implementation;
- adapter conformance;
- runtime readiness.

### Agreement to method and workflow

Requires:

- use-case needs and constraints;
- selected reusable method or workflow;
- required context, handoffs, gates, and evidence expectations.

Does not imply:

- execution started;
- tool access exists;
- approval granted.

### Method to binding

Requires:

- port or contract requirement;
- compatible adapter or implementation candidate;
- limitations and delegated responsibilities;
- product and runtime constraints.

Does not imply:

- authorization;
- safe execution capacity;
- successful integration.

### Binding to capacity assessment

Requires assessment of:

```text
context
capability
tools
permission
authority
risk controls
time and scope budget
verification path
review coverage
reversibility and recovery
```

A positive capacity assessment is contextual and time-bounded.

### Capacity to execution authorization

Requires:

- applicable authority or policy;
- allowed action and scope;
- accepted risk and conditions;
- capacity assessment sufficient for the action.

Technical permission alone is insufficient.

### Authorization to execution run

Requires:

- actual host mechanism starts or records execution;
- runtime and actor identity;
- requested scope and input references;
- execution start event.

A plan or model response is not an execution run.

### Execution to evidence case

Execution observations and artifacts become evidence only when:

- source and method are attributable;
- scope, environment, time, and version are recorded;
- coverage is known;
- relation to a claim is explicit.

Raw output may remain an artifact without being sufficient evidence.

### Evidence to gate result

Requires:

- declared gate definition;
- subject and scope;
- applicable evidence and coverage;
- evaluation method;
- result and limitations.

Passing one gate cannot imply all gates or full completion.

### Gate result to review

Review is required only when contract, policy, risk, reversibility, consumer impact, or claim scope requires it.

Review produces findings or a verdict. It does not automatically grant approval.

### Review to approval

Requires:

- policy assigning approval meaning;
- verified authority;
- applicable scope;
- resolved material conflicts;
- required evidence and conditions.

A positive review without authority remains a review result.

### Approval to completion claim

Completion evaluation requires:

- accepted objective and criteria;
- evidence references;
- verification and validation coverage;
- required gate, review, and approval state;
- known limitations and exclusions.

Approval may be required but is not sufficient for completion if criteria or evidence remain unmet.

### Completion to delivery

Requires:

- accepted delivery candidate;
- target branch, environment, registry, or consumer boundary;
- version and actual delivery record;
- rollback or recovery where applicable.

A completed artifact may remain undelivered.

### Delivery to product acceptance

Requires product-owned validation and authority.

Technical delivery does not prove:

- intended use fitness;
- user acceptance;
- business outcome;
- production adoption.

### Feedback to learning and evolution

Feedback first identifies the affected layer.

Possible outcomes:

```text
no change
local model or plan update
implementation correction
product policy update
knowledge update
skill or workflow learning candidate
contract or domain evolution proposal
```

Shared promotion requires transferability, counterexamples, compatibility, consumer impact, and target-layer authority.

---

## 3. Typed status families

One generic `status` field is prohibited for all concerns.

The names below define minimum semantic families. Issue `#8` owns machine schemas and may refine serialization without collapsing the families.

### 3.1 EpistemicDisposition

Describes the current treatment of a proposition, not execution or approval.

Minimum values:

```text
unknown
assumed
inferred
not_verified
verified
disputed
superseded
```

Rules:

- `verified` is bounded by scope, method, time, version, and coverage;
- `assumed` and `inferred` never serialize as `verified` silently;
- `unknown` is not false or safe by default.

### 3.2 SpecificationStatus

Describes intent and requirement readiness.

Minimum values:

```text
draft
clarification_required
accepted
superseded
withdrawn
```

`accepted` does not mean implementation authorized.

### 3.3 ContractStatus

Describes lifecycle of a governed agreement.

Minimum values:

```text
draft
under_review
accepted
deprecated
superseded
retired
```

Contract status is not adapter conformance or production maturity.

### 3.4 BindingStatus

Describes adapter or provider binding readiness.

Minimum values:

```text
candidate
compatible
incompatible
conditionally_compatible
selected
disabled
superseded
```

`selected` does not mean execution authorized or runtime healthy.

### 3.5 CapacityDisposition

Describes current ability to responsibly perform a bounded action.

Minimum values:

```text
insufficient
partial
sufficient
blocked
expired
```

Capacity is contextual and must name missing or limiting dimensions.

### 3.6 ExecutionStatus

Describes actual execution-run state.

Minimum values:

```text
requested
planned
authorized
running
blocked
failed
cancelled
succeeded
```

Rules:

- only a real runtime run enters `running`;
- `succeeded` means the bounded execution completed as recorded;
- `succeeded` does not imply validation, approval, delivery, or complete objective satisfaction.

### 3.7 GateOutcome

Describes one declared gate result.

Minimum values:

```text
not_evaluated
passed
failed
conditional
not_applicable
blocked
```

Rules:

- `not_applicable` requires explicit rationale;
- `conditional` identifies unmet conditions;
- gate outcome is scoped to one gate and subject.

### 3.8 ReviewDisposition

Describes review progress or result.

Minimum values:

```text
not_requested
pending
in_review
changes_requested
accepted_with_findings
completed
```

`completed` means the review process completed, not that approval was granted.

### 3.9 ApprovalStatus

Describes authority-bearing permission state.

Minimum values:

```text
not_required
pending
approved
conditionally_approved
rejected
revoked
expired
```

Rules:

- approval records authority, scope, subject, and conditions;
- `not_required` derives from policy, not omission;
- approval may expire or be revoked independently of review state.

### 3.10 CompletionDisposition

Describes objective completion as a bounded claim.

Minimum values:

```text
incomplete
partial
blocked
not_verified
complete_with_limitations
complete
```

Rules:

- `partial` identifies satisfied and unsatisfied criteria;
- `not_verified` prevents activity from being reported as completion;
- `complete_with_limitations` names accepted limitations and authority;
- `complete` requires accepted criteria and applicable evidence.

### 3.11 DeliveryStatus

Describes movement to a target boundary.

Minimum values:

```text
not_ready
ready
in_progress
delivered
failed
rolled_back
superseded
```

`delivered` does not imply release acceptance or business success.

### 3.12 ProductAcceptanceStatus

Describes product-owned acceptance.

Minimum values:

```text
not_evaluated
pending
accepted
accepted_with_limitations
rejected
revoked
```

Product acceptance authority belongs to the product or organization policy.

### 3.13 EvolutionStatus

Describes learning and shared-change progression.

Minimum values:

```text
feedback_recorded
local_update
learning_recorded
candidate
under_review
accepted
rejected
deferred
superseded
```

`candidate` is not an accepted shared change.

---

## 4. Derived-state rules

### Effective decision

An effective decision is derived from:

```text
decision
+ verified source
+ applicable authority
+ scope coverage
+ required approvals
+ resolved material conflicts
+ current validity
```

It is not a boolean stored by convenience without its derivation evidence.

### Completion

Completion disposition is derived from:

```text
accepted objective and criteria
+ evidence and coverage
+ verification and validation
+ required gates
+ review and approval state
+ known limitations
```

Execution status alone cannot derive completion.

### Embodiment

Embodiment is supported by:

```text
declared expectation
+ repeatable executable behavior
+ appropriate evidence
```

Documentation, contract presence, installation, metadata, or one success is insufficient.

### Stability

Stability is supported by:

```text
explicit ownership
+ compatibility expectations
+ controlled change behavior
+ validation requirements
+ reliable consumer expectations
```

Stability is not immutability.

---

## 5. Relationship to existing loops

### Epistemic Loop

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE
→ SELECT
→ READ EVIDENCE
→ UPDATE
```

Role: reasoning discipline inside any domain activity.

It does not own delivery phases or runtime orchestration.

### Development Loop

```text
Explore
→ Plan
→ Implement
→ Verify
→ Review
→ Document
→ Deliver
```

Role: reusable execution method for engineering work.

It may be used inside workflow phases. It is not the canonical domain relationship and does not replace product workflows.

### Workflow lifecycle

Role: ordered, capability-specific or product-specific phases, transitions, gates, handoffs, and exits.

A workflow may use the Epistemic Loop and Development Loop while remaining separately defined.

---

## 6. Negative examples

### False execution

Wrong:

```text
plan generated → ExecutionStatus = succeeded
```

Correct:

```text
plan generated → planned
host executes → running
actual outcome recorded → succeeded / failed / blocked
```

### False approval

Wrong:

```text
review verdict = positive → ApprovalStatus = approved
```

Correct:

```text
review completed
→ governing policy checks authority
→ approval issued only by required authority
```

### False completion

Wrong:

```text
unit tests pass → complete
```

Correct:

```text
unit tests support specified claims
→ remaining acceptance, validation, review, approval, and limitations assessed
→ completion disposition recorded
```

### False evolution

Wrong:

```text
one product fix works → core contract changed
```

Correct:

```text
feedback → local fix → learning candidate
→ multi-context and counterexample review
→ compatibility and authority review
→ accepted target-layer evolution
```

---

## 7. Lifecycle invariants

1. No transition silently skips required authority, evidence, or gate.
2. A skipped phase or gate is explicit, policy-authorized, and records residual risk.
3. Every material transition preserves source, scope, and responsible owner.
4. Status values from different families are never substituted for one another.
5. Product acceptance and core evolution remain authority-bearing downstream decisions.
6. Partial, blocked, not-verified, failed, rejected, revoked, and superseded states remain representable.
7. Historical decisions, approvals, and contract versions are superseded, not erased.
