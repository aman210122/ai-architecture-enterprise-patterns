# Deployment Guide: RAG for Regulated Data

## Prerequisites
Pattern 01 (Gateway) deployed, vector store provisioned, embedding model selected

## Deployment Steps
-e 1. Deploy vector store (AI Search / OpenSearch / Qdrant)
2. Configure chunking strategy per document type
3. Set up embedding pipeline (batch + incremental)
4. Wire query pipeline through Pattern 01 gateway
5. Configure guardrails (Content Safety / Guardrails / Model Armor)
6. Set up RAGAS evaluation baseline (Pattern 09)
7. Deploy to staging, run evaluation suite
8. Promote to production with monitoring
9. Configure GAIF-4 metrics: T1PR on retrieval, EMR on generation

## Validation Checklist
- [ ] All variants selected for your use case
- [ ] Platform mapping confirmed (Azure / AWS / GCP / Databricks / OSS)
- [ ] GAIF-4 metric thresholds defined
- [ ] Monitoring and alerting configured
- [ ] Rollback procedure documented and tested
- [ ] Compliance review completed (if applicable)

## GAIF-4 Integration
Every deployment should include GAIF-4 metric collection. See [Embedded Governance](../06-governance-as-architecture/embedded-governance/) for implementation details.

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
