# Port Taxonomy

## Purpose

This document defines common ports used by Native AI Framework products.

A port is a required capability. It does not choose the tool or provider.

## Port Definition

```text
Port = capability contract
Adapter = replaceable implementation
```

## 1. ModelInferencePort

Purpose:

Use AI models to generate, transform, classify, evaluate, summarize, or reason over information.

Common inputs:

```text
prompt
context
schema
rules
evaluation criteria
```

Common outputs:

```text
text
structured data
classification
evaluation report
reasoning summary
```

## 2. CodeExecutionPort

Purpose:

Execute scoped software implementation tasks.

Common inputs:

```text
implementation task
engineering contract
allowed files
rules
skills
acceptance criteria
```

Common outputs:

```text
changed files
summary
tests
risks
follow-up work
```

## 3. DesignGenerationPort

Purpose:

Generate or assist visual design, layout, component, or creative asset work.

Common inputs:

```text
brand profile
identity lock
creative direction
platform format
design rules
```

Common outputs:

```text
design draft
layout spec
component spec
asset preview
export notes
```

## 4. DesignReviewPort

Purpose:

Evaluate design quality, brand fit, campaign clarity, mobile readability, and approval readiness.

Common outputs:

```text
review decision
quality score
required fixes
recommendations
```

## 5. KnowledgeRetrievalPort

Purpose:

Retrieve product, domain, technical, and decision knowledge.

Common sources:

```text
repository docs
knowledge base
vector index
product database
document storage
```

## 6. RepositoryPort

Purpose:

Read and write repository files, branches, pull requests, issues, and review artifacts.

Common outputs:

```text
file content
commit
pull request
review comment
issue
```

## 7. WebAppPort

Purpose:

Provide the web application implementation layer.

Common capabilities:

```text
routing
pages
components
server actions
API routes
state handling
rendering
```

## 8. DatabasePort

Purpose:

Persist and query structured product data.

Common capabilities:

```text
create
read
update
delete
transaction
migration
query
```

## 9. StoragePort

Purpose:

Store files, media, exports, references, and generated assets.

Common capabilities:

```text
upload
download
presigned url
metadata
versioning
delete
```

## 10. PublishingPort

Purpose:

Export, schedule, or publish approved outputs.

Common capabilities:

```text
manual export
schedule
publish
webhook
platform API handoff
```

## 11. EvaluationPort

Purpose:

Evaluate whether output meets contract, rule, quality, safety, or business criteria.

Common outputs:

```text
approved
approved_with_comments
needs_revision
rejected
```

## 12. ObservabilityPort

Purpose:

Track logs, traces, metrics, usage, cost, and errors.

Common outputs:

```text
log event
metric
trace
alert
cost report
```

## Port Design Checklist

- [ ] Capability is clear.
- [ ] Inputs are explicit.
- [ ] Outputs are explicit.
- [ ] Failure behavior is defined.
- [ ] Risk level is known.
- [ ] Human approval requirement is clear.
- [ ] Adapter can be replaced without changing domain model.
