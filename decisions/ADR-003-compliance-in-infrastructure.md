# ADR-003: Compliance Routing in Infrastructure, Not Application Code

## Status
Accepted

## Context
Healthcare organizations handling PHI must ensure that sensitive data only reaches compliant endpoints. The common approach is to rely on application developers to implement data classification and routing logic in their code. This fails for several reasons:

- Developers make mistakes. A single missed check exposes PHI.
- Compliance logic is duplicated across every application.
- Policy changes require updating every application.
- No centralized audit of routing decisions.
- Impossible to prove compliance without inspecting every codebase.

## Decision
Implement compliance-aware routing as an infrastructure layer (Pattern 08) that sits between applications and LLM endpoints. Applications send queries to the routing layer. The routing layer classifies data sensitivity and routes to appropriate endpoints. Applications never make compliance decisions.

## Rationale
Compliance is an infrastructure concern, not an application concern. Just as network security is handled by firewalls rather than individual applications, data routing for regulatory compliance should be handled by infrastructure that applications cannot bypass.

This approach provides a single enforcement point, a single audit trail, and a single place to update when policies change. It also provides a formal safety guarantee: if the routing layer is correctly configured, no application can accidentally send PHI to a non-compliant endpoint.

## Consequences

**Positive:**
- Zero PHI violations by design (validated across 30,000 MIMIC-IV queries)
- Single point for policy updates
- Complete audit trail of all routing decisions
- Applications are simpler (no compliance logic needed)
- Provable compliance for auditors and regulators

**Negative:**
- Routing layer becomes a critical dependency
- Data classification has a cost (latency and compute)
- False positives (non-PHI classified as PHI) may route queries to more expensive endpoints
- Requires upfront investment in classification accuracy

**Mitigations:**
- Deploy routing layer with high availability and failover
- Use distribution-free statistical methods (conformal prediction) to control false positive rates
- Implement a feedback loop to improve classification over time

## Research Basis
- PHI-GUARD Paper: CARES algorithm achieved zero PHI violations across 30,000 MIMIC-IV clinical queries with distribution-free safety bound of 0.00534

## Related Patterns
- Pattern 08: Compliance-Aware Routing
- Pattern 01: Unified AI Gateway (routing sits behind the gateway)
- Pattern 11: AI Security Architecture

## GAIF-4 Relevance
Directly measures CFR (Compliance Failure Rate). Target: 0.00. Any non-zero CFR in a healthcare deployment is a potential HIPAA violation.
