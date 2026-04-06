# Deployment Guide: Compliance-Aware Data Routing
## Prerequisites: Pattern 01 (Gateway), PHI detection engine, BAA agreements with model providers
## Steps
1. Deploy data sensitivity classifier (auto-classify every data element)
2. Configure PHI detection engine: all 18 HIPAA identifier types
3. Set up sensitivity scoring (0-1 per element, not binary)
4. Implement CARES algorithm as core routing logic
5. Configure BAA-aware model router: PHI only to BAA endpoints
6. Set up regional compliance routing (HIPAA/GDPR/CCPA/state)
7. Implement consent-based routing (opt-in/out status check)
8. Deploy field-level redaction: MRN, DOB, SSN masking per policy
9. Configure de-identification pipeline: synthetic replacement
10. Set up encryption routing: level per sensitivity (field/transit/rest)
11. Implement tokenization for analytics workloads
12. Configure data residency enforcement (geo-fencing)
13. Deploy retention policy engine (auto-delete + litigation hold)
14. Set up data-level access control (RBAC+ABAC per element)
15. Configure routing decision log: immutable, every decision
16. Implement post-routing compliance verification
17. Connect DLP integration (Purview/Macie/Cloud DLP)
18. GAIF-4: CFR zero tolerance, routing accuracy, false positive rate
19. Routing latency SLA: < 50ms per decision
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
