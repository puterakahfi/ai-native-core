# ContextManagementPort

## Purpose

`ContextManagementPort` defines the boundary for resolving, validating, and packaging context that AI agents, adapters, and workflows need to perform work safely and consistently.

It exists so Native AI Framework can separate high-quality task context from ad hoc prompting.

## Position in the Framework

```text
Product / App / Task
→ Context Resolution
→ Context Pack
→ Adapter Handoff
→ Execution
→ Review
```

`ContextManagementPort` is a knowledge and execution-preparation port. It is not a memory substitute, model adapter, or task manager.

## Primary Responsibilities

- List available context packs.
- Resolve context required by a task or workflow.
- Validate required context before adapter handoff.
- Package product, app, rule, skill, adapter, and task context into a reviewable bundle.
- Track missing or stale context.
- Prevent agents from executing with incomplete context.

## Non-Responsibilities

`ContextManagementPort` must not:

- execute code,
- mutate task status,
- infer architecture without source files,
- replace product configs,
- bypass human review,
- store secrets in context packs.

## Candidate Adapters

```text
FileBackedContextPackAdapter
GitHubContextPackAdapter
DatabaseContextPackAdapter
GeneratedContextBundleAdapter
```

## Default Context Workflow

```text
Receive Task / Workflow Reference
→ Resolve Product Context
→ Resolve App Context
→ Resolve Rules / Skills
→ Resolve Adapter Contracts
→ Validate Completeness
→ Build Context Bundle
→ Handoff to Adapter
```

## Input Contract

```yaml
context_management_input:
  product_id: ""
  app_id: ""
  task_id: ""
  required_context: []
  adapter_target: ""
```

## Output Contract

```yaml
context_management_output:
  context_bundle: {}
  source_files: []
  missing_context: []
  warnings: []
  ready_for_handoff: false
```

## Quality Gates

- required product context exists,
- app context exists when app-scoped,
- required rules are resolved,
- required skills are resolved,
- adapter contract is resolved,
- no secrets are included,
- bundle is reviewable before execution.

## Dashboard Usage

`ContextManagementPort` should power:

```text
/context-packs
/task context readiness
/adapter handoff preview
```

It should help the dashboard show whether a task is safe to send to Codex or another execution adapter.
