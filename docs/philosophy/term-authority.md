# Native AI Engineering Canonical Term Authority

Status: Final candidate canonical vocabulary

Issue: `#13 — Define Native AI Engineering philosophy, axioms, laws, principles, and guardrails`

Authority entry point: [`README.md`](README.md)

This file owns the minimum philosophy-level meaning of terms required by the kernel, laws, guardrails, epistemic loop, domain-model inputs, contracts, evidence, and governed evolution.

It does not define the complete domain model owned by issue `#6`, and it does not replace accepted machine-readable contract semantics.

---

## 1. Authority Rule

```text
atomic canonical definition
→ domain specialization
→ contract and port semantics
→ skills, workflows, and adapters
→ runtime and product implementation
```

Concrete layers may qualify, constrain, or serialize a term. They must not reverse its base meaning, collapse a required distinction, or silently redefine it upstream.

Each term has one primary atomic owner:

| Artifact | Owns |
|---|---|
| This file | Minimum atomic meaning |
| Relationship maps | Relationships between terms |
| Laws | Derived invariants |
| Principles | Decision orientation |
| Guardrails | Mandatory boundaries |
| Domain model | Objects, relationships, ownership, lifecycle |
| Contract | Stable machine-readable agreement |
| Adapter | Contextual translation or implementation |
| Glossary | Navigation and short discovery labels |

A semantic change requires an explicit owner, rationale, affected-consumer review, compatibility or migration handling, validation, and required authority.

---

## 2. Retention And Usage

The 39 terms below are not a checklist every agent must recite.

They are retained because different consumers require different distinctions:

```text
repository analysis needs observation, inference, claim, evidence, scope, and verification;
a control plane needs capability, permission, authority, approval, capacity, and recovery;
a validator needs conformance, evidence layer, verification, validation, and completion boundaries;
skill evolution needs feedback, learning, learning candidate, stability, and core evolution.
```

Historical `T` numbers are traceability aliases only. Stable names are primary.

---

## 3. State And Observation Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T1 | State | The condition, configuration, event, or engineering-relevant situation of a bounded subject at a bounded time or interval | State is not its summary, observation, model, intended future, decision, or evidence by itself |
| T2 | Observable State | State for which a defined observation path can produce a bounded representation | Observable does not mean currently accessible, complete, authoritative, or accurate |
| T3 | Available State | Relevant state currently accessible to an actor through attributable observation or source records | Available does not mean complete, current, authoritative, or permission to act |
| T4 | Observation | A bounded act and result of accessing state through an attributable source, method, time, environment, and coverage | Observation is not interpretation, inference, fact, decision, authority, or complete truth |
| T5 | Source | The attributable origin of an observation, statement, record, decision, claim, or evidence item | Source existence does not prove authority, truth, recency, reliability, or coverage |
| T6 | Unknown | Explicit status for a relevant proposition that cannot be established with available evidence and capacity | Unknown is not false, absent, safe, unsafe, approved, rejected, or permission to guess |

Kernel implication:

```text
Material engineering claims and actions begin from attributable observations
or explicit unknowns concerning relevant state.
```

---

## 4. Representation And Reasoning Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T7 | Model | A structured representation used for interpretation, communication, prediction, planning, or execution | A model is not the represented state, fact, authority, execution, or proof by default |
| T8 | Interpretation | Meaning assigned to an observation, statement, artifact, or other information | Interpretation is not the observation itself, fact, or authoritative decision |
| T9 | Inference | A proposition derived through an identifiable reasoning step from observations, evidence, or other propositions | Inference is not direct observation, fact, decision, or authority by default |
| T10 | Assumption | A proposition temporarily accepted for reasoning or action without sufficient verification for the current claim scope | Assumption is not fact, evidence, decision, approval, or permission |
| T11 | Fact | A proposition treated as established within a stated scope because attributable evidence satisfies the relevant verification standard | Fact is bounded by time, version, environment, method, and coverage; it is not authority to act |
| T12 | Claim | An explicit proposition asserted about state, behavior, meaning, quality, causality, authority, completion, or result | Claim is not evidence, fact, decision, or approval by default |

Kernel implication:

```text
No observation or model is identical to the state it represents.
```

---

## 5. Evidence And Quality Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T13 | Evidence | Attributable information produced or preserved through a method that can support, weaken, distinguish, or challenge a claim within bounded scope | Evidence is not a claim, complete truth, authority, approval, or all required evidence by default |
| T14 | Verification | Determining whether a specified claim, requirement, contract, property, or result is supported by appropriate evidence | Verification is not complete product validation, approval, or proof beyond verified scope |
| T15 | Validation | Determining whether a system, artifact, decision, or behavior is fit for intended use, need, context, and acceptance scope | Validation is not identical to verification, approval, universal success, or one technical check |
| T16 | Evaluation | Systematic assessment against declared criteria producing findings, measurements, evidence, and optionally a verdict | Evaluation is not authority, approval, runtime enforcement, or complete evidence by default |
| T17 | Review | Examination of an artifact, decision, implementation, behavior, or evidence set against declared criteria by a qualified actor or process | Review is not approval unless the actor and process hold the required authority |
| T18 | Conformance | Degree to which an implementation, adapter, artifact, or behavior satisfies applicable contract or standard requirements | Conformance must name its evidence layer; contract or metadata presence is not behavioral or product proof |
| T19 | Coherence | Degree to which material intent, definitions, decisions, contracts, implementation, behavior, evidence, and approval state coexist without unresolved contradiction inside scope | Coherence is not perfect uniformity, global completeness, one preferred style, or immutability |
| T20 | Completion | Claim that the accepted objective and in-scope criteria are satisfied with appropriate evidence, required review or approval, and disclosed limitations | Completion is not activity, one green check, confidence, or partial work reported as full completion |

Common evidence layers:

```text
source and path resolution;
version compatibility;
structural declaration;
boundary consistency;
behavioral execution;
runtime integration;
security or accessibility evidence;
product acceptance;
business outcomes;
approval evidence.
```

Passing one layer does not prove the others.

---

## 6. Action, Decision, And Authority Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T21 | Capability | Ability of an actor, agent, tool, adapter, or system to perform a category of action or produce a category of result | Capability is not permission, authority, approval, quality proof, or successful execution |
| T22 | Permission | Technical, policy, or access-control allowance to attempt a named operation inside bounded scope | Permission is not capability, authority, approval, safety, or correctness by itself |
| T23 | Authority | Recognized right in a named decision domain to bind, approve, reject, delegate, supersede, or constrain action, risk, claim, or canonical meaning | Authority is not capability, permission, access, recency, confidence, silence, or ownership label alone |
| T24 | Decision | Recorded selection, rejection, commitment, or constraint intended to govern action in stated scope | A decision may be non-authoritative, conflicted, superseded, or pending approval |
| T25 | Effective Decision | A decision whose source and authority are verified, whose scope covers the action, whose approvals are satisfied, and whose material conflicts are resolved | The newest or most convenient decision is not automatically effective |
| T26 | Approval | Authority-bearing positive decision permitting a named action, claim, transition, release, risk acceptance, or canonical change within conditions | Approval is not recommendation, silence, technical permission, review verdict, or successful validation by default |
| T27 | Scope | Explicit boundary of subject, actions, claims, environments, time, consumers, risks, and responsibilities | Scope does not include all adjacent work, implied future work, or technically possible action |
| T28 | Coverage | Portion of stated scope actually observed, exercised, evaluated, reviewed, or supported by evidence | Coverage is not full scope, quality, or completion by itself |
| T29 | Capacity | Current combination of context, capability, tools, permission, authority, controls, time, validation, review, reversibility, and recovery required for bounded action | Capacity is contextual; it is not capability, access, permission, confidence, or permanent identity alone |

Decision relationship:

```text
claim + evidence + alternatives
→ decision

decision + verified authority + applicable scope + resolved conflicts
→ effective decision

effective positive decision permitting named action
→ approval
```

---

## 7. Feedback, Learning, And Evolution Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T30 | Feedback | Attributable information from execution, observation, evaluation, review, use, measurement, or consequence that can support revision of an affected layer | Feedback is not automatically correct, authoritative, final truth, learning, or direct authority to change core |
| T31 | Update | Traceable change to a working model, plan, decision, implementation, knowledge artifact, skill, workflow, proposal, or canonical artifact in response to accepted evidence, feedback, or authority | Update is not uncontrolled mutation, proof of correctness, silent drift, or core evolution by default |
| T32 | Learning | Evaluated change in future interpretation, decision, or repeatable behavior derived from feedback and evidence | Learning is not feedback collection, memory, anecdote, one success, or automatic shared promotion |
| T33 | Learning Candidate | Traceable proposal that a verified lesson may be reusable beyond its source case and should be evaluated for the smallest correct shared layer | It is not accepted shared knowledge, rule, contract change, or core evolution |
| T34 | Embodiment | State in which a declared principle, rule, contract, skill, or workflow changes repeatable executable behavior and can produce evidence appropriate to the claim | Documentation, contract presence, skill installation, metadata, or one success is not embodiment by itself |
| T35 | Stability | Condition in which an artifact has explicit ownership, compatibility expectations, controlled change behavior, validation requirements, and reliable consumer expectations | Stability is not immutability, infallibility, absence of feedback, or permanent freeze |
| T36 | Core Evolution | Accepted governed change to a canonical Native AI Engineering definition, law, principle, guardrail, domain boundary, port, contract, or other core-owned agreement | Local implementation, product policy, adapter translation, field test, or recommendation is not core evolution |

Bridge relationship:

```text
execution or use
→ evidence
→ feedback
→ affected-layer update
→ learning
→ learning candidate
→ transferability and compatibility review
→ accepted target-layer change
→ core evolution only when core authority accepts it
```

---

## 8. Source-Of-Truth And Memory Terms

| Alias | Term | Minimum meaning | Critical boundary |
|---:|---|---|---|
| T37 | Source Of Truth | Artifact, record, or system designated by relevant authority as the current primary reference for a named class of definition, decision, policy, state, or knowledge | It is not infallible, complete for all concerns, eternally current, or truth outside its scope |
| T38 | Knowledge | Explicit reviewable information accepted for use within stated scope and maintained in an attributable source-of-truth artifact or system | Knowledge is not memory, confidence, unattributed summary, or immutable truth |
| T39 | Memory | Retained context, history, preference, pattern, or prior outcome supporting retrieval and reasoning across time | Memory is not authoritative knowledge, current policy, verified present state, or approval by default |

Memory may locate a source. It must not silently supersede the current authoritative source.

---

## 9. Required Relationship Maps

### State and reasoning

```text
STATE
→ accessed through OBSERVATION
→ assigned meaning through INTERPRETATION
→ extended through INFERENCE
→ may rely on explicit ASSUMPTION
→ expressed as CLAIM
→ supported or challenged by EVIDENCE
→ may become FACT within scope
→ or remain UNKNOWN / NOT_VERIFIED
```

### Evidence and quality

```text
CLAIM
→ VERIFICATION against specified evidence requirements
→ VALIDATION against intended use and context
→ broader EVALUATION against criteria
→ REVIEW where required
→ APPROVAL only from required authority
```

### Execution capacity

```text
context
+ capability
+ tools
+ permission
+ authority
+ risk controls
+ time and scope budget
+ validation path
+ review coverage
+ reversibility and recovery
= bounded CAPACITY
```

### Embodiment

```text
declared expectation
+ repeatable executable behavior
+ appropriate evidence
= embodiment candidate
```

---

## 10. Prohibited Collapses

```text
state ≠ observation
observation ≠ interpretation
interpretation ≠ inference
inference ≠ fact
assumption ≠ fact
claim ≠ evidence
evidence ≠ approval
fact ≠ authority
capability ≠ permission
permission ≠ authority
decision ≠ effective decision
review ≠ approval
verification ≠ validation
validation ≠ complete product success
contract presence ≠ conformance
static conformance ≠ executable behavior
skill installation ≠ embodiment
feedback ≠ learning
learning ≠ automatic shared promotion
local update ≠ core evolution
stability ≠ immutability
memory ≠ source-of-truth knowledge
completion ≠ activity performed
```

---

## 11. Specialization Rule

A domain, contract, skill, adapter, runtime, or product may introduce qualified terms such as `runtime evidence`, `security approval`, or `repository state` when:

```text
the specialization inherits the base meaning;
its added boundary is explicit;
its local owner is named;
it does not redefine upstream semantics.
```

---

## 12. Current Verdict

```text
Atomic terms retained: 39
Required issue #13 terms: COVERED
Supporting consumer distinctions: COVERED
Competing glossary authority: REMOVED
State-versus-observation contradiction: RESOLVED
Term count as maturity signal: REJECTED
Machine serialization: OWNED BY #6/#8
Executable embodiment: DOWNSTREAM VALIDATION
Ready for final acceptance review: YES
```
