# ADR-001: Unified AI Gateway Over Per-Team API Keys

## Status
Accepted

## Context
As organizations scale AI adoption, individual teams begin calling LLM APIs directly. Each team manages its own API keys, rate limits, and cost tracking. This creates several problems:

- No centralized visibility into total LLM usage and spend
- Inconsistent content filtering and safety policies across teams
- Impossible to enforce organization-wide rate limits or quotas
- No single audit trail for compliance reporting
- Model swaps require changes in every application
- Shadow AI usage becomes undetectable

## Decision
Route all LLM traffic through a unified AI gateway (Pattern 01) regardless of which team, application, or model is being called.

## Rationale
A unified gateway provides a single enforcement point for governance policies, cost controls, content filtering, and observability. It decouples applications from specific model providers, making model swaps transparent to consuming applications.

The operational cost of running a gateway is far lower than the cost of retroactively discovering ungoverned AI usage, compliance violations, or runaway spend.

## Consequences

**Positive:**
- Single pane of glass for all LLM traffic
- Consistent safety and content filtering policies
- Token-level cost tracking and chargeback
- Model provider abstraction (swap without code changes)
- Natural enforcement point for rate limits and quotas
- Complete audit trail for compliance

**Negative:**
- Adds a network hop (typically 10-50ms latency)
- Single point of failure if not properly architected for high availability
- Requires team onboarding and migration from direct API calls
- Gateway team becomes a potential bottleneck for new model access

**Mitigations:**
- Deploy gateway in multiple availability zones
- Implement self-service model registration to avoid bottlenecks
- Use async patterns where latency sensitivity is high

## Platform Options
| Platform | Service |
|----------|---------|
| Databricks | Mosaic AI Gateway |
| Azure | API Management |
| AWS | API Gateway |
| GCP | Apigee |
| Open Source | Kong / Envoy |

## Related Patterns
- Pattern 01: Unified AI Gateway
- Pattern 10: FinOps for AI (cost tracking depends on gateway)
- Pattern 13: Observability for AI (telemetry collection point)

## GAIF-4 Relevance
Gateway is the primary enforcement point for CFR (Compliance Failure Rate) measurement. Without centralized routing, CFR cannot be measured accurately.
