# DomainProviderPort

## Purpose

`DomainProviderPort` defines the boundary for reading domain, DNS, SSL, redirect, and ownership verification status.

It lets Native AI Framework show whether a product domain is correctly connected without mutating domain provider configuration.

## Position in Native AI Framework

```text
Product Infrastructure Config
→ InfrastructureIntegrationPort
→ DomainProviderPort
→ Provider Adapter
→ MCP / REST API / SDK
→ Native AI Dashboard Status
→ Review / Execution / Improvement
```

## Responsibilities

- Read configured domains for a product or app.
- Read DNS status metadata.
- Read SSL certificate status.
- Read ownership verification state.
- Read redirect or canonical domain metadata when available.
- Read provider-specific domain warnings.
- Normalize domain status for dashboard display.

## Non-Responsibilities

`DomainProviderPort` must not:

- add domains,
- delete domains,
- transfer domains,
- change DNS records,
- change redirects,
- change SSL settings,
- expose provider secrets,
- replace deployment provider status.

## Input Contract

```yaml
domain_provider_input:
  provider: "vercel | cloudflare | namecheap | porkbun"
  product_id: ""
  app_id: ""
  domain: ""
  environment: "production | preview | staging | development"
  include:
    dns_status: true
    ssl_status: true
    ownership_verification: true
    redirect_metadata: true
  safety:
    read_only: true
    expose_secret_values: false
```

## Output Contract

```yaml
domain_provider_output:
  provider: ""
  product_id: ""
  app_id: ""
  domains:
    - domain: ""
      status: ""
      dns_status: ""
      ssl_status: ""
      ownership_verification: ""
      redirect_metadata: {}
      warnings: []
  source_timestamp: ""
  errors: []
```

## Default Workflow

```text
Receive Domain Status Request
→ Validate Product and Domain Scope
→ Select Domain Provider Adapter
→ Read Domain / DNS / SSL Metadata
→ Normalize Domain Status
→ Report Warnings and Missing Records
→ Return Dashboard Read Model
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
VercelDomainAdapter
CloudflareDomainAdapter
NamecheapDomainAdapter
PorkbunDomainAdapter
```

## Quality Gates

- domain scope is explicit,
- DNS and SSL status are reported separately,
- provider warnings are preserved,
- no DNS mutation is performed,
- no provider secrets are exposed,
- source timestamp is present,
- domain mutations are gated by `ReviewApprovalPort`.

## Dashboard Usage

`DomainProviderPort` should eventually power:

```text
/domains
/infrastructure/domains
/products/[productId]/domains
```

The dashboard should show connected domains, DNS health, SSL health, ownership verification, redirect warnings, and provider-specific domain issues.

## Relationship to Existing Ports

```text
InfrastructureIntegrationPort = selects domain inspection.
DeploymentProviderPort        = may provide deployment-linked domain metadata.
DomainProviderPort            = owns domain and DNS read model.
ReviewApprovalPort            = gates future domain mutations.
```

## Failure Behavior

- If provider access is missing, return `provider_auth_unavailable`.
- If domain is not configured, return `domain_not_configured`.
- If DNS status cannot be read, return `dns_status_unavailable`.
- If SSL status cannot be read, return `ssl_status_unavailable`.
- If a domain mutation is requested, return `mutation_requires_review`.
