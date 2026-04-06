# Deployment Guide: Compliance-Aware Routing
## Prerequisites: Pattern 01 (Gateway), BAA agreements, DLP tools
## Steps
1. Inventory data types: PHI (18 HIPAA identifiers), PII, sensitive, clean
2. Map endpoints: BAA-compliant, standard, redact-and-route, block
3. Deploy CARES classifier: regex + NER + ML hybrid for PHI/PII detection
4. Configure PHI routing: all PHI queries to BAA endpoint only
5. Configure PII redaction: Presidio/Purview strips PII before standard endpoint
6. Set up block rules: harmful content, policy violations never reach models
7. Configure audit trail: immutable log of every routing decision
8. Integrate enterprise DLP: sync rules with Presidio/Purview/Macie
9. Configure consent checking: verify user opt-in before AI processing
10. Set up multi-jurisdiction routing: apply strictest applicable regulation
11. Configure de-identification: Safe Harbor or Expert Determination for clinical
12. Build regulatory evidence package: on-demand audit reports
13. GAIF-4: T1PR on PHI reaching non-BAA (must be 0.00), CFR on violations
14. Monthly: review false positive rate, tune classifier thresholds
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
