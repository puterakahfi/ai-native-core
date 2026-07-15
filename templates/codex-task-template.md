# Codex Task Template

Use this template to give Codex an implementation-ready task inside the Native AI Framework.

## 1. Goal

Describe the exact implementation goal in one or two sentences.

## 2. Product Context

Explain the product, feature, and user problem.

## 3. Existing Stack

Reference the Engineering Contract.

```text
Frontend:
Backend:
Database:
AI provider:
Storage:
Testing:
```

## 4. Files or Modules to Create / Update

List expected files or modules.

```text
create:
update:
do not touch:
```

## 5. Data Model

Describe entities, value objects, tables, fields, and relationships.

## 6. API Behavior

Describe endpoints, inputs, outputs, validation, and error responses.

## 7. UI Behavior

Describe pages, components, states, and user interactions.

Required UI states:

```text
loading
empty
error
success
needs_review
approved
```

## 8. AI Behavior

Describe how AI should be used, what context is required, and where human review happens.

## 9. Business Rules

List business rules and invariants.

## 10. Error Handling

Define how the system handles invalid input, missing data, tool failure, AI failure, and permission failure.

## 11. Tests Required

List required unit, integration, and UI tests.

## 12. Acceptance Criteria

Use checkboxes:

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## 13. Constraints

List rules Codex must follow.

Example:

```text
- Follow Engineering Contract.
- Do not introduce new dependencies without approval.
- Do not change public API without updating docs.
- Do not remove tests.
- Do not hardcode secrets.
```

## 14. What Not To Change

Explicitly list files, modules, APIs, or behaviors that must not be modified.

## 15. Expected Output

Codex should provide:

1. Summary of changes
2. Files changed
3. Tests added/updated
4. How to run checks
5. Risks or follow-up work
