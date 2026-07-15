# Architecture Review Skill

## Purpose

Help reviewer agents evaluate whether a proposed design or implementation follows the Native AI Framework, Engineering Contract, and relevant rules.

## When To Use

Use this skill when reviewing:

- New product blueprint
- New module architecture
- Feature specification
- Pull request
- Generated code
- Database design
- AI workflow
- Tool/MCP integration

## Required Input

```text
- Product intent
- Blueprint or feature spec
- Engineering Contract
- Relevant rules
- Proposed implementation or design
- Known constraints
```

## Process

### 1. Check Intent Alignment

Ask:

```text
- Does this design solve the stated user problem?
- Does it support the product goal?
- Does it avoid non-goals?
```

### 2. Check Engineering Contract Compliance

Verify stack, architecture style, testing, security, and documentation requirements.

### 3. Check Architecture Boundaries

Verify separation of concerns:

```text
Domain
Application
Infrastructure
Interface
```

### 4. Check Domain Modeling

Review entities, value objects, aggregates, repositories, and business rules.

### 5. Check API and Data Flow

Verify API behavior, validation, error handling, and data lifecycle.

### 6. Check AI Workflow

Review:

```text
Input -> Context -> Prompt Flow -> Tool Use -> Output -> Evaluation -> Human Review
```

### 7. Check Security and Tool Risk

Review secrets, authorization, destructive actions, and tool permissions.

### 8. Check Testability

Verify that critical logic can be tested and acceptance criteria are clear.

### 9. Check Maintainability

Review naming, modularity, dependencies, documentation, and future extension path.

### 10. Produce Review Decision

Decision options:

```text
approved
approved_with_comments
needs_revision
rejected
```

## Output Format

```markdown
# Architecture Review: <subject>

## Decision

## Summary

## Contract Compliance

## Boundary Review

## Domain Review

## API / Data Flow Review

## AI Workflow Review

## Security Review

## Testability Review

## Maintainability Review

## Required Fixes

## Recommendations

## Final Checklist
```

## Quality Checklist

- [ ] Review references the Engineering Contract.
- [ ] Review checks architecture boundaries.
- [ ] Review checks domain correctness.
- [ ] Review checks AI workflow boundaries.
- [ ] Review checks security and tool risk.
- [ ] Review checks testability.
- [ ] Review gives a clear decision.

## Failure Handling

If the submitted artifact lacks enough context, mark it as `needs_revision` and list the missing context.

Do not approve architecture by vibes.
