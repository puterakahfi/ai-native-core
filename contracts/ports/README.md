# First-Class Port Contracts

This directory contains canonical machine-readable Native AI Engineering port contracts.

Canonical taxonomy:

```text
integration/
control/
product-surface/
capability-composition/
```

A first-class port is an abstract capability boundary. It is not the capability itself, a generic contract family, an adapter implementation, an adapter binding, or an execution run.

## Validate

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
python3 -m unittest discover -s tests -p 'test_port_inventory.py' -v

python3 scripts/validate-port-adapter-reference.py \
  tests/fixtures/port-adapter-references/valid-model-inference.port-reference.yaml
python3 -m unittest discover -s tests -p 'test_validate_port_adapter_reference.py' -v
```

Schema:

```text
schemas/port-contract.schema.yaml
```

Discovery and migration inventory:

```text
docs/port-inventory.yaml
docs/port-retention-matrix.md
```

## Current contracts

```text
integration/
  code-operation-execution.port.yaml
  database.port.yaml
  model-inference.port.yaml

control/
  agent-runtime.port.yaml
  approval-decision.port.yaml
  authorization-assessment.port.yaml
  context-resolution.port.yaml
  execution-run-management.port.yaml
  review-management.port.yaml
  rule-evaluation.port.yaml
  rule-resolution.port.yaml
  skill-resolution.port.yaml
  workflow-coordination.port.yaml

capability-composition/
  design-strategy-composition.port.yaml
  interaction-composition.port.yaml
  layout-composition.port.yaml
  visual-direction-composition.port.yaml
```

`product-surface/` remains intentionally empty. Assistant, content, creative-rendering, media, learning, template, publishing, and product-output names remain deferred until a universal reusable boundary is demonstrated.

## Boundary locks

`AgentRuntimePort` requires external ExecutionRun, CapacityAssessment, and AuthorizationAssessment references before actual runtime start. Runtime control outcomes do not own ExecutionStatus.

`WorkflowCoordinationPort` coordinates WorkflowDefinition phases, transitions, gates, handoffs, and exits. It deliberately does not create a WorkflowRun aggregate or status family. Actual phase work remains external ExecutionRuns, and concrete workflow-engine operations remain integration concerns.

`CodeExecutionPort` is not retained as one god port. `code-operation-execution` owns bounded actual operation requests and results; ExecutionRun recording, architecture, review, approval, completion, and delivery remain external.

`ToolIntegrationPort` is retired as an umbrella. Gateway translation, direct APIs, authentication, external operation execution, and tool discovery may become independent IntegrationPorts only after separate evidence and review.

Capability-composition ports synthesize and route reusable design methods. They do not own provider bindings, final implementation, review authority, release authorization, or product acceptance.

## Evidence limits

Registration in `contracts/manifest.yaml` proves artifact identity, path, version, and checksum only. A valid adapter reference proves intended compatibility only. Adapter implementation, conformance, runtime behavior, review, approval, completion, and product acceptance require separate evidence.

One-time migration generators and temporary validation workflows may support development, but they must be removed before acceptance. The retained contract tree, schema, permanent validators, tests, generated manifest, inventory, and public documentation are the reviewable source surface.
