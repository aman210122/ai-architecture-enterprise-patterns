# AI Architecture Enterprise Patterns

**222+ interactive SVG architecture diagrams for enterprise AI. Click any component for full details. Run scenarios to watch data flow through the architecture.**
![Interactive Architecture Demo](demo.gif)

Every diagram includes: spatial box-and-arrow layout, click-to-detail panels (configuration, platform mapping, anti-patterns, GAIF-4 relevance), 5 animated scenarios, 4 cross-cutting governance bars, and per-query cost tracking.

Governance: [GAIF Governance Observatory](https://github.com/aman210122/gaif-governance-observatory) | Author: [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)

---

## Patterns

### Foundation Layer

| # | Pattern | Variants | What It Answers |
|---|---------|----------|-----------------|
| 01 | [Unified AI Gateway](patterns/01-unified-ai-gateway/) | 14 | How do I route all LLM traffic through a single control point? |
| 02 | [RAG for Regulated Data](patterns/02-rag-regulated-data/) | 12 | How do I build retrieval-augmented generation with compliance? |
| 03 | [Multi-Agent Safety Gates](patterns/03-multi-agent-safety-gates/) | 12 | How do I chain agents with safety checkpoints between each? |
| 04 | [Agentic Tool Governance](patterns/04-agentic-tool-governance/) | 9 | How do I govern what agents can DO, not just what they say? |

### Operations Layer

| # | Pattern | Variants | What It Answers |
|---|---------|----------|-----------------|
| 05 | [LLMOps Pipeline](patterns/05-llmops-pipeline/) | 12 | How do I manage the full lifecycle of LLMs in production? |
| 06 | [Governance-as-Architecture](patterns/06-governance-as-architecture/) | 15 | How do I embed governance in architecture, not in PDFs? |
| 07 | [Contamination-Resistant Pipeline](patterns/07-contamination-resistant-pipeline/) | 12 | How do I prevent contamination in multi-agent systems? |
| 08 | [Compliance-Aware Routing](patterns/08-compliance-aware-routing/) | 14 | How do I route PHI/PII data to the right endpoints? |

### Quality and Economics Layer

| # | Pattern | Variants | What It Answers |
|---|---------|----------|-----------------|
| 09 | [AI Evaluation and Red Teaming](patterns/09-ai-evaluation-red-teaming/) | 15 | How do I test AI quality, safety, and bias systematically? |
| 10 | [FinOps for AI](patterns/10-finops-for-ai/) | 14 | How do I track, optimize, and allocate AI costs? |

### Infrastructure Layer

| # | Pattern | Variants | What It Answers |
|---|---------|----------|-----------------|
| 11 | [AI Security Architecture](patterns/11-ai-security-architecture/) | 12 | How do I defend against AI-specific threats? |
| 12 | [Enterprise AI Platform](patterns/12-enterprise-ai-platform/) | 15 | What infrastructure do all AI patterns run on? |

### Intelligence Layer

| # | Pattern | Variants | What It Answers |
|---|---------|----------|-----------------|
| 13 | [Observability for AI](patterns/13-observability-for-ai/) | 14 | How do I know if my AI systems are working well? |
| 14 | [AI Product Architecture](patterns/14-ai-product-architecture/) | 12 | What does a complete AI product look like? |
| 15 | [Migration and Interoperability](patterns/15-migration-interoperability/) | 12 | How do I migrate AI systems across clouds and providers? |
| 16 | [Agent Memory Architecture](patterns/16-agent-memory-architecture/) | 12 | How do agents remember across sessions with governance? |
| 17 | [Data Sovereignty and Local-First AI](patterns/17-data-sovereignty-local-first/) | 12 | Where should AI computation happen? |
| 18 | [AI Resilience Engineering](patterns/18-ai-resilience-engineering/) | 12 | How do AI systems fail and recover differently? |

---

## How Patterns Compose Together

```
                    [14. AI Products]
                    Conversational AI, Search, Copilot, CDSS
                           |
              uses patterns 02-13 + 16 as building blocks
                           |
    +----------+-----------+----------+-----------+----------+
    |          |           |          |           |          |
[02. RAG] [03. Agents] [04. Tools] [05. LLMOps] [16. Memory]
    |          |           |          |           |
    +----------+-----------+----------+-----------+
                           |
              governed and secured by
                           |
    +----------+-----------+----------+-----------+
    |          |           |          |           |
[06. Gov]  [07. Contam] [08. Comply] [10. FinOps] [11. Security]
    |          |           |          |           |
    +----------+-----------+----------+-----------+
                           |
              resilient, observable, and hosted on
                           |
    +----------+-----------+----------+-----------+----------+
    |          |           |          |           |          |
[01. GW]  [12. Platform] [13. Observe] [15. Migrate] [17. Sov] [18. Resilience]
                                       [09. Eval]
```

---

## GAIF-4 Governance Metrics

| Metric | What It Measures | Safe | Critical |
|--------|-----------------|------|----------|
| **T1PR** (Type-1 Pass Rate) | Contaminated/bad outputs passing safety filters | < 0.05 | > 0.15 |
| **CFR** (Compliance Failure Rate) | Outputs violating compliance policies | 0.00 | > 0.01 |
| **EMR** (Emergent Misinformation Rate) | Dangerous content emerging at pipeline level | < 0.05 | > 0.15 |
| **GDR** (Governance Decay Rate) | Governance effectiveness degrading over time | < 0.03 | > 0.05 |

---

## Platform Mapping

| Component | Databricks | Azure | AWS | GCP | Open Source |
|-----------|-----------|-------|-----|-----|-------------|
| Gateway | Mosaic AI GW | API Mgmt | API GW | Apigee | Kong / Envoy |
| Vector | Vector Search | AI Search | OpenSearch | Vertex Search | Qdrant |
| LLM | DBRX / External | Azure OpenAI | Bedrock | Gemini | vLLM |
| Agents | Mosaic AI Agents | Semantic Kernel | Bedrock Agents | Agent Builder | LangGraph |
| Tools | UC Functions | Azure Functions | Lambda | Cloud Functions | MCP SDK |
| Guardrails | Mosaic GW | Content Safety | Guardrails | Model Armor | NeMo |
| Eval | MLflow Eval | AI Foundry Eval | Bedrock Eval | Vertex Eval | RAGAS |
| DLP | Presidio | Purview | Macie | Cloud DLP | Presidio |
| Observe | MLflow | App Insights | CloudWatch | Cloud Monitoring | OTel |
| Compute | Serverless | AI Foundry | SageMaker | Vertex AI | K8s + vLLM |

---

## Research Basis

| Pattern | Research | Finding |
|---------|----------|---------|
| P07 | [EMG Paper](https://doi.org/10.5281/zenodo.19411743) | 74 critical drug interactions across 4,800 trials; collective delusion; gap inversion |
| P07 | ContamPerc Paper | Contamination percolation in multi-agent graphs; T1PR metric |
| P08 | [PHI-GUARD Paper](https://doi.org/10.36227/techrxiv.177220388.80392106/v1) | CARES algorithm; zero PHI violations across 30K MIMIC-IV queries |
| All | [GAIF v1.0](https://doi.org/10.5281/zenodo.19341015) | Governance framework with T1PR, CFR, EMR, GDR metrics |

---

## Getting Started

**For CTOs:** Glance at the spatial diagram. Architecture tells the story in 10 seconds.

**For Architects:** Click any component for configuration, platform mapping, anti-patterns, GAIF-4 relevance.

**For Engineers:** Run scenarios. Watch data flow. Read the log for technical details.

**For Security/Compliance:** Focus on Governance bars. Run PHI and contamination scenarios.

**For FinOps:** Read cost in response bar. Compare scenarios. Check Economics bar.

---

## License

MIT

*Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect) | Principal Enterprise Architect AI/ML*
*Governance: [GAIF Governance Observatory](https://github.com/aman210122/gaif-governance-observatory)*
