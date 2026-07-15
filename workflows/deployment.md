# Deployment Workflow

## Purpose

Define how a product instance moves from a verified implementation to a deployed,
production-ready state inside the Native AI Framework.

## Workflow

```text
Verified Implementation (QA passed, security passed, PR approved)
→ Pre-Deployment Check
→ Environment Deployment
→ Smoke Test
→ Deployment Verification
→ Post-Deployment Update (Jira, docs, team notification)
```

## 1. Pre-Deployment Check

Before deploying to any environment:

```text
- PR approved and merged to correct target branch
- QA gate passed (QualityControlPort evidence attached)
- Security gate passed (SecurityBaselinePort evidence)
- No unresolved merge conflicts
- No debug code remaining
- No hardcoded secrets
- DB migration prepared and tested (if applicable)
- Team notified (no silent production deployments)
- Rollback plan prepared for high-risk changes
```

## 2. Environment Deployment

### Staging
- Target: release branch or staging-equivalent
- Purpose: QA verification, integration testing
- Access: engineering team

### Production
- Target: master/main via approved PR only
- Purpose: live user traffic
- Access: controlled, coordinated with team
- Requires: staging verification passed + review approved

## 3. Smoke Test

After every deployment:

```text
- Application loads without 500/404 errors
- Authentication flow works
- Primary user flows for changed features work
- No new errors in server/application logs
- Database queries executing normally
```

## 4. Deployment Verification

Verify the correct version is deployed:

```text
- Git commit SHA matches expected
- Service health check passes
- Log shows no new critical errors
- Key feature accessible and functional
```

## 5. Post-Deployment

After successful deployment:

```text
- Update Jira ticket status (Done or as appropriate)
- Notify team that deployment completed
- Document any known issues or follow-up tasks
- Update runbook if deployment revealed new operational knowledge
```

## Rollback Protocol

If issues are found after deployment:

```text
Critical (site down, data corruption, auth broken):
→ Rollback immediately → assess → fix → re-deploy

Major (feature broken, site stable):
→ Assess rollback vs hotfix → team decision → execute

Minor (UI bug, non-critical):
→ Hotfix in next cycle → no rollback needed
```

## Done Criteria

- [ ] Deployment target environment is correct.
- [ ] Pre-deployment checklist completed.
- [ ] Deployment executed and verified.
- [ ] Smoke test passed.
- [ ] Post-deployment updates completed.
- [ ] No unresolved errors in production logs.
- [ ] Rollback plan was prepared before high-risk deploy.
