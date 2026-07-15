# MediaProductPort

## Purpose

`MediaProductPort` defines the boundary for media and creative product outputs.

It supports scripts, storyboards, slide decks, carousels, creative asset packs, and screen recording guides.

## Position in Native AI Framework

```text
ProductOutputPort
→ MediaProductPort
→ Media Product Contract
→ Creative Context
→ Script / Design Skills
→ Media Adapter
→ Review
→ Packaging
```

## Supported Output Types

```text
video_script
storyboard
slide_deck
carousel
creative_asset_pack
screen_recording_guide
```

## Responsibilities

- Define media goal, audience, format, channel, and creative constraints.
- Translate product context into script, storyboard, deck, or asset plan.
- Define asset requirements and review criteria.
- Produce a reviewable media package manifest.
- Preserve brand and claim safety across creative outputs.

## Non-Responsibilities

`MediaProductPort` must not:

- publish media without approval,
- generate final creative assets without review,
- bypass brand or claim safety rules,
- own social platform posting behavior,
- replace creative review decisions.

## Input Contract

```yaml
media_product_input:
  product_id: ""
  output_type: "video_script | storyboard | slide_deck | carousel | creative_asset_pack | screen_recording_guide"
  media_goal: ""
  audience: ""
  channel: ""
  format_constraints: {}
  brand_context_paths: []
  source_paths: []
```

## Output Contract

```yaml
media_product_output:
  output_type: ""
  script: ""
  storyboard: []
  slide_outline: []
  asset_manifest: []
  channel_constraints: []
  review_checklist: []
  packaging_manifest: {}
```

## Default Workflow

```text
Define Media Goal
→ Resolve Brand / Product Context
→ Choose Media Format
→ Draft Script or Storyboard
→ Define Asset Manifest
→ Review Brand / Claim / Channel Fit
→ Package Creative Assets
→ Publish only after approval
```

## Candidate Adapters

Taxonomy candidates only:

```text
VideoScriptAdapter
SlideDeckAdapter
CanvaDesignAdapter
PDFExportAdapter
YouTubePublishingAdapter
MetaContentPublishingAdapter
```

## Quality Gates

- media goal is explicit,
- target channel is explicit,
- format constraints are known,
- script/storyboard/deck is reviewable,
- brand safety is checked,
- claims are traceable,
- asset manifest is complete,
- publishing is approval-gated.

## Dashboard Usage

`MediaProductPort` should show:

```text
media output type
script status
storyboard status
asset manifest status
channel fit
creative review status
publishing readiness
```

## Relationship to Existing Ports

```text
ProductOutputPort     → selects MediaProductPort
ContentProductPort    → may supply scripts/guides
CreativeRenderingPort → may render preview artifacts
ReviewApprovalPort    → approves final media package
```

## Failure Behavior

- If media goal is missing, return `media_goal_required`.
- If channel constraints are missing, return `channel_constraints_required`.
- If brand context is missing, return `brand_context_required`.
- If creative review fails, return `media_revision_required`.
- If publishing is requested before approval, return `publishing_blocked`.
