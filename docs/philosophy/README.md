# Native AI Engineering Philosophy

Status: Final candidate ready for owner acceptance

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

This directory defines the minimal decision and governance foundation below Native AI Engineering domain models, contracts, ports, skills, workflows, adapters, runtimes, and products.

It is not decorative philosophy. A concept belongs here only when it changes a material engineering decision, prevents a known failure, has a named consumer, and has an embodiment or validation path.

---

## 1. Practical Purpose

Native AI Engineering gives agents meaningful execution capacity. The foundation exists to make these behaviors systematic:

```text
state is inspected or left explicitly unknown;
models and plans are not reported as executed reality;
tool access is not treated as authority;
claims remain proportional to evidence;
review remains distinct from approval;
completion cannot hide material gaps;
feedback can revise the affected layer;
local learning reaches the smallest correct shared layer;
products, adapters, and runtimes cannot silently redefine core.
```

If a statement does not change one of these decisions or another named downstream behavior, merge, defer, or remove it.

---

## 2. Candidate Doctrine

```text
Native AI Engineering builds systems in which agents can perform meaningful
engineering work while domain authority, source-of-truth knowledge, contracts,
risk boundaries, evidence, and evolution remain explicit and reviewable.

AI increases execution capacity. It does not erase the distinction between
state and representation, claim and evidence, capability and authority,
review and approval, or local learning and canonical change.
```

---

## 3. Candidate Kernel

### Axiom 1 — Attributable Observation

```text
Material engineering claims and actions begin from attributable observations
or explicit unknowns concerning relevant state.
```

Boundaries:

```text
not all relevant state is observable or available;
source attribution does not imply authority or correctness;
missing state remains unknown, unavailable, blocked, or not verified;
assumptions may support reversible exploration but not fabricated fact.
```

### Axiom 2 — State–Representation Separation

```text
No observation or model is identical to the state it represents.
```

Boundaries:

```text
representations may be reliable and action-guiding;
useful abstraction remains necessary;
source, scope, assumptions, unknowns, and verification status stay visible
when material to the claim or action.
```

### Bridge Law — Feedback And Governed Evolution

```text
Relevant evidence and feedback must be processed at the affected layer;
changes to shared or canonical agreements require proportionate compatibility
review and authority.
```

This allows failed verification, review findings, runtime behavior, and product evidence to revise work without allowing one local result to redefine core silently.

These statements are bounded to Native AI Engineering. They are not claims of universal science.

---

## 4. Foundation Authorities

| Responsibility | Authority |
|---|---|
| Retained derived laws | [`laws.md`](laws.md) |
| Retained principles and guardrails | [`principles-and-guardrails.md`](principles-and-guardrails.md) |
| Atomic philosophy terms | [`term-authority.md`](term-authority.md) |
| Cross-domain reasoning mechanism | [`epistemic-loop.md`](epistemic-loop.md) |
| Behavioral failure cases | [`behavioral-test-candidates.md`](behavioral-test-candidates.md) |
| Usefulness and downstream traceability | [`traceability-and-usefulness.md`](traceability-and-usefulness.md) |
| Pruning and contradiction record | [`reconciliation-and-pruning.md`](reconciliation-and-pruning.md) |
| Repository term navigation | [`../glossary.md`](../glossary.md) |
| Operational architecture view | [`../architecture-v0.2.md`](../architecture-v0.2.md) |

Discovery and audit documents preserve history; they do not compete with active authorities.

---

## 5. Retained Sets

### Laws — 10

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

### Principles — 7

```text
Domain And Capability Before Tools
Smallest Coherent Change
Reversible Progress Under Uncertainty
Correct-Layer Change
Evaluation Before Trust Expansion
Review Proportional To Risk And Authority
Explicit Boundaries Over Implicit Expectations
```

### Philosophy guardrails — 14

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

Consumers select only the items relevant to their owned decisions and failure boundaries. These lists must not be copied wholesale into every skill or workflow.

---

## 6. Epistemic Loop

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ host mechanism executes or routes
→ READ EVIDENCE
→ UPDATE
```

The loop governs reasoning about state, models, capacity, evidence, and revision.

```text
SELECT A TESTABLE RESPONSE
≠ execute the response
≠ authorize the response
≠ prove the response succeeded
```

Execution phases, gates, approvals, rollback, and delivery remain owned by the host workflow, skill, runtime, tool operation, policy, or human process.

---

## 7. Source-Role Governance

| Artifact role | Owns | Must not become |
|---|---|---|
| Philosophy / Doctrine | Purpose and durable orientation | Workflow instructions |
| Axiom | Minimal foundational assumption | Broad principle list |
| Law | Derived invariant | Slogan or local policy |
| Principle | Preferred decision orientation | Hidden mandatory rule |
| Guardrail | Universal must or must-not boundary | Optional advice |
| Canonical Term | One atomic definition | Complete domain model |
| Domain Model | Objects, relationships, ownership, lifecycle | Parallel philosophy |
| Contract | Stable machine-readable agreement | Full methodology |
| Skill / Workflow | Executable reusable behavior | Core redefinition |
| Adapter | Contextual binding or translation | Domain authority |
| Implementation Evidence | Bounded observed result | Universal truth |
| Field Test | Real-world validation | Automatic shared promotion |
| Acceptance Review | Readiness and contradiction review | New unreviewed foundation content |

---

## 8. Downstream Consumers

### `ai-native-core#6`

Define domain objects and lifecycle relationships without collapsing claim, evidence, decision, authority, approval, capacity, feedback, learning, and completion into generic status records.

### `ai-native-core#7`

Define capability and port boundaries while preserving ownership, authorization, evidence, observability, failure, and compatibility semantics.

### `ai-native-core#8`

Define shared schema primitives and machine-readable behavioral-test structure.

### `ai-native-core#9`

Keep path/version resolution, structural declaration, behavioral execution, runtime integration, product evidence, review, and approval as separate result layers.

### `ai-native-skills`

Consume relevant behavior, procedures, and tests rather than copying philosophy prose into every skill.

### `native-ai-fw`

Embody state attribution, authority routing, risk controls, execution evidence, honest completion status, and learning-candidate routing in the control plane.

### Product repositories

Provide product-specific policy, approval, release, rollback, business evidence, and real-world acceptance without weakening foundation guardrails.

---

## 9. Acceptance Boundary

Issue `#13` accepts the foundation itself. It does not wait for every downstream implementation.

Foundation acceptance requires:

```text
minimal internally consistent kernel;
retained laws, principles, and guardrails;
canonical term ownership;
epistemic-loop separation from delivery workflows;
source-role governance;
architecture and glossary reconciliation;
cross-domain negative cases;
contradiction and minimality review;
documentation navigation and relative-link review;
accepted terminology delivered to issue #6;
explicit owner acceptance.
```

Future embodiment remains separately accountable:

```text
#6 domain objects;
#7 port taxonomy;
#8 schemas;
#9 validator behavior;
ai-native-skills executable harness;
native-ai-fw runtime enforcement;
product field validation.
```

A downstream consumer must not claim embodiment before it has executable evidence.

---

## 10. Non-Goals

This foundation does not:

```text
copy spiritual, psychological, somatic, therapeutic, religious,
or metaphysical doctrine from Manuscript Kesadaran;

select a model provider, runtime, repository host, deployment platform,
or product architecture;

replace domain-driven design, ports and adapters, contracts, skills,
workflows, evaluation, or product validation;

make every principle mandatory for every consumer;

make every feedback item eligible for core promotion;

create a second delivery workflow;

use document or terminology volume as a maturity signal.
```

---

## 11. Current Maturity

```text
Canonical entry point: ESTABLISHED
Kernel wording: FINAL CANDIDATE
Retained laws: 10
Retained principles: 7
Retained guardrails: 14
Canonical terms: DEFINED
Epistemic loop: DEFINED
Behavioral candidates: 12
Architecture reconciliation: APPLIED
Glossary reconciliation: APPLIED
Contradiction and minimality review: COMPLETE
Relative-link and navigation review: PASSED
Final input package delivered to #6: YES
Executable downstream embodiment: NOT YET PROVEN
Foundation ready for owner acceptance: YES
```
