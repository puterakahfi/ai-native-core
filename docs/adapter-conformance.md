# Structured Adapter Conformance

This document defines how an executable adapter declares and validates its relationship to an `ai-native-core` contract.

Implementation discovery and decision record:

```text
docs/structured-adapter-conformance-discovery.md
```

Schemas:

```text
schemas/adapter-conformance.schema.yaml
schemas/conformance-report.schema.yaml
```

## Evidence layers

Adapter conformance is not one Boolean claim.

```text
contract identity and version resolve
→ structured interface declaration is checked
→ owned and delegated boundaries are checked
→ behavioral evidence is evaluated separately
→ runtime evidence is evaluated separately
→ product evidence and acceptance are evaluated separately
→ approval remains authority-bearing governance evidence
```

Each layer answers a different question. Passing one layer does not prove the others.

```text
structured declaration
≠ executable behavior
≠ runtime execution
≠ product acceptance
≠ approval
```

## Canonical declaration

An adapter keeps executable methodology in:

```text
skills/<adapter-id>/SKILL.md
```

Its static conformance declaration lives beside it:

```text
skills/<adapter-id>/adapter.conformance.yaml
```

Example:

```yaml
contract_schema:
  kind: adapter_conformance
  version: 1.0.0
  path: schemas/adapter-conformance.schema.yaml

adapter_conformance:
  adapter:
    id: example-adapter
    kind: skill
    patterns:
      - skill-adapter
    entrypoint: skills/example-adapter/SKILL.md

  implements:
    contract_id: example-contract
    contract_kind: skill_contract
    contract_path: contracts/skills/example/example-contract.contract.yaml
    contract_version: ^1.0.0

  capability: example_capability

  interface:
    inputs:
      - required_input
    outputs:
      - supported_output
    gates:
      - required_gate

  boundary:
    covers:
      - owned_responsibility
    delegates:
      - product_policy

  dependencies: []
  handoffs: []
  unsupported_claims: []
  adapter_requirements: []
  evidence_refs: []
```

### Executable kind

`adapter.kind` must match `metadata["ai-native-skills.type"]` in `SKILL.md`.

Official kinds:

```text
skill
workflow
meta-skill
```

### Adapter patterns

Every contract-backed declaration includes:

```text
skill-adapter
```

Additional accepted declaration patterns:

```text
facade
runtime-adapter
port-adapter
```

Patterns are not executable types. For example, a facade remains a `meta-skill` with both `skill-adapter` and `facade` patterns.

Legacy reports may preserve additional downstream pattern values such as `domain-reviewer`. Preserving a legacy value in a migration report does not automatically make it an accepted v2 declaration pattern.

`capability` may be `null` only when the implemented contract family does not define a capability identity.

## Deterministic structural checks

The validator checks:

```text
declaration schema
adapter ID and entrypoint
executable kind and declared patterns
canonical or active aliased contract path
contract ID
contract kind
version-pin compatibility
capability identity
required and declared inputs
required and allowed outputs
quality or safety gates
owned and delegated boundaries
dependencies
handoffs
unsupported claims
adapter requirement keys
evidence-reference layers
```

Unknown interface or boundary identifiers are errors. Missing required coverage is partial. Explicit ownership of a delegated responsibility is an error.

## Interface semantics

### Inputs

Every required input must be declared. Optional inputs form an allowed universe and may be omitted. Declaring an unknown input is an error.

### Outputs

Required outputs must be declared. Allowed outputs form the output universe; an adapter does not need to support every allowed output to be conformant.

```text
allowed output omitted
→ no coverage failure

required output omitted
→ PARTIAL

contract output explicitly marked unsupported
→ visible PARTIAL limitation

unknown output declared
→ ERROR
```

### Gates

Every contract quality or safety gate must be declared. Unknown gate identifiers are errors.

## Boundary declarations

A skill contract may define:

```yaml
boundary:
  covers:
    - owned_capability
  does_not_cover:
    - provider_configuration
```

A port contract uses:

```yaml
boundary:
  owns: []
  delegates: []
  does_not_own: []
```

The conformance declaration normalizes both families into:

```yaml
boundary:
  covers: []
  delegates: []
```

Use exact identifiers from the contract. Separator and case normalization support comparison, but the validator does not perform fuzzy semantic matching.

```text
contract-owned responsibility omitted
→ PARTIAL

contract-delegated responsibility omitted
→ PARTIAL

contract-delegated responsibility claimed under covers
→ ERROR

same responsibility under covers and delegates
→ ERROR
```

Adapter-specific dependencies, handoffs, or requirements may be declared beyond the reusable core contract. They are preserved as migration diagnostics rather than treated as contract-owned guarantees.

## Result classes

### Structural status

| Status | Meaning |
|---|---|
| `CONFORMANT` | all checkable required structural declarations match the resolved contract |
| `PARTIAL` | declaration exists but required coverage is incomplete or a contract responsibility is explicitly unsupported |
| `ERROR` | declaration is malformed, contradictory, incompatible, unresolved, unknown, or explicitly out of bounds |
| `NOT_CHECKABLE` | a v2 structured declaration is absent or required static evidence cannot be evaluated |

### Evidence-layer status

Every result separately records:

```text
behavioral_status
runtime_status
product_status
approval_status
```

Possible values include:

```text
BEHAVIOR_NOT_VERIFIED
EVIDENCE_REFERENCED
NOT_CHECKABLE
NOT_EVALUATED
```

`EVIDENCE_REFERENCED` means only that a reference was declared. It does not prove sufficiency, applicability, acceptance, or authority.

## Exit modes

Migration mode preserves compatibility while consumer declarations are introduced:

```text
0 → no ERROR result
1 → one or more ERROR results
```

Strict mode exposes incomplete declarations to CI:

```text
0 → all checked adapters CONFORMANT
1 → one or more ERROR results
2 → one or more PARTIAL results and no ERROR
3 → one or more NOT_CHECKABLE results and no ERROR
```

Behavioral, runtime, and product evidence do not change the static structural exit code. They remain explicit report dimensions.

## Machine-readable reports

Generate repository and per-adapter reports:

```bash
python3 scripts/validate-conformance.py \
  ../ai-native-core \
  ../ai-native-skills \
  --mode migration \
  --output-dir conformance-reports \
  --format json
```

Use YAML output with:

```bash
--format yaml
```

Generated files:

```text
conformance-reports/repository-summary.json
conformance-reports/<adapter-id>.json
```

The report schema is:

```text
schemas/conformance-report.schema.yaml
```

Reports preserve legacy migration observations without converting them into accepted declaration semantics.

## Legacy migration

Existing adapters may still declare:

```yaml
metadata:
  ai-native-skills.implements: ai-native-core/contracts/skills/<category>/<contract>.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.boundary.covers: '["owned_capability"]'
  ai-native-skills.boundary.delegates: '["provider_configuration"]'
```

These fields remain useful migration evidence, but they do not produce `CONFORMANT` under v2.

An adapter without `adapter.conformance.yaml` is:

```text
NOT_CHECKABLE
```

Textual input, output, and gate matching remains available only as supplemental `INFO` migration diagnostics. Copying contract vocabulary into prose cannot prove interface coverage.

Consumer migration belongs in `ai-native-skills`; core validators must not bulk-generate declarations from contract lists.

## Validation commands

```bash
python3 scripts/validate-conformance.py \
  ../ai-native-core \
  ../ai-native-skills \
  --mode migration

python3 -m unittest discover \
  -s tests \
  -p 'test_validate_conformance.py' \
  -v

python3 -m unittest discover \
  -s tests \
  -p 'test_conformance_semantics.py' \
  -v
```

Path and version-only compatibility remains available through:

```bash
bash scripts/validate-implements.sh ../ai-native-core
```

Behavioral contracts remain separate:

```bash
python3 scripts/run-eval.py --all --validate-tests
```

## Migration guidance

For each contract-backed adapter:

1. resolve the canonical contract and compatible version;
2. confirm the executable kind and applicable adapter patterns;
3. review actual executable ownership and handoffs;
4. create `adapter.conformance.yaml` manually;
5. declare only inputs, outputs, gates, boundaries, dependencies, handoffs, and requirements the adapter genuinely supports;
6. record unsupported contract responsibilities honestly;
7. run migration mode;
8. resolve `ERROR`, then review every `PARTIAL` and `NOT_CHECKABLE` result;
9. run strict mode when the migration slice is intended to be complete;
10. keep behavioral, runtime, product, and approval evidence separate.

Do not bulk-copy contract values without reviewing executable behavior.

## Scope boundary

Static v2 validation does not replace:

```text
behavioral skill evaluation
runtime integration testing
security review
architecture review
visual or interaction evidence
product acceptance
human review
approval authority
```

A green static report proves only that the structured declaration is internally consistent with the resolved contract at the checked version.
