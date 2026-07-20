---
name: partial-boundary
description: Fixture adapter with incomplete boundary declarations.
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/test/boundary-sample.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["owned_capability"]'
  ai-native-skills.boundary.delegates: '["provider_configuration"]'
---

# Partial boundary fixture

Handles `contract_input`, produces `contract_output`, and enforces
`contract_gate_is_enforced`.

This fixture intentionally declares only part of the owned and delegated boundary.
