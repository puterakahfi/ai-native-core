# Business Value Alignment

Business value alignment is the runtime-agnostic capability for deciding whether work is worth doing, what value it should create, how that value will be measured, and whether the agent should proceed, experiment, or stop.

It is formalized by:

```text
contracts/skills/business/business-value-alignment.contract.yaml
```

## Purpose

Use this capability before turning a request into execution when the value, priority, or success definition is unclear.

It answers:

- who benefits from this work?
- what user value is created?
- what business value is created or learned?
- how will success be measured?
- what assumptions must be true?
- what risks could make the work not worth doing?
- should the team continue, run an experiment, narrow scope, or stop?

## Boundary

This contract owns value framing and value evidence. It does not own:

- PRD authoring; use `product-requirements`.
- task breakdown; use `product-manager` or a workflow.
- architecture decisions; use `adr`, `master-engineer`, or architecture skills.
- instrumentation implementation; product adapters define concrete analytics tooling.

## Required Behavior

1. Start with user value before proposing a solution.
2. Map user value to business value, learning value, or strategic value.
3. Define measurable signals: leading, lagging, and guardrail metrics.
4. Label claims as known, assumed, or unknown.
5. State risks and assumptions that could invalidate the work.
6. End with an explicit verdict: continue, narrow scope, experiment first, or stop.

## Output Shape

```markdown
# Business Value Alignment

## Request
<what was asked>

## User Value
<who benefits and how>

## Business Value
<why this matters strategically, commercially, operationally, or as learning>

## Metrics
- Leading:
- Lagging:
- Guardrail:

## Evidence Labels
- Known:
- Assumed:
- Unknown:

## Risks
- <risk + mitigation>

## Recommendation
Verdict: CONTINUE | NARROW_SCOPE | EXPERIMENT_FIRST | STOP
Rationale: <why>
Next gate: <what must be approved or verified next>
```

## Quality Gates

- User value is explicit before solution recommendation.
- Business value maps to a metric or learning goal.
- Metrics distinguish leading, lagging, and guardrail signals.
- Assumptions and risks are explicit.
- Low-value or unclear-value work is flagged before build.
- Verdict is explicit.
