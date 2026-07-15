# ObservabilityProviderPort

## Purpose

`ObservabilityProviderPort` defines the boundary for reading runtime health, incident, error, log, and performance summaries from observability providers.

It gives Native AI Framework a read-only view of whether a product is healthy after deployment.

## Position in Native AI Framework

```text
Product Infrastructure Config
→ InfrastructureIntegrationPort
→ ObservabilityProviderPort
→ Provider Adapter
→ MCP / REST API / SDK
→ Native AI Dashboard Status
→ Review / Execution / Improvement
```

## Responsibilities

- Read product health status.
- Read incident or alert summaries.
- Read error summaries.
- Read performance summaries.
- Read uptime or availability metadata.
- Read safe log summaries.
- Normalize observability provider status for dashboard display.
- Preserve read-only MVP boundaries.

## Non-Responsibilities

`ObservabilityProviderPort` must not:

- create alerts,
- change alert rules,
- delete logs,
- mutate monitors,
- expose PII or secret values,
- replace deployment status inspection,
- approve production readiness without review.

## Input Contract

```yaml
observability_provider_input:
  provider: "sentry | betterstack | datadog | grafana_cloud | vercel"
  product_id: ""
  app_id: ""
  environment: "production | preview | staging | development"
  time_window: "24h"
  include:
    incidents: true
    errors: true
    performance: true
    uptime: true
    logs_summary: true
  safety:
    read_only: true
    expose_secret_values: false
    expose_pii: false
```

## Output Contract

```yaml
observability_provider_output:
  provider: ""
  product_id: ""
  app_id: ""
  environment: ""
  health_status: ""
  incidents: []
  error_summary: ""
  performance_summary: ""
  uptime_summary: ""
  logs_summary: ""
  source_timestamp: ""
  errors: []
```

## Default Workflow

```text
Receive Observability Request
→ Validate Product and Environment Scope
→ Select Observability Adapter
→ Read Health / Incident / Error Metadata
→ Summarize Logs Safely
→ Remove PII and Secret Values
→ Normalize Health Status
→ Return Dashboard Read Model
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
SentryObservabilityAdapter
BetterStackObservabilityAdapter
DatadogObservabilityAdapter
GrafanaCloudObservabilityAdapter
VercelObservabilityAdapter
```

## Quality Gates

- environment scope is explicit,
- read model includes source timestamp,
- log summaries are redacted,
- PII and secret values are not returned,
- incident severity is normalized,
- unknown provider status is reported safely,
- production readiness decisions remain gated by review.

## Dashboard Usage

`ObservabilityProviderPort` should eventually power:

```text
/observability
/infrastructure/observability
/products/[productId]/health
```

The dashboard should show health status, recent incidents, error trends, performance summaries, uptime, and safe log summaries.

## Relationship to Existing Ports

```text
InfrastructureIntegrationPort = selects observability inspection.
DeploymentProviderPort        = explains what was deployed.
ObservabilityProviderPort     = explains how the deployed product is behaving.
ExecutionRunPort              = records inspection runs.
ReviewApprovalPort            = gates production-impacting follow-up actions.
```

## Failure Behavior

- If provider access is missing, return `provider_auth_unavailable`.
- If observability project is missing, return `observability_project_not_found`.
- If logs are unavailable, return `logs_unavailable`.
- If PII or secrets are requested, return `sensitive_data_blocked`.
- If provider status cannot be normalized, return `unknown_observability_status`.
