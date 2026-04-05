# Variant: Conversational RAG

**Multi-turn RAG with conversation history, context carryover, and follow-up detection.**

## Live Demo

**[Launch interactive visualization](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/conversational-rag/index.html)**

Scenarios: Multi-turn factual, follow-up with pronoun resolution, sensitive conversation, topic switch handling, citation across turns.

## When to Use

**Use:** Customer support chatbots, clinical assistants, legal Q&A where users ask follow-up questions. Context must carry across turns without re-retrieval.

**Skip:** Single-turn Q&A is sufficient (see standard-rag).

## Platform Mapping

| RAG Stage | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Extraction | Document Intelligence | Textract | Document AI | Spark UDFs | Unstructured.io |
| Embedding | text-embedding-3 | Titan Embeddings | text-embedding-005 | FMAPI | all-MiniLM |
| Vector Store | AI Search | OpenSearch / Kendra | Vertex AI Search | Vector Search | Qdrant / Chroma |
| LLM | Azure OpenAI | Bedrock | Vertex AI | FMAPI | vLLM / Ollama |
| Guardrails | Content Safety | Bedrock Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |
| Orchestration | Semantic Kernel | LangChain | LangChain | LangChain | LangChain |

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
