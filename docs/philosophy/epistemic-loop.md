# Native AI Engineering Epistemic Loop

Status: Candidate foundation mechanism

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Retained laws: [`laws.md`](laws.md)

Retained principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Development Loop: [`../development-loop.md`](../development-loop.md)

Runtime contract: [`../../contracts/runtime/development-loop.contract.yaml`](../../contracts/runtime/development-loop.contract.yaml)

This document defines the cross-domain reasoning mechanism for distinguishing available state from models, assessing capacity, selecting bounded responses, reading evidence, and updating the correct layer.

It does not replace delivery workflows, specialist skills, runtime orchestration, approval policy, or the Development Loop.

---

## 1. Candidate Loop

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ HOST MECHANISM EXECUTES OR ROUTES
→ READ EVIDENCE
→ UPDATE
```

The host execution step is shown as a boundary, not an Epistemic Loop phase.

```text
SELECT A TESTABLE RESPONSE
≠ execute the response
≠ authorize the response
≠ prove the response succeeded
```

---

## 2. Mechanism Boundary

```text
Law
= explains the invariant.

Principle
= guides response selection.

Guardrail
= defines a mandatory boundary.

Epistemic Loop
= organizes reasoning about state, models, capacity, evidence, and revision.

Development Loop or specialist workflow
= owns execution phases, gates, artifacts, verification, review, documentation, and delivery.

Policy
= owns context-specific permission, approval, risk, and shortcut rules.
```

Following the loop does not create authority or prove correctness.

---

## 3. Relationship To The Development Loop

```text
Explore → Plan → Implement → Verify → Review → Document → Deliver
```

| Development Loop phase | Epistemic Loop use |
|---|---|
| Explore | OBSERVE, ASSESS CAPACITY, DECOMPOSE THE MODEL |
| Plan | DECOMPOSE THE MODEL, SELECT A TESTABLE RESPONSE |
| Implement | Host mechanism performs the selected authorized response |
| Verify | Produces evidence for READ EVIDENCE |
| Review | Produces findings and verdict evidence for READ EVIDENCE |
| Document | Records UPDATE decisions, limitations, and learning |
| Deliver | Uses authority, evidence, completion, and policy checks |

Execution belongs to the host workflow, skill, runtime, tool operation, CI mechanism, product experiment, or human process.

The host mechanism must preserve:

```text
actual action performed;
actor or execution surface;
scope;
permission and authority;
applicable policy and gates;
risk and recovery controls;
resulting state;
evidence produced;
failures and side effects.
```

Unexpected execution state returns to OBSERVE.

---

## 4. Invocation

A loop run may begin from:

```text
user instruction;
issue or acceptance criterion;
repository or product state;
current implementation;
runtime behavior;
review finding;
verification output;
approval requirement;
incident or regression;
learning candidate;
canonical change proposal.
```

Identify where possible:

```text
subject;
objective or question;
initial scope;
available sources;
authority context;
risk context;
host workflow or mechanism.
```

Missing state may allow bounded discovery. It must not be fabricated.

### Full explicit use

Appropriate for:

```text
architecture or contract changes;
high-risk or destructive actions;
production-impacting changes;
security-sensitive work;
conflicting authoritative decisions;
cross-repository evolution;
public product or marketing claims;
canonical terminology changes;
complex incidents;
shared-skill promotion.
```

### Lightweight use

May be sufficient for:

```text
low-risk local edits;
simple read-only analysis;
well-bounded verification;
routine reversible operations.
```

Lightweight use still preserves all applicable guardrails.

---

## 5. Conceptual Outputs

A complete loop run produces enough structure for a bounded next action or an honest stop condition:

```text
observation set;
source and coverage record;
unknown and not-verified record;
capacity assessment;
epistemic decomposition;
testable response selection or valid non-action;
expected evidence and validation path;
evidence reading;
update decision;
completion or limitation status;
learning candidate when justified.
```

These are conceptual outputs, not a universal serialization format. Issue `#8` owns future schema decisions.

---

## 6. OBSERVE

### Purpose

Establish available, attributable state before materially interpreting, planning, claiming, or changing the system.

### Primary question

```text
What is currently available and directly attributable within the relevant scope?
```

### Inspect

```text
source-of-truth artifacts;
repository, issue, branch, file, or product state;
runtime and tool state where permitted;
explicit user or owner statements;
existing evidence;
missing access and coverage;
conflicting or superseded sources.
```

### Preserve distinctions

```text
state vs observation;
available state vs merely observable state;
direct observation vs remembered or generated summary;
current source vs superseded source;
source existence vs authority.
```

### Output

An observation set containing:

```text
subject;
source reference;
observation or record;
time, version, ref, or environment where material;
coverage;
source status;
unknowns;
unavailable state;
conflicts.
```

### Exit condition

```text
The available-state baseline is attributable, scoped, and honest about missing coverage.
```

### Valid responses

```text
CONTINUE;
REQUEST SOURCE;
REQUEST EVIDENCE;
MARK UNKNOWN;
MARK NOT_VERIFIED;
NARROW;
BLOCK MATERIAL CLAIM.
```

### Applicable boundaries

```text
State Attribution;
State–Model Separation;
Claim–Evidence Scope;
No Fabricated State Or Evidence;
No Model-As-Fact Collapse;
No Claim Beyond Evidence Scope;
No Silent Conflict Resolution.
```

### Invalid shortcuts

```text
starting from remembered repository structure without checking;
using an agent summary as owner instruction;
claiming test status without output;
using one screenshot as complete product state;
assuming the newest source is authoritative without authority review.
```

---

## 7. ASSESS CAPACITY

### Purpose

Determine whether context, capability, tools, permission, authority, controls, evidence path, review, and recovery are sufficient for the proposed scope.

### Primary question

```text
Is there enough bounded capacity to perform and validate this scope responsibly?
```

### Capacity dimensions

```text
context availability;
source coverage;
domain and technical capability;
tool availability;
permission;
authority and approval;
risk controls;
reversibility;
recovery or rollback capacity;
time and scope budget;
validation path;
review coverage;
consumer-impact visibility.
```

### Preserve distinctions

```text
capability vs permission;
permission vs authority;
technical possibility vs policy allowance;
confidence vs capacity;
partial capacity vs full completion capacity.
```

### Output

A capacity assessment containing:

```text
requested scope;
available and missing dimensions;
risk and reversibility;
required authority or approval;
evidence path;
review and recovery coverage;
recommended response.
```

### Exit condition

```text
Capacity is sufficient for the bounded scope, or a valid narrowing, routing,
blocking, or stop response has been selected.
```

### Valid responses

```text
PROCEED;
NARROW;
ROUTE;
REQUEST AUTHORITY;
REQUEST APPROVAL;
REQUEST TOOL OR SOURCE ACCESS;
CHOOSE REVERSIBLE TEST;
MARK PARTIAL;
MARK BLOCKED;
STOP.
```

### Applicable principles and boundaries

```text
Reversible Progress Under Uncertainty;
Review Proportional To Risk And Authority;
Capability–Authority Separation;
Execution Capacity;
Capability Is Not Authority;
No Silent Scope Expansion;
No Undeclared Gate Bypass;
High-Risk Actions Require Applicable Controls.
```

### Invalid shortcuts

```text
tool access treated as authorization;
write permission treated as approved scope;
production action without recovery capacity;
full UX claim without required viewport or interaction coverage;
implementation claim without execution evidence.
```

Capacity is contextual. Insufficient capacity for full implementation may still allow discovery or a reversible test.

---

## 8. DECOMPOSE THE MODEL

### Purpose

Separate representations and epistemic states so observation, interpretation, inference, assumption, decision, authority, claim, and unknown state do not collapse into one confident narrative.

### Primary question

```text
What is observed, interpreted, inferred, assumed, claimed, decided, approved,
unknown, conflicted, superseded, or not verified?
```

### Inspect

```text
problem framing;
requirements model;
architecture model;
plan;
risk model;
product or causal hypothesis;
completion model;
learning hypothesis.
```

### Candidate categories

```text
OBSERVED;
INTERPRETED;
INFERRED;
ASSUMED;
CLAIMED;
ESTABLISHED_WITHIN_SCOPE;
DECIDED;
EFFECTIVE_DECISION;
APPROVED;
UNKNOWN;
NOT_VERIFIED;
CONFLICTED;
SUPERSEDED;
OUT_OF_SCOPE.
```

Final machine statuses belong to domain and contract work.

### Output

An epistemic decomposition containing:

```text
material proposition;
classification;
source or rationale;
scope;
verification status;
authority status;
conflicts;
assumptions and unknowns;
impact if wrong.
```

### Exit condition

```text
Material assumptions, inferences, claims, decisions, authority, conflicts,
and unknowns affecting the next response are explicit.
```

### Valid responses

```text
CONTINUE;
MARK ASSUMPTION;
MARK CONFLICTED;
REQUEST CLARIFICATION;
REQUEST AUTHORITY;
REQUEST EVIDENCE;
NARROW;
BLOCK DEPENDENT ACTION.
```

### Applicable boundaries

```text
State–Model Separation;
Decision Traceability;
No Model-As-Fact Collapse;
No Silent Conflict Resolution;
No False Completion.
```

### Invalid shortcuts

```text
inferred requirement reported as explicit requirement;
plan reported as execution;
review reported as approval;
confidence reported as evidence;
silence reported as consent;
memory reported as current authoritative state.
```

---

## 9. SELECT A TESTABLE RESPONSE

### Purpose

Choose a bounded response that is coherent with the objective, available capacity, authority, risk, existing accepted work, and evidence path.

### Primary question

```text
What is the smallest authorized response that can make progress or distinguish
the relevant competing models?
```

### Selection factors

```text
objective and accepted scope;
capacity and authority;
risk and reversibility;
expected evidence;
blast radius;
consumer impact;
existing correct work;
correct ownership layer;
cost of being wrong.
```

### Response specification

```text
response;
objective;
scope and exclusions;
host mechanism;
required permission and authority;
applicable policy and guardrails;
expected evidence;
verification or validation path;
review or approval requirement;
rollback, fallback, or stop condition.
```

### Output

A testable response selection.

### Exit condition

```text
The selected response is bounded, coherent, inside available capacity and authority,
and has an evidence path proportionate to the intended claim.
```

### Applicable principles and boundaries

```text
Domain And Capability Before Tools;
Smallest Coherent Change;
Reversible Progress Under Uncertainty;
Correct-Layer Change;
Evaluation Before Trust Expansion;
Review Proportional To Risk And Authority;
Explicit Boundaries Over Implicit Expectations;
Capability Is Not Authority;
No Silent Scope Expansion;
No Undeclared Gate Bypass;
No Unverified Promotion To Shared Layers;
High-Risk Actions Require Applicable Controls.
```

### Invalid shortcuts

```text
choosing a response only because a tool is available;
selecting provider before capability meaning;
performing adjacent refactors without scope;
choosing irreversible action when a reversible test is sufficient;
promoting a product-specific fix directly into core.
```

The selected response remains a model of intended action until the host mechanism performs it and produces evidence.

---

## 10. EXECUTION BOUNDARY

The host mechanism executes or routes the selected response.

Examples:

```text
Development Loop Implement phase;
specialist skill procedure;
workflow phase;
runtime tool operation;
CI or deployment mechanism;
human review or approval process;
product experiment.
```

The host mechanism returns or preserves:

```text
actual action;
actor or surface;
scope;
resulting state;
evidence;
failures;
side effects;
policy and gate outcomes.
```

```text
SELECT
→ HOST EXECUTION OR ROUTING
→ state and evidence
→ READ EVIDENCE
```

Unexpected material state returns to OBSERVE.

---

## 11. READ EVIDENCE

### Purpose

Determine what the resulting evidence supports, weakens, contradicts, or leaves unresolved without inflating its meaning.

### Primary questions

```text
What does the evidence show?
What claim can it support?
What claim can it not support?
What contradiction remains?
```

### Evidence dimensions

```text
source;
method;
scope;
coverage;
time and environment;
relevance;
reliability;
reproducibility where applicable;
claim supported;
limitations;
contradictory evidence.
```

### Evidence surfaces

```text
source evidence;
implementation evidence;
static conformance evidence;
behavioral evaluation evidence;
runtime evidence;
security and accessibility evidence;
product acceptance evidence;
business metric evidence;
review evidence;
approval evidence;
regression evidence.
```

### Output

An evidence reading containing:

```text
evidence item and method;
source, scope, and coverage;
supported and unsupported claims;
contradictions and limitations;
verification or validation result;
review or approval status where applicable;
required next response.
```

### Exit condition

```text
Evidence meaning is bounded to source and coverage, and material contradictions
or missing evidence are explicit.
```

### Valid readings

```text
SUPPORTS CLAIM WITHIN SCOPE;
WEAKENS CLAIM;
CONTRADICTS CLAIM;
INSUFFICIENT;
NOT RELEVANT;
NOT AUTHORITATIVE FOR DECISION;
REQUIRES BROADER VALIDATION;
REQUIRES REVIEW;
REQUIRES APPROVAL.
```

### Applicable boundaries

```text
Claim–Evidence Scope;
Coherent Completion;
Executable Embodiment;
No Fabricated State Or Evidence;
No Claim Beyond Evidence Scope;
No False Completion;
Declaration Is Not Embodiment;
Contradictory Feedback Must Be Processed.
```

### Invalid shortcuts

```text
build pass reported as complete product validity;
static declaration reported as runtime behavior;
review verdict reported as approval;
one viewport reported as responsive validation;
metric correlation reported as causation;
one local success reported as universal rule.
```

---

## 12. UPDATE

### Purpose

Revise the correct model, decision, implementation, knowledge, skill, workflow, contract proposal, or canonical layer according to evidence, feedback, authority, and compatibility obligations.

### Primary question

```text
What should continue, change, stop, narrow, route, be retested,
or become a governed learning or evolution proposal?
```

### Candidate targets

```text
working context;
interpretation or assumption;
claim;
plan or task state;
decision;
implementation;
product knowledge or policy;
skill or reference;
workflow;
behavioral evaluation;
contract or port proposal;
canonical term proposal;
domain-model proposal;
philosophy evolution proposal.
```

### Decision factors

```text
evidence reading;
feedback relevance;
authority and scope;
consumer impact;
compatibility;
regression risk;
correct ownership layer;
required approval;
remaining contradictions.
```

### Output

An update decision containing:

```text
accepted or rejected feedback;
rationale;
changed claim or model;
target layer;
required implementation or documentation update;
retest or review requirement;
compatibility impact;
completion or limitation status;
learning candidate or evolution proposal where justified.
```

### Valid responses

```text
CONTINUE;
REVISE MODEL;
REVISE PLAN;
REVISE IMPLEMENTATION;
NARROW CLAIM;
RETEST;
REQUEST MORE EVIDENCE;
ROUTE FOR REVIEW;
ROUTE FOR APPROVAL;
REVERT;
STOP;
MARK PARTIAL;
MARK BLOCKED;
ACCEPT WITH LIMITATION;
CREATE LEARNING CANDIDATE;
PROPOSE TARGET-LAYER CHANGE;
REJECT FEEDBACK WITH RATIONALE.
```

### Applicable principles and boundaries

```text
Correct-Layer Change;
Evaluation Before Trust Expansion;
Feedback Revision;
Evolution Authority;
No False Completion;
Contradictory Feedback Must Be Processed;
No Unverified Promotion To Shared Layers;
Concrete Layers Must Not Redefine Canonical Layers;
No Silent Semantic Evolution.
```

### Correct-layer path

```text
local implementation evidence
→ may update local implementation;

reusable verified learning
→ may become a learning candidate;

learning candidate
→ may propose a shared-layer change;

canonical change
→ requires canonical ownership, compatibility review, validation, and authority.
```

### Exit condition

```text
The affected layer and claim status reflect the evidence, authority,
remaining uncertainty, and required follow-up honestly.
```

After UPDATE, return to the earliest affected phase:

```text
state changed → OBSERVE;
capacity changed → ASSESS CAPACITY;
model changed → DECOMPOSE THE MODEL;
another response required → SELECT;
otherwise supported exit.
```

---

## 13. Transition Model

```text
OBSERVE
  ├─ insufficient source → REQUEST SOURCE / MARK UNKNOWN / BLOCK CLAIM
  └─ attributable baseline
       ↓
ASSESS CAPACITY
  ├─ insufficient capacity → NARROW / ROUTE / BLOCK / STOP
  └─ sufficient bounded capacity
       ↓
DECOMPOSE THE MODEL
  ├─ unresolved authority conflict → ROUTE / BLOCK
  └─ epistemic states explicit
       ↓
SELECT A TESTABLE RESPONSE
  ├─ no authorized response → STOP / REQUEST AUTHORITY
  └─ bounded response selected
       ↓
HOST MECHANISM EXECUTES OR ROUTES
       ↓
READ EVIDENCE
  ├─ insufficient or contradictory → REVISE / RETEST / NARROW
  └─ evidence supports bounded update
       ↓
UPDATE
  ├─ state changed → OBSERVE
  ├─ capacity changed → ASSESS CAPACITY
  ├─ model changed → DECOMPOSE THE MODEL
  ├─ another response required → SELECT
  └─ supported exit
```

Iteration must not become endless analysis. When capacity is sufficient and a bounded discriminating test exists, progress to selection and host execution.

---

## 14. Cross-Domain Stress Tests

## Repository analysis

```text
OBSERVE repository, branch, issue, files, contracts, and tests.
DECOMPOSE observed structure from inferred architecture and remembered context.
SELECT bounded analysis or source retrieval.
READ each repository claim against attributable evidence.
UPDATE the working model and mark missing state honestly.
```

Prevents:

```text
invented paths, branches, implementation state, and test results.
```

## Planning

```text
OBSERVE objective, acceptance criteria, constraints, and implementation.
ASSESS context, authority, and validation path.
DECOMPOSE requirements, assumptions, dependencies, and decisions.
SELECT bounded plan with evidence strategy.
UPDATE when repository evidence contradicts the plan.
```

Prevents:

```text
plan-as-execution and vague completion claims.
```

## Design

```text
OBSERVE actual surface, viewport, interaction state, design locks, and user need.
DECOMPOSE usability evidence from preference and hypothesis.
SELECT smallest coherent response preserving accepted useful work.
READ visual, interaction, responsive, accessibility, and product evidence separately.
UPDATE product, design system, or skill at the correct layer.
```

Prevents:

```text
polished screenshot treated as complete UX validation.
```

## Engineering

```text
OBSERVE code, architecture, dependencies, tests, and runtime behavior.
ASSESS write authority, blast radius, checks, and recovery.
DECOMPOSE root-cause hypothesis from verified cause and contract rule.
SELECT smallest coherent patch and verification strategy.
READ test, build, runtime, security, and review evidence by scope.
UPDATE by fixing, reverting, narrowing, or creating a learning candidate.
```

Prevents:

```text
one passing check treated as total correctness.
```

## Marketing and growth

```text
OBSERVE product truth, audience evidence, channel constraints, and metrics.
DECOMPOSE market fact, audience hypothesis, message choice, and product promise.
SELECT bounded message or measurable experiment.
READ behavioral and business evidence inside experiment scope.
UPDATE positioning or hypothesis without fabricating claims.
```

Prevents:

```text
generated claim treated as approved product truth.
```

## Runtime and tool operations

```text
OBSERVE system state, capability, permission, authority, and requested action.
ASSESS policy, risk, reversibility, recovery, and audit path.
SELECT perform, route, request approval, or safer alternative.
READ result, side effects, and audit evidence.
UPDATE bounded status without silently expanding future permission.
```

Prevents:

```text
tool access treated as authorization.
```

## Skill refinement

```text
OBSERVE verified failure, fix, evidence, and existing shared coverage.
ASSESS transferability, target repository, policy, and regression path.
DECOMPOSE local implementation detail from reusable invariant reason.
SELECT smallest correct target layer.
READ conformance, behavioral, transferability, and regression evidence.
UPDATE by promoting, keeping local, deferring, or proposing core evolution.
```

Prevents:

```text
one successful product fix promoted as a universal rule.
```

---

## 15. Anti-Patterns

```text
Observation theater
= listing sources without inspecting or using them.

Capacity theater
= naming missing authority or controls but proceeding unchanged.

Decomposition theater
= labeling assumptions while still executing them as facts.

Selection theater
= writing a detailed plan without an executable host or evidence path.

Evidence theater
= collecting outputs without mapping them to claims.

Update theater
= recording feedback while preventing revision.

Endless observation
= continuing discovery after sufficient capacity and a discriminating test exist.

Loop-as-workflow
= replacing specialist execution methodology with the Epistemic Loop.

Loop-as-authority
= assuming a well-reasoned response is authorized.

Hidden execution
= treating SELECT as performed action.
```

---

## 16. Embodiment And Evaluation

The loop is not embodied because this document exists.

Candidate evidence includes:

```text
repository claims cite attributable sources;
assumptions and unknowns remain explicit;
capacity gaps narrow or route work;
plans are not reported as execution;
tool access is not treated as authority;
claims remain proportional to evidence;
failed checks revise implementation or status;
review remains distinct from approval;
local learning selects the correct layer;
canonical changes use governed evolution.
```

Possible operationalization:

```text
structured decision records;
context-pack fields;
workflow prompts and gates;
behavioral test contracts;
review rubrics;
runtime traces without private chain of thought;
learning-candidate records;
conformance checks.
```

Machine-readable operationalization must be coordinated with issues `#6`, `#8`, and `#9`.

---

## 17. Current Verdict

```text
Cross-domain reasoning mechanism: FORMALIZED FOR CANDIDATE REVIEW
Stable-name alignment: APPLIED
Six reasoning phases: DEFINED
Execution boundary: DEFINED
Development Loop separation: DEFINED
Guardrail response behavior: DEFINED
Cross-domain stress tests: PRESENT
Behavioral candidates: LINKED
Machine-readable contract: NOT YET PROPOSED
Executable embodiment: NOT YET IMPLEMENTED
Ready for final contradiction review: YES
Ready for domain model consumption: PARTIAL
Ready to merge into main: NO
```
