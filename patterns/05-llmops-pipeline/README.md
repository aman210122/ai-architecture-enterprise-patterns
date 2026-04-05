# Pattern 05: LLMOps Pipeline
**Full LLM lifecycle: develop, test, build, deploy, monitor, operate. 12 variants. SVG architecture diagram with click-to-detail panels.**

| Lifecycle Area | Variant |
|---------------|---------|
| Prompt versioning | [Prompt Lifecycle](prompt-lifecycle/) |
| Versioned models | [Model Registry](model-registry/) |
| Automated testing | [Evaluation Harness](evaluation-harness/) |
| Version comparison | [A/B Testing](ab-testing/) |
| Gradual rollout | [Canary Deployment](canary-deployment/) |
| Auto revert | [Rollback Strategy](rollback-strategy/) |
| Behavior change | [Drift Detection](drift-detection/) |
| User signals | [Feedback Integration](feedback-integration/) |
| Token budgets | [Cost Optimization](cost-optimization/) |
| Scaling rules | [Capacity Planning](capacity-planning/) |
| LLM-specific playbooks | [Incident Response](incident-response/) |
| Audit evidence | [Compliance Audit](compliance-audit/) |

## GAIF-4 for LLMOps
| Metric | Measured At | Safe | Critical |
|--------|-----------|------|----------|
| T1PR | Output quality monitoring | < 0.05 | > 0.15 |
| CFR | Policy compliance checks | 0.00 | > 0.01 |
| EMR | Drift from baseline | < 0.05 | > 0.15 |
| GDR | All metrics trending | < 0.03 | > 0.05 |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
