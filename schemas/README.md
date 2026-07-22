# Contract Schemas

This directory contains the canonical JSON Schema registry for Native AI Engineering contract artifacts.

Architecture authority:

```text
docs/contract-schema-architecture.md
```

Discovery evidence:

```text
docs/contract-schema-discovery.yaml
```

## Contract envelope

Every active artifact declares its schema identity beside its family-owned body:

```yaml
contract_schema:
  kind: skill_contract
  version: "1.0.0"
  path: schemas/skill-contract.schema.yaml

skill_contract:
  id: example
  version: "1.0.0"
  # family-owned fields
```

Required distinction:

```text
schema version
≠ contract version
≠ adapter compatibility version
≠ product release version
```

## Active schemas

```text
common.schema.yaml
skill-contract.schema.yaml
workflow-contract.schema.yaml
runtime-contract.schema.yaml
port-contract.schema.yaml
behavioral-test-contract.schema.yaml
compatibility-manifest.schema.yaml
contract-manifest.schema.yaml
```

Supporting fixture-backed schemas:

```text
adapter-manifest.schema.yaml
domain-contract.schema.yaml
```

A supporting schema does not prove an active adapter or domain artifact exists. It defines the required shape for future first-class artifacts and is validated through positive and negative fixtures.

## Canonical family roots

```text
skill_contract
workflow_contract
runtime_contract
port_contract
skill_test
compatibility_manifest
```

`skill_test` remains the behavioral-test body root for compatibility; its schema kind is `behavioral_test_contract`.

Canonical workflow location:

```text
contracts/workflows/<id>.contract.yaml
```

Lifecycle workflows must not remain serialized as `skill_contract type: workflow` or as runtime contracts owning phase-transition lifecycles.

## Shared primitives and extensions

`common.schema.yaml` defines only primitives whose meaning is stable across families:

```text
schema identity
contract and machine identifiers
workflow phase identifiers
semantic versions
contract and schema paths
string lists
quality-gate identifiers
workflow phases and transitions
compatibility aliases
```

Family schemas own family invariants. Domain-specific structures remain explicit extensions under their owning family and are not normalized merely because they share names such as `evidence`, `approval`, `transition`, or `boundary`.

```text
shared serialization
≠ shared domain meaning
```

## Validation

Run the full repository pipeline:

```bash
python3 scripts/validate-contract-schemas.py
python3 scripts/validate-contract-identity.py
python3 scripts/validate-port-contracts.py
python3 scripts/run-eval.py --all --validate-tests

python3 -m unittest discover -s tests -p 'test_validate_contract_schemas.py' -v
python3 -m unittest discover -s tests -p 'test_contract_resolution.py' -v
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
```

Regenerate schema-aware metadata:

```bash
./scripts/generate-manifest.sh
python3 scripts/inventory-contract-schemas.py
```

`Contract integrity` CI validates schemas, family/path identity, workflow references, compatibility aliases, port semantics, behavioral tests, fixtures, manifest parity, checksums, and discovery drift.

## Compatibility

Moved contract paths are recorded in:

```text
contracts/compatibility/contract-path-aliases.contract.yaml
```

Resolvers prefer the canonical path and may resolve an active legacy alias during migration.

```text
path alias
≠ duplicate contract
≠ adapter conformance
≠ runtime compatibility proof
```

## Evidence boundary

Schema success proves structural conformance to one declared schema version. It does not prove:

```text
semantic usefulness
adapter implementation
behavioral conformance
runtime execution
review or approval
completion
product fitness
production adoption
```

Do not add an unused schema without a real artifact or explicit fixture-backed future boundary, validator coverage, migration behavior, and documented evidence limits.
