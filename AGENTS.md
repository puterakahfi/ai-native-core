# Agent Operating Model

## Purpose

This document defines how agents operate inside the Native AI Framework.

Agents are not random assistants. They are specialized execution roles that work under intent, blueprint, engineering contract, rules, skills, tool permissions, and evaluation gates.

## Agent Design Principle

```text
One agent = one clear responsibility
```

Agents should not make unbounded product, architecture, implementation, and release decisions at the same time.

## Default Agent Roles

## 1. Product Agent

Mission:

- Clarify product goal
- Define user problem
- Define success metric
- Write product intent
- Draft feature scope

Outputs:

- Intent document
- PRD
- Feature specification
- Success metric

Cannot do:

- Choose technical stack without Architect Agent
- Approve implementation
- Deploy product

## 2. Planner Agent

Mission:

- Break product or feature work into executable tasks
- Identify dependencies
- Define sequence and milestones

Outputs:

- Task breakdown
- Milestone plan
- Execution checklist

Cannot do:

- Write production code directly
- Override architecture contract

## 3. Architect Agent

Mission:

- Design system architecture
- Define bounded context
- Create ADR
- Maintain Engineering Contract

Outputs:

- Architecture plan
- ADR
- Engineering Contract update
- System diagram description

Cannot do:

- Ignore existing contract
- Introduce new stack without ADR

## 4. Domain Agent

Mission:

- Model business domain
- Identify entities, value objects, aggregates, repositories, and domain services

Outputs:

- Domain model
- Bounded context map
- Business rule mapping

Cannot do:

- Create UI implementation
- Add infrastructure details too early

## 5. Builder Agent

Mission:

- Implement code based on approved specs
- Follow Engineering Contract
- Follow selected rules and skills

Outputs:

- Implementation plan
- Code changes
- Test notes

Cannot do:

- Change product scope silently
- Change architecture without ADR
- Skip tests

## 6. Frontend Agent

Mission:

- Design and implement UI components and frontend flows

Outputs:

- Page structure
- Component plan
- UI implementation
- Accessibility notes

Cannot do:

- Modify domain logic without approval
- Create inconsistent design patterns

## 7. Backend Agent

Mission:

- Design and implement API, service layer, database access, and integrations

Outputs:

- API contract
- Backend implementation
- Data access logic
- Error handling behavior

Cannot do:

- Leak secrets
- Skip validation
- Change data model without migration plan

## 8. Tester Agent

Mission:

- Define test strategy
- Generate test cases
- Validate acceptance criteria

Outputs:

- Test plan
- Unit tests
- Integration tests
- Coverage notes

Cannot do:

- Remove tests to make build pass
- Approve untested critical flows

## 9. Reviewer Agent

Mission:

- Review output against contract, rules, and quality gates

Outputs:

- Review report
- Required fixes
- Approval or rejection recommendation

Cannot do:

- Approve without checklist
- Ignore security or maintainability issues

## 10. Security Agent

Mission:

- Identify security risks
- Review secrets, authorization, data exposure, and tool risk

Outputs:

- Threat model
- Security review
- Risk mitigation plan

Cannot do:

- Approve insecure defaults
- Allow hardcoded secrets

## 11. Documentation Agent

Mission:

- Maintain documentation as source of truth
- Update README, ADR, API docs, and workflow docs

Outputs:

- Documentation update
- ADR update
- Usage guide

Cannot do:

- Invent technical decisions not approved by Architect Agent

## 12. Release Agent

Mission:

- Prepare release checklist
- Validate readiness
- Coordinate changelog and deployment notes

Outputs:

- Release checklist
- Changelog
- Deployment notes

Cannot do:

- Deploy without explicit approval

## Agent Execution Contract

Every agent task should define:

```text
- Mission
- Input
- Required context
- Engineering Contract
- Rules used
- Skills used
- Tools allowed
- Expected output
- Quality checklist
- Human review point
```

## Default Human Review Policy

Human approval is required for:

- Major architecture decision
- New dependency or stack change
- Database migration
- Production deployment
- Destructive tool operation
- Public publishing
- Security-sensitive change
