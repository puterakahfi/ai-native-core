# UIDesignSystemPort

## Purpose

`UIDesignSystemPort` defines the control-plane boundary for UI design system governance inside Native AI Framework.

It exists so AI agents, UI mockup adapters, code execution adapters, and dashboard implementation tasks follow a reusable visual system instead of producing random page-level UI.

The design system is not only a folder of components. In an AI-native system, it is an experience contract that controls visual consistency, layout rules, component reuse, status color behavior, responsive behavior, and UI quality gates.

## Position in the Framework

```text
Product / App Intent
→ Product Blueprint
→ UI Requirements
→ UIDesignSystemPort
→ UI Tokens / Components / Patterns / Rules
→ UIDesignPort / Mockup Adapter
→ CodeExecutionPort / Implementation Adapter
→ EvaluationPort
→ ReviewApprovalPort
```

`UIDesignSystemPort` belongs to the control plane.

It feeds rules and reusable UI contracts into design, implementation, review, and evaluation workflows.

It is not a visual mockup generator, code executor, task source, publishing layer, or approval authority.

## Experience Governance Category

```text
ExperienceGovernance
├── UIDesignSystemPort
├── BrandSystemPort
├── ContentStyleGuidePort
├── AccessibilityPolicyPort
└── InteractionPatternPort
```

For the current MVP, `UIDesignSystemPort` is the primary port for dashboard UI consistency.

## Primary Responsibilities

- Define UI design tokens.
- Define reusable UI components.
- Define dashboard layout patterns.
- Define status visual rules.
- Define responsive behavior rules.
- Define accessibility baseline rules.
- Define page composition rules.
- Validate UI consistency before or after implementation.
- Provide UI constraints to `UIDesignPort` adapters.
- Provide UI constraints to `CodeExecutionPort` adapters.
- Prevent AI-generated random UI.

## Non-Responsibilities

`UIDesignSystemPort` must not:

- generate visual mockups by itself,
- execute code,
- manage task source of truth,
- publish UI changes,
- decide product roadmap,
- replace human review,
- bypass product-specific brand rules,
- become a one-off page styling dump.

## Relationship to Existing Ports

```text
UIDesignSystemPort
→ provides design rules to
  → UIDesignPort
  → CodeExecutionPort
  → WebAppPort
  → EvaluationPort
  → ReviewApprovalPort
```

### UIDesignSystemPort vs UIDesignPort

```text
UIDesignSystemPort = source of reusable UI rules, tokens, components, and layout contracts.
UIDesignPort       = adapter boundary for generating or reviewing UI mockups/directions.
```

### UIDesignSystemPort vs CodeExecutionPort

```text
UIDesignSystemPort = tells implementation adapters what visual system to follow.
CodeExecutionPort  = executes scoped code changes that implement UI.
```

### UIDesignSystemPort vs BrandSystemPort

```text
UIDesignSystemPort = product UI component and layout system.
BrandSystemPort    = brand identity, voice, logo, typography identity, and brand rules.
```

## Candidate Adapters

```text
FileBackedUIDesignSystemAdapter
StorybookDesignSystemAdapter
FigmaDesignSystemAdapter
ExampleProductDesignSystemAdapter
DatabaseDesignSystemAdapter
```

## Default UI Design System Workflow

```text
Receive UI Implementation Request
→ Resolve Product/App UI System
→ Resolve Tokens
→ Resolve Component Rules
→ Resolve Layout Pattern
→ Resolve Status Visual Rules
→ Provide Design Contract to Adapter
→ Validate Output Against UI System
→ Review / Improve
```

## Input Contract

```yaml
ui_design_system_input:
  product_id: ""
  app_id: ""
  page_id: ""
  component_scope: []
  required_patterns: []
  status_groups: []
  responsive_targets: []
```

## Output Contract

```yaml
ui_design_system_output:
  design_system_id: ""
  status: ""
  tokens: {}
  components: []
  layout_patterns: []
  status_rules: []
  responsive_rules: []
  accessibility_rules: []
  source_paths: []
  missing_contracts: []
```

## Design System Lifecycle

```text
draft
→ defined
→ active
→ used
→ reviewed
→ improved
```

## Minimum Design System Contract

A usable UI design system should define:

- color tokens,
- typography scale,
- spacing scale,
- radius rules,
- shadow rules,
- border rules,
- status color mapping,
- reusable components,
- page layout patterns,
- responsive behavior,
- empty/loading/error states,
- inspector/detail panel behavior,
- accessibility baseline.

## Dashboard Usage

`UIDesignSystemPort` should eventually power:

```text
/design-system
/ui-quality
/component-registry
/page-patterns
/status-visual-rules
```

It should allow the dashboard to show:

- tokens,
- component inventory,
- page composition patterns,
- status badge rules,
- responsive rules,
- UI consistency score,
- components used by each page,
- missing design contracts.

## Quality Gates

Outputs should be checked for:

- design token usage,
- component reuse,
- status color consistency,
- layout pattern compliance,
- responsive behavior,
- accessibility baseline,
- visual hierarchy,
- mobile readability,
- dashboard consistency,
- no one-off random styles.

## Control Plane Rule

Native AI Framework remains the control plane.

Design, mockup, and code execution adapters must follow the resolved UI design system contract.

A UI implementation task may create or improve components, but it must not silently invent a competing design system.
