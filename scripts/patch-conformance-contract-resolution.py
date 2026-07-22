#!/usr/bin/env python3
"""One-time source patch for schema-aware conformance contract resolution."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "validate-conformance.py"

text = PATH.read_text()

old_import = "import yaml\n"
new_import = "import yaml\n\nfrom contract_resolution import load_contract_document, resolve_contract_reference\n"
if "from contract_resolution import" not in text:
    if old_import not in text:
        raise SystemExit("yaml import anchor not found")
    text = text.replace(old_import, new_import, 1)

old_parse = '''def parse_contract(path: Path) -> Optional[Dict[str, Any]]:
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
'''

new_parse = '''def parse_contract(path: Path) -> Optional[Dict[str, Any]]:
    """Parse any declared contract family and extract shared checkable fields."""
    try:
        kind, contract, _document = load_contract_document(path)
        gates = contract.get("quality_gates") or contract.get("safety_gates") or []
        return {
            "kind": kind,
            "id": contract.get("id", contract.get("skill", "")),
            "version": contract.get("version", "0.0.0"),
            "quality_gates": gates,
            "outputs": contract.get("outputs", {}),
            "inputs": contract.get("inputs", {}),
            "boundary": contract.get("boundary", {}),
        }
    except Exception as exc:
        print("  WARN: failed to parse {}: {}".format(path, exc))
        return None
'''

if old_parse in text:
    text = text.replace(old_parse, new_parse, 1)
elif new_parse not in text:
    raise SystemExit("parse_contract anchor not found")

old_resolution = '''        contract_rel = impl.replace("ai-native-core/", "")
        contract_path = core_path / contract_rel
        if not contract_path.exists():
            continue

        contract = parse_contract(contract_path)
'''

new_resolution = '''        contract_rel = impl.replace("ai-native-core/", "")
        resolution = resolve_contract_reference(core_path, contract_rel)
        if not resolution:
            print("  WARN: unresolved contract reference {} for {}".format(contract_rel, skill_md))
            continue
        contract_path = resolution["path"]

        contract = parse_contract(contract_path)
'''

if old_resolution in text:
    text = text.replace(old_resolution, new_resolution, 1)
elif new_resolution not in text:
    raise SystemExit("contract resolution anchor not found")

PATH.write_text(text)
print("Patched validate-conformance.py for schema-aware contract resolution.")
