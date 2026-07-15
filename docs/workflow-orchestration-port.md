# WorkflowOrchestrationPort

## Purpose

`WorkflowOrchestrationPort` defines the boundary for triggering, coordinating, monitoring, retrying, and reviewing multi-step workflows inside Native AI Framework.

It exists so deterministic or semi-deterministic automation flows can run through replaceable workflow engines without coupling the framework control plane to n8n, Make, Zapier, GitHub Actions, Temporal, Inngest, Trigger.dev, or a custom queue system.

## Position in the Framework

```text
Intent / Task / Event / Schedule
→ Workflow Plan
→ Workflow Orchestration
→ Step Execution
→ Logs / Results
→ Review / Approval
→ Next Workflow Step
```

`WorkflowOrchestrationPort` sits between planned workflows and execution systems.

It is not an agent runtime, task source, model provider, tool gateway, or approval authority.

## Primary Responsibilities

- Trigger workflows.
- Run scheduled, event-driven, webhook-driven, or manual workflows.
- Coordinate workflow steps.
- Track workflow status.
- Retry failed steps when policy allows it.
- Pause for human approval.
- Capture logs, outputs, and errors.
- Route external tool actions through ToolIntegrationPort when needed.
- Record execution runs through ExecutionRunPort.

## Non-Responsibilities

`WorkflowOrchestrationPort` must not:

- become the source of truth for product architecture,
- replace TaskManagementPort,
- replace AgentRuntimePort for flexible autonomous agent behavior,
- bypass ReviewApprovalPort,
- expose secrets to client-side code,
- publish, delete, or mutate external systems without approval policy,
- hide workflow failures.

## Candidate Adapters

```text
N8nWorkflowAdapter
MakeWorkflowAdapter
ZapierWorkflowAdapter
GitHubActionsWorkflowAdapter
TemporalWorkflowAdapter
InngestWorkflowAdapter
TriggerDevWorkflowAdapter
CustomJobQueueAdapter
```

## Default Workflow Orchestration Flow

```text
Receive Trigger
→ Resolve Workflow Definition
→ Resolve Context / Rules / Skills
→ Start Workflow Run
→ Execute Steps
→ Pause for Approval When Needed
→ Capture Logs and Outputs
→ Store Execution Run Summary
→ Continue / Retry / Fail / Complete
```

## Input Contract

```yaml
workflow_orchestration_input:
  workflow_id: ""
  trigger_type: ""
  canonical_task_id: ""
  context_bundle_ref: ""
  steps: []
  approval_policy: ""
  retry_policy: ""
```

## Output Contract

```yaml
workflow_orchestration_output:
  workflow_run_id: ""
  status: ""
  current_step: ""
  completed_steps: []
  failed_steps: []
  logs: []
  approval_requests: []
  execution_run_ref: ""
```

## Status Flow

```text
queued
→ running
→ waiting_for_approval
→ retrying
→ completed
→ failed
→ cancelled
→ needs_review
```

## Quality Gates

- workflow definition is known,
- trigger source is known,
- context bundle is resolved when required,
- approval policy is explicit,
- retry policy is explicit,
- external actions route through ToolIntegrationPort,
- workflow run is recorded through ExecutionRunPort,
- failure details are visible,
- secrets stay server-side.

## Dashboard Usage

`WorkflowOrchestrationPort` should power:

```text
/workflows
/workflow-runs
/executions
/scheduled automations
/approval-gated workflows
```

It should make the dashboard capable of seeing which workflow ran, what triggered it, which step failed, what needs approval, and what should be retried.

## Control Plane Rule

Native AI Framework remains the control plane.

Workflow engines are execution plane adapters.

A workflow engine may execute a flow, but it must not own product architecture, task source of truth, approval authority, or framework governance.
