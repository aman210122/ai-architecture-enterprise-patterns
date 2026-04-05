# Deployment Guide: RAG for Regulated Data

## Prerequisites
- Pattern 01 (Gateway) deployed, vector store provisioned, embedding model selected, LLM endpoint accessible

## Deployment Steps
1. Deploy vector store with encryption at rest, network isolation, access control
2. Configure ingestion: connectors, extraction, OCR/processing, chunking (512-1024 tokens, 10-20% overlap)
3. Set up embedding pipeline: batch + incremental, rate limiting, dedup cache
4. Implement compliance tagging: PHI/PII detection (Presidio / DLP API), sensitivity levels, per-chunk labels
5. Quality validation gate: chunk scoring, dedup, coverage analysis
6. Index with governance metadata: sensitivity, access control, lineage, version
7. Wire query pipeline through gateway: sanitization, classification, enhancement
8. Configure retrieval: hybrid vector + BM25, security trimming by role, metadata filtering
9. Set up reranking: cross-encoder (Cohere/BGE), relevance threshold 0.70, diversity sampling
10. Context assembly: token budget (system + chunks + history + query), citation format
11. Configure guardrails: groundedness > 0.85, PHI leak scan, citation verification, content safety
12. Set up caching: semantic cache (cosine > 0.95), TTL per content type, cache warming
13. Configure fallback: 0-results path, low-relevance path, LLM timeout, circuit breaker
14. Deploy feedback loop: thumbs up/down, retrieval signals
15. Set up GAIF-4: T1PR at retrieval, CFR at guardrails, EMR at generation, GDR weekly
16. Deploy to staging, run RAGAS suite, promote with monitoring

*Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
