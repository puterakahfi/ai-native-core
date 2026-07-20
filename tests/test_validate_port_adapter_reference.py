from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-port-adapter-reference.py"
FIXTURES = ROOT / "tests" / "fixtures" / "port-adapter-references"
VALID = FIXTURES / "valid-model-inference.port-reference.yaml"
INCOMPATIBLE = FIXTURES / "incompatible-model-inference.port-reference.yaml"

spec = importlib.util.spec_from_file_location("validate_port_adapter_reference", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class PortAdapterReferenceTests(unittest.TestCase):
    def write_mutated_reference(self, mutate) -> Path:
        payload = yaml.safe_load(VALID.read_text())
        mutate(payload["port_adapter_reference"])
        path = Path(tempfile.mkdtemp()) / "reference.yaml"
        path.write_text(yaml.safe_dump(payload, sort_keys=False))
        return path

    def test_valid_reference_resolves_id_path_and_compatible_version(self):
        self.assertEqual([], module.validate_reference(VALID, root=ROOT))

    def test_incompatible_version_pin_fails(self):
        errors = module.validate_reference(INCOMPATIBLE, root=ROOT)
        self.assertTrue(any("incompatible" in error for error in errors), errors)

    def test_port_id_mismatch_fails(self):
        path = self.write_mutated_reference(
            lambda reference: reference.__setitem__("port_id", "repository")
        )
        errors = module.validate_reference(path, root=ROOT)
        self.assertTrue(any("port_id mismatch" in error for error in errors), errors)

    def test_path_outside_port_contract_tree_fails(self):
        path = self.write_mutated_reference(
            lambda reference: reference.__setitem__(
                "port_path", "contracts/skills/runtime/model-selection.contract.yaml"
            )
        )
        errors = module.validate_reference(path, root=ROOT)
        self.assertTrue(any("under contracts/ports" in error for error in errors), errors)

    def test_caret_zero_minor_pin_matches_only_same_minor_line(self):
        self.assertTrue(module.pin_accepts("^0.1.0", "0.1.9"))
        self.assertFalse(module.pin_accepts("^0.1.0", "0.2.0"))

    def test_tilde_pin_matches_same_major_minor_line(self):
        self.assertTrue(module.pin_accepts("~1.2", "1.2.9"))
        self.assertFalse(module.pin_accepts("~1.2", "1.3.0"))

    def test_cli_passes_for_valid_reference(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(VALID)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("stable ID", result.stdout)

    def test_cli_fails_for_incompatible_reference(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(INCOMPATIBLE)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("incompatible", result.stdout)


if __name__ == "__main__":
    unittest.main()
