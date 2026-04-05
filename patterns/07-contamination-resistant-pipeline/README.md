# Pattern 07: Contamination-Resistant Pipeline

**Prevent, detect, and recover from error propagation in multi-agent LLM pipelines. 12 variants from research-validated architectures.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Agents must not share state | [Isolation Barriers](isolation-barriers/) |
| Block contamination at ingestion | [Input Sanitization](input-sanitization/) |
| Independent validator at each stage | [Validation Checkpoints](validation-checkpoints/) |
| Shadow pipeline for divergence | [Canary Pipeline](canary-pipeline/) |
| Measure error propagation (T1PR) | [Contamination Percolation](contamination-percolation/) |
| Multiple models to catch inverted safety | [Redundant Generation](redundant-generation/) |
| Hold suspect outputs for human review | [Output Quarantine](output-quarantine/) |
| Need to retract contaminated outputs | [Rollback-Capable](rollback-capable/) |
| Find root cause of contamination | [Contamination Lineage](contamination-lineage/) |
| Keep serving on contamination (safer path) | [Graceful Degradation](graceful-degradation/) |
| Contamination leaking between pipelines | [Cross-Pipeline](cross-pipeline/) |
| Pipeline learns from past contamination | [Adaptive Immune System](immune-system/) |

## Research Connection

| Variant | Paper | Key Finding |
|---------|-------|-------------|
| Isolation Barriers | EMG | Collective delusion when agents share context |
| Contamination Percolation | ContamPerc | T1PR gap inversion diagnostic (~210K API calls) |
| Redundant Generation | EMG | Most safety-trained model produced worst drug interactions |
| Adaptive Immune System | GDR | Governance should improve over time, not decay |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
