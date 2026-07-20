# Native AI Engineering Domain Model — Aggregate And Lifecycle Candidates II

Status: Candidate discovery artifact — non-canonical

Issue: `#6 — Define the canonical Native AI Engineering domain model`

Branch: `6-canonical-native-ai-engineering-domain-model`

Accepted foundation: [`../philosophy/README.md`](../philosophy/README.md)

Concept ownership matrix: [`concept-ownership-matrix.md`](concept-ownership-matrix.md)

First aggregate slice: [`aggregate-lifecycle-candidates.md`](aggregate-lifecycle-candidates.md)

This document refines the second candidate aggregate slice:

```text
Contract Definition;
Workflow Definition;
Context Pack;
Product Instance;
Learning Candidate;
Evolution Proposal.
```

It remains non-canonical and does not authorize contract, schema, manifest, validator, adapter, skill, workflow, runtime, or product migration.

---

## 1. Selection Rules For This Slice

A retained aggregate must own a real consistency boundary rather than merely group related nouns.

The following distinctions are mandatory:

```text
definition ≠ registration;
definition ≠ installation;
definition ≠ application;
definition ≠ execution;
definition ≠ conformance;
context assembly ≠ source authority;
product registration ≠ product health;
learning candidate ≠ accepted reusable learning;
evolution proposal ≠ approved canonical change;
accepted evolution ≠ migrated consumer;
implemented migration ≠ verified adoption.
```

Cross-context references use identifiers, immutable references, published events, or explicit integration contracts. No aggregate may mutate another aggregate's internal state directly.

---

## 2. Candidate Aggregate Summary

| Aggregate root | Primary owner | Owns | Must not own |
|---|---|---|---|
| `Contract Definition` | C2 Capability And Agreement | contract lineage, immutable versions, owned and delegated boundaries, compatibility intent | adapter behavior, runtime execution, conformance verdict |
| `Workflow Definition` | C3 Method And Workflow | phases, transitions, gates, handoffs, methods, evidence expectations | workflow run state, execution results, approval authority |
| `Context Pack` | C8 Context, Knowledge, And Memory | task-bounded context composition, source references, retrieval snapshots, freshness, gaps | source-of-truth authority, factual correctness, decision authority |
| `Product Instance` | C9 Product Instance And Registry | product identity, repository references, product bindings, environment bindings, policy and validation references | universal core definitions, runtime execution, release eligibility, delivery authorization |
| `Learning Candidate` | C10 Feedback, Learning, And Evolution | source cases, evidence references, generalized reason, counterexamples, target-layer recommendation | direct shared-layer mutation, evolution approval, migration execution |
| `Evolution Proposal` | C10 Feedback, Learning, And Evolution | proposed shared change, affected consumers, compatibility analysis, migration plan, decision and implementation references | self-approval, silent migration, proof of downstream adoption |

---

# 3. Contract Definition Aggregate

## 3.1 Purpose

`Contract Definition` owns the versioned agreement that must remain stable across implementations and consumers.

It may define capability, workflow, runtime, port, evaluation, or another governed interface, but it does not prove that any implementation exists or conforms.

## 3.2 Aggregate Shape

```text
Contract Definition
├── Contract Identity
├── Contract Kind
├── Contract Versions
│   ├── Purpose
│   ├── Scope And Boundary
│   ├── Inputs And Outputs
│   ├── Rules And Quality Gates
│   ├── Failure Semantics
│   ├── Risk And Authority Requirements
│   ├── Adapter Or Consumer Requirements
│   ├── Compatibility Declaration
│   └── Supersession And Deprecation Metadata
├── Current Published Version Reference
├── Compatibility Policy Reference
├── Registration References
└── Deprecation Or Retirement References
```

## 3.3 Candidate Entities And Value Objects

### Contract Version

An immutable, independently addressable version snapshot.

A published version must not be rewritten in place. A semantic change creates a new version according to the governing compatibility policy.

### Contract Kind

A bounded classification such as:

```text
skill contract;
workflow contract;
runtime contract;
port contract;
test or evaluation contract;
other approved contract kind.
```

Contract kind determines required fields and validation policy. It does not determine implementation maturity.

### Ownership Boundary

An immutable value object describing responsibilities owned, delegated, and explicitly excluded by the version.

```text
owned responsibility
≠ delegated responsibility
≠ implementation evidence.
```

### Compatibility Declaration

A value object expressing intended compatibility and version-line semantics.

Compatibility declaration is not behavioral proof.

### Contract Registration Reference

A reference to a registry or manifest entry proving that a versioned artifact is registered at a path and checksum.

```text
registration
≠ publication authority;
registration
≠ implementation;
registration
≠ conformance.
```

## 3.4 Invariants

```text
Every Contract Definition has stable identity and one primary owner.

Every published Contract Version is immutable.

Every Contract Version declares its kind, scope, owned boundary, delegated boundary,
and applicable quality or validation expectations.

Owned and delegated responsibilities cannot overlap silently.

A version cannot claim compatibility broader than its governing policy permits.

A manifest or registry entry cannot convert an unpublished draft into an accepted contract.

Contract publication requires applicable authority but does not prove adapter implementation.

Contract deprecation does not delete historical identity or prior consumer references.

Contract retirement must preserve migration or replacement information when active consumers exist.

A contract cannot define provider- or product-specific implementation facts as universal requirements
unless those facts are deliberately part of the accepted public agreement.
```

## 3.5 Candidate Lifecycle

```text
DRAFT
→ mutable candidate content without publication claim;

REVIEWABLE
→ internally coherent and ready for governed review;

PUBLISHED
→ authority-bearing version accepted for consumer use;

DEPRECATED
→ still resolvable but replacement or end-of-support intent is declared;

RETIRED
→ no longer valid for new consumption under the governing policy;

SUPERSEDED
→ explicitly replaced by another contract identity or version lineage.
```

Candidate transitions:

```text
DRAFT → REVIEWABLE
when required structure and boundaries are coherent;

REVIEWABLE → PUBLISHED
through required review and publication authority;

PUBLISHED → DEPRECATED
through explicit deprecation decision and replacement guidance;

DEPRECATED → RETIRED
when migration and policy conditions are satisfied;

DRAFT or REVIEWABLE → ABANDONED
when the candidate is intentionally closed without publication;

PUBLISHED or DEPRECATED → SUPERSEDED
through explicit replacement relation.
```

`ABANDONED` may remain an archival disposition rather than an active lifecycle state.

## 3.6 Candidate Commands

```text
Create Contract Definition
Create Contract Version
Revise Draft Contract Version
Submit Contract Version For Review
Publish Contract Version
Register Contract Version
Deprecate Contract Version
Retire Contract Version
Supersede Contract Definition
Record Compatibility Policy
```

Publication, deprecation, retirement, and supersession require attributable authority.

## 3.7 Candidate Events

```text
Contract Definition Created
Contract Version Created
Contract Version Submitted For Review
Contract Version Published
Contract Version Registered
Contract Version Deprecated
Contract Version Retired
Contract Definition Superseded
Compatibility Policy Recorded
```

## 3.8 Prohibited Collapses

```text
Contract Definition ≠ contract file path;
Contract Version ≠ manifest entry;
Contract Publication ≠ adapter implementation;
Version Compatibility ≠ conformance;
Boundary Declaration ≠ behavioral ownership proof;
Contract Presence ≠ runtime integration;
Contract Version 1.0.0 ≠ production maturity.
```

---

# 4. Workflow Definition Aggregate

## 4.1 Purpose

`Workflow Definition` owns a reusable lifecycle agreement that coordinates phases, methods, gates, handoffs, evidence expectations, and exit conditions.

It does not own one execution instance. That belongs to `Workflow Run`.

## 4.2 Aggregate Shape

```text
Workflow Definition
├── Workflow Identity
├── Workflow Versions
│   ├── Purpose And Applicability
│   ├── Phases
│   │   ├── Phase Identity
│   │   ├── Purpose
│   │   ├── Entry Conditions
│   │   ├── Required And Optional Methods
│   │   ├── Required Outputs
│   │   ├── Gate Definitions
│   │   ├── Stop Points
│   │   └── Transition Rules
│   ├── Handoff Definitions
│   ├── Evidence Expectations
│   ├── Risk And Authority Requirements
│   ├── Shortcut Policy References
│   └── Adapter Requirements
├── Current Published Version Reference
└── Deprecation And Supersession References
```

## 4.3 Candidate Entities And Value Objects

### Workflow Version

An immutable published definition snapshot.

### Phase Definition

An addressable entity inside a workflow version describing one lifecycle responsibility.

A phase definition is not a phase run.

### Gate Definition

A value object or addressable entity declaring a transition condition, required evidence, blocking semantics, and applicable exception policy.

A gate definition is not a gate evaluation.

### Handoff Definition

A value object describing expected producer, consumer, artifacts, references, evidence, and unresolved-state behavior at a boundary.

### Shortcut Definition

A policy-governed reduced path that explicitly names skipped phases or gates, residual evidence, allowed risk, and applicable authority.

Silent omission is not a shortcut.

## 4.4 Invariants

```text
Every Workflow Definition has stable identity, version, owner, and applicability boundary.

Every phase has one purpose and explicit transition relationships.

Every mandatory transition condition is represented as a Gate Definition or explicit invariant.

Gate definitions identify evidence expectations and blocking semantics.

Required methods or skills are referenced by identity and compatible agreement, not copied as hidden methodology.

A workflow definition cannot claim that a workflow run occurred.

A workflow definition cannot self-authorize destructive, release, deployment, merge,
or canonical-change actions.

A shortcut must be explicit, policy-authorized, risk-bounded, and evidence-aware.

Published Workflow Versions are immutable.

Provider commands, repository paths, product policy, and concrete runtime mechanics remain adapter or product concerns unless deliberately standardized.
```

## 4.5 Candidate Lifecycle

```text
DRAFT
→ mutable workflow candidate;

REVIEWABLE
→ structurally coherent and ready for specialist or owner review;

PUBLISHED
→ accepted reusable workflow definition;

DEPRECATED
→ retained for compatibility while replacement or migration is declared;

RETIRED
→ unavailable for new workflow runs under policy;

SUPERSEDED
→ explicitly replaced by another workflow definition or lineage.
```

A `Workflow Run` may continue referencing the version with which it started even after that version is deprecated. Mid-run migration requires explicit policy and compatibility handling.

## 4.6 Candidate Commands

```text
Create Workflow Definition
Create Workflow Version
Add Phase Definition
Add Gate Definition
Define Transition
Define Handoff
Define Shortcut
Submit Workflow Version For Review
Publish Workflow Version
Deprecate Workflow Version
Retire Workflow Version
Supersede Workflow Definition
```

## 4.7 Candidate Events

```text
Workflow Definition Created
Workflow Version Created
Phase Definition Added
Gate Definition Added
Transition Defined
Handoff Defined
Shortcut Defined
Workflow Version Submitted For Review
Workflow Version Published
Workflow Version Deprecated
Workflow Version Retired
Workflow Definition Superseded
```

## 4.8 Prohibited Collapses

```text
Workflow Definition ≠ Workflow Run;
Phase Definition ≠ Phase Run;
Gate Definition ≠ Gate Evaluation;
Required Skill ≠ Skill Applied;
Published Workflow ≠ workflow embodied;
Workflow Completion Rule ≠ completed product;
Workflow Publication Authority ≠ authority to execute every workflow action.
```

---

# 5. Context Pack Aggregate

## 5.1 Purpose

`Context Pack` owns the task-, actor-, product-, or execution-bounded composition of context references needed to reason or act responsibly.

It makes source, scope, freshness, retrieval, conflicts, and gaps explicit.

It does not become a source of truth merely because it assembles source references.

## 5.2 Aggregate Shape

```text
Context Pack
├── Context Pack Identity
├── Purpose And Consumer
├── Context Requirements
├── Source References
├── Knowledge Artifact References
├── Memory Record References
├── Retrieval Results
├── Source-Of-Truth Designation References
├── Freshness And Coverage Metadata
├── Context Gaps
├── Conflict References
├── Assembly Checkpoints
└── Supersession Or Archive References
```

## 5.3 Candidate Entities And Value Objects

### Context Requirement

An immutable value object declaring a required context class, subject, minimum freshness, coverage, authority expectation, and missing-state behavior.

### Retrieval Result

An immutable occurrence record containing:

```text
retrieval method;
source reference;
retrieved version or timestamp;
query or selection boundary;
returned content reference;
coverage and limitations.
```

Retrieval result is not verification.

### Context Gap

An addressable finding describing unavailable, stale, inaccessible, conflicting, insufficiently attributable, or missing context.

### Assembly Checkpoint

An immutable snapshot of the pack composition used by a claim, plan, decision, or execution.

This allows later changes to the pack without rewriting what context was available for an earlier action.

## 5.4 Invariants

```text
Every Context Pack has a named purpose, consumer, and scope.

Every included item preserves its source reference and retrieval or version metadata.

Memory references remain distinguishable from knowledge and authoritative source references.

A Context Pack cannot designate its own assembled summary as authoritative without a C7-backed designation.

Missing, stale, inaccessible, or conflicting required context creates an explicit Context Gap.

A summary or transformed representation must retain provenance to its source items.

Freshness requirements are context-specific and must not be replaced by one universal duration.

A pack used for a material action must expose the assembly checkpoint actually used.

Updating a Context Pack does not rewrite prior execution, decision, or evidence history.

Context completeness does not imply factual correctness, approval, or sufficient execution capacity.
```

## 5.5 Candidate Lifecycle

Rather than a generic approval state, Context Pack lifecycle describes assembly usability:

```text
ASSEMBLING
→ requirements and sources are still being collected;

USABLE
→ required context is available to the declared minimum boundary;

USABLE_WITH_GAPS
→ bounded use is possible but named gaps remain;

BLOCKED
→ a required gap or conflict prevents the declared material use;

STALE
→ freshness requirements are no longer met;

SUPERSEDED
→ another pack explicitly replaces it for the declared purpose;

ARCHIVED
→ retained for history but not current use.
```

`USABLE` is not authority or correctness proof.

## 5.6 Candidate Commands

```text
Create Context Pack
Declare Context Requirement
Attach Source Reference
Attach Knowledge Artifact Reference
Attach Memory Record Reference
Record Retrieval Result
Record Context Gap
Record Context Conflict
Create Assembly Checkpoint
Mark Context Pack Stale
Supersede Context Pack
Archive Context Pack
```

## 5.7 Candidate Events

```text
Context Pack Created
Context Requirement Declared
Source Reference Attached
Knowledge Artifact Referenced
Memory Record Referenced
Retrieval Result Recorded
Context Gap Recorded
Context Conflict Recorded
Assembly Checkpoint Created
Context Pack Became Usable
Context Pack Became Blocked
Context Pack Became Stale
Context Pack Superseded
Context Pack Archived
```

## 5.8 Prohibited Collapses

```text
Context Pack ≠ source of truth;
Retrieval Result ≠ verification;
Memory Record ≠ knowledge;
Knowledge Artifact ≠ immutable truth;
Summary ≠ source;
Fresh Context ≠ authoritative context;
Complete Context Pack ≠ sufficient authority or capacity.
```

---

# 6. Product Instance Aggregate

## 6.1 Purpose

`Product Instance` owns the product-specific boundary that specializes universal Native AI Engineering agreements without redefining them.

It identifies repositories, environments, bindings, product policies, delivery targets, and validation references for one product.

## 6.2 Aggregate Shape

```text
Product Instance
├── Product Identity
├── Product Intent And Ownership References
├── Repository References
├── Product Bindings
│   ├── Capability References
│   ├── Contract And Version References
│   ├── Port References
│   ├── Adapter References
│   └── Runtime Binding References
├── Environment Bindings
├── Product Policy References
├── Delivery Targets
├── Product Validation References
├── Lifecycle And Ownership Metadata
└── Suspension, Retirement, Or Supersession References
```

## 6.3 Candidate Entities And Value Objects

### Product Binding

An entity linking a product to accepted universal definitions and product-specific implementations.

A binding may select:

```text
capability;
contract and compatible version;
port;
adapter;
runtime;
configuration reference;
applicable policy;
required evidence or review.
```

Binding does not prove runtime availability or conformance.

### Environment Binding

An entity or value object identifying environment-specific runtime, configuration, policy, secret-management reference, and delivery-target relationships.

Secrets and credentials remain outside public core artifacts.

### Delivery Target

A value object describing a product-specific merge, release, deployment, publication, export, or launch target.

Target does not imply eligibility or authorization.

### Product Validation Reference

A governed reference to product-level field evidence, acceptance, metrics, incidents, or user outcomes.

One product result cannot redefine universal core directly.

## 6.4 Invariants

```text
Every Product Instance has stable identity, owner, and repository or system-of-record references.

Every Product Binding references accepted upstream definitions by stable identity and version where applicable.

A Product Binding may specialize configuration and policy but cannot silently redefine upstream meaning.

Provider-specific implementation details remain inside product or runtime binding boundaries.

Registry presence does not prove health, activity, conformance, or delivery readiness.

Product validation references preserve product, environment, version, scope, method, and time.

Product-specific policy cannot weaken non-overridable core guardrails.

Delivery Target does not imply Release Eligibility or Delivery Authorization.

Suspension or retirement must preserve historical execution, evidence, decision, and validation references.
```

## 6.5 Candidate Lifecycle

```text
REGISTERED
→ product identity and ownership are known;

ACTIVE
→ product accepts new bindings and operational work under policy;

SUSPENDED
→ new governed activity is blocked or narrowed while history remains accessible;

RETIRED
→ product is no longer active for new delivery or development under registry policy;

SUPERSEDED
→ another Product Instance explicitly replaces the product identity or lineage.
```

Product release states, deployment states, and launch states are not Product Instance lifecycle states. They belong to execution, evaluation, and governance contexts.

## 6.6 Candidate Commands

```text
Register Product Instance
Activate Product Instance
Bind Product Capability
Bind Product Contract
Bind Product Port
Bind Product Adapter
Bind Product Runtime
Register Environment Binding
Declare Delivery Target
Attach Product Policy Reference
Attach Product Validation Reference
Suspend Product Instance
Retire Product Instance
Supersede Product Instance
```

Binding mutations require applicable product and repository authority.

## 6.7 Candidate Events

```text
Product Instance Registered
Product Instance Activated
Product Capability Bound
Product Contract Bound
Product Port Bound
Product Adapter Bound
Product Runtime Bound
Environment Binding Registered
Delivery Target Declared
Product Policy Referenced
Product Validation Referenced
Product Instance Suspended
Product Instance Retired
Product Instance Superseded
```

## 6.8 Prohibited Collapses

```text
Product Instance ≠ universal core;
Product Registry Entry ≠ Product Instance health;
Product Binding ≠ Runtime Binding activation;
Runtime Binding ≠ Execution Run;
Delivery Target ≠ Release Eligibility;
Release Eligibility ≠ Delivery Authorization;
Product Validation ≠ universal contract proof.
```

---

# 7. Learning Candidate Aggregate

## 7.1 Purpose

`Learning Candidate` owns a traceable proposal that a verified lesson from one or more source cases may be reusable beyond its original context.

It separates observed feedback from accepted shared learning.

## 7.2 Aggregate Shape

```text
Learning Candidate
├── Candidate Identity
├── Source Case References
├── Observed Failure Or Opportunity
├── Verified Fix Or Outcome References
├── Evidence References
├── Generalized Reason
├── Transferability Hypotheses
├── Counterexamples And Non-Applicability Conditions
├── Duplicate Coverage Findings
├── Target-Layer Recommendation
├── Generalization Assessment References
├── Promotion Assessment References
└── Disposition And Successor References
```

## 7.3 Candidate Entities And Value Objects

### Source Case Reference

An immutable reference to the actual case, affected scope, implementation, evidence, and verification result.

### Generalized Reason

A value object expressing why a lesson may transfer, without copying product-specific implementation details as universal instruction.

### Transferability Hypothesis

A value object naming candidate contexts in which the reason should hold and the conditions that must remain true.

### Counterexample

A value object describing conditions where the candidate rule should not apply.

### Target-Layer Recommendation

A proposed destination such as:

```text
local implementation;
product policy or design lock;
knowledge artifact;
skill rule;
skill reference;
workflow definition;
behavioral evaluation;
contract definition;
canonical core.
```

Recommendation is not authority to write.

## 7.4 Invariants

```text
Every Learning Candidate references at least one attributable source case.

A promotion-capable candidate requires verified evidence appropriate to the source claim.

The candidate distinguishes the reusable reason from the case-specific implementation.

Product names, routes, breakpoints, class names, credentials, and private implementation details
must not be promoted unless the target layer explicitly owns them.

Transferability must be tested against multiple contexts or explicit counterexamples.

Duplicate coverage must be checked before proposing new shared content.

Target-layer recommendation follows the smallest correct layer.

A Learning Candidate cannot directly mutate a shared skill, workflow, contract, knowledge source,
or canonical core artifact.

Insufficient evidence remains a gap; it is not converted into anecdotal learning.

Disposition does not erase source-case provenance.
```

## 7.5 Candidate Lifecycle

```text
CAPTURED
→ source case and candidate lesson are recorded;

EVIDENCE_GAPPED
→ evidence required for generalization is missing or insufficient;

GENERALIZED
→ reusable reason, scope, and counterexamples are explicit;

ASSESSMENT_READY
→ evidence, duplication, transferability, and target-layer inputs are sufficient for assessment;

PROMOTION_RECOMMENDED
→ assessment supports creating an Evolution Proposal or bounded shared-layer proposal;

LOCAL_ONLY
→ lesson is valid but belongs only to the product or implementation layer;

DUPLICATE
→ equivalent shared coverage already exists;

REJECTED
→ evidence or reasoning does not support the proposed learning;

SUPERSEDED
→ another candidate replaces the candidate lineage.
```

`PROMOTION_RECOMMENDED` is not approval and does not authorize repository mutation.

## 7.6 Candidate Commands

```text
Create Learning Candidate
Attach Source Case
Attach Verified Evidence
Record Generalized Reason
Record Transferability Hypothesis
Record Counterexample
Record Duplicate Coverage Finding
Recommend Target Layer
Assess Generalization
Assess Promotion
Disposition Learning Candidate
Supersede Learning Candidate
```

## 7.7 Candidate Events

```text
Learning Candidate Created
Source Case Attached
Verified Evidence Attached
Generalized Reason Recorded
Transferability Hypothesis Recorded
Counterexample Recorded
Duplicate Coverage Found
Target Layer Recommended
Generalization Assessed
Promotion Assessed
Promotion Recommended
Learning Candidate Classified Local Only
Learning Candidate Classified Duplicate
Learning Candidate Rejected
Learning Candidate Superseded
```

## 7.8 Prohibited Collapses

```text
Feedback Item ≠ Learning Candidate;
verified fix ≠ reusable rule;
Learning Candidate ≠ accepted learning;
Target-Layer Recommendation ≠ write authority;
Promotion Assessment PASS ≠ promotion executed;
local success ≠ universal contract requirement.
```

---

# 8. Evolution Proposal Aggregate

## 8.1 Purpose

`Evolution Proposal` owns a governed proposal to change a shared or canonical agreement after a learning candidate or other attributable need has been evaluated.

It coordinates compatibility, migration, authority, implementation, and adoption evidence without self-approving the change.

## 8.2 Aggregate Shape

```text
Evolution Proposal
├── Proposal Identity
├── Source Learning Candidate Or Need References
├── Target Layer And Target Artifact References
├── Proposed Change
├── Rationale And Evidence References
├── Affected Consumer Inventory
├── Compatibility Analysis
├── Risk Analysis
├── Migration Plan
├── Required Authority
├── Decision Case References
├── Implementation References
├── Verification References
├── Adoption And Migration Evidence References
└── Supersession Or Closure References
```

## 8.3 Candidate Entities And Value Objects

### Proposed Change

An immutable proposal snapshot describing additions, modifications, deprecations, removals, or semantic changes.

### Affected Consumer

An addressable reference to contracts, skills, workflows, adapters, runtimes, products, or external consumers affected by the proposal.

### Compatibility Analysis

An assessment record covering:

```text
semantic compatibility;
version impact;
contract and schema impact;
runtime and adapter impact;
product impact;
rollback or coexistence options;
unknown consumers and evidence gaps.
```

### Migration Plan

An entity or immutable plan describing consumer transition order, compatibility window, adapters or aliases, validation, rollback, and completion criteria.

Plan is not migration executed.

### Evolution Decision Reference

A reference to the C7 Decision Case accepting, rejecting, narrowing, or deferring the proposal.

The Evolution Proposal does not own the approval decision.

## 8.4 Invariants

```text
Every Evolution Proposal names one target layer and one or more target artifacts.

Every proposal preserves source evidence and rationale.

Canonical or shared change requires affected-consumer and compatibility analysis proportional to impact.

Breaking change requires explicit version, migration, coexistence, or deprecation treatment.

Unknown consumers and incomplete migration evidence remain explicit.

Proposal acceptance requires an authority-bearing C7 decision.

Accepted proposal does not mean implementation completed.

Implemented change does not mean every consumer migrated.

Migration completion requires consumer-specific evidence appropriate to the claim.

One product or adapter cannot silently declare the proposal globally adopted.

Rollback, deprecation, and supersession references remain traceable after closure.
```

## 8.5 Candidate Lifecycle

```text
DRAFT
→ proposal content is being assembled;

REVIEWABLE
→ impact, evidence, consumers, and migration approach are sufficiently explicit;

UNDER_DECISION
→ routed to the required C7 authority and review process;

ACCEPTED
→ an authority-bearing decision permits the bounded change;

REJECTED
→ an authority-bearing decision rejects the proposal;

DEFERRED
→ decision intentionally postpones the proposal with unresolved conditions;

IMPLEMENTING
→ accepted change is being applied to target artifacts;

IMPLEMENTED
→ target-layer artifacts changed, but consumer adoption may remain incomplete;

MIGRATING
→ affected consumers are transitioning under the migration plan;

VERIFIED
→ declared migration and compatibility criteria are supported by evidence;

SUPERSEDED
→ another proposal explicitly replaces this proposal lineage;

CLOSED
→ no further action is expected under the current decision.
```

Lifecycle states after `UNDER_DECISION` are driven by C7 decisions and referenced execution or evidence, not arbitrary self-mutation.

## 8.6 Candidate Commands

```text
Create Evolution Proposal
Attach Source Learning Candidate
Declare Target Layer
Record Proposed Change
Register Affected Consumer
Assess Compatibility
Assess Evolution Risk
Define Migration Plan
Submit Evolution Proposal For Decision
Record Evolution Decision Reference
Start Evolution Implementation
Record Evolution Implementation
Start Consumer Migration
Record Consumer Migration Evidence
Verify Evolution
Defer Evolution Proposal
Close Evolution Proposal
Supersede Evolution Proposal
```

## 8.7 Candidate Events

```text
Evolution Proposal Created
Source Learning Candidate Attached
Target Layer Declared
Proposed Change Recorded
Affected Consumer Registered
Compatibility Assessed
Evolution Risk Assessed
Migration Plan Defined
Evolution Proposal Submitted For Decision
Evolution Accepted
Evolution Rejected
Evolution Deferred
Evolution Implementation Started
Evolution Implemented
Consumer Migration Started
Consumer Migration Evidence Recorded
Evolution Verified
Evolution Proposal Closed
Evolution Proposal Superseded
```

## 8.8 Prohibited Collapses

```text
Evolution Proposal ≠ Evolution Decision;
Evolution Decision ≠ implementation;
implemented target change ≠ consumer migration;
consumer migration ≠ product validation;
version bump ≠ compatibility proof;
accepted local patch ≠ canonical evolution;
proposal author ≠ approval authority by default.
```

---

# 9. Cross-Aggregate Relationships

## 9.1 Contract Definition And Workflow Definition

```text
Workflow Definition
→ references Contract Definitions governing required skills, methods,
  runtime behavior, ports, evaluations, or lifecycle agreements;

Contract Definition
→ does not absorb workflow phase orchestration unless its contract kind owns it;

workflow publication
→ cannot silently change referenced contract meaning;

contract breaking change
→ may create a workflow compatibility or migration requirement.
```

## 9.2 Workflow Definition And Workflow Run

```text
Workflow Run
→ pins the Workflow Version used to start or resume the run;

Workflow Definition
→ remains immutable for the pinned published version;

new Workflow Version
→ does not rewrite active or historical Workflow Runs;

mid-run migration
→ requires explicit compatibility policy, decision, and traceable transition.
```

## 9.3 Context Pack And Material Actions

```text
Specification, Workflow Run, Execution Run, Evaluation Run, Decision Case,
Learning Candidate, and Evolution Proposal
→ may reference the Context Pack assembly checkpoint used;

Context Pack update
→ does not rewrite the reasoning inputs of prior actions;

Context Gap
→ may block, narrow, or route a material action according to policy;

context availability
→ does not replace authority or execution capacity checks.
```

## 9.4 Product Instance And Runtime Binding

```text
Product Instance
→ references accepted product and environment bindings;

Runtime Binding
→ remains owned by C4 and may be activated or suspended independently;

Product Binding
→ selects and constrains a binding for product use;

binding presence
→ does not prove adapter conformance, runtime health, or successful execution.
```

## 9.5 Learning Candidate And Evolution Proposal

```text
Learning Candidate PROMOTION_RECOMMENDED
→ may create an Evolution Proposal;

Evolution Proposal
→ references the candidate but performs independent compatibility,
  consumer, authority, and migration analysis;

Learning Candidate
→ remains source provenance and cannot mutate the proposal after snapshotting silently;

Evolution rejection
→ does not rewrite the source case or erase the candidate lesson.
```

## 9.6 Evolution Proposal And Contract Or Workflow Definitions

```text
ACCEPTED Evolution Proposal
→ may authorize bounded creation or modification work through C7;

Execution Run
→ records actual artifact mutation;

Contract or Workflow publication
→ follows its own aggregate invariants and publication authority;

Evolution Proposal IMPLEMENTED
→ cannot be claimed solely from an accepted decision or patch plan;

Evolution Proposal VERIFIED
→ requires evidence for declared target and consumer migration scope.
```

---

# 10. Transaction And Consistency Boundaries

Candidate synchronous mutation boundaries:

```text
Contract Definition transaction
→ one draft mutation, version creation, publication, deprecation,
  retirement, or supersession transition;

Workflow Definition transaction
→ one draft mutation, phase or gate definition change,
  version publication, deprecation, retirement, or supersession transition;

Context Pack transaction
→ one requirement, source, retrieval, gap, checkpoint,
  freshness, or lifecycle mutation;

Product Instance transaction
→ one product binding, environment, target, policy reference,
  validation reference, or product lifecycle mutation;

Learning Candidate transaction
→ one source, evidence, generalization, counterexample,
  recommendation, assessment, or disposition mutation;

Evolution Proposal transaction
→ one proposed-change, consumer, compatibility, migration,
  decision-reference, implementation-reference, evidence, or lifecycle mutation.
```

Cross-aggregate effects use events or application coordination.

Examples:

```text
Contract Version Published
→ registry use case may register the artifact;

Workflow Version Published
→ product or runtime owners may assess compatibility before binding it;

Context Pack Became Blocked
→ host workflow may stop or route according to policy;

Learning Candidate Promotion Recommended
→ evolution use case may create an Evolution Proposal;

Evolution Accepted
→ execution use case may prepare the authorized target-layer change;

Evolution Implemented
→ migration coordinator may start consumer migration;

Evolution Verified
→ documentation and registry views may report the bounded verified state.
```

No event bypasses target-context policy, evidence, capacity, compatibility, or authority requirements.

---

# 11. Candidate Repository Boundaries

DDD repository guidance is applied only where persistence and aggregate retrieval are actually needed.

Candidate repository interfaces:

```text
Contract Definition Repository;
Workflow Definition Repository;
Context Pack Repository;
Product Instance Repository;
Learning Candidate Repository;
Evolution Proposal Repository.
```

Rules:

```text
Repositories expose aggregate roots or aggregate snapshots for mutation.

Read models, search indexes, registries, manifests, and reporting projections
may return projections or immutable records without pretending to be aggregate repositories.

A generated manifest is a registry projection, not the Contract Definition aggregate itself.

A product registry view is not the Product Instance aggregate itself.

Repository interface requirements must not be forced on non-persistent document-only usage
until the canonical model and issue #8 schema decisions require them.
```

This refines, but does not yet change, the current DDD contract's absolute repository rule.

---

# 12. Remaining Aggregate Questions

1. Should `Contract Definition` be one lineage aggregate containing immutable versions, or should each published Contract Version become an independently addressable aggregate root linked by lineage?
2. Does `Rule Definition` belong inside Contract Definition only when contract-scoped, while reusable policies remain C7 aggregates?
3. Should Workflow Definition own reusable Gate Definitions, or may shared gate definitions be referenced from C2 contracts?
4. Which Workflow Definition changes are compatible with active Workflow Runs?
5. Should Context Pack `USABLE` and `BLOCKED` be persisted states or derived from requirements, gaps, and freshness?
6. Should assembly checkpoints be child entities or immutable independent records referenced by material actions?
7. Which Product Instance registry fields belong in universal core versus `native-ai-fw` control-plane implementation?
8. Should Product Binding and Runtime Binding share a small published-language value model or remain entirely separate with translation?
9. Should Learning Candidate disposition be one derived result or persisted lifecycle state?
10. When may multiple Learning Candidates be combined into one Evolution Proposal?
11. Should consumer migration state live inside Evolution Proposal or in independent migration-run aggregates for large distributed changes?
12. Which aggregate IDs and events require first-class schemas in issue `#8`?

---

# 13. Validation Gates

Before this slice may become canonical input:

- [ ] every aggregate has one root and a defensible consistency boundary;
- [ ] published definition versions are immutable;
- [ ] definition, registration, implementation, execution, and conformance remain distinct;
- [ ] Context Pack does not become authority or truth container;
- [ ] Product Instance specializes but does not redefine core;
- [ ] Learning Candidate cannot self-promote;
- [ ] Evolution Proposal cannot self-approve or claim consumer adoption without evidence;
- [ ] lifecycle vocabulary is aggregate-specific;
- [ ] commands requiring authority route through C7;
- [ ] events are past-tense occurrence records and do not bypass target-context gates;
- [ ] repository guidance distinguishes aggregate mutation from projections and registries;
- [ ] issue `#7` can consume capability, port, adapter, and binding boundaries;
- [ ] issue `#8` can consume identity, version, lifecycle, reference, and event requirements;
- [ ] issue `#9` can consume compatibility, conformance, readiness, and verification distinctions;
- [ ] `ai-native-skills` can map definitions to executable methods without copying runtime state into core;
- [ ] `native-ai-fw` can map product registry, context packs, bindings, runs, and migrations without redefining domain ownership.

---

# 14. Current Verdict

```text
Second aggregate inventory: COMPLETE
Contract Definition boundary: CANDIDATE DEFINED
Workflow Definition boundary: CANDIDATE DEFINED
Context Pack boundary: CANDIDATE DEFINED
Product Instance boundary: CANDIDATE DEFINED
Learning Candidate boundary: CANDIDATE DEFINED
Evolution Proposal boundary: CANDIDATE DEFINED
Definition vs execution: SEPARATED
Context vs authority: SEPARATED
Product specialization vs core: SEPARATED
Learning vs promotion: SEPARATED
Proposal vs decision vs migration: SEPARATED
Contract migrations: NONE AUTHORIZED
Canonical aggregate model ready to freeze: NO
Ready for context-map and aggregate-pruning review: YES
```