# Native AI Engineering Philosophy — Usefulness And Traceability

Status: Final candidate acceptance gate

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

This document answers one question:

```text
What does the philosophy change in real engineering work?
```

The foundation is not accepted because it is comprehensive or elegant. It is accepted only when it changes decisions, prevents known failures, names consumers, and has an embodiment path.

---

## 1. Usefulness Gate

Every retained concept must pass:

| Gate | Question |
|---|---|
| U1 Decision impact | Does this change a material engineering decision? |
| U2 Failure prevention | Which recurring failure does it prevent? |
| U3 Named consumer | Which issue, contract, skill, runtime, review, or product consumes it? |
| U4 Embodiment path | How can it change repeatable behavior or review evidence? |
| U5 Minimality | Is it the smallest retained concept producing this result? |
| U6 Scope discipline | Is it universal to Native AI Engineering rather than a local policy? |

Acceptance rule:

```text
no decision impact
+ no named consumer
+ no embodiment path
= remove, merge, or defer.
```

Stop or simplify when:

```text
new terminology adds no decision value;
a distinction has no consumer;
a principle duplicates a law or guardrail;
a mechanism becomes a second delivery workflow;
a repository or product policy is being universalized;
document volume grows faster than executable impact.
```

---

## 2. Concrete Failure Classes

| Failure | Foundation response | Practical decision change |
|---|---|---|
| Invented repository, issue, runtime, or test state | State Attribution; No Fabricated State Or Evidence | Inspect, request source, narrow, or mark unknown/not verified |
| Assumption reported as root cause | State–Model Separation; No Model-As-Fact Collapse | Label inference and select a discriminating test |
| Plan reported as completed work | State–Model Separation; Execution Capacity; No False Completion | Separate planning from execution and report the blocked surface |
| Tool access treated as authority | Capability–Authority Separation; High-Risk Actions Require Controls | Route, request authority, choose safe alternative, or stop |
| Build or screenshot reported as complete product proof | Claim–Evidence Scope; Coherent Completion | Narrow the claim and name unverified evidence layers |
| Review treated as approval | Decision Traceability; Capability Is Not Authority | Preserve review verdict while keeping approval pending |
| Contract or skill presence treated as behavior | Executable Embodiment; Declaration Is Not Embodiment | Require behavioral or runtime evidence |
| Contradictory runtime evidence ignored | Feedback Revision | Reopen, revise, retest, narrow, or reject with rationale |
| Local fix promoted directly to core | Evolution Authority; Correct-Layer Change | Create learning candidate and review transferability |
| Canonical meaning changes silently | No Silent Semantic Evolution | Require compatibility, migration, supersession, validation, and authority |

Representative adversarial cases are defined in [`behavioral-test-candidates.md`](behavioral-test-candidates.md).

---

## 3. Downstream Consumer Matrix

### `ai-native-core#6` — Canonical domain model

Must preserve distinct relationships for:

```text
state and observation;
model, interpretation, inference, assumption, and fact;
claim and evidence;
decision, effective decision, authority, and approval;
capability, permission, and capacity;
feedback, learning candidate, and accepted evolution;
partial, blocked, not-verified, and completed states.
```

Expected impact:

```text
one generic status field cannot represent every epistemic and lifecycle state;
evidence is not an untyped output blob;
approval is not a review boolean;
capability does not imply authority;
learning cannot mutate canonical definitions directly.
```

Verdict: `DIRECT CONSUMER — REQUIRED`.

### `ai-native-core#7` — Port taxonomy

Must preserve:

```text
ownership boundary;
request and response scope;
permission and authority expectations;
risk and reversibility;
observability and evidence production;
unsupported claims and errors;
consumer compatibility.
```

Verdict: `DIRECT CONSUMER — AFTER #6`.

### `ai-native-core#8` — Schemas

Must define shared primitives for:

```text
source, scope, coverage, claim, and evidence;
verification and validation targets;
authority and approval;
unknown, partial, blocked, and not-checkable semantics;
boundary ownership and delegation;
compatibility and supersession;
behavioral-test requests and results.
```

Verdict: `DIRECT CONSUMER — AFTER #6/#7`.

### `ai-native-core#9` — Conformance validator

Must keep these result layers separate:

```text
contract identity and version resolution;
structural declaration;
boundary consistency;
behavioral execution;
runtime integration;
product acceptance;
review;
approval.
```

`CONFORMANT`, `PASS`, and `product validated` must not become synonyms.

Verdict: `DIRECT CONSUMER — REQUIRED`.

### `ai-native-skills`

Consumes behaviors such as:

```text
inspect before claiming;
mark assumptions and unknowns;
assess capacity and authority;
report completion proportionally to evidence;
promote learning only to the correct layer;
run adversarial behavioral cases.
```

It must not copy the philosophy essay into every `SKILL.md`.

Verdict: `EXECUTABLE CONSUMER — FOLLOW-UP EMBODIMENT`.

### `native-ai-fw`

Consumes:

```text
source and state records;
capability, permission, and authority separation;
approval routing;
risk and recovery controls;
execution evidence;
honest completion status;
learning-candidate routing.
```

Verdict: `RUNTIME CONSUMER — FOLLOW-UP EMBODIMENT`.

### Product repositories

Own product-specific:

```text
risk and approval policy;
release and rollback;
product acceptance;
business evidence;
field validation;
product learning.
```

Products may strengthen but not silently weaken foundation guardrails.

Verdict: `FIELD VALIDATION CONSUMER — FOLLOW-UP`.

---

## 4. Existing Source Traceability

| Existing source | Foundation relationship | Action |
|---|---|---|
| Root `README.md` | Repository navigation and ownership | Philosophy entry added |
| `docs/architecture-v0.2.md` | Operational architecture consuming foundation | Reconciled; no longer competing hierarchy |
| `docs/domain-driven-model.md` | Capability before tools and domain ownership | Preserve; consume accepted kernel through #6 |
| `docs/development-loop.md` | Execution mechanism and feedback transitions | Preserve; Epistemic Loop remains distinct |
| Development Loop contract | Machine authority for phases and gates | Unchanged |
| `docs/adapter-conformance.md` | Layered evidence and declaration-versus-behavior | Preserve and align through #9 |
| Decision Provenance | Source, authority, conflict, and supersession | Preserve; align primitives through #6/#8 |
| Skill Evolution | Learning candidate and governed promotion | Preserve; executable proof through skills#27 |
| `docs/memory-vs-knowledge.md` | Memory is retrieval aid, not current authority | Preserve |
| `docs/glossary.md` | Repository navigation | Reconciled as index, not atomic authority |
| `rules/README.md` | Operational must/must-not constraints | Preserve as specialization |
| `CONTRIBUTING.md` | Correct-layer and compatibility governance | Preserve; link foundation where useful |

---

## 5. Contradictions Resolved

```text
“Engineering begins from observable/available state”
→ material claims and actions begin from attributable observations
  or explicit unknowns concerning relevant state.

“Observed state is not its model”
→ no observation or model is identical to the state it represents.

“Systems update their operational organization”
→ relevant feedback is processed at the affected layer;
  shared/canonical change requires compatibility review and authority.

“Domain is stable”
→ canonical agreements remain stable through governed change.

“Human-reviewed by default”
→ review and approval depth follows risk, reversibility, authority,
  consumer impact, and policy.

“Evaluation happens before every action”
→ applicable evidence, evaluation, review, and approval gates follow
  the claim, action, risk, contract, and policy.

“Always push after commit”
→ repository/team policy, not universal philosophy.

“Documentation-only work may skip Verify and Review”
→ a shortcut may reduce checks but cannot bypass evidence appropriate
  to the claim or authority review for canonical semantic change.
```

---

## 6. Acceptance Boundary

Issue `#13` accepts the foundation when its own documentation and governance criteria pass.

It does **not** wait for:

```text
complete #6 domain implementation;
#7 port taxonomy implementation;
#8 schemas;
#9 validator v2;
ai-native-skills runtime harness;
native-ai-fw enforcement;
product field proof.
```

Those are downstream embodiment and validation responsibilities. They remain required before claiming the philosophy is embodied by those consumers.

---

## 7. Acceptance Checklist

- [x] practical purpose and recurring failure classes are explicit;
- [x] usefulness and minimality gates are defined;
- [x] retained laws, principles, and guardrails have named consumers;
- [x] representative adversarial behavioral cases exist;
- [x] domain, port, schema, validator, skill, runtime, and product consumers are mapped;
- [x] architecture and glossary competition is reconciled;
- [x] local policy remains outside universal philosophy;
- [x] state-versus-observation contradiction is resolved;
- [x] foundation acceptance is separated from downstream embodiment;
- [ ] relative links receive final branch-level review;
- [ ] issue `#6` receives the final accepted input package;
- [ ] owner records acceptance or requested revision.

---

## 8. Current Verdict

```text
Philosophy purpose: PRACTICAL DECISION AND GOVERNANCE KERNEL
Decorative philosophy accepted: NO
Usefulness gate: PASSED FOR RETAINED SET
Direct core consumers: #6, #7, #8, #9
Executable consumers: ai-native-skills, native-ai-fw, products
Contradiction review: SUBSTANTIALLY COMPLETE
Minimality review: PASSED AFTER PRUNING AND COMPACTION
Downstream embodiment: FOLLOW-UP, NOT #13 ACCEPTANCE BLOCKER
Ready for final link review and #6 handoff: YES
```
