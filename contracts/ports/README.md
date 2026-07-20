# First-Class Port Contracts

This directory contains canonical machine-readable Native AI Engineering port contracts.

Canonical taxonomy:

```text
integration/
control/
product-surface/
capability-composition/
```

A first-class port is an abstract capability boundary. It is not the capability itself, the stable contract family in general, an adapter implementation, an adapter binding, or an execution run.

Validate all port contracts:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
```

Schema:

```text
schemas/port-contract.schema.yaml
```

Current representative contracts:

```text
integration/model-inference.port.yaml
control/execution-run-management.port.yaml
capability-composition/visual-direction-composition.port.yaml
```

`product-surface/` remains intentionally empty until issue `#7` confirms a universal reusable product-surface boundary.

Registration in `contracts/manifest.yaml` proves artifact identity, path, version, and checksum only. Adapter implementation, conformance, runtime behavior, review, approval, and product acceptance require separate evidence.
