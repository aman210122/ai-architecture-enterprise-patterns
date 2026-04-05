# Variant: Hybrid SQL + Vector RAG

**Combines Text-to-SQL over structured databases with vector search over documents in a single query.**

## Live Demo

**[Launch interactive visualization](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/hybrid-sql-vector-rag/index.html)**

Scenarios: Data+docs query, SQL-only routing, vector-only routing, sensitive hybrid (SQL ACLs + chunk ACLs), cited hybrid response.

## When to Use

**Use:** "What was revenue last quarter and what did the earnings call say about it?" Analytics + knowledge base in one answer. Questions spanning structured data AND documents.

**Skip:** Only documents, no structured data (see standard-rag). Only SQL queries needed (use Text-to-SQL directly).

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
| Text-to-SQL | Semantic Kernel | Bedrock + Athena | BigQuery + Gemini | Databricks SQL |

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
