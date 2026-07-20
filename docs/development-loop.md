# Development Loop — Agent-Driven Execution Cycle

Status: Reusable execution method governed by `contracts/runtime/development-loop.contract.yaml`

Canonical domain lifecycle and typed status semantics: [`domain-model/lifecycle-and-status.md`](domain-model/lifecycle-and-status.md)

Versioned correction of legacy review/approval and documentation-shortcut wording: issue `#26`

## What It Is

The development loop is the reusable execution cycle for Agent-Driven Development. It defines phases, gates, and transitions for performing engineering work. It is not the canonical domain lifecycle and does not replace product or capability workflows.

```text
Explore → Plan → Implement → Verify → Review → Document → Deliver
                      ↑           |         |
                      └───────────┘         |
                      (fix failures)        |
                      ↑                     |
                      └─────────────────────┘
                      (address feedback)
```

## Why It Matters

Without a formalized loop:
- Agents skip exploration → make changes to wrong files
- Agents skip planning → implement without direction
- Agents skip verification → claim "it works" without evidence
- Agents skip review → ship architecture violations
- No feedback loops → same mistakes repeat

The loop makes each phase a **gate** — agents must produce declared outputs before proceeding.

## Phases

### 1. Explore
Understand the problem space before acting.

| Activity | Purpose |
|---|---|
| Read relevant files | Understand current implementation |
| Search codebase | Find related code and usages |
| Check existing tests | Know what's covered |
| Understand architecture | Respect boundaries |

**Exit gate:** Problem space understood with evidence (file paths, code snippets).

### 2. Plan
Decide what to do and in what order.

| Output | Format |
|---|---|
| Task list | File paths + specific changes |
| Approach summary | Why this approach over alternatives |
| Verification strategy | How to prove it works |

**Exit gate:** Plan references exact files, not vague areas.

### 3. Implement
Make the changes.

| Rule | Why |
|---|---|
| Touch only what the task needs | Prevent scope creep |
| No drive-by refactors | Keep diff reviewable |
| Add required imports | Don't leave broken references |
| Match existing style | Consistency over preference |

**Exit gate:** All planned changes applied.

### 4. Verify
Prove the changes work — with real tool output, not claims.

| Check | Command |
|---|---|
| Tests | `npm test`, `pytest`, `php artisan test` |
| Lint | `eslint`, `ruff`, `pint` |
| Build | `npm run build`, `cargo build` |
| Type check | `tsc --noEmit`, `mypy` |

**Exit gate:** All checks pass with evidence (actual command output).

**Critical rule:** Agents must run actual commands. "I believe the tests will pass" is not verification.

### 5. Review
Check quality beyond pass/fail.

| Check | Contract |
|---|---|
| Architecture compliance | engineering-contract, architecture-review |
| Security scan | security-review |
| Performance impact | web-performance |
| Human approval | Required for security-sensitive changes |

**Exit gate (current `1.0.0` contract wording):** Review verdict is `APPROVE` or `CHANGES_REQUESTED`.

**Canonical interpretation:** `APPROVE` here is a legacy positive review disposition, not authority-bearing domain `Approval`. Required approval remains a separate governance decision. Issue `#26` owns the versioned contract correction.

### 6. Document
Capture what changed and why.

| Artifact | When to update |
|---|---|
| Commit message | Always — explain why, not just what |
| Docs | When behavior changes |
| ADR | When architecture decision is made |
| AGENTS.md | When convention changes |

**Exit gate:** Changes are documented and traceable.

### 7. Deliver
Ship the changes.

| Activity | Rule |
|---|---|
| Commit | Atomic commits, conventional messages |
| Push | Always push after commit (don't leave remote behind) |
| PR/Deploy | Follow team workflow |
| Rollback plan | Must exist for production deploys |

**Exit gate:** Changes are in target branch or environment.

## Transitions & Loops

```yaml
explore → plan      # context gathered
plan → implement    # plan approved or low-risk
implement → verify  # changes applied
verify → implement  # verification FAILED (fix loop)
verify → review     # verification PASSED
review → implement  # changes requested (feedback loop)
review → document   # review approved
document → deliver  # documentation complete
```

The two feedback loops are critical:
1. **Verify → Implement**: Fix failures and re-verify until green.
2. **Review → Implement**: Address review feedback and re-verify.

## Shortcuts

For low-risk work, some phases can be skipped:

| Shortcut | Skip | Condition |
|---|---|---|
| Trivial fix | Review, Document | Single file, <10 lines, tests pass |
| Docs only | Verify, Review | Only markdown/comment changes |

Shortcuts must be declared — agents cannot silently skip phases. A declared shortcut does not waive applicable repository policy, relative-link or rendering checks, contradiction review, security review, or authority-bearing approval. The current documentation-only shortcut semantics are tracked for versioned correction in issue `#26`.

## Relationship to Workflows

The Development Loop is **not** a workflow or the canonical domain lifecycle. It is an execution method that may run within a workflow phase.

```text
Workflow: bugfix-workflow
  Phase: investigate   → uses loop (Explore → Plan)
  Phase: fix           → uses loop (Implement → Verify)
  Phase: review        → uses loop (Review)
  Phase: submit        → uses loop (Document → Deliver)
```

Workflows define **what** to do. The loop defines **how** each step executes.

## Contract Reference

See `contracts/runtime/development-loop.contract.yaml` for the formal specification.
