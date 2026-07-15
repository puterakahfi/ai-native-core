# Domain First Rule

## Purpose

Ensure Native AI products start from business capability and domain model before choosing model, tool, framework, database, or adapter.

## Applies To

- Product design
- Feature design
- Architecture planning
- AI workflow design
- Adapter selection
- Implementation planning

## Must Do

1. Define product intent before implementation.
2. Define core domain before tool selection.
3. Identify bounded contexts before module structure.
4. Define ubiquitous language before database schema.
5. Define use cases before adapter selection.
6. Define business rules before prompt flow.
7. Define evaluation criteria before output approval.

## Must Not Do

1. Do not start architecture from model provider.
2. Do not start product design from prompt box.
3. Do not let web framework define the domain model.
4. Do not let database schema become the first domain artifact.
5. Do not let adapter capability override business rules.
6. Do not treat generated output as approved output.

## Correct Order

```text
Intent
-> Business Capability
-> Core Domain
-> Bounded Context
-> Domain Model
-> Use Case
-> Port
-> Adapter
-> Execution
-> Evaluation
```

## Review Checklist

- [ ] Product intent is clear.
- [ ] Core domain is named.
- [ ] Bounded contexts are identified if needed.
- [ ] Ubiquitous language exists.
- [ ] Domain model exists before adapter choice.
- [ ] Business rules are explicit.
- [ ] Evaluation criteria are defined.

## ExampleProduct Example

Correct:

```text
Creative Control -> Identity Lock -> Campaign Generation -> DesignGenerationPort -> selected adapter
```

Wrong:

```text
Design tool -> random creative output -> try to fit brand later
```
