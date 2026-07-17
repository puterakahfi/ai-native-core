# Native AI Core

Native AI Core is the public, runtime-agnostic contract layer for AI-native engineering.

It defines the shared domain model, philosophy, lifecycle, rules, workflows, templates, ports, and skill contracts used by app adapters and runtime adapters.

**68 skill contracts · 6 workflow contracts · 5 test contracts · 1 runtime contract**

## Repository Role

```text
native-ai-core    = public core/domain/contracts/philosophy
native-ai-app     = app/product adapter that consumes this core; public or private by implementer choice
native-ai-skills  = public runtime skill adapters that implement core skill contracts
```

This repository should stay free of private product context, credentials, deployment secrets, and runtime-specific profile state.

## What Belongs Here

```text
contracts/        # stable public contracts for skills, workflows, runtime bindings, and ports
rules/            # reusable framework rules
workflows/        # reusable lifecycle workflows
templates/        # generic artifact templates
skills/           # human-readable shared skill methodology
schemas/          # validation schemas when contracts stabilize
docs/             # public framework docs
```

---

## Skill Contracts

### Experience Design (14)

| Contract | Description |
|---|---|
| `master-design` | Senior Product Designer — Eight Universal Rules, genre, macrostructures |
| `macrostructures` | Layout archetypes — Marquee Hero, Studio, Editorial |
| `design-genre` | Editorial dark, minimal light, bold brand — token selection per genre |
| `design-system` | Token architecture, component library, design language governance |
| `composition` | Focal point, optical center, dead space vs breathing room, eye-flow |
| `visual-hierarchy` | Dominant/supporting/accent triad, H2 ≤ 60% H1, heading role taxonomy |
| `readability` | Line length, contrast, type size, cognitive ease |
| `responsiveness` | Mobile-first, wide/ultrawide breakpoints, max-width containers |
| `motion-design` | Animation tokens, easing, reduced-motion, stagger patterns |
| `ux-ui-patterns` | Component patterns, interaction states, behavior specs |
| `ux-psychology` | Cognitive load, habit loops, Fitts's Law, Nielsen heuristics |
| `design-review` | Design system compliance, AI slop detection, visual hierarchy gates |
| `accessibility` | WCAG 2.1 AA — semantic HTML, ARIA, keyboard nav, screen reader |
| `micro-frontend` | MFE boundary, shell contract, CSS isolation |

### Content (3)

| Contract | Description |
|---|---|
| `copywriting` | Messaging hierarchy, value prop 1000-person test, buzzword blacklist |
| `cro` | Attention flow, trust signals, 8-second window, persuasion sequence |
| `content-strategy` | Content architecture, tone, editorial workflow |

### Design Ops (4)

| Contract | Description |
|---|---|
| `redesign-workflow` | Full redesign loop — Phase 0.5 brief-signal, 35+ gates, skill-first fix |
| `dark-light-theming` | Theme switching, token mapping, prefers-color-scheme |
| `information-architecture` | Content hierarchy, navigation taxonomy, mental models |
| `web-performance` | Core Web Vitals, bundle size, render blocking, caching |

### Domain Architecture (10)

| Contract | Description |
|---|---|
| `domain-driven-design` | Bounded contexts, aggregates, value objects, domain events |
| `ports-and-adapters` | Hexagonal architecture — port definition, adapter implementation |
| `design-patterns` | GoF patterns + CQRS, Saga, Outbox |
| `service-design` | Service boundary by bounded context, sync vs async, data ownership |
| `api-contract` | OpenAPI, versioning, breaking change detection |
| `event-driven-design` | Event schema, saga, idempotency, DLQ, Outbox, CQRS |
| `ai-system-design` | RAG, agent memory, LLM evals, prompt injection defense |
| `systems-thinking` | Feedback loops, second-order effects, Conway's Law, leverage points |
| `adr` | Architecture Decision Records — immutable, superseding pattern |
| `role-switcher` | Intent detection, automatic role composition |
| `workflow-router` | Route to correct workflow from task intent |

### Software Engineering (7)

| Contract | Description |
|---|---|
| `master-engineer` | Senior Software Engineer — system design, architecture decisions |
| `refactoring` | Named code smells, green-first, small steps |
| `test-driven-development` | RED-GREEN-REFACTOR — tests before implementation |
| `technical-debt-governance` | Debt taxonomy, prioritization, paydown strategy |
| `data-modeling` | Entity design, normalization, indexing, migration strategy |
| `plan` | Actionable markdown plan with exact file paths |
| `spike` | Throwaway experiment — validate idea, produce verdict |

### Quality Control (7)

| Contract | Description |
|---|---|
| `architecture-review` | Contract compliance — layer violations, DDD gates, dependency drift |
| `systematic-debugging` | 4-phase root cause — investigate, analyze, hypothesize, fix |
| `security-review` | OWASP baseline, secrets detection, injection vectors, auth gaps |
| `threat-modeling` | STRIDE per trust boundary, data flow mapping, risk rating |
| `resilience-engineering` | Failure mode analysis, circuit breakers, chaos engineering |
| `ethics-responsible-ai` | Fairness audit, harm assessment, transparency, consent |
| `skill-eval` | APPLIED/PARTIAL/GHOST — verify skills are actually applied |

### Product Management (5)

| Contract | Description |
|---|---|
| `product-manager` | PRD authoring, acceptance criteria, task breakdown |
| `product-requirements` | Goals, non-goals, scope, metrics, acceptance criteria |
| `user-research` | User interviews, synthesis, insights, personas, JTBD |
| `experiment-design` | Hypothesis, riskiest assumption, smallest test, decision rule |
| `decision-making` | Decision framework, tradeoff analysis, reversibility |

### Context Management (4)

| Contract | Description |
|---|---|
| `context-engineering` | AGENTS.md authoring — encode constraints, guardrails, domain knowledge |
| `context-manager` | Context pack resolution — build precise context before execution |
| `prompt-optimizer` | Vague intent → precise prompt: scope, constraint, output format |
| `response-contract` | Persistent output verbosity — no filler, answer-first, code exact |

### Runtime Agent (2)

| Contract | Description |
|---|---|
| `native-ai-runtime-agent` | Runtime agent in ai-native-fw product adapters |
| `onboarding` | Bootstrap agent/engineer context — recon codebase, produce AGENTS.md |

### Runtime Operations (3)

| Contract | Description |
|---|---|
| `native-ai-runtime-ops` | Ops for AI-native canonical runtime hosts |
| `incident-response` | Structured incident lifecycle, blameless postmortem |
| `observability-design` | Logs + metrics + traces — three pillars, four golden signals, SLO |

### Native AI (1)

| Contract | Description |
|---|---|
| `native-ai-engineer` | Layer placement, runtime boundary, contract authoring |

### Model (1)

| Contract | Description |
|---|---|
| `model-selection` | Select model class by task intent, risk, capabilities, fallback |

### Business (1)

| Contract | Description |
|---|---|
| `business-value-alignment` | User value, business value, metrics, assumptions, verdict |

### Governance & Standards (3)

| Contract | Description |
|---|---|
| `language-standards` | Consistent declared language across artifacts |
| `rule-manager` | AGENTS.md/.cursorrules authoring and enforcement |
| `git-workflow` | Branch, commit, PR, merge — generic source control |

### Visual Thinking (1)

| Contract | Description |
|---|---|
| `diagram-architect` | Architecture diagrams — SVG, Excalidraw, Mermaid |

### Runtime Profile (1)

| Contract | Description |
|---|---|
| `profile-bootstrap` | Profile skeleton, skill presets, install plan, verification policy |

---

## Workflow Contracts (6)

| Contract | Description |
|---|---|
| `product-development` | Umbrella flow from discovery to launch |
| `spec-driven` | Spec before code — requirements → contract → implementation |
| `new-feature` | Team feature process — branch, implement, review, merge |
| `bugfix` | Root cause, fix, regression test, deploy |
| `code-review` | Pre-merge gates — security, quality, style, tests |
| `deployment` | Deploy gates — staging, smoke test, rollback plan, prod |

---

## Test Contracts (5)

| Contract | Test Subject |
|---|---|
| `architecture-review.test` | Architecture review skill |
| `prompt-optimizer.test` | Prompt optimizer skill |
| `response-contract.test` | Response contract skill |
| `role-switcher.test` | Role switcher meta-skill |
| `systematic-debugging.test` | Systematic debugging skill |

---

## What Does Not Belong Here

```text
products/<private-product>/
context-packs/<private-product>.yaml
runtime profile files
private deployment config
private screenshots or customer/product data
runtime-specific installed skill copies
```

---

## Contract-Driven Usage

An app adapter should include this core and then bind a product instance to a runtime:

```text
app adapter repo
  -> includes native-ai-core
  -> adds product-specific contracts/context
  -> binds to runtime adapters such as Hermes
  -> verifies output against core + product contracts
```

App adapter visibility is not part of the contract. It can be public for examples/open products or private for internal products.

---

## Adapter Pattern

Skills in `native-ai-skills` implement contracts defined here:

```yaml
name: native-ai-runtime-agent
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-agent/native-ai-runtime-agent.contract.yaml
```

---

## Related

- [ai-native-skills](https://github.com/puterakahfi/ai-native-skills) — skill adapter implementations (76 skills)
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product runtime adapter
- [skills.sh](https://skills.sh) — open skills ecosystem standard
