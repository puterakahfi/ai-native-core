# Experience Design Workflow

## Purpose

Define how a product or feature moves from blueprint to implementation-ready design inside the Native AI Framework.

Experience Design is the bridge between product intent and engineering contract. It turns a product idea into user flows, information architecture, mockups, interaction behavior, and UI states that an engineering agent can implement without guessing.

## Position in the Framework

```text
Intent
-> Blueprint
-> Experience Design
-> Engineering Contract
-> Implementation
-> Verification
-> Deployment
```

Experience Design should happen before broad implementation and before final engineering contract decisions that depend on user experience, screen structure, or interaction behavior.

## Workflow

```text
Design Request
-> Intent Alignment
-> User Flow
-> Information Architecture
-> Wireframe
-> Mockup
-> Interaction Contract
-> Design Review
-> Engineering Handoff
```

## 1. Design Request

Capture the design problem without over-building a dashboard or implementation.

Output:

- Feature or surface name
- User problem
- Target user
- Product area
- Design fidelity needed: sketch, wireframe, mockup, or implementation-ready contract

## 2. Intent Alignment

Check that the design supports product intent and blueprint.

Questions:

```text
- Which user problem does this design solve?
- Which success metric does it support?
- Is this MVP, beta, or later scale work?
- What should not be designed yet?
```

Output:

- Intent alignment note
- Non-goals
- Scope boundary

## 3. User Flow

Define how the user moves through the feature.

Output:

- Entry point
- Main path
- Alternative paths
- Empty, error, loading, success, and review states
- Human approval or correction points

## 4. Information Architecture

Define what information appears where and in what priority.

Output:

- Page or screen list
- Section hierarchy
- Primary and secondary actions
- Navigation and breadcrumbs
- Data dependencies per screen

## 5. Wireframe

Create low-fidelity layout before visual polish.

Output:

- Layout blocks
- Content hierarchy
- Component candidates
- Responsive constraints
- Accessibility considerations

## 6. Mockup

Create higher-fidelity visual direction only as needed.

Output:

- Visual layout
- Component choices
- Density and spacing notes
- Brand or product style constraints
- Variants when direction is still uncertain

## 7. Interaction Contract

Convert the design into implementation behavior.

Output:

- Click/submit/keyboard behavior
- Form validation
- State transitions
- Error handling
- AI/tool interaction points when applicable
- Acceptance criteria for rendered UI

## 8. Design Review

Review design against product intent, rules, and existing design system.

Output:

- Approved direction or requested changes
- Risks and trade-offs
- Accessibility or usability notes
- Final design artifact path

## 9. Engineering Handoff

Translate the approved design into an engineering-ready contract.

Output:

- Updated engineering contract if needed
- Implementation task
- Required files/modules
- UI verification checklist
- Browser/screenshot verification requirement

## Shared Skill

Use `skills/experience-design/master-design.md` for shared Senior Product Designer, SaaS UI/UX Designer, Design Systems Specialist, and Frontend Art Director behavior.

Product-specific design direction should be layered from `products/<product-id>/skills/` and must not be hardcoded into this shared workflow.

## Native AI Agent Behavior

When Hermes or another agent executes this workflow:

1. Read product config and relevant source-of-truth files first.
2. Prefer lightweight markdown artifacts before polished visuals.
3. Generate 2-3 variants only when the direction is uncertain.
4. Ask for design approval before implementation when fidelity or product direction is unresolved.
5. Turn approved design into an engineering task before coding.
6. Verify rendered UI with browser output or screenshot after implementation.

## Done Criteria

- [ ] Design supports product intent and blueprint.
- [ ] User flow is defined.
- [ ] Information architecture is clear.
- [ ] Wireframe or mockup exists at the requested fidelity.
- [ ] Interaction contract covers loading, empty, error, success, and review states.
- [ ] Design was reviewed or explicitly accepted.
- [ ] Engineering handoff is implementation-ready.
- [ ] UI verification requirements are stated.
