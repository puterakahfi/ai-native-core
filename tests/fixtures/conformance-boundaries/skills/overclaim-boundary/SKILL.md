---
name: overclaim-boundary
description: Fixture adapter that incorrectly claims delegated responsibility.
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/test/boundary-sample.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["owned_capability", "owned_review", "product_policy"]'
  ai-native-skills.boundary.delegates: '["provider_configuration"]'
---

# Overclaim boundary fixture

Handles `contract_input`, produces `contract_output`, and enforces
`contract_gate_is_enforced`.

This fixture intentionally claims product policy even though the contract delegates it.
