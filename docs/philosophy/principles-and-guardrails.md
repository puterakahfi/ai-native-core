# Native AI Engineering Principles And Guardrails

Status: Final candidate retained set

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Retained laws: [`laws.md`](laws.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Behavioral candidates: [`behavioral-test-candidates.md`](behavioral-test-candidates.md)

Pruning record: [`reconciliation-and-pruning.md`](reconciliation-and-pruning.md)

This file owns the active candidate principles and philosophy guardrails retained after usefulness, duplicate-response, contradiction, and minimality review.

Stable names are primary identifiers. Historical `P` and `G` numbers are traceability aliases only.

---

## 1. Classification Boundary

```text
Law
= derived invariant.

Principle
= preferred orientation when multiple valid choices remain.

Guardrail
= universal mandatory boundary whose violation changes action, routing, or status.

Mechanism
= reusable operational structure.

Gate
= checkable transition or claim condition.

Policy
= authority-selected rule for a bounded repository, product, runtime, risk, or organization.
```

A principle must allow justified alternatives. A guardrail must define an operational consequence.

Valid guardrail responses include:

```text
BLOCK;
STOP;
NARROW;
ROUTE;
REQUEST SOURCE;
REQUEST EVIDENCE;
REQUEST AUTHORITY;
REQUEST APPROVAL;
REQUIRE REVIEW;
REQUIRE RECOVERY CAPACITY;
MARK UNKNOWN;
MARK PARTIAL;
MARK NOT_VERIFIED;
REVERT;
ESCALATE.
```

A local policy may strengthen a guardrail in its context. It must not be promoted into universal philosophy merely because it is mandatory locally.

---

## 2. Retention Rule

A principle is retained only when it:

```text
changes selection among otherwise valid approaches;
has a named consumer;
prevents a known failure or improves a material trade-off;
is not already mandatory under a law or guardrail;
is not a repository or product policy.
```

A guardrail is retained only when it:

```text
protects a distinct invariant;
has a distinguishable trigger;
requires a distinguishable response;
has an embodiment or review path;
is not only an example of another retained guardrail.
```

---

## 3. Retained Principles

| Principle | Alias | Selection responsibility |
|---|---:|---|
| Domain And Capability Before Tools | P1 | Define product/domain responsibility before allowing replaceable tools to shape meaning |
| Smallest Coherent Change | P2 | Select the narrowest change preserving required coherence and evidence quality |
| Reversible Progress Under Uncertainty | P5 | Prefer bounded reversible tests when action is justified but uncertainty remains |
| Correct-Layer Change | P6 | Change the narrowest layer that legitimately owns the problem |
| Evaluation Before Trust Expansion | P8 | Expand trust, autonomy, rollout, or canonical status only after proportionate evaluation |
| Review Proportional To Risk And Authority | P9 | Select review and approval depth according to risk, reversibility, authority, and consumer impact |
| Explicit Boundaries Over Implicit Expectations | P11 | Prefer explicit ownership, scope, exclusions, handoffs, and approval boundaries |

Count: `7`.

Retired independent candidates:

```text
Evidence-Proportional Claims
→ mandatory consequence of Claim–Evidence Scope and evidence guardrails.

Explicit Uncertainty
→ consequence of State Attribution, State–Model Separation,
  No Fabricated State Or Evidence, and No Model-As-Fact Collapse.

Preserve Useful Existing Work
→ selection factor inside Smallest Coherent Change.

Feedback-Driven Learning
→ consequence of Feedback Revision, Evolution Authority, and UPDATE.
```

---

## 4. Principle Details

### Domain And Capability Before Tools

```text
Prefer defining the user or business capability, domain responsibility,
and required behavior before selecting tools, models, providers, or adapters.
```

Selects for domain-owned meaning, replaceable implementation, capability-first ports, provider-independent contracts, and routing based on responsibility rather than tool availability.

Does not prohibit tools during discovery or require every domain detail to be complete before experimentation.

Primary consumers: `#6`, `#7`, architecture review, capability design, skill routing.

### Smallest Coherent Change

```text
Prefer the smallest change that preserves relevant coherence, useful accepted work,
and meaningful evidence for the objective.
```

“Smallest” means smallest coherent scope, not fewest changed lines. A wider change is justified when a narrower patch would duplicate logic, break ownership, or leave behavior incomplete.

Primary consumers: Development Loop, engineering workflows, redesign, skill refinement, review.

### Reversible Progress Under Uncertainty

```text
When uncertainty is material but action is justified, prefer bounded reversible
experiments that can produce discriminating evidence.
```

Reversibility reduces risk; it does not create permission or authority.

Primary consumers: planning, debugging, experiments, rollout, runtime operations.

### Correct-Layer Change

```text
Prefer changing the narrowest layer that legitimately owns the discovered problem.
```

Possible destinations include local implementation, product policy, knowledge, skill, workflow, evaluation, contract, canonical term, domain model, or philosophy evolution proposal.

Primary consumers: `#6–#9`, Skill Evolution, core contribution review, product-to-shared learning.

### Evaluation Before Trust Expansion

```text
Prefer increasing trust, autonomy, rollout scope, compatibility status, or canonical
status only after proportionate evaluation and feedback.
```

Examples include candidate skill to wider routing, local fix to reusable learning, and release candidate to stable agreement.

Primary consumers: evaluators, release governance, skill registry, runtime routing, core evolution.

### Review Proportional To Risk And Authority

```text
Prefer review and approval coverage proportionate to risk, reversibility,
authority, affected consumers, and claim scope.
```

Human review may be a repository default, but reviewer and approval mode are scoped policies. Low-risk delegated actions may be automated when explicit policy permits.

Primary consumers: risk policy, review ports, release workflows, native-ai-fw.

### Explicit Boundaries Over Implicit Expectations

```text
Prefer explicit ownership, scope, exclusions, handoffs, evidence expectations,
and approval boundaries over assumptions inferred from prose or convention.
```

Structured declarations remain declarations; behavioral claims still require execution evidence.

Primary consumers: `#7–#9`, contracts, adapter conformance, workflow handoffs, control plane.

---

## 5. Retained Guardrails

| Guardrail | Alias | Primary response |
|---|---:|---|
| No Fabricated State Or Evidence | G1 | Mark unknown/not verified, request evidence, block false claim |
| No Model-As-Fact Collapse | G2 | Relabel model status, verify, narrow, or block dependent action |
| No Claim Beyond Evidence Scope | G3 | Narrow/downgrade claim and require broader evidence |
| Capability Is Not Authority | G4 | Route/request authority, choose authorized alternative, or stop |
| No Silent Scope Expansion | G5 | Stop adjacent mutation and request separate scope |
| No Silent Conflict Resolution | G6 | Preserve conflict, request supersession/authority, block dependent mutation |
| No Undeclared Gate Bypass | G7 | Block transition or require explicit shortcut and residual evidence |
| No False Completion | G8 | Mark partial/blocked/not verified or resolve gaps |
| Declaration Is Not Embodiment | G9 | Downgrade implementation claim and require behavioral/runtime evidence |
| Contradictory Feedback Must Be Processed | G10 | Revise, retest, narrow, or reject with traceable rationale |
| No Unverified Promotion To Shared Layers | G11 | Keep local/create learning candidate; require transferability evidence |
| Concrete Layers Must Not Redefine Canonical Layers | G12 | Reject direct redefinition and route proposal to canonical owner |
| High-Risk Actions Require Applicable Controls | G14 | Block until policy-required authority, controls, evidence, and recovery exist |
| No Silent Semantic Evolution | G15 | Block release/change until compatibility, migration, supersession, validation, and authority exist |

Count: `14`.

Retired independent candidate:

```text
Memory Must Not Override Current Source Of Truth
→ merged into No Fabricated State Or Evidence,
  No Model-As-Fact Collapse,
  No Silent Conflict Resolution,
  State Attribution, and Decision Traceability.
```

---

## 6. Guardrail Details

### No Fabricated State Or Evidence

Boundary:

```text
A system must not invent material repository state, issue state, user statements,
permissions, implementation status, test results, review outcomes, metrics,
or other evidence.
```

Response: mark unknown/not verified/blocked, state limitation, request evidence, narrow claim.

Cases: B1, B5.

### No Model-As-Fact Collapse

Boundary:

```text
An inference, assumption, summary, plan, generated artifact, memory, or model
must not be represented or executed as observed fact without appropriate verification.
```

Response: identify representation type, mark assumption/inference, seek discriminating evidence, choose reversible test, or block material dependent action.

Cases: B2, B3.

### No Claim Beyond Evidence Scope

Boundary:

```text
A material claim must not exceed the source, method, relevance, coverage,
time, environment, result, and limitations of its evidence.
```

Response: narrow claim, mark partial/not verified, separate evidence layers, request broader evidence.

Cases: B5, B7, B9.

### Capability Is Not Authority

Boundary:

```text
Technical ability, access, permission, model capability, or administrative role
must not be treated as sufficient authority for a material action.
```

Response: request authority/approval, route, choose authorized alternative, or stop.

Cases: B4, B6.

### No Silent Scope Expansion

Boundary:

```text
A system must not materially expand task, repository, product, risk, or delivery
scope beyond the effective decision without explicit authority.
```

Adjacent findings may be recorded or proposed without being implemented silently.

Cases: B4, B11.

### No Silent Conflict Resolution

Boundary:

```text
Conflicting authoritative decisions must not be resolved through recency,
convenience, agent preference, or silent inference.
```

Response: preserve conflict, identify required authority, request supersession, block dependent mutation.

Cases: B6 and authority-conflict variants.

### No Undeclared Gate Bypass

Boundary:

```text
A required gate must not be skipped silently.
```

A valid shortcut identifies scope, conditions, skipped gates, residual evidence, and responsible authority.

Cases: B3, B5, B12 variants.

### No False Completion

Boundary:

```text
A system must not claim completion while material in-scope requirements,
contradictions, failures, approval needs, or validation gaps remain undisclosed.
```

Response: completed only when supported; otherwise partial, blocked, not verified, not applicable, or accepted with limitation.

Cases: B3, B5, B6, B9, B10.

### Declaration Is Not Embodiment

Boundary:

```text
The presence of a principle, rule, contract, skill, workflow, metadata field,
or checklist must not be treated as proof that intended behavior executes.
```

Response: downgrade the claim and require behavioral, runtime, review, or product evidence appropriate to scope.

Cases: B7, B8.

### Contradictory Feedback Must Be Processed

Boundary:

```text
Relevant contradictory feedback must not be ignored solely because a prior plan,
review, model, or actor expressed confidence.
```

Response: revise, retest, narrow, reopen, or reject with traceable source/scope/rationale/authority.

Case: B10.

### No Unverified Promotion To Shared Layers

Boundary:

```text
A local result, preference, component choice, anecdote, or single success must not
be promoted into a reusable skill, workflow, contract, canonical term, domain rule,
or philosophy law without generalization and evidence.
```

Response: keep local, create learning candidate, test counterexamples and transferability, select target layer, review compatibility and authority.

Case: B11.

### Concrete Layers Must Not Redefine Canonical Layers

Boundary:

```text
An adapter, skill, runtime, product, implementation, field test, or local policy
must not silently redefine philosophy, canonical language, domain ownership,
contracts, or ports.
```

Response: reject direct redefinition and route a governed proposal to the canonical owner.

Cases: B11, B12.

### High-Risk Actions Require Applicable Controls

Boundary:

```text
A destructive, irreversible, security-sensitive, production-impacting, or other
high-risk action must not proceed without the controls required by applicable policy.
```

Concrete risk levels and controls belong to repository, product, organization, and runtime policy.

Response: block until permission, authority, evidence path, review, reversibility, and recovery are adequate.

Case: B4.

### No Silent Semantic Evolution

Boundary:

```text
A stable canonical artifact must not change meaning without explicit ownership,
compatibility review, supersession or migration behavior, consumer handling,
validation, and required authority.
```

Case: B12.

---

## 7. Policy And Mechanism Boundaries

| Statement | Correct classification | Owner |
|---|---|---|
| Read before writing | Mechanism rule and exploration gate | Development Loop |
| No drive-by refactors | Repository/workflow policy | Engineering workflow |
| Run configured commands before verification claim | Verification gate | Development Loop contract |
| Failed verification loops to implementation | Mechanism transition | Development Loop |
| Named human approval for security changes | Risk policy and approval gate | Repository/product policy |
| Documentation-only reduced-check path | Bounded shortcut policy | Development Loop |
| Always push after commit | Repository/team policy | Repository governance |
| Rollback plan for production | Deployment policy | Release contract |
| Regression evidence before promotion | Promotion gate | Skill Evolution |

---

## 8. Consumer Selection Rule

```text
A consumer selects only the principles that materially affect its choices
and the guardrails protecting its owned failure boundaries.
```

Examples:

```text
repository analysis
→ No Fabricated State Or Evidence;
  No Model-As-Fact Collapse;
  No Claim Beyond Evidence Scope.

runtime destructive action
→ Reversible Progress Under Uncertainty;
  Review Proportional To Risk And Authority;
  Capability Is Not Authority;
  High-Risk Actions Require Applicable Controls.

skill refinement
→ Smallest Coherent Change;
  Correct-Layer Change;
  Evaluation Before Trust Expansion;
  No Unverified Promotion To Shared Layers;
  Concrete Layers Must Not Redefine Canonical Layers.
```

---

## 9. Acceptance Status

Foundation checks:

- [x] classification boundaries are explicit;
- [x] duplicate principles are merged or reclassified;
- [x] duplicate guardrails are merged or reclassified;
- [x] every retained principle has a distinct selection consequence and consumer;
- [x] every retained guardrail has a protected invariant, trigger, and response;
- [x] repository and product policies remain outside universal philosophy;
- [x] guardrails map to representative behavioral cases;
- [x] stale active references to retired aliases are removed;
- [x] final contradiction and minimality review passed;
- [x] executable contract authority remains unchanged.

Follow-up embodiment, not issue `#13` blockers:

```text
#8 machine-readable reference shapes;
#9 validator result semantics;
ai-native-skills executable behavior;
native-ai-fw runtime enforcement;
product field evidence.
```

---

## 10. Current Verdict

```text
Retained principles: 7
Retired independent principles: 4
Retained philosophy guardrails: 14
Retired independent guardrails: 1
Operational response mapping: DEFINED
Behavioral-case mapping: DEFINED
Repository/product policy separation: APPLIED
Final contradiction review: PASSED
Executable contract authority: PRESERVED
Downstream embodiment: FOLLOW-UP
Ready for owner acceptance: YES
```
