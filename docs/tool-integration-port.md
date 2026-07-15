# ToolIntegrationPort

## Purpose

`ToolIntegrationPort` defines the boundary for connecting AI agents, workflows, and framework modules to external tools, applications, APIs, and MCP-compatible tool gateways.

It exists so Native AI Framework can use external capabilities without coupling the core domain to a specific integration vendor, app connector, authentication provider, or workflow automation platform.

## Position in the Framework

```text
Intent
→ Agent Planning
→ Tool Selection
→ Tool Integration
→ External Action / API Call
→ Result Normalization
→ Review / Approval
→ Workflow Continuation
```

`ToolIntegrationPort` sits between agent/workflow planning and external systems.

It is not a task management layer, code execution layer, UI design layer, or creative rendering layer.

## Primary Responsibilities

- Expose external app actions to agents and workflows.
- Route tool requests to the correct external integration.
- Manage least-privilege tool access policies.
- Separate read actions from write/destructive actions.
- Return normalized tool results.
- Return structured errors and execution metadata.
- Preserve auditability and review control.
- Require human approval for destructive, publishing, payment, or outbound communication actions.

## Non-Responsibilities

`ToolIntegrationPort` must not:

- define product architecture,
- create product tasks,
- execute code tasks,
- render creative assets,
- bypass human approval,
- expose secrets to client-side code,
- replace domain ports with vendor-specific logic,
- mutate external systems unless explicitly allowed by policy.

## Subtype Ports

```text
ToolIntegrationPort
├── MCPGatewayPort
├── APIConnectorPort
├── AuthBrokerPort
├── ToolExecutionPort
└── ToolRegistryPort
```

### MCPGatewayPort

Used for exposing MCP-compatible tool servers or gateways to AI agents.

Example adapters:

```text
ComposioToolGatewayAdapter
CustomMCPGatewayAdapter
LocalMCPServerAdapter
```

### APIConnectorPort

Used for direct external API integrations when MCP or a gateway is not required.

Example adapters:

```text
DirectGitHubApiAdapter
DirectMetaApiAdapter
DirectNotionApiAdapter
```

### AuthBrokerPort

Used for managing user authorization, OAuth flows, access scopes, token refresh, and permission boundaries.

Example adapters:

```text
ComposioAuthBrokerAdapter
CustomOAuthBrokerAdapter
```

### ToolExecutionPort

Used for executing approved tool actions through a controlled runtime.

Example adapters:

```text
ComposioToolExecutionAdapter
N8nWorkflowExecutionAdapter
MakeScenarioExecutionAdapter
ZapierActionAdapter
```

### ToolRegistryPort

Used for listing available tools, capabilities, permissions, and action schemas.

Example adapters:

```text
ComposioToolRegistryAdapter
CustomToolRegistryAdapter
```

## Adapter Lifecycle

```text
candidate
→ allowed
→ active
→ deprecated
→ retired
```

- `candidate`: adapter is documented but not yet used as a default workflow component.
- `allowed`: adapter may be used in approved workflows.
- `active`: adapter is the default implementation for a port in a product/app workflow.
- `deprecated`: adapter should be replaced but may still exist for compatibility.
- `retired`: adapter should not be used.

## Default Tool Integration Workflow

```text
Agent Intent
→ Tool Need Detected
→ Tool Policy Check
→ Permission Scope Check
→ Human Approval When Needed
→ Tool Execution
→ Result Normalization
→ Audit Log
→ Agent Response / Workflow Continuation
```

## Approval Gate

Tool integration must keep approval gates for high-impact actions.

Actions that should require explicit approval by default:

- sending emails or messages,
- publishing content,
- deleting records,
- modifying payments or invoices,
- changing production systems,
- updating task/project status to approved or shipped,
- posting to external platforms,
- accessing sensitive user data beyond the approved scope.

Read-only actions may run without approval when product policy allows it.

## Input Contract

A tool integration request should provide:

```yaml
tool_integration_input:
  agent_intent: ""
  tool_request: ""
  user_auth_context: ""
  permission_scope: []
  product: ""
  workflow: ""
  approval_policy: ""
  context: {}
```

## Output Contract

A tool integration adapter should return:

```yaml
tool_integration_output:
  tool_result: {}
  execution_metadata: {}
  audit_log: []
  approval_required: false
  error_details: null
  rate_limit_info: null
```

## Quality Gates

Tool integration outputs should be checked for:

- least-privilege permission use,
- server-side secret handling,
- read/write action separation,
- approval policy compliance,
- structured error handling,
- audit log completeness,
- rate limit awareness,
- user data privacy,
- external system mutation safety.

## Example Adapter Placement

```text
adapters/tool-integration/composio-tool-gateway.adapter.yaml
```

`ComposioToolGatewayAdapter` is a candidate adapter for `ToolIntegrationPort` with subtype `MCPGatewayPort`.

It should be used for controlled AI agent access to authenticated external tools, not dashboard UI design, creative rendering, task management, or code execution.

## Product Opportunities

Potential products and workflows that can use `ToolIntegrationPort`:

```text
AI Personal Workflow Agent
AI Social Media Ops Agent
AI CRM Agent
AI Calendar Assistant
AI GitHub Project Automation Agent
AI Business Operations Agent
```

Recommended flow:

```text
Agent Goal
→ ToolIntegrationPort
→ ComposioToolGatewayAdapter or another tool adapter
→ External App/API
→ Result
→ Human Review When Needed
→ Workflow Continuation
```
