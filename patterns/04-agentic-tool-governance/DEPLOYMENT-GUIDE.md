# Deployment Guide: Agentic AI with Tool Governance

## Prerequisites
Pattern 01 (Gateway) deployed, tool servers registered

## Deployment Steps
-e 1. Define tool schemas (MCP / A2A / function calling)
2. Configure per-tool permission policies
3. Set up tool authorization gateway
4. Configure sandbox environments for code execution
5. Deploy tool servers with health monitoring
6. Test: unauthorized tool calls blocked
7. Test: tool timeout and circuit breaker behavior
8. Promote to production
9. Monitor: tool invocation audit trail, side-effect logging

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
