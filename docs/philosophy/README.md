# Native AI Engineering Philosophy

Status: Candidate foundation under acceptance review

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

This directory defines the minimal decision and governance foundation below Native AI Engineering domain models, contracts, ports, skills, workflows, adapters, runtimes, and products.

It is not decorative philosophy. A concept remains here only when it changes engineering decisions, prevents a known failure, has a named consumer, and can be embodied or validated.

---

## 1. Practical Purpose

Native AI Engineering gives agents meaningful execution capacity. This foundation exists to make the following behavior systematic:

```text
agents do not invent state that was not inspected;
models and plans are not reported as executed reality;
tool access is not treated as authority;
claims remain proportional to evidence;
completion cannot hide material gaps;
review remains distinct from approval;
feedback can revise the affected layer;
local learning reaches the smallest correct shared layer;
products, adapters, and runtimes cannot silently redefine core.
```

A statement that changes none of these decisions, has no named consumer, and has no embodiment path must be merged, deferred, or removed.

---

## 2. Foundation Map

```text
Philosophy / Doctrine
→ Epistemic Axioms
→ Derived Engineering Laws
→ Principles And Guardrails
→ Canonical Language
→ Domain Model
→ Lifecycle And Capability Taxonomies
→ Contracts And Ports
→ Skills, Workflows, And Adapters
→ Runtime And Product Implementation
→ Evidence, Evaluation, And Approval
→ Learning And Governed Evolution
```

The foundation explains why lower layers exist and which distinctions they must preserve.

It does not absorb detailed domain modeling, schemas, contracts, workflow phases, skill methodology, runtime orchestration, provider configuration, or product policy.

---

## 3. Candidate Doctrine

```text
Native AI Engineering builds systems in which agents can perform meaningful
engineering work while domain authority, source-of-truth knowledge, contracts,
risk boundaries, evidence, and evolution remain explicit and reviewable.

AI increases execution capacity. It does not erase the distinction between
state and model, claim and evidence, execution and authority, review and approval,
or local learning and universal core truth.
```

---

## 4. Candidate Kernel

### Available, Attributable State

```text
Engineering work begins from available, attributable state.
```

Consequences:

```text
inspect before materially claiming or changing;
unavailable state remains unknown, blocked, or not verified;
absence of evidence does not become fabricated evidence;
observation remains bounded by source, access, time, and coverage.
```

### State Is Not Its Model

```text
Observed or recorded state is not identical to a human, agent, document,
or system model of that state.
```

Consequences:

```text
repository state ≠ repository summary;
user intent ≠ inferred intent;
architecture diagram ≠ implementation;
plan ≠ execution;
contract declaration ≠ conformance;
review verdict ≠ approval;
memory ≠ source-of-truth knowledge.
```

Models remain necessary. Their source, scope, assumptions, unknowns, and verification status must remain visible enough for the claim and risk involved.

### Evidence And Feedback Bridge

```text
AI-native engineering systems preserve continuity and update their operational
organization through appropriately scoped evidence and feedback.
```

Consequences:

```text
failed verification can revise implementation;
review feedback can revise a plan or result;
product evidence can create a learning candidate;
one local result cannot silently redefine core;
canonical evolution requires compatibility and authority review.
```

These statements are bounded to Native AI Engineering. They are not universal scientific claims outside the framework.

---

## 5. Retained Laws

Active candidate law authority: [`laws.md`](laws.md)

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

Historical candidates `Model Recognition` and `Governed Stability` were merged or reclassified after usefulness review. References to their old aliases in discovery or earlier candidate material are historical traceability and do not reactivate them as independent laws.

---

## 6. Retained Principles And Guardrails

Classification authority: [`principles-and-guardrails.md`](principles-and-guardrails.md)

### Principles

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

Retired independent principle candidates:

```text
Evidence-Proportional Claims
Explicit Uncertainty
Preserve Useful Existing Work
Feedback-Driven Learning
```

Their useful responsibilities remain preserved by retained laws, guardrails, or other principles.

### Guardrails

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

`Memory Must Not Override Current Source Of Truth` was merged into state-attribution, model-as-fact, and conflict-resolution boundaries rather than retained as a duplicate independent guardrail.

Stable names are the primary identifiers. Historical `L`, `P`, and `G` numbers are traceability aliases while the foundation remains candidate.

---

## 7. Classification Boundary

```text
Law        states a derived invariant.
Principle  guides selection among valid approaches.
Guardrail  defines a mandatory must or must-not boundary.
Mechanism  organizes reusable operation or reasoning.
Gate       controls a transition or claim.
Policy     defines mandatory behavior within named authority and scope.
```

A principle must not silently become a blocker. A mandatory boundary must not be weakened into advice.

Examples:

```text
Smallest Coherent Change
→ principle.

Capability Is Not Authority
→ philosophy guardrail.

Human review by default
→ governance posture or scoped policy.

Run configured checks before a verification claim
→ Development Loop gate.
```

---

## 8. Canonical Language

Atomic philosophy-level term authority: [`term-authority.md`](term-authority.md)

It preserves distinctions including:

```text
state ≠ observation;
observable state ≠ available state;
observation ≠ interpretation;
interpretation ≠ inference;
assumption ≠ fact;
claim ≠ evidence;
fact ≠ authority;
capability ≠ permission;
permission ≠ authority;
decision ≠ effective decision;
review ≠ approval;
verification ≠ validation;
validation ≠ evaluation;
feedback ≠ learning;
learning ≠ core evolution;
stability ≠ immutability;
memory ≠ source-of-truth knowledge.
```

Concrete layers may specialize a term, but they may not reverse its base meaning or create a competing upstream authority.

The repository-wide [`../glossary.md`](../glossary.md) is a navigation index, not a parallel atomic definition source.

---

## 9. Epistemic Loop

Reasoning mechanism: [`epistemic-loop.md`](epistemic-loop.md)

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ READ EVIDENCE
→ UPDATE
```

The loop governs reasoning about state, models, capacity, evidence, and revision. It does not replace delivery workflows or specialist methodology.

```text
SELECT A TESTABLE RESPONSE
≠ execute the response
≠ authorize the response
≠ prove the response succeeded
```

Execution, gates, approval, rollback, and delivery remain owned by the host workflow, skill, runtime, tool operation, or human process.

---

## 10. Usefulness And Embodiment

Usefulness gate: [`traceability-and-usefulness.md`](traceability-and-usefulness.md)

Pruning record: [`reconciliation-and-pruning.md`](reconciliation-and-pruning.md)

Behavioral candidates: [`behavioral-test-candidates.md`](behavioral-test-candidates.md)

Every retained statement must pass:

```text
U1 Decision impact
U2 Failure prevention
U3 Named consumer
U4 Embodiment path
U5 Minimality
U6 Scope discipline
```

Acceptance rule:

```text
No decision impact + no named consumer + no embodiment path
= remove, merge, or defer.
```

Twelve adversarial behavioral cases now test whether consumers preserve state attribution, evidence scope, authority, honest completion, feedback revision, and governed evolution.

They remain specifications, not executable proof. Machine-readable schema, runtime harness, and product validation are still required.

---

## 11. Downstream Consumers

### `ai-native-core#6` — Domain model

Must preserve distinct objects or states for claim, evidence, decision, authority, approval, capacity, feedback, learning, and completion rather than collapsing them into generic records.

### `ai-native-core#7` — Port taxonomy

Must preserve ownership, authorization, evidence production, failure, observability, and compatibility boundaries without treating capability as authority.

### `ai-native-core#8` — Contract schemas

Must define shared primitives for source, scope, coverage, claim, evidence layer, authority, approval, status, boundary, compatibility, supersession, and behavioral-test structure.

### `ai-native-core#9` — Conformance validator

Must keep structural declaration, behavioral execution, runtime integration, product evidence, review, and approval as separate result layers.

### `ai-native-skills`

Must consume relevant behaviors and tests, not copy the philosophy essay into every `SKILL.md`.

### `native-ai-fw`

Must embody state attribution, authority routing, risk controls, execution evidence, completion status, and learning-candidate routing in the control plane.

### Product repositories

Must provide real-world validation, product-specific policy, approval, release, rollback, business evidence, and acceptance criteria without weakening foundation guardrails.

---

## 12. Source-Role Governance

| Artifact role | Owns | Must not become |
|---|---|---|
| Philosophy / Doctrine | Framework purpose and durable orientation | Workflow instructions |
| Axiom | Minimal foundational assumption | Broad principle list |
| Law | Derived invariant | Slogan or local policy |
| Principle | Preferred decision orientation | Hidden mandatory rule |
| Guardrail | Stable must/must-not boundary | Optional advice |
| Canonical Term | One atomic definition | Complete domain model |
| Domain Model | Objects, relationships, ownership, lifecycle | Parallel philosophy |
| Contract | Stable machine-readable agreement | Full executable methodology |
| Skill / Workflow | Executable reusable behavior | Core redefinition |
| Adapter | Contextual binding or translation | Domain authority |
| Implementation Evidence | Bounded observed result | Universal truth |
| Field Test | Real-world validation | Automatic shared promotion |
| Acceptance Review | Readiness, contradiction, and consumer review | New unreviewed foundation content |

---

## 13. Non-Goals

This foundation does not:

```text
copy psychological, spiritual, somatic, therapeutic, religious,
or metaphysical doctrine from Manuscript Kesadaran;

claim universal scientific truth beyond Native AI Engineering;

select a provider, runtime, framework, repository host,
deployment platform, or product architecture;

replace domain-driven design, ports and adapters, contracts,
skills, workflows, evaluation, or product validation;

make every principle mandatory for every consumer;

make every feedback item eligible for core promotion;

create a second delivery workflow;

use terminology or document volume as a maturity signal.
```

`puterakahfi/manuscript-kesadaran/core` is an architectural reference for foundation discipline and source-role separation, not a Native AI Engineering domain dependency.

---

## 14. Current Maturity

```text
Canonical philosophy entry point: ESTABLISHED
Doctrine wording: CANDIDATE
Axiom set: CANDIDATE
Bridge law: CANDIDATE
Retained laws: 10 CANDIDATES
Retained principles: 7 CANDIDATES
Retained philosophy guardrails: 14 CANDIDATES
Law pruning: COMPLETE
Principle and guardrail pruning: COMPLETE
Canonical philosophy terms: DEFINED FOR CANDIDATE REVIEW
Epistemic Loop: FORMALIZED FOR CANDIDATE REVIEW
Usefulness gate: ESTABLISHED
Architecture reconciliation: APPLIED
Glossary reconciliation: APPLIED
Behavioral test candidates: 12 DEFINED
Machine-readable behavioral schema: NOT YET DEFINED
Executable behavioral harness: NOT YET IMPLEMENTED
Runtime and product embodiment: NOT YET PROVEN
Domain model consumption readiness: PARTIAL
Ready to merge into main: NO
```

---

## 15. Acceptance Gates

Issue `#13` must not be accepted until:

- [x] doctrine, axioms, bridge law, and derivation rules exist;
- [x] derived laws include boundaries, consequences, and consumers;
- [x] duplicate law candidates are pruned;
- [x] duplicate principles and guardrails are pruned;
- [x] principles, guardrails, mechanisms, gates, and policies are distinguished;
- [x] retained guardrails identify operational responses;
- [x] canonical philosophy-level terms and authority rules exist;
- [x] the Epistemic Loop is distinct from execution workflows;
- [x] usefulness and traceability gates exist;
- [x] glossary and architecture authority conflicts are reconciled;
- [x] representative behavioral test candidates exist;
- [x] behavioral candidates use retained stable foundation names;
- [ ] root repository navigation links to this entry point;
- [ ] issue `#8` confirms machine-readable behavioral-test schema direction;
- [ ] `ai-native-skills#27` maps representative candidates into an executable harness;
- [ ] `native-ai-fw` identifies runtime authority and evidence cases;
- [ ] at least one product repository validates representative cases;
- [ ] stale cross-document aliases are reviewed as historical or replaced;
- [ ] issue `#6` confirms the foundation is sufficient for domain modeling;
- [ ] final contradiction and minimality review passes;
- [ ] issue `#13` records explicit acceptance or requested revision.

Until these gates pass, this entry point is authoritative for navigation and status, while the doctrine and kernel remain candidate foundation content.
