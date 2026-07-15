# EnvironmentProviderPort

## Purpose

`EnvironmentProviderPort` defines the boundary for reading environment target metadata and environment variable presence without exposing secret values.

It lets Native AI Framework explain whether production, preview, staging, and development targets are configured enough to support product operations.

## Position in Native AI Framework

```text
Product Infrastructure Config
→ InfrastructureIntegrationPort
→ EnvironmentProviderPort
→ Provider Adapter
→ MCP / REST API / SDK
→ Native AI Dashboard Status
→ Review / Execution / Improvement
```

## Responsibilities

- Read environment targets for a product or app.
- Read environment variable names or keys when allowed.
- Read whether required environment variables are present.
- Read last-updated metadata when available.
- Read branch or deployment target mapping.
- Normalize environment readiness without exposing values.
- Report missing or stale environment metadata.

## Non-Responsibilities

`EnvironmentProviderPort` must not:

- read secret values,
- create environment variables,
- update environment variables,
- delete environment variables,
- promote environments,
- change branch mappings,
- expose provider secrets,
- decide release readiness without review.

## Input Contract

```yaml
environment_provider_input:
  provider: "vercel | github_actions | doppler | infisical | onepassword"
  product_id: ""
  app_id: ""
  environment: "production | preview | staging | development"
  required_keys: []
  include:
    target_metadata: true
    variable_names: true
    variable_presence: true
    last_updated_metadata: true
  safety:
    read_only: true
    expose_secret_values: false
```

## Output Contract

```yaml
environment_provider_output:
  provider: ""
  product_id: ""
  app_id: ""
  environment_targets:
    - name: ""
      branch: ""
      deployment_target: ""
      status: ""
  variables:
    - key: ""
      present: true
      value_exposed: false
      last_updated_at: ""
  missing_required_keys: []
  source_timestamp: ""
  errors: []
```

## Default Workflow

```text
Receive Environment Metadata Request
→ Validate Product and Environment Scope
→ Select Environment Provider Adapter
→ Read Target and Variable Metadata
→ Strip All Secret Values
→ Compare Required Keys
→ Normalize Environment Readiness
→ Return Dashboard Read Model
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
VercelEnvironmentAdapter
GitHubActionsEnvironmentAdapter
DopplerEnvironmentAdapter
InfisicalEnvironmentAdapter
OnePasswordEnvironmentAdapter
```

## Quality Gates

- required environment keys are declared when readiness is evaluated,
- variable values are never returned,
- environment target metadata is scoped,
- missing keys are reported safely,
- source timestamp is present,
- environment mutations are gated by `ReviewApprovalPort`.

## Dashboard Usage

`EnvironmentProviderPort` should eventually power:

```text
/environments
/infrastructure/environments
/products/[productId]/environments
```

The dashboard should show target readiness, required key presence, missing key warnings, branch mappings, and environment metadata freshness without showing secret values.

## Relationship to Existing Ports

```text
InfrastructureIntegrationPort = selects environment metadata inspection.
DeploymentProviderPort        = may use environment target metadata for deployment context.
EnvironmentProviderPort       = owns environment readiness read model.
ReviewApprovalPort            = gates future environment mutations.
```

## Failure Behavior

- If provider access is missing, return `provider_auth_unavailable`.
- If environment target is missing, return `environment_target_not_found`.
- If required keys are missing, return `missing_required_environment_keys`.
- If secret values are requested, return `secret_access_blocked`.
- If an environment mutation is requested, return `mutation_requires_review`.
