# Bounded Context Template

## 1. Context Name

`<context-name>`

## 2. Purpose

What business capability does this context own?

## 3. Why It Matters

Why does this context need a clear boundary?

## 4. Ubiquitous Language

```text
Term | Meaning | Notes
```

## 5. Main Actors

Who interacts with this context?

## 6. Main Use Cases

```text
Use Case | Actor | Outcome
```

## 7. Entities

List entities with identity and lifecycle.

## 8. Value Objects

List immutable values and rule objects.

## 9. Aggregates

Define consistency boundaries.

## 10. Domain Services

List domain services only when logic does not belong naturally to one entity or value object.

## 11. Domain Events

List meaningful business state changes.

## 12. Business Rules

List rules that must always be true.

## 13. Ports Needed

List required external capabilities.

## 14. Adapters Allowed

List possible adapter categories, not hard dependencies.

## 15. Human Review Points

Where is human approval required?

## 16. Evaluation Criteria

How should output or behavior be evaluated?

## 17. Open Questions

List unresolved decisions.
