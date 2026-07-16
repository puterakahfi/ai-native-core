# Experiment Design

Experiment design is the runtime-agnostic capability for turning a value hypothesis or uncertain opportunity into the smallest ethical test that can produce a decision.

It is formalized by:

```text
contracts/skills/product-management/experiment-design.contract.yaml
```

Runtime adapters may provide artifact templates, analytics tooling, survey/interview channels, waitlist forms, prototype tools, or evidence stores. The core contract only defines the required shape of the experiment and its quality gates.

## Purpose

Use experiment design when the team should learn before building. It answers:

```text
What is the riskiest assumption?
What is the smallest test that can falsify it?
What evidence is enough to continue, narrow, pivot, or stop?
```

## Boundary

Experiment design owns:

- falsifiable hypotheses
- riskiest assumption selection
- experiment type selection
- smallest-test design
- measurable success and guardrail criteria
- data collection plan
- decision rule
- next steps by outcome

Experiment design does not own:

- full PRD authoring
- production implementation
- analytics system implementation
- user research synthesis beyond experiment-specific learning
- release or launch execution

## Required Artifact

Every experiment spec must include:

```text
hypothesis
target_segment
riskiest_assumption
smallest_test
experiment_type
setup_steps
success_criteria
guardrail_criteria
duration_or_timebox
sample_or_signal_threshold
data_collection_plan
decision_rule
risks_and_mitigations
next_steps_by_outcome
```

## Experiment Types

Allowed experiment types include:

```text
concierge_test
landing_page_waitlist
prototype_test
fake_door_test
wizard_of_oz
manual_service_pilot
interview_script
smoke_test
pricing_test
content_or_offer_test
technical_spike
```

Adapters may add product-specific variants, but they should still map back to one of these abstract types.

## Quality Gates

- Hypothesis is falsifiable.
- Riskiest assumption is named before choosing the test method.
- Smallest test is smaller than building the full solution.
- Success criteria are measurable before running the experiment.
- Guardrail criteria prevent harm, misleading claims, or misleading learning.
- Decision rule defines pass, partial, and fail actions.
- Experiment states what will not be built yet.
- Data collection respects privacy and consent.
- Learning feeds a PRD, MVP slice, pivot, or stop decision.

## Decision Rule

The experiment must end with a rule like:

```text
PASS    → proceed to PRD/MVP slice
PARTIAL → run targeted follow-up discovery or narrow the value proposition
FAIL    → stop, pivot, or choose a different opportunity
```

## Relationship to Business Value Alignment

`business-value-alignment` can return:

```text
Verdict: EXPERIMENT_FIRST
```

When that happens, this capability turns the verdict into an executable learning plan. The traceability chain should be:

```text
value alignment brief → hypothesis → riskiest assumption → experiment spec → evidence → PRD/MVP/stop decision
```
