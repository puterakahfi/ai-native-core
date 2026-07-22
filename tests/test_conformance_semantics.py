from __future__ import annotations

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
FIXTURES = ROOT / "tests" / "fixtures" / "conformance-boundaries"
SCRIPT = SCRIPTS / "validate-conformance.py"

spec = importlib.util.spec_from_file_location("validate_conformance", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ConformanceSemanticTests(unittest.TestCase):
    def workspace(self):
        root = Path(tempfile.mkdtemp())
        core = root / "core"
        adapters = root / "adapters"
        shutil.copytree(FIXTURES / "core" / "contracts", core / "contracts")
        shutil.copytree(ROOT / "schemas", core / "schemas")
        skill_dir = adapters / "skills" / "valid-boundary"
        skill_dir.mkdir(parents=True)
        shutil.copy2(
            FIXTURES / "skills" / "valid-boundary" / "SKILL.md",
            skill_dir / "SKILL.md",
        )
        shutil.copy2(
            FIXTURES / "skills" / "valid-boundary" / module.DECLARATION,
            skill_dir / module.DECLARATION,
        )
        return root, core, adapters, skill_dir

    def mutate_contract(self, core: Path, mutate):
        path = (
            core
            / "contracts"
            / "skills"
            / "test"
            / "boundary-sample.contract.yaml"
        )
        payload = yaml.safe_load(path.read_text())
        mutate(payload["skill_contract"])
        path.write_text(yaml.safe_dump(payload, sort_keys=False))

    def mutate_declaration(self, skill_dir: Path, mutate):
        path = skill_dir / module.DECLARATION
        payload = yaml.safe_load(path.read_text())
        mutate(payload["adapter_conformance"])
        path.write_text(yaml.safe_dump(payload, sort_keys=False))

    def validate(self, core: Path, adapters: Path, skill_dir: Path):
        return module.validate_structured(
            core,
            adapters,
            skill_dir / "SKILL.md",
            skill_dir / module.DECLARATION,
        )

    def test_allowed_output_subset_is_conformant(self):
        root, core, adapters, skill_dir = self.workspace()
        try:
            self.mutate_contract(
                core,
                lambda body: body["outputs"]["allowed"].append("optional_output"),
            )
            result = self.validate(core, adapters, skill_dir)
            self.assertEqual("CONFORMANT", result["structural_status"])
            self.assertNotIn(
                "OUTPUT_COVERAGE_MISSING",
                {finding["code"] for finding in result["findings"]},
            )
        finally:
            shutil.rmtree(root)

    def test_required_output_gap_is_partial(self):
        root, core, adapters, skill_dir = self.workspace()
        try:
            def mutate(body):
                body["outputs"]["required"] = ["required_output"]
                body["outputs"]["allowed"].append("required_output")

            self.mutate_contract(core, mutate)
            result = self.validate(core, adapters, skill_dir)
            self.assertEqual("PARTIAL", result["structural_status"])
            self.assertIn(
                "REQUIRED_OUTPUT_MISSING",
                {finding["code"] for finding in result["findings"]},
            )
        finally:
            shutil.rmtree(root)

    def test_dependencies_handoffs_and_adapter_requirements_are_checked(self):
        root, core, adapters, skill_dir = self.workspace()
        try:
            def mutate(body):
                body["dependencies"] = ["required_dependency"]
                body["handoffs"] = ["review_handoff"]
                body["adapter_requirements"] = {
                    "provider_binding": "product_defined"
                }

            self.mutate_contract(core, mutate)
            partial = self.validate(core, adapters, skill_dir)
            self.assertEqual("PARTIAL", partial["structural_status"])
            codes = {finding["code"] for finding in partial["findings"]}
            self.assertTrue(
                {
                    "DEPENDENCIES_MISSING",
                    "HANDOFFS_MISSING",
                    "ADAPTER_REQUIREMENTS_MISSING",
                }.issubset(codes)
            )

            self.mutate_declaration(
                skill_dir,
                lambda body: body.update(
                    {
                        "dependencies": ["required_dependency"],
                        "handoffs": ["review_handoff"],
                        "adapter_requirements": ["provider_binding"],
                    }
                ),
            )
            complete = self.validate(core, adapters, skill_dir)
            self.assertEqual("CONFORMANT", complete["structural_status"])
        finally:
            shutil.rmtree(root)

    def test_adapter_specific_extensions_are_diagnostic_not_contract_overclaim(self):
        root, core, adapters, skill_dir = self.workspace()
        try:
            self.mutate_declaration(
                skill_dir,
                lambda body: body.update(
                    {
                        "dependencies": ["adapter_specific_dependency"],
                        "handoffs": ["adapter_specific_handoff"],
                        "adapter_requirements": ["adapter_specific_requirement"],
                    }
                ),
            )
            result = self.validate(core, adapters, skill_dir)
            self.assertEqual("CONFORMANT", result["structural_status"])
            codes = {
                finding["code"] for finding in result["migration_diagnostics"]
            }
            self.assertTrue(
                {
                    "ADAPTER_SPECIFIC_DEPENDENCIES",
                    "ADAPTER_SPECIFIC_HANDOFFS",
                    "ADAPTER_SPECIFIC_ADAPTER_REQUIREMENTS",
                }.issubset(codes)
            )
        finally:
            shutil.rmtree(root)

    def test_report_preserves_unknown_legacy_patterns(self):
        root, core, adapters, skill_dir = self.workspace()
        try:
            result = self.validate(core, adapters, skill_dir)
            result["adapter_patterns"].append("domain-reviewer")
            report = module.build_report(core, adapters, "migration", 1, [result])
            validator = module.validator_for(
                core / "schemas" / "conformance-report.schema.yaml",
                schemas_root=core / "schemas",
            )
            self.assertEqual([], list(validator.iter_errors(report)))
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
