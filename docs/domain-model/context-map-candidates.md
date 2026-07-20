# Native AI Engineering Domain Model — Candidate Context Map

Status: Candidate discovery artifact — non-canonical

Issue: `#6 — Define the canonical Native AI Engineering domain model`

Branch: `6-canonical-native-ai-engineering-domain-model`

Accepted foundation: [`../philosophy/README.md`](../philosophy/README.md)

Concept ownership matrix: [`concept-ownership-matrix.md`](concept-ownership-matrix.md)

Aggregate slices:

- [`aggregate-lifecycle-candidates.md`](aggregate-lifecycle-candidates.md)
- [`aggregate-lifecycle-candidates-2.md`](aggregate-lifecycle-candidates-2.md)

This document defines candidate bounded-context responsibilities, upstream/downstream relationships, integration patterns, published language, anti-corruption boundaries, and prohibited ownership leakage.

It is not yet canonical authority and does not authorize contract, schema, manifest, validator, adapter, skill, workflow, runtime, or product migration.

---

## 1. Strategic Design Rules

Native AI Engineering uses these DDD strategic-design rules:

```text
one concept has one primary semantic owner;

language is internally consistent inside a bounded context;

different contexts exchange identifiers, immutable references, events,
or explicit contracts rather than sharing mutable domain objects;

upstream publication does not grant downstream execution authority;

downstream evidence does not silently redefine upstream agreements;

provider, runtime, repository, and product models enter core-facing contexts
through an anti-corruption boundary when their semantics differ;

context relationships are explicit and may evolve through governed compatibility,
not implicit imports or shared database access.
```

The context map describes semantic ownership and dependency direction. It does not require one process, service, database, repository, deployment unit, or team per context.

---

## 2. Candidate Bounded Contexts

| ID | Bounded context | Primary semantic responsibility |
|---|---|---|
| C1 | Intent And Specification | intent references, specifications, requirements, criteria, scope, constraints, assumptions, unknowns |
| C2 | Capability And Agreement | capability definitions, use-case definitions, contract definitions, reusable rules and compatibility intent |
| C3 | Method And Workflow | skill definitions, workflow definitions, phases, gates, handoffs, methods and shortcut definitions |
| C4 | Port, Adapter, And Runtime Binding | port definitions, adapter definitions, tool definitions, runtime bindings and binding compatibility |
| C5 | Execution And Operations | workflow runs, phase runs, execution runs, operation attempts, delivery records and rollback records |
| C6 | Evidence, Evaluation, And Acceptance | observations, evidence, claims, assessments, evaluations, gates, reviews, conformance, readiness and completion |
| C7 | Governance, Risk, And Authority | decisions, effective decisions, authority, permission references, approval, policy, risk, conflict, supersession and authorization |
| C8 | Context, Knowledge, And Memory | context requirements, context packs, knowledge artifacts, memory records, retrieval results, source designations and context gaps |
| C9 | Product Instance And Registry | product identity, repositories, product bindings, environments, product policies, targets and validation references |
| C10 | Feedback, Learning, And Evolution | feedback, learning candidates, generalization, target-layer recommendation, evolution proposals, migration and adoption evidence |

The context IDs are navigation labels during discovery. Accepted names and IDs remain subject to final pruning.

---

## 3. Context Classification Candidate

This classification describes importance, not authority hierarchy.

### Core domain candidates

```text
C1 Intent And Specification;
C5 Execution And Operations;
C6 Evidence, Evaluation, And Acceptance;
C7 Governance, Risk, And Authority;
C10 Feedback, Learning, And Evolution.
```

These contexts distinguish Native AI Engineering from tool-driven automation by preserving intent, bounded execution, evidence, authority, and governed learning.

### Supporting domain candidates

```text
C2 Capability And Agreement;
C3 Method And Workflow;
C4 Port, Adapter, And Runtime Binding;
C8 Context, Knowledge, And Memory;
C9 Product Instance And Registry.
```

These contexts make the core domain repeatable, reusable, replaceable, attributable, and product-applicable.

This classification is provisional. A supporting context may still own mandatory canonical semantics.

---

## 4. Integration Pattern Policy

### Published Language

Use a stable, versioned, documented language for cross-context messages and references such as:

```text
Specification Reference;
Capability Reference;
Contract And Version Reference;
Workflow Definition Reference;
Runtime Binding Reference;
Execution Run Reference;
Evidence Reference;
Assessment Reference;
Decision Case Reference;
Context Pack Checkpoint Reference;
Product Instance Reference;
Learning Candidate Reference;
Evolution Proposal Reference.
```

Issue `#8` will decide machine-readable schema shapes.

### Open Host Service

A context may publish application-facing operations for multiple consumers without exposing aggregate internals.

Examples:

```text
resolve contract version;
start workflow run;
record execution result;
freeze evidence set;
assess claim;
derive effective decision;
assess authorization;
assemble context pack;
resolve product binding;
create evolution proposal.
```

### Customer–Supplier

Use when a stable upstream context must account for legitimate downstream needs without allowing downstream implementation details to redefine upstream language.

### Anti-Corruption Layer

Use when translating:

```text
provider models;
repository and issue-tracker models;
runtime and tool responses;
external organizational authority systems;
product-specific configuration;
legacy terminology;
third-party evaluation or deployment systems.
```

The ACL preserves source semantics and provenance while producing the bounded language required by the consuming context.

### Shared Kernel

No broad Shared Kernel is accepted as the default relationship between Native AI Engineering contexts.

A future shared kernel may contain only deliberately minimal immutable primitives such as stable identifiers, source references, scope, coverage, version references, and timestamps when issue `#8` proves that sharing reduces rather than creates semantic ambiguity.

Shared mutable entities, status enums, decision objects, evidence objects, and workflow state are prohibited across contexts.

### Conformist

Conformist behavior is not the default for product, adapter, or runtime contexts.

A downstream implementation must conform to accepted public contracts where applicable, but it may use an ACL to preserve local models and provider details. Conformance to a contract is not adoption of the upstream aggregate model.

---

# 5. Primary Context Relationships

## R1 — C2 Capability And Agreement → C1 Intent And Specification

```text
upstream: C2

downstream: C1

pattern: Open Host Service + Published Language + Customer–Supplier
```

C2 publishes stable capability, use-case, contract, rule, and compatibility references.

C1 references these definitions when expressing what a specification expects.

Invariants:

```text
C1 requirement does not mutate C2 capability definition;

unmet requirement may record a Capability Gap or learning input;

new capability need routes through C2 ownership and governed evolution;

C2 implementation details do not leak into C1 intent or acceptance semantics.
```

## R2 — C1 Intent And Specification → C5 Execution And Operations

```text
upstream: C1

downstream: C5

pattern: Published Language
```

C5 references an attributable specification version, scope, criteria, assumptions, and unknowns when execution is intended to satisfy declared work.

Invariants:

```text
execution cannot rewrite specification content;

implementation existence does not change accepted scope;

scope change creates a proposed specification version or C7 decision route;

standalone execution still requires explicit intent and scope even when no Specification aggregate exists.
```

## R3 — C2 Capability And Agreement → C3 Method And Workflow

```text
upstream: C2

downstream: C3

pattern: Open Host Service + Published Language
```

C3 references stable capabilities and contracts when defining reusable methods and workflows.

Invariants:

```text
methodology does not redefine capability ownership;

workflow phase order does not rewrite contract semantics;

skill implementation may specialize method but remains bounded by its contract;

contract breaking change creates explicit workflow compatibility work.
```

## R4 — C2 Capability And Agreement → C4 Port, Adapter, And Runtime Binding

```text
upstream: C2

downstream: C4

pattern: Open Host Service + Published Language
```

C4 exposes and implements capability boundaries through ports, adapters, tools, and runtime bindings.

Invariants:

```text
Port Definition ≠ Capability Definition;

Adapter Definition ≠ Contract Definition;

binding cannot expand upstream owned responsibility;

provider capability does not override accepted contract boundary;

issue #7 owns final port taxonomy and machine contract structure.
```

## R5 — C3 Method And Workflow → C4 Port, Adapter, And Runtime Binding

```text
upstream: C3

downstream: C4

pattern: Published Language
```

C4 may bind executable skill or workflow adapters to accepted C3 definitions.

Invariants:

```text
skill installation ≠ skill application;

adapter metadata ≠ behavioral conformance;

runtime binding selects executable surfaces but does not become method authority;

provider-specific commands remain inside C4 ACLs or product/runtime bindings.
```

## R6 — C3 Method And Workflow → C5 Execution And Operations

```text
upstream: C3

downstream: C5

pattern: Open Host Service + Published Language
```

C5 starts and coordinates Workflow Runs using pinned Workflow Definition versions.

Invariants:

```text
Workflow Definition ≠ Workflow Run;

Phase Definition ≠ Phase Run;

Gate Definition ≠ Gate Evaluation;

new workflow version does not rewrite active or historical runs;

mid-run migration requires explicit compatibility and authority.
```

## R7 — C4 Port, Adapter, And Runtime Binding → C5 Execution And Operations

```text
upstream: C4

downstream: C5

pattern: Open Host Service + Published Language
```

C5 resolves authorized runtime bindings and records actual operations against them.

Invariants:

```text
Runtime Binding ≠ Execution Run;

binding active ≠ runtime healthy;

technical permission ≠ authority;

adapter availability ≠ execution capacity;

Execution Run preserves the exact binding and tool references used.
```

Provider and tool APIs are translated through C4 anti-corruption layers before their results enter C5 domain records.

## R8 — C1, C2, C3, And C5 → C6 Evidence, Evaluation, And Acceptance

```text
upstream sources:
  C1 criteria and scope;
  C2 contracts and rules;
  C3 gate definitions and evidence expectations;
  C5 observations, artifacts and execution records;

downstream: C6

pattern: Published Language + Anti-Corruption Layer for execution outputs
```

C6 evaluates bounded claims against declared criteria using attributable evidence.

Invariants:

```text
criterion ≠ assessment;

contract presence ≠ conformance;

execution output ≠ evidence for every claim;

source inspection ≠ runtime behavior proof;

Gate Evaluation ≠ Authorization Assessment;

Review Verdict ≠ Approval.
```

C6 translates runtime and provider output into Evidence Items without inheriting provider success semantics as domain truth.

## R9 — C6 Evidence, Evaluation, And Acceptance → C5 Execution And Operations

```text
upstream: C6

downstream: C5

pattern: Published Language
```

C5 may use Gate Evaluation, readiness, completion, or review results to determine the next workflow transition.

Invariants:

```text
assessment result controls only the transition named by its policy;

PASS does not grant authority for destructive or governed action;

NOT_VERIFIED remains visible and cannot be converted to PASS by activity;

C5 cannot rewrite C6 findings or verdicts.
```

## R10 — C6 Evidence, Evaluation, And Acceptance → C7 Governance, Risk, And Authority

```text
upstream: C6

downstream: C7

pattern: Open Host Service + Published Language
```

C7 consumes evidence and assessments when making or resolving governed decisions.

Invariants:

```text
Evidence ≠ Authority;

Review Verdict ≠ Approval;

readiness ≠ authorization;

approval cannot convert missing evidence into verified fact;

C7 preserves the evidence scope and limitations it relies upon.
```

## R11 — C7 Governance, Risk, And Authority → C5 Execution And Operations

```text
upstream: C7

downstream: C5

pattern: Open Host Service + Published Language
```

C5 resolves Effective Decision and Authorization Assessment references before governed operations.

Invariants:

```text
permission ≠ authority;

approval applies only to named scope and action;

authorization is time- and action-bounded;

AUTHORIZED ≠ executed;

execution completion cannot expand authorization scope.
```

## R12 — C7 Governance, Risk, And Authority → C1, C2, C3, C4, C6, C8, C9, And C10

```text
upstream: C7

downstream: governed context

pattern: Open Host Service + Published Language
```

C7 publishes policy, authority requirements, effective decisions, supersession, risk acceptance, waiver, and authorization references.

C7 is not a god context.

Invariants:

```text
C7 governs action and change rights but does not own technical implementation facts;

C7 cannot fabricate evidence or domain state owned elsewhere;

other contexts retain their own invariants after authorization;

authority does not bypass non-overridable safety, contract, evidence, or compatibility gates;

context-specific mutation still occurs through the owning aggregate.
```

## R13 — C8 Context, Knowledge, And Memory → All Material Consumer Contexts

```text
upstream: C8

downstream: C1–C7, C9 and C10 as applicable

pattern: Open Host Service + Published Language + Anti-Corruption Layer
```

C8 assembles attributable context and source references for a declared consumer and purpose.

Invariants:

```text
Context Pack ≠ source of truth;

retrieval ≠ verification;

memory ≠ current state;

summary ≠ authoritative source;

context availability ≠ capacity or authority;

consumer records the Context Pack checkpoint actually used.
```

C8 uses ACLs for external document stores, chats, search systems, repository hosts, and memory backends.

## R14 — C2, C3, And C4 → C9 Product Instance And Registry

```text
upstream: C2, C3 and C4

downstream: C9

pattern: Published Language + Customer–Supplier
```

C9 binds product instances to accepted capabilities, contracts, methods, ports, adapters, and runtimes.

Invariants:

```text
product specialization cannot redefine upstream meaning;

product binding records exact versions and references where applicable;

product policy may narrow or specialize but cannot silently weaken core guardrails;

provider and repository details remain inside C9/C4 ACLs;

product feedback requesting upstream change routes through C10 and C7.
```

## R15 — C9 Product Instance And Registry → C1 And C5

```text
upstream: C9

downstream: C1 and C5

pattern: Published Language
```

C1 may reference product intent, ownership, policy, environment, and repository boundaries.

C5 may resolve product bindings, environment bindings, delivery targets, and product policy references.

Invariants:

```text
Product Registry Entry ≠ product health;

Product Binding ≠ Runtime Binding activation;

Delivery Target ≠ release eligibility;

product ownership reference ≠ authorization for every action;

execution remains recorded in C5.
```

## R16 — C5, C6, And C9 → C10 Feedback, Learning, And Evolution

```text
upstream sources:
  C5 execution consequences and incidents;
  C6 findings, assessments and evidence;
  C9 product metrics, validation and field outcomes;

downstream: C10

pattern: Published Language + Anti-Corruption Layer
```

C10 converts attributable feedback into bounded learning candidates and evolution proposals.

Invariants:

```text
feedback ≠ learning;

one success ≠ reusable rule;

one product result ≠ universal truth;

local fix ≠ shared promotion;

C10 preserves source case, evidence, scope, environment and counterexamples.
```

C10 ACLs remove product-specific implementation details when testing generalization, while preserving source provenance.

## R17 — C10 Feedback, Learning, And Evolution → C2, C3, C8, C9 And Other Target Contexts

```text
upstream supplier: C10

downstream owner: target context

pattern: Customer–Supplier + Published Language
```

C10 publishes Learning Candidate and Evolution Proposal references. The target context remains owner of its definitions and mutation rules.

Invariants:

```text
proposal ≠ accepted change;

promotion recommendation ≠ write authority;

C7 decision is required for governed shared or canonical change;

target context validates its own invariants before mutation;

implemented change ≠ migrated consumer;

migration evidence remains bounded by consumer and version.
```

C10 is a proposal supplier, not upstream semantic authority over every target context.

---

# 6. External And Repository Boundaries

## E1 — Provider And Tool Ecosystems → C4

```text
external upstream: model providers, coding agents, design tools,
repository APIs, browsers, databases, storage, deployment systems

downstream: C4

pattern: Anti-Corruption Layer
```

Provider request, response, error, permission, quota, and status models remain provider-specific. C4 translates them into bounded adapter, tool, binding, capability, limitation, and failure language.

## E2 — Repository And Runtime State → C5 And C8

```text
external source: repository, filesystem, runtime, environment, logs, CI

consumers: C5 for execution records; C8 for context assembly

pattern: Anti-Corruption Layer + Published Source Reference
```

The same external observation may support different bounded records without becoming one shared mutable object.

## E3 — Organizational Authority Systems → C7

```text
external source: repository roles, organization policy, identity systems,
owner instructions, approvals, legal or security authority

downstream: C7

pattern: Anti-Corruption Layer
```

C7 records attributable authority and permission references without importing one provider's access-control model as universal authority semantics.

## E4 — Product Repositories → C9

```text
external source: product repository, engineering contract, ADRs,
product policy, runtime configuration, field evidence

downstream: C9

pattern: Anti-Corruption Layer + Customer–Supplier
```

Product details remain local. C9 exposes only the canonical product-instance references required by universal consumers.

---

# 7. Repository Responsibility Mapping

This mapping describes implementation responsibility, not context ownership transfer.

| Context | `ai-native-core` | `ai-native-skills` | `native-ai-fw` | Product repositories |
|---|---|---|---|---|
| C1 | canonical specification language and contracts | specification methods | task/spec orchestration and storage adapters | product requirements and accepted scopes |
| C2 | capability, use-case and contract authority | executable capability adapters | discovery and registry consumers | product-specific capability needs and bindings |
| C3 | skill/workflow definition contracts | executable methods and workflows | orchestration and application tracking | product workflow specialization |
| C4 | port/adapter/binding language and contracts | executable skill adapters | runtime, tool and provider bindings | product-specific adapter and environment selection |
| C5 | run and operation semantics | execution methods | control plane and run records | actual implementation and delivery mechanisms |
| C6 | evidence, evaluation and conformance semantics | reviewers and evaluation runners | evidence orchestration and result storage | product acceptance and field evidence |
| C7 | decision, authority, policy and risk semantics | provenance and governance methods | policy routing and authorization enforcement | product/repository authority and risk decisions |
| C8 | context, knowledge and memory semantics | context-engineering methods | context-pack assembly and retrieval adapters | authoritative product knowledge and local memory sources |
| C9 | product-instance and binding language | product-management methods | product registry and binding control plane | product instance, repositories, environments and policies |
| C10 | feedback, learning and evolution semantics | skill-evolution workflow | learning routing and migration orchestration | source cases, feedback and product validation |

No downstream repository may redefine the canonical meaning owned by core. Core must not absorb private credentials, customer data, provider configuration, or product-specific implementation state.

---

# 8. Prohibited Context Leakage

```text
C1 must not own implementation or approval authority.

C2 must not encode provider or product implementation as universal domain fact.

C3 must not claim a method was applied because a definition exists.

C4 must not redefine capability, contract, workflow, or product policy.

C5 must not self-assess quality, approval, or canonical completion.

C6 must not self-authorize governed action.

C7 must not fabricate technical evidence or mutate foreign aggregates.

C8 must not convert retrieval, memory, or summaries into authority.

C9 must not generalize one product implementation into core.

C10 must not self-promote learning or self-approve evolution.
```

Cross-context database access, mutable-object sharing, implicit status propagation, and unversioned semantic imports are prohibited as default integration strategies.

---

# 9. Cross-Context Process Example

The following is a relationship example, not one mandatory linear workflow:

```text
C9 Product Instance
→ supplies product, repository and environment boundaries;

C8 Context Pack
→ assembles attributable sources and gaps;

C1 Specification
→ declares bounded intent, scope, requirements and criteria;

C2 Capability And Agreement
→ supplies stable capabilities and contracts;

C3 Workflow Definition
→ supplies reusable phases, gates and methods;

C4 Runtime Binding
→ resolves replaceable implementation surfaces;

C7 Authorization Assessment
→ determines whether the named operation may proceed;

C5 Workflow Run And Execution Run
→ record actual coordinated and performed work;

C6 Evidence Set And Assessments
→ evaluate claims, gates, conformance, readiness and completion;

C7 Decision Case
→ records approval, risk acceptance, conflict and effective decision;

C5 Delivery Record
→ records the authorized transition or handoff;

C10 Learning Candidate
→ evaluates reusable lessons from bounded feedback;

C10 Evolution Proposal + C7 Decision
→ govern shared or canonical change;

Target Context + C5 Execution + C6 Evidence
→ implement, migrate and verify the accepted evolution.
```

Each step may be omitted when not applicable, but omitted responsibilities remain explicit rather than silently collapsed.

---

# 10. Open Strategic Questions

1. Should C2 remain one bounded context for Capability, Use Case, Contract, and reusable Rule, or split Contract Governance after issue `#8` exposes lifecycle complexity?
2. Should C3 contain both Skill Definition and Workflow Definition, or are their ownership and evolution pressures different enough to justify separate contexts?
3. Should C4 include Tool Definition and Model Provider Binding, or should provider/tool catalog become a separate generic integration context?
4. Should C5 `Workflow Run` remain the orchestration aggregate while long-running distributed execution uses a process manager outside aggregate boundaries?
5. Should C6 Review Record be owned inside Evaluation Run or remain an independent aggregate for specialist-review lifecycle?
6. Is C7 too broad, requiring future separation between Decision Provenance and Policy/Risk, or does one decision case language provide the necessary consistency boundary?
7. Should C8 Source-Of-Truth Designation remain a cross-context governed relation rather than an aggregate-owned field?
8. Which C9 registry concepts are canonical domain concepts versus `native-ai-fw` control-plane projections?
9. Should C10 Learning Candidate and Evolution Proposal remain one bounded context while retaining separate aggregates?
10. Which relationships require explicit ACL adapters or published-language schemas in issues `#7` and `#8`?
11. Which events are public integration events versus internal aggregate events?
12. Which normalized read models may span contexts without becoming mutation authority?

---

# 11. Validation Gates

Before this context map may become canonical:

- [ ] each retained concept has one primary semantic owner;
- [ ] every relationship names upstream, downstream, and integration pattern;
- [ ] no context requires shared mutable domain objects;
- [ ] no broad Shared Kernel is introduced without demonstrated need;
- [ ] provider, runtime, repository, organizational-authority, and product models use ACLs where semantics differ;
- [ ] C7 governance does not become a god context;
- [ ] C8 context assembly does not become truth or authority;
- [ ] C10 evolution does not become self-promotion;
- [ ] product specialization cannot redefine universal core;
- [ ] definition, run, evidence, assessment, decision, authorization, and evolution remain separate across boundaries;
- [ ] repository responsibility mapping matches actual repository responsibilities;
- [ ] issue `#7` can consume C2/C4 capability, port, adapter, binding, failure, risk and observability boundaries;
- [ ] issue `#8` can define published-language schemas and stable references without copying aggregate internals;
- [ ] issue `#9` can implement layered conformance and assessment semantics without one global status;
- [ ] `ai-native-skills` can implement methods without acquiring core authority;
- [ ] `native-ai-fw` can orchestrate contexts through application services, process managers and adapters;
- [ ] product repositories can specialize the model without importing private implementation into core.

---

# 12. Current Verdict

```text
Candidate bounded contexts: 10
Primary semantic ownership: CANDIDATE ASSIGNED
Core vs supporting classification: CANDIDATE
Primary relationships: 17
External ACL boundaries: 4
Published Language policy: DEFINED
Open Host Service policy: DEFINED
Shared Kernel default: REJECTED
Shared mutable cross-context model: REJECTED
Repository responsibility mapping: DEFINED
Context leakage guardrails: DEFINED
Contract or schema migrations: NONE AUTHORIZED
Canonical context map ready to freeze: NO
Ready for context and aggregate pruning review: YES
```