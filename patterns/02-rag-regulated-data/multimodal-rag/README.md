# Variant: Multimodal RAG

**Retrieval over images, PDFs with charts, medical imaging, and video transcripts.**

## Live Demo

**[Launch interactive visualization](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/02-rag-regulated-data/multimodal-rag/index.html)**

Scenarios: Image+text query, chart understanding, medical imaging (DICOM), video transcript search, cited multimodal response.

## When to Use

**Use:** Radiology reports + X-rays, engineering blueprints + specs, video compliance review, documents with charts/diagrams. Need to search across text AND visual content.

**Skip:** Text-only documents (see standard-rag).

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
| Vision Model | GPT-4o Vision | Claude 3.5 Vision | Gemini Vision | LLaVA / BLIP-2 |
| Image Embed | CLIP (Azure) | Titan Multimodal | Vertex Multimodal | CLIP (local) |

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
