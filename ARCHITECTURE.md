# Native AI Framework Architecture

## Problem

AI-assisted software development often collapses product thinking, architecture, code generation, testing, and documentation into one unstructured conversation.

This creates inconsistent technical decisions, weak documentation, fragile code, and low trust in AI-generated output.

## Why It Matters

If AI is used to build many products, the development process must be governed by a reusable architecture. The framework must make agent output consistent, reviewable, testable, secure, and maintainable.

## Design Principle

Separate decisions, knowledge, constraints, execution, tools, memory, and evaluation into clear layers.

## Layered Architecture

```text
Intent Layer
-> Blueprint Layer
-> Engineering Contract Layer
-> Knowledge Layer
-> Rules Layer
-> Skills Layer
-> Agent Layer
-> Tool / MCP Layer
-> Memory Layer
-> Loop Layer
-> Evaluation Layer
```

## 1. Intent Layer

Defines why the product or feature exists.

Inputs:

- Product goal
- User problem
- Business constraint
- Success metric
- Non-goals

Outputs:

- Intent document
- Problem statement
- Success metric

## 2. Blueprint Layer

Turns intent into structured product and system design.

Outputs:

- Product blueprint
- Domain model
- Bounded context
- User flow
- Data flow
- API contract
- System diagram
- ADR

## 3. Engineering Contract Layer

Locks technical decisions.

Outputs:

- Architecture style
- Stack decision
- Folder convention
- API convention
- Testing rule
- Security baseline
- Documentation requirement

## 4. Knowledge Layer

Stores explicit source-of-truth knowledge.

Outputs:

- Product knowledge
- Domain knowledge
- Business rules
- Design rules
- Technical references

## 5. Rules Layer

Defines constraints agents must obey.

Examples:

- DDD rules
- Clean Architecture rules
- UI rules
- API rules
- Testing rules
- Security rules
- Code review rules

## 6. Skills Layer

Defines repeatable execution procedures.

Examples:

- Domain modeling skill
- Feature specification skill
- API design skill
- shadcn/ui implementation skill
- Test generation skill
- Architecture review skill

## 7. Agent Layer

Defines specialized roles.

Agents do not own the system. Agents execute assigned responsibilities inside the system.

## 8. Tool / MCP Layer

Defines external capabilities and access policies.

Tools should be registered with:

- Purpose
- Allowed agents
- Allowed actions
- Risk level
- Required approval
- Audit requirement

## 9. Memory Layer

Stores decision history and learning.

Memory should not replace documentation. Memory should point back to source-of-truth artifacts.

## 10. Loop Layer

Defines execution flow.

```text
Plan -> Build -> Test -> Review -> Improve -> Document -> Deploy
```

## 11. Evaluation Layer

Defines quality gates.

Evaluation areas:

- Architecture compliance
- Engineering contract compliance
- Test result
- Security compliance
- Performance
- Maintainability
- User value

## Default Workflow State

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

## Anti-Patterns

Avoid:

- One prompt for everything
- One super-agent for all work
- Code before blueprint
- Agent-selected random stack
- No ADR for major decisions
- No human approval gate
- No evaluation checklist
- Tool access without permission model
