# Pattern 06: Governance-as-Architecture

**Governance built into the architecture, not bolted on. 14 variants covering measurement, automation, compliance, development, fairness, and testing.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Need quantitative metrics in every stage | [Embedded Governance](embedded-governance/) |
| Need real-time monitoring UI | [Governance Dashboard](governance-dashboard/) |
| Need to detect controls weakening | [Decay Detection](decay-detection/) |
| Want governance rules as testable code | [Policy-as-Code](policy-as-code/) |
| Continuous compliance, not quarterly audits | [Continuous Compliance](continuous-compliance/) |
| Immutable audit trail for regulators | [Audit Trail](audit-trail/) |
| Different controls per AI risk tier | [Risk-Tiered](risk-tiered/) |
| Central standards, BU autonomy | [Governance Federation](governance-federation/) |
| Catch issues during development | [Shift-Left Governance](shift-left-governance/) |
| Model docs as deployment gate | [Model Cards](model-cards/) |
| Serve explanations with every output | [XAI Explainability](xai-explainability/) |
| Ongoing bias measurement | [Bias & Fairness](bias-fairness/) |
| GDPR consent and data rights | [Consent & Data Rights](consent-data-rights/) |
| Test governance rules themselves | [Governance Testing](governance-testing/) |

## GAIF-4 Metrics

| Metric | Safe | Critical |
|--------|------|----------|
| T1PR | < 0.05 | > 0.15 |
| CFR | 0.00 | > 0.01 |
| EMR | 0.00 | > 0.05 |
| GDR | < 0.03 | > 0.05 |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
