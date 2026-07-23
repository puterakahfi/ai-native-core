# Task Continuity

Task continuity is the runtime-agnostic capability for preserving verified task direction across chat sessions, agents, runtimes, and machines.

```text
checkpoint
→ portable handoff
→ current-source verification
→ resume or block
→ closure and durable-knowledge promotion
```

## Boundary

`task-continuity` owns:

- source-backed task checkpoints;
- transcript-independent session handoffs;
- freshness, staleness, conflict, and supersession evaluation;
- verification of current task sources before resume;
- one exact next action and its expected evidence;
- continuity closure without false completion;
- promotion requests when an official decision still exists only in chat or memory.

It does not own:

- chat transcript storage or provider memory APIs;
- product-specific checkpoint persistence;
- repository, issue, branch, or pull-request mutation;
- task implementation or execution;
- evidence generation, gate evaluation, review, or approval;
- delivery, merge, or product-acceptance authority;
- learning-candidate evaluation or promotion.

## Relationship to Context and Memory

```text
context-engineering
  authors durable institutional context

context-manager
  resolves the context required before execution

task-continuity
  preserves and verifies where an active task stopped and how it resumes

memory
  helps retrieve prior context but does not establish authoritative task state
```

Current governing sources override an older checkpoint. A newer timestamp alone does not establish higher authority.

## Status Separation

Task continuity must preserve these states independently:

```text
planned
attempted
implemented
verified
gate passed
reviewed
approved
delivered
merged
accepted
```

A successful build does not imply review or approval. A merged pull request does not imply release or product acceptance. Closure does not create authority that is absent from the linked records.

## Implementations

- Executable reusable behavior belongs in `ai-native-skills`.
- Persistent checkpoints and resume orchestration belong in a Native AI OS or product/runtime adapter.
- Product-specific source priority, staleness policy, persistence, and acceptance remain product-owned.
