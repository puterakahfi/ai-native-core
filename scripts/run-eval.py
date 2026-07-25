#!/usr/bin/env python3
"""Canonical skill-eval entry point with optional artifact-aware assertions."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

import artifact_eval
import run_eval_legacy as legacy


def extract_artifact_options(argv: list[str]) -> tuple[Path | None, bool, list[str]]:
    artifact_root: Path | None = None
    allow_commands = False
    remaining = [argv[0]]
    index = 1
    while index < len(argv):
        arg = argv[index]
        if arg == "--allow-artifact-commands":
            allow_commands = True
            index += 1
            continue
        if arg == "--artifact-root":
            if index + 1 >= len(argv):
                raise ValueError("--artifact-root requires a path")
            artifact_root = Path(argv[index + 1])
            index += 2
            continue
        if arg.startswith("--artifact-root="):
            artifact_root = Path(arg.split("=", 1)[1])
            index += 1
            continue
        remaining.append(arg)
        index += 1
    return artifact_root, allow_commands, remaining


def main() -> None:
    artifact_root, allow_commands, remaining = extract_artifact_options(sys.argv)
    sys.argv[:] = remaining
    artifact_eval.install(
        legacy,
        artifact_base=artifact_root or legacy.TESTS_DIR.parent,
        allow_commands=allow_commands,
    )
    legacy.main()


if __name__ == "__main__":
    try:
        main()
    except (
        artifact_eval.ArtifactContractError,
        legacy.EvalContractError,
        FileNotFoundError,
        ValueError,
        yaml.YAMLError,
        subprocess.TimeoutExpired,
    ) as error:
        print(f"skill-eval error: {error}", file=sys.stderr)
        raise SystemExit(2) from error
