# Workflow Orchestration Port — Legacy Navigation

Status: Superseded explanatory document

Canonical first-class contract:

```text
contracts/ports/control/workflow-coordination.port.yaml
```

Canonical display name:

```text
WorkflowCoordinationPort
```

Legacy migration alias:

```text
workflow-orchestration
```

## Why the boundary changed

The earlier `WorkflowOrchestrationPort` mixed:

```text
WorkflowDefinition coordination
workflow-engine control
actual step execution
retry and cancellation
ExecutionRun lifecycle
review and approval waiting
completion reporting
```

The canonical domain model defines `WorkflowDefinition` and `ExecutionRun`, but it does not define a separate `WorkflowRun` aggregate or status family. A port contract may not invent that lifecycle silently.

The retained control boundary is therefore workflow coordination:

```text
accepted WorkflowDefinition
+ attributable trigger
+ ContextPack
+ external gate, execution, review, and approval references
→ phase and transition selection
→ handoff records
→ exit-condition results
→ bounded coordination checkpoint
```

## Required distinctions

```text
WorkflowCoordinationPort
≠ WorkflowDefinition ownership
≠ workflow-engine runtime control
≠ ExecutionRun management
≠ skill execution
≠ gate evaluation
≠ review
≠ approval
≠ completion
≠ delivery
≠ product acceptance
```

A selected transition is not actual execution. Phase execution is recorded through external ExecutionRuns. A pending review, approval, handoff, or exit condition cannot be reported as workflow completion.

## Runtime-engine integrations

Temporal, n8n, GitHub Actions, queues, schedulers, and similar systems remain possible execution-plane integrations. Their start, pause, resume, retry, cancellation, provider state, and transport semantics require a narrower integration boundary or adapter contract. They are not owned by `WorkflowCoordinationPort`.

## Handoffs and gates

Every handoff preserves:

```text
sender
receiver
transferred artifact, context, evidence, or state references
acceptance condition
acceptance evidence
limitations
```

Every transition names the governing TransitionRule and applicable GateResult references. Coordination consumes external review and authority-bearing approval records without producing them.

## Migration

Consumers of `WorkflowOrchestrationPort` should migrate to `workflow-coordination` when they need phase, transition, gate, handoff, or exit coordination.

Consumers that need concrete workflow-engine execution must use or propose a separate integration boundary instead of expanding this control port.

## Authority

The versioned port contract and generated manifest are machine authority. This Markdown document remains only as migration and architectural explanation.
