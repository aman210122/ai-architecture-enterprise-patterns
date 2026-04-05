# AI Architecture Enterprise Patterns

**Production-tested architecture patterns for deploying AI/ML systems in regulated enterprises. 126 interactive visualizations across 10 patterns. Play with any of them in your browser.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Patterns](https://img.shields.io/badge/10_patterns-126_visualizations-purple.svg)](#)
[![Gateway](https://img.shields.io/badge/Gateway-12-blue.svg)](#pattern-01-unified-ai-gateway-12) [![RAG](https://img.shields.io/badge/RAG-12-green.svg)](#pattern-02-rag-for-regulated-data-12) [![Agents](https://img.shields.io/badge/Agents-11-orange.svg)](#pattern-03-multi-agent-safety-gates-11) [![Tools](https://img.shields.io/badge/Tools-9-purple.svg)](#pattern-04-tool-governance-9) [![LLMOps](https://img.shields.io/badge/LLMOps-12-red.svg)](#pattern-05-llmops-pipeline-12) [![Gov](https://img.shields.io/badge/Gov-15-teal.svg)](#pattern-06-governance-as-architecture-15) [![Contam](https://img.shields.io/badge/Contam-12-orange.svg)](#pattern-07-contamination-resistant-pipeline-12) [![Compliance](https://img.shields.io/badge/Compliance-14-blue.svg)](#pattern-08-compliance-aware-data-routing-14) [![Eval](https://img.shields.io/badge/Eval-15-red.svg)](#pattern-09-ai-evaluation--red-teaming-15) [![FinOps](https://img.shields.io/badge/FinOps-14-green.svg)](#pattern-10-finops-for-ai-14)

**Industries:** Healthcare (HIPAA), Financial Services (SOX, PCI-DSS), Insurance, Government (FedRAMP), Legal.

### All 126 interactive demos: `https://aman210122.github.io/ai-architecture-enterprise-patterns/`

---

## Start Here

**New to the repo?** Pick your path:

| Your role | Start with | Why |
|-----------|-----------|-----|
| **CTO / VP Eng** | [Governance Maturity](patterns/06-governance-as-architecture/governance-maturity/), [ROI Measurement](patterns/10-finops-for-ai/roi-measurement/), [Risk-Tiered](patterns/06-governance-as-architecture/risk-tiered/) | Assess governance posture, prove business value, align with EU AI Act |
| **Platform Architect** | [Reference Architecture](REFERENCE-ARCHITECTURE.md), [Multi-Platform Gateway](patterns/01-unified-ai-gateway/multi-platform/), [Embedded Governance](patterns/06-governance-as-architecture/embedded-governance/) | Understand how 10 patterns compose, build the foundation |
| **ML / AI Engineer** | [Standard RAG](patterns/02-rag-regulated-data/standard-rag/), [Linear Chain Agents](patterns/03-multi-agent-safety-gates/linear-chain/), [MCP Protocol](patterns/04-agentic-tool-governance/mcp-protocol/) | Build your first use cases |
| **Security / Compliance** | [Sensitive Data RAG](patterns/02-rag-regulated-data/sensitive-data-rag/), [Compliance Evaluation](patterns/09-evaluation-red-teaming/compliance-evaluation/), [Audit Trail](patterns/06-governance-as-architecture/audit-trail/) | Protect data, pass audit |

**Full persona guide:** [GETTING-STARTED.md](GETTING-STARTED.md) | **How patterns fit together:** [REFERENCE-ARCHITECTURE.md](REFERENCE-ARCHITECTURE.md)

---

## Pattern 01: Unified AI Gateway (12)
| Cloud | [Azure](patterns/01-unified-ai-gateway/azure-native/) [AWS](patterns/01-unified-ai-gateway/aws-native/) [GCP](patterns/01-unified-ai-gateway/gcp-native/) | Platform | [Databricks](patterns/01-unified-ai-gateway/databricks-native/) [Snowflake](patterns/01-unified-ai-gateway/snowflake-native/) |
|-------|---|---------|---|
| Multi | [Multi-Platform](patterns/01-unified-ai-gateway/multi-platform/) [Multi-Cloud](patterns/01-unified-ai-gateway/multi-cloud/) [Hybrid](patterns/01-unified-ai-gateway/hybrid/) | Self-hosted | [Open Source](patterns/01-unified-ai-gateway/open-source/) [Starter](patterns/01-unified-ai-gateway/starter/) [Federated](patterns/01-unified-ai-gateway/federated/) [Edge](patterns/01-unified-ai-gateway/edge/) |

## Pattern 02: RAG for Regulated Data (12)
| Core | [Standard](patterns/02-rag-regulated-data/standard-rag/) [GraphRAG](patterns/02-rag-regulated-data/graph-rag/) [Agentic](patterns/02-rag-regulated-data/agentic-rag/) [Sensitive](patterns/02-rag-regulated-data/sensitive-data-rag/) |
|------|---|
| Specialized | [Conversational](patterns/02-rag-regulated-data/conversational-rag/) [SQL+Vector](patterns/02-rag-regulated-data/hybrid-sql-vector-rag/) [Multimodal](patterns/02-rag-regulated-data/multimodal-rag/) [Multi-Source](patterns/02-rag-regulated-data/multi-source-rag/) [Real-Time](patterns/02-rag-regulated-data/realtime-rag/) [Evaluation](patterns/02-rag-regulated-data/evaluation-rag/) |
| Advanced | [Privacy-Preserving](patterns/02-rag-regulated-data/privacy-preserving-rag/) [Caching-Optimized](patterns/02-rag-regulated-data/caching-optimized-rag/) |

## Pattern 03: Multi-Agent Safety Gates (11)
| Gate | [Linear](patterns/03-multi-agent-safety-gates/linear-chain/) [DAG](patterns/03-multi-agent-safety-gates/dag-orchestration/) [Hierarchical](patterns/03-multi-agent-safety-gates/hierarchical/) [Human](patterns/03-multi-agent-safety-gates/human-in-the-loop/) |
|------|---|
| Decision | [Consensus](patterns/03-multi-agent-safety-gates/consensus/) [Adversarial](patterns/03-multi-agent-safety-gates/adversarial-red-blue/) [Debate](patterns/03-multi-agent-safety-gates/debate/) |
| Advanced | [Reflection](patterns/03-multi-agent-safety-gates/reflection-loop/) [Swarm](patterns/03-multi-agent-safety-gates/swarm/) [Monitor](patterns/03-multi-agent-safety-gates/parallel-monitor/) [State Machine](patterns/03-multi-agent-safety-gates/state-machine-agent/) |

## Pattern 04: Tool Governance (9)
[MCP](patterns/04-agentic-tool-governance/mcp-protocol/) [A2A](patterns/04-agentic-tool-governance/a2a-protocol/) [Function Calling](patterns/04-agentic-tool-governance/function-calling/) [Compound](patterns/04-agentic-tool-governance/compound-tools/) [Sandboxed](patterns/04-agentic-tool-governance/sandboxed-execution/) [Escalation](patterns/04-agentic-tool-governance/tool-escalation/) [Multi-Tenant](patterns/04-agentic-tool-governance/multi-tenant-isolation/) [Discovery](patterns/04-agentic-tool-governance/tool-discovery/) [Versioning](patterns/04-agentic-tool-governance/tool-versioning/)

## Pattern 05: LLMOps Pipeline (12)
| Cloud | [Azure](patterns/05-llmops-pipeline/azure-llmops/) [AWS](patterns/05-llmops-pipeline/aws-llmops/) [GCP](patterns/05-llmops-pipeline/gcp-llmops/) [Databricks](patterns/05-llmops-pipeline/databricks-llmops/) |
|-------|---|
| Self-hosted | [Open Source](patterns/05-llmops-pipeline/open-source-llmops/) [Hybrid](patterns/05-llmops-pipeline/hybrid-llmops/) |
| Specialized | [Prompt](patterns/05-llmops-pipeline/prompt-engineering/) [A/B Test](patterns/05-llmops-pipeline/model-ab-testing/) [Compliance-Gated](patterns/05-llmops-pipeline/compliance-gated/) [Data Pipeline](patterns/05-llmops-pipeline/data-pipeline/) |
| Operations | [Shadow Deploy](patterns/05-llmops-pipeline/shadow-deployment/) [Incident Response](patterns/05-llmops-pipeline/incident-response/) |

## Pattern 06: Governance-as-Architecture (15)
| Measurement | [Embedded](patterns/06-governance-as-architecture/embedded-governance/) [Dashboard](patterns/06-governance-as-architecture/governance-dashboard/) [Decay](patterns/06-governance-as-architecture/decay-detection/) |
|------------|---|
| Automation | [Policy-as-Code](patterns/06-governance-as-architecture/policy-as-code/) [Continuous](patterns/06-governance-as-architecture/continuous-compliance/) |
| Enterprise | [Audit Trail](patterns/06-governance-as-architecture/audit-trail/) [Risk-Tiered](patterns/06-governance-as-architecture/risk-tiered/) [Federation](patterns/06-governance-as-architecture/governance-federation/) [Maturity](patterns/06-governance-as-architecture/governance-maturity/) |
| Development | [Shift-Left](patterns/06-governance-as-architecture/shift-left-governance/) [Model Cards](patterns/06-governance-as-architecture/model-cards/) |
| Responsible AI | [XAI](patterns/06-governance-as-architecture/xai-explainability/) [Bias](patterns/06-governance-as-architecture/bias-fairness/) [Consent](patterns/06-governance-as-architecture/consent-data-rights/) |
| Meta | [Gov Testing](patterns/06-governance-as-architecture/governance-testing/) |

## Pattern 07: Contamination-Resistant Pipeline (12)
Research-validated from [EMG](https://doi.org/10.5281/zenodo.19411743) and ContamPerc papers.
| Prevention | [Isolation](patterns/07-contamination-resistant-pipeline/isolation-barriers/) [Sanitization](patterns/07-contamination-resistant-pipeline/input-sanitization/) |
|-----------|---|
| Detection | [Validation](patterns/07-contamination-resistant-pipeline/validation-checkpoints/) [Canary](patterns/07-contamination-resistant-pipeline/canary-pipeline/) [Percolation](patterns/07-contamination-resistant-pipeline/contamination-percolation/) [Redundant](patterns/07-contamination-resistant-pipeline/redundant-generation/) |
| Response | [Quarantine](patterns/07-contamination-resistant-pipeline/output-quarantine/) [Degradation](patterns/07-contamination-resistant-pipeline/graceful-degradation/) |
| Recovery | [Rollback](patterns/07-contamination-resistant-pipeline/rollback-capable/) [Lineage](patterns/07-contamination-resistant-pipeline/contamination-lineage/) [Cross-Pipeline](patterns/07-contamination-resistant-pipeline/cross-pipeline/) [Immune](patterns/07-contamination-resistant-pipeline/immune-system/) |

## Pattern 08: Compliance-Aware Data Routing (14)
| Cloud | [Azure](patterns/08-compliance-data-routing/azure-compliance/) [AWS](patterns/08-compliance-data-routing/aws-compliance/) [GCP](patterns/08-compliance-data-routing/gcp-compliance/) |
|-------|---|
| Multi | [Multi-Cloud](patterns/08-compliance-data-routing/multi-cloud-compliance/) [On-Prem](patterns/08-compliance-data-routing/on-prem-compliance/) |
| Routing | [Classification](patterns/08-compliance-data-routing/sensitivity-classification/) [Residency](patterns/08-compliance-data-routing/data-residency-routing/) [Consent](patterns/08-compliance-data-routing/consent-based-routing/) [Dynamic](patterns/08-compliance-data-routing/dynamic-reclassification/) [Cross-Border](patterns/08-compliance-data-routing/cross-border-routing/) |
| Advanced | [Multi-Regulation](patterns/08-compliance-data-routing/multi-regulation/) [Anonymization](patterns/08-compliance-data-routing/anonymization-routing/) [Lineage](patterns/08-compliance-data-routing/data-lineage-routing/) [Temporal](patterns/08-compliance-data-routing/temporal-compliance/) |

## Pattern 09: AI Evaluation & Red Teaming (15)
| Automated | [Red Teaming](patterns/09-evaluation-red-teaming/automated-red-teaming/) [RAGAS](patterns/09-evaluation-red-teaming/ragas-evaluation/) [LLM-as-Judge](patterns/09-evaluation-red-teaming/llm-as-judge/) [Adversarial](patterns/09-evaluation-red-teaming/adversarial-robustness/) |
|-----------|---|
| Human | [Human Eval](patterns/09-evaluation-red-teaming/human-eval/) [Domain-Specific](patterns/09-evaluation-red-teaming/domain-specific-eval/) |
| Continuous | [Safety Bench](patterns/09-evaluation-red-teaming/safety-benchmarking/) [Continuous](patterns/09-evaluation-red-teaming/continuous-eval/) [Bias](patterns/09-evaluation-red-teaming/bias-evaluation/) [Regression](patterns/09-evaluation-red-teaming/regression-testing/) |
| Specialized | [Prompt Leakage](patterns/09-evaluation-red-teaming/prompt-leakage/) [Hallucination](patterns/09-evaluation-red-teaming/hallucination-benchmarking/) [Multi-Model](patterns/09-evaluation-red-teaming/multi-model-comparison/) [Compliance](patterns/09-evaluation-red-teaming/compliance-evaluation/) [Synthetic Data](patterns/09-evaluation-red-teaming/synthetic-test-generation/) |

## Pattern 10: FinOps for AI (14)
| Cloud | [Azure](patterns/10-finops-for-ai/azure-finops/) [AWS](patterns/10-finops-for-ai/aws-finops/) [GCP](patterns/10-finops-for-ai/gcp-finops/) [Multi-Cloud](patterns/10-finops-for-ai/multi-cloud-finops/) |
|-------|---|
| Optimization | [Token-Level](patterns/10-finops-for-ai/token-level-finops/) [Model Cost](patterns/10-finops-for-ai/model-cost-optimization/) [Cache Economics](patterns/10-finops-for-ai/cache-economics/) [Inference Bench](patterns/10-finops-for-ai/inference-benchmarking/) |
| Enterprise | [Chargeback](patterns/10-finops-for-ai/chargeback/) [Budget Gov](patterns/10-finops-for-ai/budget-governance/) [Capacity Planning](patterns/10-finops-for-ai/capacity-planning/) |
| Advanced | [Waste Detection](patterns/10-finops-for-ai/waste-detection/) [Cost Anomaly](patterns/10-finops-for-ai/cost-anomaly/) [ROI Measurement](patterns/10-finops-for-ai/roi-measurement/) |

---

## Coming Soon: Patterns 11-15

| # | Pattern | Planned Variants | Description |
|---|---------|-----------------|-------------|
| 11 | **AI Security Architecture** | Prompt Injection Defense, Model Theft Prevention, Training Data Poisoning, Endpoint Security, Identity & Access, Incident Response | Defense-in-depth security for AI systems |
| 12 | **Enterprise AI Platform** | Lakehouse for AI, Workspace Design, Data Mesh, Feature Store, Networking, Compute Strategy | How to design the platform underneath the gateway |
| 13 | **Observability for AI** | LLM Tracing, AI Metrics, Alerting, Dashboards, Feedback Loops | Full observability, not just a cross-cutting bar |
| 14 | **AI Product Architecture** | Conversational AI, AI Search, Document Intelligence, Recommendations, Copilots | How to build AI products, not just infrastructure |
| 15 | **Migration & Interoperability** | Cloud Migration, Model Portability, API Compatibility, Multi-Framework | Avoid vendor lock-in at every layer |

---

## [GAIF-4](https://github.com/aman210122/gaif-governance-observatory) governance metrics in every pattern | NIST AI RMF, EU AI Act, HIPAA, SOX, PCI-DSS, GDPR, FedRAMP

**Aman Sharma** - Principal Enterprise Architect, AI/ML | 18+ years | [LinkedIn](https://linkedin.com/in/amansharmaarchitect) | [ORCID](https://orcid.org/0009-0005-5107-4485) | [GitHub](https://github.com/aman210122) | License: MIT
