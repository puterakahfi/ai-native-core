# Adapter Conformance

This document defines how an executable skill adapter declares and validates its relationship to an `ai-native-core` skill contract.

## Evidence layers

Adapter conformance is not one boolean claim.

```text
contract path resolves
→ pinned version is compatible
→ required gates, inputs, and outputs are represented
→ owned and delegated boundaries are declared consistently
→ executable behavior is evaluated in realistic cases
```

Each layer answers a different question. Passing one layer does not prove the others.

## Structured boundary declarations

A contract may define:

```yaml
boundary:
  covers:
    - owned_capability
  does_not_cover:
    - provider_configuration
```

An executable adapter declares the corresponding responsibility boundary in `SKILL.md` frontmatter:

```yaml
metadata:
  ai-native-skills.implements: ai-native-core/contracts/skills/<category>/<contract>.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["owned_capability"]'
  ai-native-skills.boundary.delegates: '["provider_configuration"]'
```

Use the exact contract boundary values. The validator normalizes case and separators, but it does not perform fuzzy semantic matching.

### `ai-native-skills.boundary.covers`

Declares responsibilities the adapter claims to implement from the contract's `boundary.covers` list.

A complete adapter should declare every contract-owned responsibility it claims as part of full conformance. A partial declaration remains a warning rather than silently becoming full coverage.

### `ai-native-skills.boundary.delegates`

Declares responsibilities the adapter explicitly preserves outside its ownership from the contract's `boundary.does_not_cover` list.

Delegation means the adapter does not absorb that responsibility. The actual owner may be another skill, workflow, runtime adapter, provider adapter, or product repository.

## Why declarations are structured

Boundary validation does not search prose for similar words.

Naive keyword matching can reward an adapter for copying contract text without making ownership or delegation explicit. Structured metadata provides a deterministic declaration that can be compared against the contract.

The declaration is still not proof of executable behavior. Behavioral evaluation, direct review, runtime tests, or product evidence remain necessary when the adapter's real behavior matters.

## Result classification

| Result | Meaning | Example |
|---|---|---|
| `ERROR` | explicit contradictory or out-of-bound claim | adapter lists `product_policy` under `covers` when the contract lists it under `does_not_cover` |
| `WARN` | declaration is partial, malformed, unknown, or delegates contract-owned work | one required `covers` item is missing |
| `NOT_CHECKABLE` | structured evidence cannot be evaluated | both boundary metadata fields are absent |
| no boundary finding | declarations match the checkable contract boundary | all owned and delegated items are declared consistently |

An explicit `ERROR` makes `validate-conformance.py` exit with status `1`.

Warnings and `NOT_CHECKABLE` results remain visible in the summary and currently exit with status `0` when no critical errors exist. Status `0` therefore means **no critical declaration error**, not universal proof of implementation quality.

## Validation commands

From an adapter repository:

```bash
../ai-native-core/scripts/validate-implements.sh ../ai-native-core

python3 ../ai-native-core/scripts/validate-conformance.py \
  ../ai-native-core \
  .
```

`validate-implements.sh` checks contract paths and version compatibility.

`validate-conformance.py` checks:

- quality-gate textual coverage;
- allowed-output textual coverage;
- required-input textual coverage;
- structured boundary declaration consistency.

Behavioral contracts are validated separately:

```bash
python3 scripts/run-eval.py --all --validate-tests
```

## Migration guidance

For every contract-backed `SKILL.md`:

1. open the implemented contract;
2. inspect `boundary.covers` and `boundary.does_not_cover`;
3. confirm the adapter's actual responsibility before declaring it;
4. add accurate `covers` and `delegates` metadata;
5. run path/version and conformance validation;
6. fix explicit overclaims before treating the adapter as conformant;
7. keep missing runtime or product evidence labeled honestly.

Do not bulk-copy boundary lists without reviewing the adapter. Matching metadata is a declaration of ownership, not decorative contract text.

## Scope boundary

This validation covers skill adapters that declare `ai-native-skills.implements` for an `ai-native-core` skill contract.

It does not replace:

- product-specific acceptance;
- runtime integration testing;
- security review;
- architecture review;
- model-output evaluation;
- human review of whether the implementation genuinely performs the declared responsibility.
