# Native AI Engineering Philosophy — Usefulness And Traceability

Status: Candidate acceptance gate

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Related foundation artifacts:

- [`laws.md`](laws.md)
- [`principles-and-guardrails.md`](principles-and-guardrails.md)
- [`term-authority.md`](term-authority.md)
- [`epistemic-loop.md`](epistemic-loop.md)

This document answers one practical question:

```text
What does the Native AI Engineering philosophy change in real engineering work?
```

The philosophy is not accepted merely because it is internally consistent, comprehensive, or well written.

It is useful only when it changes decisions, prevents known failures, produces executable boundaries, improves evidence quality, or gives downstream repositories a reusable contract foundation.

---

## 1. Direct Purpose

The Native AI Engineering philosophy exists to provide a minimal, reusable decision kernel below domain models, contracts, skills, workflows, adapters, runtimes, and products.

Its practical purpose is to make these outcomes systematic:

```text
agents do not invent state that was not inspected;
models and plans are not reported as executed reality;
tool access is not treated as authority;
claims remain proportional to evidence;
completion cannot hide material gaps;
feedback can revise the affected layer;
local learning reaches the smallest correct shared layer;
products and adapters cannot silently redefine core.
```

Without this foundation, individual contracts may be structurally valid while still encoding false certainty, false authority, false completion, or ungoverned evolution.

The philosophy does not replace implementation. It defines the distinctions and invariants that implementation must preserve.

---

## 2. Philosophy Usefulness Gate

Every philosophy statement must pass this gate before acceptance.

### U1 — Decision impact

```text
Does the statement change how a material engineering decision is made?
```

Valid impacts include:

```text
narrowing a claim;
blocking an unauthorized action;
requiring source attribution;
separating evidence layers;
changing completion status;
selecting the correct ownership layer;
requiring compatibility review;
choosing a reversible response.
```

A statement that only sounds desirable but changes no decision is not foundation material.

### U2 — Failure prevention

```text
Does the statement prevent a known recurring failure?
```

Candidate failure classes include:

```text
invented repository or issue state;
assumption executed as fact;
plan reported as execution;
tool permission treated as approval;
passing build reported as product validation;
contract presence reported as conformance;
installed skill reported as applied behavior;
review verdict reported as owner approval;
local product fix promoted as universal rule;
silent semantic drift.
```

### U3 — Named consumer

```text
Which downstream artifact, repository, issue, or quality process consumes it?
```

A philosophy statement without a plausible consumer must be merged, deferred, or removed.

### U4 — Embodiment path

```text
How can the statement change repeatable executable behavior or review evidence?
```

Possible embodiment surfaces include:

```text
domain objects and lifecycle states;
contract fields and schemas;
validator rules and result classes;
skill procedures;
workflow gates;
runtime permission and approval controls;
review rubrics;
behavioral test cases;
product acceptance evidence.
```

Documentation presence alone does not pass this gate.

### U5 — Minimality

```text
Is this the smallest concept needed to produce the decision impact?
```

A statement should be merged or removed when another axiom, law, term, guardrail, or mechanism already produces the same consequence without loss of clarity.

### U6 — Scope discipline

```text
Is the statement universal to Native AI Engineering, or is it actually a repository,
product, runtime, workflow, or risk policy?
```

Local policies must not be promoted into universal philosophy.

### Acceptance rule

```text
No decision impact + no named consumer + no embodiment path
= remove, merge, or defer.
```

---

## 3. Concrete Problems This Foundation Solves

### 3.1 Reliable repository and system analysis

Problem:

```text
An agent may infer repository state from memory, summaries, screenshots, or assumed
conventions and then report the inference as current fact.
```

Foundation response:

```text
A1 Available, Attributable State
L1 State Attribution
L2 State–Model Separation
G1 No Fabricated State Or Evidence
G2 No Model-As-Fact Collapse
```

Practical result:

```text
repository, branch, issue, file, runtime, and test claims require attributable sources;
missing access becomes UNKNOWN, BLOCKED, or NOT_VERIFIED;
plans and summaries remain distinguishable from inspected state.
```

Embodiment candidates:

```text
analysis skill behavior;
source-reference fields;
repository-review rubric;
behavioral cases for invented paths and test claims.
```

### 3.2 Safe autonomous execution

Problem:

```text
An agent or runtime can technically perform an action and incorrectly treats that
capability as permission, authority, or approval.
```

Foundation response:

```text
L5 Decision Traceability
L6 Capability–Authority Separation
L7 Execution Capacity
G4 Capability Is Not Authority
G14 High-Risk Actions Require Controls
```

Practical result:

```text
capability, permission, authority, approval, risk, reversibility, and recovery remain
separate inputs to execution;
missing authority routes or blocks instead of being inferred from access.
```

Embodiment candidates:

```text
control-plane authorization model;
tool registry risk metadata;
approval gates;
destructive-action behavioral tests;
audit records.
```

### 3.3 Honest verification and completion

Problem:

```text
A passing test, build, static contract declaration, screenshot, or review verdict is
expanded into a claim of complete product correctness.
```

Foundation response:

```text
L4 Claim–Evidence Scope
L8 Coherent Completion
L9 Executable Embodiment
G3 No Claim Beyond Evidence Scope
G8 No False Completion
G9 Declaration Is Not Embodiment
```

Practical result:

```text
static conformance, behavioral execution, runtime evidence, product validation,
review, and approval are separate evidence layers;
completion claims identify scope, coverage, limitations, and unresolved requirements.
```

Embodiment candidates:

```text
contract evidence primitives;
validator result classes;
completion status model;
review reports;
product acceptance records.
```

### 3.4 Reusable learning without polluting core

Problem:

```text
One successful product fix or adapter behavior becomes a shared skill rule, contract,
or core definition without transferability and compatibility review.
```

Foundation response:

```text
L10 Feedback Revision
L11 Evolution Authority
L12 Governed Stability
P6 Correct-Layer Change
G11 No Unverified Promotion
G12 Concrete Layers Must Not Redefine Canonical Layers
G15 No Silent Semantic Evolution
```

Practical result:

```text
local evidence becomes a learning candidate first;
the reusable reason is separated from product detail;
the smallest correct target layer is selected;
canonical change requires compatibility and authority review.
```

Embodiment candidates:

```text
skill-evolution procedure;
learning-candidate record;
regression evaluation;
compatibility analysis;
core-change review.
```

---

## 4. Downstream Consumer Matrix

### 4.1 `ai-native-core#6` — Canonical domain model

The philosophy must change domain modeling by requiring the domain model to preserve:

```text
state versus observation;
model, interpretation, inference, and assumption;
claim versus evidence;
decision versus effective decision;
review versus approval;
capability, permission, authority, and capacity;
feedback, learning candidate, and accepted evolution;
partial, blocked, not-verified, and completed states.
```

Expected domain impact:

```text
the lifecycle cannot use one generic “status” field for all epistemic states;
evidence cannot be embedded as an untyped output blob;
approval cannot be represented as a review boolean;
execution capability cannot imply decision authority;
learning cannot directly mutate canonical definitions.
```

The exact entities, aggregates, value objects, and bounded contexts remain owned by issue `#6`.

Usefulness verdict:

```text
DIRECT CONSUMER — REQUIRED
```

### 4.2 `ai-native-core#7` — Port taxonomy and contracts

The philosophy must influence port contracts through explicit fields or inherited primitives for:

```text
ownership boundary;
request and response scope;
authorization and approval expectations;
risk and reversibility;
observability;
evidence production;
errors and unsupported claims;
consumer compatibility.
```

Expected port impact:

```text
a RepositoryPort capability does not authorize every repository mutation;
a ReviewPort verdict does not automatically become Approval;
an EvaluationPort must identify evidence scope;
a provider adapter cannot redefine product or domain meaning.
```

Usefulness verdict:

```text
DIRECT CONSUMER — REQUIRED AFTER #6
```

### 4.3 `ai-native-core#8` — Contract schemas

The philosophy must inform shared schema primitives such as:

```text
source reference;
scope and coverage;
claim;
evidence reference and evidence layer;
verification or validation target;
authority requirement;
approval state;
unknown, partial, blocked, and not-checkable semantics;
boundary ownership and delegation;
compatibility and supersession.
```

Expected schema impact:

```text
contracts can distinguish declaration from evidence;
workflow gates can identify the claim they authorize;
shared primitives are defined once rather than copied with different meanings;
missing evidence cannot silently become PASS.
```

Usefulness verdict:

```text
DIRECT CONSUMER — REQUIRED AFTER #6/#7
```

### 4.4 `ai-native-core#9` — Conformance validator v2

The philosophy already changes required validator semantics:

```text
contract path and version resolution;
structural declaration conformance;
behavioral evidence;
runtime integration evidence;
product acceptance evidence;
review and approval;
```

must remain different result layers.

Expected validator impact:

```text
CONFORMANT does not mean product validated;
missing declaration differs from contradictory declaration;
NOT_CHECKABLE differs from PASS;
BEHAVIOR_NOT_VERIFIED remains visible;
static metadata cannot prove skill application.
```

Usefulness verdict:

```text
DIRECT CONSUMER — REQUIRED
```

### 4.5 `ai-native-skills`

The philosophy should affect executable behavior through:

```text
inspect-before-claim behavior;
explicit assumptions and unknowns;
capacity and authority assessment;
evidence-proportional completion reports;
correct-layer learning promotion;
behavioral test cases for false equivalences.
```

It must not be copied as a long philosophy essay into every `SKILL.md`.

Skills should consume only the relevant behavior, checks, and evidence requirements.

Usefulness verdict:

```text
EXECUTABLE CONSUMER — REQUIRED FOR EMBODIMENT
```

### 4.6 `native-ai-fw`

The philosophy should inform control-plane behavior for:

```text
state and source records;
tool capability and permission separation;
authority and approval routing;
risk and recovery controls;
execution evidence;
completion and limitation status;
feedback and learning-candidate routing.
```

The framework should not implement philosophy as hidden prompt text only.

Usefulness verdict:

```text
RUNTIME CONSUMER — REQUIRED FOR EMBODIMENT
```

### 4.7 Product repositories

Products should specialize:

```text
risk policy;
required reviewers and approvers;
product validation criteria;
release and rollback policy;
business evidence;
product-specific learning and acceptance.
```

Products may strengthen the foundation for their context but may not silently weaken truthfulness, authority, evidence, or evolution guardrails.

Usefulness verdict:

```text
VALIDATION CONSUMER — REQUIRED FOR REAL-WORLD PROOF
```

---

## 5. Existing Source Traceability

| Existing source | Existing useful behavior | Foundation interpretation | Keep / reconcile action |
|---|---|---|---|
| `README.md` | Core owns runtime-agnostic agreements | Supports explicit canonical ownership | Keep; add philosophy navigation later |
| `docs/architecture-v0.2.md` | Domain-first, ports/adapters separation | Supports P1 and G12 | Keep; reconcile stability and review wording |
| `docs/domain-driven-model.md` | Business capability before tools | Supports P1 and correct-layer ownership | Keep; remove product example from canonical authority later if needed |
| `docs/development-loop.md` | Explore before change; verify with evidence; feedback loops | Operationalizes A1, L4, L10, G7, G8 | Keep as mechanism; do not relabel as philosophy |
| `contracts/runtime/development-loop.contract.yaml` | Checkable phases, outputs, gates, transitions | Executable mechanism and policy surface | Preserve machine authority |
| `docs/adapter-conformance.md` | Conformance has multiple evidence layers | Direct expression of L4 and L9 | Keep; align terms with term authority |
| Decision Provenance contract | Source, scope, authority, conflicts, supersession | Direct expression of L1, L5, L6, G4, G6 | Preserve; later align shared primitives |
| Skill Evolution contract | Verified local learning and controlled promotion | Direct expression of L10, L11, G11, G12 | Preserve; later add behavioral evidence |
| `docs/memory-vs-knowledge.md` | Memory is retrieval aid, not source of truth | Direct expression of G13 | Keep; align definitions and authority references |
| `rules/README.md` | Mandatory must/must-not constraints | Operational guardrail specialization | Keep; link philosophy classification later |
| `CONTRIBUTING.md` | Change correct layer; inspect consumers; define validation | Operationalizes P6, P7, L11, L12 | Keep; reconcile philosophy navigation later |

---

## 6. Contradiction And Ambiguity Matrix

### C1 — “Domain is stable”

Current wording:

```text
Domain is stable.
Use cases are stable.
```

Risk:

```text
May be read as immutable, permanently correct, or protected from feedback.
```

Foundation correction:

```text
Canonical domain and use-case agreements should be stable through explicit ownership,
compatibility expectations, evidence, review, and governed evolution.
```

Action:

```text
RECONCILE WORDING
```

### C2 — “Human-reviewed by default”

Current wording:

```text
Human-reviewed by default.
```

Risk:

```text
A governance posture may be mistaken for a universal philosophy invariant or the
same approval requirement for every risk level.
```

Foundation correction:

```text
Review and approval coverage is proportionate to risk, reversibility, authority,
and consumer impact. Human review may remain the repository or product default policy.
```

Action:

```text
RECLASSIFY AS POSTURE / POLICY
```

### C3 — Evaluation before every approval, export, deployment, or publishing action

Current wording:

```text
Evaluation must happen before approval, export, deployment, or publishing.
```

Risk:

```text
“Evaluation” is too broad unless the required criteria, evidence, and policy scope
are named. It may force ceremony or hide that different actions need different gates.
```

Foundation correction:

```text
Applicable evidence, evaluation, review, and approval gates must be satisfied according
to the claim, action, risk, and governing policy.
```

Action:

```text
RECONCILE INTO POLICY-AWARE WORDING
```

### C4 — Glossary `Capability`

Current wording limits capability to what a skill contract declares an agent can do.

Risk:

```text
Ports, tools, adapters, runtimes, and systems also have capabilities.
```

Foundation correction:

```text
Capability is the ability of an actor, agent, tool, adapter, or system to perform a
category of action or produce a category of result.
```

Action:

```text
GLOSSARY NAVIGATION UPDATE REQUIRED
```

### C5 — Glossary `Conformance`

Current wording emphasizes adapter skill coverage of contract gates, inputs, and outputs.

Risk:

```text
Conformance may be mistaken for one boolean and for runtime or product proof.
```

Foundation correction:

```text
Conformance must name its evidence layer: resolution, version, structural declaration,
boundary consistency, behavioral execution, runtime integration, or product acceptance.
```

Action:

```text
GLOSSARY AND VALIDATOR ALIGNMENT REQUIRED
```

### C6 — Glossary `Verification`

Current wording defines verification mainly as running real commands.

Risk:

```text
Verification also applies to authority, source, contract path, and other specified claims.
```

Foundation correction:

```text
Verification determines whether a specified claim or requirement is supported by
appropriate evidence. Command output is one evidence method.
```

Action:

```text
GLOSSARY NAVIGATION UPDATE REQUIRED
```

### C7 — Documentation-only Development Loop shortcut

Current policy allows documentation-only work to skip Verify and Review.

Risk:

```text
Markdown may still contain broken links, contradictory terminology, unsafe policy,
or incorrect canonical claims.
```

Foundation correction:

```text
A declared documentation shortcut may reduce checks, but must retain residual evidence
appropriate to the documentation claim and must not bypass contradiction or authority review
when canonical semantics change.
```

Action:

```text
PRESERVE POLICY; REFINE CONDITIONS LATER
```

### C8 — “Always push after commit”

Current wording:

```text
Always push after commit.
```

Risk:

```text
Repository workflow policy is presented as if universal to Native AI Engineering.
```

Foundation correction:

```text
Delivery follows the repository and team workflow. Unpushed state must not be reported as
remote delivery.
```

Action:

```text
RECLASSIFY AS REPOSITORY POLICY
```

---

## 7. Candidate Pruning Review

The foundation is still candidate. The following items require explicit pruning review before acceptance.

### Strong keep candidates

These currently have distinct decision impact and downstream consumers:

```text
A1 Available, Attributable State
A2 State Is Not Identical To Its Model
Bridge Law — Evidence And Feedback Update The System

L1 State Attribution
L2 State–Model Separation
L4 Claim–Evidence Scope
L5 Decision Traceability
L6 Capability–Authority Separation
L7 Execution Capacity
L8 Coherent Completion
L9 Executable Embodiment
L10 Feedback Revision
L11 Evolution Authority
```

### Merge or reclassification review

```text
L3 Model Recognition
```

Question:

```text
Does L3 produce a distinct downstream contract or validator consequence beyond L2,
G2, and explicit assumption fields?
```

If not, merge it into the State–Model Separation law and assumption guardrail.

```text
L12 Governed Stability
```

Question:

```text
Is governed stability a distinct law, or is it better represented by L11 Evolution
Authority plus P8 Evaluation Before Trust Expansion and G15 No Silent Semantic Evolution?
```

If it adds no distinct invariant or consumer, reclassify or merge it.

### Principle pruning rule

The eleven principles must not all be copied into every skill or workflow.

Each consumer should select only principles that materially affect its decisions.

### Guardrail pruning rule

Guardrails may remain separate when they produce different block, route, evidence, or escalation behavior. Duplicate wording should be merged even when the failure names differ.

---

## 8. Before And After Examples

### Repository task

Before:

```text
“The branch is feature-x and tests pass.”
```

After:

```text
“The active branch was verified as feature-x from repository state. Unit tests pass in
this environment. Runtime and product acceptance were not evaluated.”
```

### Tool action

Before:

```text
“The token allows force push, so the agent may do it.”
```

After:

```text
“The tool has technical permission, but no effective decision authorizes force push.
The action is blocked pending explicit authority.”
```

### Design review

Before:

```text
“The redesign is complete because the desktop screenshot looks correct.”
```

After:

```text
“Desktop visual review passed. Mobile interaction and accessibility remain not verified,
so the redesign status is partial.”
```

### Skill refinement

Before:

```text
“This product fix worked, so add the exact component choice to the universal skill.”
```

After:

```text
“The verified fix creates a learning candidate. Extract the reusable decision reason,
test transferability, and promote only to the smallest correct shared layer.”
```

These changes are the intended value of the philosophy.

---

## 9. Acceptance And Stop Conditions

Issue `#13` must not be accepted solely because all candidate documents exist.

Acceptance requires:

- [ ] every retained axiom, law, principle, and guardrail passes the usefulness gate;
- [ ] every retained concept has at least one named downstream consumer;
- [ ] duplicate or decorative concepts are merged or removed;
- [ ] issue `#6` can consume the vocabulary without inventing parallel definitions;
- [ ] issue `#8` can derive shared contract primitives from the distinctions;
- [ ] issue `#9` can preserve separate structural, behavioral, runtime, and product evidence layers;
- [ ] at least representative behavioral test candidates are defined for executable embodiment;
- [ ] glossary and architecture contradictions are reconciled;
- [ ] repository and product policies remain outside universal philosophy;
- [ ] the foundation remains smaller than the systems it governs;
- [ ] a reviewer can explain what concrete engineering failure each retained concept prevents.

Stop or simplify when:

```text
new terminology adds no decision value;
a distinction has no downstream consumer;
a principle duplicates an existing law or guardrail;
a mechanism becomes a second delivery workflow;
a local policy is being universalized;
document volume grows faster than executable impact.
```

---

## 10. Current Verdict

```text
Philosophy purpose: PRACTICAL DECISION AND GOVERNANCE KERNEL
Decorative philosophy accepted: NO
Usefulness gate: ESTABLISHED FOR CANDIDATE REVIEW
Direct downstream consumers: #6, #7, #8, #9
Executable consumers: ai-native-skills, native-ai-fw, product repositories
Concrete failure classes addressed: PRESENT
Embodiment path: IDENTIFIED, NOT YET IMPLEMENTED
Candidate pruning: REQUIRED BEFORE ACCEPTANCE
Cross-document reconciliation: REQUIRED
Ready to merge philosophy to main: NOT YET
Ready to continue reconciliation: YES
```

The next slice should use this matrix to:

1. reconcile philosophy navigation and maturity status;
2. update `docs/glossary.md` into a navigation index for philosophy-level terms;
3. reconcile ambiguous architecture wording without rewriting executable contracts;
4. review L3 and L12 for merge or reclassification;
5. add explicit philosophy-consumption guidance to issue `#6`.
