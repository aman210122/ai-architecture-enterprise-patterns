# Architecture Decision Records (ADRs)

This folder contains Architecture Decision Records documenting the key design decisions behind these patterns. ADRs explain **why** each architectural choice was made, not just what it is.

Each ADR follows a consistent structure: context (what problem existed), decision (what we chose), rationale (why), consequences (tradeoffs), and connections to specific patterns and GAIF-4 metrics.

## Index

| ADR | Decision | Status |
|-----|----------|--------|
| [ADR-001](ADR-001-unified-gateway.md) | Unified AI Gateway over per-team API keys | Accepted |
| [ADR-002](ADR-002-safety-gates-between-agents.md) | Safety gates between agents, not just at boundaries | Accepted |
| [ADR-003](ADR-003-compliance-in-infrastructure.md) | Compliance routing in infrastructure, not application code | Accepted |
| [ADR-004](ADR-004-governance-as-architecture.md) | Governance embedded in architecture, not in documents | Accepted |
| [ADR-005](ADR-005-quantitative-governance-metrics.md) | Quantitative governance metrics over qualitative assessments | Accepted |

## Template

To propose a new ADR, use this structure:

```markdown
# ADR-NNN: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[What problem or situation prompted this decision?]

## Decision
[What did we decide to do?]

## Rationale
[Why did we choose this over alternatives?]

## Consequences
[What are the positive and negative results?]

## Related Patterns
[Which patterns from this repo are relevant?]

## GAIF-4 Relevance
[Which metrics does this decision affect?]
```
