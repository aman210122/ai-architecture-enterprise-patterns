# Pattern 13: Observability for AI
**AI systems are not observable with traditional APM. 12 variants. Instrument, collect, detect, alert, visualize across tokens, quality, cost, and drift.**

Traditional APM tracks latency and errors. AI observability tracks groundedness, retrieval precision, token cost, quality drift, topic drift, and hallucination rate. These are new dimensions that Datadog/New Relic do not provide out of the box.

| Observability Layer | Variant |
|--------------------|---------|
| Token-level traces | [LLM Call Tracing](llm-call-tracing/) |
| Per-stage RAG spans | [RAG Pipeline Tracing](rag-pipeline-tracing/) |
| Per-agent spans | [Agent Pipeline Tracing](agent-pipeline-tracing/) |
| Groundedness, relevance | [Quality Metrics](quality-metrics/) |
| Precision, recall, MRR | [Retrieval Metrics](retrieval-metrics/) |
| Quality, latency, topic | [Drift Detection](drift-detection/) |
| Per-query, per-team | [Cost Observability](cost-observability/) |
| Quality, SLA, budget | [Alerting Rules](alerting-rules/) |
| Real-time dashboards | [AI Dashboards](ai-dashboards/) |
| User signals analysis | [Feedback Analytics](feedback-analytics/) |
| Standard instrumentation | [OpenTelemetry](opentelemetry-integration/) |
| Splunk, Datadog, Sentinel | [SIEM/APM Integration](siem-apm-integration/) |

## What AI Observability Adds to Traditional APM
| Dimension | Traditional APM | AI Observability |
|-----------|----------------|------------------|
| Throughput | Requests/sec | Tokens/sec + requests/sec |
| Latency | P50/P95/P99 | Per-stage: retrieve, generate, guardrails |
| Errors | HTTP 5xx | Hallucination, PHI leak, safety block |
| Quality | N/A | Groundedness, relevance, faithfulness |
| Cost | Infra cost | Token cost per query per model |
| Drift | N/A | Quality drift, topic drift, prompt drift |
| Feedback | N/A | User ratings, implicit signals |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
