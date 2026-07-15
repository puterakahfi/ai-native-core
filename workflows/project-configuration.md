# Workflow: Project Configuration

## Purpose

Define the source-of-truth configuration for a project inside the Native AI Framework.

Project configuration connects product context, domain model, engineering contract, port map, adapter map, rules, review gates, and risk policy.

## Input

```text
project_metadata
framework_version
source_of_truth_files
domain_contexts
default_ports
default_adapters
required_rules
review_gates
risk_policy
```

## Process

```text
1. Define project metadata
2. Link framework version
3. Register source-of-truth files
4. Register domain contexts
5. Register default ports
6. Register default adapters
7. Register required rules
8. Register review gates
9. Register risk policy
10. Validate configuration
11. Connect context pack
```

## Output Files

```text
products/{project}/project.config.yaml
context-packs/{project}.yaml
products/{project}/adapter-map.md
products/{project}/port-map.md
```

## Configuration Responsibilities

Project config should answer:

```text
What project is this?
What framework version does it use?
What is the source of truth?
What is the core domain?
What bounded contexts exist?
What ports are available?
What adapters are selected by default?
What rules are mandatory?
What review gates are required?
What decisions require approval or ADR?
```

## Review Gates

```text
architecture_review
contract_review
port_adapter_review
risk_policy_review
```

## Done Criteria

- [ ] Project metadata exists.
- [ ] Framework version is defined.
- [ ] Source-of-truth files are linked.
- [ ] Core domain is defined.
- [ ] Bounded contexts are listed.
- [ ] Default ports are registered.
- [ ] Default adapters are registered.
- [ ] Required rules are listed.
- [ ] Review gates are listed.
- [ ] Risk policy is defined.
- [ ] Context pack is linked.

## Anti-Pattern

Do not let each adapter decide its own project context.

Correct flow:

```text
Project Config -> Context Pack -> Task Contract -> Adapter Execution -> Review
```
