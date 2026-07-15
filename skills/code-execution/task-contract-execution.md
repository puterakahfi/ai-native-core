# Skill: Task Contract Execution

## Purpose

Execute implementation work from a scoped task contract instead of a loose prompt.

## Procedure

1. Locate the task contract.
2. Read the task goal, product, app, module, and capability.
3. Follow `scope.in_scope` and `scope.out_of_scope`.
4. Only create or update files allowed by the contract.
5. Respect dependencies and approval requirements.
6. Check acceptance criteria before reporting completion.

## Rules

- Do not expand scope without explicit approval.
- Do not bypass review gates.
- Do not modify product knowledge unless allowed by the contract.
- Do not execute destructive operations.

## Output

Return:

```text
Task Contract Used
Files Created
Files Updated
Acceptance Criteria Check
Risks
Review Notes
```
