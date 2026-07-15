# Domain-Driven Design Rule

## Purpose

Ensure product and software design starts from the business domain instead of random database tables, screens, or generated code.

## Applies To

- Product blueprinting
- Domain modeling
- Backend architecture
- Database design
- API design
- AI workflow design

## Must Do

1. Identify the core domain before implementation.
2. Use a shared language between product, engineering, and agents.
3. Define bounded contexts when the product has multiple business areas.
4. Model entities, value objects, aggregates, repositories, domain services, and domain events when useful.
5. Keep business rules explicit.
6. Protect invariants inside aggregates or application services.
7. Use domain events for meaningful business state changes.
8. Keep persistence concerns separate from domain behavior.

## Must Not Do

1. Do not start with tables before understanding the domain.
2. Do not create anemic models by default when business behavior matters.
3. Do not let UI labels become the domain model without validation.
4. Do not mix unrelated bounded contexts in one module.
5. Do not expose database entities directly as public API contracts.
6. Do not invent complex DDD patterns where simple CRUD is enough.

## Core Modeling Questions

Ask:

```text
- What is the business capability?
- What language do users use?
- What are the core entities?
- What values must be immutable?
- What rules must always be true?
- What state changes matter?
- What belongs together as one consistency boundary?
- What can be eventually consistent?
```

## Review Checklist

- [ ] Core domain is identified.
- [ ] Ubiquitous language is documented.
- [ ] Bounded contexts are clear when needed.
- [ ] Entities and value objects are not confused.
- [ ] Business rules are explicit.
- [ ] Persistence model does not dominate domain model.
- [ ] Domain events are used only for meaningful state changes.

## ExampleProduct Example

Potential ExampleProduct bounded contexts:

```text
Brand Identity Context
- Brand
- BrandIdentity
- IdentityLock

Campaign Context
- Campaign
- CampaignBrief
- CreativeDirection

Generation Context
- PromptFlow
- GeneratedAsset
- GenerationJob

Review Context
- Review
- Approval
- CreativeQualityScore

Publishing Context
- Export
- PublishSchedule
- PerformanceInsight
```

Do not mix all of these into one generic `Project` model.
