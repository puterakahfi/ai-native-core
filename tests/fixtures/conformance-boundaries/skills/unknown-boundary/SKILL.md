---
name: unknown-boundary
description: Fixture adapter with an undeclared contract boundary item.
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/test/boundary-sample.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["owned_capability", "owned_review", "invented_capability"]'
  ai-native-skills.boundary.delegates: '["provider_configuration", "product_policy"]'
---

# Unknown boundary fixture

Handles `contract_input`, produces `contract_output`, and enforces
`contract_gate_is_enforced`.

This fixture intentionally declares a boundary item that the contract does not define.
