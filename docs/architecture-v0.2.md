# Native AI Engineering Architecture v0.2

Status: Operational architecture view

Philosophy foundation: [`philosophy/README.md`](philosophy/README.md)

Canonical domain model: [`domain-model/README.md`](domain-model/README.md)

Native AI OS boundary: [`native-ai-os.md`](native-ai-os.md)

## Definition

Native AI Engineering Architecture v0.2 is a domain-driven, ports-and-adapters architecture view for building AI-native digital products and operating systems.

It separates stable, governed product agreements from replaceable implementation tools.

This document explains an operational architecture model. It is not the philosophy kernel, does not redefine the canonical Native AI Engineering domain model, is not the complete Native AI OS product specification, and is not a universal numbering authority for every repository artifact.

Historical references to **Native AI Framework v0.2** describe this same architecture lineage. `Framework` remains valid for technical architecture, SDK, library, and adapter concepts, but **Native AI OS** is the product-level identity for an implementation that satisfies the qualification boundary in [`native-ai-os.md`](native-ai-os.md).

## Foundation Relationship

The architecture consumes the Native AI Engineering philosophy rather than redefining it.

The philosophy provides reusable boundaries for:

```text
state and model
claim and evidence
capability, permission, and authority
verification, validation, review, and approval
feedback, learning, and governed evolution
```

The architecture applies those boundaries to domain ownership, ports, adapters, agents, skills, knowledge, evaluation, and delivery.

## Native AI OS Relationship

Native AI OS is an executable product and control-plane implementation of Native AI Engineering. It coordinates the accepted domain model and lifecycle; it does not create a second domain model or acquire authority merely by coordinating execution.

```text
Native AI Engineering
  discipline, canonical domain model, contracts, and architecture
        ↓ implemented and coordinated by
Native AI OS
  control plane, persistent operating state, context assembly,
  runtime integration, adapter coordination, governance integration,
  learning, and observability
        ↓ applied to and validated by
product repositories
```

A runtime, framework, adapter workspace, task runner, workflow engine, or dashboard can be part of Native AI OS without independently qualifying as the complete operating system.

See [`native-ai-os.md`](native-ai-os.md) for canonical terminology, repository responsibility, control-plane boundaries, compatibility decisions, and qualification criteria.

## Core Principle

```text
Canonical domain and use-case agreements remain stable through governed change.
Ports define required capabilities and boundaries.
Adapters implement those capabilities without owning domain meaning.
Tools and providers remain replaceable.
Claims, reviews, and approvals remain scoped to appropriate evidence and authority.
Operating-system coordination does not create semantic ownership or approval authority.
```

Stability does not mean immutability. Canonical agreements may evolve through explicit ownership, compatibility review, evidence, migration, and required authority.

## Why v0.2 Exists

Version 0.1 described this lifecycle view:

```text
Intent
→ Blueprint
→ Engineering Contract
→ Knowledge
→ Rules
→ Skills
→ Agents
→ Tools
→ Memory
→ Execution Loop
→ Evaluation
→ Continuous Improvement
```

Version 0.2 improves the architecture by making it explicitly:

```text
domain-driven
port-based
adapter-agnostic
evidence-oriented
reviewed and approved proportionately to risk and authority
```

Human review may remain a repository or product governance default. The required reviewer, approver, and approval mode are policy decisions based on risk, reversibility, authority, affected consumers, and claim scope.

## Architecture Layers

```text
Intent Layer
→ Domain Layer
→ Application Layer
→ Contract Layer
→ Port Layer
→ Adapter Layer
→ Agent Layer
→ Rule Layer
→ Skill Layer
→ Knowledge Layer
→ Evaluation Layer
```

This sequence is an operational dependency view, not a bounded-context map. It must not compete with:

```text
the philosophy foundation stack;
the [canonical domain model](domain-model/README.md);
contract-family schemas owned by issue #8;
repository-specific package or deployment layers;
Native AI OS implementation topology.
```

## 1. Intent Layer

Defines product purpose, user problem, business goal, constraints, success metrics, accepted scope, and non-goals.

Intent records must remain distinguishable from inferred intent, implementation state, and delivery evidence.

## 2. Domain Layer

Defines the product domain using domain-driven modeling.

Includes:

```text
Core Domain
Subdomains
Bounded Contexts
Ubiquitous Language
Entities
Value Objects
Aggregates
Domain Events
Business Rules
```

The domain owns product meaning and business invariants. It must not be derived from one model provider, prompt shape, UI component, database table, adapter implementation, or operating-system surface.

Canonical Native AI Engineering objects, contexts, lifecycle semantics, and ownership are defined by the [canonical domain model](domain-model/README.md).

## 3. Application Layer

Defines use cases and workflows that coordinate domain behavior.

Includes:

```text
Use Cases
Policies
Application Services
Workflow Orchestration
State Transitions
Approval Gates
```

Application behavior must preserve the distinction between capability, permission, authority, decision, review, and approval.

## 4. Contract Layer

Defines stable agreements that agents, tools, workflows, ports, adapters, operating-system implementations, and product implementations must follow.

Includes:

```text
Engineering Contract
Port Contract
Adapter Contract
Evaluation Contract
Runtime Contract
Workflow Contract
Skill Contract
```

Contract presence or structural validity does not prove executable behavior, runtime integration, Native AI OS qualification, or product acceptance.

## 5. Port Layer

Defines required capabilities and boundaries without choosing implementation tools.

Examples:

```text
ModelInferencePort
CodeExecutionPort
DesignGenerationPort
DesignReviewPort
KnowledgeRetrievalPort
RepositoryPort
StoragePort
PublishingPort
EvaluationPort
```

A port capability does not automatically authorize every possible operation exposed by an adapter or control plane.

The canonical port taxonomy and first-class port-contract format remain owned by issue `#7`.

## 6. Adapter Layer

Provides replaceable implementations for ports and contracts.

Examples:

```text
model-provider adapter
coding-tool adapter
design-tool adapter
web-framework adapter
storage-provider adapter
publishing-integration adapter
runtime adapter
product adapter
```

Adapters may translate and implement a capability. They must not silently redefine domain meaning, canonical terms, contract ownership, approval authority, product policy, or Native AI OS qualification.

## 7. Agent Layer

Defines AI roles that operate inside the architecture and its authorized runtime surfaces.

Agents use contracts, rules, skills, ports, adapters, context, knowledge, and tools. Agents do not own domain decisions merely because they can execute work.

An agent-authored interpretation, plan, review, or output is not automatically an authoritative decision or approval.

## 8. Rule Layer

Defines reusable mandatory constraints.

Rules answer:

```text
What must or must not happen in this declared scope?
```

Rules may operationalize philosophy guardrails, contracts, architecture boundaries, security requirements, or repository policy. A local rule must not be presented as universal philosophy without the required generalization and authority review.

## 9. Skill Layer

Defines repeatable executable procedures and specialist methodology.

Skills answer:

```text
How should a reusable capability be performed?
```

Skill declaration or installation is not proof that the behavior was applied correctly. Behavioral evidence remains required for embodiment and conformance claims at the relevant layer.

## 10. Knowledge Layer

Stores explicit, reviewable source-of-truth product, domain, technical, policy, and decision knowledge.

Memory may assist retrieval and reasoning. Memory must not override a current authoritative source without verified supersession.

## 11. Evaluation Layer

Defines criteria, evidence requirements, quality gates, verification, validation, review, and approval integration.

Applicable evidence, evaluation, review, and approval gates must be satisfied according to:

```text
the claim being made;
the action being performed;
the affected scope and consumers;
the risk and reversibility;
the governing contract and policy;
the required authority.
```

A build, test, screenshot, static declaration, evaluation result, review verdict, OS dashboard state, or control-plane record supports only claims appropriate to its evidence method and coverage.

## Core Flow

```text
Intent
→ Domain Model
→ Use Case
→ Contract
→ Port
→ Adapter Selection
→ Authorized Execution
→ Evidence
→ Verification / Validation
→ Review / Approval where required
→ Delivery
→ Feedback and Governed Improvement
```

This flow is a relationship map, not a claim that one result automatically authorizes the next transition. Concrete contracts and policies own the applicable gates.

Native AI OS implementations may coordinate and expose this relationship through product-facing phases such as plan, design, build, test, review, release, operate, and learn. Those phases must map to the canonical relationship and preserve all required distinctions.

## Design Rule

Never let adapter, framework, runtime, or operating-system implementation choice define the domain.

Correct:

```text
Domain defines capability and meaning.
Port describes the required capability and boundary.
Contract defines the stable agreement.
Adapter implements the agreement.
Policy and authority govern material execution.
Evidence supports bounded claims.
Control-plane coordination preserves upstream ownership.
```

Wrong:

```text
Tool defines product architecture.
Tool access defines authority.
Generated output defines approved product truth.
Passing one check defines total completion.
Runtime state defines canonical domain truth.
Operating-system branding proves qualification.
```

## Illustrative Product Example

The following is an example only. It does not define the canonical Native AI Engineering domain.

Stable product concepts might include:

```text
Brand
IdentityLock
Campaign
CampaignBrief
CreativeDirection
GeneratedAsset
CreativeReview
Approval
Export
```

Replaceable adapters might include:

```text
model provider
coding tool
design tool
web framework
storage provider
publishing integration
```

A creative product is not merely a model wrapper. Its product meaning, decisions, validation criteria, and policies belong to its domain and product repository; replaceable adapters and Native AI OS coordination implement selected capabilities without acquiring that product meaning or authority.
