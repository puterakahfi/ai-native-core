---
name: missing-boundary
description: Fixture adapter without structured boundary declarations.
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/test/boundary-sample.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
---

# Missing boundary fixture

Handles `contract_input`, produces `contract_output`, and enforces
`contract_gate_is_enforced`.

This fixture intentionally omits structured boundary declarations.
