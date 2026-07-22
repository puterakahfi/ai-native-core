# Composition And Visual Hierarchy V2 — Acceptance Review

Status: candidate acceptance evidence for `ai-native-core#44`

Pull request: `#46`

## Objective

Issue `#44` requires the canonical `composition` and `visual-hierarchy` contracts to stop treating website, hero, heading-ratio, contrast-count, and spacing heuristics as universal Native AI Engineering laws.

Candidate result:

```text
composition contract v2: IMPLEMENTED
visual-hierarchy contract v2: IMPLEMENTED
breaking compatibility classification: IMPLEMENTED
counterexample behavioral contracts: IMPLEMENTED
manifest and schema discovery regeneration: IMPLEMENTED
downstream migration requirements: IMPLEMENTED
runtime or product acceptance: NOT CLAIMED
```

## Contract versions

```text
composition
contracts/skills/design/composition.contract.yaml
1.0.0 → 2.0.0

visual-hierarchy
contracts/skills/design/visual-hierarchy.contract.yaml
1.0.0 → 2.0.0
```

A major version is required because capability meaning, required inputs, required outputs, quality gates, boundaries, and adapter requirements change incompatibly.

No path alias is required because canonical paths remain unchanged. Consumers pinned to version `1.x` are not automatically upgraded.

## Removed universal composition gates

```text
focal_point_must_be_at_or_above_optical_center
no_unframed_dead_space_above_hero
every_element_anchored_to_grid_or_sibling
spacing_multiples_of_8px_base_unit
```

Replacement model:

```text
surface and viewing context
primary task or message
content roles
focal sequence
visual-weight distribution
intentional balance strategy
structural, relational, and optical anchors
named empty-space roles
responsive composition intent
rendered evidence
```

Optical center, geometric center, F/Z patterns, rule of thirds, modular spacing, grids, and above-fold scans remain available as diagnostics. They cannot establish failure without observed harm to task, message, reading, grouping, or flow.

## Removed universal visual-hierarchy gates

```text
supporting_h2_must_be_60pct_or_less_of_h1_size
no_h2_larger_than_h1
minimum_3_distinct_contrast_levels
no_section_heading_heavier_than_hero_h1
```

Replacement model:

```text
semantic, task, action, and state roles
principal, local, and temporary dominance
multiple contextual hierarchy cues
section and task progression
parent-child relationships
action, metadata, and feedback priority
responsive and state relationship preservation
actual-content and rendered evidence
```

H1/H2 ratios, heading decay, contrast-level counts, weight deltas, isolation deltas, and section-weight decay remain diagnostics. They are not universal pass thresholds.

## Surface coverage

The contracts now support multiple relevant profiles rather than one marketing-page template:

```text
marketing
product and application
editorial
static visual communication
presentation
responsive surfaces
stateful and overlay contexts
```

The required context is explicit through target surface, surface profile, content or semantic roles, task/message, viewing context, responsive context, and state context.

## Ownership and boundaries

`composition` owns:

```text
focal sequence and visual flow
visual-weight distribution
intentional balance
structural, relational, and optical anchoring
empty-space role classification
responsive composition intent
composition risks and evidence requirements
```

`visual-hierarchy` owns:

```text
semantic and task role mapping
principal, local, and state-dependent dominance
multi-cue hierarchy strategy
section and cross-section weight sequence
action, metadata, and feedback priority
responsive and state relationship preservation
hierarchy ambiguity risks and evidence requirements
```

They do not own:

```text
page macrostructure selection
component pattern selection
typeface or typography-token implementation
accessibility compliance verdict
canonical design gate identity
review scoring, coverage, or verdict
product acceptance
approval or authorization
```

`design-review` remains the authority for canonical gate identity, evidence normalization, scoring, coverage, and verdict.

## Behavioral counterexamples

`contracts/tests/composition.test.yaml` adds five cases:

```text
asymmetric editorial focal point below center
channel safe area as utility empty space
coherent non-8px spacing system
dense operational surface
responsive intent rather than coordinate preservation
```

`contracts/tests/visual-hierarchy.test.yaml` adds five cases:

```text
blocking error temporarily outranks page heading
local application task anchor may exceed page-title scale
presentation dominance resets per slide
simple surface may need only two clear emphasis levels
responsive hierarchy preserves role relationships
```

Every case references only quality gates owned by its v2 contract. The cases prohibit reintroducing the removed heuristics as universal rules.

## Compatibility and downstream migration

Canonical migration record:

```text
docs/design-contract-v2-migration.yaml
```

The merged downstream state in `puterakahfi/ai-native-skills` currently contains reviewed core-gap exemptions for:

```text
skills/composition
skills/visual-hierarchy
```

After core acceptance, downstream migration must:

1. review each executable interface and boundary against contract v2;
2. add adjacent structured conformance declarations pinned to `^2.0.0`;
3. remove exemptions only after structural conformance is confirmed;
4. run Contract Coverage, Skill And Gate Contracts, and relevant behavioral evals;
5. preserve structural, behavioral, runtime, and product evidence as separate claims.

Exact contract ID and path match are not sufficient to remove an exemption.

## Generated metadata

The schema-aware generator records:

```text
composition@2.0.0
visual-hierarchy@2.0.0
composition behavioral test@2.0.0
visual-hierarchy behavioral test@2.0.0
```

Generated artifacts:

```text
contracts/manifest.yaml
docs/contract-schema-discovery.yaml
```

Temporary validation workflows and runtime logs are absent from the final diff. `.tmp/` is now ignored to prevent validation output from entering source control.

## Validation evidence

Temporary full-suite finalization:

```text
Temporary issue 44 finalize
run 29912814602 — PASS

Temporary issue 44 regenerate
run 29913349556 — PASS
```

Permanent conformance regression on the reviewed contract content:

```text
Validate Conformance Tooling
run 29913349469 — PASS
```

The temporary suites executed the same schema, identity, port, behavioral-contract, and regression commands used by Contract Integrity, plus issue-specific assertions for removed gates, diagnostics, versions, test coverage, and migration semantics.

Exact final-head permanent workflow results are recorded in PR `#46` checks after this acceptance artifact and catalog navigation are included.

## Evidence boundary

```text
contract registration
≠ adapter conformance

structural conformance
≠ behavioral verification

behavioral verification
≠ runtime evidence

runtime evidence
≠ product acceptance

product acceptance or review
≠ approval or authorization
```

This issue does not claim downstream adapter conformance, rendered product verification, runtime installation, or authority-bearing approval.

## Acceptance matrix

| Criterion | Result |
|---|---|
| Composition no longer treats optical-center, hero dead space, or 8px spacing as universal pass rules | PASS |
| Visual hierarchy no longer treats fixed H1/H2 ratios, contrast counts, or monotonic hero dominance as universal pass rules | PASS |
| Inputs and outputs support multiple surface profiles and contexts | PASS |
| Gates express transferable reasoning | PASS |
| Diagnostic heuristics remain available without universal authority | PASS |
| Counterexample behavioral contracts are present | PASS |
| Boundaries and design-review authority are explicit | PASS |
| Compatibility impact uses a breaking major version | PASS |
| Consumer migration is explicit | PASS |
| Generated manifest and schema discovery are current | PASS |
| Temporary source artifacts are absent | PASS |
| Contract Integrity | PENDING EXACT FINAL-HEAD RUN |
| Validate Conformance Tooling | PENDING EXACT FINAL-HEAD RUN |

## Candidate verdict

```text
contract semantic correction: PASS
behavioral counterexample coverage: PASS
compatibility and migration: PASS
generated metadata: PASS
evidence boundaries: PASS
ready for owner review: PENDING EXACT FINAL-HEAD CI
ready for merge: NO — owner approval required
```
