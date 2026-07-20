# Native AI Engineering Ownership And Dependency Direction

Status: Canonical ownership and dependency model

Entry point: [`README.md`](README.md)

Bounded contexts: [`bounded-contexts.md`](bounded-contexts.md)

This document defines who owns meaning, agreement, executable behavior, orchestration, product policy, evidence, and evolution.

---

## 1. Repository ownership

### `ai-native-core`

Owns:

```text
accepted philosophy and atomic terms
canonical Native AI Engineering domain model
runtime-agnostic capability and lifecycle agreements
port and adapter base semantics
contract identity and compatibility expectations
architecture boundaries
reusable mandatory rules
public quality and evidence standards
governed core evolution
```

Does not own:

```text
runtime-installed behavior
provider credentials or commands
private product context
customer data
product-specific business policy
application implementation
production deployment state
field acceptance on behalf of a product
```

### `ai-native-skills`

Owns:

```text
executable reusable skill methods
workflow implementations
reviewer implementations
references, checklists, and rubrics
behavioral evaluation contracts and compatibility evidence
skill composition and routing behavior
```

Must preserve:

- core contract identity and version;
- core-owned inputs, outputs, gates, and boundaries;
- canonical domain meanings;
- explicit delegation and handoffs.

Does not own:

- universal domain redefinition;
- runtime orchestration state;
- product policy;
- provider authorization;
- core evolution by local edit.

### `native-ai-fw`

Owns:

```text
orchestration and control-plane behavior
product and task registries
skill discovery and resolution
context-pack assembly
runtime adapter registration
execution-run state
review and approval workflow integration
evidence capture and operational status
```

Must preserve:

- canonical object and status meanings;
- capability, permission, authority, and approval distinctions;
- contract and adapter boundaries;
- product repository ownership.

Does not own:

- universal domain meaning by runtime convenience;
- product business policy;
- automatic core evolution from runtime feedback.

### Product repositories

Own:

```text
product intent and domain specialization
product requirements and policy
implementation ecosystem and architecture decisions
product bindings and provider selection
private context, assets, and customer data
release and acceptance criteria
actual implementation and field validation
business outcomes
```

Must preserve:

- core terms and contract boundaries;
- upstream compatibility expectations;
- explicit product specialization;
- evidence and authority boundaries.

A product may propose core evolution. It may not present product-local policy or one field result as universal core by default.

### Providers and external tools

Own their own:

```text
API and operation semantics
credentials and access controls
provider-specific capabilities and limits
runtime behavior and service availability
```

They do not own Native AI Engineering domain meaning, product authority, or acceptance.

---

## 2. Canonical dependency direction

```text
Philosophy and atomic vocabulary
        ↓ constrain
Canonical domain model
        ↓ defines meaning and ownership for
Contracts and ports
        ↓ implemented or composed by
Skills, workflows, and adapters
        ↓ orchestrated by
Runtime and control plane
        ↓ specialized and accepted by
Product repositories
        ↓ produce
Field evidence and feedback
        ↓ may create
Affected-layer update or governed evolution proposal
```

The upward path is proposal and review, not silent mutation.

---

## 3. Meaning ownership versus implementation ownership

### Meaning owner

Defines what a concept means and which distinctions must remain stable.

Examples:

```text
core domain model owns ExecutionRun meaning
core term authority owns Evidence base meaning
product domain owns product-specific Campaign meaning
```

### Agreement owner

Defines a stable governed interface, boundary, or policy.

Examples:

```text
core contract owns reusable capability agreement
product engineering contract owns product stack policy
```

### Implementation owner

Defines how an agreement is executed in a concrete environment.

Examples:

```text
skill adapter owns executable method
runtime adapter owns runtime integration
product repository owns application implementation
```

### Evidence owner

Owns or preserves the attributable evidence item and method, not the claim it supports or the approval that may consume it.

### Decision authority

Owns the right to bind, approve, reject, delegate, supersede, or accept risk in a named scope.

These roles may be held by the same actor in one context, but they remain semantically separate.

---

## 4. Canonical ownership table

| Concept | Canonical owner | Common implementer or specialization |
|---|---|---|
| Atomic philosophy term | `ai-native-core/docs/philosophy` | all consumers inherit |
| Domain object and relation | `ai-native-core/docs/domain-model` | schemas, runtime, product models |
| Domain capability | core or product domain owner by scope | skills, services, adapters |
| Core contract | `ai-native-core` | skills/runtime/product adapters |
| Product engineering contract | product repository | product runtime and implementation |
| Port base meaning | canonical domain model | issue `#7` taxonomy and adapters |
| Port subtype and port contract | issue `#7` output in core | runtime/provider/product adapters |
| Skill method | `ai-native-skills` | installed runtime skill adapter |
| Workflow implementation | `ai-native-skills` or product repository by scope | runtime orchestration |
| Runtime environment and execution state | runtime/control plane | provider and product runtime adapters |
| Product binding | product repository or product registry | runtime adapter |
| Evidence item | producing source plus evidence context | evaluator/reviewer consumes |
| Review result | qualified reviewer/process | governance consumes |
| Approval | named authority in governing scope | runtime records and enforces |
| Delivery record | delivery owner or runtime | product acceptance consumes |
| Learning candidate | learning/evolution context | target-layer owner reviews |
| Core evolution | `ai-native-core` authority | downstream consumers migrate |

---

## 5. Dependency rules between bounded contexts

### Intent & Specification → Capability & Agreement

Capabilities and contracts trace to accepted requirements. Capability definitions do not rewrite intent.

### Capability & Agreement → Method & Workflow

Methods implement capabilities and agreements. Method convenience does not change capability meaning.

### Method & Workflow → Integration & Binding

Bindings are selected to execute methods. Provider availability does not define the method’s purpose.

### Integration & Binding → Runtime & Execution

Runtime executes through selected bindings. Runtime access does not confer approval authority.

### Runtime & Execution → Evidence, Evaluation & Review

Runtime produces observations and artifacts. The evidence context determines claim relation, scope, and coverage.

### Evidence, Evaluation & Review → Governance, Risk & Authority

Governance consumes findings and evidence. Evidence strength does not itself create authority.

### Governance, Risk & Authority → Product, Delivery & Registry

Governance permits, rejects, or conditions delivery. Product acceptance remains product-owned.

### Product, Delivery & Registry → Learning & Evolution

Product use and delivery produce feedback. Learning promotion remains governed by target-layer ownership.

### Context, Knowledge & Memory → all contexts

Context supports work through source references. It does not take ownership of the source object or target-context decision.

### Learning & Evolution → target context

Accepted evolution changes only the target layer named in the proposal. Broader promotion requires a new governed proposal.

---

## 6. Prohibited ownership leakage

### Provider leakage

Prohibited:

```text
provider API shape → universal domain object
provider model name → canonical capability
provider access → approval authority
```

Required response:

- keep provider concepts behind adapter bindings;
- introduce a product specialization if needed;
- propose core evolution only when transferable and approved.

### Runtime leakage

Prohibited:

```text
runtime state field → canonical lifecycle semantics
successful command → total completion
registered tool → permission or authority
```

Required response:

- map runtime state to canonical typed status families;
- preserve evidence scope and limitations;
- record authority references separately.

### Skill leakage

Prohibited:

```text
SKILL.md wording → core definition change
skill installation → behavior applied
skill behavior → product acceptance
```

Required response:

- preserve core contract and domain ownership;
- produce behavioral evidence;
- route shared changes through a learning candidate.

### Product leakage

Prohibited:

```text
one product policy → universal rule
one product entity → Native AI Engineering core entity
one field result → canonical agreement mutation
```

Required response:

- keep product meaning in product bounded contexts;
- use explicit qualified terms;
- propose transferability and compatibility review for shared evolution.

### Evidence leakage

Prohibited:

```text
one evidence item → every claim
review verdict → approval
static conformance → runtime behavior
technical validation → business success
```

Required response:

- bind evidence to claim, scope, method, and coverage;
- evaluate each required evidence layer independently;
- preserve authority-bearing decisions separately.

### Memory leakage

Prohibited:

```text
memory summary → current source of truth
prior decision → still-effective decision without validation
```

Required response:

- use memory to locate sources;
- verify current authority, version, and supersession.

---

## 7. Specialization rules

A downstream context may create qualified concepts such as:

```text
RepositoryExecutionRun
SecurityApproval
ProductAcceptanceCriterion
RuntimeEvidenceItem
DesignReviewResult
ProviderAdapterBinding
```

The specialization is valid only when:

1. it inherits the canonical base meaning;
2. added constraints and owner are explicit;
3. its scope is narrower than or compatible with the base concept;
4. it does not remove required distinctions;
5. it does not claim upstream authority.

---

## 8. Change routing

When a change is proposed, route it by responsibility.

### Change to atomic meaning, law, principle, or guardrail

Owner: philosophy foundation in `ai-native-core`.

### Change to domain object, context, lifecycle relation, or invariant

Owner: canonical domain model in `ai-native-core`.

### Change to port kind or adapter taxonomy

Owner: issue `#7` and resulting core artifacts.

### Change to contract or schema

Owner: core contract or issue `#8`, with compatibility handling.

### Change to executable reusable method

Owner: `ai-native-skills`.

### Change to orchestration or runtime state implementation

Owner: `native-ai-fw` or runtime adapter repository.

### Change to product behavior or policy

Owner: product repository.

### Reusable lesson from field evidence

Owner initially: learning candidate in the source context.

Promotion owner: smallest correct target-layer authority.

---

## 9. Evolution authority

Core evolution requires:

```text
attributable proposal
+ affected canonical object or agreement
+ source evidence and learning candidate
+ transferability and counterexamples
+ compatibility and consumer impact
+ validation and migration plan
+ core authority acceptance
```

Downstream repositories may implement local fixes immediately when authorized. They must not label the local fix as accepted core evolution before this process completes.

---

## 10. Ownership invariants

1. Every first-class concept has one canonical semantic owner.
2. Physical repository location does not automatically define semantic authority.
3. Technical access, repository permission, and runtime capability do not imply decision authority.
4. Downstream specialization inherits upstream meaning.
5. Cross-context references do not transfer aggregate ownership.
6. Product and provider facts remain downstream unless accepted through governed evolution.
7. Evidence and review inform authority; they do not replace authority.
8. Feedback updates the smallest correct layer first.
9. Canonical change preserves compatibility, migration, and consumer impact.
