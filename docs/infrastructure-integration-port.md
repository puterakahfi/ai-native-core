# InfrastructureIntegrationPort

## Purpose

`InfrastructureIntegrationPort` defines the control-plane boundary for connecting a Native AI product to its infrastructure and ecosystem providers.

It lets the framework inspect deployment, observability, domain, and environment status without requiring operators to open each provider dashboard manually.

## Position in Native AI Framework

```text
Product
→ Product Infrastructure Config
→ InfrastructureIntegrationPort
→ DeploymentProviderPort / ObservabilityProviderPort / DomainProviderPort / EnvironmentProviderPort
→ Provider Adapter
→ MCP / REST API / SDK
→ Native AI Dashboard Status
→ Review / Execution / Improvement
```

`InfrastructureIntegrationPort` sits after product configuration and before provider-specific inspection. It does not replace provider ports; it selects and coordinates them.

## Responsibilities

- Read product infrastructure configuration.
- Resolve the provider, project, environment, branch, and domain identifiers needed for status inspection.
- Select the correct provider-specific port.
- Normalize provider responses into dashboard-safe infrastructure status.
- Preserve read-only MVP boundaries.
- Prevent secret values from being exposed in dashboard read models.
- Route future mutating actions through `ReviewApprovalPort`.
- Report unavailable provider access, missing config, or unsupported status requests.

## Non-Responsibilities

`InfrastructureIntegrationPort` must not:

- trigger deployments,
- rollback deployments,
- delete deployments,
- change environment variables,
- change domains,
- mutate provider projects,
- store provider secrets,
- expose secret values,
- bypass human approval,
- replace provider-specific ports.

## Input Contract

```yaml
infrastructure_integration_input:
  product_id: ""
  app_id: ""
  environment: "production | preview | staging | development"
  provider: "vercel | netlify | render | cloudflare | sentry | ..."
  provider_project_id: ""
  provider_project_slug: ""
  branch: ""
  commit_sha: ""
  requested_status:
    deployments: true
    observability: false
    domains: true
    environments: true
  integration_mode: "mcp | rest_api | sdk | manual"
  safety:
    read_only: true
    expose_secret_values: false
    require_review_for_mutations: true
```

## Output Contract

```yaml
infrastructure_integration_output:
  product_id: ""
  app_id: ""
  provider: ""
  environment: ""
  read_only: true
  status_cards: []
  latest_deployment: {}
  preview_deployments: []
  observability_summary: {}
  domain_status: []
  environment_targets: []
  logs_summary: {}
  source_timestamp: ""
  unsupported_operations: []
  approval_required_for_actions: []
  errors: []
```

## Default Workflow

```text
Read Product Infrastructure Config
→ Validate Provider and Environment Scope
→ Select Provider Port
→ Select Provider Adapter
→ Inspect Status through MCP / REST API / SDK
→ Normalize Provider Metadata
→ Strip Secret Values
→ Publish Read-only Dashboard Status
→ Link Findings to Review / Execution / Improvement
```

Future mutating actions must follow:

```text
ReviewApprovalPort
→ Human approval
→ InfrastructureIntegrationPort
→ Provider adapter action
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
VercelDeploymentAdapter
NetlifyDeploymentAdapter
RenderDeploymentAdapter
RailwayDeploymentAdapter
GitHubActionsDeploymentAdapter
SentryObservabilityAdapter
BetterStackObservabilityAdapter
DatadogObservabilityAdapter
CloudflareDomainAdapter
VercelDomainAdapter
DopplerEnvironmentAdapter
InfisicalEnvironmentAdapter
```

## Quality Gates

- product infrastructure config exists,
- provider and environment scope are explicit,
- provider credentials are read-only for MVP,
- secret values are never returned,
- dashboard status includes source timestamp,
- unsupported provider operations are reported,
- mutating actions are blocked unless approved through `ReviewApprovalPort`.

## Dashboard Usage

`InfrastructureIntegrationPort` should eventually power:

```text
/infrastructure
/products/[productId]/infrastructure
/products/[productId]/deployments
```

The dashboard should show product infrastructure health, latest deployment status, preview deployment state, domain status, environment target metadata, and provider errors.

## Relationship to Existing Ports

```text
ProductManagementPort           = discovers product identity and configuration.
InfrastructureIntegrationPort   = resolves infrastructure provider status.
DeploymentProviderPort          = inspects deployment provider state.
ObservabilityProviderPort       = inspects runtime health and incidents.
DomainProviderPort              = inspects domain and DNS state.
EnvironmentProviderPort         = inspects environment target metadata without secrets.
ExecutionRunPort                = records infrastructure inspection runs.
ReviewApprovalPort              = gates future mutating infrastructure actions.
```

## Failure Behavior

- If product infrastructure config is missing, return `missing_infrastructure_config`.
- If provider access is unavailable, return `provider_auth_unavailable`.
- If provider project is missing, return `provider_project_not_found`.
- If provider status cannot be read, return `status_unavailable`.
- If secret values are requested, return `secret_access_blocked`.
- If a mutating operation is requested without approval, return `mutation_requires_review`.
