# Native AI OS — Terminology and Architecture Boundary

Status: Canonical architecture boundary

Canonical domain model: [`domain-model/README.md`](domain-model/README.md)

Atomic term authority: [`philosophy/term-authority.md`](philosophy/term-authority.md)

Related runtime evolution: [`puterakahfi/ai-native-fw#42`](https://github.com/puterakahfi/ai-native-fw/issues/42)

## 1. Purpose

This document defines the runtime-agnostic relationship between **Native AI Engineering**, **Native AI Core**, **Native AI OS**, executable skills, runtimes, adapters, and product repositories.

It does not create a second domain model, a competing lifecycle, or a mandatory deployment topology.

The accepted [Native AI Engineering canonical domain model](domain-model/README.md) remains authoritative for domain objects, bounded contexts, lifecycle semantics, ownership, evidence, review, approval, delivery, learning, and evolution.

## 2. Canonical distinctions

### Native AI Engineering

The discipline, principles, canonical domain model, contracts, lifecycle agreements, authority boundaries, and working model for building AI-native systems.

Native AI Engineering defines how intent, capabilities, methods, execution, evidence, governance, delivery, and learning relate without selecting one runtime, provider, product, or user interface.

### Native AI Core

The public, runtime-agnostic source of truth for Native AI Engineering domain language, contracts, ports, architecture boundaries, rules, templates, and quality standards.

Core defines what must remain stable. It does not implement the complete operating system, own private product context, select providers, or execute product work.

### Native AI OS

An executable product and control-plane system that applies Native AI Engineering across product lifecycles by coordinating product context, persistent lifecycle state, capabilities, workflows, agents, runtimes, adapters, authorized execution, artifacts, evidence, review, governance, feedback, learning, and observability.

Native AI OS consumes and specializes core-owned meaning. It must not silently redefine canonical domain objects, contracts, lifecycle semantics, authority, or approval.

### Framework

A reusable architecture, SDK, library, or implementation structure that provides extension points and conventions.

`Framework` remains a valid technical term where a framework is actually being described. It is not the canonical name for the complete Native AI OS product.

Historical uses of **Native AI Framework** may remain as compatibility or historical language until downstream migration is complete, but new product-level identity should use **Native AI OS**.

### Runtime

An execution surface in which actors, agents, skills, workflows, tools, hooks, context, and adapters operate.

A runtime can execute work without owning product-level planning, persistent lifecycle state, governance, product registry, learning, or cross-runtime coordination. Runtime presence alone does not qualify a system as Native AI OS.

### Control plane

A coordination boundary that resolves and governs product-level work across contexts without becoming every semantic owner, execution provider, or approval authority.

A control plane may coordinate:

```text
product and repository registry
intent and objective intake
context assembly
planning and task relationships
capability and adapter resolution
execution authorization requests
runtime and workflow coordination
artifact and evidence references
review and approval integration
policy and quality gates
feedback and learning proposals
observability and audit trails
```

A control plane does not automatically own:

```text
canonical domain meaning
provider implementation
product business policy
human authority
production approval
product acceptance
all execution status families
all artifacts or knowledge sources
```

Control-plane coordination is capability, not automatic permission, authority, approval, execution, or product acceptance.

### Product Brain

`Product Brain` is informal product language for the combined product-context, registry, decision, knowledge, memory, planning, and coordination experience exposed by an implementation.

It is not a canonical aggregate, bounded context, contract family, or authority source in Native AI Core.

Implementations may use the phrase in user-facing positioning if they preserve the canonical distinctions among context, knowledge, memory, decision, plan, execution, evidence, review, approval, and product acceptance.

## 3. Ecosystem relationship

```text
Native AI Engineering
  discipline, principles, canonical domain model, and working model

ai-native-core
  canonical domain, contracts, ports, terminology, boundaries, and standards
        ↓ implemented as reusable executable behavior
ai-native-skills
  skills, workflows, meta-skills, references, rubrics, and behavioral evaluation
        ↓ orchestrated and integrated by
Native AI OS
  control plane, persistent state, context assembly, orchestration, runtime integration,
  adapter coordination, governance integration, memory, learning, and observability
        ↓ applies to and learns through
product repositories
  product implementation, policy, product knowledge, delivery, and real-world validation
```

Agent runtimes, model providers, repositories, design tools, deployment systems, and other external systems remain replaceable adapters or providers behind accepted ports and bindings.

## 4. Canonical operating relationship

Native AI OS coordinates the existing canonical lifecycle; it does not replace it.

```text
IntentSpecification
→ Requirement and AcceptanceCriterion
→ DomainCapability and UseCase
→ CapabilityAgreement / Contract
→ Port requirement and AdapterBinding
→ WorkflowDefinition and SkillDefinition
→ CapacityAssessment and ExecutionAuthorization
→ ExecutionRun
→ Claim and EvidenceCase
→ GateResult, ReviewResult, and Approval where required
→ DeliveryRecord and Product Acceptance
→ FeedbackItem
→ LearningCandidate
→ accepted target-layer update or governed EvolutionProposal
```

An implementation may expose user-facing phases such as plan, design, build, test, review, release, operate, and learn. Those phases must map to the canonical objects and must not collapse required distinctions.

No transition is authorized or proven merely because the preceding artifact exists.

## 5. Native AI OS qualification criteria

A system may claim the **Native AI OS** identity when it can provide reviewable evidence for all material criteria below within its declared scope.

### 5.1 Central product-level coordination

The system coordinates product-level work across multiple capabilities, contexts, or execution surfaces rather than acting only as a passive library, isolated prompt collection, single-purpose adapter, or chat shell.

### 5.2 Explicit persistent lifecycle state

Material missions, objectives, tasks, execution attempts, artifacts, evidence, decisions, reviews, approvals, deliveries, or learning proposals have attributable and inspectable state appropriate to the claims being made.

Not every deployment must persist every domain object in one database. The requirement is explicit lifecycle state and traceability, not one storage topology.

### 5.3 Structured context assembly

Agents and workflows operate from bounded, attributable context that preserves source, scope, authority, time, uncertainty, and product ownership.

### 5.4 Capability and adapter orchestration

The system can discover, resolve, select, compose, or route capabilities, skills, ports, adapters, runtimes, and tools without allowing provider choice to redefine domain meaning.

### 5.5 Authorized execution

Material execution is bounded by capacity, permission, policy, authorization, and approval requirements appropriate to scope and risk.

Tool access or model confidence is not authority.

### 5.6 Artifact and evidence traceability

The system can distinguish generated outputs, execution artifacts, claims, evidence, gate results, review results, approvals, deliveries, and product acceptance.

### 5.7 Quality and governance gates

Completion and promotion claims are governed by checkable requirements, applicable evidence, review, approval, and human authority boundaries.

Generated output is not automatically completed, approved, delivered, accepted, or production-ready.

### 5.8 Feedback and learning flow

Execution and product feedback can produce traceable learning candidates and route accepted changes to the smallest correct owning layer.

Runtime and product observations may propose core evolution; they cannot silently redefine core.

### 5.9 Observability and explainability

The system can explain, within declared coverage:

```text
what was requested
which context and assumptions were used
which capabilities and adapters were selected
what was authorized and executed
what artifacts and evidence were produced
which gates, reviews, and approvals applied
what failed, retried, or remained partial
what learning was proposed or accepted
```

### 5.10 Human authority preservation

The system keeps product direction, architecture authority, material risk acceptance, production approval, and final product judgment with the actors and policies that legitimately own them.

Native AI OS does not imply full autonomy or agent ownership of the product.

## 6. What does not qualify by itself

The following may be useful components but do not independently qualify as Native AI OS:

```text
prompt collection
skill catalog
single agent profile
model wrapper
chat interface
task runner
workflow engine without product governance
runtime without persistent product coordination
adapter workspace
framework or SDK without operating state
static dashboard
knowledge base without execution and evidence
```

A product may initially implement only part of the qualification boundary. Such a product should state its maturity and coverage rather than claiming total OS embodiment.

## 7. Repository responsibility boundary

### `ai-native-core` owns

```text
canonical Native AI Engineering terms and domain meanings
runtime-agnostic lifecycle and architecture boundaries
contracts, ports, rules, templates, and quality standards
Native AI OS qualification boundary
compatibility guidance for canonical terminology
```

### `ai-native-skills` owns

```text
reusable executable skills, workflows, and meta-skills
specialist procedures and evidence-producing methods
behavioral evaluation for reusable capability implementation
```

### Native AI OS implementation owns

```text
control-plane application and product surfaces
persistent operating state
product and repository registry
context assembly and runtime coordination
capability, skill, adapter, and provider binding
execution orchestration and auditability
artifact, evidence, review, and approval integration
memory and learning runtime behavior
observability
```

### Product repositories own

```text
product-specific domain implementation and policy
private context, data, assets, and credentials
product acceptance criteria and release decisions
real-world validation and product feedback
```

## 8. Terminology compatibility decisions

| Term | Decision | Guidance |
|---|---|---|
| Native AI Engineering | retain | Canonical discipline and working model. |
| Native AI Core | retain | Canonical runtime-agnostic contract and architecture layer. |
| Native AI OS | add | Canonical product-level operating-system identity and qualification boundary. |
| Native AI Framework | compatibility alias / historical wording | Do not use as the new complete product identity. Preserve where required for migration or historical accuracy. |
| framework | retain when technical | Use for an actual SDK, library, architecture framework, or framework adapter. |
| framework architecture | rename where product-wide | Prefer Native AI Engineering architecture or Native AI OS architecture according to scope. |
| public framework | deprecate where it means core | Prefer public core, canonical contract layer, or architecture documentation. |
| runtime | retain | Execution surface; not synonymous with OS. |
| control plane | add | Runtime-agnostic coordination boundary with explicit non-authority rules. |
| Product OS | compatibility/product specialization | Prefer Native AI OS for the ecosystem product; use Product OS only for a bounded product-instance surface. |
| Product Brain | informal product language | Not a canonical core aggregate or authority source. |
| `native-ai-fw` / `ai-native-fw` | repository compatibility name | Runtime repository naming is migrated by its owning repository, not by core. |

## 9. Compatibility and migration rules

1. Do not bulk-replace every occurrence of `framework`.
2. Preserve technical framework meanings and `FrameworkAdapter` where semantically correct.
3. Rename product-wide identity and architecture wording only when it actually refers to the complete operating system or discipline.
4. Existing contract IDs, paths, versions, and adapter pins remain unchanged unless a separately approved migration requires them.
5. Historical issue IDs and canonical task IDs may retain legacy namespaces until their owning repository defines a migration and compatibility strategy.
6. Runtime repositories must adopt core terminology without copying this document as competing authority.
7. Product marketing may simplify language, but implementation and governance records must preserve canonical distinctions.

## 10. Non-goals

This boundary does not mandate:

```text
one agent runtime
one model provider
one user interface
one database
one deployment topology
one task manager
one product repository structure
full autonomous operation
automatic production mutation
agent ownership of approval or product acceptance
```

It also does not implement missions, tasks, execution storage, memory systems, control-plane UI, or repository rename operations.

## 11. Review checklist

Before describing a system as Native AI OS, verify:

- [ ] scope and maturity are declared;
- [ ] canonical domain meanings are preserved;
- [ ] runtime and control-plane responsibilities are distinguishable;
- [ ] lifecycle state and evidence are attributable;
- [ ] capability, permission, authority, review, and approval are not collapsed;
- [ ] provider and framework choices remain replaceable;
- [ ] product-specific policy remains outside universal core;
- [ ] feedback and learning do not silently redefine canonical agreements;
- [ ] human authority boundaries are explicit;
- [ ] limitations and partial embodiment are disclosed.
