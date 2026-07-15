# Feature Development Workflow

## Purpose

Define how a product feature moves from idea to implementation-ready task inside the Native AI Framework.

## Workflow

```text
Feature Idea
-> Intent Check
-> Feature Spec
-> Experience Design Check
-> Domain Impact
-> Contract Check
-> Rule Selection
-> Skill Selection
-> Codex Task
-> Implementation
-> Test
-> Review
-> Documentation
-> Memory Update
```

## 1. Feature Idea

Capture the raw feature request.

Output:

- Feature name
- Short description
- User problem

## 2. Intent Check

Validate that the feature supports the product intent.

Questions:

```text
- Which user problem does this solve?
- Which success metric does this support?
- Is this part of MVP or later scale path?
- What is not included?
```

## 3. Feature Spec

Use `skills/product/feature-spec.md`.

Output:

- User flow
- System flow
- Data requirements
- AI role
- Human review point
- Acceptance criteria

## 4. Experience Design Check

Use `workflows/experience-design.md` when the feature changes user flows, screens, navigation, layout, interaction behavior, or UI states.

Output:

- Design brief when user experience direction is unclear
- Wireframe or mockup when layout decisions are needed
- Mockup contract when implementation needs precise UI behavior
- UI verification checklist

Skip this step only when the feature is backend-only, documentation-only, or has no user-facing interaction changes.

## 5. Domain Impact

Use `skills/architecture/domain-modeling.md` if the feature changes core business logic.

Output:

- New entities/value objects if needed
- Updated aggregate boundaries
- New domain events
- Business rules

## 6. Contract Check

Check the Engineering Contract.

Output:

- Approved stack
- Testing requirement
- Security requirement
- Documentation requirement

## 7. Rule Selection

Select applicable rules.

Examples:

```text
rules/architecture/clean-architecture.md
rules/domain/domain-driven-design.md
rules/frontend/shadcn-ui.md
rules/testing/tdd.md
```

## 8. Skill Selection

Select required skills.

Examples:

```text
skills/product/feature-spec.md
skills/architecture/domain-modeling.md
skills/ai/prompt-flow-design.md
skills/review/architecture-review.md
```

## 9. Codex Task

Use `templates/codex-task-template.md` to prepare implementation.

Do not send vague prompts to Codex.

## 10. Implementation

Builder/Codex executes within:

```text
Feature Spec + Engineering Contract + Rules + Skills + Tests
```

## 11. Test

Run or define tests before approval.

## 12. Review

Use architecture review and code review workflow.

## 13. Documentation

Update:

- README if needed
- ADR if decision changed
- API docs if contract changed
- Feature docs if behavior changed

## 14. Memory Update

Record:

- Accepted decisions
- Known mistakes
- Reusable patterns
- Review notes

## Done Criteria

- [ ] Feature supports product intent.
- [ ] Feature spec exists.
- [ ] Experience design was completed or explicitly skipped.
- [ ] Contract checked.
- [ ] Rules selected.
- [ ] Skills selected.
- [ ] Codex task is implementation-ready.
- [ ] Tests are defined or implemented.
- [ ] Review completed.
- [ ] Documentation updated.
