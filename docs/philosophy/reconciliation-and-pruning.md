# Native AI Engineering Philosophy — Reconciliation And Pruning Record

Status: Candidate acceptance review record

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Usefulness gate: [`traceability-and-usefulness.md`](traceability-and-usefulness.md)

This document records decisions made during reconciliation and pruning.

It is not a new philosophy authority. It explains which candidate concepts remain useful, which are merged or reclassified, which existing documents were reconciled, and what still blocks acceptance.

---

## 1. Pruning Rule

A candidate foundation concept is retained only when it has:

```text
a distinct decision consequence;
a known failure class it prevents;
a named downstream consumer;
a plausible embodiment or validation path;
no smaller existing concept that produces the same result.
```

The following is not sufficient:

```text
sounds correct;
reads elegantly;
fits the architecture diagram;
adds conceptual completeness;
resembles another framework;
has already been documented at length.
```

---

## 2. Law Pruning Decisions

### 2.1 L3 Model Recognition — MERGE

Previous candidate responsibility:

```text
Unmarked inference, assumption, hypothesis, or interpretation may be consumed and
executed as if it were fact.
```

Review result:

```text
MERGE INTO:
- L2 State–Model Separation Law;
- G2 No Model-As-Fact Collapse;
- canonical terms for inference, assumption, fact, and epistemic status;
- Epistemic Loop DECOMPOSE phase.
```

Reason:

L3 describes an important failure, but it does not establish a distinct invariant beyond L2. Its executable consequence is already expressed more precisely as:

```text
models and material statements preserve source, scope, assumptions,
unknowns, and verification status;

inference and assumption must not be reported or executed as verified fact;

material epistemic status must remain explicit when consequence, reuse,
risk, or irreversibility is significant.
```

Named consumers remain:

```text
issue #6 epistemic state model;
issue #8 source/status primitives;
ai-native-skills analysis and planning behavior;
behavioral tests for assumption-as-fact failures.
```

These consumers do not require L3 to remain a separate law.

Decision:

```text
L3 is not retained as an independent law in the candidate accepted kernel.
Its useful requirements remain preserved by L2, G2, term authority, and the loop.
```

### 2.2 L12 Governed Stability — RECLASSIFY AND MERGE

Previous candidate responsibility:

```text
Stable artifacts preserve reliable consumer expectations through ownership,
compatibility, evidence, review, and controlled evolution; stability is not immutability.
```

Review result:

```text
MERGE INTO:
- L11 Evolution Authority Law;
- P8 Evaluation Before Trust Expansion;
- G15 No Silent Semantic Evolution;
- canonical term Stability;
- contract compatibility and release policy.
```

Reason:

The distinction `stability ≠ immutability` is necessary, but it functions primarily as:

```text
a canonical definition boundary;
a decision principle for trust expansion;
a mandatory semantic-evolution guardrail;
a contract and release governance concern.
```

It does not require another independent law once L11 already governs how accepted shared artifacts evolve.

Named consumers remain:

```text
issue #6 ownership and lifecycle model;
issue #7 port compatibility;
issue #8 contract versioning and migration;
issue #9 compatibility-aware conformance;
repository release and supersession policy.
```

Decision:

```text
L12 is not retained as an independent law in the candidate accepted kernel.
Its useful requirements remain preserved by L11, P8, G15, Stability, and compatibility policy.
```

---

## 3. Retained Candidate Law Families

After the first pruning pass, the retained candidate law families are:

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
10 retained candidate law families
```

The current [`laws.md`](laws.md) still contains the original candidate numbering and the two reviewed sections for traceability.

Before issue `#13` acceptance, `laws.md` must be compacted so:

```text
merged candidates are removed from the active law list;
remaining references use consistent numbering or stable names;
cross-law invariants reflect the retained set;
stress-test references no longer cite merged laws;
current verdict reports the pruned count.
```

Historical candidate reasoning may remain in the discovery or reconciliation record, not in the active canonical law list.

---

## 4. Principle And Guardrail Pruning Position

### Principles

The eleven candidate principles remain under review, but they are not intended to become a universal checklist copied into every skill or workflow.

Consumer rule:

```text
A consumer selects only principles that materially change its decisions.
```

A principle should be merged when:

```text
it produces no distinct choice;
it restates a law without decision guidance;
it duplicates another principle's selection factors;
it is actually a local policy.
```

### Guardrails

Guardrails may remain separate when they trigger different operational responses, such as:

```text
BLOCK;
NARROW;
ROUTE;
REQUEST AUTHORITY;
REQUEST EVIDENCE;
DOWNGRADE STATUS;
REVERT;
ESCALATE.
```

Guardrails should be merged when the protected invariant, trigger, and required response are materially identical.

No final principle or guardrail count is frozen by this record.

---

## 5. Canonical Term Scope

The 39 candidate atomic terms are not 39 slogans that every agent must recite.

They serve different purposes:

```text
foundation-required distinctions;
domain-model inputs;
contract-schema primitives;
review and evidence vocabulary;
supporting navigation terms.
```

Consumers should import only the vocabulary relevant to their responsibility.

Examples:

```text
A repository-analysis skill needs observation, inference, assumption, fact,
claim, evidence, scope, coverage, and verification.

A destructive-operation control plane needs capability, permission, authority,
effective decision, approval, capacity, reversibility, and evidence.

A conformance validator needs contract, claim, evidence layer, conformance,
verification, not-checkable, behavior-not-verified, and product acceptance boundaries.
```

Term count alone is not a maturity signal. Terms remain subject to merge when they do not preserve a necessary distinction for a named consumer.

---

## 6. Reconciliation Applied

### 6.1 `docs/architecture-v0.2.md`

Applied changes:

```text
classified as an operational architecture view;
linked to the philosophy foundation;
clarified that its layer sequence is not universal numbering authority;
replaced “domain is stable” with governed-stability wording;
reclassified “human-reviewed by default” as bounded governance posture/policy;
made evaluation, review, and approval proportional to claim, risk, and authority;
made contract presence distinct from executable behavior and product proof;
made capability distinct from authority;
marked the product section as illustrative rather than canonical domain authority.
```

Preserved:

```text
domain-first architecture;
ports-and-adapters boundary;
replaceable providers and tools;
agent non-ownership of domain decisions;
knowledge versus memory distinction;
contract, rule, skill, and evaluation responsibilities.
```

### 6.2 `docs/glossary.md`

Applied changes:

```text
reclassified as a navigation index;
linked philosophy-level definitions to term-authority.md;
removed competing architecture layer numbering from term definitions;
removed runtime-specific Profile as a core glossary concept;
expanded Capability beyond skill-contract declarations;
made Conformance explicitly evidence-layered;
broadened Verification beyond command execution;
distinguished Review from Approval;
distinguished Permission from Authority;
added navigation for evidence, feedback, capacity, coherence, embodiment,
learning candidate, stability, and source of truth.
```

Preserved:

```text
contract and adapter navigation;
Development Loop discovery;
skill, workflow, runtime, manifest, and port terminology;
repository-oriented usability.
```

### 6.3 Executable contracts

No machine-readable contract was modified in this slice.

Reason:

```text
existing contracts remain operational authority;
terminology changes must be coordinated with issues #6, #7, #8, and #9;
document reconciliation must not silently mutate executable semantics.
```

---

## 7. Contradictions Resolved In This Slice

```text
“Domain is stable”
→ canonical domain agreements are stable through governed change.

“Human-reviewed by default”
→ review and approval are proportionate to risk and authority;
  human review may be a bounded policy default.

“Evaluation before every approval/export/deploy/publish”
→ applicable evidence, evaluation, review, and approval gates follow
  the claim, action, risk, authority, contract, and policy.

Glossary Capability = skill contract declaration
→ capability applies to actors, agents, tools, adapters, and systems.

Glossary Conformance = one coverage result
→ conformance must name its evidence layer.

Glossary Verification = run real commands
→ verification evaluates any specified claim against appropriate evidence;
  command execution is one method.

Architecture layer numbering = universal framework hierarchy
→ architecture v0.2 is one operational dependency view.
```

---

## 8. Remaining Acceptance Blockers

Issue `#13` remains blocked from acceptance until:

```text
laws.md is compacted to the retained law set;
principles and guardrails complete duplicate-response review;
philosophy README navigation and maturity status are updated;
root README links to the philosophy entry point;
behavioral test candidates are defined for executable embodiment;
issue #6 confirms the vocabulary supports domain modeling;
contract terminology impact is reviewed with #7, #8, and #9;
document links and cross-references pass review;
explicit owner acceptance is recorded.
```

---

## 9. Current Verdict

```text
Decorative-concept policy: REJECTED
L3 Model Recognition: MERGED, NOT RETAINED AS LAW
L12 Governed Stability: RECLASSIFIED, NOT RETAINED AS LAW
Retained candidate law families: 10
Architecture reconciliation: APPLIED
Glossary authority reconciliation: APPLIED
Executable contract changes: NONE
Active law-file compaction: PENDING
Principle/guardrail pruning: PENDING
Behavioral embodiment: PENDING
Ready to merge philosophy: NO
Ready for compaction and behavioral-test design: YES
```

The next slice should compact the active philosophy artifacts around the retained kernel, update navigation and maturity status, and define representative behavioral tests proving that the foundation changes agent behavior rather than merely documenting intent.