# Issue 45 Acceptance Review

Issue: `puterakahfi/ai-native-core#45`

Scope:

```text
design-audit
image-prompt-engineering
skill-maintenance
```

## Decision summary

Three reusable executable capabilities discovered as downstream core gaps now have runtime-agnostic canonical contracts:

```text
design-audit
→ skill_contract@1.0.0

image-prompt-engineering
→ skill_contract@1.0.0

skill-maintenance
→ workflow_contract@1.0.0
```

The contract IDs describe stable capabilities and lifecycles. Downstream executable names may differ:

```text
prompt-engineer → image-prompt-engineering
skill-doctor    → skill-maintenance
```

Name mapping does not prove adapter conformance.

## Acceptance matrix

### Design audit contract distinct from design-review authority

Status: satisfied.

Evidence:

```text
contracts/skills/quality/design-audit.contract.yaml
contracts/tests/design-audit.test.yaml
```

`design-audit` owns:

- audit-context classification;
- evidence-capture planning;
- review-result referencing;
- root-cause grouping;
- gap prioritization;
- coverage limitation reporting;
- next-lifecycle recommendation;
- audit report assembly.

It explicitly does not own:

- canonical design gate identity or registry;
- design-review routing, scoring, coverage, or verdict semantics;
- specialist diagnosis without a loaded specialist;
- redesign or implementation output;
- product acceptance, approval, or authorization.

Behavioral counterexamples reject complete passes for unsupported primary domains, screenshot-only runtime claims, audit-to-redesign collapse, and audit-owned gate or verdict invention.

### Provider-neutral image prompt engineering contract

Status: satisfied.

Evidence:

```text
contracts/skills/design/image-prompt-engineering.contract.yaml
contracts/tests/image-prompt-engineering.test.yaml
```

The contract owns:

- generation-intent classification;
- provider-neutral prompt planning;
- visual-constraint structuring;
- asset, identity, text, and exclusion locks;
- declared model-dialect handoff;
- completeness and contradiction review;
- observed-output failure analysis;
- evidence-driven prompt iteration.

Provider syntax, parameter names, token or character limits, weighting conventions, model capability profiles, inference, policy enforcement, and generated-output acceptance remain external.

The canonical contract contains no DALL-E, Midjourney, Stable Diffusion, Flux, vendor parameter, fixed token-limit, fixed character-limit, or weighting-threshold rule.

Behavioral counterexamples reject fabricated syntax for unknown models, universal provider limits, loss of asset locks, generic quality-tag iteration, and policy or rights bypass claims.

### Reusable skill-maintenance lifecycle

Status: satisfied.

Evidence:

```text
contracts/workflows/skill-maintenance.contract.yaml
contracts/tests/skill-maintenance.test.yaml
```

Canonical lifecycle:

```text
audit
→ triage
→ repair
→ verify
→ report
```

The workflow treats line count, section position, reminder position, file count, and reference-file size as adapter or repository diagnostics. They do not establish universal failure by themselves.

The workflow explicitly delegates:

```text
behavioral application verdict
→ skill-eval

generalized learning promotion
→ skill-evolution

write, approval, release, and ownership policy
→ repository governance
```

Behavioral counterexamples reject automatic splitting by line count, short-file health claims despite contradiction, universal top/bottom placement thresholds, behavioral claims without skill-eval, and silent learning promotion during maintenance.

### Boundaries and handoffs explicit

Status: satisfied.

Each contract declares owned and excluded responsibilities plus adapter requirements. `skill-maintenance` additionally declares ordered handoffs, transitions, and exit conditions.

Important non-collapses:

```text
design audit
≠ design-review verdict authority

prompt structure validation
≠ generated-image evidence or acceptance

skill structural maintenance
≠ behavioral evaluation
≠ learning evolution
≠ repository approval
```

### Counterexamples prevent provider and repository detail leakage

Status: satisfied.

Registered behavioral cases cover:

```text
5 design-audit cases
5 image-prompt-engineering cases
6 skill-maintenance cases
```

These cases preserve provider-neutral and repository-neutral boundaries while allowing adapters to retain model profiles, commands, thresholds, and local operating policy.

### Compatibility and downstream migration explicit

Status: satisfied for core; downstream execution remains pending.

Evidence:

```text
docs/missing-capability-contracts-migration.yaml
```

Expected downstream mappings:

```text
skills/design-audit/SKILL.md
→ design-audit@^1.0.0

skills/prompt-engineer/SKILL.md
→ image-prompt-engineering@^1.0.0

skills/skill-doctor/SKILL.md
→ skill-maintenance@^1.0.0
```

The merged `core_gap` exemptions in `ai-native-skills` must remain until each executable is reviewed, receives an adjacent declaration, and passes structural conformance. Exemption removal is a downstream migration, not proof created by this core PR.

## Validation evidence

The controlled issue workflow executed the permanent Contract Integrity commands and additional semantic assertions before committing generated metadata. The permanent workflows are also required on the final review head.

Core validation surface:

```text
./scripts/generate-manifest.sh
python3 scripts/inventory-contract-schemas.py
python3 scripts/validate-contract-schemas.py
python3 scripts/validate-contract-identity.py
python3 scripts/validate-port-contracts.py
python3 scripts/run-eval.py --all --validate-tests
python3 -m unittest discover -s tests -p 'test_validate_contract_schemas.py' -v
python3 -m unittest discover -s tests -p 'test_contract_resolution.py' -v
python3 -m unittest discover -s tests -p 'test_validate_port_contracts.py' -v
python3 -m unittest discover -s tests -p 'test_port_inventory.py' -v
python3 -m unittest discover -s tests -p 'test_validate_port_adapter_reference.py' -v
python3 scripts/inventory-contract-schemas.py --check
```

Generated registry after this change:

```text
135 contract artifacts
```

## Known limitations

This core change does not establish:

- static conformance of the three downstream executables;
- behavioral verification of those executables;
- provider capability accuracy;
- runtime integration or model-generation evidence;
- product acceptance;
- review, approval, or authorization.

Provider dialect references in `prompt-engineer` and repository thresholds in `skill-doctor` require downstream classification as adapter-owned extensions during migration.

## Acceptance conclusion

The issue objective and core acceptance criteria are satisfied when the final review head passes Contract Integrity and Validate Conformance Tooling.

No downstream exemption should be removed and no adapter should be labeled conformant solely from this acceptance record.
