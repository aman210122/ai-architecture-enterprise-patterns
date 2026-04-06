# Deployment Guide: AI Resilience Engineering
## Prerequisites: Pattern 01 (Gateway) for centralized failover, Pattern 13 (Observability) for detection
## Steps
1. Map all AI failure modes: model timeout, rate limit, context overflow, stale data, deadlock, poison
2. Deploy model health checks: not just "is it up" but "is it producing quality answers"
3. Configure circuit breakers per model provider: open/half-open/close with AI-specific thresholds
4. Implement context window overflow handling: summarize, truncate, or split conversations
5. Set up token budget recovery: queue requests during 429, backoff, route to alternate
6. Deploy stale context detection: check vector index freshness, cache age, data currency
7. Implement agent deadlock detection: timeout on circular waits, break with forced response
8. Configure semantic retry: rewrite failed query (not blind resend), max 2 retries
9. Build graceful degradation hierarchy: full model -> cached -> static -> safe default -> error
10. Set up multi-provider failover chain: ordered list with quality thresholds per backup
11. Define AI-specific RTOs: model switch < 5s, cache < 1s, full recovery < 30s
12. Deploy chaos testing: inject model timeout, poisoned retrieval, rate limit, stale index
13. Implement conversation recovery: checkpoint conversation state, restore after failure
14. Configure bulkhead isolation: failure in one pipeline cannot cascade to others
15. Set up rate limit resilience: predictive rate limit avoidance, not just reactive
16. Monitor MTTR per failure type, track improvement over time
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
