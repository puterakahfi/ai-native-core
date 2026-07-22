from __future__ import annotations

import copy
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from schema_validation import load_yaml, validator_for

VALIDATOR_SCRIPT = SCRIPTS / "validate-contract-schemas.py"
spec = importlib.util.spec_from_file_location("validate_contract_schemas", VALIDATOR_SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

FIXTURES = ROOT / "tests" / "fixtures" / "contract-schemas"

SCHEMA_FIXTURES = {
    "skill-contract.schema.yaml": "skill.contract.yaml",
    "workflow-contract.schema.yaml": "workflow.contract.yaml",
    "runtime-contract.schema.yaml": "runtime.contract.yaml",
    "behavioral-test-contract.schema.yaml": "behavioral-test.test.yaml",
    "port-contract.schema.yaml": "port.port.yaml",
    "adapter-manifest.schema.yaml": "adapter.contract.yaml",
    "compatibility-manifest.schema.yaml": "compatibility.contract.yaml",
    "domain-contract.schema.yaml": "domain.contract.yaml",
    "contract-manifest.schema.yaml": "manifest.yaml",
}


class UnifiedContractSchemaTests(unittest.TestCase):
    def test_positive_fixtures_pass_each_schema_family(self):
        for schema_name, fixture_name in SCHEMA_FIXTURES.items():
            with self.subTest(schema=schema_name):
                validator = validator_for(ROOT / "schemas" / schema_name)
                payload = load_yaml(FIXTURES / "valid" / fixture_name)
                errors = list(validator.iter_errors(payload))
                self.assertEqual([], [error.message for error in errors])

    def test_negative_fixtures_fail_each_schema_family(self):
        for schema_name, fixture_name in SCHEMA_FIXTURES.items():
            with self.subTest(schema=schema_name):
                validator = validator_for(ROOT / "schemas" / schema_name)
                payload = load_yaml(FIXTURES / "invalid" / fixture_name)
                errors = list(validator.iter_errors(payload))
                self.assertTrue(errors, f"negative fixture unexpectedly passed: {fixture_name}")

    def test_repository_satisfies_unified_contract_pipeline(self):
        errors, _warnings = module.validate_repository(ROOT)
        self.assertEqual([], errors)

    def make_root(self) -> Path:
        root = Path(tempfile.mkdtemp())
        shutil.copytree(ROOT / "schemas", root / "schemas")
        (root / "contracts").mkdir()
        return root

    @staticmethod
    def write_yaml(path: Path, payload: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(payload, sort_keys=False))

    def skill_payload(self) -> dict:
        return load_yaml(FIXTURES / "valid" / "skill.contract.yaml")

    def workflow_payload(self) -> dict:
        return load_yaml(FIXTURES / "valid" / "workflow.contract.yaml")

    def test_duplicate_contract_identity_is_rejected(self):
        root = self.make_root()
        payload = self.skill_payload()
        self.write_yaml(root / "contracts" / "skills" / "quality" / "first.contract.yaml", payload)
        self.write_yaml(root / "contracts" / "skills" / "quality" / "second.contract.yaml", payload)

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(
            any("duplicate identity 'skill_contract:fixture-skill'" in error for error in errors),
            errors,
        )

    def test_filename_identity_drift_is_rejected(self):
        root = self.make_root()
        payload = self.skill_payload()
        self.write_yaml(root / "contracts" / "skills" / "quality" / "wrong-name.contract.yaml", payload)

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(any("filename/id mismatch" in error for error in errors), errors)

    def test_schema_kind_and_path_family_drift_are_rejected(self):
        root = self.make_root()
        payload = self.skill_payload()
        payload["contract_schema"]["kind"] = "runtime_contract"
        payload["contract_schema"]["path"] = "schemas/runtime-contract.schema.yaml"
        self.write_yaml(root / "contracts" / "skills" / "quality" / "fixture-skill.contract.yaml", payload)

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(any("path family requires 'skill_contract'" in error for error in errors), errors)

    def test_workflow_reference_to_unknown_phase_is_rejected(self):
        root = self.make_root()
        payload = self.workflow_payload()
        payload["workflow_contract"]["skill_load_order"].append(
            {"phase": "missing_phase", "load": ["fixture-skill"]}
        )
        self.write_yaml(root / "contracts" / "workflows" / "fixture-workflow.contract.yaml", payload)

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(any("references unknown phase 'missing_phase'" in error for error in errors), errors)

    def test_compatibility_alias_to_missing_target_is_rejected(self):
        root = self.make_root()
        payload = load_yaml(FIXTURES / "valid" / "compatibility.contract.yaml")
        self.write_yaml(
            root / "contracts" / "compatibility" / "fixture-path-aliases.contract.yaml",
            payload,
        )

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(any("canonical target does not exist" in error for error in errors), errors)

    def test_manifest_checksum_drift_is_rejected(self):
        root = self.make_root()
        payload = self.skill_payload()
        contract_path = root / "contracts" / "skills" / "quality" / "fixture-skill.contract.yaml"
        self.write_yaml(contract_path, payload)

        manifest = load_yaml(FIXTURES / "valid" / "manifest.yaml")
        manifest["total_contracts"] = 1
        manifest["contracts"]["skills"] = {
            "quality": [
                {
                    "id": "fixture-skill",
                    "kind": "skill_contract",
                    "schema_version": "1.0.0",
                    "schema_path": "schemas/skill-contract.schema.yaml",
                    "path": "contracts/skills/quality/fixture-skill.contract.yaml",
                    "version": "1.0.0",
                    "sha256": "0000000000000000",
                }
            ]
        }
        self.write_yaml(root / "contracts" / "manifest.yaml", manifest)

        errors, _warnings = module.validate_repository(root)
        self.assertTrue(any("metadata drift" in error for error in errors), errors)

    def test_workflow_migration_contracts_are_canonical(self):
        expected = {
            "design-refinement",
            "redesign-workflow",
            "skill-evolution",
            "development-loop",
        }
        for contract_id in expected:
            path = ROOT / "contracts" / "workflows" / f"{contract_id}.contract.yaml"
            self.assertTrue(path.exists(), path)
            payload = load_yaml(path)
            self.assertEqual("workflow_contract", payload["contract_schema"]["kind"])
            self.assertEqual(contract_id, payload["workflow_contract"]["id"])

        self.assertFalse(
            (ROOT / "contracts" / "skills" / "quality" / "design-refinement.contract.yaml").exists()
        )
        self.assertFalse(
            (ROOT / "contracts" / "skills" / "quality" / "redesign-workflow.contract.yaml").exists()
        )
        self.assertFalse(
            (ROOT / "contracts" / "skills" / "quality" / "skill-evolution.contract.yaml").exists()
        )
        self.assertFalse(
            (ROOT / "contracts" / "runtime" / "development-loop.contract.yaml").exists()
        )

    def test_internal_phase_procedures_remain_skills(self):
        for contract_id in ("design-review", "systematic-debugging"):
            path = ROOT / "contracts" / "skills" / "quality" / f"{contract_id}.contract.yaml"
            payload = load_yaml(path)
            self.assertEqual("skill_contract", payload["contract_schema"]["kind"])
            self.assertEqual("skill", payload["skill_contract"]["type"])


if __name__ == "__main__":
    unittest.main()
