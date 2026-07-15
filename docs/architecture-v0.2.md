# Native AI Framework Architecture v0.2

## Definition

Native AI Framework v0.2 is a domain-driven, ports-and-adapters framework for building AI-native digital products.

It separates stable product architecture from replaceable implementation tools.

## Core Principle

```text
Domain is stable.
Use cases are stable.
Ports define required capabilities.
Adapters implement capabilities.
Tools and providers are replaceable.
```

## Why v0.2 Exists

Version 0.1 defined the lifecycle:

```text
Intent -> Blueprint -> Engineering Contract -> Knowledge -> Rules -> Skills -> Agents -> Tools -> Memory -> Execution Loop -> Evaluation -> Continuous Improvement
```

Version 0.2 improves the architecture by making the framework explicitly:

```text
Domain-driven
Port-based
Adapter-agnostic
Evaluation-first
Human-reviewed by default
```

## Architecture Layers

```text
Intent Layer
-> Domain Layer
-> Application Layer
-> Contract Layer
-> Port Layer
-> Adapter Layer
-> Agent Layer
-> Rule Layer
-> Skill Layer
-> Knowledge Layer
-> Evaluation Layer
```

## 1. Intent Layer

Defines product purpose, user problem, business goal, constraints, and success metric.

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

## 4. Contract Layer

Defines stable agreements that agents, tools, workflows, and implementations must follow.

Includes:

```text
Engineering Contract
Port Contract
Adapter Contract
Evaluation Contract
```

## 5. Port Layer

Defines required capabilities without choosing implementation tools.

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

## 6. Adapter Layer

Provides replaceable implementations for ports.

Examples:

```text
Model provider adapter
Coding tool adapter
Design tool adapter
Web framework adapter
Storage provider adapter
Publishing integration adapter
```

## 7. Agent Layer

Defines AI roles that operate inside the framework.

Agents use contracts, rules, skills, ports, and adapters. Agents do not own domain decisions.

## 8. Rule Layer

Defines mandatory constraints.

Rules answer:

```text
What must or must not happen?
```

## 9. Skill Layer

Defines repeatable execution procedures.

Skills answer:

```text
How should work be performed?
```

## 10. Knowledge Layer

Stores source-of-truth product, domain, technical, and decision knowledge.

Memory can assist recall. Knowledge is the source of truth.

## 11. Evaluation Layer

Defines quality gates and acceptance checks.

Evaluation must happen before approval, export, deployment, or publishing.

## Core Flow

```text
Intent
-> Domain Model
-> Use Case
-> Port Contract
-> Adapter Selection
-> Execution
-> Review
-> Evaluation
-> Improvement
```

## Design Rule

Never let adapter choice define the domain.

Correct:

```text
Domain defines capability.
Port describes capability.
Adapter implements capability.
```

Wrong:

```text
Tool defines product architecture.
```

## ExampleProduct Example

Stable domain:

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

Replaceable adapters:

```text
Model provider
Coding tool
Design tool
Web framework
Storage provider
Publishing integration
```

ExampleProduct is not a model wrapper. ExampleProduct is a creative control domain implemented through replaceable adapters.
