# Pattern 11: AI Security Architecture
**Layered defense for AI-specific threats. 12 variants. Input + model + output + supply chain + incident response. Not traditional AppSec. These are threats security teams do not know exist.**

Maps to: OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, ISO 42001

| Defense Layer | Variant |
|--------------|---------|
| Direct + indirect injection | [Prompt Injection Defense](prompt-injection-defense/) |
| Extraction detection | [Model Theft Prevention](model-theft-prevention/) |
| Training data integrity | [Data Poisoning Detection](data-poisoning-detection/) |
| Crafted failure inputs | [Adversarial Input Defense](adversarial-input-defense/) |
| LLM-specific WAF, DDoS | [AI Endpoint Security](ai-endpoint-security/) |
| AI-specific playbooks | [AI Incident Response](ai-incident-response/) |
| Prevent prompt extraction | [System Prompt Protection](system-prompt-protection/) |
| Model provenance, deps | [Supply Chain Security](supply-chain-security/) |
| Content + PII + halluc | [Output Safety Filtering](output-safety-filtering/) |
| Multi-turn manipulation | [Jailbreak Defense](jailbreak-defense/) |
| Model-level RBAC | [AI IAM Architecture](ai-iam-architecture/) |
| Content attribution | [Watermarking & Provenance](watermarking-provenance/) |

## GAIF-4 for Security
| Metric | Application |
|--------|-----------|
| T1PR | Attacks passing defenses |
| CFR | Policy violations in outputs |
| EMR | Dangerous outputs unblocked |
| GDR | Defense effectiveness decay |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
