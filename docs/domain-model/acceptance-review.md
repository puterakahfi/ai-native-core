# Canonical Domain Model Acceptance Review

Status: Final review evidence for issue `#6`

Entry point: [`README.md`](README.md)

Discovery record: [`../native-ai-engineering-domain-model-discovery.md`](../native-ai-engineering-domain-model-discovery.md)

This review tests completeness, ownership, contradiction handling, minimality, and downstream usefulness of the proposed canonical Native AI Engineering domain model.

---

## 1. Acceptance scope

Issue `#6` accepts:

- canonical bounded contexts;
- domain objects and relationships;
- aggregates and invariants;
- policies, commands, and events;
- lifecycle and typed status semantics;
- repository and layer ownership;
- philosophy-to-domain traceability;
- cross-document reconciliation.

It does not accept:

- final port taxonomy or port schema (`#7`);
- unified contract schemas (`#8`);
- validator-v2 declarations and result schema (`#9`);
- runtime orchestration implementation;
- downstream repository migration;
- one product or provider as universal.

---

## 2. Philosophy preservation review

| Required foundation distinction | Domain-model representation | Verdict |
|---|---|---|
| state ≠ observation | atomic term authority plus observation/source relations | preserved |
| observation ≠ interpretation ≠ inference | separate epistemic concepts and dispositions | preserved |
| assumption ≠ fact | typed epistemic disposition and evidence requirement | preserved |
| claim ≠ evidence | `Claim` and `EvidenceItem` in `EvidenceCase` | preserved |
| capability ≠ permission ≠ authority | `DomainCapability`, `PermissionGrant`, `AuthorityGrant` | preserved |
| decision ≠ effective decision ≠ approval | `Decision`, `EffectiveDecisionAssessment`, `Approval` | preserved |
| verification ≠ validation ≠ evaluation ≠ review | separate result entities | preserved |
| scope ≠ coverage | shared value objects with separate roles | preserved |
| feedback ≠ learning candidate ≠ evolution | Learning & Evolution entities and policy | preserved |
| memory ≠ source-of-truth knowledge | separate `MemoryReference` and `KnowledgeItem` | preserved |
| execution success ≠ completion | `ExecutionStatus` and `CompletionDisposition` | preserved |
| review ≠ approval | separate contexts, entities, and status families | preserved |

Verdict: the model consumes the accepted philosophy without redefining it or creating a competing atomic vocabulary.

---

## 3. Bounded-context review

| Context | Unique ownership contribution | Overlap control | Verdict |
|---|---|---|---|
| Intent & Specification | attributable intent, requirements, acceptance, scope | does not own method or execution | retained |
| Capability & Agreement | stable capability, use case, contract identity and boundary | does not own implementation | retained |
| Method & Workflow | reusable procedure and lifecycle composition | definition remains separate from run | retained |
| Integration & Binding | replaceable binding and implementation compatibility | final taxonomy deferred to `#7` | retained |
| Runtime & Execution | actual runtime state, run, step, invocation, artifact | does not own approval or product acceptance | retained |
| Context, Knowledge & Memory | attributable context, source, gap, staleness | does not take source or target-decision ownership | retained |
| Evidence, Evaluation & Review | claims, evidence, criteria, findings, gates, completion claim | approval remains governance-owned | retained |
| Governance, Risk & Authority | policy, permission, authority, decision, approval, risk | does not produce execution evidence | retained |
| Product, Delivery & Registry | downstream product binding, delivery, acceptance relation | concrete policy stays in product repo | retained |
| Learning & Evolution | affected-layer update and shared promotion | local feedback cannot mutate core | retained |

Minimality verdict:

- no context is merely an architecture layer renamed;
- no context is a provider, tool, framework, or product category;
- Context/Knowledge remains cross-cutting but owns distinct source and staleness invariants;
- Evidence/Review and Governance/Approval remain separate because their authority and lifecycle differ;
- Product/Delivery remains separate from Runtime/Execution because technical execution and product acceptance differ;
- Learning/Evolution remains separate because governed promotion has distinct authority and compatibility invariants.

---

## 4. Aggregate review

| Aggregate | Invariant protected | Verdict |
|---|---|---|
| `IntentSpecification` | traceability from intent through acceptance and non-goals | sufficient |
| `CapabilityAgreement` | stable capability, contract identity, gates, boundary, compatibility | sufficient |
| `WorkflowDefinition` | phases, transitions, handoffs, exits, evidence requirements | sufficient |
| `AdapterBinding` | upstream meaning, compatibility, limitations, delegation | sufficient |
| `ExecutionRun` | actual execution, steps, tool outcomes, runtime status | sufficient |
| `ContextPack` | source attribution, staleness, gaps, knowledge/memory separation | sufficient |
| `EvidenceCase` | claim/evidence relation, coverage, verification, review, gate, completion | sufficient |
| `AuthorityDecision` | decision effectiveness, authority, approval, risk, exception | sufficient |
| `ProductBindingRegistry` / `ProductDeliveryCase` | product specialization, target delivery, acceptance, consumer impact | sufficient |
| `LearningEvolutionCase` | local update, transferability, compatibility, evolution authority | sufficient |

No universal aggregate includes product-private data, provider credentials, concrete runtime commands, or application implementation.

---

## 5. First-class concept ownership audit

| Concept family | Canonical owner |
|---|---|
| intent, requirement, acceptance criterion, constraint, non-goal | Intent & Specification |
| capability, use case, contract identity/version/boundary/gates | Capability & Agreement |
| skill definition, workflow definition, phase, transition, handoff | Method & Workflow |
| port reference, adapter binding, provider/product/framework binding | Integration & Binding; subtype taxonomy deferred to `#7` |
| runtime, actor, agent, execution run, step, invocation, artifact | Runtime & Execution |
| context pack, source reference, knowledge, memory, staleness, gap | Context, Knowledge & Memory |
| claim, evidence, verification, validation, evaluation, review, gate, completion | Evidence, Evaluation & Review |
| rule, policy, permission, authority, decision, approval, risk, exception | Governance, Risk & Authority |
| product instance, product binding, delivery, release acceptance, consumer impact | Product, Delivery & Registry |
| feedback, update, learning, candidate, compatibility impact, evolution | Learning & Evolution |
| model provider, SDK, framework, deployment tool | downstream adapter or product implementation |
| private customer/product data | product repository |
| runtime orchestration state implementation | `native-ai-fw` or runtime adapter |
| executable reusable methodology | `ai-native-skills` |

Verdict: every currently named first-class concept is owned or has an explicit downstream extension point.

---

## 6. Contract inventory mapping

The generated manifest currently registers 108 contract artifacts. The manifest remains the row-level inventory authority.

The domain model maps contract families and categories without copying all rows.

### Skill contract categories

| Manifest category | Primary domain context | Supporting contexts |
|---|---|---|
| architecture | Capability & Agreement; Method & Workflow | Governance; Integration & Binding |
| content | Capability & Agreement; Method & Workflow | Product; Evidence |
| context | Context, Knowledge & Memory; Method & Workflow | Evidence |
| design | Capability & Agreement; Method & Workflow | Evidence; Product |
| engineering | Method & Workflow; Capability & Agreement | Runtime; Evidence; Governance |
| governance | Governance, Risk & Authority; Method & Workflow | Evidence |
| meta | Method & Workflow | Context; Governance; Learning |
| product | Intent & Specification; Product, Delivery & Registry | Evidence; Governance |
| quality | Evidence, Evaluation & Review; Method & Workflow | Governance |
| runtime | Runtime & Execution; Method & Workflow | Integration & Binding; Evidence |
| security | Governance, Risk & Authority; Evidence, Evaluation & Review | Runtime |
| visual thinking | Method & Workflow; Evidence, Evaluation & Review | Context |

A category is an inventory/navigation classification, not automatically a bounded context.

### Workflow contracts

Primary owner: Method & Workflow.

Relations:

- requirements from Intent & Specification;
- capability and gates from Capability & Agreement;
- execution evidence from Runtime & Execution;
- gate/review evidence from Evidence, Evaluation & Review;
- approval policy from Governance;
- product acceptance from Product, Delivery & Registry.

### Runtime contracts

Primary owner: Runtime & Execution or the context matching the runtime-facing capability.

Static runtime contracts remain Capability Agreements. Implemented runtime state remains downstream.

### Behavioral test contracts

Primary owner: Evidence, Evaluation & Review.

They define criteria and expected behavior evidence; they are not provider unit tests or approval records.

### Manifest

Owner: Capability & Agreement registry/inventory concern.

It proves identity, path, checksum, and recorded version metadata only.

Verdict: no contract path or family requires migration for issue `#6`.

---

## 7. Lifecycle contradiction review

| Existing map | Canonical classification | Conflict resolution |
|---|---|---|
| Architecture v0.1 lifecycle | historical architecture view | retained as historical explanation |
| Architecture v0.2 core flow | operational relationship view | points to expanded canonical lifecycle |
| DDD modeling flow | modeling method | not treated as execution lifecycle |
| Development Loop | reusable engineering execution method | not workflow or domain lifecycle |
| Epistemic Loop | reasoning discipline | not delivery workflow |
| Workflow contract phases | capability-specific lifecycle | definition separate from execution run |
| Issue #6 required relation | canonical cross-context relationship | represented in lifecycle document |

Resolved non-collapses:

```text
operational layer ≠ bounded context
modeling flow ≠ execution lifecycle
workflow definition ≠ execution run
review result ≠ approval
execution succeeded ≠ completion
completion ≠ delivery
delivery ≠ product acceptance
feedback ≠ evolution
```

Legacy Development Loop review/approval wording is recorded and delegated to versioned follow-up issue `#26`; it is not silently changed in issue `#6`.

---

## 8. Status-family review

The model defines separate families for:

```text
EpistemicDisposition
SpecificationStatus
ContractStatus
BindingStatus
CapacityDisposition
ExecutionStatus
GateOutcome
ReviewDisposition
ApprovalStatus
CompletionDisposition
DeliveryStatus
ProductAcceptanceStatus
EvolutionStatus
```

Review verdict:

- no family can substitute for another;
- partial, blocked, unknown, not-verified, rejected, revoked, expired, and superseded states remain representable;
- machine enum shape is deferred to `#8`;
- runtime serialization is deferred to `native-ai-fw`.

---

## 9. Ownership and leakage review

Prohibited directions are explicit for:

- provider → universal domain meaning;
- adapter → canonical term or contract redefinition;
- runtime access → authority;
- skill installation → embodiment;
- product policy → universal core;
- evidence item → unlimited claim;
- review → approval;
- memory → current source of truth;
- single field test → core evolution.

Every prohibited direction has an explicit routing response through binding, evidence, governance, product specialization, or learning/evolution.

---

## 10. Downstream usefulness review

### `#7` receives

- base Port and Adapter meanings;
- Integration & Binding context;
- adapter base specializations;
- ownership and leakage rules;
- compatibility and limitation relationships.

### `#8` receives

- canonical object and aggregate names;
- required separations;
- typed status families;
- claim/evidence scope and coverage;
- workflow definition versus execution-run boundary;
- contract identity/version/boundary relationships.

### `#9` receives

- conformance as evidence-layered claim;
- structural declaration versus executable behavior distinction;
- unsupported/not-checkable need;
- evidence references, scope, and coverage;
- no static result as runtime or product proof.

### `ai-native-skills` receives

- Skill and Workflow base meanings;
- SkillAdapter ownership direction;
- behavior/installation/conformance distinctions.

### `native-ai-fw` receives

- RuntimeEnvironment, ExecutionRun, CapacityAssessment, typed statuses, evidence references, and approval separation.

### Product repositories receive

- ProductInstance and product-binding boundary;
- concrete policy and acceptance ownership;
- field evidence and learning-candidate route.

Verdict: each named downstream consumer receives decision-changing input rather than background prose.

---

## 11. Minimality and duplicate review

Retained because independently necessary:

- Intent and Requirement: source desire versus checkable condition;
- Capability and Use Case: stable ability versus goal-oriented application;
- Contract and Port: stable agreement versus requested abstract boundary;
- Skill and Workflow: bounded procedure versus sequenced composition;
- Runtime and ExecutionRun: execution surface versus one actual attempt;
- Evidence and Review: attributable support versus qualified examination;
- Review and Approval: findings versus authority-bearing permission;
- Delivery and Product Acceptance: movement versus intended-use acceptance;
- Learning Candidate and Evolution Proposal: reusable possibility versus governed change request.

Merged or rejected:

- architecture layers are not duplicated as bounded contexts;
- contract categories are not duplicated as bounded contexts;
- provider/tool/framework names are excluded from canonical objects;
- historical lifecycle diagrams are classified, not rebuilt;
- product-example entities remain examples;
- atomic philosophy definitions are referenced, not copied as new domain definitions.

---

## 12. Documentation and path review

Required navigation targets:

```text
README.md
docs/architecture-v0.2.md
docs/domain-driven-model.md
docs/engineering-contract.md
docs/ports-and-adapters.md
docs/development-loop.md
docs/glossary.md
```

All point to the canonical model or its lifecycle semantics on the issue branch.

Relative-link validation covers the root README and all Markdown files under `docs/`.

No contract, schema, manifest, or validator path is changed by this domain-model work.

---

## 13. Known follow-up

Issue `#26` owns the versioned Development Loop contract correction for legacy review `APPROVE` and documentation-only shortcut semantics.

This known contract wording does not block accepting the domain model because:

- the canonical distinction is explicit;
- active contract behavior is not silently changed;
- compatibility-governed correction has a named owner;
- downstream consumers can already distinguish ReviewResult and Approval in the model.

---

## 14. Final verdict

```text
Philosophy terminology preserved:                    PASS
One canonical domain-model entry point:              PASS
Bounded contexts and ownership explicit:             PASS
Entities and value objects defined:                   PASS
Aggregates and invariants defined:                    PASS
Policies, commands, and events defined:               PASS
Port, adapter, skill, workflow, runtime meanings:     PASS
Evidence, gate, review, approval meanings:            PASS
Typed lifecycle statuses separated:                  PASS
Learning and evolution governed:                     PASS
Conflicting layer/lifecycle maps reconciled:          PASS
Dependency direction and prohibited leakage:          PASS
Product/runtime examples kept downstream:             PASS
Glossary and architecture navigation reconciled:      PASS
Existing contract paths preserved:                   PASS
Contract inventory has explicit context mapping:      PASS
Downstream #7–#9 receive explicit inputs:             PASS
Known legacy runtime-contract wording has owner:       PASS WITH FOLLOW-UP #26
```

Recommendation: promote `docs/domain-model/README.md` and supporting documents from proposed status to canonical status, complete final documentation validation, and request owner acceptance of issue `#6`.
