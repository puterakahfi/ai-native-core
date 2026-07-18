# Native AI Core

Native AI Core is the public, runtime-agnostic contract layer for AI-native engineering.

It defines the shared domain model, philosophy, lifecycle, rules, workflows, templates, ports, and skill contracts used by app adapters and runtime adapters.

## Repository Role

```text
native-ai-core    = public core/domain/contracts/philosophy
native-ai-app     = app/product adapter that consumes this core; public or private by implementer choice
native-ai-skills  = public runtime skill adapters that implement core skill contracts
```

This repository should stay free of private product context, credentials, deployment secrets, and runtime-specific profile state.

---

## Getting Started

### As a Consumer (App Adapter)

1. **Add core as a submodule or dependency:**

   ```bash
   git submodule add https://github.com/puterakahfi/ai-native-core.git core
   ```

2. **Reference contracts in your adapter skills:**

   Each adapter skill declares which core contract it implements:

   ```yaml
   name: native-ai-runtime-agent
   metadata:
     ai-native-skills.type: skill
     ai-native-skills.implements: ai-native-core/contracts/skills/runtime/native-ai-runtime-agent.contract.yaml
   ```

3. **Use templates as starting points** for your product artifacts (ADRs, blueprints, specs).

4. **Follow workflow contracts** — they define required phases and gates. Your adapter fills in team-specific details (branch strategy, CI, approvals).

### As a Contributor

- Contracts go in `contracts/` — runtime-agnostic, stable interfaces.
- Skills (human-readable methodology) go in `skills/`.
- Rules (enforcement constraints) go in `rules/`.
- Templates (artifact starting points) go in `templates/`.
- Framework docs go in `docs/`.

---

## Contract Format

Every skill contract is a YAML file following this schema:

```yaml
skill_contract:
  id: <skill-name>              # unique identifier
  category: <category>          # e.g. design, architecture, engineering
  type: contract
  version: "1.0.0"
  capability: <snake_case>      # machine-readable capability tag
  description: >                # what any adapter for this contract must address
    ...
  roles:                        # which agent roles use this contract
    - visual_designer
  inputs:
    required: [...]             # what the skill needs to begin
    optional: [...]
  outputs:
    allowed: [...]              # what the skill may produce
  quality_gates:                # conditions that must pass
    - gate_name_snake_case
  boundary:
    covers: [...]               # what this contract owns
    does_not_cover: [...]       # explicit delegation to other contracts
```

Workflow contracts follow a similar pattern but define **phases** and **gates** instead of inputs/outputs.

---

## What Belongs Here

```text
contracts/        # stable public contracts for skills, workflows, runtime bindings, and ports
rules/            # reusable framework rules
workflows/        # reusable lifecycle workflows
templates/        # generic artifact templates
skills/           # human-readable shared skill methodology (see note below)
schemas/          # validation schemas (planned — not yet populated)
docs/             # public framework docs, port specifications, architecture
```

> **`skills/` vs `contracts/skills/`**: Contract YAML files define the *interface* — what any adapter must satisfy. Skill markdown files provide *human-readable methodology* — rationale, examples, and teaching material. Not every skill markdown has a contract (e.g. `code-execution/` series are methodology-only), and not every contract has a skill markdown. Over time, high-traffic contracts should have both.

---

## Skill Contracts

### Design (26)

| Contract | Description |
|---|---|
| `master-design` | Senior Product Designer — product experience design orchestrator |
| `adaptive-ui-patterns` | Viewport-aware component and interaction selection for mobile, tablet, and desktop |
| `design-foundation` | Base contract all design systems must satisfy — hierarchy, Ma, Kanso, tokens, accessibility |
| `design-brand` | Locked external design systems — brand tokens, typeface, component rules override genre |
| `design-genre` | Genre detection, signal matching, and slop prevention |
| `design-system` | Design token decisions and semantic roles |
| `macrostructures` | Page shape selection and layout pattern enforcement |
| `composition` | Above-fold composition and visual anchoring |
| `visual-hierarchy` | Typographic hierarchy and weight decay |
| `readability` | Legibility scoring and dead space detection |
| `responsiveness` | Breakpoint strategy, fluid grid, and touch targets |
| `motion-design` | Micro and cinematic motion with reduced-motion compliance |
| `color-theory` | Palette construction, harmony rules, temperature consistency, genre-to-palette mapping |
| `typography` | Typeface selection, modular scale, hierarchy, line-height |
| `spacing` | Visual rhythm, Ma principle, spatial hierarchy, breathing room |
| `iconography` | Icon family selection, sizing, optical alignment |
| `design-depth` | Layer stack declaration, atmosphere techniques, typography interleave |
| `design-visual` | Port — abstracts all aesthetic decisions (genre, color, typography, motion, depth) |
| `design-layout` | Port — abstracts spatial decisions (macrostructure, adaptive components, responsiveness, spacing) |
| `design-interaction` | Port — abstracts behavioral decisions (patterns, states, feedback) |
| `design-strategy` | Port — abstracts user-centered decisions (psychology, IA, CRO, content) |
| `ux-psychology` | Behavioral and psychological UX analysis |
| `ux-ui-patterns` | Layout pattern library and hero/card/nav decision tree |
| `accessibility` | WCAG 2.1 AA — semantic HTML, ARIA, keyboard nav, screen reader |
| `dark-light-theming` | FOUC prevention and token mapping for dark/light themes |
| `information-architecture` | Site map, nav hierarchy, and content grouping |

### Architecture (10)

| Contract | Description |
|---|---|
| `domain-driven-design` | Model domain using DDD building blocks and strategic patterns |
| `ports-and-adapters` | Design hexagonal architecture with explicit ports and adapters |
| `design-patterns` | Identify and apply appropriate design patterns for given forces |
| `service-design` | Design service boundaries and inter-service communication |
| `api-contract` | Design, enforce, and version API contracts between services |
| `event-driven-design` | Design event schema, producer/consumer contracts, and saga patterns |
| `ai-system-design` | Design AI-powered systems with RAG, agents, evals, and fallback |
| `systems-thinking` | Analyze systems as wholes — feedback loops, emergence, unintended consequences |
| `adr` | Author and maintain Architecture Decision Records |
| `micro-frontend` | MFE boundary, module federation, shell contract, CSS isolation |

### Engineering (8)

| Contract | Description |
|---|---|
| `master-engineer` | Software architecture and system design |
| `refactoring` | Structured code refactoring without behavior change |
| `test-driven-development` | RED-GREEN-REFACTOR — tests before implementation |
| `technical-debt-governance` | Debt inventory, classification, and paydown prioritization |
| `data-modeling` | Schema design, migrations, and domain model alignment |
| `plan` | Actionable plan authoring before execution |
| `spike` | Throwaway experiment before build |
| `git-workflow` | Source control operations — branch, commit, PR, merge |

### Quality (8)

| Contract | Description |
|---|---|
| `architecture-review` | Engineering contract compliance review |
| `systematic-debugging` | 4-phase root cause — investigate, analyze, hypothesize, fix |
| `skill-eval` | Skill application verification and gate compliance testing |
| `resilience-engineering` | Design for failure, chaos engineering, and graceful degradation |
| `ethics-responsible-ai` | Ethical analysis, fairness audit, and responsible AI governance |
| `design-review` | Design system compliance, AI slop detection, visual hierarchy gates |
| `redesign-workflow` | Autonomous redesign loop — skill-first, gate-scored |
| `web-performance` | LCP, CLS, INP optimization and performance budget |

### Security (2)

| Contract | Description |
|---|---|
| `security-review` | Security baseline validation |
| `threat-modeling` | Proactive security threat identification before implementation |

### Product (6)

| Contract | Description |
|---|---|
| `product-manager` | Product definition and task breakdown |
| `product-requirements` | Author and verify product requirements documents |
| `user-research` | Interview synthesis, JTBD, and insight generation |
| `experiment-design` | Design minimum viable experiments for product/business value |
| `decision-making` | Reversibility analysis, premortem, and decision framing |
| `business-value-alignment` | Align work with user/business value, metrics, and decision rationale |

### Content (3)

| Contract | Description |
|---|---|
| `copywriting` | Messaging hierarchy, headline formulas, and tone calibration |
| `cro` | Conversion optimization, trust signals, and friction audit |
| `content-strategy` | Microcopy, tone of voice, and information sequencing |

### Context (4)

| Contract | Description |
|---|---|
| `context-engineering` | Institutional context authoring and curation |
| `context-manager` | Context resolution and validation |
| `prompt-optimizer` | Transform intent into precise, token-efficient prompt |
| `response-contract` | Enforce output verbosity and filler elimination |

### Runtime (8)

| Contract | Description |
|---|---|
| `native-ai-engineer` | Native AI domain contract architecture and layer placement |
| `native-ai-runtime-agent` | Product adapter runtime execution |
| `native-ai-runtime-ops` | Canonical runtime operations |
| `onboarding` | Bootstrap agent/engineer context for existing codebase |
| `incident-response` | Structured incident lifecycle and blameless postmortem |
| `observability-design` | Design logs, metrics, traces stack for distributed systems |
| `profile-bootstrap` | Runtime profile bootstrap — skeleton, presets, verification |
| `model-selection` | Select model class for AI-native engineering tasks |

### Meta (2)

| Contract | Description |
|---|---|
| `role-switcher` | Intent detection and automatic role composition |
| `workflow-router` | Detect task type and route to correct workflow automatically |

### Governance (2)

| Contract | Description |
|---|---|
| `language-standards` | Enforce consistent declared language across artifacts |
| `rule-manager` | Rule authoring, validation, and enforcement |

### Visual Thinking (1)

| Contract | Description |
|---|---|
| `diagram-architect` | Renderer-agnostic diagram modeling |

---

## Runtime Contracts (7)

| Contract | Description |
|---|---|
| `core-source` | How app adapters resolve core contracts (vendor, package, or submodule) |
| `agents-md` | AGENTS.md standard — required sections, authoring rules, validation gates for project-level agent context |
| `development-loop` | Canonical execution cycle — Explore → Plan → Implement → Verify → Review → Document → Deliver |
| `memory` | Four memory types (session, persistent, episodic, procedural) — governance, promotion rules, knowledge boundary |
| `hook` | Deterministic lifecycle gates — pre/post edit, commit, submit. Guaranteed execution, not advisory |
| `tool-registration` | Tool capability declaration, risk classification (read-only → destructive), access control, MCP integration |
| `sop` | Standard Operating Procedures — deployment, incident, release, infrastructure playbooks |

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

## Documentation

The `docs/` directory contains framework concepts and port specifications:

| Document | Topic |
|---|---|
| **Architecture** | |
| [architecture-v0.2](docs/architecture-v0.2.md) | Framework architecture overview |
| [ports-and-adapters](docs/ports-and-adapters.md) | Hexagonal architecture approach |
| [port-taxonomy](docs/port-taxonomy.md) | Port classification and naming |
| [domain-driven-model](docs/domain-driven-model.md) | Domain model design |
| [engineering-contract](docs/engineering-contract.md) | Engineering contract specification |
| [memory-vs-knowledge](docs/memory-vs-knowledge.md) | When to use memory vs documentation |
| [adapter-registry](docs/adapter-registry.md) | Adapter registration and discovery |
| **Core Concepts** | |
| [agents-md](docs/agents-md.md) | AGENTS.md — project-level agent context standard |
| [development-loop](docs/development-loop.md) | Development loop — canonical agent execution cycle |
| [glossary](docs/glossary.md) | Domain glossary — all terms defined |
| **Provider Ports** | |
| [agent-runtime-port](docs/agent-runtime-port.md) | Agent runtime binding |
| [deployment-provider-port](docs/deployment-provider-port.md) | Deployment provider abstraction |
| [domain-provider-port](docs/domain-provider-port.md) | Domain provider abstraction |
| [environment-provider-port](docs/environment-provider-port.md) | Environment provider abstraction |
| [observability-provider-port](docs/observability-provider-port.md) | Observability provider abstraction |
| [persistence-port](docs/persistence-port.md) | Data persistence abstraction |
| [infrastructure-integration-port](docs/infrastructure-integration-port.md) | Infrastructure integration abstraction |
| **Product Ports** | |
| [assistant-product-port](docs/assistant-product-port.md) | AI assistant product surface |
| [content-product-port](docs/content-product-port.md) | Content product surface |
| [creative-rendering-port](docs/creative-rendering-port.md) | Creative rendering surface |
| [learning-product-port](docs/learning-product-port.md) | Learning product surface |
| [media-product-port](docs/media-product-port.md) | Media product surface |
| [template-product-port](docs/template-product-port.md) | Template product surface |
| [product-output-port](docs/product-output-port.md) | Product output abstraction |
| **System Ports** | |
| [context-management-port](docs/context-management-port.md) | Context management abstraction |
| [execution-run-port](docs/execution-run-port.md) | Execution run abstraction |
| [product-management-port](docs/product-management-port.md) | Product management abstraction |
| [quality-control-port](docs/quality-control-port.md) | Quality control abstraction |
| [review-approval-port](docs/review-approval-port.md) | Review and approval abstraction |
| [rule-management-port](docs/rule-management-port.md) | Rule management abstraction |
| [security-baseline-port](docs/security-baseline-port.md) | Security baseline abstraction |
| [skill-management-port](docs/skill-management-port.md) | Skill management abstraction |
| [tool-integration-port](docs/tool-integration-port.md) | Tool integration abstraction |
| [ui-design-system-port](docs/ui-design-system-port.md) | UI design system abstraction |
| [ui-surface-port](docs/ui-surface-port.md) | UI surface abstraction |
| [workflow-orchestration-port](docs/workflow-orchestration-port.md) | Workflow orchestration abstraction |
| **Product-Specific** | |
| [ai-coding-adapter](docs/ai-coding-adapter.md) | AI coding adapter specification |
| [product-ui-design-system-contract](docs/product-ui-design-system-contract.md) | Product UI design system contract |

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

## Contract Sync Tooling

Three layers of enforcement prevent core ↔ adapter drift:

| Layer | Tool | What it checks |
|---|---|---|
| **Path exists** | `validate-implements.sh` | `implements` reference resolves to a real contract file |
| **Version compatible** | `validate-implements.sh` | `contract-version` pin satisfies semver (`^` = major, `~` = minor) |
| **Interface satisfied** | `validate-conformance.py` | Adapter covers contract's `quality_gates`, `outputs`, `inputs` |

### Manifest

`contracts/manifest.yaml` is the auto-generated registry of all contracts with paths, versions, and checksums. Regenerate after adding/moving/deleting contracts:

```bash
./scripts/generate-manifest.sh
```

### Version Pinning

Adapter skills pin to a contract version in frontmatter:

```yaml
metadata:
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-depth.contract.yaml
  ai-native-skills.contract-version: "^2.0.0"
```

| Pin | Meaning | Breaks when |
|---|---|---|
| `^2.0.0` | Major-compatible (≥2.0.0, <3.0.0) | Core bumps to 3.0.0 |
| `~0.1` | Minor-compatible (≥0.1.0, <0.2.0) | Core bumps to 0.2.0 |

### Path + Version Validator

```bash
# From your adapter repo
../ai-native-core/scripts/validate-implements.sh ../ai-native-core
```

Checks both path existence and semver compatibility. Exit 0 = pass, 1 = broken or incompatible.

### Conformance Validator

```bash
python3 ../ai-native-core/scripts/validate-conformance.py ../ai-native-core .
```

Checks whether adapter skill body actually covers the contract's `quality_gates`, `outputs`, and `inputs`. Uses fuzzy matching (snake_case variants, word overlap). Severity:
- **ERROR**: < 50% `quality_gates` coverage — adapter is missing critical gates
- **WARN**: partial coverage — improvement opportunity

---

## Adapter Pattern

Skills in `native-ai-skills` implement contracts defined here:

```yaml
name: native-ai-runtime-agent
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/native-ai-runtime-agent.contract.yaml
```

---

## Related

- [ai-native-skills](https://github.com/puterakahfi/ai-native-skills) — skill adapter implementations
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product runtime adapter
- [skills.sh](https://skills.sh) — open skills ecosystem standard
