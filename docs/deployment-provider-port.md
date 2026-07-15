# DeploymentProviderPort

## Purpose

`DeploymentProviderPort` defines the boundary for reading deployment provider status for a product or app.

For example, ExampleProduct should be able to show Vercel production and preview deployment status inside Native AI Framework without requiring the user to open Vercel manually.

## Position in Native AI Framework

```text
Product Infrastructure Config
→ InfrastructureIntegrationPort
→ DeploymentProviderPort
→ Provider Adapter
→ MCP / REST API / SDK
→ Native AI Dashboard Status
→ Review / Execution / Improvement
```

`DeploymentProviderPort` is provider-agnostic. Provider-specific adapters such as `VercelDeploymentAdapter` implement its read model.

## Responsibilities

- Read latest deployment status.
- Read production deployment status.
- Read preview deployment status.
- Read build status.
- Read commit SHA and branch metadata.
- Read deployed URL.
- Read deployment creation time.
- Read deployment creator metadata when available.
- Read build or deployment error summaries.
- Read domain status metadata when exposed by the deployment provider.
- Read environment target metadata without exposing secret values.
- Normalize provider-specific deployment states into a common dashboard model.

## Non-Responsibilities

`DeploymentProviderPort` must not:

- trigger deployments,
- rollback deployments,
- delete deployments,
- promote deployments,
- change environment variables,
- change domains,
- mutate provider projects,
- expose secret values,
- replace observability, domain, or environment provider ports.

## MCP vs REST Mode

### MCP Mode

MCP mode is useful for:

- AI-agent inspection,
- log analysis,
- debugging assistance,
- guided infrastructure workflows,
- explaining deployment failures to an operator.

### REST API Mode

REST API mode is useful for:

- predictable dashboard polling,
- status cards,
- scheduled checks,
- stable read models,
- cacheable infrastructure summaries.

Both modes are read-only in the MVP.

## Input Contract

```yaml
deployment_provider_input:
  provider: "vercel | netlify | render | railway | github_actions"
  product_id: ""
  app_id: ""
  provider_project_id: ""
  provider_project_slug: ""
  environment: "production | preview | staging | development"
  branch: ""
  commit_sha: ""
  deployment_id: ""
  integration_mode: "mcp | rest_api | sdk"
  include:
    latest_deployment: true
    production_deployment: true
    preview_deployments: true
    logs_summary: true
    domain_status: true
    environment_target_metadata: true
  safety:
    read_only: true
    expose_secret_values: false
```

## Output Contract

```yaml
deployment_provider_output:
  provider: ""
  product_id: ""
  app_id: ""
  environment: ""
  latest_deployment:
    id: ""
    status: ""
    url: ""
    branch: ""
    commit_sha: ""
    created_at: ""
    creator: ""
  production_deployment: {}
  preview_deployments: []
  build_status: ""
  error_summary: ""
  logs_summary: ""
  domain_status: []
  environment_targets: []
  source_timestamp: ""
  errors: []
```

## Default Workflow

```text
Receive Deployment Status Request
→ Validate Product and Provider Scope
→ Select Deployment Provider Adapter
→ Read Deployment Metadata
→ Read Build / Error Summary
→ Read Domain and Environment Target Metadata if available
→ Strip Secret Values
→ Normalize Deployment Status
→ Return Dashboard Read Model
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
VercelDeploymentAdapter
NetlifyDeploymentAdapter
RenderDeploymentAdapter
RailwayDeploymentAdapter
GitHubActionsDeploymentAdapter
```

## Quality Gates

- provider project scope is explicit,
- read-only credentials are used for MVP,
- deployment status maps to a known canonical state,
- commit and branch metadata are preserved when available,
- environment metadata excludes secret values,
- logs are summarized without leaking sensitive values,
- mutating operations are blocked and routed to `ReviewApprovalPort`.

## Dashboard Usage

`DeploymentProviderPort` should eventually power:

```text
/deployments
/infrastructure/deployments
/products/[productId]/deployments
```

The dashboard should show latest deployment, production status, preview deployments, build health, deployed URL, branch, commit SHA, and actionable error summaries.

## Relationship to Existing Ports

```text
InfrastructureIntegrationPort = selects the provider status boundary.
DeploymentProviderPort        = reads deployment provider state.
DomainProviderPort            = reads domain/DNS state when separated from deployments.
EnvironmentProviderPort       = reads environment target metadata without secrets.
ExecutionRunPort              = records provider inspection runs.
ReviewApprovalPort            = gates future deployment mutations.
```

## Failure Behavior

- If provider access is missing, return `provider_auth_unavailable`.
- If provider project is missing, return `provider_project_not_found`.
- If deployment cannot be found, return `deployment_not_found`.
- If logs are unavailable, return `logs_unavailable`.
- If provider status cannot be normalized, return `unknown_deployment_status`.
- If a mutating action is requested, return `mutation_requires_review`.
