from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from contract_resolution import (
    load_contract_document,
    pin_accepts,
    resolve_contract_reference,
)


class ContractResolutionTests(unittest.TestCase):
    def test_direct_manifest_path_resolves(self):
        resolution = resolve_contract_reference(
            ROOT, "ai-native-core/contracts/ports/integration/model-inference.port.yaml"
        )
        self.assertIsNotNone(resolution)
        assert resolution is not None
        self.assertEqual(
            "contracts/ports/integration/model-inference.port.yaml",
            resolution["canonical_path"],
        )
        self.assertIsNone(resolution["alias"])
        self.assertEqual("port_contract", resolution["entry"]["kind"])

    def test_legacy_workflow_paths_resolve_to_canonical_targets(self):
        expected = {
            "contracts/skills/quality/design-refinement.contract.yaml":
                "contracts/workflows/design-refinement.contract.yaml",
            "contracts/skills/quality/redesign-workflow.contract.yaml":
                "contracts/workflows/redesign-workflow.contract.yaml",
            "contracts/skills/quality/skill-evolution.contract.yaml":
                "contracts/workflows/skill-evolution.contract.yaml",
            "contracts/runtime/development-loop.contract.yaml":
                "contracts/workflows/development-loop.contract.yaml",
        }
        for legacy, canonical in expected.items():
            with self.subTest(legacy=legacy):
                resolution = resolve_contract_reference(ROOT, legacy)
                self.assertIsNotNone(resolution)
                assert resolution is not None
                self.assertEqual(canonical, resolution["canonical_path"])
                self.assertIsNotNone(resolution["alias"])
                self.assertEqual("workflow_contract", resolution["entry"]["kind"])

    def test_contract_document_loader_uses_declared_family_root(self):
        path = ROOT / "contracts" / "workflows" / "design-refinement.contract.yaml"
        kind, body, document = load_contract_document(path)
        self.assertEqual("workflow_contract", kind)
        self.assertEqual("design-refinement", body["id"])
        self.assertIn("contract_schema", document)

    def test_semver_pin_compatibility(self):
        self.assertTrue(pin_accepts("^1.2.0", "1.9.0"))
        self.assertFalse(pin_accepts("^1.2.0", "2.0.0"))
        self.assertTrue(pin_accepts("^0.1.0", "0.1.9"))
        self.assertFalse(pin_accepts("^0.1.0", "0.2.0"))
        self.assertTrue(pin_accepts("~2.2", "2.2.7"))
        self.assertFalse(pin_accepts("~2.2", "2.3.0"))

    def test_implements_cli_accepts_active_legacy_alias(self):
        workspace = Path(tempfile.mkdtemp())
        skill = workspace / "skills" / "fixture" / "SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text(
            """---
name: fixture
description: Fixture adapter for alias resolution.
metadata:
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-refinement.contract.yaml
  ai-native-skills.contract-version: ^1.2.0
---

# Fixture
"""
        )
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate-implements.py"), str(ROOT)],
            cwd=workspace,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("ALIAS:", result.stdout)
        self.assertIn("contracts/workflows/design-refinement.contract.yaml", result.stdout)

    def test_conformance_parser_accepts_workflow_contract_family(self):
        path = SCRIPTS / "validate-conformance.py"
        spec = importlib.util.spec_from_file_location("validate_conformance", path)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)

        parsed = module.parse_contract(
            ROOT / "contracts" / "workflows" / "design-refinement.contract.yaml"
        )
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual("workflow_contract", parsed["kind"])
        self.assertEqual("design-refinement", parsed["id"])
        self.assertTrue(parsed["quality_gates"])


if __name__ == "__main__":
    unittest.main()
