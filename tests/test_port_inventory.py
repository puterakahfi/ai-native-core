from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "docs" / "port-inventory.yaml"
PORTS_ROOT = ROOT / "contracts" / "ports"
SKILLS_ROOT = ROOT / "contracts" / "skills"

DEDICATED_PORT_DOCS = {
    "docs/agent-runtime-port.md",
    "docs/workflow-orchestration-port.md",
    "docs/execution-run-port.md",
    "docs/review-approval-port.md",
    "docs/context-management-port.md",
    "docs/skill-management-port.md",
    "docs/rule-management-port.md",
    "docs/tool-integration-port.md",
}

GENERAL_DOCUMENT_NAMES = {
    "ModelInferencePort",
    "CodeExecutionPort",
    "DesignGenerationPort",
    "DesignReviewPort",
    "KnowledgeRetrievalPort",
    "RepositoryPort",
    "FileSystemPort",
    "BrowserResearchPort",
    "WebAppPort",
    "DatabasePort",
    "StoragePort",
    "PublishingPort",
    "EvaluationPort",
    "ObservabilityPort",
}


class PortInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        payload = yaml.safe_load(INVENTORY_PATH.read_text())
        cls.entries = payload["entries"]

    def entries_for_class(self, source_class: str) -> list[dict]:
        return [
            entry
            for entry in self.entries
            if entry["source_class"] == source_class
        ]

    def test_inventory_source_identities_are_unique(self):
        identities = [
            (entry["source_path"], entry["source_name"])
            for entry in self.entries
        ]
        self.assertEqual(len(identities), len(set(identities)))

    def test_inventory_source_paths_exist(self):
        missing = sorted(
            entry["source_path"]
            for entry in self.entries
            if not (ROOT / entry["source_path"]).exists()
        )
        self.assertEqual([], missing)

    def test_dedicated_port_document_inventory_is_complete(self):
        actual = {
            entry["source_path"]
            for entry in self.entries_for_class("dedicated_port_document")
        }
        self.assertEqual(DEDICATED_PORT_DOCS, actual)

    def test_contract_declared_composition_ports_are_completely_inventoried(self):
        discovered = set()
        for path in SKILLS_ROOT.rglob("*.contract.yaml"):
            payload = yaml.safe_load(path.read_text())
            contract = payload.get("skill_contract", {})
            if contract.get("type") == "port":
                discovered.add(path.relative_to(ROOT).as_posix())

        inventoried = {
            entry["source_path"]
            for entry in self.entries_for_class("skill_contract_type_port")
        }
        self.assertEqual(discovered, inventoried)

    def test_general_document_examples_are_classified(self):
        actual = {
            entry["source_name"]
            for entry in self.entries_for_class("general_document_example")
        }
        self.assertEqual(GENERAL_DOCUMENT_NAMES, actual)

    def test_migrated_entries_reference_existing_canonical_contracts(self):
        migrated = [
            entry for entry in self.entries if entry["lifecycle"] == "migrated"
        ]
        self.assertTrue(migrated)

        errors = []
        for entry in migrated:
            if not entry["canonical_contracts"]:
                errors.append(f"{entry['source_name']}: no canonical contracts")
                continue
            for contract_path in entry["canonical_contracts"]:
                path = ROOT / contract_path
                if not path.exists():
                    errors.append(
                        f"{entry['source_name']}: missing {contract_path}"
                    )
                elif not path.is_relative_to(PORTS_ROOT):
                    errors.append(
                        f"{entry['source_name']}: not under contracts/ports: "
                        f"{contract_path}"
                    )
        self.assertEqual([], errors)

    def test_non_migrated_entries_have_explicit_rationale(self):
        allowed = {"retired", "reclassified", "deferred"}
        errors = []
        for entry in self.entries:
            if entry["lifecycle"] == "migrated":
                continue
            if entry["lifecycle"] not in allowed:
                errors.append(
                    f"{entry['source_name']}: invalid lifecycle "
                    f"{entry['lifecycle']}"
                )
            if entry["canonical_contracts"]:
                errors.append(
                    f"{entry['source_name']}: non-migrated entry owns contracts"
                )
            if not str(entry.get("rationale", "")).strip():
                errors.append(f"{entry['source_name']}: missing rationale")
        self.assertEqual([], errors)

    def test_all_active_file_backed_sources_are_resolved(self):
        active_source_classes = {
            "dedicated_port_document",
            "skill_contract_type_port",
        }
        errors = []
        for entry in self.entries:
            if entry["source_class"] not in active_source_classes:
                continue
            if entry["lifecycle"] not in {"migrated", "retired"}:
                errors.append(
                    f"{entry['source_name']}: unresolved active source "
                    f"({entry['lifecycle']})"
                )
        self.assertEqual([], errors)

    def test_tool_integration_umbrella_is_retired(self):
        entry = next(
            entry
            for entry in self.entries
            if entry["source_name"] == "ToolIntegrationPort"
            and entry["source_class"] == "dedicated_port_document"
        )
        self.assertEqual("retired", entry["lifecycle"])
        self.assertEqual([], entry["canonical_contracts"])

    def test_product_surface_candidates_remain_deferred_without_fake_contracts(self):
        entry = next(
            entry
            for entry in self.entries
            if entry["source_name"] == "ProductSurfacePort candidates"
        )
        self.assertEqual("deferred", entry["lifecycle"])
        self.assertEqual([], entry["canonical_contracts"])
        self.assertEqual(
            [],
            list((PORTS_ROOT / "product-surface").glob("*.port.yaml")),
        )


if __name__ == "__main__":
    unittest.main()
