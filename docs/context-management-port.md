# Context Management Port — Legacy Navigation

Status: Superseded explanatory document

Canonical first-class contract:

```text
contracts/ports/control/context-resolution.port.yaml
```

Canonical display name:

```text
ContextResolutionPort
```

## Why the name changed

`ContextManagementPort` mixed several responsibilities behind one broad verb. The retained reusable boundary is context resolution:

```text
context request
→ attributable source references
→ gap and staleness assessment
→ versioned ContextPack checkpoint
→ scoped readiness result
```

The canonical port may resolve and assemble context, but it does not own the sources it references.

## Required distinctions

```text
ContextResolutionPort
≠ source retrieval provider
≠ source-of-truth authority
≠ knowledge acceptance
≠ memory storage
≠ skill or rule definition
≠ execution authorization
≠ execution
```

A ContextPack records a purpose-specific checkpoint. Inclusion in the pack does not transfer source authority or turn memory, inference, or assumption into accepted knowledge.

Missing, stale, conflicting, inaccessible, or insufficient context remains explicit. A positive readiness result is bounded by the named purpose and does not authorize execution.

## Legacy adapter examples

Earlier examples such as file-backed, GitHub-backed, database-backed, or generated context bundles remain possible adapters or bindings. They are not canonical core defaults.

## Migration

Consumers using the legacy name should migrate to the stable contract by declaring:

```text
port ID
canonical contract path
compatible contract version
```

The machine authority is the versioned port contract and generated manifest, not this Markdown document.
