# Pattern 07: Contamination-Resistant Pipeline

**Prevent, detect, and recover from error propagation in multi-agent LLM pipelines. 8 variants from research-validated architectures.**

Directly informed by research on emergent misinformation (EMG paper: 74 critical drug interaction events across 4,800 trials) and contamination percolation (ContamPerc paper: ~210K API calls, gap inversion diagnostic).

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Agents must not share state | [Isolation Barriers](isolation-barriers/) |
| Independent validator at each stage | [Validation Checkpoints](validation-checkpoints/) |
| Shadow pipeline for divergence detection | [Canary Pipeline](canary-pipeline/) |
| Need to retract contaminated outputs | [Rollback-Capable](rollback-capable/) |
| Measure error propagation through chains | [Contamination Percolation](contamination-percolation/) |
| Multiple models to catch inverted safety | [Redundant Generation](redundant-generation/) |
| Block contamination at ingestion | [Input Sanitization](input-sanitization/) |
| Pipeline learns from past contamination | [Adaptive Immune System](immune-system/) |

## Research Connection

| Variant | Research Paper | Key Finding |
|---------|---------------|-------------|
| Isolation Barriers | EMG | Collective delusion occurs when agents share context |
| Contamination Percolation | ContamPerc | T1PR gap inversion diagnostic detects propagation |
| Redundant Generation | EMG | Most safety-trained model produced worst drug interactions |
| Adaptive Immune System | GDR | Governance should improve over time, not decay |

## GAIF-4 Metrics for Contamination

| Metric | Role in Contamination Detection |
|--------|-------------------------------|
| T1PR | Contaminated outputs passing safety filters |
| EMR | Dangerous content only at pipeline level (not per-agent) |
| GDR | Contamination detection effectiveness degrading |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
