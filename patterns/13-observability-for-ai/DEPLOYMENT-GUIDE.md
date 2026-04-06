# Deployment Guide: Observability for AI
## Prerequisites: Pattern 01 (Gateway) for centralized metering, OTel collector
## Steps
1. Instrument LLM calls: wrap every model call with OTel span (tokens, model, prompt version)
2. Instrument RAG pipeline: span per stage (retrieve, rerank, generate, guardrails)
3. Instrument agent pipeline: span per agent with inter-agent message tracking
4. Deploy token metering: count input/output tokens per call at gateway
5. Configure quality metrics collection: sample production traffic, score groundedness/relevance
6. Set up retrieval metrics: precision, recall, MRR, NDCG on retrieved chunks
7. Deploy cost metrics: per-query cost calculation (tokens x price per model)
8. Configure user feedback collection: thumbs up/down, explicit ratings, implicit signals
9. Set up quality drift detection: 7-day rolling average, alert on downward trend
10. Configure latency anomaly detection: P95/P99 baseline, alert on 2x deviation
11. Deploy cost anomaly detection: daily spend baseline, alert on spike
12. Set up topic drift detection: embed queries, cluster, detect distribution shift
13. Configure alert rules: quality < threshold, SLA breach, budget 80%/90%/100%
14. Build AI dashboard: real-time quality, latency, cost, usage, GAIF-4
15. Deploy model comparison view: side-by-side quality vs cost vs latency
16. Configure OTel integration: export spans + metrics to OTel collector
17. Set up SIEM integration: security events to Splunk/Sentinel
18. Connect to existing APM: Datadog/New Relic custom metrics for AI
19. Configure retention: traces 30d, quality 90d, cost 1yr, audit 7yr
20. GAIF-4: track all metrics as part of governance observability
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
