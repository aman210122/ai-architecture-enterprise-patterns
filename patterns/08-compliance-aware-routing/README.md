# Pattern 08: Compliance-Aware Data Routing
**CARES algorithm for zero-violation PHI routing. 14 variants. Based on PHI-GUARD research: 0 PHI violations across 30K MIMIC-IV queries.**

Research basis: PHI-GUARD paper (CARES algorithm, compliance-aware LLM routing, zero violations, TechRxiv DOI: 10.36227/techrxiv.177220388.80392106/v1).

| Routing Layer | Variant |
|--------------|---------|
| Core routing algorithm | [CARES Algorithm](cares-algorithm/) |
| 18 HIPAA identifier types | [PHI Detection Engine](phi-detection-engine/) |
| BAA-covered endpoints only | [BAA Routing](baa-routing/) |
| Jurisdiction-based routing | [Regional Compliance](regional-compliance/) |
| User consent status | [Consent Routing](consent-routing/) |
| Per-field masking | [Field Redaction](field-redaction/) |
| Synthetic replacement | [De-Identification](de-identification/) |
| Sensitivity-based encryption | [Encryption Router](encryption-routing/) |
| Non-reversible tokens | [Tokenization](tokenization/) |
| Geographic enforcement | [Data Residency](data-residency/) |
| Auto-delete + holds | [Retention Policy](retention-policy/) |
| RBAC+ABAC on data | [Data Access Control](access-control-data/) |
| Immutable decision log | [Routing Audit](routing-audit/) |
| Enterprise DLP connection | [DLP Integration](dlp-integration/) |

## GAIF-4 for Compliance Routing
| Metric | Target | PHI-GUARD Result |
|--------|--------|-----------------|
| CFR | 0.00 (zero tolerance) | 0.00 across 30K queries |
| Routing accuracy | > 0.99 | 0.997 |
| False positive rate | < 0.05 | 0.032 |
| Classification latency | < 50ms | 38ms avg |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
