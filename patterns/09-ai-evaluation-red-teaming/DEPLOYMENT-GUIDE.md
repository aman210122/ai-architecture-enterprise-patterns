# Deployment Guide: AI Evaluation & Red Teaming
## Prerequisites: Golden dataset curated, eval framework selected, red team scheduled
## Steps
1. Curate golden dataset: 100+ Q&A pairs, human-verified, covering all use cases
2. Build adversarial suite: 40+ attack prompts across 5 categories
3. Design bias probes: 30+ paired tests across protected attributes
4. Select eval framework: MLflow Eval / RAGAS / DeepEval / custom
5. Configure LLM-as-judge: gpt-4o with 5-point rubric per dimension
6. Set up human eval workflow: 20% sample reviewed by SME
7. Define quality thresholds: accuracy > 0.85, safety > 0.95, bias < 0.05
8. Integrate eval in CI: run on every PR, block merge if below threshold
9. Set up regression testing: compare new version against baseline
10. Schedule red team: monthly adversarial testing by security team
11. Configure model comparison: same suite across all candidate models
12. GAIF-4: T1PR on bad outputs in eval, GDR on eval coverage decay
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
