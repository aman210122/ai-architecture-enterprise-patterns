# Deployment Guide: Compliance-Aware Data Routing

## Prerequisites
Pattern 01 (Gateway) deployed, data classification policy defined

## Deployment Steps
-e 1. Deploy sensitivity classification engine
2. Define routing rules per sensitivity level
3. Configure compliant endpoints (BAA / VPC / VPC-SC)
4. Wire classification into gateway
5. Test: PHI routed only to compliant endpoints
6. Test: consent-based routing
7. Configure cross-border rules if international
8. Deploy routing audit logging
9. Monitor: CFR for routing policy violations

## Validation Checklist
- [ ] Variants selected for your use case
- [ ] Platform mapping confirmed
- [ ] GAIF-4 metric thresholds defined
- [ ] Monitoring and alerting configured
- [ ] Rollback procedure documented and tested

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
