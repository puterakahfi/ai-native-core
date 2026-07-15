# SkillManagementPort

## Purpose

`SkillManagementPort` defines the boundary for discovering, resolving, validating, and applying reusable AI execution skills inside Native AI Framework.

Skills are reusable procedures. They are not one-off prompts.

## Position in the Framework

```text
Task / Workflow
→ Skill Resolution
→ Adapter Capability Check
→ Execution Procedure
→ Review
```

`SkillManagementPort` is part of execution governance. It is not a code executor, model provider, or task source.

## Primary Responsibilities

- List available skills.
- Group skills by category.
- Resolve skills required by a product, app, task, or adapter.
- Validate whether an adapter supports required skills.
- Expose skill metadata to the dashboard.
- Help prevent generic prompting by enforcing reusable procedures.

## Non-Responsibilities

`SkillManagementPort` must not:

- execute code,
- mutate task state,
- invent new skills during execution without review,
- bypass adapter contracts,
- replace rules or architecture constraints.

## Candidate Adapters

```text
MarkdownSkillAdapter
SkillRegistryYamlAdapter
GitHubSkillRegistryAdapter
DatabaseSkillRegistryAdapter
```

## Default Skill Workflow

```text
Receive Task Requirements
→ Resolve Product/App Required Skills
→ Resolve Adapter Required Skills
→ Validate Skill Availability
→ Attach Skill References to Handoff
→ Report Missing Skills
```

## Input Contract

```yaml
skill_management_input:
  product_id: ""
  app_id: ""
  task_id: ""
  adapter_name: ""
  required_skills: []
```

## Output Contract

```yaml
skill_management_output:
  resolved_skills: []
  missing_skills: []
  unsupported_skills: []
  ready_for_execution: false
```

## Quality Gates

- skill exists,
- skill category is known,
- required skills are resolved before execution,
- adapter supports required skills,
- missing skills block execution or trigger review,
- skills remain reusable and not task-specific hacks.

## Dashboard Usage

`SkillManagementPort` should power:

```text
/skills
/task required skills
/adapter supported skills
```

It should help the dashboard show whether a task has the right execution procedures before Codex or another adapter runs.
