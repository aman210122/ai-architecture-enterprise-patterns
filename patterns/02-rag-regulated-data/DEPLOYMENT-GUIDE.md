# Deployment Guide: RAG for Regulated Data

## Prerequisites
Pattern 01 (Gateway) deployed | Vector store provisioned | Embedding model selected | LLM endpoint accessible

## Steps
1. Deploy vector store (encryption, network isolation, access control)
2. Configure ingestion: connectors, extraction, OCR, chunking (512-1024t, 15% overlap)
3. Set up embedding: batch + incremental, rate limiting, dedup cache
4. Implement compliance tagging: PHI/PII (18 HIPAA types), sensitivity levels
5. Quality gate: scoring, dedup, coverage analysis, reject malformed
6. Index with governance metadata: sensitivity, ACL, lineage, version
7. Wire query pipeline through gateway: sanitization, classification, enhancement
8. Configure retrieval: hybrid vector+BM25, security trimming, metadata filter
9. Reranking: cross-encoder (Cohere/BGE), threshold 0.70, diversity
10. Context assembly: token budget (sys+chunks+history+query), citation format
11. Guardrails: groundedness >0.85, PHI scan, citation verify, content safety
12. Caching: semantic (cosine>0.95), TTL per type, warming
13. Fallback: 0-results, low-relevance, timeout, circuit breaker
14. Feedback loop: thumbs up/down, retrieval signals
15. GAIF-4: T1PR at retrieval, CFR at guardrails, EMR at generation, GDR weekly
16. Deploy staging, run RAGAS, promote with monitoring

*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
