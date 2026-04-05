# Pattern 06: Governance-as-Architecture

**Governance built into architecture, not bolted on. 15 variants. The largest pattern, directly integrates GAIF-4.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Quantitative metrics in every stage | [Embedded Governance](embedded-governance/) |
| Real-time monitoring UI | [Governance Dashboard](governance-dashboard/) |
| Detect controls weakening | [Decay Detection](decay-detection/) |
| Governance rules as testable code | [Policy-as-Code](policy-as-code/) |
| Continuous, not quarterly audits | [Continuous Compliance](continuous-compliance/) |
| Immutable audit trail | [Audit Trail](audit-trail/) |
| Different controls per risk tier | [Risk-Tiered](risk-tiered/) |
| Central standards, BU autonomy | [Governance Federation](governance-federation/) |
| Assess maturity, plan roadmap | [Governance Maturity Model](governance-maturity/) |
| Catch issues during development | [Shift-Left Governance](shift-left-governance/) |
| Model docs as deployment gate | [Model Cards](model-cards/) |
| Serve explanations with outputs | [XAI Explainability](xai-explainability/) |
| Ongoing bias measurement | [Bias & Fairness](bias-fairness/) |
| GDPR consent and data rights | [Consent & Data Rights](consent-data-rights/) |
| Test governance rules themselves | [Governance Testing](governance-testing/) |

## GAIF-4 Metrics

| Metric | Safe | Critical | What It Measures |
|--------|------|----------|-----------------|
| T1PR | < 0.05 | > 0.15 | Contaminated outputs passing filters |
| CFR | 0.00 | > 0.01 | Policy violations in completed requests |
| EMR | 0.00 | > 0.05 | Dangerous content at pipeline level |
| GDR | < 0.03 | > 0.05 | Governance effectiveness degrading |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
