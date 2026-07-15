# Domain Model Template

## 1. Product / Module

`<name>`

## 2. Core Domain

What is the main business capability?

## 3. Subdomains

```text
Subdomain | Purpose | Priority
```

## 4. Bounded Contexts

```text
Context | Responsibility | Main Model
```

## 5. Ubiquitous Language

```text
Term | Meaning | Context
```

## 6. Entities

```text
Entity | Identity | Lifecycle | Context
```

## 7. Value Objects

```text
Value Object | Attributes | Validation Rule | Context
```

## 8. Aggregates

```text
Aggregate | Root | Invariants | Context
```

## 9. Domain Services

```text
Service | Responsibility | Why entity/value object cannot own it
```

## 10. Repositories

```text
Repository | Aggregate Root | Main Methods
```

## 11. Domain Events

```text
Event | Trigger | Consumers | Context
```

## 12. Business Rules

List rules that must always be true.

## 13. State Model

```text
state_a -> state_b -> state_c
```

## 14. Ports Needed

List external capabilities required by the domain or application layer.

## 15. Adapter Candidates

List possible replaceable implementations.

## 16. Evaluation Criteria

How will this domain behavior be reviewed and validated?

## 17. Open Questions

List unresolved modeling questions.
