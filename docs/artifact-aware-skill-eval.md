# Artifact-aware skill evaluation

The canonical skill-eval runner supports two distinct evidence layers:

```text
agent output assertions
  prove required reasoning, decisions, classifications, and ordering appear in output

artifact assertions
  inspect bounded files and fixture-local evidence produced by an implementation
```

Neither layer replaces runtime, rendered, accessibility, architecture, security, product acceptance, or merge authorization evidence.

## Backward compatibility

Existing test contracts using `must_contain`, `must_not_contain`, `must_contain_one_of`, and `sequence_required` continue to execute unchanged. `artifact_assertions` is optional and additive.

## Contract shape

Add `artifact_assertions` to one behavioral test case:

```yaml
artifact_assertions:
  root: fixtures/repository-native/compliant
  files_must_exist:
    - components/button.tsx
  files_must_not_exist:
    - components/local-dialog.tsx
  path_globs_must_match:
    - components/**/*.tsx
  file_patterns_must_contain:
    - path: components/button.tsx
      pattern: '@/lib/utils'
  file_patterns_must_not_contain:
    - path: app/page.tsx
      pattern: another-component-library
```

All paths are relative. Absolute paths and `..` path traversal are rejected during contract validation.

When `--artifact-root` is provided, each case `root` resolves beneath that directory. Otherwise it resolves beneath the parent of `SKILL_EVAL_TESTS_DIR`. This allows adapter repositories to keep test contracts and fixtures together without embedding their stack policy in core.

## Result semantics

Artifact assertions extend the existing classifications:

```text
APPLIED
  output assertions and artifact assertions pass

PARTIAL
  required output or artifact content is missing while evidence exists

GHOST
  forbidden output, file, import, token, path, or other prohibited artifact is present

INCOMPLETE
  required artifact root/file or explicitly requested validator evidence is unavailable
```

A textually compliant response cannot upgrade a violating artifact. Missing artifact evidence is not treated as a pass.

## Fixture-local command evidence

Command execution is disabled by default. A test may declare:

```yaml
command_evidence:
  - argv: [validators/check-conformance]
    cwd: .
    expected_exit: 0
    timeout_seconds: 10
```

The executable must be a relative, executable file inside the artifact root. Shell commands, absolute executables, path traversal, and timeouts above 30 seconds are rejected. Execution additionally requires `--allow-artifact-commands`.

This mechanism is for deterministic fixture-local validators. It is not a general shell runner or security sandbox. Prefer file/path/content assertions whenever they are sufficient.

## Commands

```bash
python3 scripts/run-eval.py --all --validate-tests

python3 scripts/run-eval.py \
  --skill implementation-context-discovery \
  --case repository-artifact-conformance \
  --output-file /tmp/output.txt \
  --artifact-root contracts
```

Use `--report-json` to retain attributable per-assertion evidence.

## Ownership boundary

Core owns generic assertion semantics, bounded path validation, classifications, and the canonical runner. Executable skill repositories own stack-specific fixtures, expected imports, canonical component choices, prohibited parallel systems, and product-independent behavioral methodology. Product repositories own their actual stack contract and acceptance evidence.
