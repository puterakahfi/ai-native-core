# Native AI Ports and Adapters Architecture

## Problem

A Native AI Framework should not be locked to one model, one coding assistant, one design tool, one web framework, or one deployment provider.

Tools and frameworks change. The product domain, engineering contract, rules, skills, workflows, and evaluation model must stay stable.

## Why It Matters

If the framework depends directly on one implementation choice, every tool change can break the methodology.

Examples of replaceable implementation choices:

```text
Code adapter: Codex, Claude Code, Gemini CLI, Cursor, custom agent
Design adapter: Figma, design generator, design review tool, custom renderer
Web framework: Next.js, Nuxt, Remix, SvelteKit, custom frontend
AI model provider: OpenAI, Anthropic, Google, local model, internal model gateway
Storage adapter: S3, Cloudflare R2, GCS, local storage
Database adapter: PostgreSQL, MySQL, SQLite for local MVP
```

## Design Principle

```text
Domain model is stable.
Ports define required capability.
Adapters provide replaceable implementation.
```

## Core Architecture

```text
Domain Model
-> Application Use Cases
-> Ports
-> Adapters
-> Tools / Providers / Frameworks
```

The domain should not depend on adapter details.

## Native AI Framework Core

The stable framework core includes:

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

## Ports

A port defines what capability the system needs, without choosing the implementation.

Example ports:

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

An adapter implements a port.

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

The Engineering Contract chooses the default adapters for a product, but those choices can change through ADR.

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

## Anti-Patterns

Avoid:

- Making Codex the framework core
- Making Next.js the only possible web framework
- Putting provider-specific logic in domain model
- Letting adapters define business rules
- Letting model choice override Engineering Contract
- Treating tool output as approved output

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

The adapters may change. The domain should not.
