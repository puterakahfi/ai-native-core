# Native AI Engineering Epistemic Loop

Status: Candidate foundation mechanism

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Derived laws: [`laws.md`](laws.md)

Principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

Canonical term authority: [`term-authority.md`](term-authority.md)

Development Loop mechanism: [`../development-loop.md`](../development-loop.md)

Runtime contract: [`../../contracts/runtime/development-loop.contract.yaml`](../../contracts/runtime/development-loop.contract.yaml)

This document defines the candidate cross-domain reasoning loop for Native AI Engineering.

It governs how an actor distinguishes available state from its model, assesses execution capacity, chooses a bounded response, reads evidence, and updates the correct layer.

It does not replace delivery workflows, specialist skills, runtime orchestration, approval policy, or the canonical Development Loop.

---

## 1. Purpose

Native AI Engineering work is performed across changing state, incomplete context, multiple authorities, executable systems, and evidence with different scopes.

A reusable reasoning mechanism is required so that analysis, planning, design, engineering, marketing, operations, governance, and skill refinement do not each invent a different epistemic discipline.

The loop must preserve these distinctions:

```text
state ≠ observation
observation ≠ interpretation
interpretation ≠ inference
inference ≠ fact
assumption ≠ decision
decision ≠ authority
claim ≠ evidence
capability ≠ permission
permission ≠ authority
plan ≠ execution
review ≠ approval
verification ≠ complete validation
feedback ≠ final truth
local learning ≠ core evolution
```

The candidate loop is:

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ READ EVIDENCE
→ UPDATE
```

Its purpose is to produce better engineering decisions without turning philosophy into a rigid delivery process.

---

## 2. Mechanism Classification

The epistemic loop is a **mechanism**.

```text
Law        explains the invariant.
Principle  guides selection.
Guardrail  defines the mandatory boundary.
Mechanism  organizes reasoning.
Gate       controls a transition or claim.
Policy     defines bounded authority-selected behavior.
```

The loop:

- derives from the candidate axioms and laws;
- uses canonical philosophy terms;
- operationalizes principles and guardrails;
- may be embedded inside workflows and skills;
- may produce inputs to gates and policies;
- does not own product-specific execution details;
- does not create authority merely by being followed.

Following the loop is not proof that the result is correct. The result still requires evidence appropriate to its claim.

---

## 3. Relationship To The Development Loop

The canonical Development Loop is:

```text
Explore → Plan → Implement → Verify → Review → Document → Deliver
```

The Development Loop governs execution lifecycle phases, gates, outputs, and transitions.

The Epistemic Loop governs reasoning about state, models, capacity, evidence, and revision inside those phases.

```text
Development Loop
owns:
- execution lifecycle
- phase transitions
- implementation
- verification execution
- review lifecycle
- documentation
- delivery

Epistemic Loop
owns:
- state attribution
- model decomposition
- capacity reasoning
- evidence-scope reasoning
- response selection
- feedback interpretation
- target-layer update reasoning
```

### 3.1 Typical mapping

| Development Loop phase | Epistemic-loop use |
|---|---|
| Explore | OBSERVE, ASSESS CAPACITY, DECOMPOSE THE MODEL |
| Plan | DECOMPOSE THE MODEL, SELECT A TESTABLE RESPONSE |
| Implement | Host mechanism executes the selected response; new findings may re-enter OBSERVE |
| Verify | Produces evidence for READ EVIDENCE |
| Review | Produces findings and verdict evidence for READ EVIDENCE |
| Document | Records UPDATE decisions, limitations, evidence, and learning |
| Deliver | Uses capacity, authority, completion, and evidence checks before delivery claims |

### 3.2 No duplicated execution phase

The Epistemic Loop intentionally does not contain an `EXECUTE` phase.

```text
SELECT A TESTABLE RESPONSE
≠ execute the response
≠ authorize the response
≠ prove the response succeeded
```

Execution belongs to the host workflow, skill, tool operation, runtime mechanism, or human process.

The host mechanism must preserve:

```text
permission
authority
applicable policy
risk controls
required gates
rollback or recovery capacity
execution evidence
```

The relationship is:

```text
SELECT A TESTABLE RESPONSE
→ host mechanism performs or routes the bounded response
→ execution produces state and evidence
→ READ EVIDENCE
```

This boundary prevents the epistemic loop from becoming a shadow workflow or treating a plan as execution.

---

## 4. Loop Inputs

The loop may begin when an actor has a material question, task, claim, contradiction, feedback item, or proposed action.

Candidate inputs include:

```text
explicit user instruction
active issue and acceptance criteria
repository or product state
runtime behavior
current implementation
existing model or plan
review finding
verification output
approval requirement
product behavior
business metric
incident or regression
learning candidate
proposed canonical change
```

Each loop run should identify:

```text
subject
objective or question
initial scope
available sources
known authority context
risk context
host workflow or mechanism
```

When these are unavailable, the loop may still perform bounded discovery, but must not fabricate them.

---

## 5. Loop Outputs

A complete loop run should produce enough structure to support a bounded next action or an honest stop condition.

Candidate outputs are:

```text
observation set
source and coverage record
unknown and not-verified record
capacity assessment
epistemic decomposition
selected response or valid non-action
expected evidence and validation path
evidence reading
revision decision
updated target layer
completion or limitation status
learning candidate when justified
```

These are conceptual outputs, not a mandatory universal serialization format.

Issue `#8` owns future machine-readable schema decisions.

---

## 6. Phase 1 — OBSERVE

### Purpose

Establish the available, attributable state relevant to the current objective before materially interpreting, planning, or changing the system.

### Primary question

```text
What is currently available and directly attributable within the relevant scope?
```

### Required inputs

```text
subject or question
initial scope
available source paths
observation time or version where material
```

### Activities

```text
inspect relevant source-of-truth artifacts
read repository or product state
collect runtime or tool state where permitted
identify active issue and acceptance criteria
record direct user or owner statements
capture existing evidence
identify missing access and coverage
```

### Required distinctions

```text
state vs observation
available state vs merely observable state
direct observation vs remembered summary
current source vs superseded source
source existence vs source authority
```

### Candidate output

An **Observation Set** containing:

```text
observed subject
source reference
observation or record
time, version, ref, or environment where material
coverage
source status
unknowns
unavailable state
conflicts discovered
```

### Exit condition

```text
The available state baseline is attributable, scoped, and honest about missing coverage.
```

### Valid outcomes

```text
CONTINUE
REQUEST SOURCE ACCESS
REQUEST EVIDENCE
MARK UNKNOWN
MARK NOT_VERIFIED
NARROW SCOPE
BLOCK MATERIAL CLAIM
```

### Guardrails

```text
G1 No Fabricated State Or Evidence
G2 No Model-As-Fact Collapse
G3 No Claim Beyond Evidence Scope
G13 Memory Must Not Override Current Source Of Truth
```

### Invalid shortcuts

```text
starting from remembered repository structure without checking
using an agent summary as owner instruction
claiming test status without output
using a screenshot as complete product state
assuming newest source is authoritative without authority review
```

---

## 7. Phase 2 — ASSESS CAPACITY

### Purpose

Determine whether the currently available combination of context, capability, tools, permission, authority, controls, evidence path, review, and recovery is sufficient for the proposed scope.

### Primary question

```text
Is there enough bounded capacity to perform and validate this scope responsibly?
```

### Capacity dimensions

```text
context availability
source coverage
domain and technical capability
tool availability
permission
authority and approval
risk controls
reversibility
recovery or rollback capacity
time and scope budget
validation path
review coverage
consumer-impact visibility
```

### Required distinctions

```text
capability vs permission
permission vs authority
technical possibility vs policy allowance
confidence vs capacity
partial capacity vs full completion capacity
```

### Candidate output

A **Capacity Assessment** containing:

```text
requested scope
available capacity dimensions
missing capacity dimensions
risk and reversibility classification
required authority or approval
available evidence path
review and recovery coverage
recommended response
```

### Exit condition

```text
Capacity is sufficient for the selected scope, or a valid narrowing, routing,
blocking, or stop response has been identified.
```

### Valid responses

```text
PROCEED
NARROW
ROUTE
REQUEST AUTHORITY
REQUEST APPROVAL
REQUEST TOOL OR SOURCE ACCESS
CHOOSE A REVERSIBLE TEST
MARK PARTIAL
MARK BLOCKED
STOP
```

### Guardrails

```text
G4 Capability Is Not Authority
G5 No Silent Scope Expansion
G7 No Undeclared Gate Bypass
G14 No Destructive Or High-Risk Action Without Required Controls
```

### Invalid shortcuts

```text
tool access treated as authorization
write permission treated as approved scope
production action without rollback capacity
full UX claim without required viewport or interaction coverage
implementation claim without repository write evidence
```

### Capacity is contextual

Capacity is not a permanent rating of an agent, person, tool, or team.

```text
insufficient for full implementation
may still be sufficient for discovery

insufficient for production rollout
may still be sufficient for a reversible experiment

insufficient for approval
may still be sufficient for a recommendation
```

---

## 8. Phase 3 — DECOMPOSE THE MODEL

### Purpose

Separate representations and reasoning states so that observation, interpretation, inference, assumption, decision, authority, claim, and unknown state do not collapse into one confident narrative.

### Primary question

```text
What is observed, interpreted, inferred, assumed, decided, approved,
unknown, conflicted, superseded, or not verified?
```

### Model components to inspect

```text
current interpretation
problem framing
requirements model
architecture model
plan
risk model
product hypothesis
causal hypothesis
completion model
learning hypothesis
```

### Candidate epistemic categories

```text
OBSERVED
INTERPRETED
INFERRED
ASSUMED
CLAIMED
ESTABLISHED_WITHIN_SCOPE
DECIDED
EFFECTIVE_DECISION
APPROVED
UNKNOWN
NOT_VERIFIED
CONFLICTED
SUPERSEDED
OUT_OF_SCOPE
```

These are conceptual categories. Final machine statuses belong to domain and contract work.

### Candidate output

An **Epistemic Decomposition** containing:

```text
material proposition
classification
source or rationale
scope
verification status
authority status
conflicts
assumptions
unknowns
impact if wrong
```

### Exit condition

```text
Material assumptions, inferences, claims, decisions, authority, conflicts,
and unknowns affecting the next response are explicit.
```

### Guardrails

```text
G2 No Model-As-Fact Collapse
G3 No Claim Beyond Evidence Scope
G6 No Silent Conflict Resolution
G13 Memory Must Not Override Current Source Of Truth
```

### Invalid shortcuts

```text
issue interpretation treated as issue text
plan treated as execution
review recommendation treated as approval
implementation existence treated as intended scope
one metric movement treated as causal proof
agent confidence used to resolve authoritative conflict
```

### Why decomposition is not indecision

Decomposition does not prohibit action under uncertainty.

It enables action to be selected with the correct status:

```text
verified action
bounded assumption-based experiment
recommendation
request for authority
partial implementation
blocked state
```

---

## 9. Phase 4 — SELECT A TESTABLE RESPONSE

### Purpose

Choose the smallest coherent response that can advance the accepted objective, stay inside capacity and authority, and produce evidence capable of distinguishing relevant alternatives.

### Primary question

```text
What is the smallest coherent and authorized response that can produce useful evidence?
```

### Candidate response types

```text
inspect further
ask for or retrieve evidence
clarify authority
create a plan
apply a bounded implementation change
run a verification check
perform a review
execute a reversible experiment
route to a qualified actor
narrow the claim or scope
record a learning candidate
propose a target-layer change
stop or remain blocked
```

### Selection factors

```text
accepted objective
scope
capacity
risk
reversibility
authority
expected evidence
blast radius
consumer impact
existing correct work
correct ownership layer
cost of being wrong
```

### Required response specification

For a material response, identify:

```text
response
intended objective
scope and exclusions
host mechanism or workflow
required permission and authority
applicable policy and guardrails
expected evidence
verification or validation path
review or approval need
rollback, fallback, or stop condition
```

### Candidate output

A **Testable Response Selection**.

### Exit condition

```text
The response is bounded, coherent, inside available capacity and authority,
and has an evidence path proportionate to the intended claim.
```

### Principles

```text
P2 Smallest Coherent Change
P3 Evidence-Proportional Claims
P5 Reversible Progress Under Uncertainty
P6 Correct-Layer Change
P7 Preserve Useful Existing Work
P9 Review Proportional To Risk And Authority
P11 Explicit Boundaries Over Implicit Expectations
```

### Guardrails

```text
G4 Capability Is Not Authority
G5 No Silent Scope Expansion
G7 No Undeclared Gate Bypass
G11 No Unverified Promotion To Shared Layers
G14 No Destructive Or High-Risk Action Without Required Controls
```

### Invalid shortcuts

```text
choosing a response only because a tool is available
selecting a provider before defining the capability
performing adjacent refactors without authority
choosing a non-reversible action when a reversible test is sufficient
promoting a product-specific fix directly into core
```

### Selection is not execution

The selected response remains a model of intended action until the host mechanism performs it and produces attributable evidence.

---

## 10. Execution Boundary

After selection, the host mechanism owns execution.

Examples:

```text
Development Loop Implement phase
specialist skill procedure
workflow phase
runtime tool operation
CI or deployment mechanism
human review or approval process
product experiment
```

The host mechanism must return or preserve:

```text
actual action performed
actor or execution surface
scope
resulting state
evidence produced
failures
side effects
policy and gate outcomes
```

When execution reveals unexpected state, the loop may return immediately to `OBSERVE` before continuing.

```text
SELECT
→ EXECUTE THROUGH HOST MECHANISM
→ unexpected state discovered
→ OBSERVE
```

This is not failure of the loop. It is correct feedback behavior.

---

## 11. Phase 5 — READ EVIDENCE

### Purpose

Determine what the resulting evidence supports, weakens, contradicts, or leaves unresolved without inflating its meaning.

### Primary questions

```text
What does the evidence show?
What claim can it support?
What claim can it not support?
What relevant contradiction remains?
```

### Evidence dimensions

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
contradictory evidence
```

### Evidence surfaces

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
review evidence
approval evidence
learning and regression evidence
```

### Candidate output

An **Evidence Reading** containing:

```text
evidence item
method and source
scope and coverage
supported claims
unsupported claims
contradictions
limitations
verification or validation result
review or approval status where applicable
required next response
```

### Exit condition

```text
Evidence meaning is bounded to its source and coverage, and material
contradictions or missing evidence are explicit.
```

### Valid readings

```text
SUPPORTS CLAIM WITHIN SCOPE
WEAKENS CLAIM
CONTRADICTS CLAIM
INSUFFICIENT
NOT RELEVANT
NOT AUTHORITATIVE FOR DECISION
REQUIRES BROADER VALIDATION
REQUIRES REVIEW
REQUIRES APPROVAL
```

These are conceptual outcomes, not a final contract enum.

### Guardrails

```text
G1 No Fabricated State Or Evidence
G3 No Claim Beyond Evidence Scope
G8 No False Completion
G9 Declaration Is Not Embodiment
G10 Feedback Must Not Be Silenced By Confidence
```

### Invalid shortcuts

```text
build pass reported as full product validity
static declaration reported as runtime conformance
review verdict reported as approval
one viewport reported as responsive validation
metric correlation reported as causation
successful local case reported as universal rule
```

---

## 12. Phase 6 — UPDATE

### Purpose

Revise the correct model, decision, implementation, knowledge, skill, workflow, contract proposal, or canonical layer according to evidence, feedback, authority, and compatibility obligations.

### Primary question

```text
What should continue, change, stop, narrow, route, be retested,
or become a governed learning or evolution proposal?
```

### Candidate update targets

```text
working context
interpretation
assumption
claim
plan
task state
decision
implementation
product knowledge or policy
skill or reference
workflow
behavioral evaluation
contract proposal
canonical term proposal
domain-model proposal
philosophy evolution proposal
```

### Update decision factors

```text
evidence reading
feedback relevance
current authority
scope
consumer impact
compatibility
regression risk
correct ownership layer
required approval
remaining contradictions
```

### Candidate output

An **Update Decision** containing:

```text
accepted or rejected feedback
rationale
changed claim or model
selected target layer
required implementation or documentation update
retest or review requirement
compatibility impact
completion or limitation status
learning candidate or evolution proposal where justified
```

### Valid update responses

```text
CONTINUE
REVISE MODEL
REVISE PLAN
REVISE IMPLEMENTATION
NARROW CLAIM
RETEST
REQUEST MORE EVIDENCE
ROUTE FOR REVIEW
ROUTE FOR APPROVAL
REVERT
STOP
MARK PARTIAL
MARK BLOCKED
ACCEPT WITH LIMITATION
CREATE LEARNING CANDIDATE
PROPOSE TARGET-LAYER CHANGE
REJECT FEEDBACK WITH RATIONALE
```

### Guardrails

```text
G8 No False Completion
G10 Feedback Must Not Be Silenced By Confidence
G11 No Unverified Promotion To Shared Layers
G12 Concrete Layers Must Not Silently Redefine Canonical Layers
G15 No Silent Semantic Evolution
```

### Correct-layer rule

```text
local implementation evidence
may update local implementation directly;

reusable verified learning
may become a learning candidate;

a learning candidate
may propose a shared-layer change;

a canonical change
requires canonical authority, compatibility review, and acceptance.
```

### Exit condition

```text
The affected layer and claim status reflect the evidence, authority,
remaining uncertainty, and required follow-up honestly.
```

### Loop continuation

After UPDATE, the actor may:

```text
exit with a supported result
return to OBSERVE because state changed
return to ASSESS CAPACITY because scope or risk changed
return to DECOMPOSE because the model changed
return to SELECT because another response is required
```

---

## 13. Candidate Transition Model

```text
OBSERVE
  ├─ insufficient source → REQUEST EVIDENCE / MARK UNKNOWN / BLOCK
  └─ attributable baseline available
       ↓
ASSESS CAPACITY
  ├─ insufficient capacity → NARROW / ROUTE / BLOCK / STOP
  └─ sufficient for bounded scope
       ↓
DECOMPOSE THE MODEL
  ├─ unresolved authority conflict → ROUTE / BLOCK
  └─ material epistemic states explicit
       ↓
SELECT A TESTABLE RESPONSE
  ├─ no authorized response → STOP / REQUEST AUTHORITY
  └─ bounded response selected
       ↓
HOST MECHANISM EXECUTES OR ROUTES RESPONSE
       ↓
READ EVIDENCE
  ├─ insufficient or contradictory → REVISE / RETEST / NARROW
  └─ evidence supports bounded update
       ↓
UPDATE
  ├─ state changed materially → OBSERVE
  ├─ capacity changed → ASSESS CAPACITY
  ├─ model changed → DECOMPOSE THE MODEL
  ├─ another response required → SELECT
  └─ supported exit
```

The loop is iterative, but iteration must not become an excuse for endless analysis.

When capacity is sufficient and a bounded test is available, the mechanism should progress to selection and execution.

---

## 14. Invocation Rules

The epistemic loop should be invoked proportionately.

### Full explicit use

A more explicit loop record is appropriate for:

```text
architecture or contract changes
high-risk or destructive actions
production-impacting changes
security-sensitive work
conflicting authoritative decisions
cross-repository evolution
public product or marketing claims
core-term or domain-boundary changes
complex incidents
shared-skill promotion
```

### Lightweight use

A lightweight mental or documented pass may be sufficient for:

```text
low-risk local edits
simple read-only analysis
well-bounded verification
routine reversible operations
```

Lightweight use must still preserve mandatory guardrails.

### Re-entry triggers

Re-enter the loop when:

```text
new source evidence appears
user or owner corrects the model
verification fails
review requests changes
approval is denied or narrowed
runtime behavior contradicts static evidence
scope changes
risk or reversibility changes
an incident occurs
a regression appears
a local lesson is considered for shared promotion
```

---

## 15. Cross-Domain Stress Tests

### 15.1 Repository analysis

```text
OBSERVE
Read repository, branch, issue, files, contracts, and tests.

ASSESS CAPACITY
Confirm source access and inspection coverage.

DECOMPOSE
Separate observed structure from inferred architecture and remembered context.

SELECT
Produce the smallest useful analysis or retrieve missing sources.

READ
Check each repository claim against direct source evidence.

UPDATE
Correct the working model and mark missing state honestly.
```

Failure prevented:

```text
invented paths, branches, implementation status, or test results
```

### 15.2 Planning

```text
OBSERVE
Read objective, acceptance criteria, constraints, and current implementation.

ASSESS CAPACITY
Confirm context, authority, and validation path.

DECOMPOSE
Separate requirement, assumption, dependency, decision, and unresolved question.

SELECT
Choose a bounded plan with exact artifacts and evidence strategy.

READ
Review the plan against architecture and repository state.

UPDATE
Revise the plan when evidence contradicts it.
```

Failure prevented:

```text
plan-as-execution and vague implementation claims
```

### 15.3 Design

```text
OBSERVE
Inspect the actual surface, viewport, interaction state, design locks, and user need.

ASSESS CAPACITY
Confirm artifact, viewport, accessibility, and reviewer coverage.

DECOMPOSE
Separate observed usability failure from preference and hypothesis.

SELECT
Choose the smallest coherent design response preserving valid locks.

READ
Interpret visual, interaction, accessibility, and product evidence.

UPDATE
Refine the product, design system, skill, or rule at the correct layer.
```

Failure prevented:

```text
attractive screenshot treated as complete UX validation
```

### 15.4 Engineering

```text
OBSERVE
Inspect code, architecture, dependencies, tests, and runtime behavior.

ASSESS CAPACITY
Confirm write permission, authority, blast radius, checks, and rollback.

DECOMPOSE
Separate root cause, hypothesis, design choice, requirement, and contract rule.

SELECT
Choose the smallest coherent patch and verification strategy.

READ
Interpret test, lint, build, runtime, security, and review evidence by scope.

UPDATE
Fix, revert, narrow, document, or create a learning candidate.
```

Failure prevented:

```text
one passing check treated as total correctness
```

### 15.5 Marketing and growth

```text
OBSERVE
Inspect product truth, audience evidence, channel constraints, and metrics.

ASSESS CAPACITY
Confirm claim authority, legal or brand constraints, and measurement path.

DECOMPOSE
Separate market fact, audience hypothesis, message choice, and product promise.

SELECT
Choose a bounded message or measurable experiment.

READ
Interpret behavioral and business evidence inside experiment scope.

UPDATE
Refine positioning, message, channel, or hypothesis without fabricating claims.
```

Failure prevented:

```text
generated claim treated as approved product truth
```

### 15.6 Runtime and tool operation

```text
OBSERVE
Identify actual system state, tool capability, permission, and requested action.

ASSESS CAPACITY
Verify authority, policy, risk controls, reversibility, and audit path.

DECOMPOSE
Separate ability to execute from authority to execute.

SELECT
Perform, route, request approval, or choose a reversible alternative.

READ
Confirm action result, side effects, and audit evidence.

UPDATE
Record the bounded result without expanding future permission silently.
```

Failure prevented:

```text
tool access treated as authorization
```

### 15.7 Skill refinement

```text
OBSERVE
Capture verified failure, fix, before/after evidence, and existing shared coverage.

ASSESS CAPACITY
Confirm transferability, target repository, write policy, and regression path.

DECOMPOSE
Separate local implementation detail from reusable invariant reason.

SELECT
Choose the smallest correct target layer and patch.

READ
Run conformance, behavioral, transferability, and regression checks.

UPDATE
Promote, keep local, defer, reject, or propose core evolution with provenance.
```

Failure prevented:

```text
one successful product fix promoted as a universal rule
```

---

## 16. Failure And Guardrail Response Model

A loop phase may discover a guardrail violation or insufficient capacity.

Valid responses include:

```text
BLOCK
STOP
NARROW
ROUTE
REQUEST SOURCE
REQUEST EVIDENCE
REQUEST AUTHORITY
REQUEST APPROVAL
REQUIRE REVIEW
REQUIRE ROLLBACK CAPACITY
MARK UNKNOWN
MARK PARTIAL
MARK NOT_VERIFIED
REVERT
ESCALATE
```

The response must match:

```text
protected invariant
risk
reversibility
authority
scope
available capacity
applicable policy
consumer impact
```

A blocked response must not be relabeled as success.

A narrow successful response must not be reported as full completion.

---

## 17. Anti-Patterns

### Observation theater

```text
Listing sources without inspecting or using them.
```

### Capacity theater

```text
Naming risks and missing authority but proceeding unchanged.
```

### Decomposition theater

```text
Labeling assumptions while continuing to report them as facts.
```

### Selection theater

```text
Writing a detailed plan without an executable host mechanism or evidence path.
```

### Evidence theater

```text
Collecting outputs without mapping them to the claims they support.
```

### Update theater

```text
Recording feedback while preventing it from revising any affected layer.
```

### Endless observation

```text
Continuing discovery after sufficient capacity and a discriminating bounded test exist.
```

### Loop-as-workflow

```text
Using the epistemic loop to replace specialist methodology, implementation phases,
or product-specific approval policy.
```

### Loop-as-authority

```text
Assuming a well-reasoned response is authorized merely because the loop was followed.
```

### Hidden execution

```text
Treating SELECT as permission or proof that the response was performed.
```

---

## 18. Embodiment And Evaluation

The epistemic loop is not embodied merely because this document exists.

Embodiment requires evidence that relevant workflows, skills, agents, and reviews preserve its distinctions in repeatable behavior.

Candidate evaluation signals include:

```text
repository facts cite attributable sources
assumptions and unknowns remain explicit
capacity gaps narrow or route work
plans are not reported as execution
tool access is not treated as authority
claims remain proportional to evidence
failed checks revise implementation or status
review remains distinct from approval
local learning chooses the correct target layer
core changes use governed evolution
```

Possible future operationalization includes:

```text
structured decision records
context-pack fields
workflow prompts and gates
behavioral test contracts
review rubrics
runtime traces without private chain of thought
learning-candidate records
conformance checks
```

Machine-readable operationalization must be coordinated with issues `#6`, `#8`, and `#9` rather than introduced silently in this documentation slice.

---

## 19. Relationship To Core Evolution

The loop may produce a learning candidate, but it cannot accept a core change by itself.

```text
bounded execution
→ evidence
→ feedback
→ update
→ evaluated learning
→ learning candidate
→ transferability and counterexample review
→ correct target-layer decision
→ compatibility and authority review
→ accepted update or rejection
```

A product, adapter, runtime, skill, or field test may propose evolution.

Canonical authority owns acceptance.

---

## 20. Validation Gates Before Acceptance

The Epistemic Loop must not be marked accepted until:

- [ ] each phase has a distinct purpose, input, output, and exit condition;
- [ ] SELECT remains distinct from execution and authority;
- [ ] the loop does not duplicate the Development Loop or specialist workflows;
- [ ] capacity assessment preserves capability, permission, authority, risk, validation, and recovery distinctions;
- [ ] model decomposition preserves observation, interpretation, inference, assumption, fact, claim, decision, and approval distinctions;
- [ ] evidence reading remains scoped by source, method, coverage, environment, and claim;
- [ ] update selects the correct ownership layer and cannot silently evolve core;
- [ ] valid block, narrow, route, and stop responses are defined;
- [ ] the loop is usable across analysis, planning, design, engineering, marketing, runtime operations, and skill refinement;
- [ ] the loop improves decision quality without forcing full ceremonial documentation for trivial work;
- [ ] existing Development Loop contracts can reference the mechanism without contradiction;
- [ ] behavioral evaluation candidates are identified for later skill/runtime implementation;
- [ ] cross-document terminology and link review passes;
- [ ] issue `#13` records explicit acceptance or requested revision.

---

## 21. Current Verdict

```text
Cross-domain epistemic loop: FORMALIZED FOR CANDIDATE REVIEW
Phase purposes: DEFINED
Phase inputs and outputs: DEFINED
Exit conditions: DEFINED
Execution boundary: DEFINED
Development Loop separation: DEFINED
Guardrail response model: DEFINED
Cross-domain stress tests: INITIAL PASS
Behavioral embodiment: NOT YET IMPLEMENTED
Machine-readable contract: NOT YET PROPOSED
Cross-document reconciliation: NOT YET COMPLETE
Loop acceptance status: CANDIDATE
Ready for philosophy traceability matrix: YES
Ready for contradiction and glossary reconciliation: PARTIAL
Ready for domain model consumption: NOT YET, PENDING FOUNDATION ACCEPTANCE
```

The next philosophy slice should create a philosophy-to-existing-source traceability and contradiction matrix, then reconcile the philosophy entry point, glossary navigation, architecture documentation, and relevant issue `#6` inputs without rewriting established executable contracts unnecessarily.
