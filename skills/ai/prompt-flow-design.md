# Prompt Flow Design Skill

## Purpose

Help agents design structured AI workflows instead of isolated prompts.

A prompt flow defines how input, context, knowledge, rules, tools, memory, output, evaluation, and human review work together.

## When To Use

Use this skill when designing:

- AI generation feature
- AI assistant workflow
- Creative generation workflow
- Coding agent workflow
- Content automation workflow
- Review or evaluation agent
- Tool/MCP-powered workflow

## Required Input

```text
- Product intent
- User input
- Desired output
- Knowledge sources
- Applicable rules
- Required skills
- Available tools
- Human review requirement
- Evaluation criteria
```

## Process

### 1. Define Workflow Purpose

State what the AI flow must accomplish.

### 2. Define Input Contract

Specify required and optional inputs.

Example:

```text
required:
  - brand_profile
  - campaign_goal
  - target_audience
optional:
  - reference_style
  - platform
  - output_format
```

### 3. Define Context Sources

List sources the agent must use:

```text
- Product knowledge
- Domain knowledge
- Brand identity
- Engineering Contract
- Rules
- Previous decisions
```

### 4. Define Prompt Stages

Break one big prompt into stages.

Example:

```text
1. Intent interpretation
2. Context retrieval
3. Constraint selection
4. Draft generation
5. Self-check
6. Evaluation
7. Human review
8. Finalization
```

### 5. Define Tool Use

Specify allowed tools and risk level.

Tool use must follow MCP/tool governance.

### 6. Define Output Contract

Specify exact output structure.

### 7. Define Evaluation Criteria

Define how output quality will be judged.

### 8. Define Human Review Point

Specify where humans approve, reject, or edit.

### 9. Define Failure Handling

Specify what happens when context is missing, tool fails, AI output is low quality, or evaluation fails.

### 10. Define Improvement Loop

Capture feedback and update knowledge, rules, skills, or memory.

## Output Format

```markdown
# Prompt Flow: <workflow-name>

## 1. Purpose

## 2. Input Contract

## 3. Context Sources

## 4. Rules Applied

## 5. Skills Applied

## 6. Prompt Stages

## 7. Tool Use

## 8. Output Contract

## 9. Evaluation Criteria

## 10. Human Review Point

## 11. Failure Handling

## 12. Improvement Loop
```

## Quality Checklist

- [ ] AI role is specific and bounded.
- [ ] Input contract is clear.
- [ ] Context sources are explicit.
- [ ] Rules and skills are referenced.
- [ ] Tool use is governed.
- [ ] Output format is defined.
- [ ] Evaluation criteria are measurable.
- [ ] Human review point is defined.
- [ ] Failure handling exists.
- [ ] Feedback loop updates system knowledge.

## ExampleProduct Example

For ExampleProduct campaign generation:

```text
Brand Profile
-> Identity Lock
-> Campaign Goal
-> Platform Constraint
-> Creative Direction
-> Prompt Flow
-> Asset Generation
-> Creative Review
-> Human Approval
-> Export
-> Feedback Update
```

Do not allow asset generation without brand context and review gate.
