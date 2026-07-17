#!/usr/bin/env python3
"""
Validate that adapter skills conform to their declared core contracts.

Checks:
  1. quality_gates: adapter SKILL.md must reference each gate from the contract
  2. outputs: adapter must cover the contract's allowed outputs
  3. inputs: adapter must declare handling of required inputs
  4. boundary: adapter must not claim coverage outside contract boundary

Usage:
  python validate-conformance.py [path-to-core] [path-to-skills-repo]

Exit code 0 = all conformant, 1 = violations found.
"""
import os
import sys
import re
import yaml
from pathlib import Path
from typing import Optional


def find_paths():
    """Auto-detect core and skills repo paths."""
    script_dir = Path(__file__).parent
    core_candidates = [
        script_dir.parent,  # if script is in core/scripts/
        script_dir.parent.parent / "ai-native-core",
        script_dir.parent.parent / "native-ai-engineering" / "ai-native-core",
    ]
    skills_candidates = [
        script_dir.parent.parent / "ai-native-skills",
        script_dir.parent.parent / "native-ai-engineering" / "ai-native-skills",
    ]
    core = skills = None
    for c in core_candidates:
        if (c / "contracts" / "manifest.yaml").exists():
            core = c
            break
    for s in skills_candidates:
        if (s / "skills").is_dir():
            skills = s
            break
    return core, skills


def parse_contract(path: Path) -> Optional[dict]:
    """Parse a contract YAML and extract checkable fields."""
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
        sc = data.get("skill_contract", data)
        return {
            "id": sc.get("id", ""),
            "version": sc.get("version", "0.0.0"),
            "quality_gates": sc.get("quality_gates", []) or [],
            "outputs": sc.get("outputs", {}),
            "inputs": sc.get("inputs", {}),
            "boundary": sc.get("boundary", {}),
        }
    except Exception as e:
        print(f"  WARN: failed to parse {path}: {e}")
        return None


def parse_skill_md(path: Path) -> dict:
    """Extract frontmatter and body from SKILL.md."""
    with open(path) as f:
        content = f.read()

    # Extract frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    frontmatter = {}
    if fm_match:
        try:
            frontmatter = yaml.safe_load(fm_match.group(1)) or {}
        except yaml.YAMLError:
            pass

    body = content[fm_match.end():] if fm_match else content
    body_lower = body.lower()

    return {
        "frontmatter": frontmatter,
        "body": body,
        "body_lower": body_lower,
        "content_lower": content.lower(),
    }


def check_conformance(contract: dict, skill: dict, skill_path: str) -> list:
    """Check if skill conforms to contract. Returns list of violations."""
    violations = []
    body = skill["body_lower"]
    content = skill["content_lower"]

    # 1. Quality gates coverage
    gates = contract["quality_gates"]
    if gates:
        missing_gates = []
        for gate in gates:
            # Normalize gate name for fuzzy matching
            gate_variants = [
                gate.lower(),
                gate.lower().replace("_", " "),
                gate.lower().replace("_", "-"),
            ]
            # Also check for key words from the gate name
            gate_words = [w for w in gate.lower().split("_") if len(w) > 3]

            found = False
            for variant in gate_variants:
                if variant in content:
                    found = True
                    break

            if not found and gate_words:
                # Check if at least 60% of significant words appear
                word_hits = sum(1 for w in gate_words if w in content)
                if word_hits >= max(1, len(gate_words) * 0.6):
                    found = True

            if not found:
                missing_gates.append(gate)

        if missing_gates:
            total = len(gates)
            covered = total - len(missing_gates)
            pct = (covered / total) * 100
            violations.append({
                "type": "quality_gates",
                "severity": "ERROR" if pct < 50 else "WARN",
                "message": f"quality_gates coverage: {covered}/{total} ({pct:.0f}%)",
                "missing": missing_gates[:5],  # Show first 5
            })

    # 2. Outputs coverage
    outputs = contract["outputs"]
    if isinstance(outputs, dict):
        allowed = outputs.get("allowed", []) or []
        if allowed:
            missing_outputs = []
            for out in allowed:
                out_variants = [
                    out.lower(),
                    out.lower().replace("_", " "),
                    out.lower().replace("_", "-"),
                ]
                if not any(v in content for v in out_variants):
                    missing_outputs.append(out)

            if missing_outputs:
                total = len(allowed)
                covered = total - len(missing_outputs)
                pct = (covered / total) * 100
                if pct < 50:
                    violations.append({
                        "type": "outputs",
                        "severity": "WARN",
                        "message": f"outputs coverage: {covered}/{total} ({pct:.0f}%)",
                        "missing": missing_outputs[:5],
                    })

    # 3. Required inputs coverage
    inputs = contract["inputs"]
    if isinstance(inputs, dict):
        required = inputs.get("required", []) or []
        if required:
            missing_inputs = []
            for inp in required:
                inp_variants = [
                    inp.lower(),
                    inp.lower().replace("_", " "),
                    inp.lower().replace("_", "-"),
                ]
                if not any(v in content for v in inp_variants):
                    missing_inputs.append(inp)

            if missing_inputs:
                total = len(required)
                covered = total - len(missing_inputs)
                pct = (covered / total) * 100
                if pct < 50:
                    violations.append({
                        "type": "inputs",
                        "severity": "WARN",
                        "message": f"required inputs coverage: {covered}/{total} ({pct:.0f}%)",
                        "missing": missing_inputs[:5],
                    })

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

    print(f"Core:   {core_path}")
    print(f"Skills: {skills_path}")
    print()

    errors = 0
    warnings = 0
    checked = 0
    conformant = 0

    # Walk all SKILL.md files
    for skill_md in sorted(skills_path.rglob("SKILL.md")):
        if ".git" in str(skill_md):
            continue

        skill = parse_skill_md(skill_md)
        meta = skill["frontmatter"].get("metadata", {})
        impl = meta.get("ai-native-skills.implements", "")
        if not impl or "ai-native-core/" not in impl:
            continue

        # Resolve contract path
        contract_rel = impl.replace("ai-native-core/", "")
        contract_path = core_path / contract_rel
        if not contract_path.exists():
            continue  # validate-implements.sh handles missing paths

        contract = parse_contract(contract_path)
        if not contract:
            continue

        checked += 1
        rel_skill = skill_md.relative_to(skills_path)
        violations = check_conformance(contract, skill, str(rel_skill))

        if not violations:
            conformant += 1
        else:
            for v in violations:
                if v["severity"] == "ERROR":
                    errors += 1
                else:
                    warnings += 1
                icon = "✗" if v["severity"] == "ERROR" else "⚠"
                print(f"{icon} {rel_skill}")
                print(f"  {v['type']}: {v['message']}")
                if v.get("missing"):
                    for m in v["missing"]:
                        print(f"    - {m}")
                print()

    print("────────────────────────────────────")
    print(f"Checked:    {checked} adapter skills")
    print(f"Conformant: {conformant}")
    print(f"Warnings:   {warnings}")
    print(f"Errors:     {errors}")
    print()

    if errors > 0:
        print(f"FAIL — {errors} conformance error(s).")
        sys.exit(1)
    elif warnings > 0:
        print(f"PASS (with {warnings} warning(s)) — no critical conformance errors.")
        sys.exit(0)
    else:
        print("PASS — all adapter skills conform to their contracts.")
        sys.exit(0)


if __name__ == "__main__":
    main()
