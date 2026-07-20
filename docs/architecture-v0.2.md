# Native AI Framework Architecture v0.2

Status: Operational architecture view

Philosophy foundation: [`philosophy/README.md`](philosophy/README.md)

Canonical domain-model work: issue `#6`

## Definition

Native AI Framework v0.2 is a domain-driven, ports-and-adapters architecture view for building AI-native digital products.

It separates stable, governed product agreements from replaceable implementation tools.

This document explains an operational architecture model. It is not the philosophy kernel, not the final canonical Native AI Engineering domain model, and not a universal numbering authority for every repository artifact.

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

## Core Principle

```text
Canonical domain and use-case agreements remain stable through governed change.
Ports define required capabilities and boundaries.
Adapters implement those capabilities without owning domain meaning.
Tools and providers remain replaceable.
Claims, reviews, and approvals remain scoped to appropriate evidence and authority.
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

This sequence is an operational dependency view. It must not compete with:

```text
the philosophy foundation stack;
the canonical domain model owned by issue #6;
contract-family schemas owned by issue #8;
repository-specific package or deployment layers.
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

The domain owns product meaning and business invariants. It must not be derived from one model provider, prompt shape, UI component, database table, or adapter implementation.

The complete canonical Native AI Engineering domain model remains owned by issue `#6`.

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

Defines stable agreements that agents, tools, workflows, ports, adapters, and implementations must follow.

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

Contract presence or structural validity does not prove executable behavior, runtime integration, or product acceptance.

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

A port capability does not automatically authorize every possible operation exposed by an adapter.

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

Adapters may translate and implement a capability. They must not silently redefine domain meaning, canonical terms, contract ownership, approval authority, or product policy.

## 7. Agent Layer

Defines AI roles that operate inside the framework.

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

A build, test, screenshot, static declaration, evaluation result, or review verdict supports only claims appropriate to its evidence method and coverage.

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

## Design Rule

Never let adapter choice define the domain.

Correct:

```text
Domain defines capability and meaning.
Port describes the required capability and boundary.
Contract defines the stable agreement.
Adapter implements the agreement.
Policy and authority govern material execution.
Evidence supports bounded claims.
```

Wrong:

```text
Tool defines product architecture.
Tool access defines authority.
Generated output defines approved product truth.
Passing one check defines total completion.
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

A creative product is not merely a model wrapper. Its product meaning, decisions, validation criteria, and policies belong to its domain and product repository; replaceable adapters implement selected capabilities.