# Native AI Engineering Philosophy

Status: Candidate foundation

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

This file is the canonical entry point for philosophy-level work in `ai-native-core`.

It owns navigation, authority boundaries, foundation status, and the current candidate kernel. It does not yet declare the philosophy frozen, does not supersede accepted machine-readable contracts, and does not decide the canonical domain model owned by `#6`.

---

## 1. Purpose

Native AI Engineering needs a foundation below domain models, contracts, ports, skills, workflows, and runtime implementations.

That foundation must explain:

```text
what engineering work begins from
how state differs from a model of state
how claims differ from evidence
how execution capacity and authority constrain action
how feedback updates a system
how local learning may propose shared evolution
why implementations cannot silently redefine core
```

The philosophy must remain:

```text
engineering-specific
runtime-agnostic
provider-agnostic
product-agnostic
non-metaphysical
evidence-oriented
compatible with ports and adapters
usable across capability domains
```

---

## 2. Foundation Position

The candidate dependency direction is:

```text
Philosophy / Doctrine
→ Epistemic Axioms
→ Systems and Engineering Laws
→ Principles and Guardrails
→ Canonical Language
→ Native AI Engineering Domain Model
→ Lifecycle and Capability Taxonomies
→ Contracts and Ports
→ Skills, Workflows, and Adapters
→ Runtime and Product Implementation
→ Evidence, Evaluation, and Approval
→ Learning and Reviewed Evolution
```

The philosophy layer explains why the lower layers exist and what invariants they preserve.

It must not absorb the detailed responsibilities of:

```text
domain models
contracts
ports
workflow definitions
skill methodology
runtime orchestration
product policy
provider configuration
implementation evidence
```

---

## 3. Authority Model

### This file owns

```text
philosophy navigation
foundation status
source-role boundaries
candidate doctrine
candidate axioms
candidate bridge law
foundation dependency direction
rules for later derivation
```

### This file does not own

```text
final bounded contexts
final lifecycle taxonomy
final capability taxonomy
final port taxonomy
contract schemas
adapter implementation
runtime behavior
product-specific policy
provider-specific behavior
```

Those concerns remain governed by their dedicated issues, contracts, repositories, and accepted source-of-truth artifacts.

### Current supporting sources

The candidate foundation is derived from existing repository behavior and constraints, especially:

```text
README.md
docs/architecture-v0.2.md
docs/domain-driven-model.md
docs/engineering-contract.md
docs/development-loop.md
docs/memory-vs-knowledge.md
docs/adapter-conformance.md
contracts/runtime/development-loop.contract.yaml
contracts/skills/quality/decision-provenance.contract.yaml
contracts/skills/quality/skill-evolution.contract.yaml
rules/README.md
CONTRIBUTING.md
```

The complete discovery and contradiction inventory is recorded in:

```text
docs/native-ai-engineering-philosophy-discovery.md
```

---

## 4. Candidate Doctrine

```text
Native AI Engineering builds systems in which agents can perform meaningful
engineering work while domain authority, source-of-truth knowledge, contracts,
risk boundaries, evidence, and evolution remain explicit and reviewable.

AI increases execution capacity. It does not erase the distinction between
state and model, claim and evidence, execution and authority, or local learning
and universal core truth.
```

### Doctrine consequences

Native AI Engineering therefore requires systems where:

```text
agents inspect before materially changing
unknown state remains explicit
assumptions are not silently promoted to facts
execution authority remains attributable
claims are scoped to appropriate evidence
contracts remain distinct from implementations
feedback can update working models
shared evolution remains reviewed and traceable
```

---

## 5. Candidate Kernel

The smallest current candidate contains two epistemic axioms and one bridge law.

These statements are candidates under review. They are not universal scientific claims outside the bounded Native AI Engineering framework.

### Axiom 1 — Engineering Begins From Available State

```text
Engineering work begins from available, attributable state.
```

#### Meaning

Before planning or materially changing a system, the actor identifies the state that is directly available through an attributable source.

Available state may include:

```text
explicit user instruction
active issue and acceptance criteria
repository and branch state
current implementation
runtime behavior
tool and permission state
technical validation output
product behavior
review records
available evidence
```

#### Boundary

```text
Not every relevant state is always available.
Unavailable state must remain unknown, blocked, or not verified.
Absence of evidence must not become fabricated evidence.
Observation is always bounded by source, access, time, and coverage.
```

#### Existing operational expressions

```text
read before writing
inspect contracts and consumers before creating concepts
explore before planning or implementation
run actual commands before verification claims
record missing provenance as unknown rather than invented
```

### Axiom 2 — State Is Not Identical To Its Model

```text
Observed or recorded state is not identical to a human, agent, document,
or system model of that state.
```

#### Meaning

Models are necessary representations used for interpretation, planning, prediction, communication, and execution. They may be useful and still remain different from the state they represent.

Examples:

```text
repository state ≠ repository summary
user intent ≠ inferred intent
issue text ≠ agent interpretation
architecture diagram ≠ implementation
plan ≠ execution
contract declaration ≠ conformance
skill declaration ≠ skill application
test output ≠ complete product correctness
review verdict ≠ evidence itself
memory ≠ source-of-truth knowledge
```

#### Boundary

```text
This axiom does not make models untrustworthy by default.
It requires their source, scope, assumptions, and verification status to remain visible.
A verified model may guide action without becoming identical to reality.
```

#### Existing operational expressions

```text
agent-authored text is not owner approval
observed implementation proves existence, not permission or intended scope
contract metadata is not executable proof
memory must not override explicit knowledge
newest source is not automatically authoritative
```

### Bridge Law — Engineering Systems Update Through Evidence And Feedback

```text
AI-native engineering systems preserve continuity and update their operational
organization through appropriately scoped evidence and feedback.
```

#### Meaning

An engineering system preserves useful decisions, boundaries, contracts, and behavior while allowing verified feedback to update the correct layer.

Feedback may update:

```text
working context
interpretation or model
plan
task state
decision
implementation
product knowledge
skill
workflow
contract proposal
domain understanding
```

#### Boundary

```text
One result is not automatically a universal law.
One implementation cannot silently redefine core.
Feedback supports only claims within its source and coverage.
Core evolution requires explicit review, compatibility analysis, and authority.
```

#### Existing operational expressions

```text
failed verification loops back to implementation
review feedback loops back to implementation
verified product lessons may become learning candidates
shared promotion requires reusable reasoning and regression evidence
contract changes require governed compatibility review
```

---

## 6. Required Foundation Distinctions

Later philosophy artifacts and domain models must preserve these distinctions:

```text
observation ≠ interpretation
interpretation ≠ fact
assumption ≠ decision
decision ≠ authority
claim ≠ evidence
capability ≠ permission
plan ≠ execution
contract ≠ implementation
static conformance ≠ executable behavior
verification ≠ complete product validation
review verdict ≠ approval authority
memory ≠ source-of-truth knowledge
local success ≠ universal reusable law
feedback ≠ final truth
stability ≠ immutability
```

Collapsing these distinctions creates false certainty, false authority, false completion, or unsafe evolution.

---

## 7. Derivation Rules

### Axioms

An axiom must be:

```text
minimal
necessary for the framework
bounded in scope
non-metaphysical
not merely a preferred practice
usable to derive multiple downstream rules
```

### Laws

A law must:

```text
identify the axiom or bridge law from which it is derived
state the relationship or invariant clearly
include boundaries and counterexamples
explain its engineering consequence
avoid becoming an untraceable slogan
```

### Principles

A principle expresses a preferred decision orientation.

```text
A principle guides.
A principle does not silently block execution.
```

When violation must block action, the requirement belongs in a guardrail, policy, contract rule, or quality gate.

### Guardrails

A guardrail defines a stable mandatory boundary.

```text
A guardrail must state what must or must not happen.
A guardrail should be testable or reviewable where possible.
A guardrail must identify its scope and escalation behavior.
```

### Mechanisms

Mechanisms operationalize the philosophy without redefining it.

Examples:

```text
Development Loop
Decision Provenance
Adapter Conformance
Skill Evolution
Domain-Driven Model
Engineering Contract
```

A mechanism answers how a responsibility is performed. The philosophy explains why the responsibility exists and what invariant it preserves.

---

## 8. Candidate Derived-Law Families

The next slice must derive and review at least these candidate law families:

```text
Evidence–Model Separation
Model Recognition
Traceability
Capacity
Smallest Coherent Change
Coherence
Embodiment
Feedback
Evolution
```

Their current candidate statements remain in the discovery report until explicit derivation and counterexample review are completed.

No candidate law becomes canonical merely because it appears in an issue or discovery document.

---

## 9. Cross-Domain Applicability

The foundation must govern reasoning across capability domains without turning every domain into engineering implementation.

Representative applicability includes:

```text
analysis
planning
product
research
design
engineering
marketing and growth
content and communication
security
operations and reliability
governance and quality
skill and workflow refinement
runtime and tool operations
```

The same foundation may produce different domain-specific evidence, guardrails, workflows, and reviewers.

Example:

```text
Design evidence may require viewport, interaction, accessibility, and product coverage.
Engineering evidence may require tests, build, lint, runtime, and architecture review.
Marketing evidence may require product truth, claim authority, experiment scope, and metrics.
```

The philosophy defines the common distinctions and update discipline. Domain contracts define the specialized requirements.

---

## 10. Candidate Epistemic Loop

The cross-domain epistemic loop is currently:

```text
OBSERVE
→ ASSESS CAPACITY
→ DECOMPOSE THE MODEL
→ SELECT A TESTABLE RESPONSE
→ READ EVIDENCE
→ UPDATE
```

This loop governs how work reasons about state and evidence.

It is not a replacement for:

```text
product-development workflow
new-feature workflow
bugfix workflow
redesign workflow
deployment workflow
marketing workflow
incident workflow
```

Its detailed semantics remain to be formalized in a dedicated philosophy artifact after the kernel and derived laws are reviewed.

---

## 11. Evolution Boundary

More concrete layers may apply, translate, test, and challenge the philosophy.

They may not silently redefine it.

```text
implementation result
→ bounded evidence
→ learning candidate
→ generalization and counterexample review
→ target-layer decision
→ compatibility and authority review
→ accepted update or rejection
```

The correct destination may be:

```text
local implementation
product knowledge or policy
skill or reference
workflow
behavioral evaluation
contract
canonical term
domain model
philosophy evolution proposal
```

Promotion must choose the smallest correct shared layer.

---

## 12. Source-Role Governance

Each artifact should have one primary authority role.

| Artifact role | Owns | Must not become |
|---|---|---|
| Philosophy / Doctrine | Framework purpose and durable orientation | Workflow instructions |
| Axiom | Minimal foundational assumption | Broad principle list |
| Law | Derived invariant and dependency | Untraceable slogan |
| Principle | Preferred decision orientation | Hidden mandatory rule |
| Guardrail | Stable must/must-not boundary | Optional advice |
| Canonical Term | One authoritative definition | Complete domain model |
| Domain Map | Relationships between terms | Parallel definition authority |
| Mechanism / Module | Reusable operational structure | Axiom by implication |
| Contract | Stable machine-readable agreement | Full executable methodology |
| Adapter Translation | Runtime or product binding | Core redefinition |
| Implementation Evidence | Observed execution result | Universal truth |
| Field Test | Bounded real-world validation | Automatic core change |
| Stability / Freeze Review | Readiness and contradiction review | New foundation content |

---

## 13. Non-Goals

This philosophy does not:

```text
copy psychological, spiritual, somatic, therapeutic, religious,
or metaphysical doctrine from Manuscript Kesadaran

claim universal scientific truth beyond Native AI Engineering

select a model provider, agent runtime, repository provider,
framework, deployment platform, or product architecture

replace domain-driven design, ports and adapters, contracts,
skills, workflows, evaluation, or product validation

make every principle a mandatory runtime rule

make every feedback result eligible for core promotion
```

`puterakahfi/manuscript-kesadaran/core` is an architectural reference for foundation discipline and source-role separation, not a domain dependency of Native AI Engineering.

---

## 14. Maturity And Next Work

Current status:

```text
Canonical philosophy entry point: ESTABLISHED
Doctrine wording: CANDIDATE
Axiom set: CANDIDATE
Bridge law: CANDIDATE
Derived laws: DISCOVERY ONLY
Principles: NOT YET CANONICAL
Guardrails: DISTRIBUTED, NOT YET CANONICALIZED
Canonical philosophy terms: NOT YET DEFINED
Epistemic loop: CANDIDATE
Domain model consumption readiness: NOT YET
```

Next required work:

1. derive candidate laws explicitly from the kernel;
2. add boundaries, negative cases, and counterexamples;
3. classify existing statements as law, principle, guardrail, mechanism, or gate;
4. define canonical philosophy terms and authority rules;
5. formalize the epistemic loop;
6. create a philosophy-to-existing-source traceability matrix;
7. stress-test the foundation across representative capability domains;
8. complete contradiction and terminology review;
9. mark the accepted foundation ready for `#6` consumption.

Until those gates pass, this entry point is authoritative for navigation and status, while its doctrine and kernel statements remain candidate foundation content.
