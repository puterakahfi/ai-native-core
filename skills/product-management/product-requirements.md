# Product Requirements Skill Contract

## Purpose

Define the runtime-agnostic contract for authoring and verifying Product Requirements Documents (PRDs).

A PRD is the **Spec / The What** bridge between product discovery and implementation planning. It captures what should be built, why it matters, who it serves, how success will be measured, and what evidence must prove it is done.

## Boundary

Core owns:

- required PRD sections
- product/spec quality gates
- acceptance criteria and traceability requirements
- launch-readiness expectations

Adapters own:

- concrete PRD file format
- stakeholder approval workflow
- task tracker integration
- evidence storage
- product-specific template details

## Lifecycle Placement

```text
product discovery
  ↓
product requirements / PRD
  ↓
MVP planning
  ↓
technical spec
  ↓
implementation
  ↓
acceptance verification
  ↓
release / launch
```

## Required Inputs

- `product_or_feature_intent` — what outcome or feature is being considered.
- `target_users` — who needs it.
- `problem_statement` — what problem must be solved.

Optional inputs include research, business goals, technical/design constraints, market context, stakeholder feedback, and launch constraints.

## Required PRD Sections

A compliant PRD must include:

- title
- problem statement
- target users
- goals
- non-goals
- success metrics
- scope in
- scope out
- user stories or jobs-to-be-done
- functional requirements
- non-functional requirements
- acceptance criteria
- constraints
- dependencies
- risks
- open questions
- launch criteria

## Quality Gates

- Problem statement names a user or business outcome, not a preselected solution.
- Target users are explicit.
- Goals and non-goals both exist.
- Success metrics are measurable.
- Scope-in and scope-out both exist.
- Requirements are testable or trace to testable acceptance criteria.
- Acceptance criteria are verifiable.
- Non-functional requirements include reliability, security, or performance when relevant.
- Constraints and dependencies are explicit.
- Open questions are named, not hidden.
- Launch criteria define readiness, not just implementation completion.
- Implementation details are excluded unless they are constraints.

## Traceability

PRD output should preserve links:

```text
requirement → acceptance criterion → verification evidence
```

Recommended downstream links:

```text
PRD → MVP slice → technical spec → task → test/evidence
```

## Adapter Expectations

A runtime adapter should render the PRD in the product's preferred format and make approval/evidence requirements explicit. It should not silently convert vague goals into implementation tasks.
