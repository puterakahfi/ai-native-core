# AI Coding Adapter

## Problem

A framework should not depend on one coding assistant or one vendor-specific coding tool.

A coding tool is only an executor. It should not define the architecture, methodology, contract, rules, skills, or product lifecycle.

## Design Principle

```text
Framework core = stable
Coding adapter = replaceable
```

## Correct Mental Model

```text
Native AI Framework
-> Intent
-> Blueprint
-> Engineering Contract
-> Rules
-> Skills
-> Implementation Task
-> Review
-> Evaluation

AI Coding Adapter
-> Executes the implementation task
```

## Adapter Examples

Examples of coding adapters:

```text
Codex
Claude Code
Gemini CLI
Cursor agent
Copilot coding agent
Custom internal coding agent
```

These tools can be used, replaced, compared, or combined.

## What The Adapter May Do

An adapter may:

- Read the prepared context pack
- Implement a scoped task
- Modify files within allowed boundaries
- Add or update tests
- Report changed files
- Report risks and follow-up work

## What The Adapter Must Not Own

An adapter must not own:

- Product intent
- Architecture decision
- Engineering Contract
- Domain model
- Business rules
- Approval decision
- Deployment decision
- Public publishing decision

## Stable Contract

The stable contract is the implementation task.

Use:

```text
templates/implementation-task-template.md
```

Older tool-specific task templates should be treated as adapter-specific variants, not framework core.

## Review Rule

Adapter output is never automatically accepted.

It must pass:

```text
Architecture Review
Code Review
Test Review
Security Review when needed
Documentation Review
```

## ExampleProduct Example

For ExampleProduct, a coding adapter may implement Brand Identity Manager after receiving:

```text
Product intent
Feature spec
Domain model
Engineering Contract
Identity Lock rule
Brand consistency rule
Human approval rule
Implementation task
```

But the adapter must not decide that Identity Lock is optional, because that is a product and architecture rule.
