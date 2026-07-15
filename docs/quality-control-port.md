# Quality Control Port

## Purpose

`QualityControlPort` defines the boundary for testing, QA verification, and quality gates
across Native AI Framework product instances.

It ensures AI-generated and human-written code cannot proceed to production without
passing the required quality checks — manual, automated, or both.

## Position in the Framework

```text
Implementation
→ QualityControlPort
→ Test Execution (E2E, unit, integration, manual)
→ QA Gate Decision
→ Review / Deployment
```

## Primary Responsibilities

- Define testing strategy per product instance.
- Run or coordinate automated tests (E2E, unit, integration).
- Execute manual staging verification checklist.
- Block PR / deployment until quality gate is passed.
- Capture test evidence (screenshots, logs, test output).
- Communicate QA gate status to review and deployment ports.

## Non-Responsibilities

`QualityControlPort` must not:
- deploy to production by itself,
- approve code review independently,
- replace Engineering Contract as the testing strategy authority,
- auto-pass quality gate without actual test evidence.

## Test Priority Order

```text
1. Domain rules / business logic
2. Application use cases / service layer
3. API contracts (input, output, error)
4. Security-sensitive flows (auth, permission, payment)
5. Integration boundaries (DB, external API)
6. UI interaction states (E2E / Playwright)
```

Always test failure paths, not only happy paths.

## Candidate Adapters

```text
PlaywrightE2EAdapter        — browser-based E2E testing
PHPUnitAdapter              — PHP unit and integration testing
ManualStagingAdapter        — human-executed staging checklist
CITestRunnerAdapter         — automated test run in CI pipeline
```

## Test Evidence Contract

Every QA pass must include evidence:

```yaml
qa_evidence:
  staging_url: ""
  tested_flows: []
  failure_paths_tested: true
  no_console_errors: true
  no_server_errors: true
  screenshot_or_log: ""   # required for E2E and UI changes
  tested_by: ""
  tested_at: ""
```

## Quality Gate Decision

```text
passed         → proceed to PR review / deployment
passed_with_notes → proceed, but document known limitations
failed         → block PR, fix required
blocked        → cannot test, dependency missing
```

## Done Criteria

- [ ] Test strategy defined in Engineering Contract.
- [ ] Happy path and failure path both tested.
- [ ] Test evidence captured and attached to PR.
- [ ] No fatal errors in staging logs.
- [ ] Security-sensitive flows tested.
- [ ] QA gate decision is explicit (not assumed).
