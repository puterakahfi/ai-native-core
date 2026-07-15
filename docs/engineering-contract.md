# Engineering Contract

## Problem

AI agents often make random technical decisions when the stack, architecture, testing strategy, and documentation requirements are not explicitly defined.

This creates inconsistent systems and makes generated code hard to review and maintain.

## Why It Matters

The Engineering Contract is the shared agreement that all agents, tools, workflows, and generated code must follow.

It prevents agents from improvising architecture or choosing libraries without approval.

## Design Principle

```text
No agent should make random technical decisions outside the Engineering Contract.
```

## What the Contract Defines

The Engineering Contract should define:

```text
- Product name and version
- Architecture style
- Domain modeling approach
- Backend stack
- Frontend stack
- Database and ORM
- AI provider rules
- Media/storage decision
- Testing strategy
- Security baseline
- Documentation requirements
- Review requirements
```

## Contract Scope

The Engineering Contract applies to:

- Product agents
- Architect agents
- Builder agents
- Reviewer agents
- Tester agents
- Documentation agents
- Codex tasks
- MCP/tool workflows
- Generated code
- Architecture reviews

## Contract Change Rule

Any major change to the Engineering Contract requires an ADR.

Examples:

```text
- Switching backend framework
- Changing database
- Adding new AI provider
- Adding new queue system
- Changing architecture style
- Changing testing requirement
- Changing deployment strategy
```

## Contract Check Process

Before implementation, check:

1. Does the requested work fit the current contract?
2. Does it require a new dependency?
3. Does it require a new architecture decision?
4. Does it affect security?
5. Does it affect testing requirements?
6. Does it affect documentation?

## Anti-Patterns

Avoid:

- Letting Codex choose stack silently
- Adding libraries because they are convenient
- Changing folder structure without ADR
- Skipping tests despite contract requirement
- Hardcoding secrets
- Treating generated code as approved because it compiles

## Example

```yaml
architecture:
  style: Clean Architecture
  domain_modeling: Domain-Driven Design

backend:
  framework: NestJS
  database: PostgreSQL
  orm: Prisma

frontend:
  framework: Next.js
  ui: shadcn/ui
  styling: Tailwind CSS

testing:
  strategy: Test-Driven Development
  minimum_coverage: 85

documentation:
  adr: required
  api_contract: required

security:
  baseline: OWASP
  secrets: never hardcode
```

## ExampleProduct Contract

ExampleProduct has a product-specific Engineering Contract at:

```text
products/example-product/engineering-contract.yaml
```

That contract overrides generic defaults for ExampleProduct-specific creative, AI, review, and media requirements.
