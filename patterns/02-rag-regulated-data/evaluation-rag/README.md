# Variant: RAG Evaluation Pipeline

**Continuous evaluation pipeline for RAG quality. Synthetic tests, automated eval, regression testing.**

## Live Demo

**[Launch interactive visualization](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/evaluation-rag/index.html)**

Scenarios: Full eval suite run, regression detection, synthetic test generation, production sample eval, CI/CD gate check.

## When to Use

**Use:** Production RAG needs automated regression testing. Re-indexing might degrade quality. CI/CD pipeline should block bad RAG deployments. Need continuous quality monitoring.

**Skip:** Manual testing is sufficient (early stage). No production RAG to monitor yet.

## Platform Mapping

| RAG Stage | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Extraction | Document Intelligence | Textract | Document AI | Spark UDFs | Unstructured.io |
| Embedding | text-embedding-3 | Titan Embeddings | text-embedding-005 | FMAPI | all-MiniLM |
| Vector Store | AI Search | OpenSearch / Kendra | Vertex AI Search | Vector Search | Qdrant / Chroma |
| LLM | Azure OpenAI | Bedrock | Vertex AI | FMAPI | vLLM / Ollama |
| Guardrails | Content Safety | Bedrock Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |
| Orchestration | Semantic Kernel | LangChain | LangChain | LangChain | LangChain |

| Additional | Azure | AWS | GCP | Open Source |
|-----------|-------|-----|-----|-------------|
| Eval Framework | Azure AI Evaluation | Bedrock Evaluation | Vertex AI Eval | RAGAS / DeepEval |
| Test Gen | Azure OpenAI | Bedrock | Gemini | Local LLM |

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
