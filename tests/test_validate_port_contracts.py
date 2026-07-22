from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from schema_validation import validator_for

SCRIPT = SCRIPTS / "validate-port-contracts.py"
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
        cls.schema_validator = validator_for(SCHEMA)
        cls.ports_root = ROOT / "contracts" / "ports"
        cls.model_path = cls.ports_root / "integration" / "model-inference.port.yaml"
        cls.execution_path = (
            cls.ports_root / "control" / "execution-run-management.port.yaml"
        )
        cls.agent_runtime_path = cls.ports_root / "control" / "agent-runtime.port.yaml"
        cls.workflow_coordination_path = (
            cls.ports_root / "control" / "workflow-coordination.port.yaml"
        )
        cls.review_path = cls.ports_root / "control" / "review-management.port.yaml"
        cls.approval_path = cls.ports_root / "control" / "approval-decision.port.yaml"
        cls.authorization_path = (
            cls.ports_root / "control" / "authorization-assessment.port.yaml"
        )

    def write_mutated_contract(
        self,
        source: Path,
        mutate,
        kind_directory: str,
    ) -> tuple[Path, Path]:
        temp_root = Path(tempfile.mkdtemp())
        path = temp_root / "contracts" / "ports" / kind_directory / source.name
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

    @staticmethod
    def request_field_ids(path: Path, request_id: str) -> set[str]:
        contract = module.load_yaml(path)["port_contract"]
        for request in contract["interactions"]["requests"]:
            if request["id"] == request_id:
                return {field["id"] for field in request["required_fields"]}
        raise AssertionError(f"request not found: {request_id}")

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
        paths = list(self.ports_root.rglob("*.port.yaml"))
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

    def test_agent_runtime_requires_existing_execution_capacity_and_authorization(self):
        required = self.request_field_ids(
            self.agent_runtime_path, "start_agent_runtime"
        )
        self.assertTrue(
            {
                "agent_ref",
                "execution_run_ref",
                "runtime_environment_ref",
                "adapter_binding_ref",
                "capacity_assessment_ref",
                "authorization_assessment_ref",
            }.issubset(required),
            required,
        )
        self.assertEqual(set(), self.transition_families(self.agent_runtime_path))

        contract = module.load_yaml(self.agent_runtime_path)["port_contract"]
        self.assertNotIn("execution_status", contract["boundary"]["owns"])
        self.assertIn("execution_status", contract["boundary"]["does_not_own"])
        self.assertEqual("required", contract["authorization"]["mode"])

    def test_workflow_coordination_does_not_invent_workflow_run_lifecycle(self):
        legacy_path = (
            self.ports_root / "control" / "workflow-orchestration.port.yaml"
        )
        self.assertFalse(legacy_path.exists())
        self.assertTrue(self.workflow_coordination_path.exists())
        self.assertEqual(
            set(), self.transition_families(self.workflow_coordination_path)
        )

        contract = module.load_yaml(self.workflow_coordination_path)["port_contract"]
        self.assertIn(
            "workflow-orchestration", contract["compatibility"]["aliases"]
        )
        self.assertEqual("none", contract["authorization"]["mode"])
        self.assertIn(
            "workflow_run_aggregate", contract["boundary"]["does_not_own"]
        )

        for path in self.ports_root.rglob("*.port.yaml"):
            self.assertNotIn("workflow_run_ref", path.read_text(), path)

    def test_compatibility_aliases_resolve_uniquely(self):
        alias_owners: dict[str, str] = {}
        for path in self.ports_root.rglob("*.port.yaml"):
            contract = module.load_yaml(path)["port_contract"]
            for alias in contract["compatibility"]["aliases"]:
                self.assertNotIn(
                    alias,
                    alias_owners,
                    f"alias {alias!r} is owned by both {alias_owners.get(alias)!r} "
                    f"and {contract['id']!r}",
                )
                alias_owners[alias] = contract["id"]

        self.assertEqual(
            "workflow-coordination", alias_owners["workflow-orchestration"]
        )

    def test_execution_run_uses_workflow_coordination_reference(self):
        text = self.execution_path.read_text()
        self.assertIn("workflow_coordination_ref", text)
        self.assertNotIn("workflow_run_ref", text)

    def test_retired_review_approval_alias_is_not_reintroduced(self):
        aliases = set()
        for path in self.ports_root.rglob("*.port.yaml"):
            contract = module.load_yaml(path)["port_contract"]
            aliases.update(contract["compatibility"]["aliases"])
        self.assertNotIn("review-approval", aliases)

    def test_no_temporary_port_migration_artifacts_remain(self):
        temporary_artifacts = [
            *ROOT.glob(".github/workflows/tmp-port*.yml"),
            *ROOT.glob("scripts/materialize-port*.py"),
            *ROOT.glob("scripts/complete-port-inventory-migration.py"),
        ]
        self.assertEqual([], temporary_artifacts)

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
        paths = list(self.ports_root.rglob("*.port.yaml"))
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
