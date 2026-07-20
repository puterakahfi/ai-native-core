# Review Approval Port — Legacy Navigation

Status: Superseded explanatory document

The legacy `ReviewApprovalPort` combined three independent semantic families. No canonical alias preserves that collapsed name.

## Canonical contracts

```text
contracts/ports/control/review-management.port.yaml
contracts/ports/control/approval-decision.port.yaml
contracts/ports/control/authorization-assessment.port.yaml
```

Canonical display names:

```text
ReviewManagementPort
ApprovalDecisionPort
AuthorizationAssessmentPort
```

## Review management

Owns ReviewRequest, ReviewResult references, findings, reviewer attribution, and canonical `ReviewDisposition` transitions.

```text
review completed
≠ approval granted
```

## Approval decision

Records an authority-bearing decision for a named subject and scope, including conditions, provenance, validity, revocation, and expiry.

```text
positive review
≠ Approval
```

Approval requires applicable authority and policy.

## Authorization assessment

Evaluates whether one concrete action may proceed now using current permission, authority, approvals, policy, risk controls, scope, capacity, conditions, and validity.

```text
Approval
≠ action authorization by itself
≠ successful execution
```

## Required distinctions

```text
GateOutcome
≠ ReviewDisposition
≠ ApprovalStatus
≠ AuthorizationAssessment
≠ ExecutionStatus
≠ CompletionDisposition
```

The dashboard or workflow may present these records together, but it must not serialize them as one generic status or treat one family as proof of another.

## Legacy adapter examples

Dashboard, GitHub, pull-request, Slack, email, or manual review integrations remain possible adapters. Their provider permission and transport do not grant Native AI Engineering authority.

## Migration

Consumers must reference the specific boundary they use through stable port ID, canonical path, and compatible version. A single `review-approval` alias is intentionally prohibited because it would recreate the retired semantic collapse.

The machine authority is the versioned port contracts and generated manifest, not this Markdown document.
