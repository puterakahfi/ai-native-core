# ProductOutputPort

## Purpose

`ProductOutputPort` defines the control-plane boundary for deciding what a Native AI Framework product should produce.

It expands the framework beyond software-only delivery. A product can produce a web app, assistant, ebook, workbook, course, template, knowledge base, content system, automation package, or creative asset pack.

## Position in Native AI Framework

```text
Product Intent
→ Product Blueprint
→ ProductOutputPort
→ Output-specific Product Contract
→ Knowledge / Context
→ Rules
→ Skills
→ Adapter
→ Execution
→ Review
→ Packaging
→ Publishing
→ Feedback
→ Improvement
```

`ProductOutputPort` sits after product strategy and before execution planning. It does not replace `ProductManagementPort`; it specializes product direction into deliverable output boundaries.

## Supported Output Types

```text
web_app
mobile_app
console_app
ebook
workbook
video_course
prompt_pack
custom_gpt
notion_template
google_sheet_system
automation_template
knowledge_base
content_system
creative_asset_pack
```

## Responsibilities

- Identify the intended output type for a product or product module.
- Select the output-specific product port.
- Define the minimum output contract required before execution.
- Connect output type to required knowledge, context, rules, skills, and review gates.
- Preserve product intent while allowing many product packaging forms.
- Report unsupported or ambiguous output types.

## Non-Responsibilities

`ProductOutputPort` must not:

- generate the final output directly,
- execute adapter work,
- publish or sell the product,
- bypass review approval,
- mutate product files without approval,
- replace output-specific ports,
- decide business strategy without product intent and blueprint context.

## Input Contract

```yaml
product_output_input:
  product_id: ""
  module_id: ""
  product_intent_path: ""
  product_blueprint_path: ""
  requested_output_type: "ebook | custom_gpt | web_app | prompt_pack | notion_template | ..."
  target_audience: ""
  value_proposition: ""
  constraints:
    review_required: true
    publishing_allowed: false
```

## Output Contract

```yaml
product_output_output:
  product_id: ""
  module_id: ""
  output_type: ""
  selected_port: ""
  output_contract_path: ""
  required_knowledge: []
  required_rules: []
  required_skills: []
  candidate_adapters: []
  quality_gates: []
  packaging_requirements: []
  publishing_requirements: []
  unsupported_requirements: []
```

## Default Workflow

```text
Read Product Intent
→ Read Product Blueprint
→ Classify Output Type
→ Select Output-specific Product Port
→ Build Output Contract
→ Resolve Required Context / Rules / Skills
→ Select Candidate Adapter
→ Execute Draft Output
→ Review
→ Package
→ Publish only after approval
→ Capture Feedback
→ Improve Product Blueprint
```

## Candidate Adapters

These are taxonomy candidates only. They are not implemented integrations.

```text
PDFExportAdapter
GoogleDocsExportAdapter
MarkdownEbookAdapter
SlideDeckAdapter
VideoScriptAdapter
CustomGPTBuilderAdapter
OpenAIInstructionAdapter
NotionTemplateAdapter
GoogleSheetTemplateAdapter
CanvaDesignAdapter
GumroadProductAdapter
LemonSqueezyProductAdapter
YouTubePublishingAdapter
MetaContentPublishingAdapter
```

## Quality Gates

- output type is explicit,
- selected output port matches output type,
- output contract exists before execution,
- knowledge/context requirements are listed,
- rules and skills are resolved,
- packaging requirements are reviewable,
- publishing is blocked unless explicitly approved,
- feedback path exists for improvement.

## Dashboard Usage

`ProductOutputPort` should eventually power:

```text
/outputs
/products/[productId]/outputs
/products/[productId]/outputs/[outputId]
```

The dashboard should show output type, selected port, output contract status, review status, packaging status, and publishing readiness.

## Relationship to Existing Ports

```text
ProductManagementPort = discovers and validates product identity.
ProductOutputPort    = decides what the product produces.
TaskManagementPort   = tracks work required to produce it.
ExecutionRunPort     = tracks what actually ran.
ReviewApprovalPort   = decides whether output can advance.
```

## Failure Behavior

- If output type is missing, return `needs_output_classification`.
- If output contract is missing, block execution and return `contract_required`.
- If adapter is unavailable, return `adapter_unavailable`.
- If publishing is requested without approval, return `publishing_blocked`.
- If output type is unsupported, return `unsupported_output_type`.
