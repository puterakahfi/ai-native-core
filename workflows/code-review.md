# Code Review Workflow

## Purpose

Define how generated or human-written code should be reviewed inside the Native AI Framework.

The goal is not only to find bugs, but to protect architecture, maintainability, security, product intent, and long-term system quality.

## Workflow

```text
Review Input
-> Intent Check
-> Contract Check
-> Architecture Review
-> Domain Review
-> API/Data Review
-> UI Review
-> Test Review
-> Security Review
-> Documentation Review
-> Decision
```

## 1. Review Input

Required inputs:

- Feature spec or task
- Engineering Contract
- Relevant rules
- Changed files
- Test results if available

## 2. Intent Check

Ask:

```text
- Does this code solve the requested problem?
- Does it avoid unrelated changes?
- Does it respect non-goals?
```

## 3. Contract Check

Verify:

- Stack compliance
- Architecture style
- Testing requirement
- Security baseline
- Documentation requirement

## 4. Architecture Review

Check:

- Layer boundaries
- Dependency direction
- Separation of concerns
- New module consistency
- ADR requirement

## 5. Domain Review

Check:

- Business rules
- Entities and value objects
- Aggregate boundaries
- Domain event correctness
- Avoidance of anemic or over-engineered models

## 6. API/Data Review

Check:

- Input validation
- Output contract
- Error handling
- Data consistency
- Migration safety
- Backward compatibility

## 7. UI Review

Check:

- shadcn/ui consistency
- Responsive behavior
- Loading/empty/error states
- Accessibility
- Product workflow states

## 8. Test Review

Check:

- Critical paths covered
- Failure paths covered
- Test names describe behavior
- No removed tests without justification

## 9. Security Review

Check:

- No hardcoded secrets
- Authorization and permissions
- Sensitive data handling
- Destructive operations gated
- Tool/API access controlled

## 10. Documentation Review

Check:

- README updates
- ADR updates
- API docs
- Feature docs
- Known limitations

## Decision Options

```text
approved
approved_with_comments
needs_revision
rejected
```

## Output Format

```markdown
# Code Review: <feature-or-pr-name>

## Decision

## Summary

## Intent Alignment

## Contract Compliance

## Architecture Findings

## Domain Findings

## API/Data Findings

## UI Findings

## Test Findings

## Security Findings

## Documentation Findings

## Required Fixes

## Recommendations
```

## Done Criteria

- [ ] Review decision is explicit.
- [ ] Required fixes are separated from recommendations.
- [ ] Contract violations are called out.
- [ ] Security-sensitive issues are not ignored.
- [ ] Documentation gaps are noted.
