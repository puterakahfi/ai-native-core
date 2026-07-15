# Workflow: Add Module

## Purpose

Add a new module to an existing project without breaking domain boundaries, engineering contract, port map, adapter map, or review gates.

## Input

```text
project_id
module_name
module_goal
user_need
expected_output
constraints
related_existing_context
```

## Process

```text
1. Load project configuration
2. Load context pack
3. Load engineering contract
4. Load domain model
5. Check module intent
6. Check domain impact
7. Decide bounded context placement
8. Create module spec
9. Check port impact
10. Check adapter impact
11. Create feature spec
12. Create implementation task
13. Run architecture review
14. Execute through selected adapter after approval
```

## Domain Impact Decision

A module can be:

```text
part_of_existing_bounded_context
new_bounded_context
application_service_only
adapter_integration_only
small_feature_not_module
```

## Output Files

```text
products/{project}/modules/{module}/README.md
products/{project}/modules/{module}/intent.md
products/{project}/modules/{module}/module-spec.md
products/{project}/modules/{module}/domain-impact.md
products/{project}/modules/{module}/port-impact.md
products/{project}/modules/{module}/adapter-impact.md
products/{project}/modules/{module}/feature-spec.md
tasks/{project}/{module}/implementation-task.yaml
```

## Review Gates

```text
domain_impact_review
architecture_review
contract_review
port_adapter_review
human_approval_before_execution
```

## Done Criteria

- [ ] Existing project context is loaded.
- [ ] Module intent is clear.
- [ ] Domain impact is documented.
- [ ] Bounded context decision is documented.
- [ ] Port impact is documented.
- [ ] Adapter impact is documented.
- [ ] Feature spec exists.
- [ ] Implementation task exists.
- [ ] Review gates are defined.

## Anti-Pattern

Do not add modules directly from an adapter prompt.

Correct flow:

```text
Load Project -> Domain Impact -> Module Spec -> Port Impact -> Adapter Impact -> Task Contract -> Adapter Execution
```
