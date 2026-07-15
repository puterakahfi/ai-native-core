# Skill: Repository Inspection

## Purpose

Inspect the repository before making implementation changes.

## Procedure

1. Identify the product, app, module, and task being executed.
2. Read the relevant product config.
3. Read the relevant app config when the task targets an app.
4. Read the context pack.
5. Inspect runtime source paths before editing.
6. Identify existing package manager, monorepo layout, scripts, and package boundaries.
7. Confirm whether files already exist before creating new ones.

## Must Check

```text
products/{product}/product.config.yaml
products/{product}/project.config.yaml
context-packs/{product}.yaml
platform/README.md
package.json
pnpm-workspace.yaml
turbo.json
```

## Output

Return a short repository inspection summary before implementation.
