# Native AI Engineering Domain Model — Aggregate And Lifecycle Candidates

Status: Candidate discovery artifact — non-canonical

Issue: `#6 — Define the canonical Native AI Engineering domain model`

Branch: `6-canonical-native-ai-engineering-domain-model`

Accepted foundation: [`../philosophy/README.md`](../philosophy/README.md)

Concept ownership matrix: [`concept-ownership-matrix.md`](concept-ownership-matrix.md)

Discovery inventory: [`../native-ai-engineering-domain-model-discovery.md`](../native-ai-engineering-domain-model-discovery.md)

This document refines candidate aggregate roots, consistency boundaries, lifecycle transitions, commands, events, and cross-context references for the canonical Native AI Engineering domain model.

It is not yet canonical authority and does not authorize contract, schema, manifest, validator, adapter, skill, workflow, runtime, or product migration.

---

## 1. Role Of Domain-Driven Design In Core

Native AI Engineering uses Domain-Driven Design as a modeling method, not as the domain itself.

```text
DDD
→ provides strategic and tactical modeling tools;

Native AI Engineering
→ is the domain being modeled;

ai-native-core
→ owns canonical domain language, boundaries, contracts, and standards;

ai-native-skills
→ owns executable DDD methodology that implements the core contract;

native-ai-fw
→ orchestrates domain-modeling work and consumes the accepted model;

product repositories
→ own product-specific domain models and specializations.
```

Current supporting artifacts:

```text
docs/domain-driven-model.md
→ DDD guidance and product examples;

contracts/skills/architecture/domain-driven-design.contract.yaml
→ versioned reusable DDD capability agreement;

ai-native-skills/skills/domain-driven-design/SKILL.md
→ executable skill adapter pinned to the core contract.
```

Issue `#6` must not copy product examples into universal core and must not treat a DDD implementation convention as a universal domain fact without evidence.

Potential future contract review items include absolute implementation rules such as repository return shapes and layer placement. No such contract change is authorized in this issue slice.

---

## 2. Aggregate Selection Rules

A candidate aggregate root is retained only when it owns a real consistency boundary.

Use an aggregate root when:

```text
related mutations must remain coherent in one domain operation;
identity and lifecycle persist across changes;
invariants must be enforced through one root;
cross-context consumers can reference the root without mutating internals;
concurrent change requires explicit ownership or conflict handling.
```

Do not create an aggregate merely because a noun is important.

The following remain non-aggregate concepts unless a stronger consistency boundary is demonstrated:

```text
Approval
→ classification of an authority-bearing Decision Record;

Risk Acceptance
→ Decision Record specialization over a named residual risk;

Effective Decision
→ derived view over decision records, authority, policy, conflict, and supersession;

Verdict
→ value object produced by review or evaluation;

Coverage
→ value object describing observed or evaluated scope;

Authorization Assessment
→ time- and action-bounded assessment record;

Release Eligibility
→ evaluation result, not permission to release.
```

Aggregate boundaries must not be used to bypass bounded-context boundaries. Cross-context relationships use identifiers, immutable references, events, or explicit integration contracts.

---

## 3. Candidate Aggregate Summary

| Aggregate root | Primary owner | Owns | Must not own |
|---|---|---|---|
| `Specification` | C1 Intent And Specification | requirements, criteria, declared scope, constraints, versions | implementation, evidence, approval authority |
| `Workflow Run` | C5 Execution And Operations, coordinated from C3 definition | phase-run coordination, handoffs, lifecycle state, execution references | quality verdict, approval, tool implementation |
| `Execution Run` | C5 Execution And Operations | actual operation attempts, invocation records, produced artifacts, execution failures | product acceptance, review, authority source |
| `Evidence Set` | C6 Evidence, Evaluation, And Acceptance | reproducible evidence membership, scope, coverage, provenance references | claims as mutable truth, verdict, approval |
| `Decision Case` | C7 Governance, Risk, And Authority | decision records, requirements, conflicts, supersession, effective-decision derivation | fabricated technical evidence, execution result |

These are first aggregate decisions under review. Other candidates such as `Contract Definition`, `Workflow Definition`, `Context Pack`, `Product Instance`, `Learning Candidate`, and `Evolution Proposal` remain for later slices.

---

# 4. Specification Aggregate

## 4.1 Purpose

`Specification` owns the coherent statement of what is intended, required, constrained, excluded, and accepted for a bounded engineering or product scope.

It converts attributable intent into reviewable requirements without claiming that the requirements are approved, implemented, verified, or delivered.

## 4.2 Aggregate Shape

```text
Specification
├── Specification Identity
├── Intent References
├── Specification Versions
│   ├── Declared Scope
│   ├── Non-Goals
│   ├── Requirements
│   ├── Acceptance Criteria
│   ├── Constraints
│   ├── Assumptions
│   ├── Unknowns
│   └── Traceability Links
├── Current Proposed Version Reference
├── Accepted Version Reference, when governed
└── Supersession References
```

Candidate ownership:

```text
Specification identity and versions
→ C1;

approval or acceptance decision
→ C7 Decision Case;

implementation against specification
→ C5 Workflow Run and Execution Run;

evidence that criteria are satisfied
→ C6;

product-specific specialization
→ C9 Product Instance.
```

## 4.3 Candidate Entities

### `Specification Version`

An immutable or append-only version snapshot of the specification content.

A material change creates a new version rather than rewriting an already accepted version invisibly.

### `Requirement`

An addressable normative statement with stable identity inside a specification lineage.

Candidate fields:

```text
requirement_id;
statement;
type;
source_refs;
scope;
priority or criticality when policy-defined;
dependencies;
acceptance_criterion_refs;
status inside the specification lifecycle;
replaces or supersedes refs.
```

Requirement lifecycle state must not claim implementation state.

### `Acceptance Criterion`

An addressable criterion defining what evidence would support acceptance of a requirement or scope.

Candidate fields:

```text
criterion_id;
statement;
requirement_refs;
applicable_scope;
required_evidence_classes;
coverage expectation;
required reviewers or authorities by reference;
release-blocking or transition significance when policy-defined.
```

An acceptance criterion is not a gate evaluation and is not evidence that the criterion passed.

## 4.4 Candidate Value Objects

```text
Scope;
Constraint;
Non-Goal;
Assumption;
Unknown;
Source Reference;
Traceability Link;
Specification Version Identifier.
```

Assumptions and unknowns remain explicit. They must not be converted into requirements or facts without an attributable decision or evidence path.

## 4.5 Invariants

```text
Every requirement has a stable identifier within the specification lineage.

Every acceptance criterion references at least one requirement or declared scope objective.

Accepted specification content is immutable; material change creates a new version.

A specification cannot mark itself approved or authoritative.

An accepted-version reference requires an effective authority-bearing Decision Record.

Removing an accepted requirement or criterion requires explicit supersession or scope decision.

Assumptions, unknowns, and inferred intent remain distinguishable from direct intent sources.

Non-goals and constraints cannot be dropped silently during version creation.

Implementation state, test result, review verdict, and delivery state do not belong inside specification lifecycle status.
```

## 4.6 Candidate Lifecycle

```text
DRAFT
→ PROPOSED
→ ACCEPTED
→ SUPERSEDED

DRAFT or PROPOSED
→ WITHDRAWN

ACCEPTED
→ remains immutable;
  a successor version may become PROPOSED and later ACCEPTED.
```

Meaning:

```text
DRAFT
→ editable working version;

PROPOSED
→ complete enough for review or decision;

ACCEPTED
→ referenced by an effective authority-bearing decision;

SUPERSEDED
→ no longer current because a successor version was explicitly accepted;

WITHDRAWN
→ proposal intentionally removed before acceptance.
```

`ACCEPTED` is not equivalent to implemented, verified, release-ready, or delivered.

## 4.7 Candidate Commands

```text
Create Specification
Create Specification Version
Add Requirement
Revise Requirement
Add Acceptance Criterion
Record Constraint
Record Assumption
Record Unknown
Propose Specification Version
Reference Acceptance Decision
Supersede Specification Version
Withdraw Specification Proposal
```

Commands that reference acceptance or supersession require C7 authority evidence. The Specification aggregate does not generate that authority itself.

## 4.8 Candidate Events

```text
Specification Created
Specification Version Created
Requirement Added
Requirement Revised
Acceptance Criterion Added
Constraint Recorded
Assumption Recorded
Unknown Recorded
Specification Version Proposed
Specification Version Accepted
Specification Version Superseded
Specification Proposal Withdrawn
```

`Specification Version Accepted` records that an effective decision reference was applied. It does not mean the aggregate independently approved itself.

---

# 5. Workflow Run Aggregate

## 5.1 Purpose

`Workflow Run` coordinates one bounded execution lifecycle against one resolved `Workflow Definition` version.

It records phases, transitions, handoffs, blocking conditions, and related execution runs. It does not decide whether the resulting work is correct, approved, or authorized for downstream release.

## 5.2 Aggregate Shape

```text
Workflow Run
├── Workflow Definition Reference And Version
├── Run Scope
├── Initiating Actor Reference
├── Product Or Context Binding References
├── Phase Runs
├── Gate Evaluation References
├── Execution Run References
├── Handoffs
├── Blockers And Pauses
├── Run State
├── Started And Ended Times
└── Completion Assessment Reference, when available
```

A workflow definition belongs to C3. The run belongs to C5.

## 5.3 Candidate Entities

### `Phase Run`

An identified occurrence of one workflow phase within one workflow run.

Candidate fields:

```text
phase_run_id;
phase_definition_ref;
sequence or dependency refs;
state;
input refs;
output refs;
execution_run_refs;
gate_evaluation_refs;
blocker refs;
started_at;
ended_at.
```

### `Handoff Record`

Records an explicit transfer between phases, actors, methods, contexts, or repositories.

Handoff presence does not prove the receiver accepted or completed the work.

### `Workflow Blocker`

Records a missing prerequisite, evidence gap, authority gap, dependency failure, or unresolved conflict that prevents an allowed transition.

A blocker must not be represented as an ordinary warning if the governing definition or policy makes it transition-blocking.

## 5.4 Invariants

```text
One Workflow Run resolves exactly one Workflow Definition version.

Phase Runs must reference phases declared by that definition or an explicitly authorized extension.

Required phase ordering and dependency constraints must be preserved.

A transition requiring a gate cannot proceed without a corresponding Gate Evaluation result that permits it.

A transition requiring authority cannot proceed solely because a gate passed.

Workflow Run may coordinate Execution Runs but must not rewrite their observed execution records.

Workflow completion means the orchestration lifecycle ended according to its definition; it does not prove product acceptance or success.

A blocked run cannot silently advance by changing its own state.

Skipped phases require an explicit shortcut, waiver, or not-applicable decision when the definition requires them.

A retry creates a new Phase Run or Execution Run attempt; prior attempts remain attributable.
```

## 5.5 Candidate Lifecycle

```text
CREATED
→ READY
→ RUNNING
→ COMPLETED

RUNNING
↔ PAUSED

RUNNING or PAUSED
→ BLOCKED

BLOCKED
→ RUNNING
→ CANCELLED
→ FAILED

CREATED or READY or RUNNING or PAUSED or BLOCKED
→ CANCELLED

RUNNING or BLOCKED
→ FAILED
```

Meaning:

```text
CREATED
→ run identity and workflow definition are known;

READY
→ required scope, binding, context, and start prerequisites are resolved;

RUNNING
→ at least one phase is active or progressing;

PAUSED
→ intentionally suspended with resumable state;

BLOCKED
→ cannot proceed because a required condition is unresolved;

COMPLETED
→ required workflow coordination has ended according to the definition;

FAILED
→ orchestration could not complete due an unrecovered operational or invariant failure;

CANCELLED
→ intentionally terminated before completion.
```

`COMPLETED` does not mean accepted, approved, release-ready, or authorized.

## 5.6 Standalone And Nested Runs

A Workflow Run may coordinate many Execution Runs.

```text
Workflow Run
→ zero or more Phase Runs
→ zero or more Execution Runs per phase
→ zero or more Evaluation Runs by reference.
```

Evaluation and review runs may themselves be invoked by a workflow but remain owned by C6.

## 5.7 Candidate Commands

```text
Create Workflow Run
Prepare Workflow Run
Start Workflow Run
Start Phase Run
Pause Workflow Run
Resume Workflow Run
Record Workflow Blocker
Resolve Workflow Blocker
Attach Execution Run
Record Handoff
Complete Phase Run
Complete Workflow Run
Fail Workflow Run
Cancel Workflow Run
```

## 5.8 Candidate Events

```text
Workflow Run Created
Workflow Run Prepared
Workflow Run Started
Phase Run Started
Workflow Run Paused
Workflow Run Blocked
Workflow Blocker Resolved
Execution Run Attached
Handoff Recorded
Phase Run Completed
Workflow Run Completed
Workflow Run Failed
Workflow Run Cancelled
```

---

# 6. Execution Run Aggregate

## 6.1 Purpose

`Execution Run` records actual attempted work on a bounded execution surface.

It answers:

```text
what operation was attempted;
by which actor or agent;
under which scope, binding, permission, and authorization references;
which tools or adapters were invoked;
what observations, outputs, errors, and side effects were recorded;
whether the operation technically completed.
```

It does not answer whether the result satisfies requirements, is approved, or should be delivered.

## 6.2 Standalone Execution Decision

An Execution Run may exist without a Workflow Run.

This supports:

```text
bounded one-off tool operations;
standalone verification commands;
manual or agent-triggered repository inspection;
evaluation-supporting execution;
incident or recovery operations;
low-risk operations that do not require a full workflow.
```

When created inside a workflow, it references the owning Workflow Run and Phase Run.

When standalone, it must still carry explicit intent, scope, operation definition, binding, and applicable authority references.

## 6.3 Aggregate Shape

```text
Execution Run
├── Operation Definition Reference
├── Optional Workflow Run And Phase Run References
├── Actor Or Agent Reference
├── Scope
├── Capability And Binding References
├── Permission And Authorization References
├── Input References
├── Operation Attempts
│   ├── Tool Invocations
│   ├── Adapter Invocations
│   ├── Observations
│   ├── Output Artifact References
│   ├── Side-Effect References
│   └── Error Records
├── Run State
├── Technical Outcome
└── Started And Ended Times
```

## 6.4 Candidate Entities

### `Operation Attempt`

One attempt to perform the bounded operation.

A retry creates a new attempt; it must not overwrite the previous attempt.

### `Tool Invocation Record`

Immutable record of a tool call or operation including attributable request, response, timing, and error references where available.

Tool invocation success does not prove the requested engineering objective succeeded.

### `Execution Error`

A structured record of an execution-level failure.

An execution error may produce evidence for debugging or evaluation but is not automatically a domain finding or governance decision.

## 6.5 Invariants

```text
Execution Run has explicit bounded scope and operation intent.

The selected adapter or runtime binding must implement or specialize the required capability boundary.

Technical permission and authority references remain separate.

High-risk or governed operations cannot start without an applicable authorization assessment.

Tool access alone cannot create authority.

Every operation attempt is append-only and attributable.

Recorded outputs and side effects cannot be reported when no corresponding observation or operation record exists.

Retries do not erase failed attempts.

Technical completion does not produce acceptance, review approval, or delivery authorization automatically.

Execution Run must preserve unknown or unobservable side effects rather than declaring none without evidence.
```

## 6.6 Candidate Lifecycle

```text
CREATED
→ READY
→ RUNNING
→ COMPLETED

CREATED or READY
→ BLOCKED

RUNNING
→ FAILED
→ CANCELLED

BLOCKED
→ READY
→ CANCELLED

RUNNING
→ CANCELLED when interruption is supported.
```

Meaning:

```text
CREATED
→ operation and scope are recorded;

READY
→ required binding, inputs, permission, capacity, and authorization are resolved;

BLOCKED
→ execution cannot start because a required condition is missing or denied;

RUNNING
→ one or more attempts are active;

COMPLETED
→ operation returned or concluded according to the execution surface;

FAILED
→ operation could not complete successfully at the execution layer;

CANCELLED
→ execution was intentionally terminated.
```

`COMPLETED` means technical execution completion, not requirement satisfaction.

## 6.7 Technical Outcome

Candidate technical outcomes remain local to execution:

```text
RETURNED_SUCCESSFULLY;
RETURNED_WITH_ERRORS;
FAILED_TO_EXECUTE;
CANCELLED;
PARTIAL_SIDE_EFFECTS_RECORDED;
OUTCOME_UNKNOWN.
```

These outcomes must not be reused as C6 evaluation verdicts.

## 6.8 Candidate Commands

```text
Create Execution Run
Resolve Execution Binding
Attach Permission Reference
Attach Authorization Assessment
Start Execution Run
Start Operation Attempt
Record Tool Invocation
Record Output Artifact
Record Side Effect
Record Execution Error
Complete Operation Attempt
Complete Execution Run
Fail Execution Run
Cancel Execution Run
```

## 6.9 Candidate Events

```text
Execution Run Created
Execution Run Prepared
Execution Run Blocked
Execution Run Started
Operation Attempt Started
Tool Invoked
Adapter Invoked
Output Artifact Recorded
Side Effect Recorded
Execution Error Recorded
Operation Attempt Completed
Execution Run Completed
Execution Run Failed
Execution Run Cancelled
```

---

# 7. Evidence Set Aggregate

## 7.1 Purpose

`Evidence Set` owns a reproducible, bounded collection of evidence references assembled for one declared assessment scope.

It preserves:

```text
which evidence items were considered;
which subject, environment, time, and version they concern;
which methods produced them;
what coverage they provide;
which gaps or conflicts remain;
which frozen set version an assessment used.
```

It does not own claims as truth and does not produce approval.

## 7.2 Claim Ownership Decision

Claims remain independently addressable.

```text
Claim
→ statement requiring assessment;

Evidence Item
→ attributable information that may support or challenge claims;

Evidence Set
→ reproducible collection of Evidence Item references for bounded assessment;

Claim Assessment
→ relates one or more claims to evidence sets, criteria, coverage, and findings.
```

Therefore:

```text
Evidence Set does not own mutable claims;
Evidence Item may support multiple claims;
Claim may be assessed using multiple evidence sets;
assessment records preserve exact frozen evidence-set versions.
```

## 7.3 Aggregate Shape

```text
Evidence Set
├── Evidence Set Identity And Version
├── Declared Subject And Assessment Purpose
├── Scope
├── Environment And Version References
├── Evidence Item References
├── Method References
├── Coverage
├── Evidence Gaps
├── Conflict References
├── Created And Frozen Times
└── Supersession Link
```

Evidence Items may be independently addressable immutable records. The set owns membership, declared coverage, and reproducibility—not the internal lifecycle of external source artifacts.

## 7.4 Candidate Entities And Values

### `Evidence Item`

Candidate immutable entity with:

```text
evidence_item_id;
source_ref;
producer or observer ref;
method;
subject;
scope;
environment;
time;
version;
content or artifact ref;
coverage;
limitations;
integrity metadata;
supersession ref when corrected.
```

### `Evidence Gap`

Records required evidence that is missing, stale, inaccessible, conflicted, or outside coverage.

A gap must remain visible to assessments and completion decisions.

### `Coverage`

Value object describing what was actually observed, executed, measured, reviewed, or supported.

Coverage is not quality or correctness.

## 7.5 Invariants

```text
Every Evidence Item is attributable to a source and production method.

Every Evidence Set has explicit subject, scope, purpose, environment, and time boundary.

Evidence membership is append-only while OPEN.

A FROZEN Evidence Set is immutable and reproducible.

An assessment must reference a frozen Evidence Set version.

A correction creates a superseding Evidence Item or Evidence Set version rather than rewriting history invisibly.

Evidence reused across claims retains its original scope and limitations.

Coverage cannot be broadened merely because evidence is placed in a larger set.

Missing or conflicting evidence remains visible as a gap.

Evidence Set does not produce verdict, approval, authorization, or completion by itself.
```

## 7.6 Candidate Lifecycle

```text
OPEN
→ FROZEN
→ SUPERSEDED

OPEN
→ ABANDONED
```

Meaning:

```text
OPEN
→ membership and metadata may be assembled;

FROZEN
→ immutable evidence snapshot available for assessment;

SUPERSEDED
→ a newer frozen version replaces it for a declared purpose;

ABANDONED
→ incomplete working set intentionally discarded before assessment.
```

A superseded evidence set remains addressable for historical assessments.

## 7.7 Candidate Commands

```text
Create Evidence Set
Add Evidence Item Reference
Record Evidence Gap
Record Coverage
Record Conflict Reference
Freeze Evidence Set
Supersede Evidence Set
Abandon Evidence Set
```

## 7.8 Candidate Events

```text
Evidence Set Created
Evidence Item Added
Evidence Gap Recorded
Coverage Recorded
Evidence Conflict Referenced
Evidence Set Frozen
Evidence Set Superseded
Evidence Set Abandoned
```

---

# 8. Decision Case Aggregate

## 8.1 Purpose

`Decision Case` owns the attributable governance record for one bounded decision domain and scope.

It preserves decision history, required authority, conflicting records, explicit supersession, and the derivation of the currently effective decision.

It does not fabricate implementation evidence and does not execute the authorized action.

## 8.2 Aggregate Shape

```text
Decision Case
├── Decision Domain And Scope
├── Subject Or Proposed Action References
├── Authority Requirements
├── Decision Records
│   ├── Approval Specializations
│   ├── Rejection Or Constraint Decisions
│   ├── Risk Acceptance Specializations
│   └── Waiver Or Exception Specializations
├── Authority Grant References
├── Permission References
├── Policy References
├── Conflicts
├── Supersession Links
├── Effective Decision View
└── Case Lifecycle State Or Derived Resolution State
```

## 8.3 Decision Record

`Decision Record` is an entity with stable identity.

Candidate fields:

```text
decision_record_id;
decision_type;
statement;
applies_to;
source_ref;
source_statement;
source_type;
required_authority;
observed_authority_refs;
authority_status;
policy_refs;
supersedes;
conflicts_with;
rationale;
permitted_actions;
blocked_actions;
recorded_at.
```

A decision record may be authoritative, non-authoritative, conflicted, superseded, or insufficient for the proposed action.

## 8.4 Approval And Risk Acceptance

```text
Approval
→ positive authority-bearing Decision Record permitting a named action,
  transition, claim, release, risk acceptance, or canonical change.

Risk Acceptance
→ authority-bearing Decision Record accepting a named residual risk
  within scope, mitigation, duration, and policy limits.
```

Neither becomes a standalone aggregate.

## 8.5 Effective Decision

`Effective Decision` is a derived read model or value object.

It is calculated from:

```text
decision records;
source attribution;
decision scope;
required and observed authority;
policy requirements;
conflicts;
supersession;
time or expiry where applicable.
```

Newest record is not automatically effective.

An effective decision may be absent when:

```text
no authoritative decision exists;
required authority is missing;
authoritative decisions conflict;
supersession is unclear;
policy requires additional approval;
the proposed action falls outside recorded scope.
```

## 8.6 Authorization Assessment Boundary

Authorization Assessment is not stored as the effective decision itself.

It evaluates a concrete action at a point in time using:

```text
Effective Decision;
required authority;
permission facts;
capability and binding facts;
policy;
risk controls;
current scope;
current conflicts or expiry.
```

Candidate results:

```text
AUTHORIZED;
NOT_AUTHORIZED;
ROUTE_FOR_APPROVAL;
PROVENANCE_BLOCKED;
CONFLICTED;
NOT_CHECKABLE.
```

Authorization does not prove the action executed or succeeded.

## 8.7 Invariants

```text
Every material Decision Record has attributable source reference.

Every decision has explicit decision domain and scope.

Approval requires observed authority satisfying the applicable requirement.

Technical permission is not sufficient authority.

Agent-authored summary, issue, PR, report, or specification is not owner approval without attributable acceptance.

Silence is not approval.

Recency is not supersession.

Incompatible authoritative decisions remain conflicted until explicit resolution or supersession.

Unresolved authoritative conflict blocks dependent mutation and approval claims.

An accepted risk cannot erase the underlying risk or bypass a failed hard gate.

A waiver permits bounded deviation; it does not delete the governing contract or policy.

Effective Decision is derived and cannot be mutated independently from its records.
```

## 8.8 Candidate Lifecycle

A Decision Case may use a derived resolution state rather than one freely mutable status.

Candidate states:

```text
OPEN
→ no effective decision has been established;

EFFECTIVE
→ one currently governing decision exists for the declared scope;

CONFLICTED
→ incompatible authoritative decisions remain unresolved;

CLOSED
→ the case is intentionally closed and no current decision is expected;

SUPERSEDED
→ another Decision Case explicitly replaces this decision domain or scope.
```

Transitions:

```text
OPEN
→ EFFECTIVE when an authoritative unconflicted decision becomes effective;

OPEN or EFFECTIVE
→ CONFLICTED when an incompatible authoritative record is added;

CONFLICTED
→ EFFECTIVE through explicit resolution or supersession;

OPEN or EFFECTIVE or CONFLICTED
→ CLOSED through authority-bearing closure decision;

EFFECTIVE or CLOSED
→ SUPERSEDED through explicit replacement reference.
```

A new decision may require reopening or creating a successor case according to the domain policy. This remains under review.

## 8.9 Candidate Commands

```text
Open Decision Case
Record Decision
Record Approval
Record Rejection
Record Risk Acceptance
Record Waiver
Register Authority Requirement
Attach Authority Grant Reference
Attach Permission Reference
Record Decision Conflict
Resolve Decision Conflict
Supersede Decision Record
Derive Effective Decision
Assess Authorization
Close Decision Case
Supersede Decision Case
```

Commands that record approval, risk acceptance, waiver, conflict resolution, closure, or supersession require attributable authority.

## 8.10 Candidate Events

```text
Decision Case Opened
Decision Recorded
Approval Recorded
Rejection Recorded
Risk Accepted
Waiver Issued
Authority Requirement Registered
Decision Conflict Recorded
Decision Conflict Resolved
Decision Record Superseded
Decision Became Effective
Authorization Assessed
Decision Case Closed
Decision Case Superseded
```

---

# 9. Cross-Aggregate Relationships

## 9.1 Specification To Workflow Run

```text
Specification accepted version
→ referenced by Workflow Run scope;

Workflow Run
→ must not modify specification content;

scope change discovered during execution
→ produces a proposed Specification version or C7 decision route;

implementation existence
→ does not change accepted specification automatically.
```

## 9.2 Workflow Run To Execution Run

```text
Workflow Run
→ coordinates Execution Run references;

Execution Run
→ records actual operation attempts;

Execution Run completion
→ does not complete the Workflow Run automatically;

Workflow Run completion
→ does not rewrite Execution Run outcomes.
```

## 9.3 Execution Run To Evidence Set

```text
Execution Run observations and artifacts
→ may become Evidence Items;

Evidence Item creation
→ preserves execution source, method, scope, environment, and time;

Execution output
→ is not evidence for every possible claim;

Evidence Set
→ assembles bounded references for a declared assessment purpose.
```

## 9.4 Evidence Set To Decision Case

```text
Evidence Set
→ may inform Decision Records or Authorization Assessments;

Evidence
→ is not authority;

Decision Case
→ may require evidence but cannot rewrite evidence;

Approval
→ cannot convert missing evidence into verified fact.
```

## 9.5 Decision Case To Execution Run

```text
Effective Decision and Authorization Assessment
→ may permit a named Execution Run operation;

Execution Run
→ references the authorization used;

Authorization
→ does not prove the action executed;

execution completion
→ does not expand the authorization scope.
```

---

# 10. Transaction And Consistency Boundaries

Candidate synchronous consistency rules:

```text
Specification transaction
→ one aggregate version mutation or proposal transition;

Workflow Run transaction
→ one run or phase transition with required local invariants;

Execution Run transaction
→ one operation-attempt or run-state mutation;

Evidence Set transaction
→ one membership, coverage, gap, freeze, or supersession mutation;

Decision Case transaction
→ one attributable decision, conflict, supersession, or resolution mutation.
```

Cross-aggregate effects use events or application coordination rather than multi-aggregate hidden transactions.

Examples:

```text
Specification Version Accepted
→ application layer may prepare a Workflow Run;

Execution Run Completed
→ evidence adapter may create Evidence Items;

Evidence Set Frozen
→ evaluation use case may start Claim Assessment;

Decision Became Effective
→ authorization use case may assess a concrete action;

Authorization Assessed as AUTHORIZED
→ execution use case may start the permitted operation.
```

No event automatically bypasses the target context's own validation, policy, capacity, or authority requirements.

---

# 11. Prohibited Aggregate Collapses

```text
Specification Aggregate
≠ implementation project record;

Workflow Run
≠ Workflow Definition;

Execution Run
≠ successful engineering outcome;

Evidence Set
≠ verdict or truth container;

Decision Case
≠ technical permission store;

Approval
≠ Review Verdict;

Effective Decision
≠ latest Decision Record;

Gate Evaluation
≠ Authorization Assessment;

COMPLETED Workflow Run
≠ accepted product or feature;

COMPLETED Execution Run
≠ requirement satisfied;

FROZEN Evidence Set
≠ sufficient evidence;

AUTHORIZED action
≠ executed action;

executed action
≠ successful or accepted action.
```

---

# 12. Candidate Lifecycle Vocabulary Policy

Each aggregate owns its lifecycle vocabulary.

Do not create one global domain enum such as:

```text
PENDING;
APPROVED;
FAILED;
COMPLETED.
```

Cross-context reporting may expose normalized categories only as a read model:

```text
NOT_STARTED;
ACTIVE;
WAITING;
BLOCKED;
TERMINAL;
UNKNOWN.
```

Normalized categories must never replace aggregate-specific states or become mutation authority.

---

# 13. DDD Contract Reconciliation Notes

Current DDD contract strengths:

```text
explicit bounded contexts;
one aggregate root per aggregate;
immutable value objects;
past-tense domain events;
consistent ubiquitous language;
explicit context-map relationships;
product-defined persistence and event-bus choices.
```

Candidate tensions to review after the canonical model stabilizes:

```text
"repositories must only return aggregates not raw entities"
→ may be a useful default but is currently phrased as universal;

"no domain logic in application or infrastructure layer"
→ domain ownership is correct, but orchestration policy and cross-context coordination
  need precise separation from domain invariants;

"one aggregate = one transaction"
→ useful executable-skill guidance, but distributed and external consistency
  require eventual-consistency and process-manager guidance;

repository interfaces as mandatory DDD output
→ may not be necessary for every non-persistent or document-centric context.
```

Issue `#6` records these as potential downstream contract-refinement inputs. It does not silently modify contract `0.1.0`.

---

# 14. Open Questions

1. Should accepted Specification versions be entities inside one aggregate lineage or independently addressable immutable aggregate versions?
2. Should `Intent` be a separate aggregate or an immutable source entity referenced by Specification?
3. Should `Workflow Run COMPLETED` be renamed `ENDED` to reduce false-success interpretation, despite existing workflow terminology?
4. Which Execution Run operations require a Workflow Run by policy, and which may remain standalone?
5. Should Operation Attempt be its own aggregate for long-running distributed execution?
6. Should Evidence Item be an independent aggregate root or an immutable entity managed by an evidence repository outside the Evidence Set boundary?
7. Should Evidence Set freeze be mandatory before every evaluation, or may streaming evaluations reference evolving sets with explicit version checkpoints?
8. Should Decision Case lifecycle state be persisted or always derived from records and conflicts?
9. When does a materially changed decision require a successor Decision Case instead of reopening the current case?
10. Which commands and events require first-class schemas in issue `#8`?
11. Which lifecycle transitions require validator rules in issue `#9`?
12. Which aggregate IDs must be globally unique versus context-local?

---

# 15. Validation Gates

Before these aggregate candidates may become canonical:

- [ ] every aggregate owns one real consistency boundary;
- [ ] aggregate roots do not absorb another bounded context's authority;
- [ ] accepted definitions remain distinct from execution and evidence;
- [ ] Workflow Run and Execution Run completion semantics cannot imply acceptance;
- [ ] standalone Execution Runs preserve intent, scope, binding, and authority;
- [ ] evidence remains attributable, bounded, reusable, and reproducible;
- [ ] claims remain independently addressable from evidence sets;
- [ ] approval remains an authority-bearing Decision Record specialization;
- [ ] Effective Decision remains derived from records, conflict, scope, policy, and authority;
- [ ] authorization remains action- and time-bounded;
- [ ] retries and supersession preserve historical records;
- [ ] aggregate-specific lifecycle states replace generic status authority;
- [ ] candidate commands cannot bypass evidence or authority requirements;
- [ ] candidate events are past-tense occurrence records;
- [ ] current contracts can map to the model without silent migration;
- [ ] issue `#7` can consume capability and binding boundaries;
- [ ] issue `#8` can encode identifiers, references, versions, and transitions;
- [ ] issue `#9` can validate layered evidence, evaluation, completion, and authorization semantics;
- [ ] `ai-native-skills` can implement DDD methodology without copying the entire domain model into every skill;
- [ ] `native-ai-fw` can orchestrate aggregates through explicit ports and application services;
- [ ] product repositories can specialize the model without redefining universal core.

---

# 16. Current Verdict

```text
DDD in ai-native-core: YES, AS CONTRACT + MODELING FOUNDATION
DDD executable methodology: ai-native-skills
Native AI Engineering domain: UNDER ACTIVE MODELING IN #6

Specification aggregate: CANDIDATE DEFINED
Workflow Run aggregate: CANDIDATE DEFINED
Execution Run aggregate: CANDIDATE DEFINED
Standalone Execution Run: ALLOWED WITH EXPLICIT BOUNDARIES
Evidence Set aggregate: CANDIDATE DEFINED
Claims owned by Evidence Set: REJECTED
Decision Case aggregate: CANDIDATE DEFINED
Approval as standalone aggregate: REJECTED
Risk Acceptance as standalone aggregate: REJECTED
Effective Decision as mutable entity: REJECTED
Generic status authority: REJECTED
Contract migrations: NONE AUTHORIZED
Canonical aggregate model ready to freeze: NO
Ready for remaining aggregate and context-map refinement: YES
```
