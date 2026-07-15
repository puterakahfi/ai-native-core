# UISurfacePort

## Purpose

`UISurfacePort` defines the control-plane boundary for manifesting a resolved UI design system contract into a target user interface surface.

It exists because a product UI design system contract should not be limited to one runtime such as web. The same product-level visual and experience rules may need to be translated into web dashboards, console applications, mobile apps, desktop apps, or other interface surfaces.

`UISurfacePort` turns an abstract UI design system contract into platform-specific UI implementation guidance.

## Position in the Framework

```text
Product / App Intent
→ ProductUIDesignSystemContract
→ UIDesignSystemPort
→ UISurfacePort
→ Surface Adapter
→ UI Implementation
→ EvaluationPort
→ ReviewApprovalPort
```

`UIDesignSystemPort` resolves the product UI contract.

`UISurfacePort` translates that contract for a specific surface.

`CodeExecutionPort` or other implementation adapters may then execute the scoped changes.

## Surface Types

Common surface targets:

```text
web
console
mobile
desktop
admin
marketing
embedded
api_docs
```

## Primary Responsibilities

- Receive resolved product UI design system contract.
- Identify target surface type.
- Translate tokens into surface-compatible tokens.
- Translate layout patterns into surface-specific layout rules.
- Translate status semantics into surface-specific visual behavior.
- Translate component requirements into surface-compatible primitives.
- Provide implementation guidance to `CodeExecutionPort` or relevant implementation adapters.
- Preserve product visual identity across different surfaces.
- Report unsupported surface requirements.

## Non-Responsibilities

`UISurfacePort` must not:

- define the product UI design system itself,
- invent product visual rules,
- execute code changes,
- mutate task source of truth,
- publish UI changes,
- bypass review approval,
- replace platform-specific accessibility requirements,
- override product brand rules without approval.

## Relationship to Other Ports

```text
ProductUIDesignSystemContract
→ UIDesignSystemPort
→ UISurfacePort
  → WebUISurfaceAdapter
  → ConsoleUISurfaceAdapter
  → MobileUISurfaceAdapter
  → DesktopUISurfaceAdapter
→ CodeExecutionPort
→ EvaluationPort
→ ReviewApprovalPort
```

### UIDesignSystemPort vs UISurfacePort

```text
UIDesignSystemPort = resolves product UI rules and design system contract.
UISurfacePort      = translates the resolved contract into a specific UI surface.
```

### UISurfacePort vs CodeExecutionPort

```text
UISurfacePort     = produces platform-specific UI implementation guidance.
CodeExecutionPort = applies scoped implementation changes.
```

## Example Translation

Contract-level status rule:

```yaml
status_rules:
  approved: success
  failed: danger
  needs_review: warning
```

Web surface:

```text
approved     = green badge
failed       = red badge
needs_review = amber badge
```

Console surface:

```text
approved     = ✅ APPROVED
failed       = ❌ FAILED
needs_review = ⚠️ NEEDS REVIEW
```

Mobile surface:

```text
approved     = green compact pill
failed       = red compact pill
needs_review = amber compact chip
```

The semantic meaning stays the same. The manifestation changes by surface.

## Input Contract

```yaml
ui_surface_input:
  product_id: ""
  app_id: ""
  design_system_id: ""
  surface_type: "web | console | mobile | desktop | admin | marketing | embedded | api_docs"
  product_ui_design_system_contract: {}
  page_or_flow_id: ""
  target_runtime: ""
  implementation_adapter: ""
```

## Output Contract

```yaml
ui_surface_output:
  product_id: ""
  app_id: ""
  design_system_id: ""
  surface_type: ""
  target_runtime: ""
  surface_tokens: {}
  surface_components: []
  surface_layout_patterns: []
  surface_status_rules: []
  surface_responsive_rules: []
  implementation_guidance: []
  unsupported_requirements: []
  quality_gates: []
```

## Surface Adapter Candidates

```text
WebUISurfaceAdapter
ConsoleUISurfaceAdapter
MobileUISurfaceAdapter
DesktopUISurfaceAdapter
MarketingUISurfaceAdapter
DocsUISurfaceAdapter
```

## Default Workflow

```text
Receive Surface Manifestation Request
→ Resolve ProductUIDesignSystemContract
→ Select Surface Adapter
→ Translate Tokens
→ Translate Components
→ Translate Layout Patterns
→ Translate Status Rules
→ Generate Surface Implementation Guidance
→ Pass to CodeExecutionPort or Renderer
→ Evaluate Surface Consistency
→ Review / Improve
```

## Quality Gates

- product design system contract is resolved,
- surface type is explicit,
- surface adapter is selected,
- surface output preserves semantic status rules,
- surface output preserves product visual identity,
- platform constraints are respected,
- unsupported requirements are reported,
- no random surface-specific visual invention,
- output is reviewable before execution.

## Control Plane Rule

A UI implementation task must not go directly from prompt to web/mobile/console implementation.

It should follow:

```text
ProductUIDesignSystemContract
→ UIDesignSystemPort
→ UISurfacePort
→ Surface Adapter
→ CodeExecutionPort / Renderer
→ EvaluationPort
→ ReviewApprovalPort
```

This keeps multi-surface product UI consistent while still allowing each platform to express the design system appropriately.
