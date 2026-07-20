# Native AI Engineering Derived Laws

Status: Candidate foundation

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Discovery source: [`../native-ai-engineering-philosophy-discovery.md`](../native-ai-engineering-philosophy-discovery.md)

This document is the candidate authority for philosophy-level law derivation in Native AI Engineering.

It records how each law is derived from the candidate kernel, what the law means, where it applies, what it does not claim, how it can fail, and what engineering consequences follow.

The laws remain candidates until cross-domain stress tests, terminology review, contradiction review, and issue `#13` acceptance are complete.

---

## 1. Purpose

The philosophy entry point defines two candidate epistemic axioms and one bridge law:

```text
A1 — Engineering work begins from available, attributable state.

A2 — Observed or recorded state is not identical to a human, agent,
     document, or system model of that state.

BL — AI-native engineering systems preserve continuity and update their
     operational organization through appropriately scoped evidence and feedback.
```

This document derives reusable engineering laws from that kernel.

A derived law must:

```text
identify its source axiom or bridge law
state a durable relationship or invariant
remain bounded to Native AI Engineering
include counterexamples and failure modes
produce concrete engineering consequences
avoid becoming an untraceable slogan
```

---

## 2. Classification Result

The discovery issue proposed nine candidate law families. Derivation review produced the following classification:

| Discovery candidate | Result | Canonical candidate destination |
|---|---|---|
| Evidence–Model Separation | Refined and split | State–Model Separation Law + Claim–Evidence Scope Law |
| Model Recognition | Retained and refined | Model Recognition Law |
| Traceability | Retained and expanded | Decision Traceability Law |
| Capacity | Retained and expanded | Execution Capacity Law |
| Smallest Coherent Change | Reclassified | Principle, not law |
| Coherence | Retained and refined | Coherent Completion Law |
| Embodiment | Retained and refined | Executable Embodiment Law |
| Feedback | Retained and split | Feedback Revision Law + Claim Maturity consequence |
| Evolution | Retained and expanded | Evolution Authority Law + Governed Stability Law |

### Why `Smallest Coherent Change` is not a law

The statement:

```text
Prefer the smallest change that preserves system coherence
and can produce meaningful verification evidence.
```

contains `prefer`, which expresses a decision orientation rather than an invariant.

It is therefore a candidate principle:

```text
Smallest Coherent Change Principle
```

It may later produce enforceable guardrails such as scope-control gates, but it should not be presented as a law merely because it is broadly useful.

---

## 3. Law Dependency Map

```text
A1 Available, Attributable State
│
├── L1 State Attribution Law
│   ├── L4 Claim–Evidence Scope Law
│   ├── L5 Decision Traceability Law
│   └── L7 Execution Capacity Law
│
A2 State Is Not Identical To Its Model
│
├── L2 State–Model Separation Law
│   ├── L3 Model Recognition Law
│   ├── L4 Claim–Evidence Scope Law
│   ├── L5 Decision Traceability Law
│   └── L8 Coherent Completion Law
│
BL Evidence And Feedback Update The System
│
├── L7 Execution Capacity Law
├── L8 Coherent Completion Law
├── L9 Executable Embodiment Law
├── L10 Feedback Revision Law
├── L11 Evolution Authority Law
└── L12 Governed Stability Law
```

Cross-derived law:

```text
L6 Capability–Authority Separation Law
  derives from A1 + A2 + doctrine-level authority boundaries.
```

---

# 4. L1 — State Attribution Law

## Statement

```text
A material engineering claim about state must identify an attributable source,
or remain explicitly unknown, unavailable, blocked, or not verified.
```

## Derived from

```text
A1 — Engineering work begins from available, attributable state.
```

## Derivation

1. Engineering begins from available state.
2. Available state is always obtained through some bounded source, access path, observation time, or evidence surface.
3. Without source attribution, downstream actors cannot determine whether a state claim was observed, inferred, remembered, generated, or fabricated.
4. Therefore material state claims require attribution or an explicit unresolved status.

## Applies to

```text
user instructions
issue and acceptance-criteria state
repository and branch state
file and implementation state
runtime and deployment state
test and validation results
review and approval records
tool and permission state
product behavior
metrics and experiment results
```

## Boundaries

```text
Attribution does not guarantee that a source is authoritative.
Attribution does not guarantee that observation coverage is complete.
A source may be real but stale, partial, superseded, or outside the claim scope.
Not every low-risk descriptive statement requires formal provenance metadata.
```

## Counterexamples

Not a violation:

```text
“The current branch could not be confirmed because repository access failed.”
```

This preserves unknown state honestly.

Violation:

```text
“The active branch is feature-x.”
```

when no repository, tool output, or user statement supports that claim.

## Failure modes

```text
invented repository paths
invented issue status
fabricated test output
remembered decisions treated as current state
screenshots treated as complete product state
unattributed summaries treated as source of truth
```

## Engineering consequences

Systems implementing this law should support:

```text
source references
observation timestamps where material
availability and coverage status
UNKNOWN / BLOCKED / NOT_VERIFIED states
explicit distinction between observed and inferred fields
prohibition against fabricated completion evidence
```

---

# 5. L2 — State–Model Separation Law

## Statement

```text
A representation of engineering state must remain distinguishable from the state
it represents, including its source, scope, assumptions, and verification status.
```

## Derived from

```text
A2 — State is not identical to its model.
```

## Derivation

1. Agents, humans, documents, plans, diagrams, prompts, contracts, and memories all use models.
2. A model selects, compresses, interprets, predicts, or reorganizes state.
3. Selection and interpretation create the possibility of omission, drift, contradiction, and error.
4. Therefore the system must preserve the distinction between state and model rather than treating the model as self-validating reality.

## Common state–model pairs

```text
repository state ≠ repository summary
user intent ≠ inferred intent
issue text ≠ task interpretation
architecture diagram ≠ implementation
plan ≠ execution
contract ≠ implementation
contract declaration ≠ conformance
skill declaration ≠ skill application
review verdict ≠ evidence itself
memory ≠ source-of-truth knowledge
metric ≠ complete product meaning
```

## Boundaries

```text
The law does not claim that models are inherently unreliable.
The law does not prohibit decisions based on verified models.
The law does not require every model to reproduce all underlying state.
Useful abstraction remains necessary.
```

The requirement is that model identity, limits, and status remain visible enough for the claim and risk involved.

## Counterexamples

Not a violation:

```text
An architecture diagram is used to guide implementation after reviewers confirm
that it is the accepted target architecture.
```

Violation:

```text
The diagram is cited as proof that the implementation currently follows it.
```

## Failure modes

```text
plan-as-execution
prompt-as-domain-model
contract-as-proof
summary-as-authority
test-as-total-correctness
mockup-as-complete-UX-validation
metric-as-user-truth
agent-confidence-as-evidence
```

## Engineering consequences

Models should expose, where relevant:

```text
model type
source inputs
scope
assumptions
unknowns
version or time boundary
verification status
relationship to authoritative state
```

---

# 6. L3 — Model Recognition Law

## Statement

```text
An inference, assumption, hypothesis, or generated interpretation that is not
marked as such cannot be reliably distinguished from fact by downstream actors
and may therefore be executed as if it were fact.
```

## Derived from

```text
A2 — State is not identical to its model.
L2 — State–Model Separation Law.
```

## Derivation

1. A model can contain observed facts, interpretations, assumptions, and predictions.
2. Downstream systems frequently consume the representation without reconstructing how each statement was produced.
3. When epistemic status is omitted, downstream execution loses the ability to distinguish evidence-backed state from model-generated content.
4. Therefore unmarked assumptions create false certainty and unsafe execution risk.

## Required epistemic statuses

Material statements should be distinguishable as appropriate:

```text
OBSERVED
RECORDED
INFERRED
ASSUMED
HYPOTHESIS
DECIDED
APPROVED
UNKNOWN
CONTRADICTED
NOT_VERIFIED
SUPERSEDED
```

The final status vocabulary belongs to canonical term work. This law requires the distinction, not these exact labels.

## Boundaries

```text
Not every sentence requires an explicit status tag.
Conversational brevity is allowed when context makes the status unambiguous.
The law becomes stricter as consequence, irreversibility, risk, or reuse increases.
```

## Counterexamples

Not a violation:

```text
“I infer that the type error is caused by the generic return type; this still
needs verification against the current source.”
```

Violation:

```text
“The generic return type is the root cause.”
```

when the source was not inspected and no test reproduced the failure.

## Failure modes

```text
hallucinated implementation status
premature root-cause certainty
silent requirement invention
unapproved design lock
fabricated user preference
unverified marketing claim
implicit permission expansion
```

## Engineering consequences

Execution systems should preserve uncertainty instead of resolving it through invented certainty.

When a material assumption cannot be verified, the system should:

```text
narrow the claim
mark the uncertainty
seek evidence
route for decision or approval
choose a reversible test
or block dependent action
```

---

# 7. L4 — Claim–Evidence Scope Law

## Statement

```text
The strength, scope, and maturity of an engineering claim must not exceed the
source, coverage, quality, and relevance of the evidence supporting it.
```

## Derived from

```text
A1 — Engineering begins from available, attributable state.
A2 — State is not identical to its model.
L1 — State Attribution Law.
L2 — State–Model Separation Law.
```

## Derivation

1. Evidence is observed or recorded state with bounded source and coverage.
2. Claims are models or conclusions built from that evidence.
3. Evidence from one surface cannot establish unrelated or broader properties automatically.
4. Therefore claim scope must remain bounded by what the evidence actually supports.

## Evidence-layer examples

```text
contract path resolution
version compatibility
static conformance
behavioral evaluation
runtime integration
security review
product acceptance
human approval
business outcome
regression evidence
```

Passing one layer does not prove the others.

## Boundaries

```text
The law does not require perfect evidence before every action.
Exploratory and reversible work may proceed with explicitly weaker claims.
The required evidence strength depends on consequence, risk, and claim type.
```

## Counterexamples

Not a violation:

```text
“The unit tests passed for the changed module; end-to-end product behavior was
not verified.”
```

Violation:

```text
“The feature is complete and production-ready.”
```

based only on a successful unit test or build.

## Failure modes

```text
build-as-product-validation
static-conformance-as-runtime-proof
screenshot-as-interaction-proof
review-verdict-as-owner-approval
one-metric-as-market-validation
one-field-test-as-universal-law
absence-of-error-as-success
```

## Engineering consequences

Every material completion or quality claim should make clear:

```text
what was checked
what evidence was produced
what claim the evidence supports
what was not checked
what remains uncertain or delegated
```

---

# 8. L5 — Decision Traceability Law

## Statement

```text
A material engineering decision is trustworthy only to the degree that its
source, authority, scope, rationale, evidence, conflicts, and supersession chain
can be traced.
```

## Derived from

```text
A1 — Available state requires attribution.
A2 — A decision record is a model, not authority by itself.
L1 — State Attribution Law.
L2 — State–Model Separation Law.
L4 — Claim–Evidence Scope Law.
```

## Derivation

1. A decision changes what actions are permitted, required, blocked, or considered complete.
2. A recorded decision can be stale, unauthoritative, out of scope, contradicted, or superseded.
3. Recency or existence alone does not establish authority.
4. Therefore material decisions require a traceable provenance and conflict chain.

## Material decision domains

```text
scope
architecture
ownership
approval
risk acceptance
security exception
lock or preservation rule
routing
status
release readiness
destructive action
core evolution
```

## Boundaries

```text
Traceability does not require bureaucratic ceremony for every trivial choice.
The required record depth grows with impact, persistence, risk, and number of consumers.
A traceable decision can still be wrong; traceability enables review and correction.
```

## Counterexamples

Not a violation:

```text
A local variable rename follows existing style without a separate ADR.
```

Violation:

```text
A repository architecture is changed because an agent-authored issue summary
says the owner approved it, but no attributable approval exists.
```

## Failure modes

```text
newest-source-wins
silence-as-approval
implementation-existence-as-intent
agent-summary-as-owner-authority
unresolved-conflict-hidden
implicit-supersession
scope-expansion-from-narrow-instruction
```

## Engineering consequences

Material decisions should support:

```text
decision identity
decision type
applies-to scope
required and observed authority
source reference
rationale
evidence
conflicts
supersedes / superseded-by
permitted and blocked actions
verification status
```

---

# 9. L6 — Capability–Authority Separation Law

## Statement

```text
The capability to execute an action does not by itself grant the permission,
authority, approval, or policy right to execute that action.
```

## Derived from

```text
A1 — Tool, permission, and authority state must be observed.
A2 — Capability is not identical to authority.
Doctrine — Domain authority and risk boundaries remain explicit and reviewable.
```

## Derivation

1. Tools and agents may possess technical capability beyond the scope of a task or decision.
2. Capability answers whether an action can be executed.
3. Authority answers whether the action may be executed and who owns its consequences.
4. Conflating them permits silent scope expansion and destructive action.
5. Therefore capability and authority must remain separate.

## Applies especially to

```text
repository writes
force push
branch deletion
production deployment
data deletion
credential use
security exceptions
financial or legal claims
owner approval claims
core contract changes
public publishing
```

## Boundaries

```text
Authority may be delegated by explicit policy or workflow.
Low-risk autonomous execution may be authorized in advance.
The law does not require interactive approval for every permitted operation.
```

## Counterexamples

Not a violation:

```text
A CI adapter deploys automatically because an accepted release policy explicitly
authorizes deployment after all gates pass.
```

Violation:

```text
An agent force-pushes because the repository token technically allows it.
```

## Failure modes

```text
tool-access-as-authorization
write-access-as-scope
owner-silence-as-consent
runtime-capability-as-product-policy
admin-permission-as-review-approval
```

## Engineering consequences

Systems should model separately:

```text
capability availability
permission
policy
required authority
approval status
risk level
reversibility
allowed scope
```

---

# 10. L7 — Execution Capacity Law

## Statement

```text
Execution scope must not exceed the available context, capability, tools,
permission, authority, risk controls, validation path, and review capacity
required for that scope.
```

## Derived from

```text
A1 — Work begins from available state.
BL — Systems update through evidence and feedback.
L1 — State Attribution Law.
L6 — Capability–Authority Separation Law.
```

## Derivation

1. Engineering action requires enough state to choose and bound the action.
2. Execution also requires capability, tools, authority, and risk controls.
3. A trustworthy update requires an evidence and review path proportionate to the claim.
4. When one required capacity dimension is missing, the intended scope cannot be completed responsibly as stated.
5. Therefore the system must narrow, pause, route, block, or explicitly downgrade the claim.

## Capacity dimensions

```text
context availability
source coverage
domain and technical capability
tool availability
permission
authority and approval
risk controls
reversibility
time and scope budget
validation path
review coverage
rollback capacity
```

## Boundaries

```text
Capacity is contextual, not a fixed property of an agent or team.
Insufficient capacity for a full task may still allow safe discovery or a smaller test.
The law does not justify indefinite analysis when adequate capacity exists.
```

## Counterexamples

Not a violation:

```text
Repository writes are unavailable, so the agent produces a verified patch plan
and labels implementation as blocked.
```

Violation:

```text
The agent claims the implementation is complete despite lacking repository write
access and any evidence that another actor applied the patch.
```

## Failure modes

```text
scope larger than context
implementation without validation path
security-sensitive change without review coverage
production change without rollback capacity
full UX claim from one viewport
market conclusion from unmeasured campaign
```

## Engineering consequences

When capacity is insufficient, valid transitions include:

```text
NARROW
PAUSE
ROUTE
REQUEST AUTHORITY
CHOOSE A REVERSIBLE EXPERIMENT
MARK PARTIAL
MARK BLOCKED
STOP
```

The system must not resolve insufficient capacity by fabricating certainty or completion.

---

# 11. L8 — Coherent Completion Law

## Statement

```text
A system must not claim coherent completion while unresolved material
contradictions remain between authoritative intent, requirements, contracts,
architecture, implementation, behavior, evidence, and approval state.
```

## Derived from

```text
A2 — Models and state remain distinct.
BL — Feedback updates the operational organization.
L4 — Claim–Evidence Scope Law.
L5 — Decision Traceability Law.
```

## Derivation

1. Native AI Engineering coordinates multiple models and state surfaces.
2. A local success can coexist with contradictions elsewhere.
3. Completion is a system-level claim, not merely a local execution event.
4. Material contradictions show that the relevant system has not yet converged on one supportable state.
5. Therefore completion requires contradiction resolution, explicit acceptance, or honest limitation.

## Material coherence surfaces

```text
user intent
acceptance criteria
domain rules
architecture and engineering contracts
implementation
runtime behavior
security and governance constraints
test and evaluation evidence
review verdict
approval authority
delivery state
```

## Boundaries

```text
Perfect global consistency is not required.
Non-material differences may remain.
Known limitations may be accepted explicitly by the correct authority.
The law applies to the scope of the completion claim.
```

## Counterexamples

Not a violation:

```text
“The backend acceptance criteria are complete; mobile interaction validation is
out of scope for this issue.”
```

Violation:

```text
“The redesign is complete.”
```

when the desktop mockup passes review but mobile navigation remains unusable and mobile coverage was part of the accepted scope.

## Failure modes

```text
local-green-global-broken
requirements-code-drift
contract-implementation-drift
approval-review-conflation
known-failure-hidden
partial-evidence-full-completion
```

## Engineering consequences

Completion reports should distinguish:

```text
COMPLETED
PARTIAL
BLOCKED
NOT_VERIFIED
NOT_APPLICABLE
ACCEPTED_WITH_LIMITATION
```

Exact result semantics belong to contracts and domain modeling, but philosophy requires honest differentiation.

---

# 12. L9 — Executable Embodiment Law

## Statement

```text
A principle, rule, contract, skill, or workflow is embodied by a system only when
it changes repeatable executable behavior and that behavior can produce
appropriate evidence.
```

## Derived from

```text
A2 — Declaration or representation is not identical to behavior.
BL — Systems update and stabilize through evidence and feedback.
L4 — Claim–Evidence Scope Law.
L8 — Coherent Completion Law.
```

## Derivation

1. Documentation, contracts, and skills are representations of intended behavior.
2. Intended behavior may be ignored, misrouted, partially implemented, or unavailable at runtime.
3. Presence of the representation therefore does not prove application.
4. A principle becomes operational only when repeatable execution changes and the change can be evaluated.
5. Therefore embodiment requires behavior and evidence, not declaration alone.

## Examples

```text
“test first” in documentation only                 = declared
TDD routing + executable tests + evidence          = embodied candidate

“approval required” in prose only                  = declared
policy gate + blocked action + approval record     = embodied candidate

skill installed                                    = available
skill selected, applied, and behavior evaluated    = embodied candidate
```

## Boundaries

```text
Embodiment does not require perfect execution in every case.
A single successful execution is evidence, not final stabilization.
Some principles may intentionally remain advisory and not runtime-enforced.
```

## Counterexamples

Not a violation:

```text
A principle is explicitly labeled advisory and is reviewed qualitatively rather
than enforced by a hook.
```

Violation:

```text
The system claims a safety principle is implemented because it appears in a
README, while destructive actions bypass it at runtime.
```

## Failure modes

```text
documentation-theater
contract-theater
skill-installation-as-application
gate-declared-but-not-executed
review-checklist-without-evidence
```

## Engineering consequences

Embodiment evaluation may require:

```text
routing evidence
execution traces without private chain of thought
tool-call and approval records
behavioral evaluation
runtime integration tests
product evidence
regression protection
```

---

# 13. L10 — Feedback Revision Law

## Statement

```text
Appropriately scoped feedback must be able to revise the working model,
plan, decision, implementation, or other affected layer; a material claim is not
mature when relevant contradictory feedback remains unprocessed.
```

## Derived from

```text
BL — Engineering systems update through evidence and feedback.
A2 — The current model may differ from state.
L4 — Claim–Evidence Scope Law.
L8 — Coherent Completion Law.
```

## Derivation

1. The bridge law defines feedback as the mechanism of operational update.
2. Feedback can reveal mismatch between model and state.
3. A system that records feedback but prevents it from changing the affected layer is not actually updating.
4. A claim that ignores material contradictory feedback remains immature.
5. Therefore relevant feedback must participate in revision or be explicitly rejected with traceable rationale and authority.

## Feedback surfaces

```text
verification failure
review finding
runtime behavior
security finding
accessibility finding
user correction
product acceptance result
business metric
incident
regression
field test
consumer compatibility finding
```

## Boundaries

```text
Feedback is not automatically correct or authoritative.
Feedback must be evaluated for source, scope, quality, and relevance.
A rejected feedback item can still satisfy the law when rejection is reasoned and traceable.
One result is not final truth.
```

## Counterexamples

Not a violation:

```text
A review request is rejected because it conflicts with an authoritative product
lock; the conflict and rationale are recorded.
```

Violation:

```text
A failed runtime check is ignored while the system continues to claim completion
because static tests passed.
```

## Failure modes

```text
feedback-collected-not-used
review-as-ceremony
failed-test-overridden-by-confidence
user-correction-not-propagated
metric-cherry-picking
regression-not-fed-back-into-skill-or-test
```

## Engineering consequences

Feedback processing should support:

```text
ACCEPT
REJECT WITH RATIONALE
NARROW CLAIM
REVISE
RETEST
ESCALATE
CREATE LEARNING CANDIDATE
PROPOSE CORE EVOLUTION
```

---

# 14. L11 — Evolution Authority Law

## Statement

```text
A more concrete layer may apply, translate, test, and propose changes to a more
canonical layer, but it may not silently redefine that layer without the
canonical layer's review, compatibility analysis, and authority.
```

## Derived from

```text
BL — Systems preserve continuity while updating through feedback.
L5 — Decision Traceability Law.
L10 — Feedback Revision Law.
Doctrine — Core authority and repository boundaries remain explicit.
```

## Derivation

1. Implementation and field evidence are required for learning.
2. Local evidence is bounded to a product, runtime, adapter, context, and test surface.
3. Shared or canonical layers have broader consumers and compatibility obligations.
4. Direct local mutation of canonical meaning would allow one implementation to redefine all consumers silently.
5. Therefore local learning may propose, but canonical authority must review and accept the evolution.

## Dependency direction

```text
philosophy and canonical language
→ domain model
→ contracts and ports
→ skills, workflows, and adapters
→ runtime and product implementation
→ bounded evidence
→ reviewed evolution proposal
```

## Valid promotion path

```text
implementation result
→ bounded evidence
→ reusable reason
→ counterexample and transferability review
→ target-layer decision
→ compatibility analysis
→ required authority
→ accepted update or rejection
```

## Boundaries

```text
This law does not prevent bottom-up learning.
It does not make core immune to evidence.
Emergency local fixes may occur without immediate shared promotion.
The law governs canonicalization, not every local edit.
```

## Counterexamples

Not a violation:

```text
A product-specific responsive navigation fix is retained in the product repo,
then used to propose a reusable interaction rule after multi-context review.
```

Violation:

```text
A skill copies one product's breakpoint, component name, and route into a universal
core contract because the local fix succeeded once.
```

## Failure modes

```text
adapter-as-core
product-policy-as-universal-law
runtime-binding-as-domain-definition
one-case-as-skill-rule
one-case-as-core-law
silent-contract-evolution
product-history-polluting-reusable-skill
```

## Engineering consequences

Every learning candidate should choose the smallest correct destination:

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

---

# 15. L12 — Governed Stability Law

## Statement

```text
A stable Native AI Engineering artifact is protected by explicit ownership,
compatibility rules, evidence, review, and controlled evolution; stability does
not mean immutability.
```

## Derived from

```text
BL — Systems preserve continuity and update through feedback.
L10 — Feedback Revision Law.
L11 — Evolution Authority Law.
```

## Derivation

1. The framework must preserve continuity so consumers can rely on shared agreements.
2. The framework must also update when evidence reveals gaps or changed needs.
3. Immutability would prevent learning; uncontrolled change would destroy trust and compatibility.
4. Therefore stability is governed change, not absence of change.

## Stability mechanisms

```text
canonical ownership
semantic versioning
compatibility classification
explicit supersession
consumer impact review
migration guidance
behavioral evaluation
regression evidence
freeze or release review
```

## Boundaries

```text
Not every artifact requires semantic versioning.
Early release candidates may evolve more rapidly when breakage is disclosed.
Stability does not guarantee correctness; it guarantees governed expectations.
```

## Counterexamples

Not a violation:

```text
A release-candidate law is refined after counterexample review, with the change
recorded and downstream consumers rechecked.
```

Violation:

```text
A canonical term changes meaning silently while contracts and adapters continue
using the old meaning.
```

## Failure modes

```text
stable-as-frozen-dogma
change-without-compatibility-review
silent-semantic-drift
new-file-as-parallel-authority
legacy-document-competing-with-canonical-source
```

## Engineering consequences

Stable artifacts should define or inherit:

```text
owner
status
change authority
compatibility expectations
supersession behavior
validation requirements
consumer update responsibility
```

---

## 16. Cross-Law Invariants

The laws together preserve the following invariants:

```text
state remains attributable
models remain recognizable as models
uncertainty remains visible
claims remain bounded by evidence
decisions remain traceable
capability remains separate from authority
scope remains inside execution capacity
completion remains coherent with material evidence
principles require behavior before embodiment claims
feedback can revise the correct layer
local learning cannot silently redefine core
stable artifacts can evolve without silent drift
```

---

## 17. Cross-Domain Stress Examples

### Analysis

```text
Observed repository structure is attributed.
Inferred architecture is marked as inference.
Missing files remain unknown.
Analysis claims do not exceed inspected coverage.
```

Relevant laws:

```text
L1, L2, L3, L4, L7
```

### Planning

```text
A plan is treated as a model of intended work.
Dependencies and assumptions remain explicit.
The plan stays within available validation and authority capacity.
```

Relevant laws:

```text
L2, L3, L5, L7, L8
```

### Design

```text
A screenshot is not treated as complete interaction evidence.
Aesthetic preference is separated from observed usability failure.
Viewport and accessibility gaps block full completion claims when in scope.
```

Relevant laws:

```text
L2, L4, L7, L8, L10
```

### Engineering

```text
A successful build supports a build claim, not total product correctness.
Tool access does not grant destructive-action authority.
Failed tests revise implementation before completion.
```

Relevant laws:

```text
L4, L6, L7, L8, L10
```

### Marketing and growth

```text
Audience hypotheses are not presented as market facts.
Generated promises require product truth and approval authority.
Experiment results update only claims inside the experiment scope.
```

Relevant laws:

```text
L1, L3, L4, L5, L10
```

### Runtime and tool operations

```text
Installed skill availability is not treated as skill application.
Execution capability remains separate from permission.
Runtime evidence can propose but not silently redefine core.
```

Relevant laws:

```text
L6, L7, L9, L11
```

### Skill refinement

```text
A verified local case becomes a bounded learning candidate.
Reusable reasoning is separated from product implementation detail.
Promotion chooses the smallest correct shared layer.
```

Relevant laws:

```text
L4, L9, L10, L11, L12
```

---

## 18. Common False Equivalences Prohibited By The Laws

```text
available tool              ≠ authorized action
observed implementation     ≠ intended scope
agent-authored summary      ≠ owner approval
plan                        ≠ execution
contract                    ≠ implementation
contract declaration        ≠ conformance
static conformance          ≠ executable behavior
skill installed             ≠ skill applied
build passed                ≠ product validated
review passed               ≠ required approval granted
screenshot looks correct    ≠ UX validated
metric changed              ≠ causal business conclusion
feedback received           ≠ feedback accepted
local fix succeeded         ≠ universal rule established
stable                      ≠ immutable
```

---

## 19. Validation Gates Before Acceptance

These candidate laws must not be marked accepted until:

- [ ] every law has a clear kernel derivation;
- [ ] every law has boundaries and at least one counterexample;
- [ ] normative statements are not mislabeled as empirical scientific laws;
- [ ] principles are not hidden inside law wording;
- [ ] laws remain engineering-specific and non-metaphysical;
- [ ] laws apply coherently across analysis, planning, design, engineering, marketing, operations, and skill refinement;
- [ ] existing contracts and mechanisms can map to the laws without being duplicated;
- [ ] terminology is reconciled with canonical term work;
- [ ] contradictions with architecture, glossary, rules, and contracts are reviewed;
- [ ] issue `#13` records an explicit acceptance or requested revision.

---

## 20. Current Verdict

```text
Kernel derivation coverage: COMPLETE FOR CANDIDATE REVIEW
Candidate law families reviewed: COMPLETE
Smallest Coherent Change classification: PRINCIPLE
Law boundaries and counterexamples: PRESENT
Cross-domain applicability: INITIAL PASS
Canonical term dependencies: NOT YET COMPLETE
Cross-document contradiction review: PARTIAL
Law acceptance status: CANDIDATE
Ready for principles and guardrails classification: YES
Ready for domain model consumption: NOT YET
```

The next philosophy slice should classify existing orienting statements and mandatory constraints into:

```text
principles
mandatory guardrails
mechanisms
gates
policies
```

without weakening the executable rules already present in contracts and runtime behavior.
