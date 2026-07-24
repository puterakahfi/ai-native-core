# Engineering Design Quality Contracts

## Decision

Native AI Core accepts three distinct pre-stable skill contracts:

```text
clean-code@0.1.0
solid-design@0.1.0
clean-architecture@0.1.0
```

A shared `engineering-design-quality` contract is not introduced. The three capabilities may be composed by executable workflows and packs, but they have different triggers, evidence requirements, outputs, gates, and delegation boundaries. A core umbrella would blur ownership and encourage every concern to load for every engineering change.

## Why the contracts belong in core

The contracts are runtime-agnostic and reusable across languages, frameworks, repositories, and products. They define stable assessment and boundary agreements rather than implementation methodology.

They do not encode:

```text
language-specific style rules
framework-specific folder structures
provider names
product severity policy
runtime orchestration
product acceptance
merge authorization
```

Those remain adapter, runtime, or product responsibilities.

## Canonical separation

| Contract | Owns | Delegates |
|---|---|---|
| `clean-code` | internal code-expression assessment, named readability and maintainability findings, behavior-preservation lock, smallest safe local correction guidance | structural refactoring execution, architecture selection, independent review, product acceptance |
| `solid-design` | contextual SRP/OCP/LSP/ISP/DIP applicability, concrete findings, alternatives, abstraction risk, smallest justified design correction | architecture ownership, pattern implementation, refactoring execution, independent review |
| `clean-architecture` | architecture-style applicability, policy/mechanism mapping, dependency rule, repository-aware boundary mapping, boundary data translation, bounded migration guidance | architecture implementation, concrete ports/adapters, domain modeling, pattern implementation, independent acceptance |

## Relationship to existing contracts

### `master-engineer`

`master-engineer` remains the architecture and implementation owner. The new contracts provide bounded specialist analysis and handoffs; they do not take ownership of the system design decision or implementation plan.

### `architecture-review`

`architecture-review` remains the independent post-implementation compliance reviewer. A `clean-architecture` recommendation or a SOLID finding is specialist evidence, not an acceptance verdict.

### `refactoring`

`refactoring` owns behavior-preserving structural transformation. `clean-code` and `solid-design` may name smells and recommend the smallest correction, but must hand off transformation when refactoring procedure and proof are required.

### `design-patterns`

`design-patterns` owns pattern selection and implementation guidance from verified forces. `solid-design` may expose extension or dependency pressure, but must not select patterns speculatively or equate SOLID with pattern use.

### `ports-and-adapters`

`ports-and-adapters` owns concrete hexagonal port and adapter design. `clean-architecture` decides whether such boundaries are justified and where policy/mechanism separation is needed; it does not require ports at every boundary or implement them.

## Prohibited dogma

The three contracts prohibit universal prescriptions such as:

```text
maximum line, function, parameter, or class sizes as automatic verdicts
one interface per class or method
patterns or factories without verified variation pressure
DI-container presence as proof of dependency inversion
fixed Clean Architecture layer counts
generic folder trees
framework bans
ports and use cases for every function
repository-wide rewrites for local findings
```

Metrics and architecture styles may trigger investigation, but conclusions require observable evidence, verified forces, repository conventions, and explicit trade-offs.

## Evidence and authority limits

Contract presence and schema validity do not prove:

```text
adapter conformance
behavioral correctness
runtime execution
product suitability
architecture acceptance
review approval
merge authorization
production adoption
```

Each evidence layer remains separate.

## Versioning

All three contracts begin at `0.1.0` because downstream structured adapter declarations have not yet been migrated and validated.

```text
patch bump
→ wording or non-behavioral clarification

0.x minor bump
→ may be breaking; required inputs, outputs, gates, or boundaries may change

1.0.0
→ eligible only after adapter migration, behavioral validation, and boundary stability are demonstrated
```

Adapters should initially pin:

```text
^0.1.0
```

Under current compatibility semantics, that pin accepts compatible patches within the `0.1` line only.

## Adapter migration path

After the core PR is accepted and merged:

1. update each corresponding `ai-native-skills` adapter from its reviewed core-gap exemption to the canonical contract path;
2. add or update `skills/<id>/adapter.conformance.yaml` using schema `adapter_conformance@1.0.0`;
3. declare the exact contract ID, kind, path, capability, `^0.1.0` pin, required interface IDs, gates, covered boundaries, delegated boundaries, adapter requirements, dependencies, and handoffs;
4. run path and version validation;
5. run structured conformance in migration mode, then strict mode for the migrated three-skill slice;
6. run the behavioral evals in both repositories;
7. keep runtime evidence, product validation, review, approval, and authorization claims separate.

Canonical paths:

```text
contracts/skills/engineering/clean-code.contract.yaml
contracts/skills/architecture/solid-design.contract.yaml
contracts/skills/architecture/clean-architecture.contract.yaml
```

The reviewed exemption must not be removed before the core contract is published and the adapter declaration is validated. Contract publication alone does not make an executable skill conformant.

## Acceptance boundary

This decision establishes canonical meaning, stable interfaces, gates, ownership, delegation, versioning, and migration. Executable methodology remains in `ai-native-skills`; orchestration remains in Native AI OS/runtime implementations; product decisions and acceptance remain in product repositories.
