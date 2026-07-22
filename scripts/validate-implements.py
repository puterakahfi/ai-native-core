#!/usr/bin/env python3
"""Validate ai-native-skills implements references against core manifest and aliases."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

from contract_resolution import pin_accepts, resolve_contract_reference

IMPLEMENTS_KEY = "ai-native-skills.implements"
VERSION_KEY = "ai-native-skills.contract-version"


def find_core(explicit: str | None) -> Path | None:
    if explicit:
        candidate = Path(explicit).resolve()
        return candidate if (candidate / "contracts" / "manifest.yaml").is_file() else None

    script_root = Path(__file__).resolve().parents[1]
    candidates = [
        script_root,
        script_root.parent / "ai-native-core",
        script_root / "core",
        script_root.parent / "native-ai-engineering" / "ai-native-core",
    ]
    for candidate in candidates:
        if (candidate / "contracts" / "manifest.yaml").is_file():
            return candidate.resolve()
    return None


def parse_frontmatter(path: Path) -> dict[str, Any]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    payload = yaml.safe_load(match.group(1)) or {}
    return payload if isinstance(payload, dict) else {}


def metadata_value(frontmatter: dict[str, Any], key: str) -> str:
    metadata = frontmatter.get("metadata", {}) or {}
    if not isinstance(metadata, dict):
        return ""
    value = metadata.get(key, "")
    return str(value).strip()


def discover_skills(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("SKILL.md")
        if ".git" not in path.parts
    )


def main() -> int:
    core = find_core(sys.argv[1] if len(sys.argv) > 1 else None)
    if not core:
        print("ERROR: Cannot find ai-native-core with contracts/manifest.yaml")
        print("Usage: validate-implements.py [path-to-ai-native-core]")
        return 1

    workspace = Path.cwd()
    errors = 0
    warnings = 0
    aliases = 0
    checked = 0

    print(f"Core: {core}")
    print(f"Skills workspace: {workspace}\n")

    for skill_path in discover_skills(workspace):
        frontmatter = parse_frontmatter(skill_path)
        reference = metadata_value(frontmatter, IMPLEMENTS_KEY)
        if not reference or "ai-native-core/" not in reference:
            continue
        checked += 1

        resolution = resolve_contract_reference(core, reference)
        relative_skill = skill_path.relative_to(workspace)
        if not resolution:
            print(f"BROKEN: {relative_skill}")
            print(f"  → {reference}")
            print("  (not found in manifest, canonical tree, or active path aliases)\n")
            errors += 1
            continue

        alias = resolution.get("alias")
        if alias:
            aliases += 1
            print(f"ALIAS: {relative_skill}")
            print(f"  {resolution['declared_path']} → {resolution['canonical_path']}")

        pinned = metadata_value(frontmatter, VERSION_KEY)
        actual = str(resolution["entry"].get("version", ""))
        if not pinned:
            print(f"WARN: {relative_skill}")
            print("  → no contract-version pinned\n")
            warnings += 1
            continue

        try:
            compatible = pin_accepts(pinned, actual)
        except ValueError as exc:
            print(f"VERSION ERROR: {relative_skill}")
            print(f"  → {reference}")
            print(f"  {exc}\n")
            errors += 1
            continue

        if not compatible:
            print(f"VERSION MISMATCH: {relative_skill}")
            print(f"  → {resolution['canonical_path']}")
            print(f"  pinned: {pinned}, actual: {actual}\n")
            errors += 1

    print("────────────────────────────────────")
    print(f"Checked:  {checked} adapter skills")
    print(f"Aliases:  {aliases}")
    print(f"Warnings: {warnings}")
    print(f"Errors:   {errors}\n")

    if errors:
        print(f"FAIL — {errors} broken or incompatible contract reference(s).")
        return 1
    print("PASS — all contract references resolve canonically and satisfy version pins.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
