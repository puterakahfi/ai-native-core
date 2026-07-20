# Native AI Engineering Domain Model Discovery

Status: Discovery — non-canonical

Issue: `#6 — Define the canonical Native AI Engineering domain model`

Branch: `6-canonical-native-ai-engineering-domain-model`

Accepted foundation: [`philosophy/README.md`](philosophy/README.md)

This document records the source inventory, current domain signals, contradictions, ownership gaps, candidate bounded contexts, and validation plan for issue `#6`.

It is not the canonical domain model. It must not be used as machine-contract authority, final ubiquitous language, or approval to migrate existing contracts.

---

## 1. Objective

Define one canonical, runtime-agnostic Native AI Engineering domain model so that:

```text
intent;
requirements and acceptance criteria;
capabilities and use cases;
contracts and ports;
skills and workflows;
adapters and runtime bindings;
execution and evidence;
gates, review, decisions, approval, and delivery;
knowledge, memory, feedback, learning, and evolution
```

share explicit ownership, relationships, lifecycle boundaries, and prohibited semantic collapses.

The model must be useful to:

```text
ai-native-core contracts and taxonomies;
ai-native-skills executable capabilities and workflows;
native-ai-fw orchestration and control-plane behavior;
product repositories and real-world validation.
```

---

## 2. Acceptance Boundary

Issue `#6` owns:

```text
bounded contexts;
canonical domain concepts;
entity and value-object boundaries;
aggregate and lifecycle relationships;
domain policies and invariants;
commands and events where useful;
canonical ownership and dependency direction;
one ubiquitous language for first-class Native AI Engineering concepts.
```

Issue `#6` does not own:

```text
redefining philosophy, laws, principles, or guardrails accepted by #13;
freezing the final port taxonomy owned by #7;
freezing machine-readable schema structure owned by #8;
implementing validator behavior owned by #9;
implementing runtime orchestration in native-ai-fw;
moving executable skills into core;
selecting providers, tools, frameworks, or product stacks;
rewriting all existing contracts without separately approved migration.
```

A domain-model decision may identify required downstream schema or contract work without implementing it in this issue.

---

## 3. Accepted Foundation Constraints

The domain model must preserve these accepted distinctions:

```text
state ≠ observation;
observation ≠ interpretation;
interpretation ≠ inference;
inference ≠ fact;
assumption ≠ fact;
claim ≠ evidence;
capability ≠ permission;
permission ≠ authority;
decision ≠ effective decision;
review ≠ approval;
verification ≠ validation;
contract presence ≠ conformance;
static conformance ≠ executable behavior;
skill installation ≠ skill application;
feedback ≠ learning;
local update ≠ core evolution;
completion ≠ activity performed.
```

The model must also preserve:

```text
source attribution;
scope and coverage;
claim-evidence proportionality;
explicit unknown and not-verified states;
decision provenance and supersession;
authority and approval boundaries;
execution capacity and risk controls;
evidence-layered conformance;
correct-layer learning and evolution.
```

The domain model must consume the philosophy. It must not create a parallel doctrine layer.

---

## 4. Sources Inspected

### Accepted foundation

```text
docs/philosophy/README.md
docs/philosophy/laws.md
docs/philosophy/principles-and-guardrails.md
docs/philosophy/term-authority.md
docs/philosophy/epistemic-loop.md
docs/philosophy/behavioral-test-candidates.md
```

### Current architecture and modeling guidance

```text
docs/architecture-v0.2.md
docs/domain-driven-model.md
docs/ports-and-adapters.md
docs/port-taxonomy.md
docs/engineering-contract.md
docs/glossary.md
docs/memory-vs-knowledge.md
docs/development-loop.md
```

### Existing machine-contract evidence

```text
contracts/manifest.yaml
contracts/skills/quality/decision-provenance.contract.yaml
contracts/skills/quality/skill-evolution.contract.yaml
contracts/workflows/new-feature.contract.yaml
contracts/workflows/product-development.contract.yaml
contracts/runtime/development-loop.contract.yaml
contracts/runtime/memory.contract.yaml
```

The manifest currently registers 106 contracts across skill, workflow, behavioral-test, and runtime families. Manifest presence proves inventory identity, not domain ownership or semantic coherence.

---

## 5. Current Domain Signals

## 5.1 Philosophy-level concepts already accepted

The accepted philosophy provides minimum meanings for:

```text
State
Observable State
Available State
Observation
Source
Unknown
Model
Interpretation
Inference
Assumption
Fact
Claim
Evidence
Verification
Validation
Evaluation
Review
Conformance
Coherence
Completion
Capability
Permission
Authority
Decision
Effective Decision
Approval
Scope
Coverage
Capacity
Feedback
Update
Learning
Learning Candidate
Embodiment
Stability
Core Evolution
Source Of Truth
Knowledge
Memory
```

These are domain-model inputs. Their atomic meanings remain philosophy-owned unless issue `#6` introduces a compatible domain specialization.

## 5.2 Existing domain-driven modeling guidance

`docs/domain-driven-model.md` already defines generic DDD concepts:

```text
core domain;
subdomain;
bounded context;
ubiquitous language;
entity;
value object;
aggregate;
domain event;
use case;
port;
adapter.
```

However, it is primarily a modeling guide with product-oriented examples. It is not yet the canonical Native AI Engineering domain model.

Its current examples such as `Brand`, `Campaign`, `GeneratedAsset`, and `CreativeReview` are product examples and must not become universal Native AI Engineering concepts.

## 5.3 Existing capability and adapter signals

Current architecture sources establish:

```text
domain defines capability and meaning;
ports describe required capabilities and boundaries;
adapters provide replaceable implementation;
tools and providers remain replaceable;
adapters must not own domain meaning.
```

`docs/port-taxonomy.md` currently uses:

```text
Port = capability contract
Adapter = replaceable implementation
```

This is useful but potentially over-compressed. Issue `#6` must define the domain relationship among `Capability`, `Contract`, `Port`, and `Adapter` without freezing the final port categories owned by `#7`.

## 5.4 Existing workflow and execution signals

Workflow contracts already distinguish:

```text
workflow definition;
ordered phases;
entry and exit gates;
required and optional skills;
decision-provenance checks;
evidence requirements;
review routing;
release eligibility;
authorization;
adapter-defined runtime mechanisms.
```

The product-development workflow exposes a relationship among:

```text
discovery;
requirements;
MVP scope;
technical specification;
implementation;
acceptance verification;
release;
deployment;
launch;
learning.
```

The new-feature workflow exposes:

```text
plan;
design decision;
implementation;
verification;
submission;
review;
merge authorization.
```

These are workflow definitions, not automatically universal domain lifecycles. The canonical model must identify the reusable domain objects underneath them.

## 5.5 Existing decision and authority signals

The decision-provenance contract already distinguishes:

```text
Decision Record;
Decision Type;
Claim;
Source Type and Source Reference;
Required Authority;
Observed Authority;
Authority Status;
Supersession;
Conflict;
Verification;
Permitted Actions;
Blocked Actions;
Effective Decision;
Approval Routing.
```

It also establishes:

```text
newest source ≠ authority;
implementation existence ≠ permission;
agent-authored text ≠ owner approval;
silence ≠ approval;
direct instruction applies only to named scope;
unresolved authoritative conflict blocks dependent mutation.
```

The canonical domain model should preserve these distinctions while avoiding contract-specific field names becoming universal objects without review.

## 5.6 Existing evidence, gate, review, and delivery signals

Workflow contracts currently use multiple evidence and decision surfaces:

```text
Acceptance Criterion;
Evidence Requirement;
Evidence Available;
Evidence Gap;
Reviewer Verdict;
Gate Result;
Accepted Risk;
Release Eligibility;
Release Authorization;
Deployment Authorization;
Launch Authorization;
Delivery or Merge Decision.
```

They already preserve an important boundary:

```text
quality readiness ≠ authorization to perform the action.
```

For example:

```text
release-ready ≠ release authorized;
code-review approval ≠ product release approval;
technical verification ≠ product acceptance;
source-only review ≠ rendered implementation acceptance.
```

The domain model must define reusable relationships without promoting one workflow's enum set into a universal status taxonomy.

## 5.7 Existing learning and evolution signals

The skill-evolution contract already distinguishes:

```text
source case;
observed failure;
verified fix;
before/after evidence;
root reason;
learning candidate;
target-layer decision;
minimal patch;
regression evaluation;
promotion verdict;
provenance record.
```

It also defines target-layer classes:

```text
local implementation;
product design lock;
skill rule;
skill reference;
workflow rule;
regression evaluation;
core contract.
```

The accepted philosophy adds `Core Evolution` as a governed canonical change. Issue `#6` must model the relationship among feedback, update, learning, learning candidate, promotion decision, and evolution proposal without making every successful fix a shared rule.

## 5.8 Existing knowledge and memory signals

Current docs and runtime contracts distinguish:

```text
Knowledge = explicit, reviewable, version-controlled source-of-truth information;
Memory = retained context, history, preference, pattern, or prior outcome used for retrieval and reasoning.
```

The runtime memory contract currently defines:

```text
session memory;
persistent memory;
episodic memory;
procedural memory;
promotion to persistent, procedural, or knowledge.
```

Potential tension:

```text
procedural memory is described as skills;
accepted architecture treats skills as executable reusable capability/methodology artifacts;
accepted philosophy treats memory as non-authoritative retrieval support.
```

The domain model must decide whether `procedural memory` is a true memory subtype, a historical runtime label, or a relationship to versioned procedural knowledge/skills. It must not silently redefine the accepted memory contract in this issue.

---

## 6. Material Ambiguities And Contradictions

## A1 — Modeling guide versus canonical domain authority

`docs/domain-driven-model.md` explains how to perform DDD but does not define the Native AI Engineering domain itself.

Required resolution:

```text
retain as modeling guidance, or supersede its authority role;
create one canonical domain-model source;
ensure product examples remain examples.
```

## A2 — Capability, contract, and port collapse

Current wording sometimes treats:

```text
port = capability contract.
```

Potential problem:

```text
Capability is a domain ability;
Contract is a stable agreement;
Port is an architectural boundary exposing required capability;
Adapter implements or binds the port.
```

These may be related but should not be assumed identical before issue `#6` and `#7` complete their ownership review.

## A3 — Contract family ambiguity

`Engineering Contract` currently refers to a product stack and architecture agreement, while repository contracts also include:

```text
skill contracts;
workflow contracts;
runtime contracts;
behavioral test contracts;
future port contracts.
```

Required resolution:

```text
Contract as a general domain concept;
Contract Definition or Contract Artifact as a first-class agreement;
Product Engineering Agreement as a named specialization if retained;
contract family and evidence-layer relationships.
```

## A4 — Review decision, decision record, verdict, and approval

Existing sources use overlapping phrases such as:

```text
ReviewDecision;
review verdict;
Decision Record;
effective decision;
approval;
merge authorization;
release authorization.
```

Required resolution:

```text
Review produces findings and a verdict;
Decision selects or constrains action;
Effective Decision has verified authority and scope;
Approval is an authority-bearing positive decision;
Authorization determines whether a named action may proceed under applicable policy.
```

The domain model must decide whether authorization is a separate object, an approval specialization, or a policy result.

## A5 — Definition versus run or application

Current sources frequently describe artifacts but do not consistently distinguish:

```text
Workflow Definition versus Workflow Run;
Skill Definition versus Skill Application;
Contract Definition versus Contract Evaluation;
Port Definition versus Runtime Binding;
Adapter Definition versus Adapter Instance or Binding;
Evaluation Definition versus Evaluation Run;
Review Requirement versus Review Record.
```

This distinction is necessary to prevent declaration from being reported as embodiment.

## A6 — Generic status fields

Existing workflows contain useful but local statuses:

```text
PASS;
CONDITIONAL;
FAIL;
NOT_VERIFIED;
NOT_APPLICABLE;
RELEASE_READY;
NOT_READY;
AUTHORIZED;
NOT_AUTHORIZED;
ROUTE_FOR_APPROVAL.
```

Required resolution:

```text
model status ownership by concept;
do not create one universal status enum;
shared cross-cutting statuses should be minimal and justified;
workflow-specific verdicts remain specialized.
```

## A7 — Actor, agent, runtime, model, and tool ownership

Current architecture names agents, models, tools, providers, runtimes, and adapters but does not yet define whether they are:

```text
actors;
resources;
capability providers;
execution surfaces;
bindings;
or external systems.
```

The domain model must establish minimum relationships without selecting a provider or runtime architecture.

## A8 — Product and runtime binding registry

Contracts declare runtime-defined or product-defined adapter requirements, but no canonical model currently relates:

```text
Product;
Capability Requirement;
Port;
Adapter;
Runtime Binding;
Environment;
Policy;
Authorization;
Execution Run.
```

Issue `#6` should define the domain relationship. Concrete registry and orchestration behavior remain downstream responsibilities.

---

## 7. Candidate Bounded-Context Families

These are hypotheses for evaluation, not accepted contexts.

## C1 — Intent And Specification

Owns candidate concepts such as:

```text
Intent;
Objective;
Requirement;
Acceptance Criterion;
Constraint;
Non-Goal;
Scope;
Specification;
Change Request.
```

Must not own:

```text
implementation state;
execution evidence;
review verdict;
approval authority.
```

## C2 — Capability And Agreement

Owns candidate concepts such as:

```text
Capability;
Use Case;
Contract Definition;
Contract Version;
Boundary;
Required Input;
Allowed Output;
Quality Gate Requirement;
Compatibility Expectation.
```

Must not own:

```text
provider implementation;
runtime execution;
product-specific adapter selection.
```

## C3 — Method And Workflow

Owns candidate concepts such as:

```text
Skill Definition;
Workflow Definition;
Phase Definition;
Gate Definition;
Role Requirement;
Handoff Definition;
Workflow Run;
Skill Application.
```

Must preserve:

```text
definition ≠ run;
installation ≠ application;
phase completion ≠ total completion.
```

## C4 — Port, Adapter, And Binding

Owns candidate concepts such as:

```text
Port Definition;
Adapter Definition;
Adapter Binding;
Runtime Binding;
Capability Provider;
Environment Binding;
Binding Constraint.
```

The final port taxonomy remains owned by `#7`.

## C5 — Execution And Operations

Owns candidate concepts such as:

```text
Execution Request;
Execution Run;
Actor;
Execution Surface;
Tool Invocation;
Operation Result;
Side Effect;
Failure;
Recovery or Rollback Record.
```

Must preserve:

```text
capability ≠ permission;
permission ≠ authority;
plan ≠ execution;
execution ≠ success;
activity ≠ completion.
```

## C6 — Evidence, Evaluation, And Acceptance

Owns candidate concepts such as:

```text
Evidence Item;
Evidence Set;
Claim Assessment;
Verification Run;
Validation Run;
Evaluation Run;
Gate Evaluation;
Review Record;
Finding;
Verdict;
Coverage;
Conformance Assessment;
Completion Assessment.
```

Must not own authority to approve unless the relevant governance context explicitly grants it.

## C7 — Governance, Risk, And Authority

Owns candidate concepts such as:

```text
Decision Record;
Effective Decision;
Authority Requirement;
Permission Grant;
Approval;
Authorization Assessment;
Risk;
Risk Acceptance;
Policy;
Conflict;
Supersession.
```

Must preserve:

```text
review ≠ approval;
source ≠ authority;
newest ≠ authoritative;
silence ≠ approval;
readiness ≠ authorization.
```

## C8 — Context, Knowledge, And Memory

Owns candidate concepts such as:

```text
Context Pack;
Knowledge Artifact;
Source Of Truth Designation;
Memory Record;
Source Reference;
Recency or Supersession Link;
Retrieval Result.
```

Must preserve:

```text
memory ≠ current state;
memory ≠ authority;
knowledge ≠ immutable truth;
retrieval ≠ verification.
```

## C9 — Delivery, Product Binding, And Registry

Candidate responsibility:

```text
Product Binding;
Delivery Candidate;
Release Eligibility;
Delivery Authorization;
Deployment Record;
Launch Record;
Product Registry Entry.
```

Open question:

```text
Should this be a core bounded context,
a specialization across execution and governance,
or a downstream product/runtime context?
```

Issue `#6` must avoid encoding one product-release workflow as universal engineering lifecycle.

## C10 — Feedback, Learning, And Evolution

Owns candidate concepts such as:

```text
Feedback Item;
Update Decision;
Learning;
Learning Candidate;
Target-Layer Decision;
Promotion Assessment;
Evolution Proposal;
Migration Plan;
Supersession Record.
```

Must preserve:

```text
feedback ≠ learning;
one result ≠ reusable rule;
local fix ≠ shared promotion;
proposal ≠ accepted core evolution.
```

---

## 8. Candidate Cross-Context Lifecycle

The issue requests a canonical relationship comparable to:

```text
Intent
→ Requirement / Acceptance Criterion
→ Domain Capability
→ Use Case
→ Contract
→ Port
→ Workflow
→ Skill / Method
→ Adapter / Runtime Selection
→ Execution Run
→ Evidence
→ Gate Result
→ Review / Approval
→ Delivery
→ Learning Candidate
→ Contract / Skill / Knowledge Evolution
```

Discovery refinement:

```text
Intent
→ Specification owns requirements, constraints, scope, and acceptance criteria
→ Capability identifies what the system must be able to do
→ Use Case defines an application-level response using capabilities
→ Contract defines a stable agreement and boundary
→ Port exposes a required capability boundary
→ Workflow Definition coordinates methods, phases, and gates
→ Skill Definition provides reusable method or specialist behavior
→ Binding selects authorized adapters and execution surfaces for context
→ Workflow Run coordinates one bounded execution lifecycle
→ Execution Run records actual performed work and resulting state
→ Evidence Item supports or challenges claims about the run
→ Gate Evaluation determines whether a declared transition condition is met
→ Review Record produces findings and verdicts
→ Effective Decision and Approval provide authority where required
→ Delivery records an authorized transition or handoff
→ Feedback records attributable consequence or evaluation input
→ Learning Candidate proposes reusable change at the smallest correct layer
→ Governed evolution accepts, rejects, migrates, or supersedes shared agreements.
```

This is a relationship hypothesis. It is not yet an aggregate boundary or mandatory linear workflow.

---

## 9. Candidate First-Class Concept Tests

A concept should become first-class only when it has:

```text
stable identity or value semantics;
a distinct owner;
a lifecycle or invariant not owned elsewhere;
a named consumer;
a failure prevented by keeping it separate;
a plausible machine-contract or executable consumer;
no smaller existing concept that already owns the same responsibility.
```

A concept should remain a property, specialization, or example when it does not pass this test.

Examples requiring explicit review:

```text
Authorization;
Delivery;
Product Binding;
Context Pack;
Actor;
Execution Surface;
Gate Result;
Accepted Risk;
Contract Family;
Skill Application;
Adapter Binding.
```

---

## 10. Candidate Domain Policies And Invariants

The canonical model is expected to need policies comparable to:

```text
Claim Evidence Policy
- claim strength and scope cannot exceed evidence.

Execution Authorization Policy
- capability and permission are insufficient without required authority and controls.

Decision Effectiveness Policy
- a decision becomes effective only when source, authority, scope, approvals,
  conflicts, and supersession are resolved.

Completion Policy
- completion requires accepted objectives, criteria, evidence, required review
  or approval, and disclosed limitations.

Definition–Run Separation Policy
- declared contract, workflow, skill, adapter, or port is not proof of execution
  or embodiment.

Promotion Policy
- verified local learning may propose the smallest correct shared-layer change;
  it cannot promote itself.

Canonical Evolution Policy
- shared semantic changes require ownership, compatibility analysis, migration,
  validation, and authority.
```

Exact policy names and aggregate ownership remain under review.

---

## 11. Candidate Commands And Events

Commands should represent requested intent, not assumed success.

Candidate commands:

```text
DefineIntent
AcceptSpecification
RegisterCapability
PublishContractVersion
BindAdapter
StartWorkflowRun
RequestExecution
RecordEvidence
EvaluateGate
SubmitReview
RecordDecision
GrantApproval
AuthorizeDelivery
RecordFeedback
CreateLearningCandidate
ProposeCoreEvolution
AcceptEvolution
SupersedeAgreement
```

Candidate events:

```text
IntentDefined
SpecificationAccepted
CapabilityRegistered
ContractPublished
AdapterBound
WorkflowRunStarted
ExecutionStarted
ExecutionCompleted
ExecutionFailed
EvidenceRecorded
GateEvaluated
ReviewCompleted
DecisionBecameEffective
ApprovalGranted
DeliveryAuthorized
DeliveryCompleted
FeedbackRecorded
LearningCandidateCreated
EvolutionProposed
EvolutionAccepted
AgreementSuperseded
```

These are hypotheses. Events must not encode success without evidence or required authority.

---

## 12. Required Traceability

The canonical model must trace every retained first-class concept to:

```text
accepted philosophy distinction or law;
current repository source;
named owning bounded context;
entity, value-object, policy, service, command, event, or external concept role;
consumer in #7, #8, #9, ai-native-skills, native-ai-fw, or products;
compatibility impact on existing contracts;
validation case.
```

No concept should be accepted only because it appears in an existing diagram or workflow.

---

## 13. Validation Plan

### Foundation preservation

- Verify no concept collapses observation, model, assumption, claim, evidence, decision, authority, review, approval, or completion.
- Verify capability, permission, authority, and execution capacity remain separate.
- Verify feedback and learning cannot silently redefine core.

### Cross-document terminology

- Compare the candidate model against architecture, glossary, DDD guidance, port docs, workflow docs, and runtime docs.
- Mark each conflicting source as aligned, specialized, stale, superseded, or migration-required.

### Contract inventory

- Map all 106 registered contracts to owning contexts and first-class concepts.
- Verify each contract family has a clear domain role.
- Identify concepts used by contracts but unowned by the model.

### Lifecycle scenarios

Apply the model to at least:

```text
repository analysis without write authority;
new-feature implementation;
product-development release;
design review and approval;
runtime destructive action;
adapter conformance evaluation;
skill refinement and promotion;
memory versus current source-of-truth conflict;
contract semantic evolution.
```

### Negative tests

The model must prevent:

```text
plan represented as Execution Run;
contract declaration represented as Conformance Assessment;
review verdict represented as Approval;
release readiness represented as Delivery Authorization;
tool access represented as Authority;
feedback represented as Learning;
local fix represented as accepted Core Evolution;
generic status field hiding distinct lifecycle states.
```

---

## 14. Initial Decisions

Accepted for discovery:

```text
D1 The current domain-driven-model.md is guidance, not the canonical domain model.
D2 Product examples do not define Native AI Engineering bounded contexts.
D3 Definition and execution/run concepts must remain separate.
D4 Review, decision, approval, authorization, readiness, and delivery require explicit relationship modeling.
D5 Capability, Contract, Port, Adapter, and Binding require separate ownership review.
D6 Workflow-specific enums must not become one universal status taxonomy.
D7 Existing contracts remain accepted sources but do not automatically own canonical domain semantics.
D8 The canonical model should be smaller than the total vocabulary used by all contracts.
D9 Final port categories remain owned by issue #7.
D10 Machine serialization remains owned by issue #8.
```

Not yet accepted:

```text
final bounded-context count;
aggregate boundaries;
which concepts require stable identity;
authorization as object versus policy result;
Delivery as universal concept;
Product Binding as a core context;
Actor and Execution Surface taxonomy;
shared status vocabulary;
final commands and events;
contract migration or supersession plan.
```

---

## 15. Next Discovery Slice

1. Build a contract-to-context inventory for all registered contract families.
2. Produce a concept deduplication matrix across docs and contracts.
3. Decide the minimum bounded-context set.
4. Define candidate entities, value objects, policies, commands, and events per context.
5. Stress-test the candidate model against representative workflows.
6. Create the canonical domain-model entry point only after these decisions converge.

---

## 16. Current Verdict

```text
Accepted philosophy dependency: SATISFIED
Canonical domain model: NOT YET DEFINED
Current modeling guidance: USEFUL BUT NON-CANONICAL
Initial source inventory: COMPLETE FOR FIRST SLICE
Candidate context families: 10 UNDER REVIEW
Contract inventory: PARTIAL — MANIFEST FAMILY LEVEL ONLY
Definition-versus-run distinction: REQUIRED
Review/approval/authorization separation: REQUIRED
Port taxonomy: DEFER FINAL CATEGORIES TO #7
Machine schema: DEFER TO #8
Contract migrations: NONE AUTHORIZED
Ready for concept and context matrix: YES
Ready to freeze canonical model: NO
```