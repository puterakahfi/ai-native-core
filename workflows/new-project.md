# Workflow: New Project

## Purpose

Create a new AI-native product project inside the Native AI Framework.

This workflow creates the product context, domain model, contracts, ports, adapters, context pack, and initial review gates before implementation starts.

## Input

```text
project_name
product_category
target_user
user_problem
business_goal
main_workflow
constraints
preferred_stack
initial_adapters
success_metric
```

## Process

```text
1. Capture intent
2. Discover domain
3. Create product blueprint
4. Create domain model
5. Create engineering contract
6. Define port map
7. Define adapter map
8. Create project configuration
9. Create context pack
10. Create initial ADR
11. Run architecture review
```

## Output Files

```text
products/{project}/README.md
products/{project}/intent.md
products/{project}/product-blueprint.md
products/{project}/domain-model.md
products/{project}/feature-map.md
products/{project}/engineering-contract.yaml
products/{project}/port-map.md
products/{project}/adapter-map.md
products/{project}/project.config.yaml
products/{project}/adr/0001-project-initial-architecture.md
context-packs/{project}.yaml
```

## Review Gates

```text
architecture_review
domain_review
contract_review
adapter_boundary_review
human_approval_before_first_execution
```

## Done Criteria

- [ ] Project intent is clear.
- [ ] Core domain is named.
- [ ] Bounded contexts are identified if needed.
- [ ] Engineering Contract exists.
- [ ] Port map exists.
- [ ] Adapter map exists.
- [ ] Project config exists.
- [ ] Context pack exists.
- [ ] Initial ADR exists.
- [ ] Project is ready for module planning.

## Anti-Pattern

Do not start a new project by asking a code adapter to generate an app directly.

Correct flow:

```text
Intent -> Domain -> Blueprint -> Contract -> Ports -> Adapters -> Context Pack -> Module Planning
```
