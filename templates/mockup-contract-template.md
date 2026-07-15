# Mockup Contract Template

Use this template to turn a wireframe or mockup into an implementation-ready contract for an engineering agent.

A mockup contract is not just a picture. It defines structure, components, interaction behavior, states, and verification expectations.

## 1. Mockup Identity

```text
Product:
Feature or surface:
Mockup name:
Version:
Status: draft | review | approved | superseded
Owner/reviewer:
```

## 2. Source Context

```text
Design brief:
User flow:
Product blueprint:
Engineering contract:
Related rules:
Related skills:
```

## 3. Screen Inventory

List screens, routes, dialogs, drawers, or panels.

| Screen | Purpose | Entry point | Exit/next action |
|---|---|---|---|
| | | | |

## 4. Layout Structure

Describe the screen hierarchy from outer shell to inner content.

```text
App shell:
Navigation:
Page header:
Primary content:
Secondary content:
Footer/actions:
```

## 5. Component Contract

List required components and preferred implementation primitives.

| Component | Purpose | Data required | Interaction |
|---|---|---|---|
| | | | |

## 6. Interaction Behavior

Describe what happens when the user acts.

```text
Primary action:
Secondary action:
Cancel/back behavior:
Keyboard behavior:
Form validation:
AI/tool invocation:
Human review point:
```

## 7. State Contract

Define every state the UI must render.

```text
loading:
empty:
error:
success:
needs_review:
approved:
disabled:
permission_denied:
```

## 8. Data Contract

Describe data displayed or collected by the mockup.

```text
Inputs:
Outputs:
Derived values:
Persistence:
External services/tools:
```

## 9. Responsive Behavior

```text
Desktop:
Tablet:
Mobile:
Overflow:
Minimum usable viewport:
```

## 10. Accessibility Requirements

- [ ] Semantic headings and landmarks defined.
- [ ] Keyboard path exists for primary flow.
- [ ] Form inputs have labels and error text.
- [ ] Color is not the only state indicator.
- [ ] Loading and error states are announced or visible.

## 11. Visual Constraints

```text
Design system:
Spacing/density:
Tone:
Brand rules:
Existing shell/navigation to preserve:
```

## 12. Acceptance Criteria

- [ ] Screen structure matches the approved mockup.
- [ ] Primary flow works end-to-end.
- [ ] Required states render correctly.
- [ ] Existing navigation/shell is preserved.
- [ ] No unrelated feature groups or capabilities are removed.
- [ ] Implementation follows engineering contract and UI rules.

## 13. Verification Plan

```text
Commands:
Browser route:
Screenshot required: yes/no
Manual checks:
Automated tests:
Known risks:
```

## 14. Engineering Handoff

```text
Files/modules likely to update:
Files/modules to preserve:
Dependencies requiring approval:
Follow-up docs:
```
