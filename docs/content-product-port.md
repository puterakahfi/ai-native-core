# ContentProductPort

## Purpose

`ContentProductPort` defines the boundary for content-based digital products.

It supports products whose main deliverable is structured knowledge, written guidance, prompts, frameworks, or packaged content.

## Position in Native AI Framework

```text
ProductOutputPort
→ ContentProductPort
→ Content Product Contract
→ Knowledge / Context
→ Writing / Editing Skills
→ Export Adapter
→ Review
→ Packaging
→ Publishing
```

## Supported Output Types

```text
ebook
workbook
prompt_pack
playbook
guide
checklist
content_pack
knowledge_base
content_system
```

## Responsibilities

- Define content product structure.
- Resolve audience, promise, outline, modules, and required source material.
- Map content sections to knowledge/context sources.
- Define writing, editing, review, and export requirements.
- Produce a reviewable content artifact or package manifest.
- Preserve source traceability from claim to source.

## Non-Responsibilities

`ContentProductPort` must not:

- publish content without approval,
- invent unsupported claims,
- bypass editorial review,
- replace `ReviewApprovalPort`,
- own payment, storefront, or distribution behavior,
- mutate source knowledge without approval.

## Input Contract

```yaml
content_product_input:
  product_id: ""
  output_type: "ebook | workbook | prompt_pack | playbook | guide | checklist | content_pack"
  title: ""
  audience: ""
  promise: ""
  source_paths: []
  outline: []
  tone: ""
  format_constraints:
    page_size: ""
    estimated_length: ""
    export_formats: []
```

## Output Contract

```yaml
content_product_output:
  product_id: ""
  output_type: ""
  title: ""
  outline: []
  sections: []
  source_map: []
  draft_artifact_path: ""
  export_artifacts: []
  review_checklist: []
  packaging_manifest: {}
```

## Default Workflow

```text
Clarify Content Promise
→ Gather Source Knowledge
→ Build Outline
→ Draft Content Sections
→ Add Examples / Exercises / Prompts
→ Edit for Structure and Voice
→ Review Claims and Completeness
→ Export Package
→ Review Approval
→ Publish only after approval
```

## Candidate Adapters

Taxonomy candidates only:

```text
MarkdownEbookAdapter
PDFExportAdapter
GoogleDocsExportAdapter
SlideDeckAdapter
GumroadProductAdapter
LemonSqueezyProductAdapter
```

## Quality Gates

- audience and promise are explicit,
- outline exists before drafting,
- source map exists for claims,
- content is complete for selected output type,
- exercises/prompts/checklists are usable,
- export format is declared,
- editorial review is complete,
- publishing is approval-gated.

## Dashboard Usage

`ContentProductPort` should show content products with:

```text
output type
outline status
draft status
source coverage
review status
export package readiness
publishing readiness
```

## Relationship to Existing Ports

```text
ProductOutputPort    → selects ContentProductPort
ContextManagementPort → resolves source knowledge
SkillManagementPort   → resolves writing/editing skills
ExecutionRunPort      → tracks draft/export attempts
ReviewApprovalPort    → approves final package
```

## Failure Behavior

- If outline is missing, return `outline_required`.
- If source material is missing, return `source_context_required`.
- If claims are unsupported, return `claim_review_required`.
- If export adapter is unavailable, return `export_adapter_unavailable`.
- If publishing is requested before approval, return `publishing_blocked`.
