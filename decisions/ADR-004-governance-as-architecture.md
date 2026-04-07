# ADR-004: Governance Embedded in Architecture, Not in Documents

## Status
Accepted

## Context
Most organizations implement AI governance through policy documents, review boards, and approval workflows. While these are necessary, they are insufficient. A governance framework that exists only as a document on SharePoint has no enforcement mechanism. Teams can and do ignore it, often unintentionally, as they move fast to deliver AI capabilities.

The gap between documented governance and actual system behavior is measurable. In empirical analysis of three commercial AI platforms, governance decay rates (GDR) exceeded the critical threshold by 4.6x, meaning governance controls were degrading faster than organizations realized.

## Decision
Embed governance controls directly into the AI architecture (Pattern 06) as structural properties that cannot be bypassed, rather than relying on procedural compliance.

## Rationale
Architecture enforces. Documents advise. In regulated industries, advising is not enough. A content filter in the pipeline enforces content policy. A document describing content policy does not.

Governance-as-architecture means:
- Rate limits are infrastructure configs, not policy statements
- Content filtering is a pipeline stage, not a guideline
- Audit logging is automatic, not a manual process
- Model access is controlled by the gateway, not by team discipline
- Compliance routing is infrastructure, not developer responsibility

## Consequences

**Positive:**
- Governance controls cannot be accidentally bypassed
- Continuous, automated enforcement
- Measurable governance effectiveness (GDR tracking)
- Faster compliance audits (controls are inspectable infrastructure)
- Governance scales with the system automatically

**Negative:**
- Higher upfront architecture investment
- Requires governance and architecture teams to collaborate closely
- Over-constraining architecture can slow innovation
- Governance changes require infrastructure changes, not just policy updates

**Mitigations:**
- Use configuration-driven governance (policy-as-code) so changes do not require deployments
- Implement governance tiers: strict for high-risk use cases, lighter for low-risk
- Track GDR monthly to detect degradation before it becomes critical

## Research Basis
- GDR Paper: All three evaluated vendor platforms exceeded critical GDR threshold; pipeline GDR was 4.6x the critical threshold
- GAIF v1.0: 27,000-word architecture specification for governed AI systems

## Related Patterns
- Pattern 06: Governance-as-Architecture (15 variants)
- Pattern 05: LLMOps Pipeline (lifecycle governance)
- Pattern 13: Observability for AI (governance monitoring)

## GAIF-4 Relevance
GDR (Governance Decay Rate) is the primary metric. Target: below 0.03 per measurement period. Critical threshold: 0.05. Exceeding critical means governance controls are failing faster than they are being maintained.
