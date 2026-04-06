# Pattern 07: Contamination-Resistant Pipeline
**Vertical barrier walls between stages. Quarantine zone catches contaminated outputs. Based on EMG research (74 critical drug interactions across 4,800 trials).**

Unique layout: horizontal data flow with thick vertical BARRIER WALLS. Failed data diverts DOWN to red-bordered QUARANTINE ZONE. Central Contamination Detection Engine monitors all barriers.

| Defense Layer | Variant | When to Use |
|--------------|---------|-------------|
| Contamination scoring | [Contamination Detection](contamination-detection/) | Default. T1PR at every barrier. |
| Agent output consistency | [Cross-Agent Validation](cross-agent-validation/) | Multi-agent pipelines with data dependency. |
| Quarantine lifecycle | [Quarantine Management](quarantine-management/) | Review, classify, retrain from quarantined data. |
| Safety paradox | [Gap Inversion Diagnostic](gap-inversion-diagnostic/) | When safer models produce worse outcomes. |
| Multi-agent amplification | [Collective Delusion Defense](collective-delusion-defense/) | Agents reinforcing hallucinations. |
| Citation verification | [Source Grounding](source-grounding/) | Every claim must trace to source. |
| NLI + embedding check | [Hallucination Firewall](hallucination-firewall/) | Block fabricated claims at barrier. |
| Cross-model T1PR | [Model Comparison Safety](model-comparison-safety/) | Compare contamination across models. |
| Origin tracing | [Contamination Lineage](contamination-lineage/) | Trace contamination to root cause. |
| Graph isolation | [Percolation Defense](percolation-defense/) | Prevent contamination spread. ContamPerc. |
| Drug interaction DB | [Clinical Safety Gate](clinical-safety-gate/) | Healthcare: verify clinical claims. |
| Pipeline-level only | [Pipeline-Level EMR](pipeline-level-emr/) | Emergent content from agent combination. |

## Research Connection
- EMG paper (DOI: 10.5281/zenodo.19411743): 74 critical drug interactions, collective delusion, gap inversion
- ContamPerc paper (IEEE Access): contamination percolation, T1PR metric
- GAIF-4: T1PR per barrier, EMR at final wall, GDR weekly

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
