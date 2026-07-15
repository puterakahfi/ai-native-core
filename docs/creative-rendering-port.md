# CreativeRenderingPort

## Purpose

`CreativeRenderingPort` defines the boundary for generating reviewable creative outputs such as videos, motion assets, screenshots, visual exports, and campaign rendering artifacts.

It exists so Native AI Framework can support creative production workflows without coupling the core domain to a specific rendering vendor, design generator, video engine, or publishing platform.

## Position in the Framework

```text
Intent
→ Blueprint
→ Creative Direction
→ Creative Rendering
→ Review
→ Export
→ Publishing
→ Analytics
```

`CreativeRenderingPort` sits after planning and creative direction, but before publishing.

It is not a task management layer, code execution layer, or product architecture layer.

## Primary Responsibilities

- Receive approved creative briefs, brand tokens, scripts, storyboards, and asset references.
- Produce reviewable creative artifacts.
- Support preview before final export.
- Preserve brand identity rules.
- Preserve claim safety rules.
- Return rendering metadata and review notes.
- Require human approval before publishing.

## Non-Responsibilities

`CreativeRenderingPort` must not:

- create product tasks,
- mutate task management systems,
- execute application code,
- define product architecture,
- publish directly without approval,
- invent unsupported product claims,
- bypass review gates.

## Subtype Ports

```text
CreativeRenderingPort
├── VideoGenerationPort
├── ImageGenerationPort
├── ScreenshotRenderingPort
├── DesignExportPort
└── MotionGraphicsPort
```

### VideoGenerationPort

Used for product launch videos, promo videos, dashboard walkthroughs, explainer videos, motion graphics, animated captions, and social media video variants.

Example adapter:

```text
HyperFramesVideoAdapter
```

### ImageGenerationPort

Used for static visual generation, campaign images, social media graphics, product visuals, and brand-controlled image outputs.

Example adapters:

```text
ExampleProductImageAdapter
ImageModelAdapter
```

### ScreenshotRenderingPort

Used for rendering UI states, landing pages, HTML/CSS mockups, dashboard screenshots, and visual QA references.

Example adapters:

```text
PlaywrightScreenshotAdapter
HtmlCssScreenshotAdapter
```

### DesignExportPort

Used for exporting design artifacts, design tokens, component references, and production handoff packages.

Example adapters:

```text
FigmaExportAdapter
ExampleProductExportAdapter
```

### MotionGraphicsPort

Used for animated campaign assets, logo animation, short motion posts, and visual transitions.

Example adapters:

```text
HyperFramesVideoAdapter
RemotionAdapter
```

## Adapter Lifecycle

```text
candidate
→ allowed
→ active
→ deprecated
→ retired
```

- `candidate`: adapter is documented but not yet used as a default workflow component.
- `allowed`: adapter may be used in approved workflows.
- `active`: adapter is the default implementation for a port in a product/app workflow.
- `deprecated`: adapter should be replaced but may still exist for compatibility.
- `retired`: adapter should not be used.

## Default Creative Rendering Workflow

```text
Creative Brief
→ Brand Token Resolution
→ Storyboard / Scene Plan
→ Renderable Composition
→ Preview Render
→ Human Review
→ Revision Loop
→ Final Export
→ Approved Publishing Adapter
→ Performance Analysis
```

## Human Approval Gate

Creative rendering must keep a human approval gate before publishing.

Default status flow:

```text
draft
→ generated
→ needs_review
→ approved
→ exported
→ scheduled
→ published
→ analyzed
→ improved
```

Adapters may generate and export review artifacts, but they must not auto-publish unless the product workflow explicitly allows it.

## Input Contract

A creative rendering task should provide:

```yaml
creative_rendering_input:
  brief: ""
  product: ""
  campaign: ""
  brand_tokens: []
  creative_direction: ""
  target_platform: ""
  aspect_ratio: ""
  duration: ""
  source_assets: []
  script: ""
  storyboard: []
  claims: []
  review_requirements: []
```

## Output Contract

A creative rendering adapter should return:

```yaml
creative_rendering_output:
  preview_url: ""
  output_files: []
  export_metadata: {}
  review_notes: []
  quality_gate_results: []
  approval_required: true
```

## Quality Gates

Creative rendering outputs should be checked for:

- brand consistency,
- visual hierarchy,
- readability,
- claim safety,
- aspect ratio compliance,
- asset usage correctness,
- caption readability,
- motion timing when video is involved,
- export quality,
- human approval before publishing.

## ExampleProduct Product Opportunity

For ExampleProduct, `CreativeRenderingPort` can extend the product from an AI Creative Control System into an AI Campaign Rendering System.

Recommended ExampleProduct pipeline:

```text
Brand Identity Lock
→ Campaign Brief
→ Creative Direction
→ Static Design
→ Motion Variant
→ Video Promo
→ Human Review
→ Export
→ Publish
→ Analyze
→ Improve Brand Memory
```

This allows ExampleProduct to support static designs, motion variations, video promos, and campaign-ready exports while preserving brand identity and review control.

## Example Adapter Placement

```text
adapters/creative-rendering/hyperframes-video.adapter.yaml
```

`HyperFramesVideoAdapter` is a candidate adapter for `CreativeRenderingPort` with subtype `VideoGenerationPort`.

It should be used for reviewable video composition workflows, not dashboard UI mockup generation, task management, or code execution.
