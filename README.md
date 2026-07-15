# Native AI Core

Native AI Core is the public, runtime-agnostic contract layer for AI-native engineering.

It defines the shared domain model, philosophy, lifecycle, rules, workflows, templates, ports, and skill contracts used by app adapters and runtime adapters.

## Repository Role

```text
native-ai-core    = public core/domain/contracts/philosophy
native-ai-app     = app/product adapter that consumes this core; public or private by implementer choice
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

An app adapter should include this core and then bind a product instance to a runtime:

```text
app adapter repo
  -> includes native-ai-core
  -> adds product-specific contracts/context
  -> binds to runtime adapters such as Hermes
  -> verifies output against core + product contracts
```

App adapter visibility is not part of the contract. It can be public for examples/open products or private for internal products. The contract only requires correct implementation of core contracts and clean separation of product/runtime-specific context.

## Current Status

Early public core extraction. Contracts are intentionally simple and documentation-first until usage patterns stabilize.
