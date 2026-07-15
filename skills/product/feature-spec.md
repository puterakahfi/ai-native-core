# Feature Specification Skill

## Purpose

Help agents convert a product idea or request into a clear, reviewable, implementation-ready feature specification.

## When To Use

Use this skill before implementation when:

- A new feature is requested
- A feature is too vague
- Codex or builder agent needs implementation context
- A product workflow needs to be made repeatable

## Required Input

```text
- Product intent
- User problem
- Desired outcome
- Business constraints
- Existing blueprint
- Engineering Contract
- Relevant rules
```

## Process

### 1. Define Feature Goal

Write one clear sentence describing the feature outcome.

### 2. Define User Problem

Explain the specific problem this feature solves.

### 3. Define User Flow

Describe the user journey.

```text
Entry -> Action -> System Response -> Review -> Completion
```

### 4. Define System Flow

Describe backend, frontend, AI, storage, and tool interactions.

### 5. Define Data Requirements

List required data and state changes.

### 6. Define AI Role

Clarify exactly where AI assists.

Do not make AI responsible for decisions that require human approval.

### 7. Define Human Review Point

Identify where a human must review, approve, reject, or edit output.

### 8. Define Acceptance Criteria

Use clear, testable criteria.

### 9. Define Non-Goals

State what is intentionally excluded from this version.

### 10. Define Risks and Edge Cases

Include failures, invalid input, permission issues, and model output issues.

## Output Format

```markdown
# Feature Spec: <feature-name>

## 1. Feature Goal

## 2. Problem

## 3. Why It Matters

## 4. User Flow

## 5. System Flow

## 6. Data Requirements

## 7. AI Role

## 8. Human Review

## 9. API / Interface Requirements

## 10. UI Requirements

## 11. Workflow States

## 12. Acceptance Criteria

## 13. Non-Goals

## 14. Risks and Edge Cases

## 15. Required Rules

## 16. Required Skills

## 17. Codex Implementation Prompt
```

## Quality Checklist

- [ ] Feature goal is clear.
- [ ] User flow is understandable.
- [ ] System flow is implementation-ready.
- [ ] AI role is bounded.
- [ ] Human approval point is defined.
- [ ] Acceptance criteria are testable.
- [ ] Non-goals prevent scope creep.
- [ ] Required rules and skills are listed.

## Failure Handling

If the feature is too broad, reduce it to the smallest useful MVP.

If the required product context is missing, list missing context before implementation.
