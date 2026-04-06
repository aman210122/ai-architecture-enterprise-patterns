# Deployment Guide: AI Security Architecture
## Prerequisites: Pattern 01 (Gateway), WAF, SIEM configured
## Steps
1. Layer 1 (Perimeter): WAF rules, DDoS protection, rate limiting, API key auth
2. Layer 2 (Input): injection classifier, content filter, input sanitization, length limits
3. Layer 3 (Model): access control, system prompt shielding, extraction detection
4. Layer 4 (Output): PII/PHI scan, toxicity filter, groundedness gate, watermarking
5. Layer 5 (Supply Chain): model provenance, dependency scan, weight hash verification
6. Configure AI SIEM: feed security events to Splunk/Sentinel with AI-specific rules
7. Build incident response playbooks: injection, extraction, data leak, model theft
8. GAIF-4: T1PR on attacks passing, GDR on defense effectiveness decay
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
