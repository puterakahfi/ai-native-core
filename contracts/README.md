# Contracts

Contracts define stable expectations that adapters must follow.

A contract answers:

```text
What must be true, independent of which runtime or app implements it?
```

Contracts are runtime-agnostic. Runtime-specific implementations belong in adapter repositories such as `native-ai-skills` or app/runtime bindings. Those adapters may be public or private depending on product sensitivity.

## Initial Contract Areas

```text
contracts/
├── skills/
├── workflows/
├── runtime/
└── ports/
```
