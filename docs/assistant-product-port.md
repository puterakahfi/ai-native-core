# AssistantProductPort

## Purpose

`AssistantProductPort` defines the boundary for AI assistant products.

It supports custom GPTs, workflow assistants, knowledge assistants, support bots, and agent assistants where the deliverable is instruction, behavior, knowledge, tools, and reviewable assistant configuration.

## Position in Native AI Framework

```text
ProductOutputPort
→ AssistantProductPort
→ Assistant Product Contract
→ Instructions
→ Knowledge / Context
→ Rules
→ Skills
→ Tool / Adapter Plan
→ Evaluation
→ Review
→ Packaging
```

## Supported Output Types

```text
custom_gpt
ai_assistant
agent_assistant
support_bot
workflow_assistant
knowledge_assistant
```

## Responsibilities

- Define assistant purpose, audience, boundaries, and expected behavior.
- Define instruction hierarchy and operating rules.
- Resolve knowledge files and context packs.
- Declare allowed tools or adapters.
- Define refusal, escalation, and failure behavior.
- Produce reviewable assistant configuration and packaging notes.
- Support evaluation against target tasks.

## Non-Responsibilities

`AssistantProductPort` must not:

- call model APIs directly,
- upload or mutate assistant configuration without approval,
- bypass safety rules,
- grant tool access without review,
- replace product or workflow strategy,
- hide knowledge gaps.

## Input Contract

```yaml
assistant_product_input:
  product_id: ""
  output_type: "custom_gpt | ai_assistant | agent_assistant | support_bot | workflow_assistant | knowledge_assistant"
  assistant_name: ""
  target_users: []
  jobs_to_be_done: []
  instruction_source_paths: []
  knowledge_source_paths: []
  rules: []
  skills: []
  tool_policy:
    tools_allowed: []
    tools_forbidden: []
```

## Output Contract

```yaml
assistant_product_output:
  assistant_name: ""
  output_type: ""
  instruction_artifact_path: ""
  knowledge_manifest: []
  tool_manifest: []
  safety_boundaries: []
  evaluation_tasks: []
  review_checklist: []
  packaging_manifest: {}
```

## Default Workflow

```text
Define Assistant Job
→ Define Instruction Hierarchy
→ Gather Knowledge / Context
→ Apply Rules and Skills
→ Define Tool Access
→ Draft Assistant Package
→ Evaluate Against Example Tasks
→ Review Safety and Quality
→ Package for Target Builder
→ Publish only after approval
```

## Candidate Adapters

Taxonomy candidates only:

```text
CustomGPTBuilderAdapter
OpenAIInstructionAdapter
GoogleDocsExportAdapter
MarkdownEbookAdapter
NotionTemplateAdapter
```

## Quality Gates

- assistant purpose is narrow and explicit,
- instruction hierarchy is present,
- knowledge manifest is complete,
- tools are declared and reviewed,
- forbidden behavior is defined,
- escalation behavior exists,
- evaluation tasks pass,
- publishing or upload is approval-gated.

## Dashboard Usage

`AssistantProductPort` should show:

```text
assistant type
instruction status
knowledge manifest status
tool policy status
evaluation readiness
review status
packaging target
```

## Relationship to Existing Ports

```text
ProductOutputPort     → selects AssistantProductPort
ContextManagementPort → resolves knowledge/context
RuleManagementPort    → applies assistant safety rules
SkillManagementPort   → applies assistant design skills
ToolIntegrationPort   → describes allowed tools
ReviewApprovalPort    → approves package and publication
```

## Failure Behavior

- If instructions are missing, return `instructions_required`.
- If knowledge is missing, return `knowledge_manifest_required`.
- If tool policy is unclear, return `tool_policy_required`.
- If evaluation fails, return `assistant_revision_required`.
- If upload/publishing is requested before approval, return `publishing_blocked`.
