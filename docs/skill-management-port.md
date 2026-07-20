# Skill Management Port — Legacy Navigation

Status: Superseded explanatory document

Canonical first-class contract:

```text
contracts/ports/control/skill-resolution.port.yaml
```

Canonical display name:

```text
SkillResolutionPort
```

## Why the name changed

`SkillManagementPort` suggested ownership of skill definition, installation, execution, and lifecycle. The retained reusable boundary is narrower:

```text
required capabilities
→ discover versioned SkillDefinition references
→ resolve compatible skills
→ report missing or incompatible requirements
→ hand off references for method selection
```

## Required distinctions

```text
SkillResolutionPort
≠ SkillDefinition authoring
≠ skill installation
≠ skill application
≠ workflow execution
≠ adapter binding
≠ behavioral conformance
```

Discovering or selecting a skill does not prove that the skill was installed, applied correctly, or embodied in runtime behavior.

The `ai-native-skills` repository owns executable skill implementations. `native-ai-fw` may orchestrate discovery and runtime binding. Product repositories own product-specific selection and acceptance policy.

## Legacy adapter examples

Markdown, YAML registry, GitHub registry, or database-backed discovery remain possible adapter choices. They are not universal core defaults.

## Migration

Consumers using the legacy name should migrate to the stable contract through its port ID, canonical path, and compatible version pin.

The machine authority is the versioned port contract and generated manifest, not this Markdown document.
