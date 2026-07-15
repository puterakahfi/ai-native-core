# AgentRuntimePort

## Purpose

`AgentRuntimePort` defines the boundary for running, inspecting, pausing, resuming, and governing AI agent runtimes inside Native AI Framework.

It exists so agents can be executed through different runtimes without coupling the framework control plane to a specific agent framework, local assistant, hosted agent platform, or orchestration library.

## Position in the Framework

```text
Intent / Task / Workflow
→ Agent Plan
→ Agent Runtime
→ Tool / Model / Skill Usage
→ Execution Run
→ Review / Approval
```

`AgentRuntimePort` sits between agent planning and actual agent execution.

It is not a task source, workflow engine, model provider, tool gateway, or approval authority.

## Primary Responsibilities

- Start an agent run.
- Pause, resume, or stop an agent run.
- Inspect agent state and reasoning-safe summaries.
- Enforce allowed tools, skills, rules, and permission policies.
- Route tool usage through ToolIntegrationPort when external actions are needed.
- Record run metadata through ExecutionRunPort.
- Request review through ReviewApprovalPort when required.
- Keep agent runtime replaceable.

## Non-Responsibilities

`AgentRuntimePort` must not:

- create or mutate source-of-truth tasks by itself,
- bypass approval gates,
- expose secrets to agents or client-side code,
- replace WorkflowOrchestrationPort for deterministic scheduled workflows,
- replace ToolIntegrationPort for external app access,
- replace ModelInferencePort for model calls,
- replace domain/product architecture decisions.

## Candidate Adapters

```text
OpenClawAgentRuntimeAdapter
LangGraphAgentRuntimeAdapter
CrewAIAgentRuntimeAdapter
AutoGenAgentRuntimeAdapter
CustomAgentRuntimeAdapter
OpenAIAgentRuntimeAdapter
```

## Default Agent Runtime Workflow

```text
Receive Agent Execution Request
→ Resolve Context Bundle
→ Resolve Rules / Skills
→ Check Tool Permissions
→ Start Agent Run
→ Capture Agent Actions
→ Route External Tool Requests
→ Pause for Approval When Needed
→ Store Execution Run Summary
→ Handoff to Review
```

## Input Contract

```yaml
agent_runtime_input:
  agent_id: ""
  canonical_task_id: ""
  workflow_id: ""
  context_bundle_ref: ""
  allowed_tools: []
  required_skills: []
  applicable_rules: []
  approval_policy: ""
```

## Output Contract

```yaml
agent_runtime_output:
  agent_run_id: ""
  status: ""
  summary: ""
  actions_taken: []
  tool_requests: []
  approval_requests: []
  errors: []
  execution_run_ref: ""
```

## Status Flow

```text
queued
→ running
→ waiting_for_tool
→ waiting_for_approval
→ completed
→ failed
→ stopped
→ needs_review
```

## Quality Gates

- context bundle is resolved,
- applicable rules are loaded,
- required skills are available,
- allowed tools are explicit,
- external actions route through ToolIntegrationPort,
- high-impact actions require ReviewApprovalPort,
- execution summary is recorded,
- secrets are never exposed to agent-visible output.

## Dashboard Usage

`AgentRuntimePort` should power:

```text
/agents
/agent-runs
/executions
/task agent handoff
```

It should make the dashboard capable of seeing which agent runtime handled work, what actions were attempted, where approval was needed, and what output is ready for review.

## Control Plane Rule

Native AI Framework remains the control plane.

Agent runtimes are execution plane adapters.

An agent runtime may execute a plan, but it must not own product architecture, task source of truth, approval authority, or framework governance.
