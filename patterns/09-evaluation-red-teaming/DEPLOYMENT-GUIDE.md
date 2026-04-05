# Deployment Guide: AI Evaluation & Red Teaming

## Prerequisites
At least one AI use case deployed, test dataset available

## Deployment Steps
-e 1. Define evaluation metrics per use case
2. Create baseline test suite (golden dataset)
3. Set up automated evaluation pipeline
4. Run safety benchmarking before production
5. Configure red teaming (adversarial prompt generation)
6. Deploy continuous evaluation on production traffic sample
7. Set up regression testing for version updates
8. Create domain-specific evaluation rubrics
9. Wire evaluation results into Pattern 05 deployment gates

## Validation Checklist
- [ ] All variants selected for your use case
- [ ] Platform mapping confirmed (Azure / AWS / GCP / Databricks / OSS)
- [ ] GAIF-4 metric thresholds defined
- [ ] Monitoring and alerting configured
- [ ] Rollback procedure documented and tested
- [ ] Compliance review completed (if applicable)

## GAIF-4 Integration
Every deployment should include GAIF-4 metric collection. See [Embedded Governance](../06-governance-as-architecture/embedded-governance/) for implementation details.

*[AI Architecture Enterprise Patterns](https://github.com/aman210122/ai-architecture-enterprise-patterns) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
