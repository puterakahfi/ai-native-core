# Native AI Framework v0.1

## 1. Framework Definition

Native AI Framework is a reusable engineering framework for building AI-native digital products.

It defines how human product builders, software architects, AI agents, tools, rules, skills, knowledge, memory, and evaluation loops work together to produce maintainable software systems.

The framework is not a prompt collection. It is an engineering operating system for AI-assisted product development.

## 2. Core Philosophy

Traditional software development usually follows this flow:

```text
Requirements -> Architecture -> Code -> Deployment -> Maintenance
```

AI-native software development follows this flow:

```text
Intent -> Blueprint -> Experience Design -> Engineering Contract -> Knowledge -> Rules -> Skills -> Agents -> Tools -> Memory -> Execution Loop -> Evaluation -> Continuous Improvement
```

The core philosophy:

- Humans design the system.
- Agents execute inside the system.
- Rules prevent random output.
- Skills define repeatable execution methods.
- Tools provide action capability.
- Memory stores decisions and review history.
- Evaluation protects quality.

## 3. Framework Layers

### 3.1 Intent Layer

Defines the product goal, user problem, business constraint, and success metric.

Artifacts:

- Product intent
- User problem
- Success metric
- Non-goals

### 3.2 Blueprint Layer

Transforms intent into a product and system blueprint.

Artifacts:

- Product blueprint
- Domain model
- Bounded context
- Architecture Decision Record
- System diagram
- API contract
- Data model

### 3.3 Experience Design Layer

Turns product and feature blueprints into user flows, information architecture, wireframes, mockups, interaction contracts, and UI state definitions.

Artifacts:

- Design brief
- User flow
- Information architecture
- Wireframe
- Mockup
- Interaction contract
- UI state contract
- UI verification checklist

### 3.4 Engineering Contract Layer

Defines technical decisions that all agents must follow.

Artifacts:

- Stack decision
- Architecture rules
- Coding rules
- Testing rules
- Security rules
- Documentation rules

### 3.5 Knowledge Layer

Stores product, domain, business, design, and technical knowledge.

Artifacts:

- Product knowledge
- Domain knowledge
- Business rules
- Design knowledge
- Technical references

### 3.6 Rules Layer

Defines mandatory constraints.

Rules answer: what must or must not happen?

Examples:

- Clean Architecture rules
- DDD rules
- UI rules
- API rules
- Testing rules
- Security rules
- Code review rules

### 3.7 Skills Layer

Defines repeatable execution procedures.

Skills answer: how should the agent perform the work?

Examples:

- Backend skill
- Frontend skill
- Database skill
- Testing skill
- Refactoring skill
- shadcn/ui skill
- DDD skill
- API design skill
- Documentation skill

### 3.8 Agent Layer

Defines specialized AI roles.

Examples:

- Product Agent
- Planner Agent
- Architect Agent
- Builder Agent
- Reviewer Agent
- Tester Agent
- Documentation Agent

### 3.9 Tool / MCP Layer

Defines external tool access and governance.

Examples:

- IDE
- Terminal
- GitHub
- Database
- Browser
- Figma or design artifact tools
- CI/CD
- Observability
- External APIs

### 3.10 Memory Layer

Stores long-term decisions and reusable patterns.

Examples:

- Product decisions
- Previous architecture choices
- Codebase conventions
- Reusable patterns
- Known mistakes
- Review history

### 3.11 Loop Layer

Defines the repeatable execution loop.

```text
Plan -> Design -> Build -> Test -> Review -> Improve -> Document -> Deploy
```

### 3.12 Evaluation Layer

Defines quality gates.

Examples:

- Output quality
- Test result
- Architecture compliance
- Security compliance
- Performance
- Maintainability
- User value

## 4. Engineering Contract

The Engineering Contract is the shared agreement that all agents, tools, workflows, and generated code must follow.

No agent should make random technical decisions outside the contract.

Example:

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
  minimum_coverage: 85%

documentation:
  adr: required
  api_contract: required

security:
  baseline: OWASP
  secrets: never hardcode
```

## 5. Rules and Skills

Rules and skills must be separated.

```text
Rules = constraints
Skills = procedures
```

Rules define what is allowed and forbidden.
Skills define how work should be performed.

## 6. Agent Operating Model

Agents are not autonomous decision-makers by default.

Agents must operate using:

1. Intent
2. Blueprint
3. Engineering Contract
4. Relevant rules
5. Relevant skills
6. Allowed tools
7. Output format
8. Review checklist

## 7. Product Development Workflow

Default product workflow:

```text
Idea
-> Intent
-> Blueprint
-> Engineering Contract
-> Knowledge Preparation
-> Rule Selection
-> Skill Selection
-> Agent Planning
-> Execution
-> Test
-> Review
-> Documentation
-> Release
-> Evaluation
-> Memory Update
```

Default status system:

```text
idea
-> drafted
-> specified
-> contracted
-> planned
-> generated
-> needs_review
-> approved
-> implemented
-> tested
-> shipped
-> analyzed
-> improved
```

## 8. ExampleProduct as First Reference Product

ExampleProduct is the first product used to test and improve the framework.

Positioning:

```text
ExampleProduct = AI Creative Control System
```

Core workflow:

```text
Create Brand Profile
-> Define Identity Lock
-> Generate Campaign Brief
-> Generate Visual Direction
-> Generate Assets
-> Human Review
-> Approve
-> Export / Schedule
-> Analyze
-> Improve Brand Memory
```

## 9. v0.1 Scope

Version 0.1 is documentation-first.

Do first:

- Define methodology
- Define contract
- Define rules
- Define skills
- Define agents
- Define workflows
- Apply to ExampleProduct

Do later:

- CLI
- Agent runtime
- MCP automation
- Dashboard
- Evaluation engine
- Auto PR system
