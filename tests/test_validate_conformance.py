from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
FIXTURES = ROOT / "tests" / "fixtures" / "conformance-boundaries"
SCRIPT = SCRIPTS / "validate-conformance.py"
ENGINE = SCRIPTS / "conformance_validation.py"

spec = importlib.util.spec_from_file_location("conformance_validation", ENGINE)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class StructuredConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = Path(tempfile.mkdtemp())
        cls.core = cls.temp / "core"
        shutil.copytree(FIXTURES / "core" / "contracts", cls.core / "contracts")
        shutil.copytree(ROOT / "schemas", cls.core / "schemas")
        cls.adapters = FIXTURES

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.temp)

    def adapter_result(self, name: str):
        skill = self.adapters / "skills" / name / "SKILL.md"
        declaration = skill.parent / module.DECLARATION
        if declaration.exists():
            return module.validate_structured(self.core, self.adapters, skill, declaration)
        return module.validate_legacy(self.core, self.adapters, skill)

    def test_complete_declaration_is_structurally_conformant(self):
        result = self.adapter_result("valid-boundary")
        self.assertEqual("CONFORMANT", result["structural_status"])
        self.assertEqual("BEHAVIOR_NOT_VERIFIED", result["behavioral_status"])
        self.assertEqual("NOT_CHECKABLE", result["runtime_status"])
        self.assertEqual("NOT_CHECKABLE", result["product_status"])
        self.assertEqual("NOT_EVALUATED", result["approval_status"])

    def test_behavioral_reference_is_visible_but_not_runtime_or_product_proof(self):
        result = self.adapter_result("valid-evidence")
        self.assertEqual("CONFORMANT", result["structural_status"])
        self.assertEqual("EVIDENCE_REFERENCED", result["behavioral_status"])
        self.assertEqual("NOT_CHECKABLE", result["runtime_status"])
        self.assertEqual("NOT_CHECKABLE", result["product_status"])

    def test_partial_declaration_is_not_promoted_to_conformant(self):
        result = self.adapter_result("partial-boundary")
        self.assertEqual("PARTIAL", result["structural_status"])
        codes = {item["code"] for item in result["findings"]}
        self.assertIn("BOUNDARY_COVERAGE_MISSING", codes)
        self.assertIn("BOUNDARY_DELEGATION_MISSING", codes)

    def test_explicit_delegated_responsibility_overclaim_is_error(self):
        result = self.adapter_result("overclaim-boundary")
        self.assertEqual("ERROR", result["structural_status"])
        codes = {item["code"] for item in result["findings"]}
        self.assertIn("BOUNDARY_DELEGATED_RESPONSIBILITY_OVERCLAIM", codes)

    def test_missing_v2_declaration_is_not_checkable(self):
        result = self.adapter_result("missing-boundary")
        self.assertEqual("NOT_CHECKABLE", result["structural_status"])
        self.assertEqual("STRUCTURED_DECLARATION_MISSING", result["findings"][0]["code"])

    def test_malformed_declaration_is_error(self):
        result = self.adapter_result("malformed-declaration")
        self.assertEqual("ERROR", result["structural_status"])
        self.assertTrue(all(item["code"] == "DECLARATION_SCHEMA_INVALID" for item in result["findings"]))

    def test_contract_identity_kind_version_and_capability_are_deterministic(self):
        source = self.adapters / "skills" / "valid-boundary" / module.DECLARATION
        payload = yaml.safe_load(source.read_text())
        body = payload["adapter_conformance"]
        body["implements"]["contract_id"] = "wrong-contract"
        body["implements"]["contract_kind"] = "workflow_contract"
        body["implements"]["contract_version"] = "^2.0.0"
        body["capability"] = "wrong_capability"
        root = Path(tempfile.mkdtemp())
        skill_dir = root / "skills" / "valid-boundary"
        skill_dir.mkdir(parents=True)
        shutil.copy2(self.adapters / "skills" / "valid-boundary" / "SKILL.md", skill_dir / "SKILL.md")
        declaration = skill_dir / module.DECLARATION
        declaration.write_text(yaml.safe_dump(payload, sort_keys=False))
        try:
            result = module.validate_structured(self.core, root, skill_dir / "SKILL.md", declaration)
        finally:
            shutil.rmtree(root)
        codes = {item["code"] for item in result["findings"]}
        self.assertEqual("ERROR", result["structural_status"])
        self.assertTrue({"CONTRACT_ID_MISMATCH", "CONTRACT_KIND_MISMATCH", "CONTRACT_VERSION_INCOMPATIBLE", "CAPABILITY_MISMATCH"}.issubset(codes))

    def test_unknown_interface_ids_fail(self):
        source = self.adapters / "skills" / "valid-boundary" / module.DECLARATION
        payload = yaml.safe_load(source.read_text())
        payload["adapter_conformance"]["interface"]["outputs"].append("invented_output")
        root = Path(tempfile.mkdtemp())
        skill_dir = root / "skills" / "valid-boundary"
        skill_dir.mkdir(parents=True)
        shutil.copy2(self.adapters / "skills" / "valid-boundary" / "SKILL.md", skill_dir / "SKILL.md")
        declaration = skill_dir / module.DECLARATION
        declaration.write_text(yaml.safe_dump(payload, sort_keys=False))
        try:
            result = module.validate_structured(self.core, root, skill_dir / "SKILL.md", declaration)
        finally:
            shutil.rmtree(root)
        self.assertEqual("ERROR", result["structural_status"])
        self.assertIn("OUTPUT_UNKNOWN", {item["code"] for item in result["findings"]})

    def test_required_unsupported_claim_is_partial(self):
        source = self.adapters / "skills" / "valid-boundary" / module.DECLARATION
        payload = yaml.safe_load(source.read_text())
        payload["adapter_conformance"]["unsupported_claims"] = ["contract_output"]
        root = Path(tempfile.mkdtemp())
        skill_dir = root / "skills" / "valid-boundary"
        skill_dir.mkdir(parents=True)
        shutil.copy2(self.adapters / "skills" / "valid-boundary" / "SKILL.md", skill_dir / "SKILL.md")
        declaration = skill_dir / module.DECLARATION
        declaration.write_text(yaml.safe_dump(payload, sort_keys=False))
        try:
            result = module.validate_structured(self.core, root, skill_dir / "SKILL.md", declaration)
        finally:
            shutil.rmtree(root)
        self.assertEqual("PARTIAL", result["structural_status"])
        self.assertIn("REQUIRED_CLAIM_UNSUPPORTED", {item["code"] for item in result["findings"]})

    def test_legacy_text_matching_is_supplemental_only(self):
        _, body, _ = module.load_contract_document(
            self.core / "contracts" / "skills" / "test" / "boundary-sample.contract.yaml"
        )
        contract = module.interface("skill_contract", body)
        diagnostics = module.text_diagnostics(contract, {"content_lower": ""})
        self.assertEqual({"migration"}, {item["dimension"] for item in diagnostics})
        self.assertTrue(all(item["severity"] == "INFO" for item in diagnostics))
        self.assertTrue(all(item["result_class"] == "NOT_CHECKABLE" for item in diagnostics))

    def test_exit_codes_are_deterministic(self):
        valid = self.adapter_result("valid-boundary")
        partial = self.adapter_result("partial-boundary")
        missing = self.adapter_result("missing-boundary")
        error = self.adapter_result("overclaim-boundary")
        for item, migration, strict in (
            (valid, 0, 0),
            (partial, 0, 2),
            (missing, 0, 3),
            (error, 1, 1),
        ):
            report = module.build_report(self.core, self.adapters, "migration", 1, [item])
            self.assertEqual(migration, module.exit_code(report, "migration"))
            self.assertEqual(strict, module.exit_code(report, "strict"))

    def test_report_validates_and_writes_repository_and_per_adapter_files(self):
        results = [self.adapter_result("valid-boundary"), self.adapter_result("valid-evidence")]
        report = module.build_report(self.core, self.adapters, "strict", 2, results)
        validator = module.validator_for(
            self.core / "schemas" / "conformance-report.schema.yaml",
            schemas_root=self.core / "schemas",
        )
        self.assertEqual([], list(validator.iter_errors(report)))
        output = Path(tempfile.mkdtemp())
        try:
            module.write_reports(report, output, "json")
            summary = json.loads((output / "repository-summary.json").read_text())
            self.assertEqual(2, summary["conformance_report"]["summary"]["checked"])
            self.assertTrue((output / "valid-boundary.json").exists())
            self.assertTrue((output / "valid-evidence.json").exists())
        finally:
            shutil.rmtree(output)

    def test_adapter_kind_patterns_are_schema_valid(self):
        source = yaml.safe_load(
            (self.adapters / "skills" / "valid-boundary" / module.DECLARATION).read_text()
        )
        validator = module.validator_for(
            self.core / "schemas" / "adapter-conformance.schema.yaml",
            schemas_root=self.core / "schemas",
        )
        for kind in ("skill", "workflow", "meta_skill", "facade", "runtime_adapter", "port_adapter"):
            payload = copy.deepcopy(source)
            payload["adapter_conformance"]["adapter"]["kind"] = kind
            self.assertEqual([], list(validator.iter_errors(payload)), kind)

    def test_cli_generates_machine_reports_and_returns_error_for_overclaim(self):
        output = Path(tempfile.mkdtemp())
        try:
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), str(self.core), str(self.adapters), "--mode", "migration", "--output-dir", str(output), "--quiet"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(1, proc.returncode, proc.stdout + proc.stderr)
            self.assertTrue((output / "repository-summary.json").exists())
            summary = json.loads((output / "repository-summary.json").read_text())
            self.assertGreaterEqual(summary["conformance_report"]["summary"]["errors"], 1)
            self.assertGreaterEqual(summary["conformance_report"]["summary"]["not_checkable"], 1)
        finally:
            shutil.rmtree(output)


if __name__ == "__main__":
    unittest.main()
