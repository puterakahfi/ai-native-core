# Native AI Engineering Domain Model — Concept Ownership Matrix

Status: Candidate discovery artifact — non-canonical

Issue: `#6 — Define the canonical Native AI Engineering domain model`

Branch: `6-canonical-native-ai-engineering-domain-model`

Accepted foundation: [`../philosophy/README.md`](../philosophy/README.md)

Discovery inventory: [`../native-ai-engineering-domain-model-discovery.md`](../native-ai-engineering-domain-model-discovery.md)

This document classifies candidate Native AI Engineering concepts by owner, domain kind, lifecycle, and prohibited semantic collapse.

It is not yet the canonical domain model and does not authorize contract, schema, manifest, validator, adapter, or runtime migration.

---

## 1. Purpose

The repository currently uses many correct concepts without one canonical ownership model.

The main risk is not missing vocabulary. It is semantic collapse across definitions, runs, records, assessments, decisions, and authority.

This matrix exists to prevent failures such as:

```text
workflow definition treated as workflow execution;
skill installation treated as skill application;
contract presence treated as conformance;
review verdict treated as approval;
gate result treated as authorization;
release eligibility treated as permission to release;
implementation activity treated as completion;
feedback treated as accepted learning;
local change treated as canonical evolution.
```

Every retained first-class concept must have:

```text
one primary bounded-context owner;
one canonical meaning;
an explicit lifecycle or immutability rule;
named upstream and downstream relations;
prohibited collapses;
a downstream consumer.
```

---

## 2. Classification Rules

### Entity

Use when the concept has stable identity and changes across time while remaining the same domain object.

Examples:

```text
Specification;
Requirement;
Workflow Run;
Decision Record;
Learning Candidate.
```

### Aggregate Root

Use when the concept owns a consistency boundary and controls mutation of related entities or value objects.

Examples under review:

```text
Specification;
Contract Definition;
Workflow Definition;
Workflow Run;
Evidence Set;
Decision Case;
Context Pack;
Product Instance;
Learning Candidate;
Evolution Proposal.
```

### Value Object

Use when identity is irrelevant and equality is based on bounded values.

Examples:

```text
Scope;
Coverage;
Authority Requirement;
Verdict;
Compatibility Range;
Effective Decision view.
```

### Definition

A versioned description of intended or required behavior.

```text
Capability Definition;
Use Case Definition;
Contract Definition;
Port Definition;
Workflow Definition;
Skill Definition;
Policy Definition.
```

A definition is not evidence that the behavior exists or was applied.

### Run

A time-bounded attempted or completed execution of a definition or operation.

```text
Workflow Run;
Execution Run;
Verification Run;
Validation Run;
Evaluation Run.
```

A run is not success, completion, conformance, or authorization by default.

### Record

An attributable durable account of a domain occurrence, decision, observation, review, or delivery.

```text
Observation Record;
Review Record;
Decision Record;
Delivery Record;
Memory Record.
```

A record is not automatically correct, authoritative, or current.

### Assessment

A bounded determination based on declared inputs, criteria, method, and coverage.

```text
Claim Assessment;
Gate Evaluation;
Conformance Assessment;
Completion Assessment;
Authorization Assessment;
Promotion Assessment.
```

An assessment must not silently become a decision owned by another context.

### Policy

A rule governing allowed decisions or transitions within declared scope.

Policies may require review, approval, evidence, risk control, migration, or rollback.

A policy is not a capability, workflow, or execution result.

### Command

An intention to perform a named domain action.

A command requires applicable permission, authority, policy, preconditions, and execution capacity.

### Event

An attributable statement that a meaningful domain occurrence happened.

An event records an occurrence. It does not itself authorize the next action.

---

## 3. Minimal Shared Kernel

The domain contexts need a small reference kernel. This kernel owns no business lifecycle.

| Primitive | Kind | Purpose | Must not become |
|---|---|---|---|
| `ActorRef` | value object | Reference a human, agent, system, team, or service actor | Authority proof |
| `SourceRef` | value object | Reference an attributable source | Claim that the source is correct or authoritative |
| `Scope` | value object | Bound subjects, actions, claims, environments, time, and consumers | Generic free-text status |
| `Coverage` | value object | Describe what was actually observed, executed, tested, evaluated, or reviewed | Quality or completion |
| `VersionRef` | value object | Reference a versioned definition or artifact | Compatibility proof |
| `ArtifactRef` | value object | Reference a repository, document, contract, output, or generated artifact | Evidence by presence alone |
| `TimeWindow` | value object | Bound temporal validity or observation period | Current-state proof |
| `RiskLevel` | value object | Express declared risk classification | Risk acceptance |
| `ReferenceSet` | value object | Carry typed references across context boundaries | Ownership transfer |

Shared-kernel references must remain typed. A generic untyped `metadata` or `status` object must not replace owned domain concepts.

---

## 4. Candidate Bounded Contexts

The matrix currently retains ten context families for further validation.

```text
C1 Intent And Specification
C2 Capability And Agreement
C3 Method And Workflow
C4 Port, Adapter, And Runtime Binding
C5 Execution And Operations
C6 Evidence, Evaluation, And Acceptance
C7 Governance, Risk, And Authority
C8 Context, Knowledge, And Memory
C9 Product Instance And Registry
C10 Feedback, Learning, And Evolution
```

These are candidate consistency boundaries, not mandatory package names or deployment services.

---

## 5. Concept Ownership Matrix

### C1 — Intent And Specification

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Intent` | entity within `Specification` aggregate | C1 | motivates requirements and capabilities | Intent ≠ implementation state |
| `Specification` | aggregate root, versioned definition | C1 | owns requirements, constraints, scope, acceptance criteria | Specification ≠ approval |
| `Requirement` | entity | C1 | belongs to one specification version; traces to capability and evidence | Requirement ≠ task |
| `Acceptance Criterion` | entity | C1 | defines a checkable expected condition | Criterion ≠ criterion result |
| `Constraint` | value object | C1 | limits solution or operation | Constraint ≠ implementation decision unless accepted |
| `Non-Goal` | value object | C1 | explicitly excludes scope | Non-goal ≠ future prohibition outside scope |
| `Success Measure` | value object or entity when independently tracked | C1 | provides intended outcome measure | Measure definition ≠ measured evidence |
| `Specification Status` | context-specific state value | C1 | draft, reviewable, accepted, superseded where policy defines | Status ≠ approval source |

Candidate aggregate:

```text
Specification
├── Intent
├── Requirements
├── Acceptance Criteria
├── Constraints
├── Non-Goals
├── Scope
└── Success Measures
```

The aggregate may record approval references, but C7 owns authoritative decisions and approval meaning.

### C2 — Capability And Agreement

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Capability Definition` | aggregate root or entity | C2 | realized through use cases, contracts, ports, skills, and adapters | Capability ≠ authority |
| `Use Case Definition` | entity or aggregate root | C2 | coordinates domain response using capabilities | Use case ≠ workflow run |
| `Contract Definition` | aggregate root, versioned definition | C2 | defines stable agreement, boundary, gates, and compatibility | Contract presence ≠ conformance |
| `Contract Version` | value object | C2 | versions one contract line | Version ≠ maturity |
| `Compatibility Range` | value object | C2 | expresses accepted consumer compatibility | Compatible pin ≠ behavioral proof |
| `Boundary Declaration` | value object | C2 | states owned and delegated responsibility | Declaration ≠ embodiment |
| `Rule Definition` | entity or value object depending reuse | C2 | mandatory reusable constraint | Rule ≠ policy authority unless assigned |
| `Template Definition` | versioned definition | C2 | reusable artifact structure | Template ≠ completed artifact |

Candidate aggregate:

```text
Contract Definition
├── Contract Identity
├── Version
├── Boundary
├── Inputs And Outputs
├── Quality Gates
├── Compatibility Policy
└── Adapter Requirements
```

C2 defines stable agreements. C6 assesses conformance. C7 governs approval of breaking or canonical changes.

### C3 — Method And Workflow

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Skill Definition` | aggregate root, versioned definition | C3 | implements or specializes capability contracts | Skill installed ≠ skill applied |
| `Method Definition` | definition | C3 | describes reusable specialist procedure | Method ≠ execution |
| `Workflow Definition` | aggregate root, versioned definition | C3 | composes phases, methods, gates, and handoffs | Workflow definition ≠ workflow run |
| `Phase Definition` | entity within workflow aggregate | C3 | ordered or graph-linked lifecycle stage | Phase definition ≠ phase execution |
| `Gate Definition` | entity within workflow aggregate | C3 | declares transition condition and required evidence | Gate definition ≠ gate result |
| `Handoff Definition` | value object | C3 | defines output and ownership transition expectation | Handoff definition ≠ delivered artifact |
| `Skill Application` | execution reference owned by C5, definition reference owned by C3 | C5 primary | records one applied skill inside a run | Skill application ≠ skill definition |
| `Workflow Policy` | policy reference | C3 with C7 policy dependency | constrains allowed transitions and shortcuts | Workflow policy ≠ authorization |

Candidate aggregate:

```text
Workflow Definition
├── Phases
├── Gate Definitions
├── Handoffs
├── Required And Optional Skills
├── Transition Rules
└── Exit Conditions
```

Workflow execution state belongs to C5.

### C4 — Port, Adapter, And Runtime Binding

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Port Definition` | aggregate root or entity | C4 | exposes a required capability boundary | Port ≠ adapter |
| `Adapter Definition` | entity, versioned definition | C4 | declares implementation of a port or contract | Adapter declaration ≠ working integration |
| `Adapter Capability Declaration` | value object | C4 | declares supported operations and limitations | Declared capability ≠ permission |
| `Runtime Binding` | aggregate root or entity | C4 | binds definitions to adapter, runtime, configuration, and policy refs | Binding ≠ execution |
| `Tool Registration` | entity within runtime binding | C4 | registers callable tool surface | Tool access ≠ authority |
| `Provider Binding` | specialization of runtime binding | C4 | selects provider for a capability | Provider selection ≠ domain decision |
| `Repository Binding` | specialization of runtime binding | C4 | binds repository operations and policies | Repository token ≠ mutation authority |
| `Binding Compatibility Assessment` | assessment owned by C6 | C6 primary | evaluates version and declaration compatibility | Compatible binding ≠ runtime proof |

Candidate aggregate:

```text
Runtime Binding
├── Port Or Contract Reference
├── Adapter Reference
├── Runtime Surface
├── Configuration Reference
├── Capability Declaration
├── Limitations
├── Policy References
└── Compatibility References
```

Final port kinds remain owned by issue `#7`.

### C5 — Execution And Operations

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Workflow Run` | aggregate root | C5 | executes one workflow definition and coordinates phase runs | Workflow run ≠ workflow definition |
| `Phase Run` | entity within workflow run | C5 | records execution of one phase | Phase activity ≠ exit-gate pass |
| `Execution Run` | aggregate root or independently referenced entity | C5 | records actual bounded work performed through one or more operations | Execution ≠ success |
| `Operation Attempt` | entity within execution run | C5 | records one attempted operation | Attempt ≠ completion |
| `Tool Invocation` | entity within execution run | C5 | records tool request and observed result | Invocation ≠ authorized use |
| `Skill Application` | entity within workflow or execution run | C5 | records selected skill, inputs, outputs, and evidence refs | Applied reference ≠ correct behavior |
| `Execution Result` | immutable record or value object | C5 | summarizes direct run outcome and produced artifacts | Result ≠ evidence sufficiency |
| `Operational Incident` | aggregate root or entity | C5 | records degradation, failure, mitigation, and recovery | Incident closed ≠ root cause learned |
| `Delivery Record` | entity | C5 | records an executed handoff, release, deployment, export, or publication | Delivery record ≠ delivery authorization |
| `Rollback Record` | entity | C5 | records rollback execution and resulting state | Rollback plan ≠ rollback performed |

Candidate aggregate relationships:

```text
Workflow Run
├── Phase Runs
├── Skill Applications
├── Gate Evaluation References
├── Decision And Authorization References
└── Execution Run References

Execution Run
├── Operation Attempts
├── Tool Invocations
├── Produced Artifact References
├── Observation References
└── Direct Execution Result
```

C5 records performed work. C6 owns claims about whether it satisfies criteria. C7 owns whether the work was authorized.

### C6 — Evidence, Evaluation, And Acceptance

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Claim` | entity or immutable record | C6 | states a bounded proposition to assess | Claim ≠ evidence |
| `Observation Record` | immutable record | C6 | attributable observation about state | Observation ≠ interpretation or fact |
| `Evidence Item` | entity | C6 | supports, weakens, distinguishes, or challenges claims | Evidence ≠ authority |
| `Evidence Set` | aggregate root | C6 | groups evidence for declared claims, criteria, scope, and coverage | Evidence set ≠ automatic PASS |
| `Claim Assessment` | assessment record | C6 | evaluates a claim against evidence and method | Assessment ≠ approval |
| `Verification Run` | entity or specialized evaluation run | C6 | checks whether a specified claim or property is supported | Verification ≠ intended-use validation |
| `Validation Run` | entity or specialized evaluation run | C6 | checks fitness for intended use and context | Validation ≠ authorization |
| `Evaluation Run` | aggregate root | C6 | applies declared criteria and produces findings and verdict | Evaluation ≠ approval |
| `Gate Evaluation` | assessment record | C6 | evaluates one gate definition for one transition attempt | Gate PASS ≠ authority to act when approval remains |
| `Review Record` | aggregate root or entity | C6 | records reviewer, scope, evidence, findings, and verdict | Review verdict ≠ approval by default |
| `Finding` | entity when tracked; value object when immutable local result | C6 | identifies issue, severity, evidence, and affected scope | Finding ≠ decision |
| `Verdict` | value object | C6 | bounded assessment outcome | Verdict ≠ approval unless governance explicitly assigns it |
| `Conformance Assessment` | assessment record | C6 | evaluates named evidence layers against a contract | Structural conformance ≠ behavior |
| `Completion Assessment` | assessment record | C6 | evaluates whether scope and acceptance conditions are coherently complete | Activity performed ≠ completion |
| `Release Eligibility` | specialized evaluation result | C6 | states quality/readiness against release criteria | Eligibility ≠ authorization to release |

Candidate aggregate:

```text
Evidence Set
├── Claims
├── Evidence Items
├── Source And Method References
├── Scope And Coverage
└── Unknowns And Gaps

Evaluation Run
├── Criteria
├── Evidence Set References
├── Findings
├── Coverage
├── Verdict
└── Limitations
```

C6 may produce readiness or eligibility. C7 decides whether authority requirements are satisfied.

### C7 — Governance, Risk, And Authority

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Decision Case` | aggregate root candidate | C7 | groups decision records, conflicts, supersession, and effective view | Decision case ≠ review record |
| `Decision Record` | entity | C7 | attributable selection, rejection, commitment, approval, or constraint | Decision ≠ approval by default |
| `Effective Decision` | derived value object or read model | C7 | resolves currently governing decision within scope | Newest record ≠ effective decision |
| `Authority Requirement` | value object | C7 | declares required decision right for action or transition | Requirement ≠ authority held |
| `Authority Grant` | entity or external-authority reference | C7 | records assigned authority within scope | Authority ≠ technical permission |
| `Permission Grant` | entity or referenced access-control fact | C7 | records technical or policy allowance | Permission ≠ authority or approval |
| `Approval` | semantic classification of an authority-bearing positive `Decision Record` | C7 | permits named action or transition within scope | Approval ≠ review verdict |
| `Risk` | aggregate root or entity | C7 | owns risk statement, owner, mitigation, status, and exposure | Risk ≠ finding |
| `Risk Acceptance` | authority-bearing `Decision Record` specialization | C7 | accepts bounded residual risk under policy | Acceptance ≠ risk disappearance |
| `Policy Definition` | aggregate root or entity | C7 | defines governance rules, authority, controls, and exceptions | Policy ≠ workflow execution |
| `Decision Conflict` | entity or value object within decision case | C7 | preserves incompatible authoritative decisions | Conflict ≠ silently resolved by recency |
| `Supersession Link` | value object | C7 | explicitly links replaced decision or policy | Later timestamp ≠ supersession |
| `Authorization Assessment` | assessment record | C7 | determines whether a named action may proceed now | Authorization ≠ quality readiness |
| `Exception Or Waiver` | authority-bearing decision specialization | C7 | permits bounded deviation under policy | Waiver ≠ contract deletion |

Key deduplication decisions:

```text
Approval is not a standalone aggregate.
Approval is an authority-bearing positive Decision Record with bounded scope.

Risk Acceptance is not a standalone aggregate.
Risk Acceptance is an authority-bearing Decision Record over a named residual risk.

Effective Decision is not another mutable decision entity.
It is a derived view over attributable decision records, conflicts, supersession,
policy, scope, and authority.
```

Candidate aggregate:

```text
Decision Case
├── Decision Records
├── Authority Requirements
├── Authority And Permission References
├── Conflicts
├── Supersession Links
└── Effective Decision View
```

### C8 — Context, Knowledge, And Memory

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Context Pack` | aggregate root | C8 | assembles bounded context references for one task, actor, or execution | Context pack ≠ source of truth by itself |
| `Knowledge Artifact` | entity, versioned artifact | C8 | stores explicit reviewable information | Knowledge ≠ immutable truth |
| `Source Of Truth Designation` | governed relation backed by C7 decision | C8 primary relation, C7 authority | identifies primary source for named information class | Designation ≠ correctness proof |
| `Memory Record` | entity | C8 | retains history, preference, pattern, or prior outcome | Memory ≠ current state |
| `Retrieval Result` | immutable record | C8 | records what retrieval returned, from where, and when | Retrieval ≠ verification |
| `Context Requirement` | value object | C8 | declares required context classes and freshness | Requirement ≠ available context |
| `Knowledge Supersession Link` | governed relation | C8 | links superseded knowledge artifacts | Newer file ≠ authoritative supersession |
| `Context Gap` | finding or value object | C8 | records missing, stale, inaccessible, or conflicting context | Gap ≠ fabricated default |

Candidate aggregate:

```text
Context Pack
├── Context Requirements
├── Knowledge Artifact References
├── Memory Record References
├── Retrieval Results
├── Source And Freshness Metadata
└── Context Gaps
```

Procedural behavior belongs to C3 skills and workflows, not a generic memory type.

### C9 — Product Instance And Registry

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Product Instance` | aggregate root | C9 | owns product-specific intent, policy, bindings, implementation refs, and validation refs | Product instance ≠ universal core |
| `Product Registry Entry` | entity | C9 | registers product identity, repository, lifecycle, and ownership refs | Registry presence ≠ product health |
| `Product Binding` | entity | C9 | binds product instance to capabilities, contracts, ports, runtimes, and adapters | Product binding ≠ runtime execution |
| `Environment Binding` | entity or value object | C9 | binds environment-specific runtime and policy references | Environment config ≠ product policy |
| `Delivery Target` | value object | C9 | describes product-specific release, deployment, export, or publication target | Target ≠ authorized delivery |
| `Product Policy Reference` | reference relation | C9 | links product-specific policy owned by product repository or C7 | Reference ≠ policy satisfaction |
| `Product Validation Reference` | reference relation | C9 | links real-world product evidence | One field test ≠ universal truth |

C9 does not own delivery execution, release eligibility, or authorization:

```text
Delivery execution record → C5
Release eligibility → C6
Delivery authorization → C7
Product-specific target and binding → C9
```

This separation prevents one product-development workflow from becoming the universal engineering lifecycle.

### C10 — Feedback, Learning, And Evolution

| Concept | Candidate kind | Lifecycle owner | Relations | Prohibited collapse |
|---|---|---|---|---|
| `Feedback Item` | entity | C10 | records attributable consequence, observation, review, metric, or user input for revision | Feedback ≠ learning |
| `Learning Candidate` | aggregate root | C10 | proposes a reusable lesson from verified source cases | Candidate ≠ accepted shared change |
| `Generalization Assessment` | assessment record | C10 | tests transferability, counterexamples, and correct layer | One success ≠ generalized rule |
| `Target Layer Recommendation` | value object or proposed decision | C10 | recommends local, product, skill, workflow, eval, knowledge, or core destination | Recommendation ≠ authority to modify |
| `Promotion Assessment` | evaluation record | C10 with C6 method | evaluates evidence, duplication, transferability, regressions, and policy | Assessment PASS ≠ automatic write authority |
| `Evolution Proposal` | aggregate root | C10 | proposes change to shared or canonical agreement | Proposal ≠ accepted evolution |
| `Migration Plan` | entity or value object within evolution proposal | C10 | defines consumer compatibility and transition | Plan ≠ migration executed |
| `Evolution Decision` | C7 `Decision Record` reference | C7 primary | accepts, rejects, defers, or narrows proposal | Decision ≠ implementation |
| `Evolution Record` | immutable record | C10 | records accepted change, migration, and supersession refs | Record ≠ downstream adoption proof |

Candidate aggregates:

```text
Learning Candidate
├── Source Cases
├── Verified Evidence References
├── Generalized Reason
├── Counterexamples
├── Target Layer Recommendation
├── Duplicate Coverage Findings
└── Promotion Assessment References

Evolution Proposal
├── Proposed Shared Change
├── Affected Consumers
├── Compatibility Analysis
├── Migration Plan
├── Required Authority
└── Decision And Implementation References
```

---

## 6. Cross-Concept Deduplication Decisions

### Definition, Application, And Evidence

```text
Skill Definition
≠ Skill Installation
≠ Skill Application
≠ Skill Application Evidence
≠ Skill Conformance Assessment.
```

```text
Workflow Definition
≠ Workflow Run
≠ Phase Run
≠ Gate Evaluation
≠ Workflow Completion Assessment.
```

```text
Contract Definition
≠ Contract Registration
≠ Contract Compatibility
≠ Structural Conformance
≠ Behavioral Conformance
≠ Runtime Integration
≠ Product Acceptance.
```

### Review, Decision, Approval, And Authorization

```text
Review Record
→ findings and verdict produced from evidence;

Decision Record
→ attributable selection, rejection, commitment, or constraint;

Approval
→ authority-bearing positive Decision Record;

Effective Decision
→ currently governing decision view after scope, authority,
   conflict, policy, and supersession resolution;

Authorization Assessment
→ determination whether one action may proceed now.
```

Therefore:

```text
review verdict ≠ approval;
approval ≠ technical permission;
permission ≠ authority;
readiness ≠ authorization;
authorization ≠ successful execution.
```

### Gate, Readiness, Eligibility, And Completion

```text
Gate Definition
→ declared transition condition;

Gate Evaluation
→ evidence-backed result for one transition attempt;

Readiness Or Eligibility
→ evaluation result across declared criteria;

Completion Assessment
→ coherence judgment across accepted scope;

Authorization
→ governance result for the named action.
```

A passed gate may still be blocked by another gate, missing approval, policy, authority, or execution capacity.

### Binding And Execution

```text
Adapter Definition
≠ Runtime Binding
≠ Tool Registration
≠ Tool Invocation
≠ Execution Result
≠ Runtime Integration Evidence.
```

### Feedback And Evolution

```text
Feedback Item
≠ Learning Candidate
≠ Generalized Learning
≠ Evolution Proposal
≠ Evolution Decision
≠ Migration Execution
≠ Consumer Adoption.
```

---

## 7. Generic Status Is Rejected

The canonical model must not introduce one shared enum such as:

```text
PENDING
APPROVED
FAILED
COMPLETED
```

for unrelated contexts.

Each aggregate owns context-specific state with explicit transitions.

Examples:

```text
Specification State
Workflow Run State
Execution Run State
Evaluation State
Decision Case State
Risk State
Learning Candidate State
Evolution Proposal State
```

A cross-context summary may expose normalized categories for UI or reporting, but that summary is a read model, not canonical lifecycle authority.

---

## 8. Candidate Commands

Commands are illustrative domain actions. Final command names remain under canonical-model review.

### C1

```text
Define Intent
Create Specification
Add Requirement
Add Acceptance Criterion
Revise Specification
Supersede Specification Version
```

### C2

```text
Register Capability
Define Use Case
Publish Contract Version
Deprecate Contract Version
Declare Compatibility
```

### C3

```text
Publish Skill Definition
Publish Workflow Definition
Add Phase Definition
Add Gate Definition
Deprecate Method Version
```

### C4

```text
Register Adapter Definition
Create Runtime Binding
Activate Binding
Suspend Binding
Register Tool
```

### C5

```text
Start Workflow Run
Start Phase Run
Start Execution Run
Invoke Tool
Record Operation Result
Record Delivery
Record Rollback
```

### C6

```text
Record Observation
Add Evidence
Assess Claim
Run Verification
Run Validation
Run Evaluation
Evaluate Gate
Complete Review
Assess Conformance
Assess Completion
```

### C7

```text
Record Decision
Resolve Decision Conflict
Supersede Decision
Grant Authority
Grant Permission
Assess Authorization
Accept Risk
Issue Waiver
```

### C8

```text
Create Context Pack
Register Knowledge Artifact
Designate Source Of Truth
Record Memory
Retrieve Context
Record Context Gap
Supersede Knowledge Artifact
```

### C9

```text
Register Product Instance
Bind Product Capability
Bind Product Runtime
Register Environment
Declare Delivery Target
```

### C10

```text
Record Feedback
Create Learning Candidate
Assess Generalization
Propose Evolution
Approve Evolution Proposal
Execute Migration
Record Evolution
```

Commands that require authority must carry or resolve decision and authorization references. Command existence is not authorization.

---

## 9. Candidate Domain Events

Events are illustrative and must remain past-tense occurrence records.

```text
Intent Defined
Specification Version Created
Requirement Added
Acceptance Criterion Added
Specification Superseded

Capability Registered
Use Case Defined
Contract Version Published
Contract Version Deprecated

Skill Definition Published
Workflow Definition Published
Gate Definition Added

Adapter Registered
Runtime Binding Activated
Runtime Binding Suspended
Tool Registered

Workflow Run Started
Phase Run Started
Execution Run Started
Operation Attempted
Tool Invoked
Execution Run Completed
Delivery Recorded
Rollback Recorded

Observation Recorded
Evidence Added
Claim Assessed
Verification Completed
Validation Completed
Evaluation Completed
Gate Evaluated
Review Completed
Conformance Assessed
Completion Assessed

Decision Recorded
Decision Became Effective
Decision Conflict Recorded
Decision Superseded
Authority Granted
Permission Granted
Authorization Assessed
Risk Accepted
Waiver Issued

Context Pack Created
Knowledge Artifact Registered
Source Of Truth Designated
Memory Recorded
Context Gap Recorded
Knowledge Artifact Superseded

Product Instance Registered
Product Binding Activated
Environment Registered

Feedback Recorded
Learning Candidate Created
Generalization Assessed
Evolution Proposed
Evolution Accepted
Migration Completed
Evolution Recorded
```

An event may trigger another context to evaluate or act. It must not silently bypass that context's policy, evidence, or authority gates.

---

## 10. Candidate Context Map

```text
C1 Intent And Specification
  defines what is wanted and how acceptance is expressed
        ↓
C2 Capability And Agreement
  defines stable capabilities, use cases, contracts, and reusable rules
        ↓
C3 Method And Workflow
  defines reusable execution methods and lifecycle coordination
        ↓
C4 Port, Adapter, And Runtime Binding
  binds required capability boundaries to replaceable implementations
        ↓
C5 Execution And Operations
  performs authorized work and records actual runs and delivery
        ↓
C6 Evidence, Evaluation, And Acceptance
  evaluates claims, gates, conformance, readiness, and completion
        ↔
C7 Governance, Risk, And Authority
  governs decisions, approval, risk, policy, and authorization

C8 Context, Knowledge, And Memory
  supplies attributable context and source references to all contexts

C9 Product Instance And Registry
  binds universal definitions to product-specific repositories,
  environments, targets, policies, and validation references

C10 Feedback, Learning, And Evolution
  processes consequences and proposes governed change at the correct layer
```

Dependency constraints:

```text
C2 must not depend on provider or product implementation details;
C3 may reference C2 definitions but must not own contract authority;
C4 implements or binds C2/C3 agreements but must not redefine them;
C5 records execution but must not self-assess authoritative success;
C6 evaluates evidence but must not self-authorize governed actions;
C7 may authorize actions but must not fabricate technical evidence;
C8 may supply context but must not override current authoritative sources;
C9 specializes universal concepts but must not redefine core;
C10 may propose shared change but must not self-promote without authority.
```

---

## 11. Existing Source Reconciliation

### `docs/domain-driven-model.md`

Retain as DDD guidance and product-example material.

Do not treat its example entities such as `Brand`, `Campaign`, or `GeneratedAsset` as Native AI Engineering core concepts.

Its generic `ReviewDecision` example must be replaced or annotated after the canonical model is accepted because review verdict, decision, approval, and authorization are distinct concepts.

### `docs/port-taxonomy.md`

Retain as pre-canonical port inventory.

Issue `#7` must consume C2 capability ownership and C4 port/binding boundaries. It must not define `Port = capability contract` as strict identity.

### `docs/contract-catalog.md`

Preserve its distinctions:

```text
skill contract → reusable capability interface;
workflow contract → ordered lifecycle agreement;
runtime contract → runtime-facing agreement;
test contract → behavioral evaluation case;
manifest entry → registered artifact identity, not implementation proof.
```

### `docs/adapter-conformance.md`

Map its evidence layers into C6 `Conformance Assessment`:

```text
path resolution;
version compatibility;
structural representation;
boundary declaration consistency;
behavioral evaluation;
runtime integration;
product acceptance.
```

No single Boolean conformance state may replace these layers.

### `contracts/skills/quality/decision-provenance.contract.yaml`

Use as strong evidence for C7 ownership:

```text
Decision Record;
Effective Decision;
Authority Requirement;
Conflict;
Supersession;
Authorization Assessment.
```

The contract's records must not become the complete canonical aggregate automatically; issue `#6` still owns domain generalization.

### `contracts/skills/quality/skill-evolution.contract.yaml`

Use as strong evidence for C10 ownership:

```text
Learning Candidate;
Generalization Assessment;
Target Layer Recommendation;
Promotion Assessment;
Evolution Proposal;
Migration And Promotion References.
```

### `contracts/workflows/new-feature.contract.yaml`

Use as evidence for separation between:

```text
workflow definition;
workflow run;
execution evidence;
review verdict;
merge authorization.
```

### `contracts/workflows/product-development.contract.yaml`

Use as evidence for separation between:

```text
acceptance criterion;
criterion assessment;
release eligibility;
release authorization;
deployment execution;
launch execution;
post-launch feedback.
```

Its product lifecycle is a workflow specialization, not the universal Native AI Engineering aggregate lifecycle.

### `contracts/runtime/memory.contract.yaml`

Candidate conflict:

```text
procedural behavior is currently classified as a memory type;
canonical ownership places reusable executable procedure in C3 Skill Or Workflow Definition.
```

No contract change is authorized in this artifact. The canonical model must record whether this becomes terminology clarification, compatibility alias, or future migration proposal.

---

## 12. Current Retention Decisions

### Retain as first-class candidate concepts

```text
Specification
Requirement
Acceptance Criterion
Capability Definition
Use Case Definition
Contract Definition
Skill Definition
Workflow Definition
Port Definition
Adapter Definition
Runtime Binding
Product Instance
Workflow Run
Execution Run
Evidence Item
Evidence Set
Evaluation Run
Gate Evaluation
Review Record
Decision Record
Decision Case
Risk
Context Pack
Knowledge Artifact
Memory Record
Feedback Item
Learning Candidate
Evolution Proposal
```

### Retain as derived view, value object, assessment, or specialization

```text
Effective Decision
Approval
Risk Acceptance
Release Eligibility
Authorization Assessment
Completion Assessment
Conformance Assessment
Verdict
Coverage
Scope
Compatibility Range
Delivery Authorization
Deployment Record
Launch Record
Promotion Assessment
Target Layer Recommendation
```

### Reject as generic universal concepts

```text
one global Status enum;
one global Approval state;
one Boolean Conformance field;
one generic Result object for all contexts;
one universal Product Development lifecycle;
Port as strict synonym for Capability Contract;
procedural Skill as generic Memory Record;
ReviewDecision as collapsed review, decision, and approval object.
```

---

## 13. Open Questions

The following remain unresolved and must be answered before freezing the canonical model:

1. Should `Capability Definition` and `Use Case Definition` be separate aggregates or entities under one capability aggregate?
2. Should `Contract Definition` own `Rule Definition`, or should reusable rules have independent lifecycle and references?
3. Should `Execution Run` always belong to one `Workflow Run`, or support standalone execution with optional workflow reference?
4. Should `Review Record` be an aggregate root or an entity within an `Evaluation Run` aggregate?
5. Should `Evidence Set` own claims, or should claims be independently addressable entities linked to many evidence sets?
6. Should `Decision Case` be the aggregate root over decisions, authority, conflicts, and supersession?
7. How should external organizational authority and technical permission systems be referenced without importing provider-specific models?
8. Should `Product Binding` specialize `Runtime Binding`, or remain a distinct product-context relation?
9. Which product-registry concepts belong in universal core versus `native-ai-fw` control-plane ownership?
10. How should existing `procedural memory` terminology migrate without breaking runtime-contract consumers?
11. Which concepts require canonical IDs and versioning rules in issue `#8`?
12. Which cross-context events are public domain events versus internal implementation events?

---

## 14. Validation Gates For This Matrix

Before this matrix may become canonical input:

- [ ] every first-class concept has one primary owner;
- [ ] definitions, runs, records, assessments, decisions, and events remain distinct;
- [ ] review, decision, approval, permission, authority, readiness, and authorization remain distinct;
- [ ] contract, port, adapter, binding, and execution remain distinct;
- [ ] generic status and Boolean conformance models are rejected;
- [ ] product examples remain outside universal core ownership;
- [ ] current contract concepts map without silent contract migration;
- [ ] candidate aggregates explain their consistency boundaries;
- [ ] candidate commands and events do not bypass evidence or authority;
- [ ] issue `#7` can consume capability and port boundaries;
- [ ] issue `#8` can consume entity, reference, lifecycle, and schema requirements;
- [ ] issue `#9` can consume layered conformance and assessment semantics;
- [ ] `ai-native-skills` can map definitions to executable applications;
- [ ] `native-ai-fw` can map runs, bindings, decisions, evidence, and product registry behavior;
- [ ] representative product repositories can specialize the model without redefining core.

---

## 15. Current Verdict

```text
Concept inventory: SUFFICIENT FOR DEDUPLICATION
Primary owner assigned: CANDIDATE FOR RETAINED CONCEPTS
Definitions versus runs: SEPARATED
Review versus approval: SEPARATED
Readiness versus authorization: SEPARATED
Contract versus port versus adapter versus binding: SEPARATED
Generic status model: REJECTED
Boolean conformance model: REJECTED
Candidate bounded contexts: 10
Candidate aggregate roots: UNDER REVIEW
Contract migrations: NONE AUTHORIZED
Canonical model ready to freeze: NO
Ready for aggregate and lifecycle refinement: YES
```
