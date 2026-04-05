# Pattern 02: RAG for Regulated Data

**Retrieval-augmented generation with compliance boundaries at every stage. 12 variants. Cloud-agnostic with platform mapping.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Standard vector search + generation | [Standard RAG](standard-rag/) |
| Knowledge graph + entity resolution | [GraphRAG](graph-rag/) |
| Self-correcting retrieval (CRAG) | [Agentic RAG](agentic-rag/) |
| PHI/PII-aware zero-trust retrieval | [Sensitive Data RAG](sensitive-data-rag/) |
| Multi-turn with history | [Conversational RAG](conversational-rag/) |
| Text-to-SQL + vector fusion | [Hybrid SQL+Vector](hybrid-sql-vector-rag/) |
| Images, charts, DICOM + text | [Multimodal RAG](multimodal-rag/) |
| Federated retrieval across platforms | [Multi-Source RAG](multi-source-rag/) |
| Streaming, seconds-to-searchable | [Real-Time RAG](realtime-rag/) |
| Automated quality testing | [Evaluation RAG](evaluation-rag/) |
| Data stays local, federated search | [Privacy-Preserving RAG](privacy-preserving-rag/) |
| 60%+ repeated queries, tiered cache | [Caching-Optimized RAG](caching-optimized-rag/) |

## GAIF-4 Metrics for RAG

| Metric | RAG Application |
|--------|----------------|
| T1PR | Contaminated retrieval results passing filters |
| CFR | Compliance violations in generated answers |
| EMR | Hallucinated content not present in sources |
| GDR | Retrieval quality degrading over time |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Vector Store | AI Search | OpenSearch | Vertex Search | Vector Search | Qdrant / Weaviate |
| Embedding | Azure OpenAI | Titan | Vertex Embed | DBRX | sentence-transformers |
| Generation | Azure OpenAI | Bedrock | Gemini | DBRX | vLLM / Ollama |
| Guardrails | Content Safety | Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
