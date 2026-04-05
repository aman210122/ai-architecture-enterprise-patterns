# Pattern 09: AI Evaluation & Red Teaming

**Systematic AI quality, safety, and compliance evaluation. 15 variants.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Find vulnerabilities | [Automated Red Teaming](automated-red-teaming/) |
| RAG quality evaluation | [RAGAS](ragas-evaluation/) |
| Scalable eval without humans | [LLM-as-Judge](llm-as-judge/) |
| Gold standard with human raters | [Human Eval](human-eval/) |
| Pre-deploy safety gate | [Safety Benchmarking](safety-benchmarking/) |
| Ongoing production quality | [Continuous Eval](continuous-eval/) |
| Test against attacks | [Adversarial Robustness](adversarial-robustness/) |
| Demographic bias testing | [Bias Evaluation](bias-evaluation/) |
| Catch version degradation | [Regression Testing](regression-testing/) |
| Healthcare/legal/finance eval | [Domain-Specific](domain-specific-eval/) |
| System prompt extraction risk | [Prompt Leakage](prompt-leakage/) |
| Per-model hallucination profile | [Hallucination Benchmarking](hallucination-benchmarking/) |
| Compare models head-to-head | [Multi-Model Comparison](multi-model-comparison/) |
| Test against regulations | [Compliance Evaluation](compliance-evaluation/) |
| Generate test data safely | [Synthetic Test Generation](synthetic-test-generation/) |

## GAIF-4 Metrics for Evaluation

| Metric | Evaluation Application |
|--------|----------------------|
| T1PR | Red team prompts bypassing safety |
| CFR | Compliance test failures |
| EMR | Dangerous outputs in evaluation |
| GDR | Evaluation effectiveness degrading |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
