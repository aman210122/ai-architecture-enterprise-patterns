# ADR-002: Safety Gates Between Agents, Not Just at Boundaries

## Status
Accepted

## Context
The default approach to AI safety in multi-agent pipelines is to place safety filters at the system input and output. User query goes through a content filter on the way in, final response goes through a content filter on the way out.

This approach fails for multi-agent systems because dangerous content can emerge at intermediate stages. In experiments with 4,800 clinical trials across 4 model families, 74 critical drug interaction events were generated spontaneously by agents at intermediate pipeline stages with no adversarial input. Output-only filtering missed these because the final agent sometimes "cleaned up" the dangerous intermediate content into plausible-sounding but clinically incorrect responses.

## Decision
Place safety gates between every agent handoff in a multi-agent pipeline (Pattern 03), not just at system input and output.

## Rationale
Emergent misinformation (EMR) is a pipeline-level phenomenon. Per-agent safety filters may pass individually while the combined pipeline produces dangerous outputs. Intermediate safety gates catch contamination at the point of origin rather than after it has propagated and compounded through downstream agents.

The cost of intermediate filtering (additional latency and compute per gate) is negligible compared to the risk of undetected dangerous outputs in safety-critical domains.

## Consequences

**Positive:**
- Catches contamination at point of origin
- Prevents error compounding across agents
- Enables per-stage T1PR measurement
- Makes debugging easier (know which agent produced the problem)
- Reduces blast radius of any single agent failure

**Negative:**
- Adds latency at each handoff (typically 50-200ms per gate)
- Increases token usage (each gate consumes tokens for evaluation)
- Requires defining safety criteria for intermediate outputs, not just final outputs
- More complex pipeline orchestration

**Mitigations:**
- Use lightweight classifiers for intermediate gates, full LLM-based evaluation only at final output
- Run gates asynchronously where real-time response is not required
- Define gate criteria based on the receiving agent's requirements, not generic safety rules

## Research Basis
- EMG Paper: 74 critical drug interaction events across 4,800 trials; collective delusion behavior where agents reinforced each other's errors
- ContamPerc Paper: T1PR gap inversion diagnostic showing contamination propagation patterns

## Related Patterns
- Pattern 03: Multi-Agent Safety Gates
- Pattern 07: Contamination-Resistant Pipeline
- Pattern 09: AI Evaluation and Red Teaming

## GAIF-4 Relevance
Intermediate gates enable per-stage T1PR and EMR measurement. Without them, you can only measure these metrics at system level and cannot identify which agent is the source of failures.
