# Native AI Core Contract Catalog

This document explains how to browse the public contracts without duplicating the generated inventory in multiple human-maintained tables.

## Canonical inventory

[`contracts/manifest.yaml`](../contracts/manifest.yaml) is the authoritative registry of contract artifacts. It records registered IDs, paths, checksums, and skill-contract versions where applicable.

The manifest is generated from repository contents:

```bash
./scripts/generate-manifest.sh
```

Do not hand-edit the manifest. Regenerate it after any contract content, path, filename, or version change and commit the resulting diff.

A manifest entry proves that an artifact is registered at a specific path and checksum. It does not, by itself, prove runtime implementation, adapter conformance, production maturity, or product adoption.

## Inventory structure

```text
contracts/
├── skills/<category>/*.contract.yaml
├── workflows/*.contract.yaml
├── runtime/*.contract.yaml
├── tests/*.test.yaml
└── manifest.yaml
```

### Skill contracts

Skill contracts define reusable capability interfaces. They describe required inputs, allowed outputs, quality gates, roles, and explicit boundaries without choosing a runtime implementation.

Browse [`contracts/skills/`](../contracts/skills/) by domain category:

- architecture
- content
- context
- design
- engineering
- governance
- meta
- product
- quality
- runtime
- security
- visual thinking

The directory structure and generated manifest are authoritative when a category list in prose becomes stale.

### Workflow contracts

[`contracts/workflows/`](../contracts/workflows/) defines ordered lifecycle agreements. Workflow contracts focus on phases, gates, handoffs, evidence, and exit conditions rather than one atomic capability.

### Runtime contracts

[`contracts/runtime/`](../contracts/runtime/) defines runtime-facing agreements such as core resolution, project context, execution loops, memory, hooks, tool registration, and standard operating procedures.

Runtime contracts remain implementation-agnostic. Provider commands, deployment policy, credentials, and product-specific runtime state belong in adapters or product repositories.

### Behavioral test contracts

[`contracts/tests/`](../contracts/tests/) contains behavioral evaluation cases used by the `skill-eval` runner.

A test contract defines realistic triggers, required behavior, prohibited behavior, ordering constraints, and the quality gates under evaluation. It is not a unit test for a specific model provider.

## Finding the right contract

Use this sequence:

```text
1. Identify the capability or lifecycle that must remain stable.
2. Search contracts/manifest.yaml by ID or path.
3. Open the contract and inspect inputs, outputs, quality gates, and boundary.
4. Inspect adjacent port and architecture documentation when the contract delegates work.
5. Locate the executable adapter in ai-native-skills or the owning runtime/product repository.
6. Verify the adapter's pinned contract version and conformance evidence.
```

Start with these framework documents when the required contract is unclear:

- [Architecture v0.2](architecture-v0.2.md)
- [Ports and adapters](ports-and-adapters.md)
- [Port taxonomy](port-taxonomy.md)
- [Domain-driven model](domain-driven-model.md)
- [Glossary](glossary.md)

## Contract identity and maturity

Contracts declare versions independently. Maturity is evaluated per contract, not inferred from repository age or manifest presence.

General interpretation:

```text
0.x   evolving or pre-stable contract; a minor bump may be incompatible
1.x+  semantic-version compatibility line; breaking changes require a new major version
```

Adapter compatibility depends on the declared pin:

```text
^1.2.0  accepts compatible versions in major line 1
^0.2.0  accepts compatible patches in the 0.2 line
~1.2    accepts versions in the 1.2 line
```

The repository validator is the source of truth for supported pin semantics. See [`scripts/validate-implements.sh`](../scripts/validate-implements.sh).

Do not label a contract production-stable solely because its version is `1.0.0`. Maturity also requires coherent boundaries, review, compatible adapters, and appropriate validation evidence.

## Core-to-adapter relationship

```text
ai-native-core
  declares capability, boundary, contract version, and quality gates
        ↓ implemented by
ai-native-skills
  executable reusable skill and workflow adapters
        ↓ orchestrated or specialized by
native-ai-fw and product repositories
  runtime adapters, product policies, provider bindings, and real-world validation
```

A private or product-specific implementation may consume a public core contract without publishing its internal context. Core remains free of credentials, customer data, deployment configuration, and runtime-installed copies.

## Keeping the catalog current

When adding, moving, deleting, or changing a contract:

1. update the contract version according to compatibility impact;
2. update affected public documentation;
3. regenerate `contracts/manifest.yaml`;
4. inspect the contract version and manifest path, checksum, and total changes;
5. validate dependent adapters when available;
6. disclose adapters or products that still require migration.

Human-readable summary tables should link to the generated manifest rather than attempt to become a second inventory authority.