# Test-Driven Development Rule

## Purpose

Ensure AI-generated implementation remains verifiable, maintainable, and safe to change.

## Applies To

- Backend features
- Frontend logic
- Domain logic
- API behavior
- AI workflow orchestration
- Critical product flows

## Must Do

1. Define acceptance criteria before implementation.
2. Write or update tests for critical behavior.
3. Prefer testing domain and application logic before infrastructure details.
4. Include failure cases, not only happy paths.
5. Keep tests readable as product behavior documentation.
6. Run relevant tests before marking work as done.
7. Document untested areas and why they are not covered yet.

## Must Not Do

1. Do not remove tests just to make a build pass.
2. Do not mark generated code as complete without test strategy.
3. Do not rely only on manual testing for critical logic.
4. Do not mock everything until the test becomes meaningless.
5. Do not ignore flaky tests without documenting cause.

## Test Priority

Prioritize:

```text
1. Domain rules
2. Application use cases
3. API contracts
4. Security-sensitive flows
5. AI output evaluation logic
6. Integration boundaries
7. UI interaction states
```

## Review Checklist

- [ ] Acceptance criteria are defined.
- [ ] Critical paths have tests.
- [ ] Failure paths have tests.
- [ ] Domain/application logic can be tested without real infrastructure.
- [ ] Test names describe behavior clearly.
- [ ] Untested areas are documented.
- [ ] Tests were considered before approval.

## ExampleProduct Example

For ExampleProduct, tests should cover:

```text
- Identity Lock validation
- Brand consistency rule application
- Campaign brief generation boundaries
- Creative review checklist scoring
- Approval gate before export/publish
- Asset state transition rules
```
