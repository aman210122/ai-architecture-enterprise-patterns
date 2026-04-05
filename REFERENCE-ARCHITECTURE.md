# Enterprise AI Reference Architecture

**How all 10 patterns compose into a complete platform. Use this guide to understand dependencies, implementation sequence, and which patterns to start with.**

## Architecture Layers

```
  Layer 5: Business Value
  +-----------------------------------------------------------------+
  | Pattern 10: FinOps for AI                                       |
  | ROI measurement, cost optimization, chargeback, capacity plan   |
  +-----------------------------------------------------------------+

  Layer 4: Quality & Safety
  +-----------------------------------------------------------------+
  | Pattern 09: Evaluation    | Pattern 07: Contamination-Resistant |
  | Red teaming, benchmarks,  | Isolation, validation, rollback,   |
  | regression, compliance    | percolation detection, immune sys  |
  +-----------------------------------------------------------------+

  Layer 3: Governance (spans all layers)
  +-----------------------------------------------------------------+
  | Pattern 06: Governance-as-Architecture                          |
  | GAIF-4 metrics, policy-as-code, audit trail, risk-tiered,      |
  | decay detection, maturity model, bias, explainability           |
  +-----------------------------------------------------------------+

  Layer 2: Operations
  +-----------------------------------------------------------------+
  | Pattern 05: LLMOps       | Pattern 08: Compliance Routing      |
  | CI/CD, deploy, monitor,  | Data classification, residency,    |
  | prompt eng, A/B testing   | consent, cross-border, anonymize   |
  +-----------------------------------------------------------------+

  Layer 1: Runtime Intelligence
  +-----------------------------------------------------------------+
  | Pattern 02: RAG     | Pattern 03: Agents  | Pattern 04: Tools  |
  | 12 retrieval archs  | 11 topologies       | 9 tool protocols   |
  +-----------------------------------------------------------------+

  Layer 0: Foundation
  +-----------------------------------------------------------------+
  | Pattern 01: Unified AI Gateway                                  |
  | All LLM traffic through one governance-aware control plane      |
  +-----------------------------------------------------------------+
```

## Implementation Sequence

### Phase 1: Foundation (Month 1-2)
**Start here. Everything else builds on this.**

1. **Pattern 01: Unified AI Gateway** - Deploy your gateway first. All LLM traffic must route through it before you can govern anything. Start with the [Starter](patterns/01-unified-ai-gateway/starter/) variant and graduate to your cloud-native variant.

2. **Pattern 08: Compliance Routing** - Wire up data classification early. Start with [Sensitivity Classification](patterns/08-compliance-data-routing/sensitivity-classification/) engine. Without classification, you cannot route.

### Phase 2: First Use Cases (Month 2-4)
**Build your first production AI capability.**

3. **Pattern 02: RAG** - Most enterprises start with RAG. Pick the variant matching your data. [Standard RAG](patterns/02-rag-regulated-data/standard-rag/) for internal knowledge, [Sensitive Data RAG](patterns/02-rag-regulated-data/sensitive-data-rag/) if you handle PHI/PII.

4. **Pattern 05: LLMOps** - Deploy your first RAG through a proper pipeline. Start with your cloud variant. Add [Prompt Engineering](patterns/05-llmops-pipeline/prompt-engineering/) for fast iteration.

### Phase 3: Governance (Month 3-5)
**Formalize governance before scaling.**

5. **Pattern 06: Governance** - Start with [Governance Maturity Model](patterns/06-governance-as-architecture/governance-maturity/) to assess where you are. Implement [Embedded Governance](patterns/06-governance-as-architecture/embedded-governance/) with GAIF-4 metrics. Add [Risk-Tiered](patterns/06-governance-as-architecture/risk-tiered/) for proportional controls.

6. **Pattern 09: Evaluation** - Establish quality baselines. Start with [RAGAS](patterns/09-evaluation-red-teaming/ragas-evaluation/) for RAG quality and [Safety Benchmarking](patterns/09-evaluation-red-teaming/safety-benchmarking/) before production.

### Phase 4: Advanced Capabilities (Month 5-8)
**Add agents, tools, and advanced patterns.**

7. **Pattern 03: Multi-Agent** - Start with [Linear Chain](patterns/03-multi-agent-safety-gates/linear-chain/) and graduate to more complex topologies as needed.

8. **Pattern 04: Tool Governance** - When agents need tools. Start with [Function Calling](patterns/04-agentic-tool-governance/function-calling/) and add [MCP](patterns/04-agentic-tool-governance/mcp-protocol/) as tools standardize.

9. **Pattern 07: Contamination** - Critical once you have multi-agent pipelines. Start with [Validation Checkpoints](patterns/07-contamination-resistant-pipeline/validation-checkpoints/) and add [Contamination Percolation](patterns/07-contamination-resistant-pipeline/contamination-percolation/) monitoring.

### Phase 5: Optimization (Month 6+)
**Optimize cost and prove value.**

10. **Pattern 10: FinOps** - Once you have production usage, start with [Token-Level](patterns/10-finops-for-ai/token-level-finops/) attribution and [ROI Measurement](patterns/10-finops-for-ai/roi-measurement/) to prove business value.

## Pattern Dependencies

| Pattern | Depends On | Feeds Into |
|---------|-----------|------------|
| 01: Gateway | None (foundation) | Everything |
| 02: RAG | 01 (gateway routes traffic) | 05 (deployed via LLMOps) |
| 03: Agents | 01 (gateway), 04 (tools) | 07 (needs contamination defense) |
| 04: Tools | 01 (gateway authorizes) | 03 (agents use tools) |
| 05: LLMOps | 01 (deploys through gateway) | 02, 03 (deploys all use cases) |
| 06: Governance | None (spans all) | All patterns |
| 07: Contamination | 03 (protects agent pipelines) | 06 (feeds governance metrics) |
| 08: Compliance | 01 (gateway classifies) | 02, 03 (routing decisions) |
| 09: Evaluation | 02, 03 (evaluates outputs) | 05 (gates deployments) |
| 10: FinOps | 01 (tracks usage) | 06 (cost governance) |

## Minimum Viable Enterprise AI Platform

If you can only implement 4 patterns to start, pick these:

1. **Pattern 01** - Gateway (foundation)
2. **Pattern 02** - RAG (first use case)
3. **Pattern 06** - Governance (compliance)
4. **Pattern 05** - LLMOps (operations)

These 4 give you: governed traffic routing, a production RAG pipeline, quantitative governance metrics, and CI/CD for AI. Everything else adds depth.

---

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
