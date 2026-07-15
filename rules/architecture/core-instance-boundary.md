# Core Instance Boundary Rule

## Purpose

Keep the Native AI Framework reusable by separating product-agnostic core contracts from product-specific instance configuration.

## Applies To

- Framework contracts
- Domain models
- Product instances
- Runtime bindings
- Rules and skills
- Workflows and templates
- Ports and adapters
- Platform SDK fixtures and generated views

## Layer Contract

```text
Native AI Framework Core
  owns product-agnostic methodology, contracts, ports, rules, skills, workflows, templates, evaluation, and adapter taxonomy.

Product Instance
  owns product-specific intent, blueprint, domain model, engineering contract, feature map, rule overrides, skills, workflows, adapter choices, and deployment targets.

Runtime Binding
  owns how a runtime such as Hermes Agent executes a product instance through tools, profiles, skills, memory, cron, gateway, MCP, and approvals.
```

## Must Do

1. Put reusable framework concepts in core artifacts.
2. Put product-specific facts under `products/<product-id>/`.
3. Put runtime-specific execution details in binding or adapter files.
4. Generalize before promoting a product-specific rule, skill, workflow, or adapter into core.
5. Keep product instances isolated from each other.
6. Keep runtime tools replaceable through ports and adapters.
7. Make product instance source-of-truth references explicit in `project.config.yaml`.
8. Make runtime assumptions explicit in `runtime.binding.yaml`.

## Must Not Do

1. Do not make ExampleProduct-specific behavior part of the core framework.
2. Do not make Hermes Agent the framework core; Hermes is a runtime adapter.
3. Do not put product deployment targets, brand rules, UI preferences, or credentials in core artifacts.
4. Do not let a runtime binding override the Engineering Contract.
5. Do not let platform SDK fixtures become hidden source-of-truth for product domain decisions.
6. Do not couple core workflows to one model provider, coding assistant, UI framework, or deployment provider.

## Promotion Rule

A product-specific artifact may be promoted to core only when all are true:

- It is useful for more than one product instance.
- Product names, domains, credentials, URLs, and deployment targets have been removed.
- It is expressed as a product-agnostic contract, rule, skill, workflow, template, or adapter.
- Review confirms it does not weaken existing core boundaries.

## Review Checklist

- [ ] Is this artifact core, product instance, or runtime binding?
- [ ] Does the file path match that layer?
- [ ] Are product-specific facts isolated under `products/<product-id>/`?
- [ ] Are runtime-specific facts isolated in binding/adapter files?
- [ ] Does the change preserve replaceability of tools and providers?
- [ ] Does the Engineering Contract remain the product authority?
- [ ] Does the change need ADR or approval under the risk policy?

## ExampleProduct Example

Correct:

```text
products/example-product/deployment.md
products/example-product/engineering-contract-v0.2.yaml
products/example-product/runtime.binding.yaml
```

Incorrect:

```text
rules/architecture/example-product-beta-domain.md
workflows/deploy-to-beta-example-product.md
skills/example-product-only-dashboard-rule.md
```

The incorrect examples should remain under `products/example-product/` unless generalized.
