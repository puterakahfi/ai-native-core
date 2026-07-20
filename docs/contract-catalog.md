# Native AI Core Contract Catalog

This document explains how to browse public contracts without duplicating the generated inventory in human-maintained tables.

## Canonical inventory

[`contracts/manifest.yaml`](../contracts/manifest.yaml) is the authoritative registry of contract artifacts. It records registered IDs, paths, versions where supported, and checksums.

Generate it with:

```bash
./scripts/generate-manifest.sh
```

Do not hand-edit the manifest. A manifest entry proves registration at one path and checksum. It does not prove adapter implementation, runtime behavior, conformance, maturity, or product adoption.

## Inventory structure

```text
contracts/
├── skills/<category>/*.contract.yaml
├── ports/<kind>/*.port.yaml
├── workflows/*.contract.yaml
├── runtime/*.contract.yaml
├── tests/*.test.yaml
└── manifest.yaml
```

### Skill contracts

[`contracts/skills/`](../contracts/skills/) defines reusable capability agreements: inputs, outputs, gates, roles, and owned/delegated boundaries.

A skill contract is not automatically a port. Legacy `skill_contract.type: port` artifacts remain explicit migration inputs until issue `#7` moves their stable boundaries into first-class port contracts.

### Port contracts

[`contracts/ports/`](../contracts/ports/) defines versioned capability boundaries between consumer contexts and replaceable adapters or composition facades.

Kinds:

```text
integration
control
product-surface
capability-composition
```

Port contracts are validated by:

```bash
python3 scripts/validate-port-contracts.py
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
```

The schema and semantic checks validate declared structure and boundary consistency. They do not prove adapter behavior.

### Workflow contracts

[`contracts/workflows/`](../contracts/workflows/) defines ordered lifecycle agreements with phases, gates, handoffs, evidence, and exit conditions.

### Runtime contracts

[`contracts/runtime/`](../contracts/runtime/) defines runtime-facing implementation-agnostic agreements such as core resolution, execution methods, memory, hooks, tool registration, and operating procedures.

### Behavioral test contracts

[`contracts/tests/`](../contracts/tests/) contains behavioral evaluation cases consumed by the evaluation runner.

## Finding the right contract

```text
1. Identify the capability, boundary, or lifecycle that must remain stable.
2. Search contracts/manifest.yaml by ID or path.
3. Determine whether the artifact is a skill, port, workflow, runtime, or test contract.
4. Inspect inputs/interactions, outputs/responses, failures, gates, and boundaries.
5. Inspect canonical domain and port documentation.
6. Locate executable adapters in ai-native-skills, native-ai-fw, or product repositories.
7. Verify path, version pin, declaration conformance, runtime evidence, and product evidence separately.
```

Start with:

- [Canonical domain model](domain-model/README.md)
- [Port taxonomy](port-taxonomy.md)
- [Port retention matrix](port-retention-matrix.md)
- [Ports and adapters](ports-and-adapters.md)
- [Architecture v0.2](architecture-v0.2.md)
- [Glossary](glossary.md)

## Contract identity and maturity

```text
0.x   evolving or pre-stable contract; a minor bump may be incompatible
1.x+  semantic-version compatibility line; breaking changes require a new major version
```

Compatibility depends on actual pins and validation results, not the version label alone.

A contract can be registered and schema-valid while still lacking:

```text
compatible adapter;
behavioral conformance;
runtime evidence;
review or approval;
product validation;
production adoption.
```

## Core-to-adapter relationship

```text
ai-native-core
  canonical domain, port, and contract agreement
        ↓ implemented by
ai-native-skills, native-ai-fw, or provider/framework adapters
  executable or concrete behavior
        ↓ specialized and validated by
product repositories
  product policy, binding, implementation, and field evidence
```

## Keeping the catalog current

When adding, moving, deleting, or changing a contract:

1. classify compatibility impact;
2. update the contract version;
3. update affected canonical documentation;
4. run the applicable schema and semantic validators;
5. regenerate `contracts/manifest.yaml`;
6. inspect IDs, paths, versions, checksums, family placement, and total count;
7. validate dependent adapters when available;
8. disclose migrations and evidence gaps.

Human-readable tables should explain meaning and migration, not compete with the generated manifest.
