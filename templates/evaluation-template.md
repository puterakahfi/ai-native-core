# Evaluation Template

# Evaluation: <artifact-or-feature-name>

## 1. Evaluation Target

What is being evaluated?

```text
product blueprint | feature spec | generated code | UI design | AI output | workflow | release
```

## 2. Context

Reference the relevant product, feature, contract, rules, and skills.

## 3. Evaluation Criteria

### Product Value

- [ ] Solves the stated user problem
- [ ] Supports success metric
- [ ] Avoids non-goals

### Architecture Compliance

- [ ] Follows Engineering Contract
- [ ] Preserves architecture boundaries
- [ ] Uses approved stack
- [ ] Documents major decisions with ADR

### Rule Compliance

- [ ] Relevant rules are applied
- [ ] No mandatory rule is violated
- [ ] Exceptions are documented

### Skill Execution Quality

- [ ] Correct skill was used
- [ ] Output follows expected format
- [ ] Process was not skipped

### Testability

- [ ] Acceptance criteria are testable
- [ ] Critical paths have test plan
- [ ] Failure paths are covered

### Security

- [ ] No hardcoded secrets
- [ ] Access control considered
- [ ] Sensitive operations require approval
- [ ] Tool usage is safe and auditable

### Maintainability

- [ ] Clear naming
- [ ] Modular structure
- [ ] Low unnecessary coupling
- [ ] Documentation updated

### Human Review

- [ ] Human approval point is defined
- [ ] Public/destructive action is gated
- [ ] Review decision is recorded

## 4. Findings

List issues, risks, and observations.

## 5. Decision

```text
approved
approved_with_comments
needs_revision
rejected
```

## 6. Required Fixes

- 

## 7. Recommendations

- 

## 8. Memory Update

What should be added to decision history, known mistakes, or reusable patterns?
