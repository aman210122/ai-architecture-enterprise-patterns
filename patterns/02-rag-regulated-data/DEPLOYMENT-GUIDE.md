# Deployment Guide: RAG for Regulated Data

## Prerequisites
- Pattern 01 (Gateway) deployed
- Vector store provisioned (AI Search / OpenSearch / Qdrant)
- Embedding model selected and accessible
- LLM endpoint available through gateway
- Data classification policy defined

## Deployment Steps

1. **Deploy vector store** with compliance-aware configuration (encryption at rest, network isolation, access control)
2. **Configure ingestion pipeline**: connectors per source type, extraction, OCR/processing, chunking strategy per document type
3. **Set up embedding pipeline**: batch + incremental modes, rate limit handling, embedding cache for dedup
4. **Implement compliance tagging**: PHI/PII detection (Presidio / DLP API), sensitivity classification, access control labels per chunk
5. **Quality validation gate**: chunk quality scoring, dedup detection, coverage analysis, reject malformed chunks
6. **Index with governance metadata**: sensitivity labels, access control, source lineage, versioning
7. **Wire query pipeline through Pattern 01 gateway**: input sanitization, query classification, enhancement
8. **Configure retrieval**: hybrid vector + BM25, access control filtering (security trimming by user role), metadata filtering
9. **Set up reranking**: cross-encoder reranker (Cohere / BGE), relevance threshold, diversity sampling
10. **Context assembly**: window management, token budget allocation (system + chunks + history + query), citation format injection
11. **Configure guardrails**: groundedness threshold (0.85), PHI leak detection on output, citation verification, content safety
12. **Set up caching**: semantic cache (cosine > 0.95 = hit), TTL per content type, cache warming for common queries
13. **Configure fallback paths**: 0 results path, low relevance path, LLM timeout path, circuit breaker
14. **Deploy feedback loop**: thumbs up/down collection, retrieval quality signals, loop back to reranking weights
15. **Set up GAIF-4 metrics**: T1PR at retrieval, CFR at guardrails, EMR at generation, GDR trending weekly
16. **Configure RAG quality metrics**: precision, recall, MRR, NDCG, groundedness, answer relevancy
17. **Deploy to staging**: run RAGAS evaluation suite, verify all scenarios (clean, PHI, hallucination, cache, fallback)
18. **Promote to production with monitoring**: per-stage latency, token cost tracking, quality dashboards

## Validation Checklist
- [ ] Ingestion pipeline processes all document types
- [ ] PHI/PII detection catches all 18 HIPAA identifier types
- [ ] Access control filtering works per user role
- [ ] Groundedness threshold blocks hallucinations
- [ ] Fallback path works when 0 results returned
- [ ] Cache hit serves correct responses within TTL
- [ ] GAIF-4 metrics reporting to governance dashboard
- [ ] Token cost tracking per query
- [ ] Rollback procedure documented and tested

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
