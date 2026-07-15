# Diagram Architect Skill

## Purpose

Create renderer-agnostic diagrams for systems, workflows, contracts, runtime topology, responsibilities, and decisions.

This skill is a core visual-thinking capability. It decides what the diagram should communicate before any runtime chooses how to render it.

## Boundary

```text
diagram-architect = diagram reasoning, spec, truth model, verification
renderer adapter  = Mermaid, Excalidraw, SVG/HTML, image, ASCII, or another output format
runtime adapter   = Hermes/Codex/Claude/etc. execution of the diagram skill
```

Do not put renderer-specific syntax, visual style, or tool commands in the core contract. Core owns the diagram model; adapters own rendering.

## When To Use

Use this skill when the task is to visualize or explain:

- architecture or infrastructure topology
- runtime/session/profile sync models
- Native AI core/app/skill/runtime boundaries
- workflow or lifecycle stages
- contract-to-adapter relationships
- responsibility maps or ownership boundaries
- data/control flows
- decision trees or migration paths

Do not use this skill for pure graphic design, illustration, branding art, or UI mockups unless the task first needs a conceptual diagram spec.

## Core Responsibilities

### 1. Diagram Intent Classification

Name the diagram's purpose and audience before choosing a format.

Common intents:

```text
explain topology
clarify ownership
show flow direction
compare alternatives
prevent architectural misinterpretation
handoff implementation
support decision review
```

Completion criterion: the diagram purpose and audience are explicit.

### 2. View Selection

Choose the smallest diagram view that answers the question.

Common views:

```text
system_topology
runtime_topology
layer_boundary_map
workflow_lifecycle
contract_to_adapter_map
responsibility_map
data_flow
sequence_flow
decision_tree
```

Completion criterion: the chosen view is named and non-goal views are avoided.

### 3. Renderer-Agnostic Spec

Produce a neutral diagram spec before rendering:

```yaml
diagram:
  id: example
  title: Example Diagram
  type: runtime_topology
  purpose: Explain source of truth and client access
  audience: engineering
  boundaries: []
  nodes: []
  edges: []
  legend: []
  constraints: []
  verification: []
```

Completion criterion: every visual element traces to a node, edge, boundary, legend item, or constraint.

### 4. Truth Preservation

Prefer correctness over visual novelty.

Rules:

- Directional edges must reflect real data/control/ownership flow.
- Boundaries must mean ownership, trust, runtime, product, deployment, or lifecycle scope.
- Constraints and anti-patterns should be shown when omission would mislead.
- Examples must not look like required architecture.

Completion criterion: the diagram cannot be read as a false architecture recommendation.

### 5. Renderer Recommendation

After the spec exists, recommend a renderer:

```text
polished technical architecture -> SVG/HTML renderer
hand-drawn exploration -> Excalidraw renderer
docs-native quick view -> Mermaid renderer
terminal note -> ASCII renderer
presentation/story -> slide/infographic renderer
```

Completion criterion: renderer choice follows the diagram purpose and audience.

## Output Modes

### Diagram Brief

```markdown
## Intent
## Audience
## View
## Source Context
## Must Show
## Must Not Imply
## Renderer Recommendation
```

### Diagram Spec

```yaml
diagram:
  id:
  title:
  type:
  purpose:
  audience:
  boundaries:
    - id:
      label:
      meaning:
  nodes:
    - id:
      label:
      boundary:
      kind:
      description:
  edges:
    - from:
      to:
      label:
      direction:
      kind:
  legend:
    - symbol:
      meaning:
  constraints:
    - text:
      reason:
  verification:
    - check:
```

### Renderer Handoff

```markdown
## Diagram Spec Source
## Renderer
## Rendering Constraints
## Required Labels
## Verification Checklist
```

## Verification Checklist

- [ ] Purpose and audience are explicit.
- [ ] Diagram type/view is the smallest useful view.
- [ ] Nodes, edges, and boundaries are renderer-agnostic.
- [ ] Directionality and ownership are labeled.
- [ ] Constraints/non-goals are shown when important.
- [ ] Renderer is selected after the spec.
- [ ] Rendered artifact, if any, is checked against the spec.
