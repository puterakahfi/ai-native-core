# Native AI Engineering Contract Schema Architecture

Status: Candidate canonical architecture for issue `#8`

Upstream authority:

```text
#13 philosophy and source-role authority
→ #6 domain model and ownership
→ #7 port taxonomy and first-class port contracts
→ #8 contract schemas and workflow canonicalization
```

Discovery evidence:

```text
docs/contract-schema-discovery.yaml
```

## 1. Objective

Every active contract artifact must identify its schema deterministically, validate through one repository-executable pipeline, register complete manifest metadata, and preserve domain ownership without forcing unrelated extension meaning into one universal shape.

## 2. Contract document envelope

Every contract document uses a schema-identity sibling beside its family root:

```yaml
contract_schema:
  kind: skill_contract
  version: "1.0.0"
  path: schemas/skill-contract.schema.yaml

skill_contract:
  id: example
  version: "1.0.0"
  # family-owned body
```

This shape is chosen because it:

- gives each artifact explicit schema identity;
- lets the manifest read kind and schema version without path or grep inference;
- preserves existing family roots for compatible consumers;
- keeps contract version separate from schema version;
- allows schema migration without silently changing domain contract identity.

Required distinction:

```text
schema version
≠ contract version
≠ adapter compatibility version
≠ product release version
```

## 3. Canonical active families

```text
skill_contract
workflow_contract
runtime_contract
port_contract
behavioral_test_contract
compatibility_manifest
```

Supporting schemas also define:

```text
adapter_manifest
domain_contract
contract_manifest
```

`adapter_manifest` and `domain_contract` schemas are validated through fixtures until active first-class artifacts exist. They must not be treated as implemented runtime or domain behavior merely because schemas exist.

## 4. Shared primitives

`schemas/common.schema.yaml` owns primitives that must have the same meaning across families:

```text
schema identity
contract ID
semantic version
non-empty string
machine identifier
path reference
string list
quality-gate identifier list
adapter requirement map
compatibility reference
```

Family schemas may specialize these primitives. They may not redefine their base meaning.

Shared serialization does not collapse domain concepts:

```text
observation ≠ model ≠ assumption
claim ≠ evidence
review ≠ approval
permission ≠ authority
feedback ≠ learning
```

Those distinctions remain family- and domain-owned structures even when they reuse shared identifiers, references, or version primitives.

## 5. Extension boundary

The discovery found many domain-specific structures such as design direction, concurrency, scope diff, evidence policy, memory taxonomy, tool risk, and deployment authorization.

Canonical rule:

```text
shared primitive
→ define once in common schema

family invariant
→ define in family schema

domain-specific extension
→ preserve under the owning family contract and validate as an explicit extension surface
```

Issue `#8` does not normalize every domain extension into one generic field. A field named `evidence`, `approval`, `boundary`, or `transition` is not assumed semantically equivalent across families without an upstream ownership decision.

Existing top-level domain extensions remain compatible in schema version `1.0.0`. The unified validator reports their shape and may recommend migration into an `extensions` namespace, but it does not rewrite domain meaning merely for structural symmetry.

## 6. Workflow classification

A contract is a `workflow_contract` when it owns a sequenced lifecycle composed from phases and one or more of:

```text
ordered transitions
gates
handoffs
exit conditions
cross-capability or cross-owner coordination
```

A skill may contain internal procedure phases without becoming a workflow. The deciding question is not whether a `phases` field exists; it is whether the artifact owns a reusable capability method or a lifecycle coordinating phases, gates, handoffs, and transitions.

### Migrate to workflow contracts

```text
design-refinement
redesign-workflow
skill-evolution
development-loop
```

`development-loop` remains an execution method in domain meaning. It is serialized as `workflow_contract` with `workflow_kind: execution_method`; this does not turn it into a product workflow or canonical domain lifecycle.

### Remain skill contracts

```text
design-review
systematic-debugging
```

Their phase lists describe internal expert procedures. They do not own a separately coordinated lifecycle aggregate.

## 7. Canonical workflow location and shape

Canonical location:

```text
contracts/workflows/<id>.contract.yaml
```

Canonical root:

```text
workflow_contract
```

Canonical workflow fields:

```text
id
type = workflow
version
category
workflow_kind
purpose
phases
transitions
skill_load_order
quality_gates
adapter_requirements
```

Optional capability, roles, boundary, inputs, outputs, handoffs, exit conditions, compatibility, and domain extensions remain explicit when applicable.

A workflow definition is not an execution run. Schema validity does not prove the workflow was selected, authorized, executed, reviewed, completed, or accepted.

## 8. Compatibility and path migration

Moved contract paths are recorded in:

```text
contracts/compatibility/contract-path-aliases.contract.yaml
```

A path alias records:

```text
legacy path
canonical path
contract identity
contract kind
compatible version range
migration status
```

Resolvers must prefer the canonical path and may temporarily resolve an active legacy alias. The old file does not remain as a second machine authority.

```text
path alias
≠ duplicate contract
≠ adapter conformance
≠ runtime compatibility proof
```

## 9. Manifest v2

Every generated entry records:

```text
id
kind
schema_version
schema_path
contract_version
path
checksum
```

The generator parses YAML and schema identity. It must not infer kind from a directory alone or extract version using grep.

Manifest regeneration is deterministic except for a timestamp that remains stable when semantic registry content is unchanged.

## 10. Unified validation pipeline

The canonical pipeline validates:

1. YAML and document envelope;
2. declared schema path, kind, and version;
3. family JSON Schema;
4. filename, path family, and contract identity;
5. contract and alias uniqueness;
6. semantic family invariants;
7. workflow phase, transition, handoff, and reference integrity;
8. runtime/workflow separation;
9. compatibility alias targets;
10. generated manifest identity and drift.

Port-specific semantic validation remains active and is consumed by the unified pipeline rather than weakened.

## 11. Evidence boundary

Schema validation proves structural conformance to a declared version. It does not prove:

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

Those evidence layers remain separately owned and separately reported.
