# Getting Started: Find Your Path

**126 visualizations can be overwhelming. Start here based on your role.**

## By Role

### CTO / VP of Engineering
**Your questions:** "Are we governing AI properly?" "What's our AI spend?" "Are we compliant?"

| Start With | Why |
|-----------|-----|
| [Governance Maturity Model](patterns/06-governance-as-architecture/governance-maturity/) | Assess where your org stands today |
| [Risk-Tiered Governance](patterns/06-governance-as-architecture/risk-tiered/) | EU AI Act alignment, proportional controls |
| [ROI Measurement](patterns/10-finops-for-ai/roi-measurement/) | Prove AI investments are paying off |
| [Budget Governance](patterns/10-finops-for-ai/budget-governance/) | Control AI spending across teams |
| [Compliance-Gated Deployment](patterns/05-llmops-pipeline/compliance-gated/) | Regulatory approval before production |

### Enterprise / Platform Architect
**Your questions:** "How do I design the AI platform?" "What goes where?" "How do patterns fit together?"

| Start With | Why |
|-----------|-----|
| [Reference Architecture](REFERENCE-ARCHITECTURE.md) | How all 10 patterns compose |
| [Multi-Platform Gateway](patterns/01-unified-ai-gateway/multi-platform/) | Foundation: all traffic through one plane |
| [Databricks LLMOps](patterns/05-llmops-pipeline/databricks-llmops/) | Operations pipeline for your platform |
| [Embedded Governance](patterns/06-governance-as-architecture/embedded-governance/) | GAIF-4 metrics in every stage |
| [Multi-Cloud Compliance](patterns/08-compliance-data-routing/multi-cloud-compliance/) | Unified policy across platforms |

### ML / AI Engineer
**Your questions:** "How do I build this RAG pipeline?" "How do agents work?" "What tools should agents use?"

| Start With | Why |
|-----------|-----|
| [Standard RAG](patterns/02-rag-regulated-data/standard-rag/) | Most common first use case |
| [Agentic RAG](patterns/02-rag-regulated-data/agentic-rag/) | Self-correcting retrieval |
| [Linear Chain Agents](patterns/03-multi-agent-safety-gates/linear-chain/) | Simplest multi-agent pattern |
| [MCP Protocol](patterns/04-agentic-tool-governance/mcp-protocol/) | Standard tool integration |
| [RAGAS Evaluation](patterns/09-evaluation-red-teaming/ragas-evaluation/) | Measure RAG quality |

### Security / Compliance Officer
**Your questions:** "Is PHI protected?" "Do we pass audit?" "Are we vulnerable?"

| Start With | Why |
|-----------|-----|
| [Sensitive Data RAG](patterns/02-rag-regulated-data/sensitive-data-rag/) | PHI/PII-aware retrieval |
| [Compliance Evaluation](patterns/09-evaluation-red-teaming/compliance-evaluation/) | Regulatory test suites |
| [Audit Trail](patterns/06-governance-as-architecture/audit-trail/) | Immutable evidence for auditors |
| [Cross-Border Routing](patterns/08-compliance-data-routing/cross-border-routing/) | International data transfer |
| [Automated Red Teaming](patterns/09-evaluation-red-teaming/automated-red-teaming/) | Find vulnerabilities |

### Data / Analytics Leader
**Your questions:** "How does data flow?" "What about data quality?" "Cost per query?"

| Start With | Why |
|-----------|-----|
| [Data Pipeline](patterns/05-llmops-pipeline/data-pipeline/) | Training data lifecycle |
| [Sensitivity Classification](patterns/08-compliance-data-routing/sensitivity-classification/) | Data classification engine |
| [Token-Level FinOps](patterns/10-finops-for-ai/token-level-finops/) | Per-query cost tracking |
| [Data Lineage Routing](patterns/08-compliance-data-routing/data-lineage-routing/) | Track data origin and restrictions |
| [Caching-Optimized RAG](patterns/02-rag-regulated-data/caching-optimized-rag/) | Reduce retrieval costs |

## By Use Case

| I want to... | Go to |
|--------------|-------|
| Build my first RAG app | Pattern 02: [Standard RAG](patterns/02-rag-regulated-data/standard-rag/) |
| Set up an AI gateway | Pattern 01: [Starter](patterns/01-unified-ai-gateway/starter/) then your cloud variant |
| Deploy multi-agent pipeline | Pattern 03: [Linear Chain](patterns/03-multi-agent-safety-gates/linear-chain/) |
| Establish AI governance | Pattern 06: [Governance Maturity](patterns/06-governance-as-architecture/governance-maturity/) |
| Red team my AI | Pattern 09: [Automated Red Teaming](patterns/09-evaluation-red-teaming/automated-red-teaming/) |
| Control AI costs | Pattern 10: [Token-Level FinOps](patterns/10-finops-for-ai/token-level-finops/) |
| Handle PHI/PII safely | Pattern 08: [Azure Compliance](patterns/08-compliance-data-routing/azure-compliance/) (or your cloud) |
| Prevent contamination | Pattern 07: [Validation Checkpoints](patterns/07-contamination-resistant-pipeline/validation-checkpoints/) |
| CI/CD for AI | Pattern 05: Your cloud variant |
| Understand how patterns fit together | [Reference Architecture](REFERENCE-ARCHITECTURE.md) |

---

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
