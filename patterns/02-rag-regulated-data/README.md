# Pattern 02: RAG for Regulated Data

**End-to-end retrieval-augmented generation with compliance boundaries at every stage. 12 variants. 7-stage ingestion, 8-stage query pipeline, governed vector store, 4 cross-cutting bars.**

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

## Architecture (all variants share this structure)

**Ingestion (7 stages):** Sources -> Extract -> Process -> Chunk -> Embed -> Compliance Tag -> Quality Validate -> Vector Store

**Query (8 stages):** Input -> Classify -> Enhance -> Retrieve -> Rerank -> Context Assembly -> Generate -> Guardrails -> Response

**4 cross-cutting bars:** Governance (GAIF-4), Observability (tracing, precision, recall), Operations (cache, rate limit, fallback), Economics (token cost, cache savings)

**Feedback Loop:** User signals loop back to improve retrieval and ranking

## GAIF-4 Metrics for RAG

| Metric | RAG Application | Safe | Critical |
|--------|----------------|------|----------|
| T1PR | Contaminated retrievals passing filters | < 0.05 | > 0.15 |
| CFR | Compliance violations in responses | 0.00 | > 0.01 |
| EMR | Hallucinated content not in sources | < 0.05 | > 0.15 |
| GDR | Retrieval quality degrading over time | < 0.03 | > 0.05 |

## RAG Quality Metrics

| Metric | What It Measures |
|--------|-----------------|
| Retrieval Precision | Relevant chunks in top-K results |
| Groundedness | Claims supported by source chunks |
| Answer Relevancy | Response addresses the query |
| Context Recall | Relevant info retrieved from index |
| MRR | Rank of first relevant result |
| NDCG | Graded relevance of ranked results |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Vector Store | AI Search | OpenSearch | Vertex Search | Vector Search | Qdrant / Weaviate |
| Embedding | Azure OpenAI | Titan | Vertex Embed | DBRX | sentence-transformers |
| Generation | Azure OpenAI | Bedrock | Gemini | DBRX / External | vLLM / Ollama |
| Guardrails | Content Safety | Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |
| Orchestration | Prompt Flow | Bedrock KB | Agent Builder | LangChain | LangChain / LlamaIndex |
| DLP | Purview | Macie | Cloud DLP | Presidio | Presidio |
| Tracing | App Insights | X-Ray | Cloud Trace | MLflow | OpenTelemetry |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
