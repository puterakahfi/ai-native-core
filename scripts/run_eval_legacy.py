#!/usr/bin/env python3
"""
Skill-eval runner — validates skill test contracts and checks whether agent output
satisfies each case.

Examples:
  # Legacy single-output mode (same output evaluated against all cases)
  python scripts/run-eval.py --skill role-switcher --output-file /tmp/output.txt

  # Recommended per-case mode
  python scripts/run-eval.py --skill role-switcher --output-dir /tmp/eval-outputs
  python scripts/run-eval.py --all --output-dir /tmp/eval-outputs

  # Contract validation only; no model output required
  python scripts/run-eval.py --all --validate-tests

Per-case output layout:
  <output-dir>/<skill>/<case-id>.txt

Also accepted for a single skill:
  <output-dir>/<case-id>.txt
  <output-dir>/<skill>--<case-id>.txt
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

TESTS_DIR = Path(
    os.environ.get(
        "SKILL_EVAL_TESTS_DIR",
        Path(__file__).parent.parent / "contracts" / "tests",
    )
)

VALID_CLASSIFICATIONS = {"APPLIED", "PARTIAL", "GHOST", "INCOMPLETE"}


class EvalContractError(ValueError):
    """Raised when a skill eval contract is malformed."""


def load_test(skill_name: str) -> dict[str, Any]:
    path = TESTS_DIR / f"{skill_name}.test.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No test file found: {path}")

    with path.open(encoding="utf-8") as handle:
        document = yaml.safe_load(handle)

    validate_test_document(document, path=path, expected_skill=skill_name)
    return document


def discover_skill_names() -> list[str]:
    if not TESTS_DIR.exists():
        raise FileNotFoundError(f"Skill eval tests directory does not exist: {TESTS_DIR}")

    return sorted(path.name.removesuffix(".test.yaml") for path in TESTS_DIR.glob("*.test.yaml"))


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvalContractError(f"{label} must be a non-empty string")
    return value


def _validate_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise EvalContractError(f"{label} must be a list")

    result: list[str] = []
    for index, item in enumerate(value):
        result.append(_require_string(item, f"{label}[{index}]"))
    return result


def validate_test_document(
    document: Any,
    *,
    path: Path,
    expected_skill: str | None = None,
) -> None:
    if not isinstance(document, dict):
        raise EvalContractError(f"{path}: root must be a mapping")

    skill_test = document.get("skill_test")
    if not isinstance(skill_test, dict):
        raise EvalContractError(f"{path}: missing skill_test mapping")

    skill_name = _require_string(skill_test.get("skill"), f"{path}: skill_test.skill")
    if expected_skill and skill_name != expected_skill:
        raise EvalContractError(
            f"{path}: skill_test.skill '{skill_name}' does not match filename '{expected_skill}'"
        )

    _require_string(skill_test.get("version"), f"{path}: skill_test.version")

    cases = skill_test.get("cases")
    if not isinstance(cases, list) or not cases:
        raise EvalContractError(f"{path}: skill_test.cases must be a non-empty list")

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        label = f"{path}: cases[{index}]"
        if not isinstance(case, dict):
            raise EvalContractError(f"{label} must be a mapping")

        case_id = _require_string(case.get("id"), f"{label}.id")
        if case_id in seen_ids:
            raise EvalContractError(f"{path}: duplicate case id '{case_id}'")
        seen_ids.add(case_id)

        _require_string(case.get("trigger"), f"{label}.trigger")

        must_contain = _validate_string_list(case.get("must_contain"), f"{label}.must_contain")
        must_not_contain = _validate_string_list(
            case.get("must_not_contain"), f"{label}.must_not_contain"
        )
        one_of = _validate_string_list(
            case.get("must_contain_one_of"), f"{label}.must_contain_one_of"
        )

        sequence_required = case.get("sequence_required", [])
        if not isinstance(sequence_required, list):
            raise EvalContractError(f"{label}.sequence_required must be a list")
        for sequence_index, sequence in enumerate(sequence_required):
            sequence_label = f"{label}.sequence_required[{sequence_index}]"
            if not isinstance(sequence, dict):
                raise EvalContractError(f"{sequence_label} must be a mapping")
            _require_string(sequence.get("pattern"), f"{sequence_label}.pattern")
            _require_string(
                sequence.get("must_come_before"),
                f"{sequence_label}.must_come_before",
            )

        if not must_contain and not must_not_contain and not one_of and not sequence_required:
            raise EvalContractError(f"{label} must define at least one assertion")

        positive = {item.casefold() for item in must_contain}
        negative = {item.casefold() for item in must_not_contain}
        contradictions = sorted(positive & negative)
        if contradictions:
            raise EvalContractError(
                f"{label} contains contradictory positive/negative patterns: {contradictions}"
            )


def run_case(case: dict[str, Any], output: str) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": case["id"],
        "description": case.get("description", ""),
        "must_contain": [],
        "must_contain_one_of": [],
        "must_not_contain": [],
        "sequence_required": [],
        "classification": "APPLIED",
        "verdict": "APPLIED",
        "failures": [],
    }

    output_folded = output.casefold()

    for pattern in case.get("must_contain", []):
        found = pattern.casefold() in output_folded
        result["must_contain"].append({"pattern": pattern, "found": found})
        if not found:
            result["failures"].append(f"MISSING must_contain: '{pattern}'")

    one_of = case.get("must_contain_one_of", [])
    if one_of:
        found_patterns = [pattern for pattern in one_of if pattern.casefold() in output_folded]
        found_any = bool(found_patterns)
        result["must_contain_one_of"].append(
            {
                "patterns": one_of,
                "found": found_any,
                "matched": found_patterns,
            }
        )
        if not found_any:
            result["failures"].append(f"MISSING must_contain_one_of: {one_of}")

    forbidden_hit = False
    for pattern in case.get("must_not_contain", []):
        found = pattern.casefold() in output_folded
        result["must_not_contain"].append({"pattern": pattern, "found": found})
        if found:
            result["failures"].append(f"FOUND must_not_contain: '{pattern}'")
            forbidden_hit = True

    for sequence in case.get("sequence_required", []):
        before_pattern = sequence["pattern"]
        after_patterns = sequence["must_come_before"].split("|")
        before_position = output_folded.find(before_pattern.casefold())
        existing_after_positions = [
            output_folded.find(pattern.casefold())
            for pattern in after_patterns
            if output_folded.find(pattern.casefold()) >= 0
        ]
        after_position = min(existing_after_positions, default=-1)
        ok = before_position >= 0 and (after_position < 0 or before_position < after_position)
        result["sequence_required"].append(
            {
                "pattern": before_pattern,
                "must_come_before": sequence["must_come_before"],
                "ok": ok,
            }
        )
        if not ok:
            result["failures"].append(
                f"SEQUENCE VIOLATION: '{before_pattern}' must come before "
                f"'{sequence['must_come_before']}'"
            )

    if forbidden_hit:
        classification = "GHOST"
    elif result["failures"]:
        classification = "PARTIAL"
    else:
        classification = "APPLIED"

    result["classification"] = classification
    result["verdict"] = classification
    return result


def missing_output_result(case: dict[str, Any], expected_paths: list[Path]) -> dict[str, Any]:
    return {
        "id": case["id"],
        "description": case.get("description", ""),
        "classification": "INCOMPLETE",
        "verdict": "INCOMPLETE",
        "failures": [
            "MISSING OUTPUT: expected one of " + ", ".join(str(path) for path in expected_paths)
        ],
        "must_contain": [],
        "must_contain_one_of": [],
        "must_not_contain": [],
        "sequence_required": [],
    }


def candidate_output_paths(output_dir: Path, skill_name: str, case_id: str) -> list[Path]:
    return [
        output_dir / skill_name / f"{case_id}.txt",
        output_dir / f"{skill_name}--{case_id}.txt",
        output_dir / f"{case_id}.txt",
    ]


def read_case_output(output_dir: Path, skill_name: str, case_id: str) -> tuple[str | None, list[Path]]:
    candidates = candidate_output_paths(output_dir, skill_name, case_id)
    for path in candidates:
        if path.is_file():
            return path.read_text(encoding="utf-8"), candidates
    return None, candidates


def summarize_results(results: list[dict[str, Any]]) -> tuple[str, dict[str, int]]:
    counts = {
        "applied": sum(result["classification"] == "APPLIED" for result in results),
        "partial": sum(result["classification"] == "PARTIAL" for result in results),
        "ghost": sum(result["classification"] == "GHOST" for result in results),
        "incomplete": sum(result["classification"] == "INCOMPLETE" for result in results),
        "total": len(results),
    }

    if counts["incomplete"]:
        overall = "INCOMPLETE"
    elif counts["ghost"]:
        overall = "GHOST"
    elif counts["partial"]:
        overall = "PARTIAL"
    else:
        overall = "APPLIED"

    return overall, counts


def run_skill_eval(
    skill_name: str,
    *,
    output: str | None = None,
    output_dir: Path | None = None,
    case_id: str | None = None,
) -> dict[str, Any]:
    test = load_test(skill_name)
    cases: list[dict[str, Any]] = test["skill_test"]["cases"]

    if case_id:
        cases = [case for case in cases if case["id"] == case_id]
        if not cases:
            raise EvalContractError(f"No case '{case_id}' found for skill '{skill_name}'")

    results: list[dict[str, Any]] = []
    for case in cases:
        if output_dir is not None:
            case_output, expected_paths = read_case_output(output_dir, skill_name, case["id"])
            if case_output is None:
                results.append(missing_output_result(case, expected_paths))
            else:
                results.append(run_case(case, case_output))
        elif output is not None:
            results.append(run_case(case, output))
        else:
            raise ValueError("Either output or output_dir is required for behavioral evaluation")

    overall, summary = summarize_results(results)
    return {
        "skill": skill_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall": overall,
        "summary": summary,
        "cases": results,
    }


def aggregate_reports(reports: list[dict[str, Any]]) -> dict[str, Any]:
    classifications = [report["overall"] for report in reports]
    if "INCOMPLETE" in classifications:
        overall = "INCOMPLETE"
    elif "GHOST" in classifications:
        overall = "GHOST"
    elif "PARTIAL" in classifications:
        overall = "PARTIAL"
    else:
        overall = "APPLIED"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall": overall,
        "skills": reports,
        "summary": {
            "applied": sum(item == "APPLIED" for item in classifications),
            "partial": sum(item == "PARTIAL" for item in classifications),
            "ghost": sum(item == "GHOST" for item in classifications),
            "incomplete": sum(item == "INCOMPLETE" for item in classifications),
            "total": len(classifications),
        },
    }


def print_skill_report(report: dict[str, Any]) -> None:
    icons = {"APPLIED": "✓", "PARTIAL": "~", "GHOST": "✗", "INCOMPLETE": "!"}
    overall = report["overall"]
    summary = report["summary"]

    print(f"\n{'=' * 72}")
    print(f"SKILL EVAL — {report['skill']}")
    print(
        f"Overall: [{icons.get(overall, '?')}] {overall}  "
        f"({summary['applied']}/{summary['total']} cases APPLIED)"
    )
    print("=" * 72)

    for case in report["cases"]:
        classification = case["classification"]
        print(
            f"\n  [{icons.get(classification, '?')}] "
            f"{case['id']} — {case.get('description', '')}"
        )
        for failure in case.get("failures", []):
            print(f"       ↳ {failure}")


def print_aggregate_report(report: dict[str, Any]) -> None:
    for skill_report in report["skills"]:
        print_skill_report(skill_report)

    summary = report["summary"]
    print(f"\n{'=' * 72}")
    print("ALL SKILL EVALS")
    print(
        f"Overall: {report['overall']} — "
        f"{summary['applied']}/{summary['total']} skills APPLIED"
    )
    print("=" * 72)


def validate_selected_tests(skill_name: str | None, all_skills: bool) -> list[str]:
    skill_names = discover_skill_names() if all_skills or not skill_name else [skill_name]
    for name in skill_names:
        load_test(name)
    return skill_names


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="skill-eval runner")
    target = parser.add_mutually_exclusive_group(required=False)
    target.add_argument("--skill", help="Skill name to evaluate")
    target.add_argument("--all", action="store_true", help="Evaluate all discovered skill tests")

    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--output", help="Agent output text (legacy single-output mode)")
    source.add_argument("--output-file", help="Path to one agent output file")
    source.add_argument(
        "--output-dir",
        help="Directory containing per-case outputs: <skill>/<case-id>.txt",
    )

    parser.add_argument("--case", help="Evaluate one case; requires --skill")
    parser.add_argument(
        "--validate-tests",
        action="store_true",
        help="Validate test contracts only; no outputs required",
    )
    parser.add_argument("--report-json", help="Save JSON report to this path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.case and not args.skill:
        raise SystemExit("--case requires --skill")

    if args.validate_tests:
        skill_names = validate_selected_tests(args.skill, args.all)
        print(f"Validated {len(skill_names)} skill eval contract(s) in {TESTS_DIR}")
        raise SystemExit(0)

    if not args.skill and not args.all:
        raise SystemExit("Behavioral evaluation requires --skill or --all")

    if args.all and not args.output_dir:
        raise SystemExit("--all requires --output-dir so each case can use its own output")

    output: str | None = None
    if args.output_file:
        output = Path(args.output_file).read_text(encoding="utf-8")
    elif args.output is not None:
        output = args.output
    elif not args.output_dir:
        print("Reading agent output from stdin (Ctrl+D to finish)...")
        output = sys.stdin.read()

    output_dir = Path(args.output_dir) if args.output_dir else None

    if args.all:
        reports = [
            run_skill_eval(skill_name, output_dir=output_dir)
            for skill_name in discover_skill_names()
        ]
        report: dict[str, Any] = aggregate_reports(reports)
        print_aggregate_report(report)
    else:
        report = run_skill_eval(
            args.skill,
            output=output,
            output_dir=output_dir,
            case_id=args.case,
        )
        print_skill_report(report)

    if args.report_json:
        report_path = Path(args.report_json)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"\nReport saved: {report_path}")

    overall = report["overall"]
    if overall not in VALID_CLASSIFICATIONS:
        raise SystemExit(f"Unknown eval classification: {overall}")
    raise SystemExit(0 if overall == "APPLIED" else 1)


if __name__ == "__main__":
    try:
        main()
    except (EvalContractError, FileNotFoundError, ValueError, yaml.YAMLError) as error:
        print(f"skill-eval error: {error}", file=sys.stderr)
        raise SystemExit(2) from error
