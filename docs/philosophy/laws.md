# Native AI Engineering Derived Laws

Status: Final candidate retained kernel

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Principles and guardrails: [`principles-and-guardrails.md`](principles-and-guardrails.md)

Behavioral candidates: [`behavioral-test-candidates.md`](behavioral-test-candidates.md)

Historical derivation and pruning decisions remain in the discovery and reconciliation records. This file contains only the active law set.

---

## 1. Retention Rule

A philosophy-level law is retained only when it:

```text
states a distinct engineering invariant;
changes a material decision;
prevents a recurring failure;
has a named consumer;
has an embodiment or validation path;
cannot be replaced by a smaller retained concept.
```

Stable law names are the primary identifiers. Historical `L` numbers remain traceability aliases only.

---

## 2. Kernel Source

### Axiom 1 — Attributable Observation

```text
Material engineering claims and actions begin from attributable observations
or explicit unknowns concerning relevant state.
```

### Axiom 2 — State–Representation Separation

```text
No observation or model is identical to the state it represents.
```

### Bridge Law — Feedback And Governed Evolution

```text
Relevant evidence and feedback must be processed at the affected layer;
changes to shared or canonical agreements require proportionate compatibility
review and authority.
```

---

## 3. Active Law Set

| Stable law name | Historical alias | Distinct responsibility |
|---|---:|---|
| State Attribution | L1 | Material state claims require attributable observation or honest unresolved status |
| State–Model Separation | L2 | Representations remain distinguishable from represented state |
| Claim–Evidence Scope | L4 | Claim strength cannot exceed evidence source, method, scope, and coverage |
| Decision Traceability | L5 | Material decisions preserve source, authority, scope, conflicts, and supersession |
| Capability–Authority Separation | L6 | Ability or access does not grant the right to act |
| Execution Capacity | L7 | Action scope remains inside available context, authority, controls, and validation capacity |
| Coherent Completion | L8 | Completion cannot hide material contradiction, missing evidence, or required approval |
| Executable Embodiment | L9 | Declared expectations count as embodied only when behavior changes and produces evidence |
| Feedback Revision | L10 | Relevant contradictory feedback must revise the affected layer or be rejected traceably |
| Evolution Authority | L11 | Concrete layers may propose but cannot silently redefine canonical layers |

Retired independent candidates:

```text
Model Recognition
→ merged into State–Model Separation, epistemic terms, and model-as-fact guardrails.

Governed Stability
→ merged into Evolution Authority, Stability, compatibility policy,
  evaluation-before-trust principles, and semantic-evolution guardrails.
```

---

## 4. State Attribution

### Statement

```text
A material engineering claim about state must identify an attributable observation
or source, or remain explicitly unknown, unavailable, blocked, or not verified.
```

### Derived from

```text
Axiom 1 — Attributable Observation
```

### Decision consequence

An actor must not invent branch names, file contents, issue state, runtime behavior, test results, approval, or completion evidence to fill missing access.

### Boundaries

```text
attribution does not prove authority, freshness, completeness, or correctness;
formal provenance depth grows with consequence, persistence, risk, and reuse;
low-risk conversation does not require ceremony when status is already unambiguous.
```

### Consumers and cases

```text
#6 epistemic state model;
#8 source/status primitives;
repository-analysis skills;
B1 Unverified Repository State.
```

---

## 5. State–Model Separation

### Statement

```text
A representation of engineering state must remain distinguishable from the state
it represents, including its source, scope, assumptions, unknowns, and verification status.
```

### Derived from

```text
Axiom 2 — State–Representation Separation
```

### Decision consequence

Plans, summaries, diagrams, prompts, memories, contracts, and generated artifacts must not be reported as current implementation or observed fact without appropriate verification.

### Boundaries

```text
models may be reliable and action-guiding;
useful abstraction remains necessary;
not every sentence requires an explicit status tag;
required visibility grows with risk and downstream reuse.
```

### Consumers and cases

```text
#6 model and assumption relationships;
analysis, planning, design, and debugging skills;
B2 Assumption Presented As Root Cause;
B3 Plan Reported As Execution.
```

---

## 6. Claim–Evidence Scope

### Statement

```text
The strength, scope, and maturity of a material claim must not exceed the
source, method, relevance, coverage, and limitations of its supporting evidence.
```

### Derived from

```text
Axiom 1;
Axiom 2;
State Attribution;
State–Model Separation.
```

### Decision consequence

A passing build supports a build claim; it does not prove runtime behavior, product acceptance, security, accessibility, or release readiness unless those layers were evaluated.

### Boundaries

```text
perfect evidence is not required before every reversible action;
required evidence strength depends on the claim, risk, and consequence;
exploration may proceed with explicitly weaker claims.
```

### Consumers and cases

```text
#8 evidence primitives;
#9 layered conformance results;
review and completion reporting;
B5 Passing Build Expanded Into Product Completion;
B7 Static Conformance Treated As Behavioral Proof;
B9 Screenshot Treated As Complete UX Validation.
```

---

## 7. Decision Traceability

### Statement

```text
A material engineering decision is trustworthy only to the degree that its
source, authority, scope, rationale, evidence, conflicts, and supersession state
can be traced.
```

### Derived from

```text
Axiom 1;
Axiom 2;
State Attribution;
Claim–Evidence Scope.
```

### Decision consequence

Recency, existence, implementation state, agent confidence, silence, or a review verdict cannot silently establish an effective decision.

### Boundaries

```text
trivial local choices do not require separate architecture records;
record depth grows with impact, persistence, risk, and consumer count;
a traceable decision can still be wrong and remain open to revision.
```

### Consumers and cases

```text
#6 decision and authority model;
Decision Provenance;
review and approval ports;
B4 Tool Permission Without Authority;
B6 Review Verdict Treated As Approval.
```

---

## 8. Capability–Authority Separation

### Statement

```text
The capability or technical permission to perform an action does not by itself
grant authority, approval, accepted scope, or policy right to perform it.
```

### Derived from

```text
Axiom 1;
Axiom 2;
doctrine-level authority boundaries.
```

### Decision consequence

Available repository, runtime, deployment, or administrative access must be checked against the effective decision and applicable policy before material action.

### Boundaries

```text
authority may be delegated explicitly;
low-risk autonomy may be authorized in advance by policy;
interactive approval is not required for every already-authorized operation.
```

### Consumers and cases

```text
#6 capability, permission, and authority relationships;
#7 port authority boundaries;
native-ai-fw control plane;
B4 Tool Permission Without Authority;
B6 Review Verdict Treated As Approval.
```

---

## 9. Execution Capacity

### Statement

```text
Execution scope must not exceed the available context, capability, tools,
permission, authority, risk controls, reversibility, recovery support,
validation path, and review capacity required for that scope.
```

### Derived from

```text
Axiom 1;
Bridge Law;
State Attribution;
Capability–Authority Separation.
```

### Decision consequence

Missing capacity must produce a smaller scope, reversible experiment, route, block, or honest limitation rather than fabricated completion.

### Boundaries

```text
capacity is contextual, not a permanent rating of an actor;
insufficient capacity for full implementation may permit discovery or planning;
the law does not justify indefinite analysis when sufficient capacity exists.
```

### Consumers and cases

```text
#6 capacity model;
workflow routing;
runtime risk controls;
B3 Plan Reported As Execution;
B4 Tool Permission Without Authority;
B9 Screenshot Treated As Complete UX Validation.
```

---

## 10. Coherent Completion

### Statement

```text
A system must not claim completion while unresolved material contradictions remain
between effective intent, requirements, contracts, architecture, implementation,
behavior, evidence, approval, and delivery state inside the claim scope.
```

### Derived from

```text
Axiom 2;
Bridge Law;
Claim–Evidence Scope;
Decision Traceability.
```

### Decision consequence

Completion reports must distinguish completed, partial, blocked, not verified, and accepted-with-limitation states where material.

### Boundaries

```text
perfect global consistency is not required;
non-material differences may remain;
known limitations may be accepted by the required authority;
the law applies only to the stated completion scope.
```

### Consumers and cases

```text
#6 task and lifecycle state model;
#8 status primitives;
release and product acceptance;
B3 Plan Reported As Execution;
B5 Passing Build Expanded Into Product Completion;
B9 Screenshot Treated As Complete UX Validation.
```

---

## 11. Executable Embodiment

### Statement

```text
A principle, rule, contract, skill, or workflow is embodied only when it changes
repeatable executable behavior and that behavior can produce evidence appropriate
to the claim.
```

### Derived from

```text
Axiom 2;
Bridge Law;
Claim–Evidence Scope;
Coherent Completion.
```

### Decision consequence

Documentation, metadata, installation, or declared gates cannot be used as proof that routing, behavior, enforcement, or product outcomes actually occur.

### Boundaries

```text
embodiment does not require perfect execution in every case;
one successful execution is evidence, not final stabilization;
advisory principles may remain qualitatively reviewed rather than runtime-enforced.
```

### Consumers and cases

```text
#9 behavioral conformance;
ai-native-skills#27 runtime harness;
native-ai-fw execution traces;
B7 Static Conformance Treated As Behavioral Proof;
B8 Installed Skill Treated As Applied Skill.
```

---

## 12. Feedback Revision

### Statement

```text
Relevant evidence and feedback must be processed at the affected working layer;
material contradictory feedback may be rejected only with traceable rationale,
scope, and authority.
```

### Derived from

```text
Bridge Law — Feedback And Governed Evolution;
Axiom 2;
Claim–Evidence Scope;
Coherent Completion.
```

### Decision consequence

A failed runtime check, user correction, review finding, regression, or product result must be able to reopen, narrow, revise, retest, or stop the affected claim or implementation.

### Boundaries

```text
feedback is not automatically correct or authoritative;
one result is not final truth;
reasoned traceable rejection can satisfy the law.
```

### Consumers and cases

```text
Development Loop feedback transitions;
review and incident workflows;
product feedback processing;
B10 Contradictory Feedback Ignored.
```

---

## 13. Evolution Authority

### Statement

```text
A more concrete layer may apply, translate, test, and propose changes to a more
canonical layer, but it may not silently redefine that layer without compatibility
review and the required canonical authority.
```

### Derived from

```text
Bridge Law — Feedback And Governed Evolution;
Decision Traceability;
Feedback Revision;
doctrine-level repository ownership.
```

### Decision consequence

A local product fix becomes a learning candidate first. Promotion requires a reusable reason, counterexamples, transferability evidence, correct target-layer selection, compatibility review, and authority.

### Boundaries

```text
bottom-up learning remains required;
core is not immune to evidence;
emergency local fixes may remain local before shared promotion;
the law governs canonicalization, not every local edit.
```

### Consumers and cases

```text
#6 ownership and evolution model;
#7 and #8 compatibility boundaries;
Skill Evolution;
B11 Local Fix Promoted Directly Into Core;
B12 Canonical Semantic Change Without Migration.
```

---

## 14. Cross-Law Invariants

```text
material state claims remain attributable;
representations remain recognizable as representations;
claims remain bounded by evidence;
material decisions remain traceable;
capability remains separate from authority;
action remains inside available capacity;
completion remains honest about contradictions and gaps;
declaration remains separate from behavior;
feedback can revise the affected layer;
local learning cannot silently redefine core.
```

---

## 15. Acceptance Status

```text
Retained law families: 10
Duplicate law pruning: COMPLETE
Kernel derivation: ALIGNED
Boundaries and counterexamples: PRESENT
Named consumers: PRESENT
Behavioral-case mapping: PRESENT
Machine-readable law IDs: NOT REQUIRED BY ISSUE #13
Executable downstream embodiment: FOLLOW-UP VALIDATION
Ready for final contradiction review: YES
```
