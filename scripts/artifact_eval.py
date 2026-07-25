"""Bounded artifact assertions for the canonical skill-eval runner."""
from __future__ import annotations

import fnmatch
import os
import subprocess
from pathlib import Path
from typing import Any, Callable

MAX_COMMAND_TIMEOUT_SECONDS = 30


class ArtifactContractError(ValueError):
    pass


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ArtifactContractError(f"{label} must be a non-empty string")
    return value


def string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ArtifactContractError(f"{label} must be a list")
    return [require_string(item, f"{label}[{index}]") for index, item in enumerate(value)]


def relative_path(value: Any, label: str) -> str:
    text = require_string(value, label)
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        raise ArtifactContractError(f"{label} must be a bounded relative path")
    return text


def file_patterns(value: Any, label: str) -> list[dict[str, str]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ArtifactContractError(f"{label} must be a list")
    result = []
    for index, item in enumerate(value):
        item_label = f"{label}[{index}]"
        if not isinstance(item, dict):
            raise ArtifactContractError(f"{item_label} must be a mapping")
        result.append({
            "path": relative_path(item.get("path"), f"{item_label}.path"),
            "pattern": require_string(item.get("pattern"), f"{item_label}.pattern"),
        })
    return result


def commands(value: Any, label: str) -> list[dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ArtifactContractError(f"{label} must be a list")
    result = []
    for index, item in enumerate(value):
        item_label = f"{label}[{index}]"
        if not isinstance(item, dict):
            raise ArtifactContractError(f"{item_label} must be a mapping")
        argv = item.get("argv")
        if not isinstance(argv, list) or not argv:
            raise ArtifactContractError(f"{item_label}.argv must be a non-empty list")
        argv = [require_string(arg, f"{item_label}.argv[{i}]") for i, arg in enumerate(argv)]
        relative_path(argv[0], f"{item_label}.argv[0]")
        timeout = item.get("timeout_seconds", 10)
        if not isinstance(timeout, int) or not 1 <= timeout <= MAX_COMMAND_TIMEOUT_SECONDS:
            raise ArtifactContractError(
                f"{item_label}.timeout_seconds must be between 1 and {MAX_COMMAND_TIMEOUT_SECONDS}"
            )
        expected_exit = item.get("expected_exit", 0)
        if not isinstance(expected_exit, int):
            raise ArtifactContractError(f"{item_label}.expected_exit must be an integer")
        result.append({
            "argv": argv,
            "cwd": relative_path(item.get("cwd", "."), f"{item_label}.cwd"),
            "timeout_seconds": timeout,
            "expected_exit": expected_exit,
        })
    return result


def validate_assertions(value: Any, label: str) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ArtifactContractError(f"{label} must be a mapping")
    result = {
        "root": relative_path(value.get("root"), f"{label}.root"),
        "files_must_exist": [relative_path(v, f"{label}.files_must_exist[{i}]") for i, v in enumerate(string_list(value.get("files_must_exist"), f"{label}.files_must_exist"))],
        "files_must_not_exist": [relative_path(v, f"{label}.files_must_not_exist[{i}]") for i, v in enumerate(string_list(value.get("files_must_not_exist"), f"{label}.files_must_not_exist"))],
        "path_globs_must_match": string_list(value.get("path_globs_must_match"), f"{label}.path_globs_must_match"),
        "file_patterns_must_contain": file_patterns(value.get("file_patterns_must_contain"), f"{label}.file_patterns_must_contain"),
        "file_patterns_must_not_contain": file_patterns(value.get("file_patterns_must_not_contain"), f"{label}.file_patterns_must_not_contain"),
        "command_evidence": commands(value.get("command_evidence"), f"{label}.command_evidence"),
    }
    if not any(result[key] for key in result if key != "root"):
        raise ArtifactContractError(f"{label} must define at least one artifact assertion")
    return result


def bounded(base: Path, relative: str) -> Path:
    base = base.resolve()
    candidate = (base / relative).resolve()
    if candidate != base and base not in candidate.parents:
        raise ArtifactContractError(f"artifact path escapes root: {relative}")
    return candidate


def execute(assertions: dict[str, Any], base: Path, allow_commands: bool = False) -> dict[str, Any]:
    root = bounded(base, assertions["root"])
    result: dict[str, Any] = {
        "root": str(root), "checks": [], "failures": [],
        "missing_evidence": False, "forbidden_hit": False,
    }
    if not root.is_dir():
        result["missing_evidence"] = True
        result["failures"].append(f"MISSING ARTIFACT ROOT: {root}")
        return result

    def record(kind: str, subject: str, ok: bool, failure: str | None = None) -> None:
        result["checks"].append({"kind": kind, "subject": subject, "ok": ok})
        if failure:
            result["failures"].append(failure)

    for rel in assertions["files_must_exist"]:
        ok = bounded(root, rel).exists()
        record("files_must_exist", rel, ok, None if ok else f"MISSING required artifact: '{rel}'")
        result["missing_evidence"] = result["missing_evidence"] or not ok
    for rel in assertions["files_must_not_exist"]:
        found = bounded(root, rel).exists()
        record("files_must_not_exist", rel, not found, f"FOUND forbidden artifact: '{rel}'" if found else None)
        result["forbidden_hit"] = result["forbidden_hit"] or found

    paths = [str(path.relative_to(root)) for path in root.rglob("*")]
    for pattern in assertions["path_globs_must_match"]:
        matches = sorted(path for path in paths if fnmatch.fnmatch(path, pattern))
        record("path_globs_must_match", pattern, bool(matches), None if matches else f"NO artifact paths matched glob: '{pattern}'")

    for item in assertions["file_patterns_must_contain"]:
        path = bounded(root, item["path"])
        if not path.is_file():
            result["missing_evidence"] = True
            record("file_patterns_must_contain", item["path"], False, f"MISSING artifact file: '{item['path']}'")
            continue
        found = item["pattern"].casefold() in path.read_text(encoding="utf-8").casefold()
        record("file_patterns_must_contain", item["path"], found, None if found else f"MISSING artifact pattern '{item['pattern']}' in '{item['path']}'")

    for item in assertions["file_patterns_must_not_contain"]:
        path = bounded(root, item["path"])
        if not path.is_file():
            result["missing_evidence"] = True
            record("file_patterns_must_not_contain", item["path"], False, f"MISSING artifact file: '{item['path']}'")
            continue
        found = item["pattern"].casefold() in path.read_text(encoding="utf-8").casefold()
        record("file_patterns_must_not_contain", item["path"], not found, f"FOUND forbidden artifact pattern '{item['pattern']}' in '{item['path']}'" if found else None)
        result["forbidden_hit"] = result["forbidden_hit"] or found

    for item in assertions["command_evidence"]:
        if not allow_commands:
            result["missing_evidence"] = True
            record("command_evidence", item["argv"][0], False, "COMMAND EVIDENCE DISABLED: pass --allow-artifact-commands")
            continue
        executable = bounded(root, item["argv"][0])
        cwd = bounded(root, item["cwd"])
        if not executable.is_file() or not os.access(executable, os.X_OK):
            result["missing_evidence"] = True
            record("command_evidence", item["argv"][0], False, f"INVALID fixture-local executable: '{item['argv'][0]}'")
            continue
        completed = subprocess.run(
            [str(executable), *item["argv"][1:]], cwd=cwd,
            capture_output=True, text=True, timeout=item["timeout_seconds"],
            check=False, env={"PATH": os.environ.get("PATH", "")},
        )
        ok = completed.returncode == item["expected_exit"]
        record("command_evidence", item["argv"][0], ok, None if ok else f"COMMAND exit mismatch: expected {item['expected_exit']}, got {completed.returncode}")
    return result


def install(
    legacy: Any,
    artifact_base: Path,
    allow_commands: bool = False,
) -> None:
    original_validate: Callable[..., None] = legacy.validate_test_document
    original_run_case: Callable[..., dict[str, Any]] = legacy.run_case

    def validate(document: Any, *, path: Path, expected_skill: str | None = None) -> None:
        original_validate(document, path=path, expected_skill=expected_skill)
        for index, case in enumerate(document["skill_test"]["cases"]):
            validate_assertions(case.get("artifact_assertions"), f"{path}: cases[{index}].artifact_assertions")

    def run_case(case: dict[str, Any], output: str) -> dict[str, Any]:
        result = original_run_case(case, output)
        assertions = validate_assertions(case.get("artifact_assertions"), f"case[{case['id']}].artifact_assertions")
        result["artifact_assertions"] = None
        if assertions is None:
            return result
        artifact_result = execute(assertions, artifact_base, allow_commands)
        result["artifact_assertions"] = artifact_result
        result["failures"].extend(artifact_result["failures"])
        if artifact_result["missing_evidence"]:
            classification = "INCOMPLETE"
        elif result["classification"] == "GHOST" or artifact_result["forbidden_hit"]:
            classification = "GHOST"
        elif artifact_result["failures"] or result["classification"] == "PARTIAL":
            classification = "PARTIAL"
        else:
            classification = "APPLIED"
        result["classification"] = classification
        result["verdict"] = classification
        return result

    legacy.validate_test_document = validate
    legacy.run_case = run_case
