# Contracts

Contracts define stable expectations that adapters must follow.

A contract answers:

```text
What must be true, independent of which runtime or app implements it?
```

Contracts are runtime-agnostic. Runtime-specific implementations belong in adapter repositories such as `native-ai-skills` or app/runtime bindings. Those adapters may be public or private depending on product sensitivity.

## Contract Areas

```text
contracts/
├── skills/       ← invariant agent capabilities (cross-team, cross-product)
├── workflows/    ← process templates: required phases, gates, skill deps
│                   product adapters define: branch strategy, issue tracker, approval policy
├── runtime/      ← runtime source of truth and binding contracts
└── ports/        ← abstract port contracts (future)
```

## Skills vs Workflows

| | Skills | Workflows |
|---|---|---|
| **What** | Agent capability | Sequenced process |
| **Invariant?** | Yes — same across teams | No — teams implement differently |
| **Implementation** | `ai-native-skills/skills/` | `ai-native-fw/products/<product>/workflows/` |
| **Composable?** | Standalone | Workflow composes skills |

A workflow contract defines **what phases must exist and what gates must pass**.
It does not define branch names, tool integrations, or team-specific steps — those live in the product adapter.
