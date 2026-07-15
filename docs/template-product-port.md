# TemplateProductPort

## Purpose

`TemplateProductPort` defines the boundary for reusable system templates.

It supports Notion templates, Google Sheet systems, Airtable bases, workflow templates, and dashboard templates.

## Position in Native AI Framework

```text
ProductOutputPort
→ TemplateProductPort
→ Template Product Contract
→ Schema / Workflow Context
→ Template Adapter
→ Review
→ Packaging
```

## Supported Output Types

```text
notion_template
google_sheet_template
airtable_base
workflow_template
dashboard_template
google_sheet_system
automation_template
```

## Responsibilities

- Define template user, workflow, fields, views, and expected outputs.
- Define template schema and setup instructions.
- Define import/export packaging requirements.
- Produce a reviewable template manifest.
- Protect users from fragile or undocumented template logic.

## Non-Responsibilities

`TemplateProductPort` must not:

- create external workspace resources without approval,
- publish templates without review,
- own payment or storefront behavior,
- hide formulas, automations, or dependencies,
- mutate user data.

## Input Contract

```yaml
template_product_input:
  product_id: ""
  output_type: "notion_template | google_sheet_template | airtable_base | workflow_template | dashboard_template"
  template_name: ""
  target_user: ""
  workflow_steps: []
  schema: {}
  views: []
  automation_requirements: []
```

## Output Contract

```yaml
template_product_output:
  template_name: ""
  schema_manifest: {}
  view_manifest: []
  formula_manifest: []
  automation_manifest: []
  setup_instructions: []
  review_checklist: []
  packaging_manifest: {}
```

## Default Workflow

```text
Define Workflow
→ Define Schema
→ Define Views
→ Define Formula / Automation Rules
→ Generate Template Manifest
→ Review Usability and Safety
→ Package Setup Instructions
→ Publish only after approval
```

## Candidate Adapters

Taxonomy candidates only:

```text
NotionTemplateAdapter
GoogleSheetTemplateAdapter
SlideDeckAdapter
GumroadProductAdapter
LemonSqueezyProductAdapter
```

## Quality Gates

- user workflow is explicit,
- schema is documented,
- formulas or automations are listed,
- setup instructions exist,
- no hidden dependencies,
- template can be reviewed before publication,
- publishing is approval-gated.

## Dashboard Usage

`TemplateProductPort` should show:

```text
template type
schema status
view count
automation status
setup readiness
review status
packaging readiness
```

## Relationship to Existing Ports

```text
ProductOutputPort     → selects TemplateProductPort
ToolIntegrationPort   → describes external tool boundaries
PersistencePort       → may describe structured state
ReviewApprovalPort    → approves template package
```

## Failure Behavior

- If schema is missing, return `schema_required`.
- If setup instructions are missing, return `setup_required`.
- If automation requirements are unsafe, return `automation_review_required`.
- If external creation is requested before approval, return `approval_required`.
