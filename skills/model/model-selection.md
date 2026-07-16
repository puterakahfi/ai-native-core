# Model Selection Skill Contract

## Purpose

Define the runtime-agnostic contract for selecting a model class for AI-native engineering work.

This contract owns **what must be considered** before choosing a model. It does not name concrete providers such as OpenAI, Anthropic, Gemini, local models, or profile-specific aliases. Those belong in runtime adapters and Hermes profile configuration.

## Building Block

This contract covers the **Model / The Brain** block of AI-native engineering:

- specialized cognitive domains
- context-aware reasoning
- architectural reasoning
- QA and security analysis

## Boundary

Core owns:

- task intent and risk classification requirements
- capability classes required by a task
- quality gates for choosing a model class
- fallback and verification expectations

Adapters own:

- concrete provider/model names
- price and latency data sources
- profile aliases
- local model availability
- runtime-specific routing commands
- eval runner integration

## Required Inputs

- `task_intent` — what work is being requested.
- `task_risk` — low, medium, high, or critical impact if wrong.
- `required_capabilities` — e.g. coding, reasoning, vision, long-context, private/offline, tool-use.
- `context_constraints` — context size, trust level, sensitive data, and source freshness constraints.

## Output Modes

A compliant adapter may produce:

- `model_selection_decision` — selected model class and rationale.
- `model_routing_plan` — route by task phase or subtask.
- `fallback_model_plan` — what to use when preferred model is unavailable or fails.
- `cost_latency_quality_tradeoff` — explicit tradeoff statement.
- `verification_plan` — proof required after model output.
- `escalation_policy` — when to ask a human or use stronger review.

## Model Classes

| Class | Use for | Avoid for |
|---|---|---|
| `fast_general` | simple chat, summarization, low-risk classification | security, architecture, repo edits |
| `reasoning` | root cause, architecture, security, cross-file planning | cheap bulk transforms |
| `coding_agent` | repository edits, TDD, refactors, PR review | tasks without repo/tool context |
| `vision` | screenshots, UI review, diagrams | text-only work |
| `local_private` | sensitive/offline work | tasks requiring stronger unavailable reasoning |

## Quality Gates

- Classify task intent before model choice.
- Make required capabilities explicit.
- Privacy constraints override cost and latency preferences.
- High-risk tasks require reasoning or specialized review.
- Repository-changing coding tasks require a coding-agent or tool-capable model.
- Vision tasks require vision capability.
- Define fallback for unavailable/failing models.
- Record cost/latency/quality tradeoff.
- Match verification depth to task risk.
- Never claim unsupported model capabilities.

## Adapter Expectations

A runtime adapter should map abstract classes to concrete runtime choices. Example: a Hermes adapter may map `reasoning` to a configured provider/model alias, map `coding_agent` to Codex/Claude Code/OpenCode, and map `vision` to a vision-capable Hermes model.

The adapter must fail closed when no model satisfies required risk/capability constraints.
