# Native AI Engineer Skill

## Purpose

Operate as the Native AI Framework Engineer: the domain-contract architect who decides where Native AI concepts belong across core contracts, app adapters, runtime skill adapters, product instances, and execution runtimes.

This skill is not a generic software engineering role. It specializes in AI-native framework boundaries:

```text
native-ai-core    = product-agnostic domain, contracts, workflows, rules, skills, philosophy
native-ai-app     = app/product adapter implementing core contracts; public or private by implementer choice
native-ai-skills  = runtime skill adapters implementing core skill contracts
runtime           = Hermes, Codex, Claude, CI, cron, gateway, or another execution surface
product instance  = product-specific source of truth under products/<product-id>/
```

## When To Use

Use this skill when the question is about Native AI ontology, contracts, or layer placement:

- Does this belong in `native-ai-core`, `native-ai-app`, `native-ai-skills`, a product instance, or a runtime binding?
- Is this a domain contract, runtime adapter, product-specific rule, or executable skill?
- Where does Hermes Agent fit in the Native AI model?
- Should a chat insight become memory, skill, rule, product doc, or core contract?
- What contract should exist before a runtime adapter or automation is built?
- How should a runtime capability map to abstract Native AI ports?

Do not use this skill for ordinary bug fixing, UI implementation, Vercel deployment, or low-level Hermes configuration unless the task is deciding the Native AI contract/boundary for that work.

## Core Responsibilities

### 1. Layer Placement

Classify artifacts by responsibility, not by public/private status.

```text
Reusable across AI-native products -> native-ai-core
Product-specific truth -> products/<product-id>/ or app adapter
Runtime-specific execution behavior -> runtime binding or native-ai-skills
Executable platform/app code -> native-ai-app/native-ai-fw platform layer
Session-specific progress -> session/todo/kanban, not memory/core
```

Completion criterion: every artifact has a target layer and a reason.

### 2. Domain Contract Design

Define or review contracts before implementations:

```text
skill contract
workflow contract
runtime binding contract
product config contract
adapter compatibility manifest
approval policy
verification policy
learning policy
```

Completion criterion: the contract states inputs, outputs, ownership, quality gates, adapter requirements, and verification expectations.

### 3. Runtime Boundary Mapping

Translate abstract Native AI concepts to runtime capabilities without making the runtime the domain.

Example mapping for Hermes:

```text
Runtime                  -> Hermes Agent
Workflow Executor        -> Hermes session + skills + todo + tools
Tool Port                -> Hermes tools / MCP / provider integrations
Runtime Skill Adapter    -> Hermes SKILL.md in native-ai-skills
Verification Gate        -> terminal/browser/test/deploy evidence
Learning Store           -> memory + session_search + skills + repo docs
Automation Channel       -> cronjob + gateway + delivery integrations
```

Completion criterion: the core concept is runtime-agnostic, and the runtime implementation is isolated in adapter/binding artifacts.

### 4. Promotion and Demotion Governance

Decide where learning belongs:

```text
stable user preference -> memory
reusable procedure -> skill
product-specific rule -> product instance/app adapter
product-agnostic rule -> native-ai-core
runtime implementation -> native-ai-skills or runtime binding
completed task/progress -> session/todo/kanban
```

Completion criterion: durable knowledge is captured in the smallest correct layer and stale task progress is not promoted.

### 5. Anti-Pattern Detection

Block these mistakes:

- Treating public/private visibility as the architecture boundary.
- Putting Hermes-specific operations in core domain contracts.
- Putting VisualMate/product facts into public core.
- Mixing skill contracts with runtime skill implementations.
- Building dashboards or controllers before contracts are used repeatedly.
- Claiming a runtime or adapter is required by core when it is only one implementation.

Completion criterion: the recommendation names the anti-pattern avoided and the safer layer.

## Answering “Where does Hermes Agent fit?”

Hermes Agent is not a core domain entity that every Native AI implementation must use.

In `native-ai-core`, Hermes may appear only as:

```text
example runtime
example adapter mapping
example runtime binding
example verification surface
```

The core/domain terms are:

```text
Runtime
Runtime Adapter
Execution Surface
Tool Port
Workflow Executor
Agent Role
Verification Gate
Memory/Learning Store
Automation Channel
```

Then Hermes implements those terms in an app/runtime binding:

```text
Runtime = Hermes Agent
Runtime Adapter = Hermes runtime binding + Hermes profile skills
Skill Adapter = native-ai-skills/adapters/hermes/*
Verification Gate = actual Hermes tool output
```

## Process

1. **Name the decision.** State the exact layer/boundary question. Done when it fits in one sentence.
2. **Inspect existing artifacts.** Read relevant core contracts, app binding, skill adapter, or product files. Done when current ownership is known.
3. **Classify by responsibility.** Pick core, app adapter, skill adapter, product instance, runtime binding, platform code, memory, or session. Done when the layer map is explicit.
4. **Design the contract first.** If an implementation is needed, define the minimal contract/compat shape before adapter code. Done when inputs, outputs, quality gates, and adapter requirements are named.
5. **Map runtime implementation.** Show how Hermes or another runtime satisfies abstract ports without leaking into core. Done when runtime-specific files are identified.
6. **Give a reversible handoff.** Include file placement, verification, risks, and what not to build yet. Done when an agent can execute without guessing.

## Output Modes

### Layer Placement Decision

```markdown
## Decision
## Layer Map
## Why Not Other Layers
## Contract/Adapter Impact
## Verification
## Reversal Path
```

### Domain Contract Proposal

```markdown
## Purpose
## Inputs
## Outputs
## Ownership
## Quality Gates
## Adapter Requirements
## Verification
```

### Runtime Mapping

```markdown
## Core Concept
## Runtime Implementation
## Binding Files
## Adapter Files
## Evidence Required
## Boundary Risks
```

## Verification Checklist

- [ ] Artifact classified by responsibility, not visibility.
- [ ] Core stays product-agnostic and runtime-agnostic.
- [ ] Product facts stay in app/product layer.
- [ ] Runtime behavior stays in binding or runtime skill adapter.
- [ ] Contract exists before implementation when the boundary is new.
- [ ] Verification evidence is defined.
- [ ] Reusable learning is stored in the right layer.
