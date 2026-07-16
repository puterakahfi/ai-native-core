# Profile Bootstrap Skill Contract

## Purpose

Define the runtime-agnostic contract for bootstrapping a reproducible Native AI runtime profile.

This contract says **what must be true** for a generated profile skeleton. Runtime adapters decide **how** to create it for a concrete runtime such as Hermes.

## Boundary

```text
profile-bootstrap contract = runtime-agnostic requirements
Hermes profile bootstrap   = Hermes adapter implementation
profile distribution       = reusable profile shape, not live state
product instance           = product-specific source of truth outside the reusable profile
```

Core owns the contract and safety gates. Runtime adapters own commands, paths, install scripts, and runtime-specific verification.

## When To Use

Use this contract when designing or evaluating:

- a runtime profile generator
- a reusable profile distribution
- minimum skill packs for a runtime profile
- a profile skeleton for AI-native engineering
- adapter requirements for Hermes, Claude Code, Codex, CI, or another execution surface

Do not use this contract to store product-specific facts, credentials, live session state, or runtime-specific command sequences.

## Required Capabilities

A conforming adapter must define:

1. **Runtime target.** Name the concrete runtime the adapter bootstraps.
2. **Profile skeleton.** Define reusable files and directories to create.
3. **Skill preset manifest.** Declare meta-skills, workflows, foundational skills, and preset-specific packs.
4. **Safety exclusions.** Explicitly exclude live runtime state and secrets.
5. **Generation behavior.** Support idempotent creation, dry-run/plan mode, and overwrite protection.
6. **Verification plan.** Verify the generated profile and installed skills with real runtime output.

## Preset Model

Required presets:

- `minimal` — enough to route work and understand Native AI boundaries.
- `engineering` — default coding/product engineering profile.

Optional presets:

- `product` — product/design/CRO surface work.
- `runtime-ops` — canonical runtime host operations.
- `full` — complete workstation profile.

Adapters may add runtime-specific preset names, but they must map back to this core preset model.

## Safety Rules

Reusable profile distributions must not include:

```text
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
auth.json
.env
.env.*
logs/
cache/
secrets/
tokens/
credentials/
```

Product facts belong in product instances or app/runtime bindings, not in the reusable profile skeleton.

## Output Modes

### Contract Handoff

```markdown
## Runtime Target
## Selected Preset
## Profile Skeleton
## Skill Packs
## Safety Exclusions
## Adapter Requirements
## Verification Plan
```

### Adapter Review

```markdown
## Contract Coverage
## Runtime-Specific Behavior
## Missing Gates
## Unsafe Inclusions
## Verification Evidence
## Required Fixes
```

## Quality Gates

- [ ] Runtime target is explicit.
- [ ] Profile skeleton is reproducible.
- [ ] Skill preset manifest is declarative.
- [ ] Meta-skills and core workflows are represented.
- [ ] Runtime boundary skills are represented.
- [ ] Product-specific facts are excluded.
- [ ] Live runtime state and secrets are excluded.
- [ ] Runtime-specific commands live in adapter implementation, not in core.
- [ ] Verification compares installed profile state against the manifest.
