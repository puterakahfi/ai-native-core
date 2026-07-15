# Native AI Framework Principles

These principles define how AI-native engineering should work inside this framework.

## 1. System Thinking Over Prompt Tricks

Do not rely on clever prompts alone. Build repeatable systems with clear inputs, processes, outputs, review gates, and feedback loops.

## 2. Architecture Over Code Generation

Code generation is not the starting point. Architecture, domain modeling, constraints, and contracts must guide implementation.

## 3. Context Over Tokens

The quality of AI execution depends on structured context, not just larger context windows.

## 4. Knowledge Over Memory

Memory is useful for history. Knowledge is the source of truth.

Product facts, domain rules, architecture decisions, and technical references should live in explicit knowledge artifacts.

## 5. Blueprint Over Improvisation

Agents should not invent systems from vague prompts. They should execute from product blueprints and engineering contracts.

## 6. Rules Over Random Output

Rules define constraints that protect consistency, security, maintainability, and product quality.

## 7. Skills Over Generic Prompting

A skill is a reusable execution procedure. Agents should use skills when performing repeatable engineering work.

## 8. Agent Collaboration Over One Super-Agent

Different responsibilities should be separated across agent roles: product, planning, architecture, building, testing, review, security, and documentation.

## 9. Evaluation Over Blind Automation

Every generated output must be evaluated against quality gates before being accepted.

## 10. Human Review Over Full Autopilot

The default mode is human-in-the-loop. Fully automated publishing, deployment, or destructive operations require explicit approval.

## 11. Long-Term Maintainability Over Quick Demos

The framework prioritizes systems that can be maintained, reviewed, extended, and reused.

## 12. Productization Over One-Off Output

Every useful workflow should be designed so it can become a reusable asset, internal tool, automation template, digital product, or SaaS feature.
