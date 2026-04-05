# AI Architecture Enterprise Patterns

**Production-tested architecture patterns for deploying AI/ML systems in regulated enterprises. Each pattern includes an interactive visualization you can play with in your browser.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Gateway Variants](https://img.shields.io/badge/AI_Gateway-12_variants-blue.svg)](#pattern-01-unified-ai-gateway)
[![RAG Variants](https://img.shields.io/badge/RAG-10_variants-green.svg)](#pattern-02-rag-for-regulated-data)
[![Interactive](https://img.shields.io/badge/22_visualizations-interactive-purple.svg)](#how-it-works)

---

## Why This Exists

Most AI architecture guides show you how to build a chatbot. They skip the hard parts: sensitive data routing, compliance gates, governance decay, multi-model orchestration, agent safety boundaries, and the reality that your LLM pipeline has to survive an audit.

This repository collects architecture patterns designed and validated across 18+ years of enterprise architecture in regulated industries. Each pattern includes an interactive browser-based visualization with animated data flow, a production deployment guide, and governance metrics mapping.

**Industries:** Healthcare (HIPAA), Financial Services (SOX, PCI-DSS), Insurance, Government (FedRAMP), Legal, and any organization handling sensitive data under regulatory constraints.

---

## How It Works

**Interactive visualization** - Open the HTML file in any browser. Click scenario buttons to watch data flow through the architecture end-to-end. Click any section to expand and explore sub-components. No install, no dependencies.

### GitHub Pages

All 22 interactive demos are live at `https://aman210122.github.io/ai-architecture-enterprise-patterns/`

---

## Pattern 01: Unified AI Gateway

Route all LLM and ML traffic through a single governance-aware control plane. **12 variants.**

**Cloud-native:**

| Variant | Stack | Demo |
|---------|-------|------|
| [Azure Native](patterns/01-unified-ai-gateway/azure-native/) | Azure APIM + Azure OpenAI + Content Safety | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/azure-native/index.html) |
| [AWS Native](patterns/01-unified-ai-gateway/aws-native/) | API Gateway + Bedrock + Guardrails for AI | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/aws-native/index.html) |
| [GCP Native](patterns/01-unified-ai-gateway/gcp-native/) | Apigee + Vertex AI + Gemini + Model Armor | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/gcp-native/index.html) |

**Platform-native:**

| Variant | Stack | Demo |
|---------|-------|------|
| [Databricks Native](patterns/01-unified-ai-gateway/databricks-native/) | Mosaic AI GW + FMAPI + Unity Catalog | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/databricks-native/index.html) |
| [Snowflake Native](patterns/01-unified-ai-gateway/snowflake-native/) | Cortex + Snowpark + Arctic + Streamlit | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/snowflake-native/index.html) |

**Multi-platform:**

| Variant | Stack | Demo |
|---------|-------|------|
| [Multi-Platform](patterns/01-unified-ai-gateway/multi-platform/) | Databricks + Azure AI Foundry + Snowflake | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/multi-platform/index.html) |
| [Multi-Cloud](patterns/01-unified-ai-gateway/multi-cloud/) | Kong + Azure + AWS + GCP | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/multi-cloud/index.html) |
| [Hybrid](patterns/01-unified-ai-gateway/hybrid/) | Cloud + on-prem dual-tier | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/hybrid/index.html) |

**Self-hosted and specialized:**

| Variant | Stack | Demo |
|---------|-------|------|
| [Open Source](patterns/01-unified-ai-gateway/open-source/) | LiteLLM + vLLM/Ollama + Llama/Mistral | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/open-source/index.html) |
| [Starter](patterns/01-unified-ai-gateway/starter/) | Single provider + reverse proxy | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/starter/index.html) |
| [Federated](patterns/01-unified-ai-gateway/federated/) | Multi-BU gateways + central governance | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/federated/index.html) |
| [Edge](patterns/01-unified-ai-gateway/edge/) | On-device SLM + offline-capable | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/01-unified-ai-gateway/edge/index.html) |

---

## Pattern 02: RAG for Regulated Data

Retrieval-augmented generation with compliance boundaries at every stage. **10 variants.** Each variant is cloud-agnostic with a [platform mapping table](patterns/02-rag-regulated-data/) for Azure, AWS, GCP, Databricks, and open-source stacks.

**Core RAG architectures:**

| Variant | Architecture | Demo |
|---------|-------------|------|
| [Standard RAG](patterns/02-rag-regulated-data/standard-rag/) | Vector search + chunking + generation with guardrails | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/standard-rag/index.html) |
| [GraphRAG](patterns/02-rag-regulated-data/graph-rag/) | Knowledge graph traversal + entity resolution | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/graph-rag/index.html) |
| [Agentic RAG](patterns/02-rag-regulated-data/agentic-rag/) | Self-correcting retrieval (CRAG / Self-RAG) | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/agentic-rag/index.html) |
| [Sensitive Data RAG](patterns/02-rag-regulated-data/sensitive-data-rag/) | PHI/PII-aware with zero-trust retrieval | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/sensitive-data-rag/index.html) |

**Specialized RAG architectures:**

| Variant | Architecture | Demo |
|---------|-------------|------|
| [Conversational RAG](patterns/02-rag-regulated-data/conversational-rag/) | Multi-turn with conversation history + follow-up detection | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/conversational-rag/index.html) |
| [Hybrid SQL+Vector](patterns/02-rag-regulated-data/hybrid-sql-vector-rag/) | Text-to-SQL + vector search in a single query | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/hybrid-sql-vector-rag/index.html) |
| [Multimodal RAG](patterns/02-rag-regulated-data/multimodal-rag/) | Images, charts, medical scans + text retrieval | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/multimodal-rag/index.html) |
| [Multi-Source RAG](patterns/02-rag-regulated-data/multi-source-rag/) | Federated retrieval across platforms | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/multi-source-rag/index.html) |
| [Real-Time RAG](patterns/02-rag-regulated-data/realtime-rag/) | Streaming ingestion, seconds-to-searchable | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/realtime-rag/index.html) |
| [RAG Evaluation](patterns/02-rag-regulated-data/evaluation-rag/) | Automated quality testing + regression detection | [Launch](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/evaluation-rag/index.html) |

---

### Future Patterns

| # | Pattern | Status |
|---|---------|--------|
| 03 | Multi-Agent Pipeline with Safety Gates | Planned |
| 04 | Governance-as-Architecture | Planned |
| 05 | Contamination-Resistant Pipeline | Planned |
| 06 | Risk-Tiered AI Deployment | Planned |

---

## Governance Integration

Every pattern includes quantitative metrics from [GAIF-4](https://github.com/aman210122/gaif-governance-observatory):

| Metric | What It Measures |
|--------|-----------------|
| **T1PR** | Contaminated outputs bypassing safety filters |
| **CFR** | Policy violations in completed requests |
| **EMR** | Dangerous content emerging at the pipeline level |
| **GDR** | Governance effectiveness degrading over time |

---

## Standards Mapping

NIST AI RMF, EU AI Act, WHO AI Ethics, HIPAA, SOX, PCI-DSS, GDPR, FedRAMP

---

## Author

**Aman Sharma** - Principal Enterprise Architect, AI/ML | 18+ years in regulated industries

[LinkedIn](https://linkedin.com/in/amansharmaarchitect) | [ORCID](https://orcid.org/0009-0005-5107-4485) | [GitHub](https://github.com/aman210122)

**Related:** [GAIF Governance Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Research Papers](https://orcid.org/0009-0005-5107-4485)

---

## License

MIT License. See [LICENSE](LICENSE) for details.
