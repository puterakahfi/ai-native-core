# Code Execution Skills

## Purpose

Code execution skills define reusable procedures for AI coding adapters.

These skills are not owned by Codex, Claude Code, Gemini CLI, Cursor, or any single coding tool.

Adapters can declare which skills they support and which skills are required for a task.

## Rule

```text
Skill = reusable procedure
Adapter = replaceable executor
Task Contract = scoped instruction for execution
```

A code adapter must not invent architecture, bypass product config, or ignore review gates.
