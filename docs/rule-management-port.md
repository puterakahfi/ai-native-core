# Rule Management Port — Legacy Navigation

Status: Superseded explanatory document

The legacy `RuleManagementPort` combined discovery, applicability, evaluation, enforcement, blocking, and authority. It is replaced by two independently versioned boundaries.

## Canonical contracts

```text
contracts/ports/control/rule-resolution.port.yaml
contracts/ports/control/rule-evaluation.port.yaml
```

Canonical display names:

```text
RuleResolutionPort
RuleEvaluationPort
```

## Rule resolution

```text
subject and action scope
→ discover governed Rule references
→ determine applicability
→ report conflicts and coverage gaps
```

Resolution does not determine whether the action conforms.

## Rule evaluation

```text
resolved Rule references
+ subject evidence
+ bounded scope
→ findings, violations, limitations, and evaluation disposition
```

Evaluation does not grant authority or permission to proceed.

## Required distinctions

```text
Rule availability
≠ rule applicability
≠ rule evaluation
≠ approval
≠ authorization assessment
≠ execution enforcement
```

A positive evaluation result is not an approval. A rule violation may block an action only through applicable policy and authorization handling; the evaluation port does not create authority by itself.

Rule authoring and mutation remain separate governed capabilities. Product policy remains product-owned.

## Legacy adapter examples

Markdown rules, registries, architecture-rule adapters, product-rule adapters, and database-backed sources remain possible implementations or bindings. They are not canonical core defaults.

## Migration

Consumers must select the boundary they actually need and pin its stable ID, canonical path, and compatible version.

The machine authority is the versioned port contracts and generated manifest, not this Markdown document.
