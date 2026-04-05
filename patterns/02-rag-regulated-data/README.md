# Pattern 02: RAG for Regulated Data

**Retrieval-augmented generation with compliance boundaries at every pipeline stage. 10 variants covering every RAG architecture from standard vector search to real-time streaming retrieval.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Standard document Q&A | [Standard RAG](standard-rag/) |
| Complex entity relationships | [GraphRAG](graph-rag/) |
| First retrieval may miss context | [Agentic RAG](agentic-rag/) |
| Data across multiple platforms | [Multi-Source RAG](multi-source-rag/) |
| PHI/PII, strict compliance | [Sensitive Data RAG](sensitive-data-rag/) |
| Multi-turn conversations | [Conversational RAG](conversational-rag/) |
| Structured data + documents | [Hybrid SQL+Vector RAG](hybrid-sql-vector-rag/) |
| Images, charts, medical scans | [Multimodal RAG](multimodal-rag/) |
| Live data, streaming events | [Real-Time RAG](realtime-rag/) |
| Quality monitoring, regression testing | [Evaluation RAG](evaluation-rag/) |

## Architecture (11 sections, 2 pipelines)

**Ingestion Pipeline:** Document Sources -> Extraction -> Chunking & Embedding -> Vector Store -> Metadata Catalog

**Query Pipeline:** Query Processing -> Retrieval -> Context Assembly -> Generation -> Validation -> Response

**Cross-cutting:** Data Classification & Compliance, Retrieval Quality & Observability

## RAG Quality Metrics

| Metric | What It Measures |
|--------|-----------------|
| Retrieval precision | Relevant chunks / total retrieved |
| Groundedness | Answer supported by retrieved context |
| Hallucination rate | Claims not in source documents |
| Citation accuracy | Citations match source content |

## Platform Mapping

Each variant is cloud-agnostic. Use this table to pick services for your stack:

| RAG Stage | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Extraction | Document Intelligence | Textract | Document AI | Spark UDFs | Unstructured.io |
| Embedding | text-embedding-3 | Titan Embeddings | text-embedding-005 | FMAPI | all-MiniLM |
| Vector Store | AI Search | OpenSearch / Kendra | Vertex AI Search | Vector Search | Qdrant / Chroma |
| LLM | Azure OpenAI | Bedrock | Vertex AI | FMAPI | vLLM / Ollama |
| Guardrails | Content Safety | Bedrock Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
