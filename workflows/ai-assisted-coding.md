# AI-Assisted Coding Workflow

## Purpose

Define how to use Codex or other coding agents safely and effectively inside the Native AI Framework.

AI-assisted coding must be contract-driven, not prompt-driven.

## Workflow

```text
Spec
-> Contract Check
-> Context Pack
-> Codex Task
-> Implementation
-> Local Check
-> Test
-> Review
-> Fix Loop
-> Documentation
```

## 1. Spec

Start from an approved feature spec.

Required:

- Feature goal
- User flow
- System flow
- Acceptance criteria
- Non-goals

## 2. Contract Check

Reference the Engineering Contract before coding.

The coding agent must know:

- Architecture style
- Stack
- Folder convention
- Testing rule
- Security baseline
- Documentation requirement

## 3. Context Pack

Prepare only relevant context.

Context pack should include:

```text
- Product intent
- Feature spec
- Engineering Contract
- Relevant rules
- Relevant skills
- Existing files/modules
- What not to change
```

## 4. Codex Task

Use `templates/codex-task-template.md`.

A good Codex task must include:

1. Goal
2. Existing stack
3. Files or modules to create/update
4. Data model
5. API behavior
6. UI behavior
7. Edge cases
8. Error handling
9. Acceptance criteria
10. What not to change

## 5. Implementation

The coding agent implements the smallest complete change.

Rules:

- Do not introduce new dependencies without approval.
- Do not change architecture silently.
- Do not skip validation.
- Do not remove tests to pass checks.
- Do not hardcode secrets.

## 6. Local Check

Run relevant checks where possible:

```text
lint
typecheck
test
build
```

## 7. Test

Tests should cover:

- Happy path
- Failure path
- Business rules
- Security-sensitive behavior
- AI workflow output validation when applicable

## 8. Review

Use:

- Architecture review
- Code review
- Security review when needed

## 9. Fix Loop

If review fails:

```text
needs_revision -> fix -> test -> review
```

## 10. Documentation

Update docs for:

- New API behavior
- New architecture decision
- New workflow
- New rule or skill discovered

## Done Criteria

- [ ] Implementation follows feature spec.
- [ ] Engineering Contract is followed.
- [ ] Relevant rules are applied.
- [ ] Tests exist or test gap is documented.
- [ ] Review is complete.
- [ ] Documentation is updated when needed.
- [ ] No unauthorized stack or dependency change.
