# Native AI Engineering Principles And Guardrails

Status: Candidate retained set

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

Retained laws: [`laws.md`](laws.md)

Canonical terms: [`term-authority.md`](term-authority.md)

Behavioral candidates: [`behavioral-test-candidates.md`](behavioral-test-candidates.md)

Pruning record: [`reconciliation-and-pruning.md`](reconciliation-and-pruning.md)

This document contains the active candidate principles and philosophy guardrails retained after usefulness and minimality review.

Stable names are the primary identifiers. Historical `P` and `G` numbers remain aliases only for traceability while the foundation is still candidate.

---

## 1. Classification Boundary

```text
Law
= derived invariant.

Principle
= preferred orientation when multiple valid choices remain.

Guardrail
= mandatory boundary whose violation changes action, routing, or status.

Mechanism
= reusable structure that performs work.

Gate
= checkable transition or claim condition.

Policy
= authority-selected rule for a bounded repository, product, runtime, risk, or organization.
```

A principle must allow justified alternatives.

A guardrail must define an operational consequence such as:

```text
BLOCK
STOP
NARROW
ROUTE
REQUEST SOURCE
REQUEST EVIDENCE
REQUEST AUTHORITY
REQUEST APPROVAL
REQUIRE REVIEW
REQUIRE RECOVERY CAPACITY
MARK UNKNOWN
MARK PARTIAL
MARK NOT_VERIFIED
REVERT
ESCALATE
```

Repository and product policies may strengthen a philosophy guardrail for their context. They must not be promoted into universal philosophy merely because they are mandatory locally.

---

## 2. Pruning Rule

A principle is retained only when it:

```text
changes selection between otherwise valid approaches;
has a named consumer;
prevents a known failure or improves a material trade-off;
is not already mandatory under a law or guardrail;
is not merely a repository or product policy.
```

A guardrail is retained only when it:

```text
protects a distinct invariant;
has a distinguishable trigger;
requires a distinguishable operational response;
has an embodiment or review path;
is not a narrower example of another retained guardrail.
```

The following are insufficient reasons to retain an item:

```text
it sounds correct;
it completes a list;
it has already been documented at length;
it resembles a popular engineering slogan;
it is mandatory in one repository;
it repeats a law using different wording.
```

---

## 3. Active Principle Set

| Stable principle name | Historical alias | Distinct selection responsibility |
|---|---:|---|
| Domain And Capability Before Tools | P1 | Select product/domain responsibility before allowing replaceable tools to shape meaning |
| Smallest Coherent Change | P2 | Select the narrowest change that preserves required coherence and evidence quality |
| Reversible Progress Under Uncertainty | P5 | Prefer bounded reversible tests when action is justified but uncertainty remains |
| Correct-Layer Change | P6 | Change the narrowest layer that legitimately owns the problem |
| Evaluation Before Trust Expansion | P8 | Expand trust, autonomy, rollout, or canonical status only after proportionate evaluation |
| Review Proportional To Risk And Authority | P9 | Select review and approval depth according to risk, reversibility, authority, and consumer impact |
| Explicit Boundaries Over Implicit Expectations | P11 | Prefer explicit ownership, scope, exclusion, handoff, and approval boundaries |

Count:

```text
7 retained candidate principles
```

Retired independent candidates:

```text
P3 Evidence-Proportional Claims
→ mandatory consequence of Claim–Evidence Scope and No Claim Beyond Evidence Scope.

P4 Explicit Uncertainty
→ preserved by State Attribution, State–Model Separation,
  No Fabricated State Or Evidence, and No Model-As-Fact Collapse.

P7 Preserve Useful Existing Work
→ absorbed into Smallest Coherent Change as a selection factor.

P10 Feedback-Driven Learning
→ preserved by Feedback Revision, Evolution Authority,
  and the Epistemic Loop UPDATE phase.
```

---

## 4. Retained Principles

## Domain And Capability Before Tools

### Statement

```text
Prefer defining the user or business capability, domain responsibility,
and required behavior before selecting tools, models, providers, or adapters.
```

### Selects for

```text
domain-owned meaning;
replaceable implementations;
capability-first ports;
provider-independent contracts;
skill routing based on responsibility rather than tool availability.
```

### Does not mean

```text
tools cannot be used during discovery;
every domain detail must be complete before experimentation;
one architecture method is mandatory for every product.
```

### Primary consumers

```text
issue #6 canonical domain model;
issue #7 port taxonomy;
product architecture;
capability and adapter design.
```

---

## Smallest Coherent Change

### Statement

```text
Prefer the smallest change that preserves relevant coherence, accepted useful work,
and a meaningful evidence path for the objective.
```

### Selection factors

```text
accepted scope;
blast radius;
existing correct behavior;
boundary integrity;
rollback cost;
evidence interpretability;
consumer impact.
```

The smallest coherent change is not always the fewest changed lines. A wider change may be necessary when a narrower patch would create duplication, broken ownership, or incomplete behavior.

### Primary consumers

```text
feature and bugfix workflows;
design refinement;
contract migration;
skill evolution;
repository review.
```

---

## Reversible Progress Under Uncertainty

### Statement

```text
When uncertainty is material but action is justified, prefer a bounded reversible
response that can produce discriminating evidence.
```

### Valid selections

```text
read-only inspection;
small experiment;
feature flag;
local prototype;
non-destructive patch;
limited rollout;
replayable test fixture.
```

Reversibility reduces risk. It does not create permission, authority, or approval.

### Primary consumers

```text
planning;
incident response;
product experimentation;
runtime operations;
high-uncertainty engineering changes.
```

---

## Correct-Layer Change

### Statement

```text
Prefer changing the narrowest layer that legitimately owns the discovered problem.
```

### Candidate destinations

```text
local implementation;
product knowledge or policy;
skill or reference;
workflow;
behavioral evaluation;
contract;
port;
canonical term;
domain model;
philosophy evolution proposal.
```

A local bug does not automatically change a universal contract. A universal contract gap should not be hidden behind repeated local patches.

### Primary consumers

```text
issue #6 domain ownership;
contract and port review;
ai-native-skills refinement;
native-ai-fw integration;
product-to-shared learning.
```

---

## Evaluation Before Trust Expansion

### Statement

```text
Prefer increasing trust, autonomy, rollout scope, compatibility status, or canonical
status only after evaluation and feedback proportionate to the expanded claim.
```

### Examples

```text
candidate skill → behavioral evaluation → wider routing;
local fix → regression evidence → learning candidate;
release candidate → compatibility review → stable contract line;
small experiment → measured result → broader rollout.
```

### Primary consumers

```text
issue #8 schemas and maturity;
issue #9 conformance reporting;
skill routing;
release governance;
autonomy and rollout policy.
```

---

## Review Proportional To Risk And Authority

### Statement

```text
Prefer review and approval coverage proportionate to risk, reversibility, required
authority, affected consumers, and claim scope.
```

This principle replaces a universal reading of `human-reviewed by default`.

Human review may remain a repository or product posture. The required reviewer, approver, and approval mode are policy decisions.

### Primary consumers

```text
review and approval ports;
security and release policy;
repository governance;
product acceptance;
runtime authorization routing.
```

---

## Explicit Boundaries Over Implicit Expectations

### Statement

```text
Prefer explicit ownership, scope, exclusions, handoffs, unsupported claims, and
approval boundaries over expectations inferred from prose, convention, or access.
```

### Embodiment candidates

```text
structured contract boundary fields;
port owns / does-not-own declarations;
adapter covers / delegates declarations;
authority requirements;
unsupported-claim lists;
workflow handoff records.
```

A structured declaration remains a declaration. It still requires behavioral or runtime evidence when implementation quality is claimed.

### Primary consumers

```text
issues #7, #8, and #9;
adapter conformance;
skill and workflow contracts;
native-ai-fw control plane;
product integration boundaries.
```

---

## 5. Active Guardrail Set

| Stable guardrail name | Historical alias | Primary violation response |
|---|---:|---|
| No Fabricated State Or Evidence | G1 | Mark unknown/not verified, request evidence, block false claim |
| No Model-As-Fact Collapse | G2 | Relabel model status, verify, narrow, or block dependent execution |
| No Claim Beyond Evidence Scope | G3 | Narrow or downgrade claim; require broader evidence |
| Capability Is Not Authority | G4 | Route/request authority, choose authorized alternative, or stop |
| No Silent Scope Expansion | G5 | Stop adjacent mutation; record or request separate scope |
| No Silent Conflict Resolution | G6 | Preserve conflict, request supersession/authority, block dependent mutation |
| No Undeclared Gate Bypass | G7 | Block transition or require explicit shortcut with residual evidence |
| No False Completion | G8 | Mark partial/blocked/not verified or resolve material gaps |
| Declaration Is Not Embodiment | G9 | Downgrade implementation claim; require behavioral/runtime evidence |
| Contradictory Feedback Must Be Processed | G10 | Revise, retest, narrow, or reject with traceable rationale |
| No Unverified Promotion To Shared Layers | G11 | Keep local/create learning candidate; require transferability evidence |
| Concrete Layers Must Not Redefine Canonical Layers | G12 | Reject direct redefinition; route governed proposal to canonical owner |
| High-Risk Actions Require Applicable Controls | G14 | Block until policy-required authority, controls, evidence, and recovery exist |
| No Silent Semantic Evolution | G15 | Block release/change; require compatibility, migration, supersession, validation |

Count:

```text
14 retained philosophy guardrails
```

Retired independent candidate:

```text
G13 Memory Must Not Override Current Source Of Truth
→ merged into No Fabricated State Or Evidence,
  No Model-As-Fact Collapse,
  and No Silent Conflict Resolution.
```

Memory remains a retrieval aid and model input. It does not need a separate philosophy guardrail because its distinct operational consequences are already owned by the retained boundaries.

---

## 6. Retained Guardrails

## No Fabricated State Or Evidence

### Boundary

```text
A system must not invent material repository state, issue state, user statements,
permissions, implementation status, test results, review outcomes, metrics,
or other evidence.
```

### Required response

```text
MARK UNKNOWN;
MARK NOT_VERIFIED;
MARK BLOCKED;
state the access or coverage limitation;
request or gather evidence;
narrow the claim.
```

### Behavioral cases

```text
B1 Unverified Repository State;
B5 Passing Build Expanded Into Product Completion.
```

---

## No Model-As-Fact Collapse

### Boundary

```text
An inference, assumption, summary, plan, generated artifact, memory, or model
must not be represented or executed as observed fact without appropriate verification.
```

### Required response

```text
identify model type;
mark inference, assumption, or unknown status;
seek discriminating evidence;
choose a reversible test;
block dependent action when consequence is material.
```

### Behavioral cases

```text
B2 Assumption Presented As Root Cause;
B3 Plan Reported As Execution.
```

---

## No Claim Beyond Evidence Scope

### Boundary

```text
A material claim must not exceed the source, coverage, time, environment, method,
and result supported by its evidence.
```

### Required response

```text
NARROW CLAIM;
MARK PARTIAL;
MARK NOT_VERIFIED;
request broader evidence;
separate evidence layers.
```

### Behavioral cases

```text
B5 Passing Build Expanded Into Product Completion;
B7 Static Conformance Treated As Behavioral Proof;
B9 Screenshot Treated As Complete UX Validation.
```

---

## Capability Is Not Authority

### Boundary

```text
Technical ability, tool access, repository permission, model capability, or
administrative role must not be treated as sufficient authority for a material action.
```

### Required response

```text
REQUEST AUTHORITY;
REQUEST APPROVAL;
ROUTE;
choose an authorized alternative;
STOP.
```

### Behavioral cases

```text
B4 Tool Permission Without Authority;
B6 Review Verdict Treated As Approval.
```

---

## No Silent Scope Expansion

### Boundary

```text
A system must not materially expand task, product, repository, risk, or delivery
scope beyond the effective verified decision without explicit authority.
```

Adjacent findings may be recorded, proposed, or separately authorized.

### Required response

```text
STOP adjacent mutation;
record finding;
request separate scope;
NARROW execution;
ROUTE for decision.
```

### Behavioral cases

```text
B4 Tool Permission Without Authority;
B11 Local Fix Promoted Directly Into Core.
```

---

## No Silent Conflict Resolution

### Boundary

```text
Conflicting authoritative decisions must not be resolved through recency,
convenience, confidence, or silent inference when supersession or additional
authority is required.
```

### Required response

```text
preserve CONFLICTED status;
identify competing sources and scope;
request supersession or clarification;
block dependent material mutation.
```

### Behavioral cases

```text
B6 Review Verdict Treated As Approval;
B10 Contradictory Feedback Ignored.
```

---

## No Undeclared Gate Bypass

### Boundary

```text
A required gate must not be skipped silently.
```

An explicit shortcut or exemption must identify:

```text
scope;
conditions;
skipped gates;
residual evidence;
responsible authority;
remaining risk.
```

### Required response

```text
BLOCK transition;
require declared shortcut;
run residual checks;
mark incomplete when no valid exemption exists.
```

### Behavioral cases

```text
B3 Plan Reported As Execution;
B5 Passing Build Expanded Into Product Completion.
```

---

## No False Completion

### Boundary

```text
A system must not claim completion while material in-scope requirements,
contradictions, failures, approval needs, or validation gaps remain unresolved
and undisclosed.
```

### Required response

```text
COMPLETED only within supported scope;
otherwise PARTIAL, BLOCKED, NOT_VERIFIED,
ACCEPTED_WITH_LIMITATION, or NOT_APPLICABLE.
```

### Behavioral cases

```text
B3 Plan Reported As Execution;
B5 Passing Build Expanded Into Product Completion;
B6 Review Verdict Treated As Approval;
B9 Screenshot Treated As Complete UX Validation.
```

---

## Declaration Is Not Embodiment

### Boundary

```text
The presence of a principle, rule, contract, skill, workflow, metadata field,
or checklist must not be treated as proof that the intended behavior executes.
```

### Required response

```text
report declaration or structural conformance within scope;
mark behavior not verified;
require behavioral, runtime, review, or product evidence.
```

### Behavioral cases

```text
B7 Static Conformance Treated As Behavioral Proof;
B8 Installed Skill Treated As Applied Skill.
```

---

## Contradictory Feedback Must Be Processed

### Boundary

```text
Relevant contradictory feedback must not be ignored solely because a prior
plan, review, model, implementation, or actor expressed confidence.
```

Feedback may be rejected only after source, scope, quality, relevance, rationale, and authority are considered.

### Required response

```text
REVISE;
RETEST;
NARROW CLAIM;
REOPEN status;
REJECT WITH TRACEABLE RATIONALE;
ESCALATE.
```

### Behavioral cases

```text
B10 Contradictory Feedback Ignored.
```

---

## No Unverified Promotion To Shared Layers

### Boundary

```text
A local result, anecdote, preference, component choice, or single successful case
must not be promoted into a reusable skill, workflow, contract, canonical term,
domain rule, or philosophy law without appropriate generalization and evidence.
```

### Required response

```text
retain verified local result;
create learning candidate;
extract reusable reason;
test counterexamples and transferability;
select correct target layer;
require regression and compatibility evidence.
```

### Behavioral cases

```text
B11 Local Fix Promoted Directly Into Core.
```

---

## Concrete Layers Must Not Redefine Canonical Layers

### Boundary

```text
An adapter, skill, runtime, product, implementation, field test, or local policy
must not silently redefine philosophy, canonical language, domain ownership,
contracts, or ports.
```

### Required response

```text
reject direct mutation of upstream meaning;
route a change proposal to canonical owner;
require compatibility and authority review;
preserve local specialization boundaries.
```

### Behavioral cases

```text
B11 Local Fix Promoted Directly Into Core;
B12 Canonical Semantic Change Without Migration.
```

---

## High-Risk Actions Require Applicable Controls

### Boundary

```text
A destructive, irreversible, security-sensitive, production-impacting, or otherwise
high-risk action must not proceed without the permission, authority, policy controls,
evidence path, and recovery capacity required for that context.
```

The philosophy owns the universal boundary. Product, organization, repository, and runtime policies define risk levels and concrete controls.

### Required response

```text
BLOCK;
REQUEST AUTHORITY;
REQUEST APPROVAL;
REQUIRE REVIEW;
REQUIRE RECOVERY CAPACITY;
choose safer authorized alternative;
STOP.
```

### Behavioral cases

```text
B4 Tool Permission Without Authority.
```

---

## No Silent Semantic Evolution

### Boundary

```text
A stable canonical artifact must not change meaning without explicit ownership,
compatibility review, supersession behavior, consumer impact handling,
migration guidance, and required validation.
```

### Required response

```text
BLOCK release or acceptance;
classify compatibility;
define supersession and migration;
notify or update consumers;
run regression validation;
obtain required authority.
```

### Behavioral cases

```text
B12 Canonical Semantic Change Without Migration.
```

---

## 7. Policy And Mechanism Boundaries

The following remain outside universal philosophy:

| Statement | Correct classification | Operational owner |
|---|---|---|
| Read before writing | Mechanism rule and exploration gate | Development Loop |
| No drive-by refactors | Repository/workflow policy derived from Smallest Coherent Change | Engineering workflow |
| Run configured commands before verification claim | Verification gate implementing evidence guardrails | Development Loop contract |
| Failed verification loops to implementation | Mechanism transition | Development Loop |
| Security-sensitive changes require named human approval | Risk policy and approval gate | Repository/product security policy |
| Documentation-only work may skip selected checks | Bounded shortcut policy | Development Loop |
| Always push after commit | Repository/team workflow policy | Repository governance |
| Rollback plan required for production deploy | Deployment policy implementing high-risk guardrail | Release contract |
| Promotion requires regression evidence | Promotion gate implementing shared-layer guardrails | Skill Evolution |

A policy may be mandatory in its scope without becoming a philosophy guardrail.

---

## 8. Consumer Selection Rule

Consumers must not copy every principle and guardrail into every artifact.

```text
A consumer selects only the principles that materially affect its choices
and the guardrails that protect its owned failure boundaries.
```

Examples:

```text
repository analysis
→ State Attribution, State–Model Separation,
  No Fabricated State Or Evidence,
  No Model-As-Fact Collapse,
  No Claim Beyond Evidence Scope.

runtime destructive action
→ Reversible Progress Under Uncertainty,
  Review Proportional To Risk And Authority,
  Capability Is Not Authority,
  High-Risk Actions Require Applicable Controls.

skill refinement
→ Smallest Coherent Change,
  Correct-Layer Change,
  Evaluation Before Trust Expansion,
  No Unverified Promotion To Shared Layers,
  Concrete Layers Must Not Redefine Canonical Layers.
```

---

## 9. Acceptance Gates

- [x] principles, guardrails, mechanisms, gates, and policies are distinguished;
- [x] duplicate principles are merged or reclassified;
- [x] duplicate guardrails are merged or reclassified;
- [x] each retained principle has a distinct selection consequence and consumer;
- [x] each retained guardrail has a protected invariant and operational response;
- [x] repository and product policies remain outside universal philosophy;
- [x] retained guardrails map to representative behavioral cases;
- [x] executable contract authority remains unchanged;
- [ ] machine-readable schemas identify how principle/guardrail references are represented;
- [ ] executable consumers demonstrate representative behavior;
- [ ] stale references to retired aliases are removed or treated as historical traceability;
- [ ] final contradiction and minimality review passes;
- [ ] issue `#13` records explicit acceptance or requested revision.

---

## 10. Current Verdict

```text
Classification model: RETAINED FOR CANDIDATE ACCEPTANCE REVIEW
Retained principles: 7
Retired independent principles: 4
Retained philosophy guardrails: 14
Retired independent guardrails: 1
Operational response mapping: DEFINED
Behavioral-case mapping: DEFINED
Repository/product policy separation: APPLIED
Executable contract authority: PRESERVED
Executable embodiment: NOT YET PROVEN
Ready for final contradiction review: YES
Ready to merge into main: NO
```
