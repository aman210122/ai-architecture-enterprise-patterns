# Pattern 02: RAG for Regulated Data

**True SVG architecture diagram with click-to-detail panels. 12 variants. 7-stage ingestion, 8-stage query, governed vector store, 4 cross-cutting layers.**

Click any component in the diagram for full details: configuration, platform mapping, anti-patterns, and GAIF-4 relevance.

## Variants

| Your situation | Variant |
|---------------|---------|
| Standard vector + generation | [Standard RAG](standard-rag/) |
| Knowledge graph, multi-hop | [GraphRAG](graph-rag/) |
| Self-correcting (CRAG) | [Agentic RAG](agentic-rag/) |
| PHI/PII zero-trust | [Sensitive Data](sensitive-data-rag/) |
| Multi-turn chat | [Conversational](conversational-rag/) |
| SQL + vector combined | [SQL+Vector](hybrid-sql-vector-rag/) |
| Images, DICOM, charts | [Multimodal](multimodal-rag/) |
| Cross-platform search | [Multi-Source](multi-source-rag/) |
| Seconds-to-searchable | [Real-Time](realtime-rag/) |
| Quality testing | [Evaluation](evaluation-rag/) |
| Data stays local | [Privacy-Preserving](privacy-preserving-rag/) |
| 60%+ query repetition | [Caching-Optimized](caching-optimized-rag/) |

## GAIF-4 Metrics

| Metric | Measured At | Safe | Critical |
|--------|-----------|------|----------|
| T1PR | Retrieve stage | < 0.05 | > 0.15 |
| CFR | Guardrails stage | 0.00 | > 0.01 |
| EMR | Guardrails stage | < 0.05 | > 0.15 |
| GDR | Weekly trending | < 0.03 | > 0.05 |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | OSS |
|-----------|-------|-----|-----|------------|-----|
| Vector Store | AI Search | OpenSearch | Vertex Search | Vector Search | Qdrant |
| Embedding | Azure OpenAI | Titan | Vertex Embed | DBRX | sentence-transformers |
| LLM | Azure OpenAI | Bedrock | Gemini | DBRX | vLLM |
| Guardrails | Content Safety | Guardrails | Model Armor | Mosaic GW | NeMo |
| DLP | Purview | Macie | Cloud DLP | Presidio | Presidio |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
