# LearningProductPort

## Purpose

`LearningProductPort` defines the boundary for learning products.

It supports tutorials, mini courses, lesson modules, assignments, and assessments where the deliverable is a structured learning path.

## Position in Native AI Framework

```text
ProductOutputPort
→ LearningProductPort
→ Learning Product Contract
→ Curriculum Context
→ Lesson / Assessment Skills
→ Media or Content Adapter
→ Review
→ Packaging
```

## Supported Output Types

```text
video_tutorial
mini_course
course_module
lesson_plan
assignment
assessment
```

## Responsibilities

- Define learner, outcome, prerequisites, and course promise.
- Structure modules, lessons, assignments, and assessments.
- Map learning objectives to lesson content.
- Define script, slide, workbook, or platform package requirements.
- Produce reviewable learning artifacts.

## Non-Responsibilities

`LearningProductPort` must not:

- publish courses without approval,
- replace subject-matter review,
- make unsupported learning claims,
- execute video production directly,
- own payment or platform distribution.

## Input Contract

```yaml
learning_product_input:
  product_id: ""
  output_type: "video_tutorial | mini_course | course_module | lesson_plan | assignment | assessment"
  learner_profile: ""
  learning_outcomes: []
  prerequisites: []
  modules: []
  source_paths: []
  delivery_format: ""
```

## Output Contract

```yaml
learning_product_output:
  curriculum_outline: []
  lesson_plans: []
  scripts: []
  assignments: []
  assessments: []
  review_checklist: []
  packaging_manifest: {}
```

## Default Workflow

```text
Define Learner Outcome
→ Build Curriculum Outline
→ Draft Lessons
→ Add Exercises / Assignments
→ Add Assessment
→ Prepare Media or Content Package
→ Review Learning Quality
→ Package
→ Publish only after approval
```

## Candidate Adapters

Taxonomy candidates only:

```text
VideoScriptAdapter
SlideDeckAdapter
PDFExportAdapter
GoogleDocsExportAdapter
YouTubePublishingAdapter
```

## Quality Gates

- learning outcome is explicit,
- prerequisites are known,
- lesson sequence is coherent,
- assignments support outcomes,
- assessments match objectives,
- source claims are reviewable,
- media package is approval-gated.

## Dashboard Usage

`LearningProductPort` should show:

```text
curriculum status
lesson count
assignment status
assessment status
media package status
review status
```

## Relationship to Existing Ports

```text
ProductOutputPort     → selects LearningProductPort
ContentProductPort    → may generate workbooks/guides
MediaProductPort      → may generate scripts/slides/video plans
ReviewApprovalPort    → approves course package
```

## Failure Behavior

- If outcomes are missing, return `learning_outcomes_required`.
- If source context is missing, return `curriculum_context_required`.
- If assessment does not match outcomes, return `assessment_alignment_required`.
- If publishing is requested before approval, return `publishing_blocked`.
