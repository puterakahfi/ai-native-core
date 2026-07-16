#!/usr/bin/env python3
"""
skill-eval runner — checks if agent output satisfies skill test cases
Usage:
  python run-eval.py --skill role-switcher --output "agent output text here"
  python run-eval.py --skill role-switcher --output-file /tmp/agent_output.txt
  python run-eval.py --all --output-dir /tmp/eval-outputs/
"""

import argparse
import json
import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path

TESTS_DIR = Path(__file__).parent.parent / "contracts" / "tests"


def load_test(skill_name: str) -> dict:
    path = TESTS_DIR / f"{skill_name}.test.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No test file found: {path}")
    with open(path) as f:
        return yaml.safe_load(f)


def run_case(case: dict, output: str) -> dict:
    result = {
        "id": case["id"],
        "description": case.get("description", ""),
        "must_contain": [],
        "must_not_contain": [],
        "sequence_required": [],
        "verdict": "APPLIED",
        "classification": "APPLIED",
        "failures": [],
    }

    # must_contain checks
    for pattern in case.get("must_contain", []):
        found = pattern.lower() in output.lower()
        result["must_contain"].append({"pattern": pattern, "found": found})
        if not found:
            result["failures"].append(f"MISSING must_contain: '{pattern}'")

    # must_contain_one_of checks
    one_of = case.get("must_contain_one_of", [])
    if one_of:
        found_any = any(p.lower() in output.lower() for p in one_of)
        if not found_any:
            result["failures"].append(f"MISSING must_contain_one_of: {one_of}")

    # must_not_contain checks
    generic_hit = False
    for pattern in case.get("must_not_contain", []):
        found = pattern.lower() in output.lower()
        result["must_not_contain"].append({"pattern": pattern, "found": found})
        if found:
            result["failures"].append(f"FOUND must_not_contain: '{pattern}'")
            generic_hit = True

    # sequence checks
    for seq in case.get("sequence_required", []):
        before_pattern = seq["pattern"]
        after_patterns = seq["must_come_before"].split("|")
        before_pos = output.lower().find(before_pattern.lower())
        after_pos = min(
            (output.lower().find(p.lower()) for p in after_patterns if output.lower().find(p.lower()) >= 0),
            default=-1
        )
        ok = before_pos >= 0 and (after_pos < 0 or before_pos < after_pos)
        result["sequence_required"].append({
            "pattern": before_pattern,
            "must_come_before": seq["must_come_before"],
            "ok": ok,
        })
        if not ok:
            result["failures"].append(f"SEQUENCE VIOLATION: '{before_pattern}' must come before '{seq['must_come_before']}'")

    # classify
    if generic_hit:
        result["classification"] = "GHOST"
    elif result["failures"]:
        result["classification"] = "PARTIAL"
    else:
        result["classification"] = "APPLIED"

    result["verdict"] = result["classification"]
    return result


def run_skill_eval(skill_name: str, output: str) -> dict:
    test = load_test(skill_name)
    cases = test.get("skill_test", {}).get("cases", [])

    results = []
    for case in cases:
        r = run_case(case, output)
        results.append(r)

    applied = sum(1 for r in results if r["classification"] == "APPLIED")
    partial = sum(1 for r in results if r["classification"] == "PARTIAL")
    ghost = sum(1 for r in results if r["classification"] == "GHOST")

    overall = "APPLIED" if applied == len(results) else ("GHOST" if ghost > 0 else "PARTIAL")

    return {
        "skill": skill_name,
        "timestamp": datetime.utcnow().isoformat(),
        "overall": overall,
        "summary": {"applied": applied, "partial": partial, "ghost": ghost, "total": len(results)},
        "cases": results,
    }


def print_report(report: dict):
    skill = report["skill"]
    overall = report["overall"]
    s = report["summary"]

    icon = {"APPLIED": "✓", "PARTIAL": "~", "GHOST": "✗"}.get(overall, "?")
    print(f"\n{'='*60}")
    print(f"SKILL EVAL — {skill}")
    print(f"Overall: [{icon}] {overall}  ({s['applied']}/{s['total']} cases APPLIED)")
    print(f"{'='*60}")

    for case in report["cases"]:
        c_icon = {"APPLIED": "✓", "PARTIAL": "~", "GHOST": "✗"}.get(case["classification"], "?")
        print(f"\n  [{c_icon}] {case['id']} — {case['description']}")
        for f in case.get("failures", []):
            print(f"       ↳ {f}")


def main():
    parser = argparse.ArgumentParser(description="skill-eval runner")
    parser.add_argument("--skill", help="Skill name to evaluate")
    parser.add_argument("--output", help="Agent output text (inline)")
    parser.add_argument("--output-file", help="Path to file containing agent output")
    parser.add_argument("--report-json", help="Save JSON report to this path")
    args = parser.parse_args()

    if not args.skill:
        parser.print_help()
        sys.exit(1)

    if args.output_file:
        with open(args.output_file) as f:
            output = f.read()
    elif args.output:
        output = args.output
    else:
        print("Reading agent output from stdin (Ctrl+D to finish)...")
        output = sys.stdin.read()

    report = run_skill_eval(args.skill, output)
    print_report(report)

    if args.report_json:
        Path(args.report_json).parent.mkdir(parents=True, exist_ok=True)
        with open(args.report_json, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\nReport saved: {args.report_json}")

    sys.exit(0 if report["overall"] == "APPLIED" else 1)


if __name__ == "__main__":
    main()
