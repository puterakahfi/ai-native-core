#!/usr/bin/env python3
"""
Validate that adapter skills conform to their declared core contracts.

Checks:
  1. quality_gates: adapter SKILL.md must reference each gate from the contract
  2. outputs: adapter must cover the contract's allowed outputs
  3. inputs: adapter must declare handling of required inputs
  4. boundary declarations: adapter must explicitly declare covered and delegated
     contract boundary items; explicit out-of-bound claims fail validation

Boundary validation is declaration-based. It does not infer executable behavior from
keyword overlap in prose. Missing structured boundary declarations are reported as
NOT_CHECKABLE rather than treated as conformant.

Usage:
  python validate-conformance.py [path-to-core] [path-to-skills-repo]

Exit code 0 = no critical errors, 1 = conformance errors found.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

BOUNDARY_COVERS_KEY = "ai-native-skills.boundary.covers"
BOUNDARY_DELEGATES_KEY = "ai-native-skills.boundary.delegates"
BOUNDARY_MAPPING_KEY = "ai-native-skills.boundary"


def find_paths():
    """Auto-detect core and skills repo paths."""
    script_dir = Path(__file__).parent
    core_candidates = [
        script_dir.parent,
        script_dir.parent.parent / "ai-native-core",
        script_dir.parent.parent / "native-ai-engineering" / "ai-native-core",
    ]
    skills_candidates = [
        script_dir.parent.parent / "ai-native-skills",
        script_dir.parent.parent / "native-ai-engineering" / "ai-native-skills",
    ]
    core = skills = None
    for candidate in core_candidates:
        if (candidate / "contracts" / "manifest.yaml").exists():
            core = candidate
            break
    for candidate in skills_candidates:
        if (candidate / "skills").is_dir():
            skills = candidate
            break
    return core, skills


def parse_contract(path: Path) -> Optional[Dict[str, Any]]:
    """Parse a contract YAML and extract checkable fields."""
    try:
        with path.open(encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        skill_contract = data.get("skill_contract", data)
        return {
            "id": skill_contract.get("id", ""),
            "version": skill_contract.get("version", "0.0.0"),
            "quality_gates": skill_contract.get("quality_gates", []) or [],
            "outputs": skill_contract.get("outputs", {}),
            "inputs": skill_contract.get("inputs", {}),
            "boundary": skill_contract.get("boundary", {}),
        }
    except Exception as exc:
        print("  WARN: failed to parse {}: {}".format(path, exc))
        return None


def parse_skill_md(path: Path) -> Dict[str, Any]:
    """Extract frontmatter and body from SKILL.md."""
    with path.open(encoding="utf-8") as handle:
        content = handle.read()

    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    frontmatter = {}
    if frontmatter_match:
        try:
            frontmatter = yaml.safe_load(frontmatter_match.group(1)) or {}
        except yaml.YAMLError:
            pass

    body = content[frontmatter_match.end() :] if frontmatter_match else content
    return {
        "frontmatter": frontmatter,
        "body": body,
        "body_lower": body.lower(),
        "content_lower": content.lower(),
    }


def _normalize_boundary_item(value: str) -> str:
    """Normalize an explicit boundary identifier without fuzzy semantic matching."""
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower())
    return re.sub(r"_+", "_", normalized).strip("_")


def _string_list(raw: Any, label: str) -> Tuple[Optional[List[str]], List[str]]:
    """Parse a structured boundary list and return values plus declaration errors."""
    if raw is None:
        return None, []

    value = raw
    if isinstance(raw, str):
        stripped = raw.strip()
        if not stripped:
            return [], []
        try:
            value = json.loads(stripped)
        except json.JSONDecodeError:
            try:
                value = yaml.safe_load(stripped)
            except yaml.YAMLError:
                value = stripped

    if isinstance(value, str):
        value = [value]

    if not isinstance(value, list):
        return [], ["{} must be a list or a serialized list".format(label)]

    result = []
    errors = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append("{}[{}] must be a non-empty string".format(label, index))
            continue
        result.append(item.strip())
    return result, errors


def _boundary_metadata(skill: Dict[str, Any]) -> Tuple[Any, Any]:
    metadata = skill.get("frontmatter", {}).get("metadata", {}) or {}
    if not isinstance(metadata, dict):
        return None, None

    covers = metadata.get(BOUNDARY_COVERS_KEY)
    delegates = metadata.get(BOUNDARY_DELEGATES_KEY)
    nested = metadata.get(BOUNDARY_MAPPING_KEY)
    if isinstance(nested, dict):
        if covers is None:
            covers = nested.get("covers")
        if delegates is None:
            delegates = nested.get("delegates")
    return covers, delegates


def _boundary_violation(
    severity: str, message: str, missing: Optional[List[str]] = None
) -> Dict[str, Any]:
    return {
        "type": "boundary",
        "severity": severity,
        "message": message,
        "missing": missing or [],
    }


def check_boundary(
    contract: Dict[str, Any], skill: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Validate explicit adapter boundary declarations against the contract boundary."""
    boundary = contract.get("boundary", {})
    if not isinstance(boundary, dict):
        return []

    raw_contract_covers = boundary.get("covers", []) or []
    raw_contract_delegates = boundary.get("does_not_cover", []) or []
    contract_covers = [item for item in raw_contract_covers if isinstance(item, str)]
    contract_delegates = [item for item in raw_contract_delegates if isinstance(item, str)]

    invalid_contract_items = [
        "covers[{}]".format(index)
        for index, item in enumerate(raw_contract_covers)
        if not isinstance(item, str)
    ] + [
        "does_not_cover[{}]".format(index)
        for index, item in enumerate(raw_contract_delegates)
        if not isinstance(item, str)
    ]
    if invalid_contract_items:
        return [
            _boundary_violation(
                "NOT_CHECKABLE",
                "contract boundary contains non-string items",
                invalid_contract_items,
            )
        ]

    if not contract_covers and not contract_delegates:
        return []

    raw_covers, raw_delegates = _boundary_metadata(skill)
    if raw_covers is None and raw_delegates is None:
        required = []
        if contract_covers:
            required.append(BOUNDARY_COVERS_KEY)
        if contract_delegates:
            required.append(BOUNDARY_DELEGATES_KEY)
        return [
            _boundary_violation(
                "NOT_CHECKABLE",
                "structured adapter boundary declarations are absent",
                required,
            )
        ]

    declared_covers, covers_errors = _string_list(raw_covers, BOUNDARY_COVERS_KEY)
    declared_delegates, delegates_errors = _string_list(
        raw_delegates, BOUNDARY_DELEGATES_KEY
    )

    violations = []
    declaration_errors = covers_errors + delegates_errors
    if declaration_errors:
        violations.append(
            _boundary_violation(
                "WARN", "boundary declarations are malformed", declaration_errors
            )
        )

    if declared_covers is None and contract_covers:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter cover declarations are missing",
                [BOUNDARY_COVERS_KEY],
            )
        )
        declared_covers = []
    if declared_delegates is None and contract_delegates:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter delegation declarations are missing",
                [BOUNDARY_DELEGATES_KEY],
            )
        )
        declared_delegates = []

    declared_covers = declared_covers or []
    declared_delegates = declared_delegates or []

    contract_cover_map = {
        _normalize_boundary_item(item): item for item in contract_covers
    }
    contract_delegate_map = {
        _normalize_boundary_item(item): item for item in contract_delegates
    }
    declared_cover_map = {
        _normalize_boundary_item(item): item for item in declared_covers
    }
    declared_delegate_map = {
        _normalize_boundary_item(item): item for item in declared_delegates
    }

    empty_declared_items = [
        item
        for item in declared_covers + declared_delegates
        if not _normalize_boundary_item(item)
    ]
    if empty_declared_items:
        violations.append(
            _boundary_violation(
                "WARN",
                "boundary declarations normalize to empty identifiers",
                empty_declared_items,
            )
        )

    overlap = sorted(set(declared_cover_map) & set(declared_delegate_map))
    if overlap:
        violations.append(
            _boundary_violation(
                "ERROR",
                "adapter declares the same responsibility as both covered and delegated",
                [declared_cover_map[item] for item in overlap],
            )
        )

    out_of_bound = sorted(set(declared_cover_map) & set(contract_delegate_map))
    if out_of_bound:
        violations.append(
            _boundary_violation(
                "ERROR",
                "adapter explicitly claims responsibility delegated by the contract",
                [contract_delegate_map[item] for item in out_of_bound],
            )
        )

    unknown_covers = sorted(
        set(declared_cover_map) - set(contract_cover_map) - set(contract_delegate_map)
    )
    if unknown_covers:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter cover declarations are not defined by the contract boundary",
                [declared_cover_map[item] for item in unknown_covers],
            )
        )

    unknown_delegates = sorted(
        set(declared_delegate_map) - set(contract_delegate_map) - set(contract_cover_map)
    )
    if unknown_delegates:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter delegation declarations are not defined by the contract boundary",
                [declared_delegate_map[item] for item in unknown_delegates],
            )
        )

    delegated_contract_covers = sorted(
        set(declared_delegate_map) & set(contract_cover_map)
    )
    if delegated_contract_covers:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter delegates responsibilities that the contract assigns to it",
                [contract_cover_map[item] for item in delegated_contract_covers],
            )
        )

    missing_covers = sorted(set(contract_cover_map) - set(declared_cover_map))
    if missing_covers:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter does not declare all contract-owned responsibilities",
                [contract_cover_map[item] for item in missing_covers],
            )
        )

    missing_delegates = sorted(set(contract_delegate_map) - set(declared_delegate_map))
    if missing_delegates:
        violations.append(
            _boundary_violation(
                "WARN",
                "adapter does not explicitly preserve all contract delegations",
                [contract_delegate_map[item] for item in missing_delegates],
            )
        )

    return violations


def check_conformance(
    contract: Dict[str, Any], skill: Dict[str, Any], skill_path: str
) -> List[Dict[str, Any]]:
    """Check whether a skill declaration conforms to a contract."""
    del skill_path
    violations = []
    content = skill["content_lower"]

    gates = contract["quality_gates"]
    if gates:
        missing_gates = []
        for gate in gates:
            gate_variants = [
                gate.lower(),
                gate.lower().replace("_", " "),
                gate.lower().replace("_", "-"),
            ]
            gate_words = [word for word in gate.lower().split("_") if len(word) > 3]

            found = any(variant in content for variant in gate_variants)
            if not found and gate_words:
                word_hits = sum(1 for word in gate_words if word in content)
                if word_hits >= max(1, len(gate_words) * 0.6):
                    found = True

            if not found:
                missing_gates.append(gate)

        if missing_gates:
            total = len(gates)
            covered = total - len(missing_gates)
            percentage = (covered / total) * 100
            violations.append(
                {
                    "type": "quality_gates",
                    "severity": "ERROR" if percentage < 50 else "WARN",
                    "message": "quality_gates coverage: {}/{} ({:.0f}%)".format(
                        covered, total, percentage
                    ),
                    "missing": missing_gates[:5],
                }
            )

    outputs = contract["outputs"]
    if isinstance(outputs, dict):
        allowed = outputs.get("allowed", []) or []
        if allowed:
            missing_outputs = []
            for output in allowed:
                output_variants = [
                    output.lower(),
                    output.lower().replace("_", " "),
                    output.lower().replace("_", "-"),
                ]
                if not any(variant in content for variant in output_variants):
                    missing_outputs.append(output)

            if missing_outputs:
                total = len(allowed)
                covered = total - len(missing_outputs)
                percentage = (covered / total) * 100
                if percentage < 50:
                    violations.append(
                        {
                            "type": "outputs",
                            "severity": "WARN",
                            "message": "outputs coverage: {}/{} ({:.0f}%)".format(
                                covered, total, percentage
                            ),
                            "missing": missing_outputs[:5],
                        }
                    )

    inputs = contract["inputs"]
    if isinstance(inputs, dict):
        required = inputs.get("required", []) or []
        if required:
            missing_inputs = []
            for required_input in required:
                input_variants = [
                    required_input.lower(),
                    required_input.lower().replace("_", " "),
                    required_input.lower().replace("_", "-"),
                ]
                if not any(variant in content for variant in input_variants):
                    missing_inputs.append(required_input)

            if missing_inputs:
                total = len(required)
                covered = total - len(missing_inputs)
                percentage = (covered / total) * 100
                if percentage < 50:
                    violations.append(
                        {
                            "type": "inputs",
                            "severity": "WARN",
                            "message": "required inputs coverage: {}/{} ({:.0f}%)".format(
                                covered, total, percentage
                            ),
                            "missing": missing_inputs[:5],
                        }
                    )

    violations.extend(check_boundary(contract, skill))
    return violations


def main():
    core_path = skills_path = None

    if len(sys.argv) >= 3:
        core_path = Path(sys.argv[1])
        skills_path = Path(sys.argv[2])
    elif len(sys.argv) == 2:
        core_path = Path(sys.argv[1])

    if not core_path or not skills_path:
        auto_core, auto_skills = find_paths()
        core_path = core_path or auto_core
        skills_path = skills_path or auto_skills

    if not core_path or not (core_path / "contracts").exists():
        print("ERROR: Cannot find ai-native-core")
        sys.exit(1)
    if not skills_path or not (skills_path / "skills").exists():
        print("ERROR: Cannot find ai-native-skills")
        sys.exit(1)

    print("Core:   {}".format(core_path))
    print("Skills: {}".format(skills_path))
    print()

    errors = 0
    warnings = 0
    not_checkable = 0
    checked = 0
    conformant = 0

    for skill_md in sorted(skills_path.rglob("SKILL.md")):
        if ".git" in str(skill_md):
            continue

        skill = parse_skill_md(skill_md)
        metadata = skill["frontmatter"].get("metadata", {})
        impl = (
            metadata.get("ai-native-skills.implements", "")
            if isinstance(metadata, dict)
            else ""
        )
        if not impl or "ai-native-core/" not in impl:
            continue

        contract_rel = impl.replace("ai-native-core/", "")
        contract_path = core_path / contract_rel
        if not contract_path.exists():
            continue

        contract = parse_contract(contract_path)
        if not contract:
            continue

        checked += 1
        rel_skill = skill_md.relative_to(skills_path)
        violations = check_conformance(contract, skill, str(rel_skill))

        if not violations:
            conformant += 1
            continue

        for violation in violations:
            severity = violation["severity"]
            if severity == "ERROR":
                errors += 1
                icon = "✗"
            elif severity == "WARN":
                warnings += 1
                icon = "⚠"
            elif severity == "NOT_CHECKABLE":
                not_checkable += 1
                icon = "?"
            else:
                warnings += 1
                icon = "⚠"
                severity = "WARN"
            print("{} {}".format(icon, rel_skill))
            print(
                "  {} [{}]: {}".format(
                    violation["type"], severity, violation["message"]
                )
            )
            for missing in violation.get("missing", []):
                print("    - {}".format(missing))
            print()

    print("────────────────────────────────────")
    print("Checked:       {} adapter skills".format(checked))
    print("Conformant:    {}".format(conformant))
    print("Warnings:      {}".format(warnings))
    print("Not checkable: {}".format(not_checkable))
    print("Errors:        {}".format(errors))
    print()

    if errors > 0:
        print("FAIL — {} conformance error(s).".format(errors))
        sys.exit(1)
    if warnings > 0 or not_checkable > 0:
        print(
            "PASS — no critical conformance errors "
            "({} warning(s), {} not-checkable boundary result(s)).".format(
                warnings, not_checkable
            )
        )
        sys.exit(0)

    print("PASS — all checked adapter declarations satisfy the checkable contract fields.")
    sys.exit(0)


if __name__ == "__main__":
    main()
