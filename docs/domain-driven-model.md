# Domain-Driven Modeling Guide

Status: Modeling guide with non-normative product examples

Canonical Native AI Engineering domain model: [`domain-model/README.md`](domain-model/README.md)

## Purpose

This document explains how products use domain-driven modeling to keep product logic stable while tools, models, frameworks, and providers change. It is a guide, not the canonical Native AI Engineering domain model.

## Problem

AI-native products often start from tools instead of domain.

Examples:

```text
Start from prompt box
Start from model capability
Start from coding assistant
Start from design generator
Start from web framework
```

This creates products that are shaped by tools instead of user problems and business rules.

## Design Principle

```text
Business capability first.
Domain model second.
Ports third.
Adapters last.
```

## Core Concepts

## Core Domain

The most important business capability of the product.

Example:

```text
Illustrative product core domain = Creative Control
```

## Subdomain

A smaller business area inside the product domain.

Example:

```text
Brand Identity
Campaign Planning
Generation
Creative Review
Export
Feedback
```

## Bounded Context

A boundary where a model and language are consistent.

Example:

```text
IdentityLock in Brand Identity Context has different meaning from CreativeDirection in Campaign Context.
```

## Ubiquitous Language

Shared language used by product, engineering, agents, and documentation.

Example:

```text
Identity Lock
Campaign Brief
Creative Review
Approval Gate
Generated Asset
```

## Entity

An object with identity and lifecycle.

Examples:

```text
Brand
Campaign
GeneratedAsset
CreativeReview
```

## Value Object

An immutable object defined by value.

Examples:

```text
ColorRule
CampaignGoal
ReviewDecision
CTA
PlatformFormat
```

## Aggregate

A consistency boundary around related domain objects.

Examples:

```text
Brand Aggregate
Campaign Aggregate
Review Aggregate
```

## Domain Event

A meaningful business state change.

Examples:

```text
IdentityLockApproved
CampaignBriefApproved
AssetGenerated
AssetApproved
AssetExported
```

## Native AI Domain Modeling Flow

```text
Product Intent
-> Business Capability
-> Core Domain
-> Subdomains
-> Bounded Contexts
-> Ubiquitous Language
-> Entities and Value Objects
-> Aggregates
-> Domain Events
-> Use Cases
-> Ports
-> Adapters
```

## AI-Specific Domain Questions

Ask:

```text
What decision belongs to the domain?
What can AI assist?
What must remain human-approved?
What is a replaceable adapter?
What is source-of-truth knowledge?
What output needs evaluation?
What state transitions matter?
```

## Anti-Patterns

Avoid:

```text
Prompt as domain model
Model provider as product architecture
Tool output as approved decision
Database table as first design artifact
One super-agent owning all decisions
Memory replacing knowledge
```

## Illustrative Product Example

The following example is product-specific and non-normative.

Wrong:

```text
ExampleProduct is an image generation app.
```

Better:

```text
ExampleProduct is a creative control system.
```

Domain model:

```text
Brand
IdentityLock
Campaign
CampaignBrief
CreativeDirection
PromptFlow
GeneratedAsset
CreativeReview
Approval
Export
PerformanceInsight
```

AI models, design tools, and publishing tools implement capabilities through adapters. They do not define the domain.
