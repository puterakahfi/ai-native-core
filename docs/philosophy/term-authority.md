# Native AI Engineering Canonical Term Authority

Status: Candidate canonical vocabulary

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Derived laws: [`laws.md`](laws.md)

Principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

This document is the candidate atomic authority for philosophy-level terms used across Native AI Engineering.

It defines the minimum stable meaning and boundary of each term required by the doctrine, axioms, laws, principles, guardrails, epistemic loop, domain model, contracts, ports, skills, workflows, evaluation, and governed evolution.

It does not define the complete Native AI Engineering domain model owned by issue `#6`, and it does not silently replace accepted machine-readable contract semantics.

---

## 1. Purpose

Native AI Engineering coordinates people, agents, documents, models, tools, repositories, runtime systems, evidence, and decisions.

Without one atomic term authority, the same word may acquire different meanings in different layers:

```text
state may mean repository state, task state, memory, or an agent summary;
model may mean an AI model, domain model, architecture diagram, or interpretation;
fact may mean observation, confidence, decision, or accepted claim;
evidence may mean output, test result, review verdict, or approval;
authority may be confused with permission, capability, access, or ownership;
validation may be confused with verification, evaluation, review, or approval.
```

That drift creates:

```text
false certainty
false authority
false completion
untraceable decisions
incompatible contracts
parallel glossary authority
silent semantic evolution
```

This document prevents that collapse by defining one minimum meaning for each philosophy-level term.

---

## 2. Term Authority Model

### 2.1 Atomic definition authority

For terms listed in this document:

```text
atomic canonical definition
→ relationship maps and laws
→ domain specialization
→ contract and port semantics
→ skills, workflows, and adapters
→ runtime and product implementation
```

The atomic definition owns the minimum meaning.

More concrete layers may:

```text
specialize
qualify
constrain
add required fields
add allowed statuses
add evidence requirements
translate into runtime or product language
```

They must not:

```text
reverse the base meaning
collapse required distinctions
replace a term with a contradictory local definition
use an implementation detail as the universal definition
silently redefine the term for upstream layers
```

### 2.2 One primary owner per definition

A term should have one primary atomic definition.

Other artifacts may reference or explain it, but they should not maintain competing definitions.

```text
Canonical Term File  owns the atomic definition.
Relationship Map     owns relationships between terms.
Law                  owns a derived invariant using the terms.
Principle            owns decision orientation.
Guardrail            owns a mandatory boundary.
Domain Model         owns domain objects and relationships.
Contract             owns stable machine-readable agreement.
Adapter               owns contextual translation or implementation.
Glossary Index        owns navigation and short discovery labels.
```

### 2.3 Relationship to `docs/glossary.md`

`docs/glossary.md` remains the broad repository glossary and navigation index.

For philosophy-level terms defined here:

```text
this file owns the candidate atomic meaning;
the glossary should eventually link to this authority;
the glossary may provide a short index label but must not contradict this file;
conflicting existing wording is a reconciliation task before issue #13 acceptance.
```

Until issue `#13` is accepted, a conflict between this candidate vocabulary and an accepted contract or existing canonical artifact must be recorded and reviewed rather than silently resolved.

### 2.4 Context-specific qualification

A concrete layer should qualify a term rather than redefine it.

Examples:

```text
evidence
→ source evidence
→ static conformance evidence
→ behavioral evidence
→ runtime evidence
→ product acceptance evidence

approval
→ design approval
→ security approval
→ release approval

state
→ repository state
→ task state
→ runtime state
→ product state
```

Each qualified term inherits the base definition and narrows its scope.

### 2.5 Change governance

A material change to an atomic term requires:

```text
explicit owner
change rationale
affected-law review
affected-domain review
contract and consumer impact analysis
supersession or migration behavior
validation evidence
required authority
```

Adding an example is not necessarily a semantic change. Changing what the term includes, excludes, permits, proves, or owns is a semantic change.

---

## 3. Epistemic State Terms

### T1 — State

#### Definition

```text
State is the condition, configuration, event record, or other engineering-relevant
situation of a bounded subject at a bounded time or interval.
```

A state claim must identify enough scope to be meaningful.

Common scope dimensions include:

```text
subject
time or version
environment
repository or product
actor or system
coverage
```

#### State is not

```text
a summary of state
a model of state
an interpretation of state
an intended future state
a decision about state
evidence by itself
```

#### Boundary

State can exist without being currently known, observable, available, authoritative, or recorded.

---

### T2 — Observable State

#### Definition

```text
Observable state is state for which a defined observation path can produce a
bounded representation or record.
```

Examples of observation paths:

```text
repository read
runtime inspection
API response
user statement
issue record
test execution
product interaction
metric collection
review record
```

#### Observable state is not

```text
necessarily currently accessible
necessarily complete
necessarily authoritative
necessarily accurate without method review
identical to the observation record
```

#### Naming decision

The original issue candidate used:

```text
Engineering work begins from observable state.
```

The candidate axiom was refined to:

```text
Engineering work begins from available, attributable state.
```

This refinement avoids implying that every observable state is currently accessible to the actor.

---

### T3 — Available State

#### Definition

```text
Available state is observable or recorded state that the current actor can access
through an attributable source within the current execution context.
```

#### Available state is not

```text
all relevant state
complete coverage
authoritative by default
current by default
permission to act
```

#### Required consequence

Unavailable relevant state must remain explicit as:

```text
UNKNOWN
UNAVAILABLE
BLOCKED
NOT_VERIFIED
OUT_OF_COVERAGE
```

Exact machine statuses belong to contracts and domain modeling.

---

### T4 — Observation

#### Definition

```text
An observation is a bounded act and resulting record of accessing state through
an attributable method, source, time, environment, and coverage.
```

An observation should make visible, where material:

```text
what was observed
how it was observed
source
when
where or in which environment
coverage
limitations
```

#### Observation is not

```text
interpretation
inference
fact by default
decision
authority
complete truth
```

An observation can be incorrect, stale, partial, noisy, or misunderstood.

---

### T5 — Source

#### Definition

```text
A source is the attributable origin from which an observation, statement,
record, decision, claim, or evidence item is obtained.
```

Examples:

```text
direct owner instruction
approved system of record
repository content
runtime output
contract artifact
policy document
review record
metric system
agent-authored summary
```

#### Source is not

```text
authority by default
truth by default
current by default
complete coverage by default
```

Source type, authority, recency, scope, and reliability are separate properties.

---

### T6 — Unknown

#### Definition

```text
Unknown is the explicit status of a relevant proposition whose truth, value,
state, source, authority, or result cannot be established with currently
available evidence and capacity.
```

#### Unknown is not

```text
false
absent
approved
rejected
safe
unsafe
permission to guess
```

Unknown is valid engineering state. It may trigger evidence gathering, scope narrowing, routing, a reversible experiment, or a blocked status.

---

## 4. Representation And Reasoning Terms

### T7 — Model

#### Definition

```text
A model is a structured representation of state, relationships, behavior,
causality, constraints, or expected outcomes used for interpretation,
communication, prediction, planning, or execution.
```

Examples:

```text
domain model
architecture model
repository summary
user-intent interpretation
implementation plan
risk model
market hypothesis
AI model output
```

#### Model is not

```text
the state it represents
fact by default
authority by default
execution by default
proof of correctness
```

A model can be useful, verified, and action-guiding while remaining a model.

---

### T8 — Interpretation

#### Definition

```text
Interpretation is meaning assigned to an observation, record, statement,
artifact, or other available information.
```

Examples:

```text
interpreting an error log as a dependency failure
interpreting a user statement as a scope constraint
interpreting a metric change as a possible response to a campaign
```

#### Interpretation is not

```text
the observation itself
fact by default
inference necessarily
authoritative decision
```

Interpretations should expose relevant assumptions and alternative readings when material.

---

### T9 — Inference

#### Definition

```text
An inference is a proposition derived from observations, evidence, or other
propositions through an identifiable reasoning step.
```

#### Inference is not

```text
direct observation
fact by default
assumption by default
decision
authority
```

An inference may become well-supported, but its derivation and scope remain relevant.

Example:

```text
Observation: the build fails after a dependency upgrade.
Inference: the dependency upgrade may have introduced an incompatible type change.
```

---

### T10 — Assumption

#### Definition

```text
An assumption is a proposition temporarily accepted for reasoning or action
without sufficient verification for the current claim scope.
```

Assumptions may be necessary when complete information is unavailable.

They must remain visible when they materially affect:

```text
scope
risk
authority
architecture
implementation
validation
completion
```

#### Assumption is not

```text
fact
decision
approval
evidence
permission
```

A justified assumption may support a reversible test. It must not be silently executed as verified fact.

---

### T11 — Fact

#### Definition

```text
A fact is a proposition treated as established within a stated scope because
available attributable evidence satisfies the relevant verification standard.
```

A fact is always bounded by relevant dimensions such as:

```text
time
version
environment
coverage
method
claim scope
```

#### Fact is not

```text
raw observation by default
universal truth beyond scope
immutable forever
authority to act
a decision or approval
```

New evidence may narrow, supersede, or invalidate a previously established fact without making the earlier classification dishonest if its original scope and evidence were stated correctly.

---

### T12 — Claim

#### Definition

```text
A claim is an explicit proposition asserted about state, behavior, meaning,
quality, causality, authority, completion, or result.
```

Examples:

```text
the branch exists
the test passes
the implementation conforms
the design is usable
the feature is complete
the owner approved the change
the campaign caused the metric increase
```

#### Claim is not

```text
evidence
fact by default
decision by default
approval by default
```

Every material claim has an evidence scope, even when the evidence is missing.

---

## 5. Evidence And Quality Terms

### T13 — Evidence

#### Definition

```text
Evidence is attributable information produced or preserved through a method that
can support, weaken, distinguish, or challenge a claim within a bounded scope.
```

Evidence should be evaluated by:

```text
source
method
scope
coverage
time and environment
relevance
reliability
reproducibility where applicable
claim supported
limitations
```

#### Evidence is not

```text
a claim by itself
complete truth by default
authority by default
approval by default
all required evidence by default
```

#### Evidence qualification

Common qualified evidence types include:

```text
source evidence
implementation evidence
static conformance evidence
behavioral evaluation evidence
runtime evidence
security evidence
accessibility evidence
product acceptance evidence
business metric evidence
approval evidence
learning and regression evidence
```

Each evidence type supports only claims appropriate to its method and coverage.

---

### T14 — Verification

#### Definition

```text
Verification is the process of determining whether a specified claim,
requirement, contract, property, or result is supported by appropriate evidence.
```

Verification asks:

```text
Does the available evidence support this specified claim within its scope?
```

Examples:

```text
verifying that tests pass
verifying that a contract path resolves
verifying that a required field exists
verifying that a user statement authorizes the named action
```

#### Verification is not

```text
complete product validation by default
evaluation of every quality dimension
approval by default
proof beyond the verified scope
```

---

### T15 — Validation

#### Definition

```text
Validation is the process of determining whether a system, artifact, decision,
or behavior is fit for its intended use, need, context, and acceptance scope.
```

Validation asks:

```text
Does this work appropriately for the intended purpose and context?
```

Examples:

```text
validating that a design works across required interactions and viewports
validating that a feature solves the accepted user problem
validating that an operational procedure is usable during an incident
```

#### Validation is not

```text
identical to verification
approval by default
universal product success
one passing technical check
```

Verification and validation may overlap, but neither automatically contains the other.

---

### T16 — Evaluation

#### Definition

```text
Evaluation is a systematic assessment against declared criteria that produces
findings, measurements, evidence, and optionally a verdict.
```

Evaluation may include:

```text
verification
validation
comparison
quality scoring
risk assessment
behavioral testing
human review
product measurement
```

#### Evaluation is not

```text
authority by default
approval by default
runtime enforcement by default
complete evidence by default
```

---

### T17 — Review

#### Definition

```text
Review is an examination of an artifact, decision, implementation, behavior, or
evidence set against declared criteria by a qualified actor or process.
```

A review may produce:

```text
findings
questions
risks
change requests
recommendation
verdict
```

#### Review is not

```text
approval unless the reviewer has the required authority and the process assigns it
implementation evidence by itself
execution
final truth
```

---

### T18 — Conformance

#### Definition

```text
Conformance is the degree to which an implementation, adapter, artifact, or
behavior satisfies the applicable requirements of a contract or standard.
```

Conformance may be assessed at different evidence layers:

```text
path resolution
version compatibility
schema or structural validity
static declaration coverage
boundary consistency
behavioral execution
runtime integration
product acceptance
```

#### Conformance is not

```text
one boolean proven by any single layer
contract presence
metadata presence
runtime or product quality by default
```

A conformance claim must name the evaluated layer.

---

### T19 — Coherence

#### Definition

```text
Coherence is the degree to which material intent, requirements, definitions,
decisions, contracts, architecture, implementation, behavior, evidence, and
approval state can coexist without unresolved contradiction inside a stated scope.
```

#### Coherence is not

```text
perfect uniformity
absence of all disagreement
global completeness
one preferred style
immutability
```

Known limitations or differences may remain coherent when their scope, rationale, ownership, and acceptance are explicit.

---

### T20 — Completion

#### Definition

```text
Completion is a claim that the accepted objective and in-scope criteria have been
satisfied with appropriate evidence, required review or approval, and disclosed
limitations.
```

#### Completion is not

```text
implementation activity alone
one green check
one review verdict
absence of visible errors
confidence
partial completion reported as full completion
```

When completion cannot be supported, the system should use an honest narrower status such as partial, blocked, not verified, or accepted with limitation.

Exact status taxonomies belong to domain and contract work.

---

## 6. Action, Decision, And Authority Terms

### T21 — Capability

#### Minimum philosophy definition

```text
Capability is the ability of an actor, agent, tool, adapter, or system to perform
a category of action or produce a category of result.
```

This is the minimum meaning required by the philosophy.

Issue `#6` owns the complete Native AI Engineering capability taxonomy and may define domain-specific capability objects and relationships without contradicting this boundary.

#### Capability is not

```text
permission
authority
approval
quality proof
successful execution
```

---

### T22 — Permission

#### Definition

```text
Permission is a technical, policy, or access-control allowance for an actor or
system to attempt a named operation within a bounded scope.
```

Examples:

```text
repository write permission
filesystem access
API token scope
runtime tool allowance
delegated low-risk action policy
```

#### Permission is not

```text
capability by itself
authority by itself
approval by itself
proof that the action is safe or correct
```

Permission may be necessary without being sufficient.

---

### T23 — Authority

#### Definition

```text
Authority is the recognized right within a named decision domain to bind,
approve, reject, delegate, supersede, or constrain an action, decision, claim,
risk acceptance, or canonical meaning.
```

Authority should identify:

```text
decision domain
holder or delegated role
scope
conditions
supersession rights
policy constraints
```

#### Authority is not

```text
capability
permission
access
ownership label alone
recency
confidence
silence or absence of objection
```

Authority can be delegated, but delegation must be attributable and scoped.

---

### T24 — Decision

#### Definition

```text
A decision is a recorded selection, rejection, commitment, or constraint among
alternatives that is intended to govern action within a stated scope.
```

A decision record may include:

```text
subject
choice or constraint
scope
source
authority
rationale
evidence
conditions
supersedes
conflicts
status
```

#### Decision is not

```text
fact
observation
evidence
authority by itself
approval by default
```

A decision may exist but remain non-authoritative, conflicted, superseded, or pending approval.

---

### T25 — Effective Decision

#### Definition

```text
An effective decision is a decision whose source and required authority are
verified, whose scope covers the proposed action, whose required approvals are
satisfied, and whose material conflicts or supersession state are resolved.
```

#### Effective decision is not

```text
the newest decision by default
the most convenient interpretation
an agent-authored summary without authority
a decision that bypasses applicable policy
```

---

### T26 — Approval

#### Definition

```text
Approval is an authority-bearing positive decision that permits a named action,
claim, transition, release, risk acceptance, or canonical change within stated
scope and conditions.
```

Approval should be attributable to the authority required by the decision domain.

#### Approval is not

```text
review verdict by default
recommendation
lack of objection
silence
technical permission
successful validation
```

A review can include approval only when the process and reviewer authority explicitly establish it.

---

### T27 — Scope

#### Definition

```text
Scope is the explicit boundary of the subject, actions, claims, environments,
time, consumers, risks, and responsibilities to which a statement, decision,
evidence item, task, contract, or approval applies.
```

#### Scope is not

```text
all adjacent work
all implied future work
all technically possible actions
all consumers or environments by default
```

A direct instruction or approval authorizes only the scope it actually covers.

---

### T28 — Coverage

#### Definition

```text
Coverage is the portion of a stated scope that was actually observed, exercised,
evaluated, reviewed, or supported by evidence.
```

#### Coverage is not

```text
the full declared scope by default
quality by itself
completion by itself
```

Examples:

```text
one viewport is partial responsive coverage
unit tests are partial behavior coverage
one repository adapter is partial cross-adapter coverage
one user cohort is partial market coverage
```

---

### T29 — Capacity

#### Definition

```text
Capacity is the currently available combination of context, capability, tools,
permission, authority, risk controls, time and scope budget, validation path,
review coverage, reversibility, and recovery support required for a bounded action.
```

Capacity is contextual and task-specific.

#### Capacity is not

```text
capability alone
tool access alone
permission alone
actor confidence
a permanent identity or rating
```

When capacity is insufficient for the requested scope, valid responses include narrowing, pausing, routing, requesting authority, choosing a reversible test, marking partial, or stopping.

---

## 7. Execution And Learning Terms

### T30 — Feedback

#### Definition

```text
Feedback is attributable information produced by execution, observation,
evaluation, review, use, measurement, or consequence that can support revision
of a model, decision, behavior, implementation, or other affected layer.
```

#### Feedback is not

```text
automatically correct
automatically authoritative
final truth
an instruction to change core directly
learning by itself
```

Material feedback must be processed through acceptance, rejection with rationale, narrowing, revision, retesting, escalation, or learning-candidate creation.

---

### T31 — Update

#### Definition

```text
An update is a traceable change to a working model, context, plan, decision,
implementation, knowledge artifact, skill, workflow, contract proposal, domain
understanding, or canonical artifact in response to accepted evidence, feedback,
or authority.
```

#### Update is not

```text
uncontrolled mutation
silent semantic drift
proof that the new state is correct
core evolution by default
```

The target layer and compatibility impact must match the update scope.

---

### T32 — Learning

#### Definition

```text
Learning is an evaluated change in future interpretation, decision, or repeatable
behavior derived from feedback and evidence.
```

Learning may remain:

```text
local to one task
local to one product
procedural within a skill
shared across workflows
candidate input to contract or core evolution
```

#### Learning is not

```text
feedback collection alone
memory alone
one anecdote
one successful result
automatic promotion to a shared layer
```

---

### T33 — Learning Candidate

#### Definition

```text
A learning candidate is a traceable proposal that a verified lesson may be
reusable beyond its source case and should be evaluated for promotion to the
smallest correct shared layer.
```

A learning candidate should preserve:

```text
source case
observed failure
verified change
before and after evidence
reusable reason
counterexamples
candidate target layer
```

#### Learning candidate is not

```text
accepted shared knowledge
canonical rule
contract change
core evolution
```

---

### T34 — Embodiment

#### Definition

```text
Embodiment is the state in which a principle, rule, contract, skill, workflow,
or other declared expectation changes repeatable executable behavior and that
behavior can produce evidence appropriate to the claim.
```

#### Embodiment is not

```text
documentation presence
contract presence
skill installation
metadata declaration
one successful execution
perfect execution in every case
```

Embodiment claims require evidence from the relevant execution surface.

---

### T35 — Stability

#### Definition

```text
Stability is the condition in which an artifact or agreement has explicit
ownership, known compatibility expectations, controlled change behavior,
validation requirements, and reliable consumer expectations.
```

#### Stability is not

```text
immutability
infallibility
absence of feedback
permanent freeze
silent resistance to change
```

Stable artifacts may evolve through governed review and migration.

---

### T36 — Core Evolution

#### Definition

```text
Core evolution is an accepted, governed change to a canonical Native AI
Engineering definition, law, principle, guardrail, domain boundary, port,
contract, or other core-owned agreement.
```

Core evolution requires, where applicable:

```text
verified source learning
reusable invariant reason
counterexample and transferability review
correct target-layer decision
compatibility analysis
consumer impact review
required authority
validation and migration evidence
explicit acceptance or supersession
```

#### Core evolution is not

```text
local implementation change
product policy change
adapter translation
one field test
one agent recommendation
silent contract drift
```

Concrete layers may propose core evolution. They may not declare it accepted on behalf of core authority.

---

## 8. Source-Of-Truth And Memory Terms

### T37 — Source Of Truth

#### Definition

```text
A source of truth is an artifact, record, or system designated by the relevant
authority as the current primary reference for a named class of definition,
decision, policy, state, or knowledge.
```

#### Source of truth is not

```text
infallible
complete for all concerns
eternally current
truth outside its designated scope
```

A source of truth can be superseded through explicit authority and governed change.

---

### T38 — Knowledge

#### Minimum philosophy definition

```text
Knowledge is explicit, reviewable information accepted for use within a stated
scope and maintained in an attributable source-of-truth artifact or system.
```

#### Knowledge is not

```text
memory alone
agent confidence
unattributed summary
immutable truth
```

The complete Native AI Engineering knowledge model may be refined by issue `#6` and later contract work.

---

### T39 — Memory

#### Definition

```text
Memory is retained context, history, preference, pattern, or prior outcome used
to support retrieval and reasoning across time.
```

#### Memory is not

```text
authoritative knowledge by default
current policy by default
verified present state
approval
```

Memory should point to source-of-truth artifacts when material and must not override a current authoritative source without verified supersession.

---

## 9. Relationship Maps

These maps organize the terms. They do not create alternative definitions.

### 9.1 State and reasoning map

```text
STATE
→ observable through an observation path
→ available to an actor through a source
→ captured as an OBSERVATION
→ assigned meaning through INTERPRETATION
→ extended through INFERENCE
→ may rely on explicit ASSUMPTIONS
→ expressed as a CLAIM
→ supported or challenged by EVIDENCE
→ may become an established FACT within scope
→ or remain UNKNOWN / NOT_VERIFIED
```

Required distinctions:

```text
state ≠ observation
observation ≠ interpretation
interpretation ≠ inference
inference ≠ fact
assumption ≠ fact
claim ≠ evidence
fact ≠ authority
```

### 9.2 Decision and authority map

```text
CLAIM + EVIDENCE + ALTERNATIVES
→ DECISION

DECISION + REQUIRED AUTHORITY + RESOLVED SCOPE/CONFLICTS
→ EFFECTIVE DECISION

EFFECTIVE POSITIVE DECISION AUTHORIZING A NAMED ACTION
→ APPROVAL
```

Required distinctions:

```text
capability ≠ permission
permission ≠ authority
decision ≠ authority
review ≠ approval
verification ≠ approval
```

### 9.3 Evidence and quality map

```text
CLAIM
→ VERIFICATION against specified evidence requirements
→ VALIDATION against intended use and context
→ broader EVALUATION against declared criteria
→ REVIEW findings or verdict where required
→ APPROVAL only from required authority
```

These processes may overlap but do not silently prove one another.

### 9.4 Execution capacity map

```text
context
+ capability
+ tools
+ permission
+ authority
+ risk controls
+ time and scope budget
+ validation path
+ review coverage
+ reversibility and recovery
= bounded EXECUTION CAPACITY
```

Missing one material dimension may require narrowing, routing, blocking, or status downgrade.

### 9.5 Feedback and evolution map

```text
EXECUTION OR USE
→ EVIDENCE
→ FEEDBACK
→ UPDATE
→ LEARNING
→ LEARNING CANDIDATE
→ generalization and compatibility review
→ accepted target-layer change
→ CORE EVOLUTION only when core authority accepts it
```

### 9.6 Embodiment map

```text
DECLARED PRINCIPLE / RULE / CONTRACT / SKILL
+ repeatable executable behavior
+ appropriate evidence
= EMBODIED CANDIDATE

repeated evaluation and regression protection
→ stronger embodiment confidence
```

---

## 10. Common False Equivalences

The canonical vocabulary prohibits these collapses:

```text
state                       ≠ summary of state
observable state            ≠ currently available state
available state             ≠ complete state
observation                 ≠ fact by default
interpretation              ≠ observation
inference                   ≠ fact
assumption                  ≠ decision
claim                       ≠ evidence
evidence                    ≠ approval
fact                        ≠ authority
capability                  ≠ permission
permission                  ≠ authority
decision                    ≠ effective decision
review verdict              ≠ approval authority
verification                ≠ validation
validation                  ≠ complete product success
evaluation                  ≠ approval
contract presence           ≠ conformance
static conformance          ≠ executable behavior
skill installation          ≠ embodiment
feedback                    ≠ final truth
learning                    ≠ automatic shared promotion
local update                ≠ core evolution
stability                   ≠ immutability
memory                      ≠ source-of-truth knowledge
completion                  ≠ activity performed
```

---

## 11. Contextual Specialization Rules

A domain, contract, skill, workflow, adapter, runtime, or product may introduce a specialized term when:

```text
the base term is insufficiently specific;
the specialization inherits the base meaning;
the added boundary is explicit;
the local owner is named;
the specialization does not redefine upstream semantics.
```

Valid examples:

```text
runtime evidence is evidence from an execution environment;
product approval is approval inside a product decision domain;
repository state is state of a repository at a named ref and time;
behavioral conformance is conformance evaluated through executable cases;
security validation is validation against intended security requirements and context.
```

Invalid examples:

```text
a product calling generated copy “evidence” without an evidence method;
a runtime calling tool access “authority”;
a skill calling installation “embodiment”;
a repository calling a passing build “product validation”;
an adapter redefining a canonical term because its provider uses different wording.
```

---

## 12. Term Status And Compatibility

Current status:

```text
Atomic term authority structure: ESTABLISHED FOR CANDIDATE REVIEW
Required issue #13 terms: DEFINED
Supporting distinction terms: DEFINED
Observable vs available state: RESOLVED
Verification vs validation vs evaluation: RESOLVED FOR CANDIDATE REVIEW
Capability vs permission vs authority: RESOLVED FOR CANDIDATE REVIEW
Decision vs effective decision vs approval: RESOLVED FOR CANDIDATE REVIEW
Feedback vs learning vs core evolution: RESOLVED FOR CANDIDATE REVIEW
Relationship to docs/glossary.md: MIGRATION REQUIRED
Machine-readable contract impact: NOT YET APPLIED
Domain model consumption readiness: PARTIAL, PENDING ACCEPTANCE
```

These definitions are candidates until issue `#13` acceptance.

They constrain later domain work by preserving required distinctions, but issue `#6` still owns the complete canonical domain objects, bounded contexts, aggregates, lifecycle taxonomy, and capability taxonomy.

---

## 13. Validation Gates Before Acceptance

The vocabulary must not be marked accepted until:

- [ ] every required issue `#13` term has one atomic definition;
- [ ] definitions do not silently collapse observation, interpretation, inference, assumption, fact, claim, evidence, decision, and authority;
- [ ] observable state and available state remain distinct;
- [ ] capability, permission, authority, decision, and approval remain distinct;
- [ ] verification, validation, evaluation, review, and approval remain distinct;
- [ ] evidence types inherit the base evidence definition;
- [ ] domain and contract specializations can inherit the terms without contradiction;
- [ ] `docs/glossary.md` is reconciled as navigation rather than parallel authority;
- [ ] current contracts are reviewed for conflicting definitions or status semantics;
- [ ] issue `#6` confirms that the vocabulary is sufficient for domain modeling;
- [ ] cross-document links and terminology are reviewed;
- [ ] issue `#13` records explicit acceptance or requested revision.

---

## 14. Current Verdict

```text
Canonical term authority model: ESTABLISHED FOR CANDIDATE REVIEW
Atomic philosophy terms defined: 39
Required epistemic distinctions: PRESERVED
Source-role boundary: DEFINED
Contextual specialization rule: DEFINED
False-equivalence review: INITIAL PASS
Glossary reconciliation: NOT YET APPLIED
Contract terminology review: NOT YET COMPLETE
Term acceptance status: CANDIDATE
Ready for epistemic-loop formalization: YES
Ready for philosophy traceability matrix: PARTIAL
Ready for domain model consumption: NOT YET, PENDING ACCEPTANCE
```

The next philosophy slice should formalize the cross-domain epistemic loop using these terms, define phase inputs and outputs without duplicating delivery workflows, and test the loop against analysis, planning, design, engineering, marketing, runtime operations, and skill refinement.