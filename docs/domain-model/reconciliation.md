# Canonical Domain Model Reconciliation

Status: Canonical cross-document reconciliation record

Entry point: [`README.md`](README.md)

This document classifies existing framework documents so they reference the canonical domain model instead of competing with it.

It preserves useful operational views and modeling guides while removing ambiguous authority.

---

## 1. Authority roles

| Artifact | Authority role |
|---|---|
| `docs/philosophy/**` | philosophy, atomic vocabulary, laws, principles, guardrails, epistemic loop, source-role governance |
| `docs/domain-model/**` | Native AI Engineering bounded contexts, objects, lifecycle, invariants, ownership, and domain relationships |
| accepted contracts | stable machine-readable capability and lifecycle agreements |
| `docs/architecture-v0.2.md` | operational architecture and dependency view |
| `docs/domain-driven-model.md` | domain-driven modeling guide and product-example teaching material |
| `docs/ports-and-adapters.md` | ports-and-adapters pattern and examples |
| issue `#7` output | final port kinds, adapter taxonomy, and port contracts |
| `docs/development-loop.md` | reusable engineering execution method |
| `docs/glossary.md` | navigation index and short labels |
| `ai-native-skills` | executable reusable methods and workflow adapters |
| `native-ai-fw` | orchestration, control plane, runtime state, and bindings |
| product repositories | product intent, policy, implementation, delivery, acceptance, and field validation |

---

## 2. Architecture v0.2 reconciliation

Current operational layers:

```text
Intent
Domain
Application
Contract
Port
Adapter
Agent
Rule
Skill
Knowledge
Evaluation
```

Reconciliation:

- keep the list as an operational dependency and responsibility view;
- do not interpret each layer as one bounded context;
- treat `Agent` as an actor specialization inside Runtime & Execution;
- treat `Rule` as a Governance object that may operationalize philosophy, contract, security, or product policy;
- treat `Skill` as a Method & Workflow object implemented downstream;
- treat `Knowledge` as part of Context, Knowledge & Memory;
- treat `Evaluation` as part of Evidence, Evaluation & Review;
- point canonical meanings and ownership to `docs/domain-model/`.

The architecture core flow remains useful:

```text
Intent
→ Domain Model
→ Use Case
→ Contract
→ Port
→ Adapter Selection
→ Authorized Execution
→ Evidence
→ Verification / Validation
→ Review / Approval where required
→ Delivery
→ Feedback and Governed Improvement
```

The canonical domain model expands this relationship with requirements, acceptance criteria, workflow and skill definitions, capacity, execution runs, typed gate results, completion claims, product acceptance, learning candidates, and evolution proposals.

No architecture version bump is required merely for adding the domain authority. Future architectural changes remain separately governed.

---

## 3. Domain-driven model guide reconciliation

Current role:

- explains DDD concepts;
- teaches business capability first, domain model second, ports third, adapters last;
- uses a creative product as an illustration.

Required reconciliation:

- mark the document as a modeling guide, not the canonical Native AI Engineering domain model;
- link the canonical domain model;
- preserve DDD definitions and anti-patterns;
- label all product concepts as illustrative;
- avoid saying “Native AI Framework core domain” when the example refers to a product core domain;
- use the canonical contexts and objects when describing Native AI Engineering itself.

The product example remains valid as an example. It cannot define universal entities such as `Brand`, `Campaign`, or `GeneratedAsset` in core.

---

## 4. Engineering Contract reconciliation

Current role:

- guides product or repository stack, architecture, security, testing, documentation, and review policy;
- contains concrete product/provider examples.

Canonical interpretation:

```text
Contract
  core base meaning: stable governed agreement

Product Engineering Contract
  product- or repository-owned specialization
  defining implementation ecosystem and engineering policy
```

Required boundaries:

- a product engineering contract may choose default providers and frameworks;
- it may specialize core requirements for the product;
- it does not become the universal parent type for every core contract;
- it does not override accepted core meaning silently;
- major changes preserve ADR, authority, compatibility, and evidence requirements.

The existing document should identify its product/repository policy role explicitly.

---

## 5. Ports and adapters reconciliation

Current role:

- explains stable domain, required capability, replaceable implementation;
- lists example ports and adapters;
- mixes provider, framework, product-surface, and control-plane boundaries.

Canonical interpretation:

```text
Port
  abstract required capability and boundary

Adapter
  replaceable implementation or translation binding a concrete target
  to an upstream port or contract
```

Required reconciliation:

- point base meanings and ownership to the canonical domain model;
- keep examples explicitly non-exhaustive;
- defer exhaustive port and adapter subtype taxonomy to issue `#7`;
- preserve provider and framework details downstream;
- avoid treating a web framework as domain meaning.

---

## 6. Port taxonomy reconciliation

Issue `#7` remains the authority for:

```text
port kinds
adapter subtype taxonomy
machine-readable port_contract shape
port dependency direction
port compatibility and conformance
```

Issue `#6` supplies:

- base port and adapter meanings;
- Integration & Binding context;
- AdapterBinding aggregate;
- dependency and ownership rules;
- capability/permission/authority separation;
- downstream specialization constraints.

Issue `#7` must not reverse these meanings.

---

## 7. Development Loop reconciliation

Current execution method:

```text
Explore → Plan → Implement → Verify → Review → Document → Deliver
```

Canonical role:

- reusable engineering execution method;
- may be used inside workflow phases;
- produces execution, evidence, review, documentation, and delivery records;
- remains distinct from domain lifecycle and Epistemic Loop.

Required corrections:

- `ReviewDisposition = completed` must not be described as authority-bearing approval by default;
- documentation-only shortcuts must not silently claim no verification or review is applicable when link, rendering, authority, or contradiction review matters;
- “changes are in target branch or environment” is a delivery condition, not total product completion;
- actual commands are one verification method, not the only possible verification method.

The Development Loop contract may later be refined through its own compatibility-governed change. Issue `#6` only establishes the relationship and avoids rewriting runtime behavior.

---

## 8. Glossary reconciliation

Current role:

- navigation index;
- short discovery definitions;
- points philosophy terms to atomic authority;
- defers domain objects to issue `#6`.

Required reconciliation:

- point domain-object terms to `docs/domain-model/README.md`;
- keep atomic philosophy terms delegated to `docs/philosophy/term-authority.md`;
- avoid duplicating complete context, aggregate, lifecycle, and status definitions;
- mark issue `#6` as accepted authority after merge;
- add missing navigation entries only where they improve discovery.

Authority order remains:

```text
atomic canonical term
→ canonical domain model
→ contract or port specialization
→ skill, workflow, adapter, runtime, or product specialization
→ example or historical document
```

---

## 9. Contract-family reconciliation

### Skill contracts

Domain relationship:

```text
DomainCapability / UseCase
→ CapabilityAgreement
→ SkillDefinition
→ SkillAdapter
→ behavioral evidence
```

Skill contract presence does not prove skill application.

### Workflow contracts

Domain relationship:

```text
WorkflowDefinition
→ PhaseDefinition / TransitionRule / HandoffDefinition / ExitCondition
→ executable workflow adapter
→ ExecutionRun
```

Workflow definition and execution run remain separate.

### Runtime contracts

Domain relationship:

```text
runtime-facing CapabilityAgreement
→ RuntimeAdapter or control-plane implementation
→ RuntimeEnvironment / ExecutionRun evidence
```

Static runtime contract conformance does not prove integration or product acceptance.

### Behavioral test contracts

Domain relationship:

```text
criteria and trigger
→ EvaluationResult / EvidenceCase
→ bounded conformance claim
```

Behavioral tests remain evidence contracts, not model-provider unit tests or approval records.

### Manifest

Domain role:

- registry of contract identity, path, checksum, and recorded version metadata;
- evidence for artifact identity and inventory only.

It is not implementation, runtime, or maturity evidence.

---

## 10. Adapter conformance reconciliation

Current evidence layers include:

```text
path resolution
version compatibility
structural declaration
boundary consistency
textual interface coverage
behavioral evaluation
runtime integration
product acceptance
```

Canonical relation:

- each layer creates scoped evidence for a named claim;
- one layer does not imply the others;
- conformance results belong to Evidence, Evaluation & Review;
- approval and product acceptance remain separate;
- issue `#9` owns structured validator-v2 semantics.

The domain model does not prescribe current validator implementation.

---

## 11. Memory and knowledge reconciliation

Canonical relation:

```text
SourceOfTruth
→ KnowledgeItem
→ ContextPack reference

MemoryReference
→ helps retrieve or reason
→ must verify current authoritative source before material claim or action
```

Memory cannot silently override knowledge, current state, policy, contract, decision, or approval.

---

## 12. Product-example reconciliation

Examples are allowed when they are:

- labeled illustrative;
- scoped to a product instance;
- absent from canonical aggregate requirements;
- not used to select universal providers or frameworks;
- not used as contract identity unless the contract is intentionally product-scoped.

Examples such as `Brand`, `Campaign`, `GeneratedAsset`, `Next.js`, `Codex`, or `OpenAI` remain downstream product or adapter concepts.

---

## 13. Historical layer and lifecycle maps

Historical documents may retain prior diagrams for traceability when clearly labeled.

They must not remain ambiguous active authorities.

Classification rule:

```text
accepted canonical model
  current object and ownership authority

operational architecture view
  current implementation/dependency explanation

modeling guide
  teaching method

historical view
  traceability only

example
  non-normative illustration
```

---

## 14. Required navigation updates

After acceptance:

- root `README.md` points domain readers to `docs/domain-model/README.md`;
- `architecture-v0.2.md` identifies the domain model as accepted authority;
- `domain-driven-model.md` identifies itself as a guide;
- `engineering-contract.md` identifies product/repository policy ownership;
- `ports-and-adapters.md` points base meanings to the domain model and taxonomy to `#7`;
- `development-loop.md` points lifecycle semantics to the domain model;
- `glossary.md` points domain objects to the accepted model.

---

## 15. Contradiction review

### Resolved by classification

```text
operational layer ≠ bounded context
modeling flow ≠ domain lifecycle
workflow definition ≠ Development Loop
Epistemic Loop ≠ delivery workflow
contract presence ≠ implementation
review verdict ≠ approval
execution success ≠ completion
technical delivery ≠ product acceptance
product example ≠ universal domain
```

### Deferred intentionally

```text
port and adapter exhaustive taxonomy            #7
contract and workflow schemas                   #8
structured conformance result semantics         #9
runtime implementation and state serialization  native-ai-fw
product specialization and acceptance            product repositories
```

### No path migration required

The domain-model change does not require existing contract paths to move. Contract and schema migrations remain separately approved downstream work.

---

## 16. Reconciliation verdict

```text
Philosophy remains upstream authority:                    YES
Canonical domain model has one entry point:               YES
Operational architecture preserved without competition:   YES
DDD guide preserved as guide:                             YES
Engineering Contract qualified as product specialization: YES
Ports/adapters base relationship preserved:               YES
Development and Epistemic loops remain distinct:          YES
Glossary remains navigation rather than authority:         YES
Contract paths preserved:                                  YES
Provider and product examples remain non-normative:        YES
Downstream issues retain their owned decisions:            YES
```
