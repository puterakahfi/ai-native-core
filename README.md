# Native AI Core

Native AI Core is the public, runtime-agnostic contract layer for AI-native engineering.

It defines the shared domain model, philosophy, lifecycle, rules, workflows, templates, ports, and skill contracts used by app adapters and runtime adapters.

## Repository Role

```text
native-ai-core    = public core/domain/contracts/philosophy
native-ai-app     = private app/product adapter that consumes this core
native-ai-skills  = public runtime skill adapters that implement core skill contracts
```

This repository should stay free of private product context, credentials, deployment secrets, and runtime-specific profile state.

## What Belongs Here

```text
contracts/        # stable public contracts for skills, workflows, runtime bindings, and ports
rules/            # reusable framework rules
workflows/        # reusable lifecycle workflows
templates/        # generic artifact templates
skills/           # human-readable shared skill methodology
schemas/          # validation schemas when contracts stabilize
docs/             # reusable concept and port documentation
```

## What Does Not Belong Here

```text
products/<private-product>/
context-packs/<private-product>.yaml
runtime profile files
private deployment config
private screenshots or customer/product data
runtime-specific installed skill copies
```

## Contract-Driven Usage

A private app adapter should include this core and then bind a product instance to a runtime:

```text
private app repo
  -> includes native-ai-core
  -> adds product-specific contracts/context
  -> binds to runtime adapters such as Hermes
  -> verifies output against core + product contracts
```

## Current Status

Early public core extraction. Contracts are intentionally simple and documentation-first until usage patterns stabilize.
