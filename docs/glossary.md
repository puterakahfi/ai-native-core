# Native AI Core — Glossary Index

Status: Navigation index

Philosophy-level term authority: [`philosophy/term-authority.md`](philosophy/term-authority.md)

Philosophy entry point: [`philosophy/README.md`](philosophy/README.md)

Canonical domain model: [`domain-model/README.md`](domain-model/README.md)

Native AI OS terminology boundary: [`native-ai-os.md`](native-ai-os.md)

This glossary helps readers discover terms used across `ai-native-core` contracts, documentation, ports, adapters, evaluation material, and operating-system integrations.

It is not a competing atomic definition authority.

For philosophy-level terms such as `state`, `model`, `assumption`, `claim`, `evidence`, `authority`, `verification`, `validation`, `feedback`, `capacity`, `coherence`, `embodiment`, and `core evolution`, the minimum candidate meaning is owned by [`philosophy/term-authority.md`](philosophy/term-authority.md).

For complete Native AI Engineering domain objects, aggregates, bounded contexts, and lifecycle semantics, use the [canonical domain model](domain-model/README.md).

For the distinction among Native AI Engineering, Native AI Core, Native AI OS, framework, runtime, control plane, and Product Brain, use the [Native AI OS boundary](native-ai-os.md).

---

## A

**ADD — Agent-Driven Development**  
An engineering approach in which agents perform meaningful lifecycle work under explicit intent, contracts, boundaries, evidence, review, and authority. Humans and organizations retain the decision rights required by the governing scope and risk.

**Adapter**  
A replaceable implementation or translation that binds a runtime, provider, product, framework, or executable behavior to a core-owned port or contract. An adapter implements or specializes an agreement; it must not silently redefine upstream domain meaning or canonical terms.

**Agent**  
An AI actor assigned bounded responsibilities and capabilities. An agent may reason, use tools, produce artifacts, and execute authorized work. Agent capability or confidence is not authority or approval.

**AGENTS.md**  
A runtime-agnostic project context file containing repository-specific commands, conventions, architecture constraints, and prohibitions for agents. Product or repository context remains outside universal core semantics.

**Approval**  
An authority-bearing positive decision permitting a named action, transition, release, risk acceptance, claim, or canonical change within a bounded scope. See the atomic definition in [`philosophy/term-authority.md`](philosophy/term-authority.md).

---

## B

**Bounded Context**  
A boundary within which a domain model and ubiquitous language remain internally consistent. Different contexts may specialize the same base term without contradicting its canonical upstream meaning.

---

## C

**Capability**  
The ability of an actor, agent, tool, adapter, or system to perform a category of action or produce a category of result. Capability is not permission, authority, approval, quality proof, or successful execution. See [`philosophy/term-authority.md`](philosophy/term-authority.md).

**Coherence**  
The degree to which material intent, requirements, definitions, decisions, contracts, architecture, implementation, behavior, evidence, and approval state can coexist without unresolved contradiction inside a stated scope. See [`philosophy/term-authority.md`](philosophy/term-authority.md).

**Conformance**  
The degree to which an implementation, adapter, artifact, or behavior satisfies applicable contract or standard requirements. A conformance claim must name its evidence layer, such as path resolution, version compatibility, structural declaration, boundary consistency, behavioral execution, runtime integration, or product acceptance. See [Adapter Conformance](adapter-conformance.md).

**Context Engineering**  
The discipline of providing relevant, attributable, timely context to an agent or system while preserving source, scope, authority, and uncertainty boundaries.

**Contract**  
A stable machine-readable agreement defining what must remain true about a capability, workflow, runtime component, port, evaluation, or other governed interface. Contracts define stable expectations; executable skills, workflows, adapters, and runtimes implement them.

**Contract Version**  
A semantic or pre-stable version associated with a contract so consumers can declare compatibility and detect breaking changes. Version labels do not prove implementation quality or maturity by themselves.

**Control Plane**  
A coordination boundary that resolves and governs product-level work across contexts without becoming every semantic owner, external execution provider, product-acceptance owner, or authority source. A control plane may coordinate context, planning, capability resolution, execution requests, evidence, gates, reviews, approvals, learning proposals, and observability. Coordination capability is not automatic permission, authority, approval, execution, or product acceptance. See [Native AI OS](native-ai-os.md).

**Core**  
The `ai-native-core` repository and its accepted runtime-agnostic domain language, ports, contracts, architecture boundaries, rules, templates, and quality standards.

**Coverage**  
The portion of a declared scope that was actually observed, executed, evaluated, reviewed, or supported by evidence. Coverage is not quality or completion by itself.

---

## D

**Decision**  
A recorded selection, rejection, commitment, or constraint among alternatives intended to govern action within a stated scope. A decision may remain non-authoritative, conflicted, superseded, or pending approval. See [`philosophy/term-authority.md`](philosophy/term-authority.md).

**Development Loop**  
The canonical execution cycle:

```text
Explore → Plan → Implement → Verify → Review → Document → Deliver
```

The Development Loop owns execution phases, gates, outputs, and transitions. The Epistemic Loop governs reasoning about state, models, capacity, evidence, and updates inside those phases.

---

## E

**Embodiment**  
The state in which a declared principle, rule, contract, skill, or workflow changes repeatable executable behavior and can produce evidence appropriate to the claim. Documentation, installation, or metadata presence alone is not embodiment.

**Evidence**  
Attributable information produced or preserved through a method that can support, weaken, distinguish, or challenge a claim within bounded scope. Evidence is not authority, approval, or complete truth by default. See [`philosophy/term-authority.md`](philosophy/term-authority.md).

**Evaluation**  
A systematic assessment against declared criteria producing findings, measurements, evidence, and optionally a verdict. Evaluation is not approval or runtime enforcement by default.

**Exit Gate**  
A checkable condition that must be satisfied before a lifecycle phase, claim, promotion, release, or other governed transition may proceed.

---

## F

**Fact**  
A proposition treated as established within a stated scope because available attributable evidence satisfies the relevant verification standard. A fact is bounded by time, version, environment, method, and coverage; it is not authority to act.

**Feedback**  
Attributable information produced by execution, observation, evaluation, review, use, measurement, or consequence that can support revision of a model, decision, behavior, implementation, or affected layer. Feedback is not automatically correct, authoritative, or final truth.

**Framework**  
A reusable architecture, SDK, library, or implementation structure that supplies conventions and extension points. `Framework` remains valid when an actual technical framework is meant. It is not the canonical product-level name for Native AI OS, and framework presence alone does not prove operating-system qualification.

---

## G

**Gate / Quality Gate**  
A checkable condition controlling whether work may transition, a claim may be made, or an artifact may be promoted. Gates operationalize contracts, guardrails, and policies in a specific lifecycle.

**Guardrail**  
A stable mandatory boundary protecting authority, safety, truthfulness, scope, evidence, or canonical ownership. A guardrail must define the required block, narrow, route, review, escalation, or status response when violated.

---

## H

**Hook**  
A deterministic script or integration triggered at a named lifecycle point. A hook can enforce selected behavior, but its presence does not prove complete policy or product correctness.

---

## I

**Implements**  
Metadata used by an adapter or executable artifact to declare which core contract it intends to implement. The declaration is not proof of behavioral conformance.

**Inference**  
A proposition derived from observations, evidence, prior models, or reasoning rather than directly recorded as the observed state itself. Inference must remain distinguishable from fact when material.

---

## K

**Knowledge**  
Explicit, reviewable information accepted for use within a stated scope and maintained in an attributable source-of-truth artifact or system. Knowledge is not memory or immutable truth by default.

---

## L

**Learning Candidate**  
A traceable proposal that a verified lesson may be reusable beyond its source case and should be evaluated for promotion to the smallest correct shared layer. A learning candidate is not yet an accepted rule, contract, skill change, or core evolution.

---

## M

**Manifest**  
The generated contract registry at `contracts/manifest.yaml`, containing contract identity, path, checksum, and recorded version metadata. It is an inventory source, not proof of executable implementation.

**Memory**  
Retained context, history, preference, pattern, or prior outcome used to support retrieval and reasoning across time. Memory is not authoritative knowledge, current state, or approval by default.

**Meta-Skill**  
An executable skill that routes, composes, or coordinates other capabilities rather than owning all specialist methodology itself.

**Model**  
A bounded representation used for interpretation, prediction, planning, communication, or execution. A model may be useful and verified while remaining different from the state it represents.

---

## N

**Native AI Core**  
The public, runtime-agnostic source of truth for Native AI Engineering domain language, contracts, ports, architecture boundaries, rules, templates, and quality standards. Core defines stable meaning and agreements; it does not implement the complete operating system.

**Native AI Engineering**  
The discipline, principles, canonical domain model, contracts, lifecycle agreements, authority boundaries, and working model for building AI-native systems.

**Native AI OS**  
An executable product and control-plane system that applies Native AI Engineering across product lifecycles by coordinating product context, persistent lifecycle state, capabilities, workflows, agents, runtimes, adapters, authorized execution, artifacts, evidence, review, governance, feedback, learning, and observability. It consumes and specializes core meaning without silently redefining canonical domain objects, authority, or approval. See [`native-ai-os.md`](native-ai-os.md).

---

## O

**Observation**  
An attributable record produced by an observation path about a bounded subject, time, environment, and coverage. Observation is not interpretation or fact by default.

---

## P

**Permission**  
A technical, policy, or access-control allowance to attempt a named operation within bounded scope. Permission may be necessary but is not sufficient authority or approval.

**Phase**  
A named step in a workflow or execution loop with declared purpose, outputs, gates, and transitions.

**Port**  
An abstract capability and boundary through which an application, product, control plane, or integration requests behavior without owning a concrete implementation. The canonical taxonomy remains owned by issue `#7`.

**Principle**  
A preferred decision orientation used when multiple valid options remain. A principle guides but does not silently block action.

**Product Brain**  
Informal product language for a combined product-context, registry, decision, knowledge, memory, planning, and coordination experience. It is not a canonical aggregate, bounded context, contract family, or authority source in Native AI Core.

**Product Instance**  
A product-specific source-of-truth boundary containing product intent, policy, configuration, implementation, and validation that must not be generalized into universal core by default.

---

## R

**Review**  
An examination of an artifact, decision, implementation, behavior, or evidence set against declared criteria by a qualified actor or process. A review may produce findings or a verdict; it is approval only when the required authority and process explicitly assign approval meaning.

**Rule**  
A reusable mandatory constraint stating what must or must not happen in a declared scope. Rules may operationalize philosophy guardrails, contracts, architecture boundaries, security requirements, or repository policy.

**Runtime**  
An execution surface in which agents, skills, tools, hooks, context, and adapters operate. Runtime behavior remains distinct from static declarations, Native AI OS qualification, and product acceptance. A runtime may be one component of Native AI OS without being the complete operating system.

**Runtime Contract**  
An implementation-agnostic agreement governing runtime-facing capabilities or lifecycle behavior under `contracts/runtime/`.

---

## S

**Scope**  
The explicit boundary of subjects, actions, claims, environments, time, consumers, risks, and responsibilities to which an instruction, decision, evidence item, contract, or approval applies.

**Shortcut**  
A declared, policy-authorized reduced lifecycle path for bounded low-risk work. A shortcut must identify skipped gates and residual evidence; silent omission is not a shortcut.

**Skill**  
A repeatable executable procedure for performing a bounded capability, typically represented by a `SKILL.md` implementation. Skill presence or installation is not proof that the behavior was applied.

**Skill Adapter**  
An executable skill implementation that binds or specializes a reusable core skill contract while preserving explicit ownership and delegation boundaries.

**Skill Contract**  
A YAML agreement defining a reusable skill capability, roles, inputs, outputs, quality gates, boundaries, and adapter requirements.

**Source of Truth**  
An artifact, record, or system designated by relevant authority as the current primary reference for a named class of definition, decision, policy, state, or knowledge.

**Stability**  
The condition in which an artifact or agreement has explicit ownership, known compatibility expectations, controlled change behavior, validation requirements, and reliable consumer expectations. Stability does not mean immutability.

---

## T

**Transition**  
An allowed movement between lifecycle states or phases under declared conditions and gates.

---

## V

**Validation**  
The process of determining whether a system, artifact, decision, or behavior is fit for its intended use, need, context, and acceptance scope.

**Verification**  
The process of determining whether a specified claim, requirement, contract, property, or result is supported by appropriate evidence. Running a real command is one verification method; verification also applies to source, authority, contract identity, and other bounded claims.

**Version Pinning**  
A compatibility declaration binding an adapter or consumer to an accepted contract version range. A compatible pin is necessary evidence for compatibility but not proof of behavioral conformance.

---

## W

**Workflow**  
A sequenced lifecycle composing capabilities, skills, gates, ownership, evidence, handoffs, and exit conditions.

**Workflow Contract**  
A stable machine-readable agreement defining workflow phases, transitions, gates, ownership, evidence expectations, handoffs, and exit conditions. Executable methodology remains in skills or workflow implementations.

---

## Authority Reminder

When definitions appear to conflict, use this order:

```text
accepted atomic canonical term
→ accepted canonical domain model
→ accepted contract or port specialization
→ accepted Native AI OS architecture boundary
→ specialized rule, skill, workflow, or adapter meaning
→ runtime or product implementation
→ examples and historical documentation
```

Accepted philosophy terms and the canonical domain model do not silently rewrite machine-readable contracts. Contract migrations remain compatibility-governed and conflicts must be recorded and reconciled explicitly.
