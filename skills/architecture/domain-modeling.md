# Domain Modeling Skill

## Purpose

Help agents transform product intent and business rules into a clear domain model before implementation.

## When To Use

Use this skill when:

- Designing a new product
- Designing a new module
- Adding a core business feature
- Creating backend architecture
- Creating database schema
- Preparing API contracts

## Required Input

```text
- Product intent
- User problem
- Core workflow
- Business rules
- Existing domain model if any
- Engineering Contract
```

## Process

### 1. Identify Business Capability

Define the business capability being modeled.

Example:

```text
Brand Identity Management
Campaign Generation
Creative Review
Asset Export
```

### 2. Extract Ubiquitous Language

List important terms used by users, product, and engineering.

Output:

```text
Term | Meaning | Notes
```

### 3. Identify Actors

List who interacts with this domain.

Examples:

```text
Brand Owner
Designer
Social Media Manager
AI Agent
Reviewer
```

### 4. Identify Use Cases

List meaningful business actions.

Format:

```text
As a <user>, I want to <action>, so that <outcome>.
```

### 5. Identify Entities

Entities have identity and lifecycle.

Ask:

```text
- Does this object need an ID?
- Does it change over time?
- Is its identity more important than its attributes?
```

### 6. Identify Value Objects

Value objects are defined by their attributes.

Ask:

```text
- Is this immutable?
- Is equality based on value?
- Can it validate a business rule?
```

### 7. Identify Aggregates

Define consistency boundaries.

Ask:

```text
- What must change together?
- What invariants must always hold?
- What can be eventually consistent?
```

### 8. Identify Domain Services

Use domain services only when business logic does not naturally belong to a single entity or value object.

### 9. Identify Repositories

Define repositories around aggregate roots, not every table.

### 10. Identify Domain Events

Use events for meaningful state changes.

Examples:

```text
BrandIdentityLocked
CampaignBriefApproved
AssetGenerated
CreativeApproved
AssetExported
```

## Output Format

```markdown
# Domain Model: <module-name>

## Business Capability

## Ubiquitous Language

## Actors

## Use Cases

## Entities

## Value Objects

## Aggregates

## Domain Services

## Repositories

## Domain Events

## Business Rules

## Open Questions
```

## Quality Checklist

- [ ] Domain model follows product language.
- [ ] Entities and value objects are not confused.
- [ ] Aggregates protect meaningful invariants.
- [ ] Repositories are not created for every table blindly.
- [ ] Domain events represent real business events.
- [ ] Business rules are explicit.
- [ ] Open questions are documented.

## Failure Handling

If the product intent is unclear, stop and produce a list of missing inputs instead of inventing the domain.

If the domain is simple CRUD, do not over-engineer DDD patterns.
