# Memory vs Knowledge

## Problem

AI systems often confuse memory with knowledge.

Memory can remember previous interactions or decisions, but it should not replace explicit source-of-truth documentation.

## Why It Matters

If important product and architecture decisions only live in memory, the system becomes fragile.

Agents may forget, misremember, or apply context incorrectly.

## Design Principle

```text
Knowledge is source of truth.
Memory is decision history and retrieval aid.
```

## Knowledge

Knowledge is explicit, reviewable, and version-controlled.

Examples:

```text
- Product intent
- Product blueprint
- Engineering Contract
- ADR
- Domain model
- Business rules
- API contract
- Design system rules
- Security rules
- Workflow documentation
```

Knowledge should live in the repository.

## Memory

Memory stores useful history and patterns.

Examples:

```text
- Previous decisions
- Known mistakes
- Review history
- Reusable patterns
- Product preferences
- Lessons learned
```

Memory should point back to source-of-truth knowledge when possible.

## How Agents Should Use Them

Agents should:

1. Read knowledge first.
2. Use memory to recover prior context.
3. Verify memory against documentation.
4. Update documentation when a decision becomes official.
5. Record important outcomes in memory or decision logs.

## What Belongs in Knowledge

Use repository docs for:

- Accepted architecture decisions
- Product definitions
- Domain rules
- Engineering contracts
- Workflows
- Templates
- Rules
- Skills

## What Belongs in Memory

Use memory for:

- Why a decision was made
- Mistakes to avoid
- Review comments
- User/team preferences
- Reusable patterns discovered during execution

## Anti-Patterns

Avoid:

- Treating chat history as source of truth
- Letting memory override Engineering Contract
- Keeping architecture decisions only in AI memory
- Updating memory but not documentation
- Letting agents rely on vague remembered preferences

## Native AI Framework Rule

When a decision becomes official, it must become documentation.

Suggested locations:

```text
ADR -> docs or product adr directory
Engineering decision -> engineering-contract.yaml
Product decision -> product blueprint
Workflow decision -> workflows directory
Rule decision -> rules directory
Skill decision -> skills directory
```

## ExampleProduct Example

If ExampleProduct decides that every generation must require Identity Lock, that cannot only live in memory.

It must be documented in:

```text
products/example-product/engineering-contract.yaml
products/example-product/product-blueprint.md
products/example-product/rules/identity-lock.md
```
