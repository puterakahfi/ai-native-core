# Native AI Ports And Adapters Architecture

Status: Architecture pattern and non-exhaustive examples

Canonical base meanings and ownership: [`domain-model/README.md`](domain-model/README.md)

Native AI OS terminology and qualification: [`native-ai-os.md`](native-ai-os.md)

Final port kinds, adapter taxonomy, and first-class port contracts: issue `#7`

## Problem

An AI-native product or operating system should not be locked to one model, one coding assistant, one design tool, one web framework, one agent runtime, or one deployment provider.

Tools and frameworks change. The product domain, engineering contract, rules, skills, workflows, evaluation model, and canonical authority boundaries must stay stable.

## Why It Matters

If the architecture depends directly on one implementation choice, every tool change can break the methodology or silently redefine product meaning.

Examples of replaceable implementation choices:

```text
Code adapter: Codex, Claude Code, Gemini CLI, Cursor, custom agent
Design adapter: Figma, design generator, design review tool, custom renderer
Web framework: Next.js, Nuxt, Remix, SvelteKit, custom frontend
AI model provider: OpenAI, Anthropic, Google, local model, internal model gateway
Agent runtime: Hermes, Codex, Claude Code, custom runtime
Storage adapter: S3, Cloudflare R2, GCS, local storage
Database adapter: PostgreSQL, MySQL, SQLite for local MVP
```

## Design Principle

```text
Domain model is stable.
Ports define required capability.
Adapters provide replaceable implementation.
Control-plane coordination preserves upstream ownership.
```

## Core Architecture

```text
Domain Model
-> Application Use Cases
-> Ports
-> Adapters
-> Tools / Providers / Frameworks / Runtimes
```

The domain should not depend on adapter or operating-system implementation details.

## Stable Architecture Concerns

The following is an operational concern list, not a bounded-context map, exhaustive domain model, or Native AI OS qualification checklist:

```text
Intent
Blueprint
Engineering Contract
Domain Model
Rules
Skills
Agents
Workflows
Evaluation
Memory and Knowledge
```

Native AI OS implementations may coordinate these concerns, but coordination does not transfer their semantic ownership or authority. See [`native-ai-os.md`](native-ai-os.md).

## Ports

A port defines what capability the system needs, without choosing the implementation.

Non-exhaustive example ports:

```text
CodeExecutionPort
DesignGenerationPort
DesignReviewPort
ModelInferencePort
KnowledgeRetrievalPort
RepositoryPort
FileSystemPort
BrowserResearchPort
DatabasePort
StoragePort
PublishingPort
EvaluationPort
ObservabilityPort
```

## Adapters

An adapter implements or translates a port or contract while preserving upstream meaning and boundary. The exhaustive subtype taxonomy remains owned by issue `#7`.

Example:

```text
CodeExecutionPort
├── CodexAdapter
├── ClaudeCodeAdapter
├── GeminiCliAdapter
├── CursorAdapter
└── CustomCodingAgentAdapter
```

```text
DesignGenerationPort
├── FigmaAdapter
├── StitchAdapter
├── ClaudeDesignAdapter
├── HTMLCssRendererAdapter
└── CustomDesignAgentAdapter
```

```text
WebAppPort
├── NextJsAdapter
├── NuxtAdapter
├── RemixAdapter
└── SvelteKitAdapter
```

## Adapter Contract

Every adapter should define:

```text
- Adapter name
- Port implemented
- Purpose
- Inputs
- Outputs
- Capabilities
- Limitations
- Risk level
- Required approval
- Failure behavior
- Evaluation method
```

## Engineering Contract Relationship

The Engineering Contract may choose default adapters for a product, but those choices can change through ADR or another governed product decision.

Example:

```yaml
ports:
  code_execution:
    default_adapter: codex
    alternatives: [claude_code, gemini_cli, cursor]

  design_generation:
    default_adapter: figma
    alternatives: [stitch, claude_design, html_css_renderer]

  web_app:
    default_adapter: nextjs
    alternatives: [nuxt, remix]
```

A Native AI OS control plane may resolve or coordinate these bindings. It does not make the selected adapter canonical domain meaning, and it does not acquire product approval authority merely by selecting or invoking an adapter.

## Anti-Patterns

Avoid:

- Making Codex the core
- Making Next.js the only possible web framework
- Making one runtime synonymous with Native AI OS
- Putting provider-specific logic in the domain model
- Letting adapters define business rules
- Letting model choice override the Engineering Contract
- Treating tool output as approved output
- Treating control-plane access as authority
- Treating operating-system branding as qualification evidence

## ExampleProduct Example

ExampleProduct domain concepts should remain stable:

```text
Brand
IdentityLock
Campaign
CampaignBrief
CreativeDirection
GeneratedAsset
CreativeReview
Approval
Export
```

But implementations may vary:

```text
CodeExecutionPort -> CodexAdapter or ClaudeCodeAdapter
DesignGenerationPort -> FigmaAdapter or StitchAdapter
ModelInferencePort -> OpenAIAdapter or AnthropicAdapter or GoogleAdapter
WebAppPort -> NextJsAdapter or NuxtAdapter
StoragePort -> R2Adapter or S3Adapter
```

The adapters may change. The domain should not. Native AI OS may coordinate the bindings and execution while preserving the product domain, evidence, governance, and authority boundaries.
