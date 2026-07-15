# Port Adapter Boundary Rule

## Purpose

Keep product domain logic independent from replaceable implementation tools.

## Applies To

- Model provider integration
- Code execution tool integration
- Design tool integration
- Web application framework choice
- Storage provider integration
- Database provider integration
- Publishing integration
- Tool integration

## Must Do

1. Describe required capability as a port.
2. Implement the capability through an adapter.
3. Keep domain model independent from adapter details.
4. Keep business rules outside tool-specific code.
5. Make adapter choices explicit in the Engineering Contract.
6. Use ADR for major adapter changes.
7. Define adapter input, output, limitation, failure behavior, and risk level.
8. Review adapter output before accepting it as final product output.

## Must Not Do

1. Do not make one tool the framework core.
2. Do not let adapters define product rules.
3. Do not put provider SDK logic inside domain entities.
4. Do not couple prompt flow to one model without abstraction.
5. Do not skip human approval for high-risk adapter actions.
6. Do not treat tool output as automatically approved.

## Port Examples

```text
CodeExecutionPort
DesignGenerationPort
DesignReviewPort
ModelInferencePort
KnowledgeRetrievalPort
RepositoryPort
DatabasePort
StoragePort
PublishingPort
EvaluationPort
ObservabilityPort
```

## Review Checklist

- [ ] Required capability is described as a port.
- [ ] Adapter is explicit.
- [ ] Domain does not depend on adapter details.
- [ ] Adapter risk level is known.
- [ ] Failure behavior is defined.
- [ ] Major adapter change has ADR.
- [ ] Output is reviewed before acceptance.

## ExampleProduct Example

ExampleProduct domain concepts should remain stable:

```text
Brand
IdentityLock
Campaign
CampaignBrief
CreativeDirection
GeneratedAsset
CreativeReview
Approval
Export
```

The tools that implement code, design, model inference, storage, and publishing may change without changing the domain model.
