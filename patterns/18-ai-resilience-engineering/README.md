# Pattern 18: AI Resilience Engineering
**LLM systems fail differently than traditional systems. 12 variants. Circuit breakers, context overflow, deadlock, stale context, semantic retry, graceful degradation.**

AWS published dedicated AI agent resilience guidance in 2026. Traditional resilience patterns (retry, circuit breaker, bulkhead) need AI-specific adaptations because LLM failures are semantic, not just HTTP errors.

| Failure Type | Variant |
|-------------|---------|
| Open/half/close for LLMs | [Circuit Breaker](circuit-breaker-llm/) |
| Conversation exceeds window | [Context Window Overflow](context-window-overflow/) |
| Rate limit hit mid-response | [Token Budget Recovery](token-budget-recovery/) |
| Vector index is outdated | [Stale Context Detection](stale-context-detection/) |
| Agents waiting on each other | [Agent Deadlock Resolution](agent-deadlock-resolution/) |
| Rewrite query, not blind retry | [Semantic Retry](semantic-retry/) |
| Model -> cache -> static -> error | [Graceful Degradation](graceful-degradation-hierarchy/) |
| GPT -> Claude -> Gemini -> local | [Multi-Provider Failover](multi-provider-failover-chain/) |
| AI-specific RTO targets | [Recovery Time Objectives](recovery-time-objectives/) |
| Inject AI-specific failures | [Chaos Testing](chaos-testing-ai/) |
| Handle 429s gracefully | [Rate Limit Resilience](rate-limit-resilience/) |
| Restore context after failure | [Conversation Recovery](conversation-recovery/) |

## Why Traditional Resilience Is Not Enough
| Traditional Pattern | AI Adaptation Needed |
|--------------------|---------------------|
| HTTP retry | Semantic retry (rewrite query, not just resend) |
| Circuit breaker | Model-aware (different thresholds per model provider) |
| Timeout | Token-based timeout (not just wall-clock) |
| Failover | Quality-aware failover (backup model may be worse) |
| Cache | Semantic cache (not exact-match, similarity-based) |
| Health check | Quality check (model is "up" but producing bad answers) |

## AI-Specific RTO Targets
| Recovery Action | Target RTO |
|----------------|-----------|
| Model provider switch | < 5 seconds |
| Cache fallback | < 1 second |
| Graceful degradation | < 2 seconds |
| Conversation recovery | < 10 seconds |
| Full pipeline recovery | < 30 seconds |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
