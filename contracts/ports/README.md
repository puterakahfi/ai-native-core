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

Validate contracts and adapter references:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v

python3 scripts/validate-port-adapter-reference.py \
  tests/fixtures/port-adapter-references/valid-model-inference.port-reference.yaml
python3 -m unittest discover -s tests -p 'test_validate_port_adapter_reference.py' -v
```

Schema:

```text
schemas/port-contract.schema.yaml
```

Current contracts:

```text
integration/
  model-inference.port.yaml

control/
  execution-run-management.port.yaml
  agent-runtime.port.yaml
  workflow-coordination.port.yaml
  context-resolution.port.yaml
  skill-resolution.port.yaml
  rule-resolution.port.yaml
  rule-evaluation.port.yaml
  review-management.port.yaml
  approval-decision.port.yaml
  authorization-assessment.port.yaml

capability-composition/
  visual-direction-composition.port.yaml
```

`AgentRuntimePort` requires external ExecutionRun, CapacityAssessment, and AuthorizationAssessment references before actual runtime start. Runtime control outcomes do not own ExecutionStatus.

`WorkflowCoordinationPort` coordinates WorkflowDefinition phases, transitions, gates, handoffs, and exits. It deliberately does not create a WorkflowRun aggregate or status family. Actual phase work remains external ExecutionRuns, and concrete workflow-engine operations remain integration concerns.

`product-surface/` remains intentionally empty until issue `#7` confirms a universal reusable product-surface boundary.

Registration in `contracts/manifest.yaml` proves artifact identity, path, version, and checksum only. Adapter implementation, conformance, runtime behavior, review, approval, and product acceptance require separate evidence.

One-time migration generators and temporary validation workflows may support development, but they must be removed before acceptance. The retained contract tree, schema, permanent validators, tests, generated manifest, and public documentation are the reviewable source surface.
