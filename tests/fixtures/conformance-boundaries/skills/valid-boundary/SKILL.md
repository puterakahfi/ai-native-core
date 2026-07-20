---
name: valid-boundary
description: Fixture adapter with complete boundary declarations.
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/test/boundary-sample.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["owned_capability", "owned_review"]'
  ai-native-skills.boundary.delegates: '["provider_configuration", "product_policy"]'
---

# Valid boundary fixture

Handles `contract_input`, produces `contract_output`, and enforces
`contract_gate_is_enforced`.

Implements the owned capability and review while delegating provider
configuration and product policy.
