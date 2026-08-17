# Native AI Core Contract Catalog

This document explains how to find and interpret public contracts without duplicating the generated registry in hand-maintained tables.

Schema architecture:

```text
docs/contract-schema-architecture.md
```

Workflow migration decisions:

```text
docs/workflow-contract-migration.yaml
```

## Canonical inventory

[`contracts/manifest.yaml`](../contracts/manifest.yaml) is the authoritative generated registry. Every entry records:

```text
contract ID
contract kind
schema version
schema path
canonical artifact path
contract version
checksum
```

Generate it with:

```bash
./scripts/generate-manifest.sh
```

The generator parses declared YAML schema identity. It does not infer contract kind from a directory alone or extract version using text matching.

Do not hand-edit the manifest.

## Contract document identity

Every active artifact declares:

```yaml
contract_schema:
  kind: workflow_contract
  version: "1.0.0"
  path: schemas/workflow-contract.schema.yaml

workflow_contract:
  id: example-workflow
  version: "1.0.0"
```

```text
schema version
≠ contract version
```

The family root owns contract meaning. The schema identity selects its structural agreement.

## Inventory structure

```text
contracts/
├── skills/<category>/*.contract.yaml
├── ports/<kind>/*.port.yaml
├── workflows/*.contract.yaml
├── runtime/*.contract.yaml
├── domains/*.contract.yaml
├── tests/*.test.yaml
├── compatibility/*.contract.yaml
└── manifest.yaml
```

### Skill contracts

[`contracts/skills/`](../contracts/skills/) defines reusable executable capability methods: inputs, outputs, roles, gates, and owned or delegated boundaries.

Internal procedure phases do not automatically make a skill a workflow. `design-review` and `systematic-debugging` remain skills because their phases describe one bounded expert method.

Four legacy design composition artifacts still declare `type: port` as compatibility sources. Their first-class port contracts remain authoritative.

### Workflow contracts

[`contracts/workflows/`](../contracts/workflows/) defines sequenced lifecycles coordinating phases with transitions, gates, handoffs, exit conditions, skills, or ownership changes.

Canonical location and root:

```text
contracts/workflows/<id>.contract.yaml
workflow_contract
```

Migrated lifecycle contracts:

```text
design-refinement
redesign-workflow
skill-evolution
development-loop
```

`development-loop` uses `workflow_kind: execution_method`. It remains an engineering execution method, not a product workflow or the canonical domain lifecycle.

A WorkflowDefinition is not actual execution, a workflow-engine session, or an ExecutionRun.

### Port contracts

[`contracts/ports/`](../contracts/ports/) defines versioned capability boundaries between consumer contexts and replaceable adapters or composition facades.

Kinds:

```text
integration
control
product-surface
capability-composition
```

Port-specific semantic validation remains active in addition to the unified family schema pipeline.

```text
AgentRuntimePort runtime observation
≠ ExecutionStatus

WorkflowCoordinationPort checkpoint
≠ WorkflowRun aggregate
```

### Domain contracts

[`contracts/domains/`](../contracts/domains/) defines runtime-agnostic domain meaning, ownership boundaries, and invariants that must remain stable across consuming products, control planes, and runtime adapters.

Canonical location and root:

```text
contracts/domains/<id>.contract.yaml
domain_contract
```

A domain contract may reference existing ports for delegated capabilities without redefining their interaction semantics. Domain schema validity establishes structural conformance only; it does not prove implementation, runtime behavior, review, approval, or product acceptance.

### Runtime contracts

[`contracts/runtime/`](../contracts/runtime/) defines runtime-facing agreements such as core resolution, memory, hooks, tool registration, and operating procedures.

Runtime contracts do not own ordered workflow lifecycles after schema v1 migration. They do not replace ports or create authority by themselves.

### Behavioral test contracts

[`contracts/tests/`](../contracts/tests/) contains behavioral evaluation cases consumed by `scripts/run-eval.py`.

The compatibility body root remains `skill_test`; the declared schema kind is `behavioral_test_contract`.

### Compatibility manifests

[`contracts/compatibility/`](../contracts/compatibility/) records governed migration references such as legacy path aliases.

Current workflow aliases:

```text
contracts/skills/quality/design-refinement.contract.yaml
→ contracts/workflows/design-refinement.contract.yaml

contracts/skills/quality/redesign-workflow.contract.yaml
→ contracts/workflows/redesign-workflow.contract.yaml

contracts/skills/quality/skill-evolution.contract.yaml
→ contracts/workflows/skill-evolution.contract.yaml

contracts/runtime/development-loop.contract.yaml
→ contracts/workflows/development-loop.contract.yaml
```

The canonical target is the only machine authority. Alias resolution does not prove downstream migration or adapter conformance.

## Finding the right contract

```text
1. Identify the stable domain, capability, lifecycle, runtime surface, boundary, or test.
2. Search contracts/manifest.yaml by ID, kind, or path.
3. Open the declared schema and family body.
4. Inspect inputs, outputs, interactions, gates, failures, boundaries, and compatibility.
5. Verify referenced domain objects and status families against the canonical domain model.
6. Resolve legacy paths through compatibility manifests.
7. Locate executable adapters in ai-native-skills, ai-native-fw, or products.
8. Verify schema, path, version, conformance, runtime evidence, and product evidence separately.
```

Start with:

- [Canonical domain model](domain-model/README.md)
- [Contract schemas](../schemas/README.md)
- [Port taxonomy](port-taxonomy.md)
- [Ports and adapters](ports-and-adapters.md)
- [Adapter conformance](adapter-conformance.md)
- [Architecture v0.2](architecture-v0.2.md)
- [Glossary](glossary.md)

## Validation

```bash
python3 scripts/validate-contract-schemas.py
python3 scripts/validate-contract-identity.py
python3 scripts/validate-port-contracts.py
python3 scripts/run-eval.py --all --validate-tests

python3 -m unittest discover -s tests -p 'test_validate_contract_schemas.py' -v
python3 -m unittest discover -s tests -p 'test_contract_resolution.py' -v
```

Generated metadata:

```bash
./scripts/generate-manifest.sh
python3 scripts/inventory-contract-schemas.py
```

## Contract identity and maturity

```text
0.x   evolving or pre-stable contract; a minor bump may be incompatible
1.x+  semantic-version compatibility line; breaking changes require a new major version
```

Compatibility depends on actual pins, aliases, and validation results—not the version label alone.

A contract can be registered and schema-valid while still lacking:

```text
compatible adapter
behavioral conformance
runtime evidence
review or approval
product validation
production adoption
```

## Keeping the catalog current

When adding, moving, deleting, or changing a contract:

1. classify contract kind and schema version;
2. classify semantic and compatibility impact;
3. verify referenced objects and statuses against the domain model;
4. update contract version where required;
5. add or retire migration aliases explicitly;
6. run unified and family-specific validators;
7. regenerate manifest and discovery reports;
8. validate dependent adapters and path pins;
9. disclose remaining evidence gaps.

Human-readable documentation explains meaning and migration. It does not compete with the generated manifest or family contract artifacts.
