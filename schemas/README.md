# Schemas

**Status: Planned**

This directory will contain JSON Schema or YAML Schema definitions for validating contracts programmatically.

Planned schemas:

```text
schemas/
├── skill-contract.schema.yaml      # validates contracts/skills/**/*.contract.yaml
├── workflow-contract.schema.yaml   # validates contracts/workflows/*.contract.yaml
├── test-contract.schema.yaml       # validates contracts/tests/*.test.yaml
└── runtime-contract.schema.yaml    # validates contracts/runtime/*.contract.yaml
```

Until schemas are formalized, contracts follow the structure documented in the root README under **Contract Format**.
