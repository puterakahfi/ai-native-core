# AGENTS.md — Project-Level Agent Context

## What It Is

AGENTS.md is the foundational artifact of Agent-Driven Development. It gives AI agents persistent, project-specific context that survives across sessions, tools, and team members.

Different runtimes use different file names:

| Runtime | File | Location |
|---|---|---|
| OpenAI Codex | `AGENTS.md` | Repo root |
| Anthropic Claude Code | `CLAUDE.md` | Repo root or `.claude/` |
| Cursor AI | `.cursorrules` | Repo root |
| Cursor AI (scoped) | `.cursor/rules/*.mdc` | Per-concern rules |
| Hermes Agent | `AGENTS.md` | Repo root (auto-loaded) |
| General | `AGENTS.md` | Repo root |

The format varies but the purpose is identical: **tell the agent how this project works**.

## Why It Matters

Without AGENTS.md:
- Agents guess at conventions → inconsistent code style
- Agents don't know build commands → can't verify their own work
- Agents don't know architecture constraints → violate boundaries
- Every session starts from zero → no accumulated project knowledge
- Team members give conflicting instructions → agent follows the last one

With AGENTS.md:
- One source of truth for agent behavior
- Version-controlled → team-shared, reviewable, auditable
- Agent can self-verify → run tests, lint, build before claiming done
- Architecture constraints are explicit → agents respect boundaries

## Required Sections

Per the `agents-md.contract.yaml`, every AGENTS.md must include:

### 1. Project Identity
What this project is, in one paragraph.

```markdown
## Project
Facility Scheduler — a Laravel/PHP application for managing sports facility bookings.
PHP 8.2, Laravel 11, PostgreSQL, Tailwind CSS, Livewire.
```

### 2. Build & Test Commands
Exact, copy-pasteable commands. Not descriptions — commands.

```markdown
## Commands
- Test: `php artisan test`
- Lint: `./vendor/bin/pint --test`
- Build: `npm run build`
- Dev: `php artisan serve & npm run dev`
```

### 3. Code Style
Specific conventions with examples.

```markdown
## Code Style
- Controllers: single-action invokable (`__invoke`)
- Models: no business logic, use Action classes
- Naming: `CreateBookingAction`, not `BookingCreator`
- Imports: grouped (PHP, Laravel, App), alphabetical within groups
```

### 4. Architecture Constraints
Structural decisions the agent must respect.

```markdown
## Architecture
- Hexagonal: domain logic in `app/Domain/`, no framework imports
- Actions pattern: one public method per action class
- No Eloquent in domain layer — use repository interfaces
- See ADR-003 for the event sourcing decision
```

### 5. Do Not (Prohibitions)
At least 3 enforceable items. Not aspirational — enforceable.

```markdown
## Do Not
- Never commit .env or any file containing secrets
- Never add dependencies without checking existing ones first
- Never modify database migrations after they've been deployed
- Never use `any` as a TypeScript type
- Never refactor code outside the scope of the current task
```

## Authoring Principles

1. **Concise > Comprehensive** — Agents ignore bloated files. Keep under 500 lines.
2. **Specific > General** — Every rule must be enforceable, not aspirational.
3. **Commands > Descriptions** — Give exact commands, not "run the tests."
4. **Examples > Prose** — Show the right pattern, don't describe it.
5. **Version-controlled** — Check into git. Review changes in PRs.
6. **Single source** — Don't duplicate rules across CLAUDE.md and .cursorrules.

## Relationship to Other Contracts

```text
AGENTS.md (project context)
  ├── references → Engineering Contract (architecture decisions)
  ├── references → Rules (enforceable constraints)
  ├── consumed by → Skills (procedural knowledge)
  └── consumed by → Workflows (sequenced processes)
```

AGENTS.md is the **entry point**. It tells agents where to find everything else. It does NOT contain everything — it points to contracts, rules, and docs.

## Validation

An AGENTS.md is valid when:
- All required sections are present
- Build/test commands are runnable
- Do-not section has ≥ 3 enforceable items
- No vague instructions ("follow best practices")
- No duplicated rules across files
- Under 500 lines

## Contract Reference

See `contracts/runtime/agents-md.contract.yaml` for the formal specification.
