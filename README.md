# Native AI Core

Native AI Core is the public, runtime-agnostic contract layer for AI-native engineering.

It defines the shared domain model, architecture boundaries, ports, lifecycle agreements, rules, templates, and quality contracts that executable skills, runtime adapters, and product adapters implement.

Core describes **what must remain stable**. Adapters decide **how it is implemented**.

## Start here

| You are | Start with |
|---|---|
| Reading the framework architecture | [Architecture v0.2](docs/architecture-v0.2.md) |
| Looking for a capability or lifecycle contract | [Contract catalog](docs/contract-catalog.md) |
| Implementing a skill adapter | [Adapter implementation path](#implement-a-contract) |
| Building a runtime or product adapter | [Repository boundaries](#repository-boundaries) and [ports and adapters](docs/ports-and-adapters.md) |
| Checking terminology | [Glossary](docs/glossary.md) |
| Contributing a contract, document, rule, schema, or template | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Inspecting the generated inventory | [contracts/manifest.yaml](contracts/manifest.yaml) |

## Architecture position

```text
ai-native-core
  canonical domain language, ports, contracts, boundaries, and quality standards
        ↓ implemented as executable reusable behavior
ai-native-skills
  skills, workflows, reviewers, references, and behavioral evaluation
        ↓ orchestrated or specialized by
native-ai-fw and product repositories
  runtime adapters, provider bindings, product policy, implementation, and validation
```

The design rule is simple:

```text
Domain defines capability.
Port describes capability.
Contract defines the stable agreement.
Adapter implements the agreement.
Provider and product choices remain replaceable.
```

See [Architecture v0.2](docs/architecture-v0.2.md), [ports and adapters](docs/ports-and-adapters.md), and [port taxonomy](docs/port-taxonomy.md) for the complete framework model.

## Repository boundaries

### Native AI Core owns

- runtime-agnostic domain concepts and terminology;
- public skill, workflow, runtime, evaluation, and port contracts;
- architecture boundaries and delegation rules;
- reusable rules and generic templates;
- public framework and port documentation;
- generated contract identity and checksum metadata.

### Native AI Core does not own

```text
private product context or customer data
credentials and deployment secrets
provider-specific commands or implementation
runtime-installed profile state
private screenshots and product assets
application-specific business policy
copies of installed runtime skills
```

Those concerns belong in executable skill adapters, `native-ai-fw`, provider adapters, or product repositories.

## Implement a contract

### 1. Resolve core

Consume core through the dependency strategy appropriate to the adapter repository, such as a submodule, vendored source, or pinned package.

Example submodule setup:

```bash
git submodule add https://github.com/puterakahfi/ai-native-core.git core
```

### 2. Select the contract

Search [`contracts/manifest.yaml`](contracts/manifest.yaml) by ID or path, then inspect the contract's:

- inputs;
- outputs;
- quality gates;
- roles;
- `covers` boundary;
- `does_not_cover` delegation;
- version.

### 3. Declare the implementation

An executable skill adapter identifies the core contract and pins a compatible version:

```yaml
name: native-ai-runtime-agent
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/native-ai-runtime-agent.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
```

The contract path and version pin are evidence of intent, not proof of full conformance.

### 4. Validate the adapter

From the adapter repository:

```bash
../ai-native-core/scripts/validate-implements.sh ../ai-native-core

python3 ../ai-native-core/scripts/validate-conformance.py \
  ../ai-native-core \
  .
```

The first command checks contract path and version compatibility. The second checks whether adapter content covers required gates, inputs, outputs, and boundaries.

### 5. Validate behavior

Behavioral evaluation contracts live under `contracts/tests/` and run through:

```bash
python3 scripts/run-eval.py --all --validate-tests
```

Per-case model or agent outputs can be evaluated with `--skill`, `--output-file`, or `--output-dir`. See the runner help and script documentation for supported modes.

## Contract shape

A skill contract is a YAML interface, not executable methodology:

```yaml
skill_contract:
  id: example-capability
  category: engineering
  type: skill
  version: "1.0.0"
  capability: example_capability
  description: >
    Runtime-agnostic capability description.
  roles:
    - example_role
  inputs:
    required: []
    optional: []
  outputs:
    allowed: []
  quality_gates: []
  boundary:
    covers: []
    does_not_cover: []
```

Workflow contracts use the same principles but emphasize ordered phases, gates, ownership, evidence, handoffs, and exit conditions.

## Repository map

```text
contracts/skills/<category>/
  reusable capability contracts

contracts/workflows/
  ordered lifecycle contracts

contracts/runtime/
  runtime-facing, implementation-agnostic agreements

contracts/tests/
  behavioral evaluation contracts

contracts/manifest.yaml
  generated registry of contract IDs, paths, versions, and checksums

docs/
  architecture, domain, glossary, port, and integration documentation

rules/
  reusable mandatory constraints

templates/
  generic artifact starting points

skills/
  shared human-readable methodology where core-level teaching material is appropriate

schemas/
  reserved validation schemas; only add with a real artifact and validator path

scripts/
  manifest, compatibility, conformance, and behavioral-eval tooling
```

The generated [contract manifest](contracts/manifest.yaml) is the canonical detailed inventory. Human-maintained docs should explain navigation and meaning rather than duplicate every registered row.

## Contract identity and maturity

Contracts version independently.

```text
0.x   evolving or pre-stable line; a minor bump may be incompatible
1.x+  stable major line; breaking behavior requires a new major version
```

Compatibility still depends on the actual pin and validation result. Manifest presence, repository age, or a `1.0.0` label alone does not prove adapter implementation or production maturity.

Current pin semantics are implemented by [`scripts/validate-implements.sh`](scripts/validate-implements.sh):

```text
^1.2.0  compatible versions in major line 1
^0.2.0  compatible patches in the 0.2 line
~1.2    versions in the 1.2 line
exact   exact version only
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for compatibility classification and version-bump rules.

## Manifest governance

[`contracts/manifest.yaml`](contracts/manifest.yaml) is generated from repository contract files.

Regenerate it after any contract content, version, path, filename, addition, or deletion change:

```bash
./scripts/generate-manifest.sh
```

Review and commit the resulting ID, path, version, checksum, and total changes. Do not hand-edit the manifest.

## Validation tools

| Tool | Responsibility |
|---|---|
| [`generate-manifest.sh`](scripts/generate-manifest.sh) | regenerate contract registry and checksums |
| [`validate-implements.sh`](scripts/validate-implements.sh) | validate adapter paths and pinned versions |
| [`validate-conformance.py`](scripts/validate-conformance.py) | inspect adapter coverage of contract interfaces |
| [`run-eval.py`](scripts/run-eval.py) | validate and execute behavioral evaluation contracts |

These checks answer different questions. A valid manifest, compatible pin, conformant adapter, and passing behavior evaluation are separate evidence layers.

## Canonical documentation

### Framework and domain

- [Architecture v0.2](docs/architecture-v0.2.md)
- [Domain-driven model](docs/domain-driven-model.md)
- [Engineering contract](docs/engineering-contract.md)
- [Glossary](docs/glossary.md)
- [Memory vs knowledge](docs/memory-vs-knowledge.md)

### Ports and adapters

- [Ports and adapters](docs/ports-and-adapters.md)
- [Port taxonomy](docs/port-taxonomy.md)
- [Adapter registry](docs/adapter-registry.md)
- [Contract catalog](docs/contract-catalog.md)

### Runtime concepts

- [AGENTS.md standard](docs/agents-md.md)
- [Development loop](docs/development-loop.md)

Provider, product, system, and UI port specifications remain under [`docs/`](docs/). The contract catalog explains how to navigate them without duplicating the generated manifest.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing contracts or public framework boundaries.

The guide covers:

- repository and layer ownership;
- skill, workflow, runtime, and test contracts;
- docs, rules, templates, and schemas;
- contract versioning and compatibility;
- manifest regeneration;
- adapter path/version and conformance validation;
- behavioral test validation;
- documentation-only review;
- pull-request completion criteria.

## Related repositories

- [`ai-native-skills`](https://github.com/puterakahfi/ai-native-skills) — executable reusable skill and workflow adapters
- [`native-ai-fw`](https://github.com/puterakahfi/ai-native-fw) — orchestration, control plane, discovery, and runtime/product adapters
- [`skills.sh`](https://skills.sh) — compatible skill discovery and installation ecosystem
