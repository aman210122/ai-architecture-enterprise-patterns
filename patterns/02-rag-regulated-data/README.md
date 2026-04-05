# Pattern 02: RAG for Regulated Data

**End-to-end retrieval-augmented generation with compliance boundaries. 12 variants. 7-stage ingestion, 8-stage query, governed vector store, 4 cross-cutting bars.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Standard vector search + generation | [Standard RAG](standard-rag/) |
| Entity relationships, multi-hop reasoning | [GraphRAG](graph-rag/) |
| Self-correcting retrieval (CRAG/Self-RAG) | [Agentic RAG](agentic-rag/) |
| PHI/PII zero-trust, field-level redaction | [Sensitive Data RAG](sensitive-data-rag/) |
| Multi-turn chat with follow-up detection | [Conversational RAG](conversational-rag/) |
| Databases + documents combined | [Hybrid SQL+Vector](hybrid-sql-vector-rag/) |
| Images, charts, DICOM + text | [Multimodal RAG](multimodal-rag/) |
| Search across multiple platforms | [Multi-Source RAG](multi-source-rag/) |
| Seconds-to-searchable streaming | [Real-Time RAG](realtime-rag/) |
| Automated quality testing + regression | [Evaluation RAG](evaluation-rag/) |
| Data stays local, federated search | [Privacy-Preserving RAG](privacy-preserving-rag/) |
| 60%+ repeated queries, tiered cache | [Caching-Optimized RAG](caching-optimized-rag/) |

## GAIF-4 Metrics for RAG

| Metric | RAG Application | Safe | Critical |
|--------|----------------|------|----------|
| T1PR | Contaminated retrievals passing filters | < 0.05 | > 0.15 |
| CFR | Compliance violations in responses | 0.00 | > 0.01 |
| EMR | Hallucinated content not in sources | < 0.05 | > 0.15 |
| GDR | Retrieval quality degrading over time | < 0.03 | > 0.05 |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Vector Store | AI Search | OpenSearch | Vertex Search | Vector Search | Qdrant / Weaviate |
| Embedding | Azure OpenAI | Titan | Vertex Embed | DBRX | sentence-transformers |
| Generation | Azure OpenAI | Bedrock | Gemini | DBRX / External | vLLM / Ollama |
| Guardrails | Content Safety | Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
