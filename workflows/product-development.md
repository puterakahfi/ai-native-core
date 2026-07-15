# Product Development Workflow

## Purpose

This workflow defines how to move from product idea to evaluated AI-native product output.

## Workflow

```text
Idea
-> Intent
-> Blueprint
-> Experience Design
-> Engineering Contract
-> Knowledge Preparation
-> Rule Selection
-> Skill Selection
-> Agent Planning
-> Execution
-> Test
-> Review
-> Documentation
-> Release
-> Evaluation
-> Memory Update
```

## 1. Idea

Capture raw idea without over-designing.

Output:

- Idea note
- Initial problem hypothesis

## 2. Intent

Clarify why the product or feature exists.

Output:

- Product goal
- User problem
- Business constraint
- Success metric
- Non-goals

## 3. Blueprint

Turn intent into a structured product and system design.

Output:

- Product blueprint
- User flow
- Domain model
- Data flow
- AI flow
- Human review points

## 4. Experience Design

Turn the product blueprint into user flows, information architecture, wireframes, mockups, and interaction contracts before broad implementation.

Use `workflows/experience-design.md` when the product or feature requires UI, UX, screen, navigation, or interaction decisions.

Output:

- Design brief
- User flow
- Information architecture
- Wireframe or mockup
- Interaction contract
- UI verification checklist

## 5. Engineering Contract

Lock technical decisions before implementation.

Output:

- Stack decision
- Architecture rule
- Testing strategy
- Security baseline
- Documentation requirement

## 6. Knowledge Preparation

Collect and structure required context.

Output:

- Product knowledge
- Domain knowledge
- Business rules
- Technical references

## 7. Rule Selection

Choose rules that must be enforced.

Output:

- Rule list
- Review checklist

## 8. Skill Selection

Choose skills needed for execution.

Output:

- Skill list
- Expected output format

## 9. Agent Planning

Assign work to agent roles.

Output:

- Agent plan
- Task breakdown
- Tool permissions

## 10. Execution

Agents execute within contract, rules, skills, and tool boundaries.

Output:

- Generated artifact
- Implementation plan
- Code changes when applicable

## 11. Test

Validate behavior and acceptance criteria.

Output:

- Test result
- Coverage notes
- Failed cases

## 12. Review

Review output against quality gates.

Output:

- Review report
- Required fixes
- Approval/rejection recommendation

## 13. Documentation

Update source-of-truth documentation.

Output:

- README update
- ADR update
- Feature docs
- API docs

## 14. Release

Prepare release with human approval.

Output:

- Release checklist
- Changelog
- Deployment notes

## 15. Evaluation

Measure quality and user value.

Output:

- Evaluation report
- Improvement opportunities

## 16. Memory Update

Record accepted decisions and known mistakes.

Output:

- Decision log
- Reusable pattern
- Known issue

## Default Status System

```text
idea
-> drafted
-> specified
-> contracted
-> planned
-> generated
-> needs_review
-> approved
-> implemented
-> tested
-> shipped
-> analyzed
-> improved
```
