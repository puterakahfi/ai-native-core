# Native AI Engineering Derived Laws

Status: Candidate retained kernel

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

Pruning record: [`reconciliation-and-pruning.md`](reconciliation-and-pruning.md)

This document contains the active candidate law set retained after usefulness and pruning review.

It intentionally does not preserve every historical derivation paragraph. Historical candidates, rejected classifications, and extended reasoning remain available in the discovery and reconciliation records.

---

## 1. Purpose

A philosophy-level law is retained only when it:

```text
states a distinct engineering invariant;
changes a material decision;
prevents a known recurring failure;
has a named downstream consumer;
has a plausible embodiment or validation path;
cannot be replaced by a smaller retained concept.
```

A law is not retained because it sounds correct, completes a diagram, or has already been documented at length.

The active law set exists to prevent:

```text
invented state;
model-as-reality collapse;
claims broader than evidence;
untraceable decisions;
capability treated as authority;
execution beyond available capacity;
false completion;
declaration treated as behavior;
feedback that cannot revise the system;
local implementation silently redefining core.
```

---

## 2. Kernel Source

The laws derive from the candidate philosophy kernel:

### Axiom 1 — Available, Attributable State

```text
Engineering work begins from available, attributable state.
```

### Axiom 2 — State–Model Separation

```text
Observed or recorded state is not identical to a human, agent, document,
or system model of that state.
```

### Bridge Law — Evidence And Feedback

```text
AI-native engineering systems preserve continuity and update their operational
organization through appropriately scoped evidence and feedback.
```

These statements are bounded to Native AI Engineering. They are not claims of universal science outside the framework.

---

## 3. Active Law Set

Stable law names are the primary identifiers. Historical `L` numbers remain aliases for traceability until later schema work decides whether machine-readable law IDs are required.

| Stable law name | Historical alias | Distinct responsibility |
|---|---:|---|
| State Attribution | L1 | State claims require attributable source or honest unresolved status |
| State–Model Separation | L2 | Representations remain distinguishable from represented state |
| Claim–Evidence Scope | L4 | Claim strength cannot exceed evidence scope and quality |
| Decision Traceability | L5 | Material decisions preserve source, authority, scope, conflict, and supersession |
| Capability–Authority Separation | L6 | Ability to act does not grant the right to act |
| Execution Capacity | L7 | Execution scope remains inside available operational and validation capacity |
| Coherent Completion | L8 | Completion cannot hide material contradiction or missing evidence |
| Executable Embodiment | L9 | Declared expectations count as embodied only when behavior changes measurably |
| Feedback Revision | L10 | Relevant feedback can revise the affected layer or be rejected traceably |
| Evolution Authority | L11 | Concrete layers may propose but cannot silently redefine canonical layers |

Retired independent candidates:

```text
L3 Model Recognition
→ merged into State–Model Separation, model-as-fact guardrails,
  canonical epistemic terms, and the DECOMPOSE phase.

L12 Governed Stability
→ merged into Evolution Authority, evaluation-before-trust principles,
  semantic-evolution guardrails, the Stability definition, and compatibility policy.
```

---

## 4. Law Dependency Map

```text
A1 Available, Attributable State
├─ State Attribution
├─ Claim–Evidence Scope
├─ Decision Traceability
└─ Execution Capacity

A2 State Is Not Identical To Its Model
├─ State–Model Separation
├─ Claim–Evidence Scope
├─ Decision Traceability
├─ Capability–Authority Separation
├─ Coherent Completion
└─ Executable Embodiment

Bridge Law — Evidence And Feedback
├─ Execution Capacity
├─ Coherent Completion
├─ Executable Embodiment
├─ Feedback Revision
└─ Evolution Authority
```

Dependencies express derivation, not lifecycle order.

---

## 5. State Attribution Law

### Statement

```text
A material engineering claim about state must identify an attributable source,
or remain explicitly unknown, unavailable, blocked, or not verified.
```

### Decision consequence

An actor may not resolve missing state by inventing branch names, file contents, issue status, runtime behavior, test output, approval, or completion evidence.

### Boundaries

```text
Attribution does not guarantee authority, freshness, completeness, or correctness.
Low-risk conversational statements do not always require formal provenance fields.
Required attribution depth grows with consequence, persistence, risk, and reuse.
```

### Counterexample

Valid:

```text
“The current branch could not be confirmed because repository access failed.”
```

Invalid:

```text
“The active branch is feature-x.”
```

when no repository state, tool output, or attributable user statement supports it.

### Primary consumers

```text
issue #6 state and provenance model;
issue #8 source-reference primitives;
repository-analysis and research skills;
behavioral tests for invented state and fabricated evidence.
```

---

## 6. State–Model Separation Law

### Statement

```text
A representation of engineering state must remain distinguishable from the state
it represents, including its source, scope, assumptions, unknowns, and verification status.
```

### Decision consequence

Plans, summaries, diagrams, prompts, contracts, memories, reviews, and generated interpretations may guide action but cannot be presented as direct proof of the represented state.

Material inference, assumption, and hypothesis must remain recognizable when consequence, risk, reuse, or irreversibility is significant.

### Common distinctions

```text
repository state ≠ repository summary
user intent ≠ inferred intent
architecture diagram ≠ implementation
plan ≠ execution
contract ≠ implementation
skill declaration ≠ skill application
review verdict ≠ approval
memory ≠ source-of-truth knowledge
metric ≠ complete product meaning
```

### Boundaries

```text
Models are necessary and may be highly reliable.
The law does not require every model to reproduce all underlying state.
A verified model may guide action without becoming identical to reality.
```

### Primary consumers

```text
issue #6 epistemic-state objects;
issue #8 assumption and verification primitives;
analysis, planning, design, and engineering skills;
runtime context records and behavioral evaluations.
```

---

## 7. Claim–Evidence Scope Law

### Statement

```text
The strength, scope, and maturity of an engineering claim must not exceed the
source, method, coverage, quality, and relevance of its supporting evidence.
```

### Decision consequence

Passing one evidence layer does not prove another:

```text
path resolution
≠ version compatibility
≠ structural conformance
≠ behavioral execution
≠ runtime integration
≠ product acceptance
≠ business outcome
≠ required approval
```

### Counterexample

Valid:

```text
“The unit tests passed for the changed module. Runtime integration and product
acceptance were not evaluated.”
```

Invalid:

```text
“The feature is complete and production-ready.”
```

based only on a passing unit test or build.

### Boundaries

Exploratory and reversible work may proceed with weaker evidence when uncertainty and claim scope remain explicit.

### Primary consumers

```text
issue #8 evidence and claim primitives;
issue #9 layered conformance results;
verification, review, and completion reporting;
product acceptance and marketing-claim controls.
```

---

## 8. Decision Traceability Law

### Statement

```text
A material engineering decision is reliable only to the degree that its source,
authority, scope, rationale, evidence, conflicts, and supersession chain can be traced.
```

### Decision consequence

Decision existence, recency, implementation presence, or silence does not establish effective authority.

Material decision records should support, where applicable:

```text
decision identity and type;
source and required authority;
applies-to scope;
rationale and evidence;
conflicts;
supersedes and superseded-by;
permitted and blocked actions;
approval and verification status.
```

### Boundaries

Traceability depth is proportional to impact. A local variable rename does not require an ADR; an architecture change, destructive operation, or risk acceptance does.

### Primary consumers

```text
issue #6 decision and approval lifecycle;
issue #8 decision and authority primitives;
control-plane routing;
review, approval, and audit records.
```

---

## 9. Capability–Authority Separation Law

### Statement

```text
The capability to execute an action does not by itself grant the permission,
authority, approval, or policy right to execute that action.
```

### Decision consequence

Systems must model separately:

```text
capability;
technical permission;
policy allowance;
required authority;
approval status;
risk;
reversibility;
allowed scope.
```

### Counterexample

Valid:

```text
A deployment adapter runs automatically because an accepted release policy
explicitly authorizes deployment after named gates pass.
```

Invalid:

```text
An agent force-pushes because the repository token technically allows it.
```

### Boundaries

Authority may be delegated in advance. The law does not require interactive approval for every low-risk operation covered by explicit policy.

### Primary consumers

```text
issue #6 governance and authority model;
issue #7 control and integration port contracts;
native-ai-fw tool and action authorization;
high-risk and destructive-action behavioral tests.
```

---

## 10. Execution Capacity Law

### Statement

```text
Execution scope must not exceed the available context, capability, tools,
permission, authority, risk controls, validation path, review coverage,
reversibility, and recovery support required for that scope.
```

### Decision consequence

When a material capacity dimension is missing, valid responses include:

```text
NARROW
PAUSE
ROUTE
REQUEST SOURCE
REQUEST AUTHORITY
CHOOSE A REVERSIBLE TEST
MARK PARTIAL
MARK BLOCKED
STOP
```

Insufficient capacity must not be resolved through fabricated certainty or completion.

### Boundaries

Capacity is contextual, not a permanent rating of an agent or team. Insufficient capacity for a full task may still permit safe discovery or a smaller experiment.

### Primary consumers

```text
issue #6 execution and governance contexts;
issue #7 port authorization, failure, and observability semantics;
workflow and runtime routing;
product release and recovery policy.
```

---

## 11. Coherent Completion Law

### Statement

```text
A system must not claim completion while unresolved material contradictions remain
between authoritative intent, requirements, contracts, architecture, implementation,
behavior, evidence, review, approval, and delivery state inside the claim scope.
```

### Decision consequence

Completion reports must distinguish states such as:

```text
COMPLETED
PARTIAL
BLOCKED
NOT_VERIFIED
NOT_APPLICABLE
ACCEPTED_WITH_LIMITATION
```

Exact enums belong to domain and contract work. The philosophy requires honest differentiation.

### Counterexample

Valid:

```text
“Desktop visual review passed. Mobile interaction and accessibility remain not
verified, so the redesign status is partial.”
```

Invalid:

```text
“The redesign is complete.”
```

when mobile interaction was in scope and remains unusable.

### Boundaries

Perfect global consistency is not required. Non-material differences and explicitly accepted limitations may remain.

### Primary consumers

```text
issue #6 lifecycle and completion model;
issue #8 status and gate-result primitives;
workflow completion reporting;
product acceptance and release decisions.
```

---

## 12. Executable Embodiment Law

### Statement

```text
A principle, rule, contract, skill, or workflow is embodied only when it changes
repeatable executable behavior and that behavior can produce evidence appropriate
to the embodiment claim.
```

### Decision consequence

```text
documentation presence ≠ embodiment
contract presence ≠ implementation
skill installation ≠ skill application
metadata declaration ≠ runtime behavior
one successful execution ≠ stable embodiment
```

### Counterexample

Invalid:

```text
A system claims a safety principle is implemented because it appears in a README,
while destructive actions bypass it at runtime.
```

### Boundaries

Some principles may remain advisory and be reviewed qualitatively. Embodiment does not require perfect execution in every case, but it requires relevant behavioral evidence.

### Primary consumers

```text
issue #9 separation of static and behavioral conformance;
ai-native-skills behavioral test harness;
native-ai-fw routing and execution evidence;
product validation and regression protection.
```

---

## 13. Feedback Revision Law

### Statement

```text
Appropriately scoped feedback must be able to revise the affected model, plan,
decision, implementation, claim, or other owned layer, or be rejected with
traceable rationale and authority.
```

### Decision consequence

Material contradictory feedback cannot be recorded ceremonially and then ignored while the system continues making the same completion or quality claim.

Valid feedback responses include:

```text
ACCEPT
REJECT WITH RATIONALE
NARROW CLAIM
REVISE
RETEST
ESCALATE
CREATE LEARNING CANDIDATE
PROPOSE TARGET-LAYER CHANGE
```

### Boundaries

Feedback is not automatically correct, authoritative, or final truth. It must be evaluated for source, scope, quality, relevance, and authority.

### Primary consumers

```text
issue #6 feedback and learning lifecycle;
workflow failure and review loops;
product metrics and incident handling;
skill refinement and regression evaluation.
```

---

## 14. Evolution Authority Law

### Statement

```text
A more concrete layer may apply, translate, test, and propose changes to a more
canonical layer, but it may not silently redefine that layer without the canonical
layer's review, compatibility analysis, and authority.
```

### Decision consequence

Valid promotion path:

```text
implementation result
→ bounded evidence
→ reusable reason
→ counterexample and transferability review
→ smallest correct target-layer decision
→ compatibility analysis
→ required authority
→ accepted update or rejection
```

A stable artifact may evolve; stability means governed consumer expectations, not immutability.

### Counterexample

Valid:

```text
A product-specific navigation fix remains local, then becomes a reusable learning
candidate after multi-context testing.
```

Invalid:

```text
A skill copies one product's breakpoint, route, and component name into a universal
core contract because the local fix succeeded once.
```

### Primary consumers

```text
issue #6 learning and evolution context;
issue #7 and #8 compatibility and supersession semantics;
skill-evolution procedures;
core, contract, and glossary change review.
```

---

## 15. Cross-Law Invariants

Together the retained laws preserve:

```text
state remains attributable;
models remain recognizable as models;
material uncertainty remains visible;
claims remain bounded by evidence;
decisions remain traceable;
capability remains separate from authority;
execution remains inside capacity;
completion remains coherent with evidence and approval;
declarations require behavior before embodiment claims;
feedback can revise the correct layer;
local learning cannot silently redefine canonical meaning.
```

---

## 16. Consumer Rule

Consumers must not copy all laws into every artifact.

A domain model, contract, skill, workflow, runtime, reviewer, or product should reference only laws that materially affect its responsibility.

Examples:

```text
repository analysis
→ State Attribution, State–Model Separation, Claim–Evidence Scope

destructive tool operation
→ Decision Traceability, Capability–Authority Separation, Execution Capacity

conformance validator
→ Claim–Evidence Scope, Executable Embodiment, Coherent Completion

skill refinement
→ Feedback Revision, Executable Embodiment, Evolution Authority
```

---

## 17. Acceptance Gates

The retained laws must not be accepted until:

- [x] each has a distinct decision consequence;
- [x] each names recurring failures it prevents;
- [x] each has at least one downstream consumer;
- [x] duplicate independent candidates are merged or reclassified;
- [x] historical numbering is no longer the primary authority;
- [ ] behavioral test candidates cover representative false-equivalence failures;
- [ ] principles and guardrails pass equivalent pruning review;
- [ ] issue `#6` confirms the law set is sufficient for domain modeling;
- [ ] cross-document references are reviewed for stale retired-law aliases;
- [ ] issue `#13` records explicit acceptance or requested revision.

---

## 18. Current Verdict

```text
Retained candidate laws: 10
Independent Model Recognition law: MERGED
Independent Governed Stability law: MERGED / RECLASSIFIED
Stable law names: PRIMARY IDENTIFIERS
Historical law numbers: TRACEABILITY ALIASES
Decision usefulness: PRESENT
Named consumers: PRESENT
Behavioral embodiment: CANDIDATES REQUIRED
Law acceptance status: CANDIDATE
Ready for domain model consumption: PARTIAL, PENDING FOUNDATION ACCEPTANCE
```
