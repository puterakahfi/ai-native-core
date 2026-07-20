# Native AI Engineering Philosophy Discovery Report

Status: Discovery

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Branch: `13-native-ai-engineering-philosophy`

This document is a discovery artifact. It inventories and classifies the foundation already present in `ai-native-core`, identifies contradictions and missing concepts, and proposes a minimal kernel for review.

It is **not** yet the canonical Native AI Engineering philosophy, does not supersede existing architecture or contracts, and does not introduce a new machine-readable contract family.

---

## 1. Objective

Determine what philosophy-level foundation already exists implicitly across the repository before adding doctrine, axioms, laws, principles, guardrails, canonical terms, or a cross-domain epistemic loop.

The discovery must answer:

```text
What is already stable?
What is only an implementation or workflow rule?
What is duplicated or contradictory?
What is missing?
What is the smallest engineering-specific kernel that can govern every domain?
```

The result must remain:

```text
runtime-agnostic
provider-agnostic
product-agnostic
engineering-specific
non-metaphysical
evidence-oriented
compatible with ports and adapters
```

---

## 2. Sources Inspected

The initial discovery inspected the following current sources on the issue branch:

| Source | Current responsibility | Philosophy signal |
|---|---|---|
| `README.md` | Repository purpose, ownership, adapter boundary | Core owns stable agreements; adapters implement them |
| `docs/architecture-v0.2.md` | Current framework architecture | Domain-first, adapter-agnostic, evaluation-first, human-reviewed |
| `docs/domain-driven-model.md` | Product domain modeling guidance | Business capability before tools; tool output is not approved decision |
| `docs/engineering-contract.md` | Product technical decision constraints | Agents must not improvise material technical decisions silently |
| `docs/development-loop.md` | Human-readable execution cycle | Explore before acting; verify with real evidence; feedback loops |
| `contracts/runtime/development-loop.contract.yaml` | Machine-readable execution loop | Read before writing; scope control; reproducible verification |
| `docs/memory-vs-knowledge.md` | Source-of-truth distinction | Memory is not knowledge; remembered context must be verified |
| `docs/adapter-conformance.md` | Static adapter conformance model | Evidence is layered; declaration is not executable proof |
| `contracts/skills/quality/decision-provenance.contract.yaml` | Decision authority verification | Source, authority, scope, conflict, and unknown must be explicit |
| `contracts/skills/quality/skill-evolution.contract.yaml` | Learning promotion workflow | Verified cases may propose minimal reusable improvements, not silently redefine core |
| `rules/README.md` | Mandatory rule placement | Rules are testable must/must-not constraints |
| `docs/glossary.md` | Current shared vocabulary | Some useful definitions, but also stale layer and runtime-specific terminology |
| `CONTRIBUTING.md` | Change governance and validation | Inspect before changing; preserve behavior; evidence before completion |

This inventory is sufficient for the first discovery report. Later implementation must still inspect affected consumers and any additional source discovered during cross-document review.

---

## 3. Current Foundation Classification

The repository already contains a substantial philosophy, but it is distributed and mostly labeled as architecture, design principles, rules, workflow gates, or quality contracts.

### 3.1 Doctrine-like statements already present

The following statements act like doctrine because they define durable framework orientation rather than one workflow:

```text
Core defines stable, runtime-agnostic agreements.
Adapters decide how those agreements are implemented.
Domain capability must not be defined by a replaceable tool or provider.
Agents execute within contracts and boundaries; they do not own domain authority.
Knowledge is an explicit source of truth; memory is a retrieval and history aid.
Evaluation and evidence are required before trusted completion claims.
Product and runtime implementation must remain outside universal core ownership.
```

These should be preserved, reviewed, and restated under one philosophy entry point rather than duplicated across architecture documents.

### 3.2 Implicit epistemic axioms

Two minimal assumptions are repeatedly implied but never stated canonically.

#### Candidate Axiom A — Engineering begins from observable state

Existing support:

```text
Explore before plan or implementation.
Read relevant files.
Search the codebase.
Check existing tests.
Use actual command output.
Inspect existing contracts and consumers before creating a concept.
```

The repository therefore already behaves as if engineering work must begin from available, attributable state rather than invention.

Boundary:

```text
Not every relevant state is always observable.
Unavailable state must be recorded as unknown, blocked, or not verified.
Absence of evidence must not become fabricated evidence.
```

#### Candidate Axiom B — State is not identical to its model

Existing support:

```text
Memory must not replace knowledge.
Agent-authored summaries are not owner approval.
Observed implementation proves existence, not permission or scope.
Contract declaration is not executable proof.
Tool output is not automatically an approved decision.
Newest source is not automatically authoritative.
```

The repository therefore already distinguishes real or recorded state from summaries, assumptions, declarations, interpretations, and claims, but this distinction has no single canonical definition.

### 3.3 Implicit bridge law

#### Candidate Bridge Law — Engineering systems update through evidence and feedback

Existing support:

```text
Verification failures loop back to implementation.
Review feedback loops back to implementation.
Verified product lessons may become learning candidates.
Promotion requires before/after evidence and regression evaluation.
A single implementation cannot silently redefine a shared contract.
```

This is broader than the development loop. It describes how an AI-native engineering system preserves continuity while changing its context, plan, implementation, skill, workflow, contract, or domain understanding through evidence.

### 3.4 Existing principles

The following are best classified as advisory or orienting principles rather than axioms or hard rules:

```text
Business capability first.
Domain model before ports.
Ports before adapters.
Prefer replaceable providers and tools.
Evaluation-first.
Human-reviewed by default.
Knowledge before memory.
Consistency over local preference.
Prefer the smallest justified reusable improvement.
```

Principles guide decisions but require separate guardrails when violation must block execution.

### 3.5 Existing mandatory guardrails

The repository already contains enforceable or blocking constraints that should be promoted into a coherent guardrail model:

```text
Do not invent missing source metadata.
Do not treat agent-authored text as owner approval.
Do not treat observed implementation as permission or intended scope.
Do not silently resolve authoritative conflicts.
Do not let a tool or provider define the domain.
Do not claim verification without actual evidence.
Do not silently skip required phases.
Do not silently expand scope.
Do not force-push without explicit request.
Do not promote unverified anecdotes into shared skills or core.
Do not copy product-specific implementation into reusable skills.
Do not treat contract metadata as proof of executable behavior.
Do not let memory override explicit source-of-truth knowledge.
```

These are currently distributed across contracts and docs. The philosophy work should define their common rationale without weakening their existing machine-readable enforcement.

### 3.6 Existing mechanisms, not philosophy

The following should remain mechanisms derived from the philosophy rather than becoming the philosophy itself:

| Mechanism | Purpose |
|---|---|
| Development Loop | Executes Explore → Plan → Implement → Verify → Review → Document → Deliver |
| Decision Provenance | Verifies source, authority, scope, conflict, and supersession |
| Adapter Conformance | Separates contract resolution, version, static coverage, boundaries, and behavioral evidence |
| Skill Evolution | Converts verified cases into minimal reusable improvements |
| Domain-Driven Model | Models product domains and bounded contexts |
| Engineering Contract | Locks product-specific technical decisions |

A philosophy kernel should explain **why** these mechanisms exist and what invariant they preserve. It should not duplicate their complete operational procedures.

---

## 4. Missing Canonical Concepts

The following terms are required by current behavior but are not yet canonically defined with stable boundaries:

```text
observable state
observation
model
fact
inference
assumption
unknown
claim
decision
authority
evidence
feedback
capacity
coherence
embodiment
validation
verification
evaluation
review
approval
learning candidate
core evolution proposal
```

Current documents use several of these words correctly in context, but downstream systems cannot yet rely on one authority for their exact meaning.

### 4.1 Required distinctions

The philosophy layer must prevent these states from collapsing:

```text
observation ≠ interpretation
interpretation ≠ fact
assumption ≠ decision
decision ≠ authority
claim ≠ evidence
plan ≠ execution
contract ≠ implementation
static conformance ≠ executable behavior
verification ≠ total product validation
review verdict ≠ approval authority
memory ≠ source-of-truth knowledge
successful local fix ≠ universal reusable law
```

---

## 5. Contradictions and Structural Drift

### 5.1 Competing architecture layer models

`docs/architecture-v0.2.md` defines:

```text
Intent
→ Domain
→ Application
→ Contract
→ Port
→ Adapter
→ Agent
→ Rule
→ Skill
→ Knowledge
→ Evaluation
```

`docs/glossary.md` still references a different numbered model containing Blueprint, Engineering Contract, Knowledge, Rules, Skills, Tool/MCP, Memory, Loop, and Evaluation layers.

This makes layer numbers and ownership unreliable. The philosophy implementation should not invent a third competing numbering system. It should define foundation relationships first, then allow `#6` to reconcile the canonical domain and architecture model.

### 5.2 Principles and guardrails are conflated

`rules/README.md` says rules are guardrails, while other documents use “design principle,” “critical rule,” quality gates, contract rules, and anti-patterns without a shared classification.

Required separation:

```text
Axiom      minimal foundational assumption
Law        derived invariant or reliable system relation
Principle  preferred decision orientation
Guardrail  mandatory must/must-not boundary
Mechanism  reusable operational structure
Gate       checkable transition or acceptance condition
```

### 5.3 Evidence has no canonical taxonomy

The repository correctly requires evidence but does not consistently distinguish:

```text
source evidence
implementation evidence
static conformance evidence
behavioral evaluation evidence
runtime evidence
product acceptance evidence
human approval evidence
learning and regression evidence
```

This allows “evidence-backed” to remain too broad unless the evidence type and claim scope are explicit.

### 5.4 Stable does not mean immutable

Architecture v0.2 says domain and use cases are stable. Skill evolution and contract versioning show they are actually **more stable and governed**, not immutable.

Candidate clarification:

```text
Stable means protected by explicit ownership, evidence, compatibility review,
and controlled evolution. Stable does not mean permanently frozen.
```

### 5.5 Human review semantics are unresolved

Architecture says “human-reviewed by default,” while the development loop allows declared low-risk shortcuts and product-defined approval mechanisms.

The philosophy should distinguish:

```text
human review as default governance posture
human approval as authority-bearing decision
runtime automation as delegated execution
low-risk shortcut as explicit policy exception
```

### 5.6 Runtime-specific terminology exists in the core glossary

The current glossary includes Hermes-specific `Profile` terminology and an older `Skill Adapter` definition based on `extends` and `type: skill-adapter`.

These should be reviewed by `#6` and later taxonomy work. The philosophy report only records the drift; it does not rename these concepts prematurely.

### 5.7 Feedback is lifecycle-local rather than framework-wide

Feedback exists in verification loops, review loops, product learning, and skill evolution, but no cross-domain rule explains how feedback may update a model without automatically rewriting core.

The new kernel must define:

```text
feedback may update working models and local decisions;
verified reusable learning may become an evolution proposal;
core changes require explicit review, compatibility analysis, and authority.
```

### 5.8 Capacity is missing as a first-class constraint

Current work checks context, risk, permissions, approval, and validation in separate places. There is no common concept explaining why an agent must narrow, pause, route, or refuse a scope when execution capacity is insufficient.

Candidate capacity dimensions:

```text
context availability
capability availability
tool availability
permission and authority
risk controls
time or scope budget
validation path
review coverage
```

---

## 6. Candidate Minimal Kernel

The following is a discovery candidate, not an accepted canonical foundation.

### 6.1 Candidate doctrine

```text
Native AI Engineering builds systems in which agents can perform meaningful
engineering work while domain authority, source-of-truth knowledge, contracts,
risk boundaries, evidence, and evolution remain explicit and reviewable.

AI increases execution capacity. It does not erase the distinction between
state and model, claim and evidence, execution and authority, or local learning
and universal core truth.
```

### 6.2 Candidate axioms

#### A1 — Engineering begins from observable state

```text
Engineering work begins from available, attributable state.
```

#### A2 — State is not identical to its model

```text
Observed or recorded state is not identical to a human, agent, document,
or system model of that state.
```

### 6.3 Candidate bridge law

```text
AI-native engineering systems preserve continuity and update their operational
organization through appropriately scoped evidence and feedback.
```

### 6.4 Candidate derived laws

| Candidate law | Statement |
|---|---|
| Evidence–Model Separation | Observation, interpretation, assumption, decision, claim, and evidence must remain distinguishable. |
| Model Recognition | An unmarked assumption tends to be executed as if it were fact. |
| Traceability | A material decision is trustworthy only to the degree that its source, scope, authority, rationale, and evidence are traceable. |
| Capacity | Execution scope must not exceed available context, capability, permissions, risk controls, and validation capacity. |
| Smallest Coherent Change | Prefer the smallest change that preserves system coherence and can produce meaningful verification evidence. |
| Coherence | Quality increases as intent, requirements, contracts, architecture, implementation, runtime behavior, and evidence contradict each other less. |
| Embodiment | A principle is embodied only when it changes repeatable executable behavior and produces appropriate evidence. |
| Feedback | No material engineering claim is mature before it meets appropriate feedback and survives relevant iteration. |
| Evolution | Implementations and field tests may propose core change, but no adapter, runtime, product, or single case may silently redefine core. |

---

## 7. Candidate Cross-Domain Epistemic Loop

This loop governs how a workflow reasons. It is not a replacement for product-development, new-feature, redesign, bugfix, deployment, marketing, or operational workflows.

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ READ EVIDENCE
→ UPDATE
```

### OBSERVE

```text
What is directly present, recorded, or supported?
What source produced it?
What relevant state is unavailable?
```

### ASSESS CAPACITY

```text
Are context, capability, tools, permissions, risk controls,
review coverage, and validation paths sufficient for this scope?
```

### DECOMPOSE THE MODEL

```text
What is observed?
What is inferred?
What is assumed?
What is decided?
What is approved?
What is unknown, contradicted, or not verified?
```

### SELECT A TESTABLE RESPONSE

```text
What is the smallest coherent response that can produce useful evidence
without silently expanding scope or authority?
```

### READ EVIDENCE

```text
What do source, technical, runtime, review, user, and product evidence show?
What claim does each evidence type actually support?
```

### UPDATE

```text
What should continue, change, stop, narrow, escalate, or become a learning candidate?
Does the update belong in context, plan, implementation, product knowledge,
skill, workflow, contract, or a reviewed core evolution proposal?
```

---

## 8. Representative Stress Tests

The candidate kernel must be tested before acceptance.

### 8.1 Repository analysis

```text
OBSERVE      Inspect repository, branch, issue, files, tests, and current behavior.
ASSESS       Confirm access, context completeness, and available validation.
DECOMPOSE    Separate actual structure from remembered or inferred structure.
SELECT       Produce the smallest useful analysis or discovery artifact.
READ         Compare claims against direct repository sources.
UPDATE       Correct the working model; do not invent missing repository facts.
```

Expected guardrail:

```text
No repository path, implementation status, issue state, or test result is invented.
```

### 8.2 Planning

```text
OBSERVE      Read acceptance criteria and current implementation.
ASSESS       Confirm scope and verification capacity.
DECOMPOSE    Separate requirement, assumption, dependency, and unresolved decision.
SELECT       Create a plan with exact affected artifacts and evidence strategy.
READ         Validate the plan against architecture and repository state.
UPDATE       Revise the plan before execution when evidence contradicts it.
```

Expected guardrail:

```text
Plan is a model of intended work, not proof that work occurred.
```

### 8.3 Design

```text
OBSERVE      Inspect actual surface, interaction state, design locks, and user need.
ASSESS       Confirm artifact coverage, viewport coverage, and reviewer capability.
DECOMPOSE    Separate observed usability issue from aesthetic preference.
SELECT       Make the smallest coherent design change that preserves valid locks.
READ         Review visual, interaction, accessibility, and product evidence.
UPDATE       Refine the design system, skill, or product artifact at the correct layer.
```

Expected guardrail:

```text
A screenshot or attractive artifact is not complete UX or product validation.
```

### 8.4 Engineering

```text
OBSERVE      Inspect code, architecture, tests, dependencies, and runtime behavior.
ASSESS       Confirm permissions, blast radius, and executable validation commands.
DECOMPOSE    Separate root cause, hypothesis, implementation choice, and contract rule.
SELECT       Apply the smallest coherent patch.
READ         Run tests, build, lint, review, and relevant runtime checks.
UPDATE       Fix, revert, document, or create a learning candidate based on evidence.
```

Expected guardrail:

```text
Compilation or one passing test does not prove total product correctness.
```

### 8.5 Marketing and growth

```text
OBSERVE      Inspect product truth, audience evidence, channel constraints, and metrics.
ASSESS       Confirm claim authority, legal or brand boundaries, and measurement path.
DECOMPOSE    Separate market fact, audience hypothesis, message choice, and promise.
SELECT       Run the smallest meaningful campaign or messaging experiment.
READ         Interpret behavioral and business evidence within the experiment scope.
UPDATE       Refine positioning, message, channel, or hypothesis without fabricating claims.
```

Expected guardrail:

```text
A generated marketing claim is not product evidence or approved promise.
```

### 8.6 Tool permission and destructive action

```text
OBSERVE      Identify requested action and actual system state.
ASSESS       Verify permission, authority, reversibility, and policy requirements.
DECOMPOSE    Separate capability to execute from authority to execute.
SELECT       Route for approval or choose a reversible alternative.
READ         Confirm result and audit evidence.
UPDATE       Record the decision without expanding future permission silently.
```

Expected guardrail:

```text
Tool access is not authorization.
```

### 8.7 Skill refinement

```text
OBSERVE      Capture verified failure, fix, and before/after evidence.
ASSESS       Confirm transferability and regression evaluation capacity.
DECOMPOSE    Separate local implementation detail from reusable invariant reason.
SELECT       Patch the smallest correct shared layer.
READ         Run regression and conformance checks.
UPDATE       Promote, defer, reject, or propose a core change with provenance.
```

Expected guardrail:

```text
One successful case does not become a universal skill or core law automatically.
```

---

## 9. Artifact Authority Proposal

The philosophy work should evaluate the following source-role taxonomy:

| Artifact role | Owns | Must not become |
|---|---|---|
| Philosophy / Doctrine | Framework purpose and durable orientation | Workflow instructions |
| Axiom | Minimal foundational assumption | Broad principle list |
| Law | Derived invariant and dependency | Untraceable slogan |
| Principle | Preferred decision orientation | Hidden mandatory rule |
| Guardrail | Stable must/must-not boundary | Optional advice |
| Canonical Term | One authoritative definition | Full domain or workflow model |
| Domain Map | Relationships between canonical terms | Parallel term authority |
| Mechanism / Module | Reusable operational structure | New axiom by implication |
| Contract | Stable machine-readable agreement | Complete executable methodology |
| Adapter Translation | Runtime or product binding | Core redefinition |
| Implementation Evidence | Observed execution result | Universal truth |
| Field Test | Bounded real-world validation | Automatic core change |
| Stability / Freeze Review | Readiness and contradiction review | New foundation content |

Dependency direction candidate:

```text
Philosophy and axioms
→ laws
→ principles, guardrails, and canonical terms
→ domain model and mechanics
→ contracts and ports
→ adapters, skills, and workflows
→ runtime and product implementation
→ evidence and field tests
→ reviewed learning and evolution proposals
```

---

## 10. Recommended Implementation Sequence

The next implementation steps for issue `#13` should be:

1. Create one canonical philosophy entry point.
2. Refine and accept the minimal doctrine, two axioms, and bridge law.
3. Derive laws with explicit source relationships and counterexamples.
4. Separate principles from mandatory guardrails.
5. Define atomic canonical terms and ownership rules.
6. Formalize the cross-domain epistemic loop without duplicating the development loop.
7. Create a philosophy-to-existing-source traceability matrix.
8. Add negative examples for common false equivalences.
9. Apply the kernel to analysis, planning, design, engineering, marketing, operations, and skill evolution.
10. Reconcile documentation navigation without prematurely resolving domain taxonomy owned by `#6`.
11. Perform contradiction, terminology, and link review.
12. Only then mark the philosophy foundation ready for `#6` consumption.

Candidate future artifacts must be justified individually. A likely structure is:

```text
docs/philosophy/README.md
docs/philosophy/doctrine.md
docs/philosophy/axioms.md
docs/philosophy/laws.md
docs/philosophy/principles-and-guardrails.md
docs/philosophy/epistemic-loop.md
docs/philosophy/term-authority.md
```

Do not create all files merely to match the proposed structure. Begin with the smallest coherent set that has clear authority and avoids duplicated definitions.

---

## 11. Decisions Deferred

This discovery report intentionally does not decide:

```text
final axiom wording
whether philosophy becomes a machine-readable contract family
final architecture layer numbering
final Native AI Engineering bounded contexts
final lifecycle and capability taxonomies
final port taxonomy
final contract schemas
runtime orchestration behavior
product-specific validation policy
```

Those decisions belong to the issue sequence:

```text
#13 philosophy/kernel
→ #6 canonical domain model
→ #7 port taxonomy
→ #8 contract schemas
→ #9 conformance validator v2
```

---

## 12. Discovery Verdict

```text
Existing philosophy fragments: STRONG
Canonical philosophy authority: MISSING
Implicit epistemic axioms: PRESENT BUT UNDECLARED
Evidence orientation: STRONG BUT UNTYPED
Decision authority model: STRONG
Cross-domain capacity model: MISSING
Cross-domain feedback law: PRESENT BUT DISTRIBUTED
Principle/guardrail separation: INCONSISTENT
Artifact role governance: PARTIAL
Ready to freeze domain model: NO
Ready to implement philosophy kernel: YES
```

The repository does not need a philosophical rewrite. It needs **canonicalization, derivation, terminology ownership, and cross-domain unification** of principles that already exist in executable or reviewable form.
