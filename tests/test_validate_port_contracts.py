from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-port-contracts.py"
SCHEMA = ROOT / "schemas" / "port-contract.schema.yaml"
INVALID_FIXTURE = (
    ROOT
    / "tests"
    / "fixtures"
    / "port-contracts"
    / "invalid"
    / "missing-boundary.port.yaml"
)

spec = importlib.util.spec_from_file_location("validate_port_contracts", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class PortContractValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = module.load_yaml(SCHEMA)
        Draft202012Validator.check_schema(cls.schema)
        cls.schema_validator = Draft202012Validator(cls.schema)
        cls.model_path = (
            ROOT
            / "contracts"
            / "ports"
            / "integration"
            / "model-inference.port.yaml"
        )
        cls.execution_path = (
            ROOT
            / "contracts"
            / "ports"
            / "control"
            / "execution-run-management.port.yaml"
        )
        cls.review_path = (
            ROOT
            / "contracts"
            / "ports"
            / "control"
            / "review-management.port.yaml"
        )
        cls.approval_path = (
            ROOT
            / "contracts"
            / "ports"
            / "control"
            / "approval-decision.port.yaml"
        )
        cls.authorization_path = (
            ROOT
            / "contracts"
            / "ports"
            / "control"
            / "authorization-assessment.port.yaml"
        )

    def write_mutated_contract(
        self,
        source: Path,
        mutate,
        kind_directory: str,
    ) -> tuple[Path, Path]:
        temp_root = Path(tempfile.mkdtemp())
        path = (
            temp_root
            / "contracts"
            / "ports"
            / kind_directory
            / source.name
        )
        path.parent.mkdir(parents=True)
        payload = module.load_yaml(source)
        mutate(payload)
        path.write_text(yaml.safe_dump(payload, sort_keys=False))
        return temp_root, path

    @staticmethod
    def transition_families(path: Path) -> set[str]:
        contract = module.load_yaml(path)["port_contract"]
        return {
            transition["status_family"]
            for transition in contract["state_transitions"]
        }

    def test_schema_uses_standard_root_keywords(self):
        self.assertEqual("Native AI Engineering Port Contract", self.schema["title"])
        self.assertEqual("object", self.schema["type"])
        self.assertNotIn("$title", self.schema)
        self.assertNotIn("$type", self.schema)

    def test_schema_rejects_non_object_root(self):
        errors = list(self.schema_validator.iter_errors([]))
        self.assertTrue(errors)
        self.assertTrue(
            any("is not of type 'object'" in error.message for error in errors),
            [error.message for error in errors],
        )

    def test_repository_contracts_pass(self):
        paths = list((ROOT / "contracts" / "ports").rglob("*.port.yaml"))
        self.assertEqual(
            [],
            module.validate_paths(paths, schema_path=SCHEMA, root=ROOT),
        )

    def test_review_approval_and_authorization_remain_separate(self):
        self.assertEqual(
            {"review_disposition"}, self.transition_families(self.review_path)
        )
        self.assertEqual(
            {"approval_status"}, self.transition_families(self.approval_path)
        )
        self.assertEqual(set(), self.transition_families(self.authorization_path))

        authorization = module.load_yaml(self.authorization_path)["port_contract"]
        self.assertEqual("required", authorization["authorization"]["mode"])
        self.assertTrue(
            authorization["authorization"]["authority_reference_required"]
        )

    def test_retired_review_approval_alias_is_not_reintroduced(self):
        aliases = set()
        for path in (ROOT / "contracts" / "ports").rglob("*.port.yaml"):
            contract = module.load_yaml(path)["port_contract"]
            aliases.update(contract["compatibility"]["aliases"])
        self.assertNotIn("review-approval", aliases)

    def test_negative_fixture_fails_schema_validation(self):
        payload = module.load_yaml(INVALID_FIXTURE)
        errors = list(self.schema_validator.iter_errors(payload))
        self.assertTrue(errors)
        self.assertTrue(
            any("boundary" in error.message for error in errors),
            [error.message for error in errors],
        )

    def test_boundary_overlap_fails_semantic_validation(self):
        def mutate(payload):
            boundary = payload["port_contract"]["boundary"]
            boundary["does_not_own"].append(boundary["owns"][0])

        temp_root, path = self.write_mutated_contract(
            self.model_path, mutate, "integration"
        )
        errors = module.validate_paths([path], schema_path=SCHEMA, root=temp_root)
        self.assertTrue(any("boundary overlap" in error for error in errors))

    def test_multiple_status_families_fail(self):
        def mutate(payload):
            payload["port_contract"]["state_transitions"].append(
                {
                    "status_family": "approval_status",
                    "from": "pending",
                    "to": "approved",
                    "condition": "An authority-bearing approval decision was recorded.",
                }
            )

        temp_root, path = self.write_mutated_contract(
            self.execution_path, mutate, "control"
        )
        errors = module.validate_paths([path], schema_path=SCHEMA, root=temp_root)
        self.assertTrue(
            any("only one typed status family" in error for error in errors)
        )

    def test_authorization_none_cannot_require_authority_reference(self):
        def mutate(payload):
            authorization = payload["port_contract"]["authorization"]
            authorization["mode"] = "none"
            authorization["required_for"] = []
            authorization["authority_reference_required"] = True

        temp_root, path = self.write_mutated_contract(
            self.model_path, mutate, "integration"
        )
        errors = module.validate_paths([path], schema_path=SCHEMA, root=temp_root)
        self.assertTrue(
            any("cannot require an authority reference" in error for error in errors)
        )

    def test_cli_passes_for_repository_contracts(self):
        paths = list((ROOT / "contracts" / "ports").rglob("*.port.yaml"))
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn(f"PASS — {len(paths)} port contract(s)", result.stdout)


if __name__ == "__main__":
    unittest.main()
