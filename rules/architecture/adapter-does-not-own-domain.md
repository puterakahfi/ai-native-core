# Adapter Does Not Own Domain Rule

## Purpose

Prevent replaceable tools, providers, and frameworks from defining product domain, business rules, approval rules, or architecture decisions.

## Applies To

- Model adapters
- Coding adapters
- Design adapters
- Web framework adapters
- Storage adapters
- Publishing adapters
- Evaluation adapters

## Must Do

1. Keep business rules in domain or application layer.
2. Keep adapter logic behind ports.
3. Treat adapter output as draft until reviewed.
4. Require ADR for major adapter changes.
5. Evaluate adapter output against rules and contracts.
6. Keep provider-specific details out of domain entities.
7. Keep approval decisions outside automated adapter output by default.

## Must Not Do

1. Do not let model choice define product positioning.
2. Do not let coding tool choose architecture without review.
3. Do not let design tool change brand identity rules.
4. Do not let web framework define bounded contexts.
5. Do not let publishing integration bypass approval.
6. Do not let storage provider shape core domain language.
7. Do not let evaluation adapter approve final output alone.

## Boundary Rule

```text
Domain owns meaning.
Application owns use case.
Port owns capability contract.
Adapter owns implementation detail.
Evaluation owns quality gate.
Human owns critical approval by default.
```

## Review Checklist

- [ ] Adapter is behind a port.
- [ ] Domain language is independent from adapter terms.
- [ ] Business rules are not hidden inside tool-specific code.
- [ ] Adapter output goes through review.
- [ ] Approval gate is not bypassed.
- [ ] Adapter change does not silently change product behavior.

## ExampleProduct Example

Identity Lock is domain/application logic.

A model or design adapter can use Identity Lock as context, but it cannot decide that Identity Lock is optional.
