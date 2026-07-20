from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-conformance.py"
FIXTURES = ROOT / "tests" / "fixtures" / "conformance-boundaries"

spec = importlib.util.spec_from_file_location("validate_conformance", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class BoundaryConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = module.parse_contract(
            FIXTURES / "core/contracts/skills/test/boundary-sample.contract.yaml"
        )
        assert cls.contract is not None

    def skill(self, name: str):
        return module.parse_skill_md(FIXTURES / f"skills/{name}/SKILL.md")

    def boundary_violations(self, name: str):
        return module.check_boundary(self.contract, self.skill(name))

    def test_valid_delegation_has_no_boundary_violations(self):
        self.assertEqual([], self.boundary_violations("valid-boundary"))

    def test_missing_boundary_is_not_checkable_not_false_pass(self):
        violations = self.boundary_violations("missing-boundary")
        self.assertEqual(1, len(violations))
        self.assertEqual("NOT_CHECKABLE", violations[0]["severity"])

    def test_partial_boundary_reports_missing_coverage_and_delegation(self):
        violations = self.boundary_violations("partial-boundary")
        messages = {violation["message"] for violation in violations}
        self.assertIn(
            "adapter does not declare all contract-owned responsibilities", messages
        )
        self.assertIn(
            "adapter does not explicitly preserve all contract delegations", messages
        )
        self.assertTrue(all(v["severity"] == "WARN" for v in violations))

    def test_overclaiming_delegated_responsibility_is_error(self):
        violations = self.boundary_violations("overclaim-boundary")
        errors = [violation for violation in violations if violation["severity"] == "ERROR"]
        self.assertEqual(1, len(errors))
        self.assertIn("product_policy", errors[0]["missing"])

    def test_unknown_boundary_claim_is_warning(self):
        violations = self.boundary_violations("unknown-boundary")
        warnings = [violation for violation in violations if violation["severity"] == "WARN"]
        self.assertEqual(1, len(warnings))
        self.assertIn("invented_capability", warnings[0]["missing"])

    def test_existing_gate_input_output_checks_still_run(self):
        skill = self.skill("valid-boundary")
        skill["content_lower"] = ""
        skill["body_lower"] = ""
        violations = module.check_conformance(self.contract, skill, "fixture")
        types = {violation["type"] for violation in violations}
        self.assertTrue({"quality_gates", "inputs", "outputs"}.issubset(types))


if __name__ == "__main__":
    unittest.main()
