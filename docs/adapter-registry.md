# Adapter Registry

## Purpose

The Adapter Registry documents replaceable implementations for Native AI Framework ports.

The framework core should define what capability is needed. The adapter registry documents which tool or provider currently implements that capability.

## Design Principle

```text
Port = required capability
Adapter = replaceable implementation
```

## Registry Format

Each adapter entry should include:

```text
- Port name
- Adapter name
- Purpose
- Capabilities
- Limitations
- Risk level
- Required approval
- Failure behavior
- Replacement options
```

## Common Ports

```text
ModelInferencePort
CodeExecutionPort
DesignGenerationPort
DesignReviewPort
WebAppPort
RepositoryPort
DatabasePort
StoragePort
PublishingPort
EvaluationPort
ObservabilityPort
```

## Example Registry

```text
Port: CodeExecutionPort
Current adapter: project-specific
Alternatives: allowed
Risk level: medium to high
Approval: required for large changes, destructive changes, dependency changes, and architecture changes
```

```text
Port: DesignGenerationPort
Current adapter: project-specific
Alternatives: allowed
Risk level: medium
Approval: required for public-facing brand output
```

```text
Port: WebAppPort
Current adapter: project-specific
Alternatives: allowed through ADR
Risk level: high
Approval: required for framework migration
```

## Adapter Change Rule

Changing an adapter is allowed, but the change must not silently change the product domain.

Major adapter changes require ADR when they affect:

```text
architecture
cost
security
workflow
output quality
developer experience
runtime behavior
product capability
```

## Anti-Pattern

Wrong:

```text
We use one tool, therefore the framework is designed around that tool.
```

Correct:

```text
The framework defines the capability. The tool implements the capability.
```
