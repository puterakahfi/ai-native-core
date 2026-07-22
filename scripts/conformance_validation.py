#!/usr/bin/env python3
"""Structured adapter conformance validator v2."""
from __future__ import annotations

import argparse, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import yaml

from contract_resolution import load_contract_document, pin_accepts, resolve_contract_reference
from schema_validation import format_schema_error, validator_for

DECLARATION = "adapter.conformance.yaml"
EVIDENCE_BOUNDARY = [
    "static declaration conformance does not prove executable behavior",
    "behavioral evidence is separate from runtime evidence",
    "runtime evidence is separate from product acceptance",
    "product evidence is separate from approval",
    "approval is not evaluated by this validator",
]


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text())
    if not isinstance(value, dict):
        raise ValueError("document root must be a mapping")
    return value


def parse_skill(path: Path) -> dict[str, Any]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    fm = yaml.safe_load(match.group(1)) if match else {}
    fm = fm if isinstance(fm, dict) else {}
    return {"frontmatter": fm, "content_lower": content.lower()}


def norm(value: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.strip().lower())).strip("_")


def strings(value: Any) -> list[str]:
    if value is None: return []
    if isinstance(value, str): return [value]
    if isinstance(value, dict): return [str(key) for key in value]
    if not isinstance(value, list): return []
    result = []
    for item in value:
        if isinstance(item, str): result.append(item)
        elif isinstance(item, dict):
            for key in ("id", "skill", "name", "contract", "capability"):
                if isinstance(item.get(key), str): result.append(item[key]); break
    return result


def unique(values: list[str]) -> list[str]:
    found, result = set(), []
    for value in values:
        key = norm(value)
        if key and key not in found: found.add(key); result.append(value)
    return result


def interface(kind: str, body: dict[str, Any]) -> dict[str, Any]:
    inputs, outputs = body.get("inputs") or {}, body.get("outputs") or {}
    inputs = inputs if isinstance(inputs, dict) else {}
    outputs = outputs if isinstance(outputs, dict) else {}
    boundary = body.get("boundary") or {}
    boundary = boundary if isinstance(boundary, dict) else {}
    if kind == "port_contract":
        covers = strings(boundary.get("owns"))
        delegates = strings(boundary.get("delegates")) + strings(boundary.get("does_not_own"))
    else:
        covers = strings(boundary.get("covers"))
        delegates = strings(boundary.get("does_not_cover"))
    return {
        "id": str(body.get("id", body.get("skill", ""))),
        "kind": kind,
        "version": str(body.get("version", "0.0.0")),
        "capability": str(body.get("capability", "")) or None,
        "required_inputs": unique(strings(inputs.get("required"))),
        "optional_inputs": unique(strings(inputs.get("optional"))),
        "required_outputs": unique(strings(outputs.get("required"))),
        "allowed_outputs": unique(strings(outputs.get("allowed"))),
        "gates": unique(strings(body.get("quality_gates") or body.get("safety_gates"))),
        "covers": unique(covers), "delegates": unique(delegates),
        "dependencies": unique(strings(body.get("dependencies"))),
        "handoffs": unique(strings(body.get("handoffs"))),
        "adapter_requirements": unique(strings(body.get("adapter_requirements"))),
    }


def issue(code, cls, dimension, message, expected=(), actual=(), severity=None):
    return {"code": code, "severity": severity or ("ERROR" if cls == "ERROR" else "WARN"),
            "result_class": cls, "dimension": dimension, "message": message,
            "expected": list(expected), "actual": list(actual), "evidence_refs": []}


def maps(values): return {norm(v): v for v in values if norm(v)}


def compare(expected, actual, dimension, missing_code, unknown_code, required_only=False):
    e, a, findings = maps(expected), maps(actual), []
    missing = sorted(set(e) - set(a))
    unknown = sorted(set(a) - set(e))
    if missing:
        findings.append(issue(missing_code, "PARTIAL", dimension,
            f"adapter declaration is missing contract {dimension}", [e[x] for x in missing], actual))
    if unknown and not required_only:
        findings.append(issue(unknown_code, "ERROR", dimension,
            f"adapter declaration contains unknown {dimension}", expected, [a[x] for x in unknown]))
    return findings


def legacy_list(raw):
    if raw is None: return []
    if isinstance(raw, list): return strings(raw)
    if not isinstance(raw, str): return []
    try: return strings(json.loads(raw))
    except Exception:
        try: return strings(yaml.safe_load(raw))
        except Exception: return [raw]


def text_diagnostics(contract, skill):
    diagnostics, content = [], skill["content_lower"]
    for dim, expected in (("inputs", contract["required_inputs"]),
                          ("outputs", contract["required_outputs"] + contract["allowed_outputs"]),
                          ("gates", contract["gates"])):
        missing = [item for item in expected if not any(v in content for v in
                   (item.lower(), item.lower().replace("_", " "), item.lower().replace("_", "-")))]
        if missing: diagnostics.append(issue(f"LEGACY_TEXT_{dim.upper()}_MISSING", "NOT_CHECKABLE", "migration",
            f"legacy prose does not mention all contract {dim}; prose is supplemental only", missing, severity="INFO"))
    return diagnostics


def status(findings):
    classes = {item["result_class"] for item in findings}
    if "ERROR" in classes: return "ERROR"
    if "PARTIAL" in classes: return "PARTIAL"
    if "NOT_CHECKABLE" in classes: return "NOT_CHECKABLE"
    return "CONFORMANT"


def result(adapter_id, adapter_kind, adapter_path, declaration_path, contract, findings, migration, evidence):
    layers = {ref.get("layer") for ref in evidence}
    return {"adapter_id": adapter_id, "adapter_kind": adapter_kind, "adapter_path": adapter_path,
            "declaration_path": declaration_path, "contract": contract,
            "structural_status": status(findings),
            "behavioral_status": "EVIDENCE_REFERENCED" if "behavioral" in layers else "BEHAVIOR_NOT_VERIFIED",
            "runtime_status": "EVIDENCE_REFERENCED" if "runtime" in layers else "NOT_CHECKABLE",
            "product_status": "EVIDENCE_REFERENCED" if "product" in layers else "NOT_CHECKABLE",
            "approval_status": "NOT_EVALUATED", "findings": findings,
            "migration_diagnostics": migration, "evidence_refs": evidence}


def validate_schema(core: Path, path: Path):
    try: payload = load_yaml(path)
    except Exception as exc: return None, [issue("DECLARATION_YAML_INVALID", "ERROR", "schema", str(exc))]
    validator = validator_for(core / "schemas/adapter-conformance.schema.yaml", schemas_root=core / "schemas")
    errors = sorted(validator.iter_errors(payload), key=lambda e: list(e.absolute_path))
    return payload, [issue("DECLARATION_SCHEMA_INVALID", "ERROR", "schema", format_schema_error(e)) for e in errors]


def validate_structured(core: Path, adapters: Path, skill_path: Path, declaration_path: Path):
    skill, findings, migration = parse_skill(skill_path), [], []
    adapter_id = str(skill["frontmatter"].get("name", skill_path.parent.name))
    payload, schema_findings = validate_schema(core, declaration_path)
    if schema_findings:
        return result(adapter_id, "unknown", str(skill_path.relative_to(adapters)),
                      str(declaration_path.relative_to(adapters)), None, schema_findings, [], [])
    decl = payload["adapter_conformance"]; adapter = decl["adapter"]; impl = decl["implements"]
    entrypoint = str(skill_path.relative_to(adapters))
    if adapter["id"] != adapter_id: findings.append(issue("ADAPTER_ID_MISMATCH", "ERROR", "adapter_identity",
        "declaration adapter ID does not match SKILL.md", [adapter_id], [adapter["id"]]))
    if adapter["entrypoint"] != entrypoint: findings.append(issue("ADAPTER_ENTRYPOINT_MISMATCH", "ERROR", "adapter_identity",
        "declaration entrypoint does not match SKILL.md path", [entrypoint], [adapter["entrypoint"]]))
    resolved = resolve_contract_reference(core, impl["contract_path"])
    if not resolved:
        findings.append(issue("CONTRACT_REFERENCE_UNRESOLVED", "ERROR", "contract_identity",
                              "contract path cannot be resolved", actual=[impl["contract_path"]]))
        return result(adapter_id, adapter["kind"], entrypoint, str(declaration_path.relative_to(adapters)),
                      None, findings, migration, decl["evidence_refs"])
    kind, body, _ = load_contract_document(resolved["path"]); contract = interface(kind, body)
    cref = {"declared_path": resolved["declared_path"], "canonical_path": resolved["canonical_path"],
            "contract_id": contract["id"], "contract_kind": kind, "contract_version": contract["version"],
            "version_pin": impl["contract_version"], "alias_used": bool(resolved.get("alias"))}
    for code, actual, expected, dim in (
        ("CONTRACT_ID_MISMATCH", impl["contract_id"], contract["id"], "contract_identity"),
        ("CONTRACT_KIND_MISMATCH", impl["contract_kind"], kind, "contract_identity"),
        ("CAPABILITY_MISMATCH", decl.get("capability"), contract["capability"], "capability")):
        if actual != expected: findings.append(issue(code, "ERROR", dim, "declaration does not match resolved contract", [str(expected)], [str(actual)]))
    try: compatible = pin_accepts(impl["contract_version"], contract["version"])
    except Exception as exc:
        compatible = False; findings.append(issue("CONTRACT_VERSION_PIN_INVALID", "ERROR", "contract_identity", str(exc), actual=[impl["contract_version"]]))
    if not compatible and not any(f["code"] == "CONTRACT_VERSION_PIN_INVALID" for f in findings):
        findings.append(issue("CONTRACT_VERSION_INCOMPATIBLE", "ERROR", "contract_identity",
                              "version pin is incompatible", [contract["version"]], [impl["contract_version"]]))
    declared_inputs = decl["interface"]["inputs"]
    universe_inputs = unique(contract["required_inputs"] + contract["optional_inputs"])
    findings += compare(contract["required_inputs"], declared_inputs, "inputs", "REQUIRED_INPUT_MISSING", "INPUT_UNKNOWN", True)
    unknown = sorted(set(maps(declared_inputs)) - set(maps(universe_inputs)))
    if unknown: findings.append(issue("INPUT_UNKNOWN", "ERROR", "inputs", "adapter declares unknown inputs", universe_inputs, [maps(declared_inputs)[x] for x in unknown]))
    findings += compare(unique(contract["required_outputs"] + contract["allowed_outputs"]), decl["interface"]["outputs"],
                        "outputs", "OUTPUT_COVERAGE_MISSING", "OUTPUT_UNKNOWN")
    findings += compare(contract["gates"], decl["interface"]["gates"], "gates", "GATE_COVERAGE_MISSING", "GATE_UNKNOWN")
    covers, delegates = decl["boundary"]["covers"], decl["boundary"]["delegates"]
    cm, dm, ac, ad = maps(contract["covers"]), maps(contract["delegates"]), maps(covers), maps(delegates)
    overlap = sorted(set(ac) & set(ad)); overclaim = sorted(set(ac) & set(dm))
    if overlap: findings.append(issue("BOUNDARY_COVER_DELEGATE_OVERLAP", "ERROR", "boundary", "same responsibility is covered and delegated", actual=[ac[x] for x in overlap]))
    if overclaim: findings.append(issue("BOUNDARY_DELEGATED_RESPONSIBILITY_OVERCLAIM", "ERROR", "boundary", "adapter claims delegated responsibility", [dm[x] for x in overclaim], [ac[x] for x in overclaim]))
    findings += compare(contract["covers"], covers, "boundary", "BOUNDARY_COVERAGE_MISSING", "BOUNDARY_COVER_UNKNOWN")
    missing_delegates = sorted(set(dm) - set(ad)); unknown_delegates = sorted(set(ad) - set(dm) - set(cm)); delegated_owned = sorted(set(ad) & set(cm))
    if missing_delegates: findings.append(issue("BOUNDARY_DELEGATION_MISSING", "PARTIAL", "boundary", "contract delegations are missing", [dm[x] for x in missing_delegates], delegates))
    if unknown_delegates: findings.append(issue("BOUNDARY_DELEGATION_UNKNOWN", "ERROR", "boundary", "unknown delegation", contract["delegates"], [ad[x] for x in unknown_delegates]))
    if delegated_owned: findings.append(issue("BOUNDARY_OWNED_RESPONSIBILITY_DELEGATED", "PARTIAL", "boundary", "contract-owned responsibility is delegated", [cm[x] for x in delegated_owned], delegates))
    for dim in ("dependencies", "handoffs", "adapter_requirements"):
        expected, actual = contract[dim], decl[dim]
        findings += compare(expected, actual, dim, f"{dim.upper()}_MISSING", f"{dim.upper()}_UNKNOWN", True)
        extras = sorted(set(maps(actual)) - set(maps(expected)))
        if extras: migration.append(issue(f"ADAPTER_SPECIFIC_{dim.upper()}", "NOT_CHECKABLE", "migration", f"additional adapter {dim}", actual=[maps(actual)[x] for x in extras], severity="INFO"))
    required_claims = maps(contract["required_inputs"] + contract["required_outputs"] + contract["allowed_outputs"] + contract["gates"] + contract["covers"] + contract["adapter_requirements"])
    delegated_claims = maps(contract["delegates"])
    for claim in decl["unsupported_claims"]:
        key = norm(claim)
        if key in required_claims: findings.append(issue("REQUIRED_CLAIM_UNSUPPORTED", "PARTIAL", "unsupported_claims", "required responsibility marked unsupported", [required_claims[key]], [claim]))
        elif key not in delegated_claims: migration.append(issue("UNSCOPED_UNSUPPORTED_CLAIM", "NOT_CHECKABLE", "migration", "unsupported claim is not defined by contract", actual=[claim], severity="INFO"))
    migration += text_diagnostics(contract, skill)
    return result(adapter_id, adapter["kind"], entrypoint, str(declaration_path.relative_to(adapters)), cref, findings, migration, decl["evidence_refs"])


def validate_legacy(core: Path, adapters: Path, skill_path: Path):
    skill = parse_skill(skill_path); metadata = skill["frontmatter"].get("metadata") or {}
    if not isinstance(metadata, dict): metadata = {}
    impl = str(metadata.get("ai-native-skills.implements", "")).strip()
    if not impl: return None
    adapter_id = str(skill["frontmatter"].get("name", skill_path.parent.name))
    findings = [issue("STRUCTURED_DECLARATION_MISSING", "NOT_CHECKABLE", "migration", f"{DECLARATION} is absent; legacy metadata cannot establish v2 conformance", actual=[impl])]
    migration, cref = [], None
    resolved = resolve_contract_reference(core, impl)
    if resolved:
        kind, body, _ = load_contract_document(resolved["path"]); contract = interface(kind, body)
        pin = str(metadata.get("ai-native-skills.contract-version", ""))
        cref = {"declared_path": resolved["declared_path"], "canonical_path": resolved["canonical_path"],
                "contract_id": contract["id"], "contract_kind": kind, "contract_version": contract["version"],
                "version_pin": pin, "alias_used": bool(resolved.get("alias"))}
        covers = legacy_list(metadata.get("ai-native-skills.boundary.covers")); delegates = legacy_list(metadata.get("ai-native-skills.boundary.delegates"))
        if covers or delegates: migration.append(issue("LEGACY_BOUNDARY_METADATA_PRESENT", "NOT_CHECKABLE", "migration", "legacy boundary metadata can seed reviewed migration", actual=covers + delegates, severity="INFO"))
        migration += text_diagnostics(contract, skill)
    else: findings.append(issue("LEGACY_CONTRACT_REFERENCE_UNRESOLVED", "ERROR", "contract_identity", "legacy contract reference cannot be resolved", actual=[impl]))
    return result(adapter_id, str(metadata.get("ai-native-skills.type", "unknown")), str(skill_path.relative_to(adapters)), None, cref, findings, migration, [])


def discover(core: Path, adapters: Path, adapter_filter=None):
    total, results = 0, []
    for skill_path in sorted(adapters.rglob("SKILL.md")):
        if ".git" in skill_path.parts: continue
        skill = parse_skill(skill_path); metadata = skill["frontmatter"].get("metadata") or {}
        impl = str(metadata.get("ai-native-skills.implements", "")) if isinstance(metadata, dict) else ""
        declaration = skill_path.parent / DECLARATION
        if not impl and not declaration.exists(): continue
        total += 1
        adapter_id = str(skill["frontmatter"].get("name", skill_path.parent.name))
        if adapter_filter and adapter_id != adapter_filter: continue
        results.append(validate_structured(core, adapters, skill_path, declaration) if declaration.exists() else validate_legacy(core, adapters, skill_path))
    return total, [item for item in results if item]


def build_report(core, adapters, mode, discovered, results):
    counts = {name: sum(r["structural_status"] == name for r in results) for name in ("CONFORMANT", "PARTIAL", "ERROR", "NOT_CHECKABLE")}
    return {"contract_schema": {"kind": "conformance_report", "version": "1.0.0", "path": "schemas/conformance-report.schema.yaml"},
            "conformance_report": {"version": "1.0.0", "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "mode": mode, "core_root": str(core), "adapters_root": str(adapters),
            "summary": {"discovered": discovered, "checked": len(results), "conformant": counts["CONFORMANT"],
            "partial": counts["PARTIAL"], "errors": counts["ERROR"], "not_checkable": counts["NOT_CHECKABLE"],
            "behavior_not_verified": sum(r["behavioral_status"] == "BEHAVIOR_NOT_VERIFIED" for r in results)},
            "results": results, "evidence_boundary": EVIDENCE_BOUNDARY}}


def write_reports(report, out: Path, fmt: str):
    out.mkdir(parents=True, exist_ok=True); suffix = "json" if fmt == "json" else "yaml"
    dump = (lambda v: json.dumps(v, indent=2) + "\n") if fmt == "json" else (lambda v: yaml.safe_dump(v, sort_keys=False))
    (out / f"repository-summary.{suffix}").write_text(dump(report))
    for item in report["conformance_report"]["results"]:
        body = dict(report["conformance_report"]); body["results"] = [item]
        s = item["structural_status"]
        body["summary"] = {"discovered": 1, "checked": 1, "conformant": int(s == "CONFORMANT"), "partial": int(s == "PARTIAL"),
                           "errors": int(s == "ERROR"), "not_checkable": int(s == "NOT_CHECKABLE"),
                           "behavior_not_verified": int(item["behavioral_status"] == "BEHAVIOR_NOT_VERIFIED")}
        (out / f"{item['adapter_id']}.{suffix}").write_text(dump({"contract_schema": report["contract_schema"], "conformance_report": body}))


def exit_code(report, mode):
    s = report["conformance_report"]["summary"]
    if s["errors"]: return 1
    if mode == "strict" and s["not_checkable"]: return 3
    if mode == "strict" and s["partial"]: return 2
    return 0


def cli(argv=None):
    p = argparse.ArgumentParser(); p.add_argument("core_root", type=Path); p.add_argument("adapters_root", type=Path)
    p.add_argument("--mode", choices=["migration", "strict"], default="migration"); p.add_argument("--adapter")
    p.add_argument("--output-dir", type=Path); p.add_argument("--format", choices=["json", "yaml"], default="json"); p.add_argument("--quiet", action="store_true")
    a = p.parse_args(argv); core, adapters = a.core_root.resolve(), a.adapters_root.resolve()
    if not (core / "contracts/manifest.yaml").is_file() or not (adapters / "skills").is_dir(): return 1
    discovered, results = discover(core, adapters, a.adapter); report = build_report(core, adapters, a.mode, discovered, results)
    validator = validator_for(core / "schemas/conformance-report.schema.yaml", schemas_root=core / "schemas")
    errors = [format_schema_error(e) for e in validator.iter_errors(report)]
    if errors:
        for error in errors: print(f"REPORT ERROR: {error}", file=sys.stderr)
        return 1
    if a.output_dir: write_reports(report, a.output_dir, a.format)
    if not a.quiet:
        for item in results: print(f"{item['adapter_id']}: {item['structural_status']} / {item['behavioral_status']}")
        print(yaml.safe_dump(report["conformance_report"]["summary"], sort_keys=False).strip())
    return exit_code(report, a.mode)


if __name__ == "__main__": raise SystemExit(cli())
