# Variant: Real-Time RAG

**Continuous ingestion over streaming data. Index updates in seconds, not hours.**

## Live Demo

**[Launch interactive visualization](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/realtime-rag/index.html)**

Scenarios: Live data query, streaming ingestion, time-windowed retrieval, real-time alert RAG, cited with timestamp.

## When to Use

**Use:** Knowledge base changes continuously. Need answers based on data from seconds ago. Real-time clinical alerts, live news feeds, event-driven compliance monitoring, IoT data analysis.

**Skip:** Static documents are sufficient (see standard-rag). Batch ingestion is fast enough (see standard-rag).

## Platform Mapping

| RAG Stage | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Extraction | Document Intelligence | Textract | Document AI | Spark UDFs | Unstructured.io |
| Embedding | text-embedding-3 | Titan Embeddings | text-embedding-005 | FMAPI | all-MiniLM |
| Vector Store | AI Search | OpenSearch / Kendra | Vertex AI Search | Vector Search | Qdrant / Chroma |
| LLM | Azure OpenAI | Bedrock | Vertex AI | FMAPI | vLLM / Ollama |
| Guardrails | Content Safety | Bedrock Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |
| Orchestration | Semantic Kernel | LangChain | LangChain | LangChain | LangChain |

| Additional | Azure | AWS | GCP | Databricks |
|-----------|-------|-----|-----|------------|
| Streaming | Event Hubs | Kinesis | Pub/Sub | Structured Streaming |
| Live Index | AI Search (push) | OpenSearch (live) | Vertex AI (streaming) | Delta Sync |

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
