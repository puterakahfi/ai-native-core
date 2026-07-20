# ToolIntegrationPort Migration Record

Status: legacy navigation and migration record

Canonical taxonomy: [`port-taxonomy.md`](port-taxonomy.md)

Canonical inventory: [`port-inventory.yaml`](port-inventory.yaml)

Canonical machine contracts: [`../contracts/ports/`](../contracts/ports/)

## Decision

```text
ToolIntegrationPort
→ RETIRE AS ONE UMBRELLA CONTRACT
```

The former document bundled several independently owned and independently versioned concerns:

```text
tool and schema discovery
protocol or gateway translation
direct API translation
external authentication and token lifecycle
external operation execution
permission and least-privilege enforcement
audit and observability
review and approval routing
```

They do not form one coherent port contract.

No first-class contract or compatibility alias named `tool-integration` is created. Reintroducing that umbrella would collapse provider translation, permission, authority, execution, review, and approval.

## Required separation

```text
external OAuth or provider permission
≠ Native AI Engineering authority
≠ ReviewDisposition
≠ ApprovalStatus
≠ AuthorizationAssessment

registered tool capability
≠ authorized operation
≠ actual execution
≠ successful ExecutionRun
≠ completion
≠ product acceptance
```

A tool or gateway adapter may expose several capabilities, but each declared port reference must preserve one accepted boundary and version line.

## Candidate narrower integration boundaries

The following historical subtype names remain candidates, not accepted first-class contracts:

```text
MCPGatewayPort
APIConnectorPort
AuthBrokerPort
ToolExecutionPort
ToolRegistryPort
```

Their current status is `DEFER` until each has:

```text
a real consumer context;
a coherent request, response, and failure boundary;
accepted authorization and mutation semantics;
replaceable adapter evidence;
a stable compatibility path;
clear ownership relative to ExecutionRun, review, approval, and product policy.
```

General candidate status is recorded in [`port-inventory.yaml`](port-inventory.yaml) and [`port-retention-matrix.md`](port-retention-matrix.md).

## Accepted related boundaries

Current accepted first-class contracts that cover narrower, evidenced concerns include:

```text
contracts/ports/integration/model-inference.port.yaml
contracts/ports/integration/code-operation-execution.port.yaml
contracts/ports/integration/database.port.yaml
contracts/ports/control/agent-runtime.port.yaml
contracts/ports/control/workflow-coordination.port.yaml
contracts/ports/control/execution-run-management.port.yaml
contracts/ports/control/review-management.port.yaml
contracts/ports/control/approval-decision.port.yaml
contracts/ports/control/authorization-assessment.port.yaml
```

These contracts are related; none is a replacement god port for every external tool operation.

## Downstream adapter migration

Legacy runtime or product manifests may still contain declarations such as:

```yaml
adapter:
  port: ToolIntegrationPort
  subtype_port: MCPGatewayPort
```

That declaration is discovery evidence only. It does not prove compatibility with a first-class core port.

A downstream adapter may migrate only after the relevant narrower contract is accepted, using a stable declaration such as:

```yaml
port_adapter_reference:
  adapter_id: example-adapter
  port_id: accepted-port-id
  port_path: contracts/ports/<kind>/<accepted-port-id>.port.yaml
  port_version: ^0.1.0
```

Validate the reference with:

```bash
python3 scripts/validate-port-adapter-reference.py <reference.yaml>
```

A valid ID, path, and version pin proves intended compatibility only. Implementation conformance, runtime behavior, authority, review, approval, completion, and product acceptance require separate evidence.

## Historical adapter examples

Names previously listed here—including Composio, custom MCP servers, direct API adapters, OAuth brokers, n8n, Make, and Zapier—remain downstream candidate examples. They are not default providers, accepted bindings, or proof that a universal tool-integration contract exists.

## Authority rule

This Markdown file is explanatory only.

```text
contracts/ports/**/*.port.yaml
→ machine semantics

docs/port-inventory.yaml
→ discovery classification and migration status

docs/port-retention-matrix.md
→ human-readable decision rationale

this file
→ legacy navigation and migration guidance
```
