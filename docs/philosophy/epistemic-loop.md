# Native AI Engineering Epistemic Loop

Status: Final candidate foundation mechanism

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Retained laws: [`laws.md`](laws.md)

Retained principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Development Loop: [`../development-loop.md`](../development-loop.md)

Runtime contract: [`../../contracts/runtime/development-loop.contract.yaml`](../../contracts/runtime/development-loop.contract.yaml)

The Epistemic Loop organizes reasoning about relevant state, representations, capacity, evidence, and revision. It does not replace delivery workflows, specialist methodology, runtime orchestration, policy, approval, or the Development Loop.

---

## 1. Loop

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ host mechanism executes or routes
→ READ EVIDENCE
→ UPDATE
```

The host execution step is a boundary, not an Epistemic Loop phase.

```text
SELECT A TESTABLE RESPONSE
≠ execute the response
≠ authorize the response
≠ prove the response succeeded
```

---

## 2. Kernel Relationship

```text
Axiom 1 — Attributable Observation
Material claims and actions begin from attributable observations
or explicit unknowns concerning relevant state.

Axiom 2 — State–Representation Separation
No observation or model is identical to the state it represents.

Bridge Law — Feedback And Governed Evolution
Relevant evidence and feedback are processed at the affected layer;
shared or canonical change requires compatibility review and authority.
```

The loop operationalizes this kernel without becoming another law, workflow, or policy.

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
| Deliver | Applies authority, evidence, completion, and policy checks |

The host mechanism owns:

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

## 4. Invocation And Output

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

A completed loop run produces enough information for a bounded next action or honest stop:

```text
observation and source record;
unknown and not-verified state;
capacity assessment;
epistemic decomposition;
selected response or valid non-action;
expected evidence;
evidence reading;
revision decision;
target-layer update;
completion or limitation status;
learning candidate when justified.
```

These are conceptual outputs. Issue `#8` owns future machine-readable shapes.

---

## 5. OBSERVE

### Purpose

Establish attributable observations and explicit unknowns relevant to the objective before material interpretation, planning, or mutation.

### Questions

```text
What was directly observed?
Through which source and method?
At what ref, time, environment, and coverage?
What remains unavailable, unknown, conflicted, or not verified?
```

### Output

```text
subject;
observation;
source;
method;
time, version, ref, or environment;
coverage and limitations;
unknowns and conflicts.
```

### Exit

The observation baseline is attributable and honest about missing coverage.

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

### Guardrails

```text
No Fabricated State Or Evidence;
No Model-As-Fact Collapse;
No Claim Beyond Evidence Scope;
No Silent Conflict Resolution.
```

---

## 6. ASSESS CAPACITY

### Purpose

Determine whether the available combination of context, capability, tools, permission, authority, controls, validation, review, reversibility, and recovery supports the proposed scope.

### Questions

```text
Can this scope be performed?
May it be performed?
Can it be validated and reviewed?
Can failure or side effects be contained or recovered?
```

### Output

```text
requested scope;
available and missing capacity dimensions;
risk and reversibility;
required authority or approval;
validation and review path;
recommended response.
```

### Exit

Capacity is sufficient for a bounded scope, or a valid narrowing, route, block, or stop is selected.

### Valid responses

```text
PROCEED;
NARROW;
ROUTE;
REQUEST AUTHORITY;
REQUEST APPROVAL;
REQUEST ACCESS;
CHOOSE REVERSIBLE TEST;
MARK PARTIAL;
MARK BLOCKED;
STOP.
```

### Guardrails

```text
Capability Is Not Authority;
No Silent Scope Expansion;
No Undeclared Gate Bypass;
High-Risk Actions Require Applicable Controls.
```

---

## 7. DECOMPOSE THE MODEL

### Purpose

Separate observation, interpretation, inference, assumption, claim, decision, authority, and unknown state so they cannot collapse into one confident narrative.

### Questions

```text
What is observed?
What is interpreted or inferred?
What is assumed?
What is claimed or established within scope?
What was decided, approved, conflicted, or superseded?
What remains unknown or not verified?
```

### Output

```text
material proposition;
epistemic classification;
source or rationale;
scope;
verification status;
authority status;
assumptions;
unknowns;
conflicts;
impact if wrong.
```

### Exit

Material assumptions, claims, authority, conflicts, and unknowns affecting the next response are explicit.

### Guardrails

```text
No Model-As-Fact Collapse;
No Silent Conflict Resolution;
Capability Is Not Authority;
No False Completion.
```

---

## 8. SELECT A TESTABLE RESPONSE

### Purpose

Choose the smallest coherent, authorized response that can produce discriminating evidence without exceeding capacity.

### Questions

```text
What response addresses the objective?
What is the smallest coherent scope?
What can be tested or observed afterward?
Is the response reversible or recoverable?
What authority, policy, gate, and host mechanism apply?
```

### Valid response types

```text
inspect;
clarify;
plan;
implement;
review;
test;
prototype;
route;
request authority;
record adjacent finding;
create learning candidate;
stop.
```

### Exit

A bounded response is selected with owner, host mechanism, expected evidence, and authority conditions—or valid non-action is recorded.

### Principles

```text
Smallest Coherent Change;
Reversible Progress Under Uncertainty;
Correct-Layer Change;
Review Proportional To Risk And Authority;
Explicit Boundaries Over Implicit Expectations.
```

### Guardrails

```text
Capability Is Not Authority;
No Silent Scope Expansion;
No Undeclared Gate Bypass;
High-Risk Actions Require Applicable Controls.
```

---

## 9. READ EVIDENCE

### Purpose

Determine what the produced evidence supports, weakens, contradicts, or leaves unresolved.

### Questions

```text
What actually happened?
Which claim does each evidence item support?
What method, scope, coverage, environment, and limitation apply?
What remains unverified?
What feedback contradicts the working model or completion claim?
```

### Evidence layers remain separate

```text
source or path resolution;
version compatibility;
structural declaration;
behavioral execution;
runtime integration;
security or accessibility evidence;
product acceptance;
business outcome;
review;
approval.
```

### Exit

Evidence is mapped to supported, weakened, contradicted, and unresolved claims without scope inflation.

### Guardrails

```text
No Claim Beyond Evidence Scope;
No False Completion;
Declaration Is Not Embodiment;
Contradictory Feedback Must Be Processed.
```

---

## 10. UPDATE

### Purpose

Revise the affected model, plan, decision, implementation, status, learning record, or shared-layer proposal according to processed evidence and authority.

### Questions

```text
What continues, changes, stops, narrows, or escalates?
Which layer owns the update?
Does the claim or completion status change?
Is retesting required?
Is there a reusable learning candidate?
Does shared promotion require compatibility review and authority?
```

### Valid outcomes

```text
ACCEPT;
REJECT WITH RATIONALE;
REVISE;
RETEST;
NARROW CLAIM;
MARK PARTIAL;
MARK BLOCKED;
MARK NOT_VERIFIED;
ESCALATE;
CREATE LEARNING CANDIDATE;
PROPOSE CANONICAL CHANGE;
EXIT.
```

### Guardrails

```text
Contradictory Feedback Must Be Processed;
No Unverified Promotion To Shared Layers;
Concrete Layers Must Not Redefine Canonical Layers;
No Silent Semantic Evolution.
```

---

## 11. Transition Model

```text
OBSERVE
├─ missing source → request / unknown / block
└─ attributable baseline
     ↓
ASSESS CAPACITY
├─ insufficient → narrow / route / block / stop
└─ sufficient bounded capacity
     ↓
DECOMPOSE THE MODEL
├─ unresolved authority conflict → route / block
└─ material epistemic states explicit
     ↓
SELECT A TESTABLE RESPONSE
├─ no authorized response → request authority / stop
└─ bounded response selected
     ↓
HOST MECHANISM EXECUTES OR ROUTES
     ↓
READ EVIDENCE
├─ insufficient or contradictory → revise / retest / narrow
└─ adequate scoped evidence
     ↓
UPDATE
├─ state changed → OBSERVE
├─ capacity changed → ASSESS CAPACITY
├─ model changed → DECOMPOSE THE MODEL
├─ further response required → SELECT
└─ supported exit
```

---

## 12. Cross-Domain Stress Matrix

| Domain | Pressure | Correct loop behavior |
|---|---|---|
| Repository analysis | Expected branch/file state is unavailable | Mark not verified; inspect or bound the claim |
| Planning | Plan is detailed but no execution access exists | Report planning complete and implementation blocked |
| Design | Desktop screenshot looks polished | Keep interaction, responsive, and accessibility dimensions not verified |
| Engineering | Build passes | Support only the build claim; retain other evidence layers |
| Marketing | Generated audience hypothesis sounds plausible | Keep it as hypothesis until evidence and approval exist |
| Runtime operation | Tool can perform destructive action | Separate capability from authority and apply risk policy |
| Skill refinement | One product fix succeeds | Create learning candidate and test transferability before promotion |

---

## 13. Prohibited Shortcuts

```text
memory or summary as current state;
interpretation as observation;
assumption as fact;
plan as execution;
tool access as authority;
review as approval;
static declaration as runtime behavior;
one check as total completion;
feedback recorded but unable to revise work;
one local success as universal law.
```

---

## 14. Proportional Use

Use the full explicit loop for architecture, contracts, canonical terminology, production or destructive actions, authority conflicts, public claims, and shared-skill promotion.

Low-risk read-only or local work may use a lighter representation, but mandatory guardrails still apply.

---

## 15. Current Verdict

```text
Cross-domain reasoning mechanism: DEFINED
Kernel wording: ALIGNED
Execution boundary: DEFINED
Development Loop separation: DEFINED
Stable-name references: APPLIED
Cross-domain stress examples: PRESENT
Machine-readable serialization: OWNED BY #8
Executable harness: FOLLOW-UP IN ai-native-skills#27
Ready for final acceptance review: YES
```
