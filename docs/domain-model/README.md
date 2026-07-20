# Native AI Engineering Canonical Domain Model

Status: Proposed canonical source of truth for issue `#6`

Philosophy authority: [`../philosophy/README.md`](../philosophy/README.md)

Atomic term authority: [`../philosophy/term-authority.md`](../philosophy/term-authority.md)

Discovery record: [`../native-ai-engineering-domain-model-discovery.md`](../native-ai-engineering-domain-model-discovery.md)

This directory defines the runtime-agnostic Native AI Engineering domain model: its bounded contexts, domain objects, lifecycle relationships, ownership, invariants, and extension boundaries.

It answers:

```text
what the first-class concepts are;
which context owns each concept;
how concepts relate across the engineering lifecycle;
which distinctions must never be collapsed;
which layers may specialize or implement the concepts;
which later issues own port taxonomy, schema shape, and validator behavior.
```

It does not implement runtime orchestration, choose providers, encode one product as universal, or replace the accepted philosophy foundation.

---

## 1. Authority

When accepted through issue `#6`, this directory is the canonical authority for:

- Native AI Engineering bounded contexts;
- domain objects and relationships;
- aggregate and invariant boundaries;
- lifecycle semantics;
- base meanings of workflow, skill, port, adapter, runtime, execution run, evidence, gate result, review, approval, delivery, and evolution;
- ownership and dependency direction between core, executable adapters, runtime, and products.

Authority order:

```text
accepted philosophy and atomic terms
→ accepted canonical domain model
→ accepted contracts and port semantics
→ executable skills, workflows, and adapters
→ runtime and product implementation
→ examples and historical documentation
```

A lower layer may specialize a concept. It may not reverse its base meaning, collapse a required distinction, or silently redefine it upstream.

---

## 2. Model at a glance

The domain is organized into ten bounded contexts:

```text
Intent & Specification
Capability & Agreement
Method & Workflow
Integration & Binding
Runtime & Execution
Context, Knowledge & Memory
Evidence, Evaluation & Review
Governance, Risk & Authority
Product, Delivery & Registry
Learning & Evolution
```

These are ownership boundaries, not deployment services, package folders, architecture layers, or mandatory repository splits.

The canonical lifecycle relationship is:

```text
IntentSpecification
→ Requirement and AcceptanceCriterion
→ DomainCapability and UseCase
→ CapabilityAgreement / Contract
→ Port requirement and AdapterBinding
→ WorkflowDefinition and SkillDefinition
→ CapacityAssessment and ExecutionAuthorization
→ ExecutionRun
→ Claim and EvidenceCase
→ GateResult, ReviewResult, and Approval where required
→ DeliveryRecord and Product Acceptance
→ FeedbackItem
→ LearningCandidate
→ accepted target-layer update or governed EvolutionProposal
```

No arrow means that the preceding artifact automatically authorizes or proves the next state.

---

## 3. Canonical base meanings

### Intent

An attributable expression of desired outcome, problem, need, constraint, or direction within scope.

Inferred intent remains explicitly labeled and cannot silently replace attributable intent.

### Requirement

A condition that must be satisfied by a capability, artifact, behavior, system, or delivery.

### Acceptance Criterion

A checkable condition used to determine whether a requirement or accepted objective has been satisfied within scope.

### Domain Capability

A stable ability required by the domain, independent of one provider, tool, runtime, or implementation.

### Use Case

A goal-oriented application of one or more domain capabilities for an actor or system boundary.

### Contract

A stable governed agreement defining what must remain true for a capability, workflow, runtime surface, port, evaluation, or other interface.

Contract presence is not implementation, conformance, execution, or product acceptance.

### Port

An abstract required capability and boundary through which a context requests behavior without owning a concrete implementation.

Issue `#7` owns the exhaustive port taxonomy and first-class port-contract shape.

### Adapter

A replaceable implementation or translation that binds a concrete runtime, provider, product, framework, or executable behavior to an upstream port or contract.

An adapter implements or specializes meaning; it does not own upstream canonical meaning.

Named base adapter specializations are:

```text
SkillAdapter       executable reusable method implementing a skill contract
RuntimeAdapter     runtime-specific implementation or integration
ProviderAdapter    provider or external-system integration
ProductAdapter     product-specific binding or specialization
FrameworkAdapter   framework or technology mapping behind a stable boundary
```

Issue `#7` may refine the exhaustive subtype taxonomy without reversing this base relationship.

### Skill

A repeatable executable procedure or specialist method for performing a bounded capability.

Skill declaration, installation, or metadata is not proof that the method was applied correctly.

### Workflow

A sequenced lifecycle that composes capabilities, skills, gates, ownership, evidence, handoffs, transitions, and exit conditions.

A workflow is not the same as the cross-domain Epistemic Loop or the Development Loop execution method.

### Runtime

An execution surface in which actors, agents, skills, workflows, tools, hooks, context, and adapters operate.

### Execution Run

A bounded actual attempt to execute authorized work in a named runtime and scope, with attributable steps, events, artifacts, and outcomes.

A plan, workflow definition, or requested action is not an execution run.

### Evidence

A typed, attributable, scoped item produced or preserved through a method that can support, weaken, distinguish, or challenge a claim.

Evidence is related to a claim; it is not an untyped output blob or approval by default.

### Gate Result

The outcome of evaluating a declared transition or quality condition against the applicable evidence and scope.

A passing gate supports only the transition or claim governed by that gate.

### Review

A qualified examination producing findings or a verdict against declared criteria.

Review is not approval unless the required authority and governing process explicitly assign approval meaning.

### Approval

An authority-bearing positive decision permitting a named action, transition, release, claim, risk acceptance, or canonical change under stated scope and conditions.

### Delivery

A recorded movement of an accepted artifact, change, capability, or release candidate into its intended target branch, environment, registry, or consumer boundary.

Delivery is not automatically product validation, adoption, or business outcome.

### Learning Candidate

A traceable proposal that a verified lesson may be reusable beyond its source case and should be evaluated for promotion to the smallest correct shared layer.

### Core Evolution

An accepted, governed change to a core-owned canonical definition, boundary, contract, law, principle, guardrail, or other shared agreement.

Local updates, product policy, adapter behavior, runtime state, or single field tests are not core evolution.

---

## 4. Required non-collapses

The model preserves:

```text
state ≠ observation
observation ≠ interpretation
interpretation ≠ inference
assumption ≠ fact
claim ≠ evidence
evidence ≠ approval
capability ≠ permission
permission ≠ authority
decision ≠ effective decision
review ≠ approval
verification ≠ validation
validation ≠ evaluation
contract presence ≠ conformance
static conformance ≠ executable behavior
workflow definition ≠ execution run
execution success ≠ completion
technical delivery ≠ product acceptance
feedback ≠ learning
learning candidate ≠ accepted evolution
memory ≠ source-of-truth knowledge
```

These distinctions are invariants, not documentation preferences.

---

## 5. Supporting model documents

- [`bounded-contexts.md`](bounded-contexts.md) — contexts, ownership, collaboration, and anti-corruption boundaries
- [`domain-objects.md`](domain-objects.md) — entities, value objects, aggregates, policies, commands, events, and invariants
- [`lifecycle-and-status.md`](lifecycle-and-status.md) — canonical lifecycle relation and typed status families
- [`ownership-and-dependencies.md`](ownership-and-dependencies.md) — repository ownership, dependency direction, and prohibited leakage
- [`philosophy-traceability.md`](philosophy-traceability.md) — accepted philosophy consequences in the domain model
- [`reconciliation.md`](reconciliation.md) — relationship to existing architecture, glossary, DDD guidance, contracts, and execution loops

The documents extend this entry point. They do not create competing meanings.

---

## 6. Downstream issue boundaries

This model supplies stable concepts and ownership to:

```text
#7  port kinds, adapter taxonomy details, first-class port contracts
#8  canonical schemas and workflow-contract serialization
#9  structured conformance declarations, evidence references, and result semantics
```

Downstream consumers must preserve this model. They may propose changes through governed core evolution; they may not silently decide unresolved upstream meaning locally.

---

## 7. Product and runtime boundary

Core owns runtime-agnostic meaning and relationships.

`ai-native-skills` owns executable reusable methods and workflow adapters.

`native-ai-fw` owns orchestration, control-plane behavior, discovery, runtime bindings, and execution-state implementation.

Product repositories own product intent, business policy, implementation, private context, provider selection, deployment configuration, acceptance, and field validation.

Examples may illustrate the model but never become mandatory provider, runtime, framework, or product behavior.

---

## 8. Acceptance status

This entry point remains proposed until issue `#6` completes:

- philosophy-to-domain traceability review;
- bounded-context and ownership review;
- object, aggregate, policy, event, and invariant review;
- lifecycle and status contradiction review;
- contract inventory mapping;
- architecture and glossary reconciliation;
- relative-link and applicable documentation validation;
- explicit owner acceptance or requested revision.
