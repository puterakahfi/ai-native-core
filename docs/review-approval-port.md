# ReviewApprovalPort

## Purpose

`ReviewApprovalPort` defines the boundary for human-in-the-loop review, approval, rejection, and revision control across Native AI Framework workflows.

It exists so AI-generated outputs, task execution results, publishing actions, destructive actions, and production changes cannot silently proceed without the required review gate.

## Position in the Framework

```text
Generated Output / Execution Run
→ Review Request
→ Human Review
→ Approval / Rejection / Revision
→ Next Workflow Step
```

`ReviewApprovalPort` is a governance and safety port. It is not a task manager, code executor, or UI generator.

## Primary Responsibilities

- Create review requests.
- Track reviewer decisions.
- Record approval, rejection, and revision notes.
- Block unsafe workflow steps until approved.
- Link decisions to tasks, execution runs, PRs, generated assets, and publishing actions.
- Expose review status to the dashboard.
- Preserve audit trail for human decisions.

## Non-Responsibilities

`ReviewApprovalPort` must not:

- execute code,
- publish content by itself,
- mutate production systems without an approved downstream adapter,
- auto-approve high-impact actions,
- hide reviewer identity or decision metadata,
- replace acceptance criteria evaluation.

## Candidate Adapters

```text
ManualApprovalAdapter
DashboardApprovalAdapter
GitHubReviewAdapter
PullRequestReviewAdapter
SlackApprovalAdapter
EmailApprovalAdapter
```

## Status Flow

```text
not_requested
→ requested
→ in_review
→ approved
→ rejected
→ revision_requested
→ expired
```

## Default Review Workflow

```text
Receive Reviewable Output
→ Create Review Request
→ Notify Reviewer
→ Record Decision
→ Attach Notes
→ Unblock or Block Next Step
→ Store Audit Trail
```

## Input Contract

```yaml
review_approval_input:
  review_subject_type: ""
  review_subject_id: ""
  canonical_task_id: ""
  reviewer: ""
  required_decision: ""
  risk_level: ""
  approval_policy: ""
```

## Output Contract

```yaml
review_approval_output:
  review_id: ""
  status: ""
  decision: ""
  reviewer: ""
  notes: []
  approved_at: null
  next_action: ""
```

## Quality Gates

- reviewer is known,
- review subject is linked,
- decision is explicit,
- approval policy is respected,
- high-impact actions are not auto-approved,
- decision is auditable,
- revision request preserves context.

## Dashboard Usage

`ReviewApprovalPort` should power:

```text
/reviews
/task review state
/execution run approval
/publishing approval
/destructive action approval
```

It should make the dashboard the human approval layer for AI-native development workflows.
