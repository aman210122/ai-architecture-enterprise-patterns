# ADR-005: Quantitative Governance Metrics Over Qualitative Assessments

## Status
Accepted

## Context
Most AI governance frameworks rely on qualitative assessments: checklists, maturity models, risk ratings (low/medium/high), and periodic manual reviews. These approaches have three problems:

1. They are subjective. Two assessors can rate the same system differently.
2. They are point-in-time. A system that passes an annual review can degrade the next day.
3. They are not actionable. "Medium risk" does not tell an engineer what to fix.

As AI systems scale to multiple agents, models, and pipelines, qualitative governance cannot keep pace.

## Decision
Adopt computable governance metrics (GAIF-4) that can be measured automatically, continuously, and objectively.

## Rationale
Four metrics cover the critical dimensions of AI governance:

| Metric | What It Measures | Safe Threshold | Critical Threshold |
|--------|-----------------|----------------|-------------------|
| T1PR | Bad outputs passing safety filters | < 0.05 | > 0.15 |
| CFR | Outputs violating compliance policies | 0.00 | > 0.01 |
| EMR | Dangerous content emerging at pipeline level | < 0.05 | > 0.15 |
| GDR | Governance controls degrading over time | < 0.03 | > 0.05 |

Each metric is:
- Computable from system telemetry (no manual assessment needed)
- Continuous (measured on every request or at regular intervals)
- Objective (same inputs produce same measurements)
- Actionable (a high T1PR tells you to fix safety filters; a high GDR tells you to update configurations)

## Consequences

**Positive:**
- Objective, reproducible governance measurement
- Continuous monitoring instead of point-in-time reviews
- Early warning when governance degrades (GDR)
- Clear thresholds that trigger remediation
- Comparable across systems, teams, and time periods
- Audit-friendly (metrics provide evidence trail)

**Negative:**
- Requires instrumentation in the pipeline to collect metrics
- Thresholds may need calibration for specific domains
- Does not replace all qualitative assessment (ethical considerations, stakeholder impact)
- Initial setup cost for metric collection infrastructure

**Mitigations:**
- Start with one metric (T1PR is usually easiest) and add others incrementally
- Use the GAIF-4 toolkit (59 tests) to validate metric collection
- Complement quantitative metrics with periodic qualitative reviews for aspects metrics cannot capture

## Research Basis
- GAIF-4 v1.5: Four computable clinical AI safety metrics (Zenodo DOI: 10.5281/zenodo.19378438)
- GAIF v1.0: 27,000-word architecture specification (Zenodo DOI: 10.5281/zenodo.19341015)
- EMG Paper: EMR metric validated across 97,000 API calls and 4 model families
- ContamPerc Paper: T1PR metric validated across 210,000 API calls and 5 model families
- GDR Paper: GDR metric validated against 3 commercial AI platforms

## Related Patterns
- All patterns reference GAIF-4 metrics
- Pattern 06: Governance-as-Architecture (governance structure)
- Pattern 09: AI Evaluation and Red Teaming (metric validation)
- Pattern 13: Observability for AI (metric collection)

## GAIF-4 Relevance
This ADR is about adopting GAIF-4 itself. The GAIF Governance Observatory toolkit provides 59 automated tests for validating metric collection and threshold compliance.
