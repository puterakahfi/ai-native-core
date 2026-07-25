from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
import artifact_eval


class ArtifactEvalTests(unittest.TestCase):
    def test_text_only_case_remains_unchanged(self):
        legacy = SimpleNamespace()
        legacy.validate_test_document = lambda document, path, expected_skill=None: None
        legacy.run_case = lambda case, output: {
            "classification": "APPLIED", "verdict": "APPLIED", "failures": []
        }
        artifact_eval.install(legacy, Path("."))
        result = legacy.run_case({"id": "case"}, "output")
        self.assertEqual("APPLIED", result["classification"])
        self.assertIsNone(result["artifact_assertions"])

    def test_compliant_fixture_passes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            fixture = base / "fixture"
            (fixture / "components").mkdir(parents=True)
            (fixture / "components/button.tsx").write_text(
                'import { cn } from "@/lib/utils"\n', encoding="utf-8"
            )
            assertions = artifact_eval.validate_assertions({
                "root": "fixture",
                "files_must_exist": ["components/button.tsx"],
                "files_must_not_exist": ["components/local-dialog.tsx"],
                "path_globs_must_match": ["components/*.tsx"],
                "file_patterns_must_contain": [
                    {"path": "components/button.tsx", "pattern": "@/lib/utils"}
                ],
                "file_patterns_must_not_contain": [
                    {"path": "components/button.tsx", "pattern": "another-ui"}
                ],
            }, "artifact_assertions")
            result = artifact_eval.execute(assertions, base)
            self.assertEqual([], result["failures"])
            self.assertFalse(result["missing_evidence"])
            self.assertFalse(result["forbidden_hit"])

    def test_forbidden_pattern_is_detected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            fixture = base / "fixture"
            fixture.mkdir()
            (fixture / "page.tsx").write_text(
                'import { Dialog } from "another-ui"\n', encoding="utf-8"
            )
            assertions = artifact_eval.validate_assertions({
                "root": "fixture",
                "file_patterns_must_not_contain": [
                    {"path": "page.tsx", "pattern": "another-ui"}
                ],
            }, "artifact_assertions")
            result = artifact_eval.execute(assertions, base)
            self.assertTrue(result["forbidden_hit"])
            self.assertTrue(result["failures"])

    def test_missing_root_is_missing_evidence(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            assertions = artifact_eval.validate_assertions({
                "root": "missing",
                "files_must_exist": ["page.tsx"],
            }, "artifact_assertions")
            result = artifact_eval.execute(assertions, Path(temp_dir))
            self.assertTrue(result["missing_evidence"])

    def test_path_escape_is_rejected(self):
        with self.assertRaises(artifact_eval.ArtifactContractError):
            artifact_eval.validate_assertions({
                "root": "../escape",
                "files_must_exist": ["page.tsx"],
            }, "artifact_assertions")

    def test_absolute_command_is_rejected(self):
        with self.assertRaises(artifact_eval.ArtifactContractError):
            artifact_eval.validate_assertions({
                "root": "fixture",
                "command_evidence": [{"argv": ["/bin/sh", "-c", "exit 0"]}],
            }, "artifact_assertions")

    def test_command_is_disabled_by_default(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            fixture = base / "fixture"
            fixture.mkdir()
            validator = fixture / "validator"
            validator.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            validator.chmod(0o755)
            assertions = artifact_eval.validate_assertions({
                "root": "fixture",
                "command_evidence": [{"argv": ["validator"]}],
            }, "artifact_assertions")
            result = artifact_eval.execute(assertions, base)
            self.assertTrue(result["missing_evidence"])

    def test_fixture_local_command_can_be_enabled(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            fixture = base / "fixture"
            fixture.mkdir()
            validator = fixture / "validator"
            validator.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            validator.chmod(0o755)
            assertions = artifact_eval.validate_assertions({
                "root": "fixture",
                "command_evidence": [{"argv": ["validator"]}],
            }, "artifact_assertions")
            result = artifact_eval.execute(assertions, base, allow_commands=True)
            self.assertEqual([], result["failures"])


if __name__ == "__main__":
    unittest.main()
