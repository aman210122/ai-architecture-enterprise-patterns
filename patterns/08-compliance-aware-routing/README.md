# Pattern 08: Compliance-Aware Routing (CARES)
**Diamond decision tree routing queries to correct endpoints. PHI to BAA, PII redacted, clean to standard. Based on PHI-GUARD research (zero violations, 30K queries).**

Unique layout: CARES classifier on left, diamond decision nodes branching to 4 endpoint paths. Visual decision tree, not pipeline.

| Compliance Area | Variant | When to Use |
|----------------|---------|-------------|
| CARES algorithm | [CARES Algorithm](cares-algorithm/) | Default. Full classification pipeline. |
| PHI detection + BAA | [PHI Routing](phi-routing/) | Healthcare with BAA endpoints. |
| PII strip + route | [PII Redaction](pii-redaction/) | Financial, insurance PII handling. |
| BAA lifecycle | [BAA Management](baa-endpoint-management/) | Managing provider agreements. |
| End-to-end HIPAA | [HIPAA Compliance](hipaa-compliance/) | Healthcare regulatory compliance. |
| EU data residency | [GDPR Routing](gdpr-routing/) | European data protection. |
| State-specific rules | [State Privacy Laws](state-privacy-laws/) | CCPA, CPRA, state regulations. |
| Multiple regulations | [Multi-Jurisdiction](multi-jurisdiction/) | Cross-border data flows. |
| 4-level classification | [Sensitivity Classification](sensitivity-classification/) | Data classification system. |
| Enterprise DLP | [DLP Integration](dlp-integration/) | Presidio, Purview, Macie. |
| User opt-in/out | [Consent Routing](consent-routing/) | GDPR/CCPA consent flows. |
| Safe Harbor / Expert | [De-Identification](de-identification/) | Clinical de-identification. |
| Immutable logging | [Audit Trail](audit-trail/) | 7-year compliance retention. |
| On-demand evidence | [Regulatory Evidence](regulatory-evidence/) | Audit packages for regulators. |

## Research Connection
- PHI-GUARD (TechRxiv DOI: 10.36227/techrxiv.177220388): CARES algorithm, zero violations
- Submitted IEEE JBHI (Manuscript JBHI-01214-2026)
- 30,247 MIMIC-IV queries classified with zero PHI leaks

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
