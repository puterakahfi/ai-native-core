# Native AI Engineering Philosophy — Reconciliation And Pruning Record

Status: Candidate acceptance review record

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Usefulness gate: [`traceability-and-usefulness.md`](traceability-and-usefulness.md)

This document records candidate concepts that were merged, reclassified, or retained during usefulness and contradiction review.

It is a decision record, not a competing philosophy authority.

---

## 1. Pruning Rule

A candidate is retained only when it has:

```text
a distinct decision consequence;
a known failure class it prevents;
a named downstream consumer;
a plausible embodiment or validation path;
no smaller retained concept that produces the same result.
```

The following are not sufficient:

```text
sounds correct;
reads elegantly;
completes a diagram;
resembles another framework;
has already been documented at length.
```

---

## 2. Law Decisions

## Model Recognition — MERGED

Historical alias:

```text
L3
```

Useful responsibility:

```text
unmarked inference, assumption, hypothesis, or interpretation may be consumed
and executed as verified fact.
```

Merged into:

```text
State–Model Separation;
No Model-As-Fact Collapse;
canonical inference, assumption, fact, and verification terms;
Epistemic Loop DECOMPOSE phase.
```

Reason:

The failure is important, but it does not create a distinct invariant beyond State–Model Separation. Its consumers need explicit epistemic status, not another independent law.

Decision:

```text
NOT RETAINED AS INDEPENDENT LAW
```

---

## Governed Stability — RECLASSIFIED AND MERGED

Historical alias:

```text
L12
```

Useful responsibility:

```text
stable artifacts preserve reliable consumer expectations through ownership,
compatibility, evidence, review, and controlled evolution;
stability is not immutability.
```

Merged into:

```text
Evolution Authority;
Evaluation Before Trust Expansion;
No Silent Semantic Evolution;
canonical Stability definition;
contract compatibility, migration, and release policy.
```

Reason:

The distinction is necessary, but its engineering consequences are already owned by evolution authority, trust-expansion decisions, semantic guardrails, and compatibility mechanisms.

Decision:

```text
NOT RETAINED AS INDEPENDENT LAW
```

---

## Retained Laws

```text
State Attribution
State–Model Separation
Claim–Evidence Scope
Decision Traceability
Capability–Authority Separation
Execution Capacity
Coherent Completion
Executable Embodiment
Feedback Revision
Evolution Authority
```

Count:

```text
10 retained candidate laws
```

Active compaction is complete in [`laws.md`](laws.md). Historical reasoning remains in discovery and this record.

---

## 3. Principle Decisions

## Evidence-Proportional Claims — MERGED

Historical alias:

```text
P3
```

Merged into:

```text
Claim–Evidence Scope;
No Claim Beyond Evidence Scope;
Coherent Completion.
```

Reason:

This is a mandatory truthfulness boundary, not an optional selection orientation.

---

## Explicit Uncertainty — MERGED

Historical alias:

```text
P4
```

Merged into:

```text
State Attribution;
State–Model Separation;
No Fabricated State Or Evidence;
No Model-As-Fact Collapse;
Epistemic Loop OBSERVE and DECOMPOSE phases.
```

Reason:

Material uncertainty must remain visible; it is not merely a preferred style.

---

## Preserve Useful Existing Work — ABSORBED

Historical alias:

```text
P7
```

Absorbed into:

```text
Smallest Coherent Change
```

Reason:

Preserving correct accepted work is a selection factor for coherent change, not a separate principle with a distinct decision surface.

---

## Feedback-Driven Learning — MERGED

Historical alias:

```text
P10
```

Merged into:

```text
Feedback Revision;
Evolution Authority;
Epistemic Loop UPDATE phase.
```

Reason:

Feedback revision is already an invariant. Shared promotion is already governed by evolution authority. Another advisory principle adds no distinct selection behavior.

---

## Retained Principles

```text
Domain And Capability Before Tools
Smallest Coherent Change
Reversible Progress Under Uncertainty
Correct-Layer Change
Evaluation Before Trust Expansion
Review Proportional To Risk And Authority
Explicit Boundaries Over Implicit Expectations
```

Count:

```text
7 retained candidate principles
```

---

## 4. Guardrail Decisions

## Memory Must Not Override Current Source Of Truth — MERGED

Historical alias:

```text
G13
```

Merged into:

```text
No Fabricated State Or Evidence;
No Model-As-Fact Collapse;
No Silent Conflict Resolution;
State Attribution;
Decision Traceability.
```

Reason:

Memory is one model and retrieval surface. When stale or conflicting memory appears, the required behavior is already to verify current sources, preserve epistemic status, and avoid silently resolving authority conflicts.

A separate guardrail produces no distinct trigger or response.

Decision:

```text
NOT RETAINED AS INDEPENDENT GUARDRAIL
```

---

## Retained Guardrails

```text
No Fabricated State Or Evidence
No Model-As-Fact Collapse
No Claim Beyond Evidence Scope
Capability Is Not Authority
No Silent Scope Expansion
No Silent Conflict Resolution
No Undeclared Gate Bypass
No False Completion
Declaration Is Not Embodiment
Contradictory Feedback Must Be Processed
No Unverified Promotion To Shared Layers
Concrete Layers Must Not Redefine Canonical Layers
High-Risk Actions Require Applicable Controls
No Silent Semantic Evolution
```

Count:

```text
14 retained candidate philosophy guardrails
```

Each retained guardrail now has:

```text
protected boundary;
required operational response;
representative behavioral-case mapping;
named consumer surface.
```

---

## 5. Reconciliation Applied

## `docs/architecture-v0.2.md`

Applied:

```text
classified as an operational architecture view;
linked to philosophy authority;
clarified that layer sequence is not universal numbering authority;
replaced immutable-stability wording with governed-change wording;
reclassified human review as bounded posture or policy;
separated evaluation, review, and approval;
separated capability from authority;
marked product examples as illustrative.
```

Preserved:

```text
domain-first architecture;
ports-and-adapters boundaries;
replaceable tools and providers;
agent non-ownership of domain decisions;
knowledge versus memory;
contract, rule, skill, and evaluation responsibilities.
```

## `docs/glossary.md`

Applied:

```text
reclassified as navigation index;
linked philosophy terms to term-authority.md;
removed competing layer numbering;
removed runtime-specific Profile from core terminology;
expanded Capability beyond skill declarations;
made Conformance evidence-layered;
broadened Verification beyond command execution;
distinguished Review, Approval, Permission, and Authority.
```

## Executable contracts

No machine-readable contract was modified during philosophy reconciliation.

```text
existing contracts remain operational authority;
terminology migration belongs to issues #6, #7, #8, and #9;
document reconciliation must not silently mutate executable semantics.
```

---

## 6. Behavioral Alignment

[`behavioral-test-candidates.md`](behavioral-test-candidates.md) now uses retained stable law, principle, and guardrail names.

Twelve cases cover:

```text
invented repository state;
assumption-as-fact;
plan-as-execution;
tool permission without authority;
build-as-product-completion;
review-as-approval;
static conformance as behavior;
installed skill as applied skill;
screenshot as complete UX proof;
contradictory feedback ignored;
local fix promoted directly to core;
canonical semantic change without migration.
```

These cases remain specifications until schemas and executable consumers exist.

---

## 7. Alias Policy

Stable names are the primary candidate identifiers.

Historical aliases remain only for traceability:

```text
L1–L12
P1–P11
G1–G15
```

A reference to a retired alias in discovery or an earlier candidate document does not reactivate that item as independent authority.

Before final acceptance, active navigation and behavioral specifications must use stable names. Historical records may preserve aliases when their role is explicit.

---

## 8. Remaining Acceptance Blockers

```text
root repository navigation must link the philosophy entry point;
issue #8 must confirm behavioral-test schema direction;
ai-native-skills#27 must map representative cases into an executable harness;
native-ai-fw must identify runtime authority and evidence cases;
at least one product repository must validate representative behavior;
issue #6 must confirm domain-model sufficiency;
final contradiction and minimality review must pass;
explicit owner acceptance must be recorded in issue #13.
```

---

## 9. Current Verdict

```text
Decorative-concept policy: REJECTED
Retained candidate laws: 10
Retired independent laws: 2
Retained candidate principles: 7
Retired independent principles: 4
Retained candidate guardrails: 14
Retired independent guardrails: 1
Architecture reconciliation: APPLIED
Glossary reconciliation: APPLIED
Active artifact compaction: APPLIED
Behavioral stable-name mapping: APPLIED
Executable contract changes: NONE
Executable embodiment: NOT YET PROVEN
Ready for final contradiction review: YES
Ready to merge philosophy: NO
```
