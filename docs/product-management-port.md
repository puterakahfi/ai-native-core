# ProductManagementPort

## Purpose

`ProductManagementPort` defines the boundary for discovering, reading, validating, and presenting AI-native product definitions inside Native AI Framework.

It exists so the dashboard and agents can reason about products without coupling to one file format, repository layout, or registry backend.

## Position in the Framework

```text
Product Intent
→ Product Blueprint
→ Product Management
→ Apps / Modules / Tasks / Adapters
→ Execution Workflow
```

`ProductManagementPort` is a core command-center port. It is not a code execution, task execution, deployment, or persistence adapter.

## Primary Responsibilities

- List available products.
- Read product configuration.
- Validate product metadata and blueprint completeness.
- Link products to apps, modules, context packs, adapters, rules, skills, and tasks.
- Expose product status for the dashboard.
- Preserve the product as the highest-level unit of AI-native work.

## Non-Responsibilities

`ProductManagementPort` must not:

- execute code,
- create tasks without a TaskManagementPort workflow,
- mutate product files without approval,
- deploy applications,
- replace product domain decisions with UI state,
- bypass engineering contracts.

## Candidate Adapters

```text
ProductConfigAdapter
GitHubRepositoryProductAdapter
LocalProductRegistryAdapter
DatabaseProductRegistryAdapter
```

## Default Product Management Workflow

```text
Read Product Registry
→ Resolve Product Config
→ Validate Product Metadata
→ Link Apps / Modules / Context
→ Show Dashboard Summary
→ Flag Missing Configuration
```

## Input Contract

```yaml
product_management_input:
  product_id: ""
  registry_source: ""
  include_apps: true
  include_modules: true
  include_adapters: true
```

## Output Contract

```yaml
product_management_output:
  products: []
  validation_results: []
  missing_fields: []
  source_paths: []
```

## Quality Gates

- product identity exists,
- product source path is known,
- app links are resolvable,
- required adapters are resolvable,
- required context pack is resolvable,
- product config does not become runtime state.

## Dashboard Usage

`ProductManagementPort` should power:

```text
/products
/products/[productId]
```

It should make the dashboard capable of showing product identity, app inventory, module map, adapter map, and source-of-truth health.
