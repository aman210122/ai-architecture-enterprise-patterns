# AI Architecture Enterprise Patterns

**Production-tested architecture patterns for deploying AI/ML systems in regulated enterprises. Each pattern includes an interactive visualization you can play with in your browser.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Gateway](https://img.shields.io/badge/AI_Gateway-12-blue.svg)](#pattern-01-unified-ai-gateway-12-variants)
[![RAG](https://img.shields.io/badge/RAG-10-green.svg)](#pattern-02-rag-for-regulated-data-10-variants)
[![Agents](https://img.shields.io/badge/Multi--Agent-10-orange.svg)](#pattern-03-multi-agent-safety-gates-10-variants)
[![Tools](https://img.shields.io/badge/Tool_Gov-8-purple.svg)](#pattern-04-tool-governance-8-variants)
[![LLMOps](https://img.shields.io/badge/LLMOps-10-red.svg)](#pattern-05-llmops-pipeline-10-variants)
[![Governance](https://img.shields.io/badge/Governance-14-teal.svg)](#pattern-06-governance-as-architecture-14-variants)
[![Interactive](https://img.shields.io/badge/64_visualizations-interactive-purple.svg)](#)

---

## Why This Exists

Most AI architecture guides show you how to build a chatbot. They skip the hard parts: sensitive data routing, compliance gates, governance decay, multi-model orchestration, agent safety boundaries, and the reality that your LLM pipeline has to survive an audit.

This repository collects architecture patterns designed and validated across 18+ years of enterprise architecture in regulated industries.

**Industries:** Healthcare (HIPAA), Financial Services (SOX, PCI-DSS), Insurance, Government (FedRAMP), Legal, and any organization handling sensitive data.

### GitHub Pages: All 64 interactive demos live at `https://aman210122.github.io/ai-architecture-enterprise-patterns/`

---

## Pattern 01: Unified AI Gateway (12 variants)

| Category | Variants |
|----------|---------|
| Cloud-native | [Azure](patterns/01-unified-ai-gateway/azure-native/), [AWS](patterns/01-unified-ai-gateway/aws-native/), [GCP](patterns/01-unified-ai-gateway/gcp-native/) |
| Platform-native | [Databricks](patterns/01-unified-ai-gateway/databricks-native/), [Snowflake](patterns/01-unified-ai-gateway/snowflake-native/) |
| Multi-platform | [Multi-Platform](patterns/01-unified-ai-gateway/multi-platform/), [Multi-Cloud](patterns/01-unified-ai-gateway/multi-cloud/), [Hybrid](patterns/01-unified-ai-gateway/hybrid/) |
| Self-hosted | [Open Source](patterns/01-unified-ai-gateway/open-source/), [Starter](patterns/01-unified-ai-gateway/starter/), [Federated](patterns/01-unified-ai-gateway/federated/), [Edge](patterns/01-unified-ai-gateway/edge/) |

## Pattern 02: RAG for Regulated Data (10 variants)

| Category | Variants |
|----------|---------|
| Core | [Standard](patterns/02-rag-regulated-data/standard-rag/), [GraphRAG](patterns/02-rag-regulated-data/graph-rag/), [Agentic](patterns/02-rag-regulated-data/agentic-rag/), [Sensitive](patterns/02-rag-regulated-data/sensitive-data-rag/) |
| Specialized | [Conversational](patterns/02-rag-regulated-data/conversational-rag/), [SQL+Vector](patterns/02-rag-regulated-data/hybrid-sql-vector-rag/), [Multimodal](patterns/02-rag-regulated-data/multimodal-rag/), [Multi-Source](patterns/02-rag-regulated-data/multi-source-rag/), [Real-Time](patterns/02-rag-regulated-data/realtime-rag/), [Evaluation](patterns/02-rag-regulated-data/evaluation-rag/) |

## Pattern 03: Multi-Agent Safety Gates (10 variants)

| Category | Variants |
|----------|---------|
| Gate-based | [Linear](patterns/03-multi-agent-safety-gates/linear-chain/), [DAG](patterns/03-multi-agent-safety-gates/dag-orchestration/), [Hierarchical](patterns/03-multi-agent-safety-gates/hierarchical/), [Human-in-Loop](patterns/03-multi-agent-safety-gates/human-in-the-loop/) |
| Decision | [Consensus](patterns/03-multi-agent-safety-gates/consensus/), [Adversarial](patterns/03-multi-agent-safety-gates/adversarial-red-blue/), [Debate](patterns/03-multi-agent-safety-gates/debate/) |
| Advanced | [Reflection](patterns/03-multi-agent-safety-gates/reflection-loop/), [Swarm](patterns/03-multi-agent-safety-gates/swarm/), [Monitor](patterns/03-multi-agent-safety-gates/parallel-monitor/) |

## Pattern 04: Tool Governance (8 variants)

| Category | Variants |
|----------|---------|
| Protocols | [MCP](patterns/04-agentic-tool-governance/mcp-protocol/), [A2A](patterns/04-agentic-tool-governance/a2a-protocol/), [Function Calling](patterns/04-agentic-tool-governance/function-calling/) |
| Execution | [Compound Tools](patterns/04-agentic-tool-governance/compound-tools/), [Sandboxed](patterns/04-agentic-tool-governance/sandboxed-execution/) |
| Enterprise | [Escalation](patterns/04-agentic-tool-governance/tool-escalation/), [Multi-Tenant](patterns/04-agentic-tool-governance/multi-tenant-isolation/), [Discovery](patterns/04-agentic-tool-governance/tool-discovery/) |

## Pattern 05: LLMOps Pipeline (10 variants)

| Category | Variants |
|----------|---------|
| Cloud-specific | [Azure](patterns/05-llmops-pipeline/azure-llmops/), [AWS](patterns/05-llmops-pipeline/aws-llmops/), [GCP](patterns/05-llmops-pipeline/gcp-llmops/), [Databricks](patterns/05-llmops-pipeline/databricks-llmops/) |
| Self-hosted | [Open Source](patterns/05-llmops-pipeline/open-source-llmops/), [Hybrid](patterns/05-llmops-pipeline/hybrid-llmops/) |
| Specialized | [Prompt Engineering](patterns/05-llmops-pipeline/prompt-engineering/), [A/B Testing](patterns/05-llmops-pipeline/model-ab-testing/), [Compliance-Gated](patterns/05-llmops-pipeline/compliance-gated/), [Data Pipeline](patterns/05-llmops-pipeline/data-pipeline/) |

## Pattern 06: Governance-as-Architecture (14 variants)

Governance built into the architecture, not bolted on. Integrates [GAIF-4](https://github.com/aman210122/gaif-governance-observatory) metrics.

| Category | Variants |
|----------|---------|
| Measurement | [Embedded](patterns/06-governance-as-architecture/embedded-governance/), [Dashboard](patterns/06-governance-as-architecture/governance-dashboard/), [Decay Detection](patterns/06-governance-as-architecture/decay-detection/) |
| Automation | [Policy-as-Code](patterns/06-governance-as-architecture/policy-as-code/), [Continuous Compliance](patterns/06-governance-as-architecture/continuous-compliance/) |
| Enterprise | [Audit Trail](patterns/06-governance-as-architecture/audit-trail/), [Risk-Tiered](patterns/06-governance-as-architecture/risk-tiered/), [Federation](patterns/06-governance-as-architecture/governance-federation/) |
| Development | [Shift-Left](patterns/06-governance-as-architecture/shift-left-governance/), [Model Cards](patterns/06-governance-as-architecture/model-cards/) |
| Responsible AI | [XAI Explainability](patterns/06-governance-as-architecture/xai-explainability/), [Bias & Fairness](patterns/06-governance-as-architecture/bias-fairness/), [Consent & Data Rights](patterns/06-governance-as-architecture/consent-data-rights/) |
| Meta-governance | [Governance Testing](patterns/06-governance-as-architecture/governance-testing/) |

---

### Future Patterns

| # | Pattern | Variants | Status |
|---|---------|----------|--------|
| 07 | Contamination-Resistant Pipeline | Isolation, Validation, Canary, Rollback, Percolation, Redundant, Sanitization, Immune System | Planned |
| 08 | Compliance-Aware Data Routing | Azure, AWS, GCP, Multi-Cloud, On-Prem | Planned |
| 09 | AI Evaluation & Red Teaming | Automated, RAGAS, LLM-as-Judge, Human, Safety | Planned |
| 10 | FinOps for AI | Azure, AWS, GCP, Multi-Cloud, Token-Level | Planned |

---

## Governance: [GAIF-4](https://github.com/aman210122/gaif-governance-observatory) metrics (T1PR, CFR, EMR, GDR) in every pattern.

## Standards: NIST AI RMF, EU AI Act, WHO AI Ethics, HIPAA, SOX, PCI-DSS, GDPR, FedRAMP

## Author

**Aman Sharma** - Principal Enterprise Architect, AI/ML | 18+ years in regulated industries

[LinkedIn](https://linkedin.com/in/amansharmaarchitect) | [ORCID](https://orcid.org/0009-0005-5107-4485) | [GitHub](https://github.com/aman210122) | [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory)

## License: MIT
