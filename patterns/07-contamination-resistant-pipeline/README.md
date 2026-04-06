# Pattern 07: Contamination-Resistant Pipeline
**Detect, isolate, validate, recover from contamination in multi-agent LLM systems. 12 variants. Based on EMG and ContamPerc research findings.**

Research basis: EMG paper (74 critical drug interaction events across 4,800 trials, collective delusion behavior, gap inversion), ContamPerc paper (contamination percolation in multi-agent graphs, T1PR metric).

| Defense Layer | Variant |
|--------------|---------|
| Full defense stack | [Standard Defense](standard-defense/) |
| Different families per agent | [Model Diversity](model-diversity/) |
| Architecture-enforced isolation | [Isolation Enforcement](isolation-enforcement/) |
| Multi-model agreement check | [Consensus Validation](consensus-validation/) |
| Trace claims to source | [Provenance Tracking](provenance-tracking/) |
| Agents converge on wrong answer | [Collective Delusion Monitor](collective-delusion-monitor/) |
| Safest model, worst outcomes | [Gap Inversion Diagnostic](gap-inversion-diagnostic/) |
| Spread through agent graph | [Contamination Percolation](contamination-percolation/) |
| Hold suspect outputs | [Quarantine Architecture](quarantine-architecture/) |
| Swap model, re-run | [Clean Re-Execution](clean-re-execution/) |
| Revert to clean checkpoint | [Rollback Recovery](rollback-recovery/) |
| Remove bad claims post-hoc | [Output Scrubbing](output-scrubbing/) |

## GAIF-4 for Contamination
| Metric | Application | Source |
|--------|-----------|--------|
| T1PR | Contamination passing filters | EMG paper |
| CFR | Percolation rate across agents | ContamPerc paper |
| EMR | Emergent misinformation (pipeline) | EMG paper |
| GDR | Detection effectiveness decay | GAIF-4 framework |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
