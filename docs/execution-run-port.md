# ExecutionRunPort

## Purpose

`ExecutionRunPort` defines the boundary for recording, tracking, and reviewing execution attempts performed by AI adapters, workflows, jobs, and automation systems.

It exists so every AI execution is traceable, reviewable, and connected back to its task, adapter, inputs, outputs, files changed, commands run, and review status.

## Position in the Framework

```text
Task
→ Adapter Handoff
→ Execution Run
→ Output / Summary
→ Review
→ Approval / Revision
```

`ExecutionRunPort` is an execution tracking port. It is not the task source, code executor, or approval authority.

## Primary Responsibilities

- Create execution run records.
- Track run status.
- Link runs to tasks, adapters, PRs, commits, and review gates.
- Store execution summaries.
- Store commands run, files changed, errors, and risks.
- Expose execution history to the dashboard.
- Support auditability and rollback analysis.

## Non-Responsibilities

`ExecutionRunPort` must not:

- execute code itself,
- approve its own output,
- replace TaskManagementPort,
- mutate source-of-truth tasks without approval,
- hide failed execution details,
- store secrets in run logs.

## Candidate Adapters

```text
LocalRunLogAdapter
GitHubCommentRunAdapter
PostgreSQLRunAdapter
FileRunLogAdapter
ObservabilityRunAdapter
```

## Status Flow

```text
queued
→ running
→ completed
→ failed
→ needs_review
→ approved
→ revision_requested
→ archived
```

## Default Execution Run Workflow

```text
Receive Adapter Handoff
→ Create Run Record
→ Start Execution
→ Capture Output
→ Capture Files Changed / Commands Run
→ Store Summary
→ Mark Needs Review
→ Link Approval Decision
```

## Input Contract

```yaml
execution_run_input:
  canonical_task_id: ""
  adapter_name: ""
  workflow: ""
  input_context_refs: []
  approval_policy: ""
```

## Output Contract

```yaml
execution_run_output:
  run_id: ""
  status: ""
  summary: ""
  files_changed: []
  commands_run: []
  errors: []
  risks: []
  review_required: true
```

## Quality Gates

- run is linked to canonical task id,
- adapter name is recorded,
- input context is traceable,
- commands and file changes are captured,
- errors are not hidden,
- secrets are not logged,
- review state is explicit.

## Dashboard Usage

`ExecutionRunPort` should power:

```text
/executions
/task execution history
/adapter run history
/review handoff summary
```

It should help the dashboard answer: what ran, why it ran, what changed, what failed, and what needs review.
