# Workflow: GitHub Project Task to Execution Contract

## Purpose

Define the single-task flow for Native AI Framework.

GitHub Project is the task management system.
Local contract files are execution artifacts linked from the same task.
Code adapters such as Codex must reference the same canonical task identity.

## Principle

```text
One logical task.
Many adapters around the same task.
No duplicate task identity.
```

## Flow

```text
GitHub Project #9 Task
-> canonical_task_id assigned
-> execution contract artifact generated or linked
-> contract path attached to the same task
-> CodeExecutionAdapter reads the linked contract
-> CodeExecutionAdapter executes allowed scope
-> execution summary is reported back to the same GitHub Project task
-> review gates update the same task status
```

## Roles

### GitHubProjectTaskAdapter

Responsible for:

```text
- task lifecycle
- task status
- review visibility
- execution tracking
- board management
```

### LocalFileTaskContractAdapter

Responsible for:

```text
- storing detailed execution contract artifacts
- preserving exact scope, skills, allowed files, and acceptance criteria
- giving code adapters a stable contract path to read
```

### CodeExecutionAdapter

Responsible for:

```text
- reading the linked contract path
- referencing the same canonical_task_id
- executing only allowed scope
- reporting result back to the same task manager item
```

## Required Identity Fields

Every execution contract artifact must include:

```yaml
identity:
  canonical_task_id: ""
  task_manager: "GitHubProjectTaskAdapter"
  task_manager_url: "https://github.com/users/native-ai/projects/9"
  contract_artifact: ""
  rule: "GitHub Project item and implementation contract must represent the same logical task using the same canonical_task_id."
```

Every code execution section must include:

```yaml
execution_reference:
  code_execution_adapter: "CodexAdapter"
  must_reference_canonical_task_id: ""
  must_read_contract_path: ""
  must_not_create_new_task: true
  must_report_back_to_task_manager: true
```

## Status Flow

```text
draft
ready_for_execution
in_progress
generated
needs_review
revision_requested
approved
implemented
tested
shipped
failed
```

## Rules

- Do not create task contracts without a canonical task identity.
- Do not let Codex create a second task.
- Do not treat local YAML as an independent task source.
- Do not mark a task as approved or shipped without human approval.
- Every execution summary must reference the canonical_task_id.
- Every pull request or commit related to a task should mention the canonical_task_id.

## Output

The adapter handoff must return:

```text
canonical_task_id
project_item_reference
contract_path
files_created
files_updated
commands_to_run
acceptance_criteria_check
risks
review_notes
```
