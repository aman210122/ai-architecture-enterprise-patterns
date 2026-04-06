# Pattern 09: AI Evaluation & Red Teaming
**Test inputs feed the Eval Engine. 2x3 score card grid shows quality across 6 dimensions. 15 variants covering every evaluation approach.**

Unique layout: left column (test inputs: golden, adversarial, bias, regression), center (eval engine with LLM judge + rubric + human eval + thresholds), right (2x3 score card grid: accuracy, safety, fairness, groundedness, robustness, latency). Overall verdict bar at bottom.

| Eval Approach | Variant |
|--------------|---------|
| Curated Q&A pairs | [Golden Dataset](golden-dataset/) |
| Jailbreak, injection | [Adversarial Testing](adversarial-testing/) |
| Demographic parity | [Bias & Fairness](bias-fairness/) |
| NLI entailment | [Groundedness Eval](groundedness-eval/) |
| Consistency scoring | [Robustness Testing](robustness-testing/) |
| P50/P95/P99 SLA | [Latency Benchmarking](latency-benchmarking/) |
| gpt-4o evaluator | [LLM-as-Judge](llm-as-judge/) |
| 20% SME review | [Human Evaluation](human-eval/) |
| Version comparison | [Regression Testing](regression-testing/) |
| Monthly red team | [Red Team Operations](red-team-ops/) |
| Quality gate in PR | [Eval in CI/CD](eval-in-ci/) |
| Multi-model scoring | [Model Comparison](model-comparison/) |
| ToxiGen, BBQ, BOLD | [Safety Benchmarks](safety-benchmarks/) |
| PharmD panel | [Clinical Evaluation](clinical-eval/) |
| MLflow vs RAGAS | [Eval Framework](eval-framework/) |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
