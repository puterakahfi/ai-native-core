# Master Design Skill

## Purpose

Operate as a shared design skill for AI-native product work.

`master-design` combines these reusable roles:

```text
Senior Product Designer
SaaS UI/UX Designer
Design Systems Specialist
Frontend Art Director
```

Use this skill to turn product intent and blueprint into experience design artifacts that are clear enough for engineering agents to implement and verify.

This is a core/shared skill. Product-specific design rules belong under `products/<product-id>/skills/` and should be layered on top of this skill.

## When To Use

Use this skill during the Experience Design phase when:

- A product, feature, screen, dashboard, workflow, or module needs UI/UX direction.
- The user asks for design, wireframe, mockup, layout, SaaS UI, product UX, design system direction, or frontend art direction.
- A mockup must become an engineering-ready interaction contract.
- Existing UI needs product-design critique before implementation.
- A rendered UI needs design review after implementation.

Do not use this skill to override product-specific brand or layout rules. Load product-specific skills and runtime binding policies when available.

## Required Inputs

```text
- Product intent or feature goal
- Product blueprint or feature spec
- Target user and user problem
- Existing design system or UI constraints
- Relevant product-specific design rules
- Required output fidelity: brief, flow, wireframe, mockup, critique, or handoff
```

If required context is missing, list the missing context and proceed only with explicit assumptions.

## Process

### 1. Clarify the Design Goal

Define the exact user outcome and product surface.

Output:

- Design goal
- Target user
- User problem
- Success criteria
- Non-goals

### 2. Map the User Flow

Describe how the user moves from entry point to completed outcome.

```text
Entry -> Primary action -> System response -> Review/correction -> Output -> Next action
```

Include alternative paths, empty states, error states, and human review points.

### 3. Define Information Architecture

Prioritize information and actions before visual polish.

Output:

- Page/screen list
- Section hierarchy
- Primary action
- Secondary actions
- Navigation and context markers
- Data requirements per section

### 4. Shape the Layout

Create layout direction at the requested fidelity.

For low fidelity, produce a wireframe. For higher fidelity, produce a mockup direction. For implementation handoff, produce a mockup contract.

Consider:

- Visual hierarchy
- Density and spacing
- Responsive behavior
- Accessibility
- Existing shell/navigation
- Product design system constraints

### 5. Select Component Strategy

Map layout blocks to implementation-friendly components.

Output:

- Component candidates
- State ownership
- Reusable sections
- Design system primitives
- Custom component justification when needed

### 6. Define Interaction Contract

Specify behavior that engineering must implement.

Output:

```text
click behavior:
submit behavior:
validation:
loading state:
empty state:
error state:
success state:
needs_review state:
approved state:
keyboard behavior:
AI/tool behavior:
```

### 7. Produce Engineering Handoff

Turn approved design into implementation-ready instructions.

Output:

- Design brief or mockup contract path
- Files/modules likely affected
- UI acceptance criteria
- Browser/screenshot verification requirements
- Risks and open questions

### 8. Review Rendered Output

When reviewing implemented UI, compare the rendered result against product intent, design contract, design system, and UI verification checklist.

Output:

- What works
- What breaks hierarchy/usability
- Required fixes
- Optional polish
- Verification evidence needed before done

## Output Modes

### Design Brief Mode

Use when direction is still unclear.

Output:

- Product/feature context
- User problem
- Target user
- Scope
- User flow summary
- Required states
- Review criteria

### Wireframe Mode

Use when layout and content priority are needed but visual direction is not locked.

Output:

- Screen structure
- Content hierarchy
- Actions
- State blocks
- Responsive notes

### Mockup Contract Mode

Use when implementation needs precise UI behavior.

Output:

- Screen inventory
- Layout structure
- Component contract
- Interaction behavior
- State contract
- Responsive behavior
- Acceptance criteria
- Verification plan

### Design Review Mode

Use after screenshot, rendered UI, or implementation exists.

Output:

- Product fit
- UX clarity
- Visual hierarchy
- Design system consistency
- Accessibility concerns
- Specific fixes

## Quality Checklist

- [ ] Design supports product intent and user problem.
- [ ] Primary user flow is clear.
- [ ] Information hierarchy is explicit.
- [ ] Required states are covered.
- [ ] Component strategy can be implemented in the approved stack.
- [ ] Accessibility and responsive behavior are considered.
- [ ] Product-specific rules are respected.
- [ ] Handoff includes verification criteria.
- [ ] Mockup does not become a substitute for engineering contract.

## Failure Handling

If the design scope is too broad, reduce it to the smallest useful product surface.

If visual direction is disputed, produce two or three variants with trade-offs instead of mixing them into one unclear design.

If product-specific rules conflict with shared design instincts, product-specific rules win and the conflict should be documented.

If implementation starts before design is approved, keep the change reversible and verify rendered output before claiming done.
