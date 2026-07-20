# Agent Runtime Port — Contract Navigation

Status: Explanatory navigation

Canonical first-class contract:

```text
contracts/ports/control/agent-runtime.port.yaml
```

Canonical display name:

```text
AgentRuntimePort
```

## Retained boundary

`AgentRuntimePort` controls one bounded agent-runtime session through a replaceable runtime adapter.

```text
existing ExecutionRun
+ Agent reference
+ RuntimeEnvironment
+ CapacityAssessment
+ AuthorizationAssessment
+ compatible AdapterBinding
→ runtime start or control operation
→ attributable runtime observations
→ external ExecutionRun recording
```

The port may request start, inspect, pause, resume, or stop operations. It does not own the canonical execution lifecycle.

## Required distinctions

```text
AgentRuntimePort
≠ Agent entity ownership
≠ workflow definition
≠ ExecutionRun management
≠ ExecutionStatus
≠ model inference
≠ tool execution
≠ review
≠ approval
≠ completion
≠ product acceptance
```

Only an actual host/runtime start observation can support transition of an external ExecutionRun into `running`. A runtime request, generated plan, or model response cannot.

Starting or resuming material agent execution requires a current action-specific authorization assessment. Tool registration or provider permission does not create authority.

## Runtime events

Runtime events are observations intended for attributable external recording. They do not silently mutate ExecutionStatus, become evidence without scope and method, or prove broader completion.

## Adapter examples

Potential adapters include Hermes, hosted agent platforms, local agent runtimes, graph runtimes, or custom execution surfaces. These examples are implementation candidates, not canonical defaults.

`native-ai-fw` owns concrete runtime binding and control-plane implementation. Core owns the runtime-agnostic boundary only.

## Dashboard usage

A dashboard may display runtime instance, agent, ExecutionRun reference, observed capabilities, events, blockers, and external review or approval references together. It must not serialize them as one generic status.

## Authority

The versioned port contract and generated manifest are machine authority. This document explains the boundary and does not define competing request, response, status, or compatibility semantics.
