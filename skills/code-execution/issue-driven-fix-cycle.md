# Skill: Issue-Driven Fix Cycle

## Purpose

Execute a complete bugfix or task cycle driven by an issue tracker ticket:
read the issue, prepare the branch, implement the fix, verify it, open a PR,
and report back to the issue tracker.

This skill covers the full agent loop from issue intake to ready-for-review.

## When To Use

Use this skill when:

- An issue tracker ticket is the starting point for work.
- The work type is bugfix, security fix, small task, or scoped improvement.
- The agent is expected to own the full cycle end-to-end with minimal human input.
- The output must include a branch, a commit, a PR, and an issue tracker update.

Do not use this skill for:

- Large feature development with multiple modules or UI design decisions (use `workflows/feature-development.md`).
- Architecture changes that require an ADR.
- Any destructive database or infrastructure operation.

## Required Input

```text
- Issue tracker ticket ID
- Project repo path and remote
- Active release branch or target branch for PR
- Stack context (language, framework, test runner)
```

## Procedure

### Phase 1: Issue Intake

1. Read the issue: summary, description, acceptance criteria, reporter, latest comments.
2. Identify affected files, modules, or code paths mentioned in the issue.
3. Confirm the fix scope: what changes, what stays untouched.

### Phase 2: Pre-Work Git Checklist

Before touching any code:

1. Confirm current repo path (`pwd`).
2. Confirm current branch (`git branch --show-current`).
3. Check working tree state (`git status`).
4. Confirm remote (`git remote -v`).
5. Check recent commits (`git log --oneline -5`).
6. Fetch latest remote state (`git fetch origin`).
7. Identify the correct **source branch** per project SOP.
8. Stash or clean any unrelated local changes before branching.

### Phase 3: Branch

1. Create a new branch from the source branch following the project's naming convention.
2. Confirm the new branch is clean and tracking the correct remote.

### Phase 4: Inspect Affected Code

1. Read the affected file(s) at the exact reported line(s).
2. Trace the data flow: where does the input come from, how is it used, where does it go.
3. Check for other call sites with the same pattern in the codebase.
4. Understand the fix before writing any code.

### Phase 5: Implement

1. Apply the minimal fix that satisfies the issue acceptance criteria.
2. Do not refactor unrelated code.
3. Add a short inline comment referencing the ticket ID when the fix is non-obvious.
4. Match existing code style, indentation, and conventions.

### Phase 6: Verify

1. Run syntax/lint check on modified files.
2. Run automated tests if available.
3. If no automated test exists, write a targeted ad-hoc verification script or manual test steps.
4. Confirm the fix handles all stated edge cases.
5. Confirm no regression in adjacent code paths.

### Phase 7: Commit

1. Stage only the files related to the fix.
2. Write a commit message that references the ticket ID and summarises what changed and why.
3. Push the branch to remote.

### Phase 8: Pull Request

1. Open a PR from the fix branch targeting the source branch.
2. PR title and description must make the change reviewable without reading the diff — include what the issue was, what was changed, and how to verify.
3. Do not merge the PR without explicit human approval.

### Phase 9: Issue Tracker Update

1. Transition the issue status at start of work and again after the PR is ready, per project workflow.
2. Post a comment with the branch name, PR link, summary of what was fixed, and verification steps for QA.
3. Draft the comment first; post only after human confirmation unless explicitly authorized to auto-post.

## Output

Return:

```text
Issue Read            — ticket ID, summary, affected file:line
Pre-Work Check        — branch, status, source branch confirmed
Branch Created        — branch name, tracking remote
Fix Applied           — files changed, lines changed, approach
Verification Result   — test output or manual check result
Commit                — commit SHA, message summary
PR                    — PR URL or creation command
Issue Updated         — transition applied, comment drafted or posted
Risks                 — anything unverified, deferred, or out of scope
```

## Quality Checklist

- [ ] Issue fully read before any code change.
- [ ] Pre-work git checklist completed.
- [ ] Branch created from correct source branch.
- [ ] Fix is minimal — no unrelated changes.
- [ ] Syntax/lint check passed.
- [ ] Verification covers relevant edge cases.
- [ ] Commit message references ticket ID.
- [ ] PR targets correct branch.
- [ ] Issue tracker updated.
- [ ] Draft comment shown to human before posting.

## Failure Handling

- **Cannot reproduce the issue**: stop, document what was inspected, ask the reporter for clarification.
- **Affected code has changed since the report**: re-read, re-analyze, re-confirm scope before fixing.
- **Merge conflict**: follow project SOP for conflict resolution — do not resolve by merging shared/staging branches into the fix branch.
- **Verification fails**: do not push. Fix the root cause, re-verify, then push.
