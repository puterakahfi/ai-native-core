# Security Baseline Port

## Purpose

`SecurityBaselinePort` defines the boundary for security validation, scanning,
and enforcement across Native AI Framework product instances.

It ensures that AI-generated and human-written code meets the required security
baseline before reaching production.

## Position in the Framework

```text
Implementation
→ SecurityBaselinePort
→ Security Scan / Review
→ Security Gate Decision
→ Review / Deployment
```

## Primary Responsibilities

- Enforce security baseline rules per product instance.
- Detect secrets, credentials, and sensitive data in code.
- Validate SQL injection prevention.
- Validate input sanitization and output encoding.
- Validate authorization and access control.
- Validate dependency security.
- Block deployment until security gate is passed.
- Preserve audit trail for security decisions.

## Non-Responsibilities

`SecurityBaselinePort` must not:
- deploy to production by itself,
- auto-approve security-sensitive changes,
- replace Engineering Contract as the security strategy authority,
- expose secret values in scan reports or logs.

## Security Baseline (OWASP-aligned)

Minimum security requirements for all product instances:

```text
A01 Broken Access Control   → verify permission at every endpoint/action
A02 Cryptographic Failures  → no hardcoded secrets, HTTPS, proper password hashing
A03 Injection               → parameterized queries, sanitized input
A04 Insecure Design         → acceptance criteria include security cases
A05 Misconfiguration        → no debug info exposed to users, config from env
A06 Vulnerable Components   → dependency audit before adding packages
A07 Auth Failures           → proper session management, logout clears session
A08 Data Integrity          → validate all input, never trust client data
A09 Logging Failures        → log security events, never log sensitive data
A10 SSRF                    → validate URL input before HTTP requests
```

## Candidate Adapters

```text
StaticAnalysisScanAdapter   — Psalm, PHPStan, Semgrep
SecretsDetectionAdapter     — detect-secrets, truffleHog
DependencyAuditAdapter      — composer audit, npm audit
ManualSecurityReviewAdapter — human security checklist
```

## Security Gate Decision

```text
passed          → proceed to deployment
passed_with_notes → proceed, document residual risk
needs_fix       → block deployment, fix required
critical        → block immediately, escalate to team lead
```

## Sensitive Data Policy

```text
Never log:     password, token, API key, credit card, SSN, session token
May log:       user ID, timestamp, action type, IP address, error code
Never commit:  .env, private key, credential file, certificate
```

## Done Criteria

- [ ] No hardcoded secrets or credentials detected.
- [ ] All SQL queries use parameterized statements or safe escaping.
- [ ] All user input validated and sanitized.
- [ ] Authorization check present at every protected endpoint.
- [ ] Dependency audit clean (no known critical vulnerabilities).
- [ ] Security review checklist completed.
- [ ] Security gate decision is explicit.
