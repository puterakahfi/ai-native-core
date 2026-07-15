# RuleManagementPort

## Purpose

`RuleManagementPort` defines the boundary for discovering, resolving, validating, and enforcing framework rules that constrain AI agents, adapters, workflows, and implementation tasks.

Rules are constraints. Skills are procedures.

## Position in the Framework

```text
Product / App / Task
→ Rule Resolution
→ Boundary Enforcement
→ Adapter Handoff
→ Review
```

`RuleManagementPort` is part of governance. It is not a skill registry, task source, or execution adapter.

## Primary Responsibilities

- List available rules.
- Group rules by category.
- Resolve applicable rules for a product, app, task, or adapter.
- Validate architecture and boundary constraints.
- Detect rule violations.
- Expose rule readiness to the dashboard.
- Block or warn before unsafe execution.

## Non-Responsibilities

`RuleManagementPort` must not:

- execute code,
- create tasks,
- replace human approval,
- mutate production systems,
- become a vendor-specific adapter policy only.

## Candidate Adapters

```text
MarkdownRuleAdapter
RuleRegistryYamlAdapter
ArchitectureRuleAdapter
ProductRuleAdapter
DatabaseRuleRegistryAdapter
```

## Default Rule Workflow

```text
Receive Task / Workflow Reference
→ Resolve Product Rules
→ Resolve App Rules
→ Resolve Architecture Rules
→ Validate Planned Action
→ Report Violations
→ Block / Warn / Allow
```

## Input Contract

```yaml
rule_management_input:
  product_id: ""
  app_id: ""
  task_id: ""
  adapter_name: ""
  planned_action: ""
```

## Output Contract

```yaml
rule_management_output:
  applicable_rules: []
  violations: []
  warnings: []
  action: "allow"
```

## Quality Gates

- applicable rules are resolved,
- architecture boundary rules are checked,
- destructive actions require approval,
- adapter boundaries are preserved,
- violations are visible before execution,
- rule decisions are auditable.

## Dashboard Usage

`RuleManagementPort` should power:

```text
/rules
/task rule readiness
/adapter safety boundaries
/review gates
```

It should help the dashboard explain why an action is allowed, blocked, or needs review.
