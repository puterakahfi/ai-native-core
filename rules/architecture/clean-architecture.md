# Clean Architecture Rule

## Purpose

Ensure generated software keeps business logic independent from frameworks, databases, UI, and external services.

## Applies To

- Backend services
- Application modules
- Domain logic
- API handlers
- Background jobs
- AI workflow orchestration

## Must Do

1. Keep domain logic independent from infrastructure.
2. Put business rules in domain or application layer, not controllers.
3. Use interfaces/ports for external dependencies.
4. Keep database, framework, API, and third-party integrations in outer layers.
5. Make use cases/application services explicit.
6. Keep dependencies pointing inward.
7. Use DTOs or mappers at boundaries when needed.
8. Make side effects visible and testable.

## Must Not Do

1. Do not put business logic inside controllers, route handlers, or UI components.
2. Do not let domain entities import framework-specific modules.
3. Do not let database schema shape the entire domain model blindly.
4. Do not call external APIs directly from domain objects.
5. Do not hide critical side effects inside utility functions.
6. Do not introduce new architecture style without ADR.

## Layer Guidance

```text
Domain Layer
- Entities
- Value Objects
- Domain Services
- Domain Events

Application Layer
- Use Cases
- Commands / Queries
- Ports
- Transaction boundaries

Infrastructure Layer
- Database repositories
- External APIs
- File storage
- Queue implementation
- AI provider clients

Interface Layer
- REST controllers
- GraphQL resolvers
- UI actions
- CLI handlers
- Webhook handlers
```

## Review Checklist

- [ ] Domain logic is framework-independent.
- [ ] Controllers only coordinate request/response behavior.
- [ ] Application services express use cases clearly.
- [ ] Infrastructure dependencies are behind interfaces or ports.
- [ ] Tests can run against domain/application logic without real infrastructure.
- [ ] New architectural decisions are documented in ADR.

## ExampleProduct Example

For ExampleProduct, `BrandIdentity`, `IdentityLock`, and `CampaignBrief` should not depend on Next.js, Prisma, OpenAI API, or Cloudflare R2.

AI generation, storage, and export providers belong in infrastructure. Brand consistency rules belong in domain/application logic.
