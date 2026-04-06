# Deployment Guide: AI Security Architecture
## Prerequisites: Pattern 01 (Gateway) for centralized enforcement, SIEM configured
## Steps
1. Conduct AI threat modeling: OWASP LLM Top 10, MITRE ATLAS mapping
2. Map AI attack surfaces: prompts, system prompts, tools, training data, weights, APIs
3. Risk-score every AI endpoint by exposure, sensitivity, blast radius
4. Deploy prompt injection detection: classifier + regex for direct and indirect
5. Configure input sanitization: control chars, encoding attacks, length limits
6. Implement jailbreak detection: role-play, persona, multi-turn manipulation patterns
7. Deploy content shield: pre-model filtering for hate, CSAM, violence, self-harm
8. Configure model access control: per-model auth, scoped API keys, rate limits
9. Implement system prompt protection: extraction detection, prompt shielding
10. Deploy model theft prevention: query rate detection, output perturbation
11. Configure output filtering: harmful content, toxicity, policy violations
12. Implement PII/PHI leak prevention: scan every output for personal data
13. Deploy hallucination safety gate: block harmful medical/legal/financial claims
14. Set up AI content watermarking for provenance tracking
15. Configure model provenance: origin, training data, fine-tune history verification
16. Deploy dependency scanning: Hugging Face, PyPI model dependency audit
17. Implement weight integrity: cryptographic hash verification of model files
18. Create AI incident response playbooks: injection breach, data extraction, model theft
19. Configure AI-specific SIEM rules: prompt extraction attempts, unusual patterns
20. GAIF-4: T1PR on attacks, CFR on output violations, GDR on defense decay
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
