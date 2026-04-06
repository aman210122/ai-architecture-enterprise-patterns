# Pattern 11: AI Security Architecture
**Defense-in-depth: 5 layers from perimeter to supply chain. 12 variants. OWASP LLM Top 10 mapped to defense layers.**

Unique layout: vertical funnel narrowing from wide (perimeter) to narrow (supply chain). Each layer shows threats on left, defenses on right. Side panel maps OWASP LLM Top 10 to defense layers. AI SIEM and incident response panels.

| Defense Layer | Variant | OWASP |
|--------------|---------|-------|
| Direct+indirect injection | [Prompt Injection](prompt-injection-defense/) | LLM01 |
| Extraction detection | [Model Theft](model-theft-prevention/) | LLM10 |
| Training data audit | [Data Poisoning](data-poisoning-detection/) | LLM03 |
| Crafted failure inputs | [Adversarial Input](adversarial-input-defense/) | -- |
| LLM-specific WAF/DDoS | [Endpoint Security](ai-endpoint-security/) | LLM04 |
| AI-specific playbooks | [Incident Response](ai-incident-response/) | -- |
| Prevent prompt extraction | [Prompt Protection](system-prompt-protection/) | LLM07 |
| Model provenance, deps | [Supply Chain](supply-chain-security/) | LLM05 |
| Content+PII+halluc | [Output Filtering](output-safety-filtering/) | LLM02,06 |
| Multi-turn manipulation | [Jailbreak Defense](jailbreak-defense/) | LLM01 |
| Model-level RBAC | [AI IAM](ai-iam-architecture/) | LLM08 |
| Content attribution | [Watermarking](watermarking-provenance/) | -- |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
