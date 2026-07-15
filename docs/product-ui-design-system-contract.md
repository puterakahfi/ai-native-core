# Product UI Design System Contract

## Purpose

`ProductUIDesignSystemContract` defines the locked UI design system contract that a product must follow when AI agents, UI design adapters, and code execution adapters generate or implement UI.

It connects a product to a specific UI design system so every page, dashboard, component, and AI-generated output stays consistent with that product's visual rules.

## Why It Exists

AI-native development must not rely on vague prompts such as:

```text
make the UI clean and modern
```

Instead, each product should resolve a concrete design contract through `UIDesignSystemPort`.

```text
Product
→ ProductUIDesignSystemContract
→ UIDesignSystemPort
→ Design / Code Adapter
→ Consistent UI Output
```

## Global vs Product Contract

A product can inherit from a global design system and then define product-specific extensions.

```text
GlobalUIDesignSystemContract
→ ProductUIDesignSystemContract
→ PagePatternContract
```

### GlobalUIDesignSystemContract

Defines shared rules across Native AI Framework products:

- base tokens,
- layout principles,
- component behavior,
- accessibility baseline,
- reusable status semantics,
- shared dashboard patterns.

### ProductUIDesignSystemContract

Defines product-specific visual governance:

- product visual direction,
- product color roles,
- product typography direction,
- product component variants,
- product dashboard patterns,
- product-specific UI rules,
- product quality gates.

### PagePatternContract

Defines page-specific rules:

- dashboard page,
- registry viewer,
- inspector page,
- review page,
- execution page,
- settings page,
- command center page.

## Control Plane Role

`ProductUIDesignSystemContract` is a control-plane contract.

It is resolved by `UIDesignSystemPort` and consumed by:

```text
UIDesignPort
CodeExecutionPort
WebAppPort
EvaluationPort
ReviewApprovalPort
```

It prevents UI generation and UI implementation from becoming product-inconsistent.

## Required Contract Shape

```yaml
product_ui_design_system:
  product_id: ""
  app_id: ""
  design_system_id: ""
  status: "draft | defined | active | used | reviewed | improved"

  inherits_from:
    - "global-ui-design-system"

  visual_direction:
    style: ""
    personality: []
    must_feel_like: []
    must_not_feel_like: []

  tokens:
    color_roles: {}
    typography_roles: {}
    spacing_roles: {}
    radius_roles: {}
    shadow_roles: {}

  layout_patterns: []
  required_components: []
  status_rules: []
  responsive_rules: []
  accessibility_rules: []
  page_patterns: []

  quality_gates: []

  used_by:
    pages: []
    adapters: []
    workflows: []
```

## Minimum Required Fields

Every product UI design system contract should define:

- product id,
- app id,
- design system id,
- status,
- visual direction,
- color roles,
- layout patterns,
- required components,
- status rules,
- responsive rules,
- quality gates,
- used by pages/adapters/workflows.

## Example: Native AI Framework Dashboard

```yaml
product_ui_design_system:
  product_id: "native-ai-framework"
  app_id: "web"
  design_system_id: "native-ai-command-center-ui"
  status: "active"

  inherits_from:
    - "global-dashboard-ui"

  visual_direction:
    style: "clean_blue_saas"
    personality:
      - "calm"
      - "technical"
      - "structured"
      - "premium developer tool"
    must_feel_like:
      - "AI system command center"
      - "developer tool"
      - "operational dashboard"
    must_not_feel_like:
      - "generic admin panel"
      - "cyberpunk"
      - "neon AI generator"
      - "random template"

  tokens:
    color_roles:
      background: "bgApp"
      surface: "bgSurface"
      border: "borderSubtle"
      primary: "accentBlue"
      text_primary: "textPrimary"
      text_secondary: "textSecondary"
    typography_roles:
      page_title: "pageTitle"
      section_title: "sectionTitle"
      body: "bodyText"
      metadata: "metadataText"
    spacing_roles:
      page_padding: "pagePadding"
      card_gap: "cardGap"
      section_gap: "sectionGap"
    radius_roles:
      card: "radiusCard"
      badge: "radiusBadge"
      panel: "radiusPanel"
    shadow_roles:
      card: "shadowCard"
      panel: "shadowPanel"

  layout_patterns:
    - "app_shell"
    - "command_center_page"
    - "registry_viewer"
    - "right_inspector"
    - "metric_row"
    - "filter_toolbar"

  required_components:
    - "AppShell"
    - "SidebarNav"
    - "Topbar"
    - "PageHeader"
    - "SectionCard"
    - "MetricCard"
    - "StatusBadge"
    - "SourceBadge"
    - "FilterToolbar"
    - "InspectorPanel"
    - "MetadataField"
    - "EmptyState"
    - "ErrorState"
    - "LoadingState"

  status_rules:
    - "adapter_status_badge_rules"
    - "task_status_badge_rules"
    - "execution_status_badge_rules"

  responsive_rules:
    - "desktop_fluid_command_center_layout"
    - "tablet_compact_grid_layout"
    - "mobile_stacked_content_layout"

  accessibility_rules:
    - "readable_contrast"
    - "focus_visible"
    - "semantic_headings"
    - "keyboard_accessible_filters"

  page_patterns:
    - "tasks_page"
    - "adapters_page"
    - "ports_page"
    - "executions_page"
    - "reviews_page"

  quality_gates:
    - "must_use_shared_components"
    - "must_use_status_badge_rules"
    - "must_support_responsive_layout"
    - "must_not_create_random_page_level_styles"
    - "must_keep_clean_blue_saas_direction"
    - "must_preserve_command_center_information_density"

  used_by:
    pages:
      - "/tasks"
      - "/adapters"
      - "/products"
      - "/context-packs"
      - "/skills"
      - "/ports"
      - "/executions"
      - "/reviews"
    adapters:
      - "FileBackedUIDesignSystemAdapter"
      - "ExampleProductDesignAdapter"
      - "HtmlCssMockupAdapter"
      - "StorybookPreviewAdapter"
      - "CodexAdapter"
    workflows:
      - "dashboard_design_system_foundation"
      - "adapter_registry_viewer"
      - "task_command_center"
```

## Enforcement Rule

UI-generating or UI-implementing adapters must resolve this contract before producing product UI.

They must not invent new visual rules unless the task explicitly updates the product design system contract and passes human review.

## Evaluation Rule

`EvaluationPort` should use this contract to check:

- whether shared components are used,
- whether status colors are consistent,
- whether layout patterns are followed,
- whether responsive behavior is preserved,
- whether the product visual direction is still recognizable,
- whether the implementation created random one-off styles.
