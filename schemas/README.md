# Schemas

This directory contains reusable validation schemas connected to real artifacts and validator paths.

## Active schema

```text
schemas/port-contract.schema.yaml
```

Validates:

```text
contracts/ports/**/*.port.yaml
```

Validation path:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
```

The port schema validates structural completeness for:

```text
identity and version;
port kind and direction;
semantic and binding ownership;
boundary ownership and delegation;
requests, responses, events, and streams;
structured failures;
typed state transitions;
authorization invariants;
idempotency;
observability;
adapter contract references;
compatibility and breaking-change declarations;
quality gates.
```

The semantic validator additionally checks filename/ID alignment, kind-directory alignment, disjoint boundaries, one owned status family, authorization consistency, duplicate interaction IDs, aliases, and legacy contract references.

Schema or validator success does not prove:

```text
adapter implementation;
runtime behavior;
review or approval;
product fitness;
production maturity;
field adoption.
```

## Planned unified schemas

Issue `#8` owns unified schema direction for the remaining contract families and may absorb or reference the accepted port schema without collapsing port-specific semantics.

```text
skill-contract.schema.yaml
workflow-contract.schema.yaml
test-contract.schema.yaml
runtime-contract.schema.yaml
```

Do not add an unused schema without a real artifact, fixtures, validator path, and documented evidence boundary.
