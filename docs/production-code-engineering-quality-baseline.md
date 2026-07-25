# Production-Code Engineering Quality Baseline

Status: proposed through [`ai-native-core#56`](https://github.com/puterakahfi/ai-native-core/issues/56)

## Decision

Native AI Engineering defines one runtime-agnostic production-code quality baseline that is attached automatically to substantive production-code work.

The baseline is a **quality lifecycle overlay**. It is not:

- a second primary lifecycle;
- a replacement for `new-feature`, `bugfix`, `spec-driven`, refactoring, or product-development workflows;
- an umbrella skill that absorbs TDD, clean code, SOLID, DDD, design patterns, or architecture review;
- a runtime implementation;
- merge, release, or product-acceptance authority.

The primary lifecycle continues to own the delivery sequence. The baseline adds stable cross-workflow obligations for applicability, capability composition, evidence, gates, review, and blocking semantics.

Canonical contract:

```text
contracts/workflows/production-code-quality-baseline.contract.yaml
```

Behavioral protection:

```text
contracts/tests/production-code-quality-baseline.test.yaml
```

## Why this exists

Individual engineering capabilities already exist, but availability alone does not make them default execution behavior.

Without a shared composition contract, one workflow may require TDD while another only implies RED-GREEN behavior, clean-code review may be optional or late, and SOLID, DDD, patterns, or architecture applicability may be skipped silently.

The baseline closes that lifecycle gap while preserving anti-over-engineering constraints.

```text
available capability ≠ resolved capability
resolved capability ≠ executed capability
executed capability ≠ evidence-backed PASS
green CI ≠ architecture approval
technical review ≠ merge authorization
technical delivery ≠ product acceptance
```

## Applicability

Every routed task first records one classification:

| Classification | Meaning |
|---|---|
| `PRODUCTION_CODE_CHANGE` | Creates or materially changes production behavior |
| `NON_PRODUCTION_CHANGE` | No material production behavior impact |
| `DISPOSABLE_EXPERIMENT` | Explicitly bounded throwaway work with no production submission |
| `NOT_VERIFIED` | Repository impact or intended outcome is not sufficiently established |

Production-code examples include features, bug fixes, behavior changes, refactors, structural or data migrations, and generated code intended for repository submission.

Documentation, analysis without implementation, and static configuration with no production behavior may be non-production. The label is determined from outcome and repository impact, not from file extension or artifact name alone.

`NOT_VERIFIED` blocks a complete production-code quality claim.

## Default composition

For `PRODUCTION_CODE_CHANGE`, the routed primary lifecycle attaches the baseline:

```text
workflow-router
→ one primary lifecycle
→ production-code quality baseline overlay
→ applicability map
→ phase-specific capability resolution
→ execution and evidence
→ independent architecture and code review
→ authority handoff
```

### Always required

The baseline always evaluates:

- effective scope and acceptance traceability;
- repository implementation context and conventions;
- behavior-test strategy;
- TDD or an attributable authorized exception;
- affected regression coverage;
- clean-code quality;
- module and ownership boundaries;
- error and failure-path behavior;
- product-defined test, lint, type, build, contract, migration, and runtime checks;
- independent architecture review;
- code review before merge authorization.

### Conditional concerns

The concern is always classified, but the specialist loads only when material forces justify it:

- SOLID design;
- Domain-Driven Design;
- design patterns;
- Clean Architecture;
- ports and adapters;
- security and threat modeling;
- performance;
- resilience and observability;
- data and migration safety;
- user-facing design and accessibility.

Valid applicability outcomes:

```text
APPLICABLE
PARTIAL
NOT_APPLICABLE
NOT_JUSTIFIED
NOT_VERIFIED
BLOCKED
```

`NOT_APPLICABLE` and `NOT_JUSTIFIED` require inspectable rationale. Silence is `NOT_VERIFIED`, never PASS.

## TDD rule and exception boundary

Production behavior changes use RED-GREEN-REFACTOR:

```text
failing behavior or regression reproduction
→ RED evidence
→ minimal passing implementation
→ GREEN evidence
→ refactor while tests remain green
```

An exception is valid only when it includes:

- attributable authority;
- bounded scope;
- explicit reason;
- alternative verification;
- residual risk and non-PASS semantics when evidence remains insufficient.

An agent does not authorize its own exception. A test file, timestamp, or post-hoc test does not prove test-first ordering.

## Evidence and gate semantics

A PASS-like claim requires evidence appropriate to that claim.

Command output may prove a test, lint, typecheck, or build result. It does not by itself prove clean-code quality, SOLID correctness, domain modeling quality, justified pattern selection, or architecture acceptance.

The normalized handoff keeps these distinct:

```yaml
engineering_quality_baseline:
  production_code_applicability: PRODUCTION_CODE_CHANGE
  assessments: []
  capabilities_resolved: []
  capabilities_executed: []
  claims: []
  evidence_refs: []
  gate_results: []
  reviewer_results: []
  blocking_gaps: []
  final_quality_state: NOT_VERIFIED
  transition_eligibility: BLOCKED
```

A runtime may implement richer records, but must preserve canonical distinctions among workflow definition, capability resolution, execution, claims, evidence, gates, reviews, approval, merge authorization, delivery, and product acceptance.

## Blocking behavior

Mandatory `NEEDS_WORK`, `BLOCKED`, or `NOT_VERIFIED` results prevent unsupported completion or merge-readiness claims.

The baseline never self-authorizes:

- merge;
- deployment;
- release;
- production mutation;
- delivery acceptance;
- product acceptance.

Those authorities remain product- and runtime-policy decisions.

## Ownership

| Layer | Ownership |
|---|---|
| `ai-native-core` | Universal quality-composition contract and status semantics |
| `ai-native-skills` | Executable routing, capability loading, procedures, and behavioral evaluation |
| Native AI OS / `ai-native-fw` | Resolution, execution records, evidence persistence, gate evaluation, transitions, and observability |
| Product repositories | Commands, thresholds, stack rules, exceptions, reviewers, merge policy, and product acceptance |

Individual capability ownership remains unchanged:

- `test-driven-development` owns RED-GREEN-REFACTOR;
- `clean-code` owns internal code-expression quality;
- `solid-design` owns pragmatic SOLID assessment;
- `domain-driven-design` owns domain modeling;
- `design-patterns` owns force-justified pattern selection;
- `clean-architecture` owns architecture-style applicability and policy/mechanism boundaries;
- `master-engineer` owns implementation and architecture synthesis;
- `architecture-review` owns independent architecture acceptance;
- `code-review-workflow` owns technical review and merge-readiness mapping.

## Downstream migration

### `ai-native-skills`

The executable adapter should:

1. classify production-code applicability during routing;
2. keep exactly one primary workflow;
3. attach the baseline as an overlay;
4. resolve phase-specific required skills;
5. classify conditional concerns before specialist loading;
6. emit execution, evidence, gate, reviewer, and blocking records;
7. preserve anti-dogma behavior through positive and adversarial evals.

Tracking: [`ai-native-skills#137`](https://github.com/puterakahfi/ai-native-skills/issues/137)

### Native AI OS

The runtime should:

1. persist an engineering quality execution plan;
2. distinguish resolved, executed, and evidenced capabilities;
3. link claims to evidence;
4. evaluate canonical gate results;
5. enforce configured transition blocking;
6. expose quality status and remaining authority truthfully.

Tracking: [`ai-native-fw#85`](https://github.com/puterakahfi/ai-native-fw/issues/85)

## Non-goals

The baseline does not mandate:

- DDD for CRUD or thin-domain systems;
- interfaces for every implementation;
- a named design pattern without verified forces;
- a fixed Clean Architecture folder tree or layer count;
- a universal framework, language, test tool, or coverage percentage;
- self-approved technical, merge, release, or product decisions.
