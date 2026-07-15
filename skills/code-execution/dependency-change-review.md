# Skill: Dependency Change Review

## Purpose

Control dependency changes before installation or execution.

## Procedure

1. Identify the package manifest being updated.
2. List each dependency added, removed, or changed.
3. Explain why the dependency is needed.
4. Check whether the dependency belongs to an app or shared package.
5. Do not install dependencies unless the task explicitly allows it.
6. Return commands for the human reviewer to run.

## Rules

- Dependency changes require approval when the product risk policy says so.
- Prefer package-local dependencies over root dependencies unless the tool is shared across workspace.
- Do not add heavy dependencies without justification.

## Output

Return:

```text
Dependencies Added
Manifest Updated
Reason
Commands To Run
Risks
```
