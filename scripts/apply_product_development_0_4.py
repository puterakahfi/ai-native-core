#!/usr/bin/env python3
from pathlib import Path
import yaml

path = Path('contracts/workflows/product-development.contract.yaml')
doc = yaml.safe_load(path.read_text(encoding='utf-8'))
wc = doc['workflow_contract']

wc['version'] = '0.4.0'
wc['purpose'] = (
    'Defines the end-to-end AI-native workflow for developing a digital product from initial idea through '
    'Discovery and Product Brief, PRD, MVP Definition, Product Experience Design, Solution Design, Delivery '
    'Planning, implementation, evidence-backed Product Acceptance, release, deployment, launch, and real-user '
    'Product Validation and Learning. Runtime adapters provide concrete storage, design, task tracking, preview, '
    'deployment, analytics, evidence, and approval mechanisms.'
)

wc['skill_load_order'] = [
    {'phase': 'discovery', 'load': ['model-selection', 'user-research', 'business-value-alignment', 'experiment-design', 'product-manager', 'decision-making']},
    {'phase': 'requirements', 'load': ['product-requirements', 'business-value-alignment', 'product-manager', 'decision-provenance']},
    {'phase': 'mvp_definition', 'load': ['business-value-alignment', 'experiment-design', 'product-manager', 'decision-making', 'spike', 'decision-provenance']},
    {'phase': 'product_experience_design', 'load': ['information-architecture', 'master-design', 'design-foundation', 'accessibility', 'decision-provenance']},
    {'phase': 'solution_design', 'load': ['implementation-context-discovery', 'spec-workflow', 'native-ai-engineer', 'master-engineer', 'api-contract', 'data-modeling', 'decision-provenance']},
    {'phase': 'delivery_planning', 'load': ['delivery-work-breakdown', 'product-manager', 'decision-provenance']},
    {'phase': 'implementation', 'load': ['new-feature-workflow', 'test-driven-development', 'master-engineer', 'systematic-debugging']},
    {'phase': 'acceptance_verification', 'load': ['skill-eval', 'code-review-workflow', 'decision-provenance', 'design-review', 'security-review', 'threat-modeling', 'web-performance', 'accessibility']},
    {'phase': 'release', 'load': ['git-workflow', 'deployment-workflow', 'decision-provenance']},
    {'phase': 'deploy', 'load': ['deployment-workflow', 'observability-design', 'resilience-engineering', 'decision-provenance']},
    {'phase': 'launch', 'load': ['business-value-alignment', 'product-manager', 'content-strategy', 'copywriting', 'cro', 'observability-design', 'decision-provenance']},
    {'phase': 'product_validation_learning', 'load': ['business-value-alignment', 'product-manager', 'observability-design', 'user-research', 'experiment-design', 'decision-making', 'decision-provenance']},
]

wc['quality_gates'] = [
    'opportunity_and_business_value_must_be_explicit_before_prd',
    'discovery_must_produce_a_lightweight_product_brief_before_prd_when_the_opportunity_is_vague',
    'prd_scope_and_readiness_claims_require_verified_authority',
    'prd_must_have_user_value_business_value_goals_non_goals_metrics_scope_and_acceptance_criteria',
    'experiment_first_verdict_must_produce_experiment_design_before_prd_or_build',
    'mvp_scope_must_be_explicit_smaller_than_full_product_value_aligned_and_authorized',
    'mvp_definition_must_own_product_outcome_and_scope_not_detailed_delivery_topology',
    'core_product_experience_must_be_defined_before_solution_design_when_user_or_consumer_interaction_is_material',
    'implementation_context_must_be_inspected_before_material_architecture_or_technology_decisions',
    'solution_design_must_trace_to_verified_prd_mvp_and_experience_decisions',
    'delivery_planning_must_follow_sufficient_solution_design_and_prefer_independently_testable_vertical_outcomes',
    'every_task_must_trace_to_acceptance_criteria',
    'implementation_must_use_new_feature_workflow_boundaries',
    'every_in_scope_acceptance_criterion_must_have_direct_evidence_and_a_matrix_status',
    'changed_user_facing_output_requires_facade_backed_design_acceptance',
    'code_review_workflow_approval_is_required_before_release_eligibility',
    'accepted_risk_and_scope_removal_require_verified_authority',
    'no_release_when_required_evidence_primary_domain_coverage_or_provenance_is_missing',
    'release_ready_does_not_self_authorize_release',
    'release_must_have_notes_version_or_tag_rollback_plan_and_authorization',
    'deployment_authority_and_health_must_be_verified_before_launch',
    'launch_must_define_support_analytics_feedback_loop_and_authorization',
    'product_validation_must_distinguish_real_user_value_from_engineering_verification_and_product_acceptance',
    'workflow_completion_requires_reviewed_usage_evidence_and_an_owned_next_action',
]

wc['stop_points'] = [
    'after_discovery_recommendation',
    'after_experiment_design',
    'after_prd_draft',
    'after_mvp_definition',
    'after_product_experience_design',
    'after_solution_design',
    'after_delivery_plan',
    'before_release',
    'before_deploy',
    'before_launch',
    'after_product_validation_review',
]

wc['compatibility'] = {
    'previous_contract_version': '0.3.0',
    'phase_migrations': {
        'mvp_slice': 'mvp_definition',
        'technical_spec': 'solution_design',
        'learn': 'product_validation_learning',
    },
    'new_phases': ['product_experience_design', 'delivery_planning'],
    'preserved_semantics': [
        'single_product_lifecycle_owner',
        'decision_provenance',
        'acceptance_matrix',
        'release_eligibility_and_authorization_separation',
        'deployment_and_launch_authorization',
        'platform_specialists_as_overlays',
        'direct_entry_when_verified_upstream_artifacts_exist',
    ],
}

wc['phases'] = [
    {
        'id': 'discovery', 'order': 1,
        'description': 'Understand users, jobs, pains, alternatives, opportunity evidence, product and business value, experiment needs, and decision owners; package the result as a lightweight Product Brief.',
        'gate': 'problem_target_user_expected_outcome_value_success_signals_assumptions_evidence_gaps_early_non_goals_and_decision_owners_must_be_explicit_before_prd',
        'skills': {'required': ['user-research', 'business-value-alignment', 'experiment-design', 'product-manager'], 'optional': ['model-selection', 'decision-making', 'decision-provenance']},
        'outputs': ['product_brief', 'problem_evidence', 'target_users_and_jobs', 'expected_outcome_and_value', 'success_signals', 'assumptions_and_evidence_gaps', 'early_non_goals', 'decision_owners'],
    },
    {
        'id': 'requirements', 'order': 2,
        'description': 'Author and verify a PRD with value, goals, non-goals, metrics, scope, requirements, acceptance criteria, launch criteria, evidence plan, and approval sources.',
        'gate': 'prd_readiness_and_scope_provenance_required_before_mvp_or_downstream_design',
        'skills': {'required': ['product-requirements', 'decision-provenance'], 'optional': ['business-value-alignment', 'product-manager']},
    },
    {
        'id': 'mvp_definition', 'order': 3,
        'description': 'Select and approve the smallest valuable end-to-end product outcome or experiment, included and deferred criteria, success metric, risks, assumptions, and scope authority without prematurely defining detailed engineering topology.',
        'gate': 'mvp_outcome_scope_success_metric_and_approval_provenance_must_be_explicit_before_experience_or_solution_design',
        'skills': {'required': ['business-value-alignment', 'experiment-design', 'product-manager', 'decision-making', 'decision-provenance'], 'optional': ['spike']},
    },
    {
        'id': 'product_experience_design', 'order': 4,
        'description': 'Define the core user or consumer journey, flows, information architecture, interaction map, required states, responsive and accessibility expectations, and experience decisions before solution design when interaction is material.',
        'gate': 'core_mvp_experience_must_be_understandable_evaluable_and_traceable_or_explicitly_not_applicable_before_solution_design',
        'skills': {'required': ['information-architecture', 'master-design'], 'optional': ['design-foundation', 'accessibility', 'decision-provenance']},
    },
    {
        'id': 'solution_design', 'order': 5,
        'description': 'Inspect implementation context and translate verified PRD, MVP, and experience decisions into architecture, frontend, backend, domain, data, API, security, deployment, observability, testing, and executable specification decisions.',
        'gate': 'solution_design_and_material_technology_decisions_must_trace_to_verified_inputs_context_constraints_risks_and_authority',
        'skills': {'required': ['implementation-context-discovery', 'spec-workflow', 'native-ai-engineer', 'master-engineer'], 'optional': ['api-contract', 'domain-driven-design', 'data-modeling', 'diagram-architect', 'decision-provenance']},
    },
    {
        'id': 'delivery_planning', 'order': 6,
        'description': 'Define release unit, independently testable vertical slices, dependencies, branch and PR topology, acceptance traceability, activation, rollback, verification, and reviewer plan after sufficient solution design exists.',
        'gate': 'delivery_plan_must_trace_to_verified_mvp_and_solution_decisions_and_each_slice_must_produce_an_observable_outcome',
        'skills': {'required': ['delivery-work-breakdown', 'decision-provenance'], 'optional': ['product-manager', 'git-workflow']},
    },
    {
        'id': 'implementation', 'order': 7,
        'description': 'Implement approved slices through new-feature-workflow with default engineering quality, tests, implementation-context mapping, verification evidence, decision provenance, and scope control.',
        'gate': 'implementation_must_trace_to_verified_acceptance_criteria_experience_solution_and_delivery_decisions',
        'skills': {'required': ['new-feature-workflow', 'test-driven-development', 'master-engineer'], 'optional': ['systematic-debugging', 'refactoring']},
    },
    {
        'id': 'acceptance_verification', 'order': 8,
        'description': 'Reconcile every in-scope PRD criterion with direct evidence, affected-domain reviewers, decision authority, risk provenance, coverage, and explicit product-level verdicts before release.',
        'gate': 'acceptance_matrix_and_release_decision_provenance_must_be_complete_before_release',
        'skills': {'required': ['skill-eval', 'code-review-workflow', 'decision-provenance'], 'optional': ['design-review', 'security-review', 'threat-modeling', 'web-performance', 'accessibility']},
    },
    {
        'id': 'release', 'order': 9,
        'description': 'Prepare traceable release artifacts only for a release-ready candidate while preserving required release authorization.',
        'gate': 'release_ready_traceable_artifacts_rollback_plan_and_explicit_release_authorization_status_are_required',
        'skills': {'required': ['git-workflow', 'decision-provenance'], 'optional': ['deployment-workflow']},
    },
    {
        'id': 'deploy', 'order': 10,
        'description': 'Execute the approved delivery path, verify the actual delivered candidate, health, observability, resilience, and rollback readiness.',
        'gate': 'required_delivery_approval_health_and_rollback_readiness_must_be_verified_before_launch',
        'skills': {'required': ['deployment-workflow', 'observability-design', 'decision-provenance'], 'optional': ['resilience-engineering', 'incident-response']},
    },
    {
        'id': 'launch', 'order': 11,
        'description': 'Make the product available to intended users with approval, communication, support, measurement, monitoring, and feedback channels.',
        'gate': 'launch_approval_user_access_support_measurement_monitoring_and_feedback_must_be_live',
        'skills': {'required': ['product-manager', 'business-value-alignment', 'observability-design'], 'optional': ['content-strategy', 'copywriting', 'cro', 'decision-provenance']},
    },
    {
        'id': 'product_validation_learning', 'order': 12,
        'description': 'Compare real-user qualitative and quantitative evidence with the original value hypothesis, distinguish product validation from engineering verification and PRD acceptance, and produce an attributable continue, improve, pivot, narrow, or stop decision.',
        'gate': 'reviewed_real_usage_evidence_an_owned_next_decision_and_the_next_prd_or_backlog_action_are_required_for_workflow_completion',
        'skills': {'required': ['product-manager', 'business-value-alignment', 'observability-design', 'user-research', 'decision-making', 'decision-provenance'], 'optional': ['experiment-design', 'incident-response', 'skill-evolution']},
    },
]

path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120), encoding='utf-8')
