# Implementation Task Template

Use this template to prepare an implementation-ready task for any coding tool or engineering agent.

The Native AI Framework should not depend on one coding tool. The implementation task is the stable contract. The tool that executes it can be replaced.

## 1. Goal

Describe the exact implementation goal.

## 2. Product Context

Explain the product, feature, and user problem.

## 3. Engineering Contract

Reference the approved stack, architecture, testing, security, and documentation rules.

## 4. Files or Modules

List files or modules to create, update, or preserve.

```text
create:
update:
preserve:
```

## 5. Data Model

Describe entities, value objects, tables, fields, and relationships.

## 6. API Behavior

Describe endpoints, inputs, outputs, validation, and error responses.

## 7. UI Behavior

Describe pages, components, states, and interactions.

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

Describe how AI is used, required context, output contract, and human review point.

## 9. Business Rules

List business rules and invariants.

## 10. Error Handling

Describe invalid input, missing data, tool failure, model failure, and permission failure behavior.

## 11. Tests Required

List required unit, integration, and UI tests.

## 12. Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## 13. Constraints

Example constraints:

```text
- Follow Engineering Contract.
- Do not introduce new dependencies without approval.
- Do not change public API without updating docs.
- Do not remove tests.
- Do not hardcode secrets.
```

## 14. Expected Output

The executor should provide:

1. Summary of changes
2. Files changed
3. Tests added or updated
4. How to run checks
5. Risks or follow-up work
