# Skill: Package Boundary Review

## Purpose

Protect monorepo and architecture boundaries during code changes.

## Procedure

1. Identify affected app or package.
2. Check allowed dependency direction.
3. Ensure domain/core packages do not depend on UI, app, framework, or adapter implementation.
4. Ensure apps depend on packages, not packages depending on apps.
5. Ensure runtime code stays under `platform/`.
6. Ensure product knowledge stays under `products/`.

## Native AI Framework Boundary

```text
products/ = product knowledge and configuration
platform/apps/ = runnable applications
platform/packages/ = shared implementation packages
```

## Invalid Examples

```text
platform/packages/core -> platform/apps/web
platform/packages/core -> Next.js
platform/packages/core -> React UI
platform/packages/ui -> product config mutation
```

## Output

Return a package boundary review summary.
