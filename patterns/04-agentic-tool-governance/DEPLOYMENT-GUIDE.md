# Deployment Guide: Tool Governance
## Prerequisites: Pattern 01 (Gateway), tool servers deployed
## Steps
1. Define tool schemas (MCP/A2A/function calling)
2. Configure per-tool permission policies (RBAC+ABAC)
3. Set up tool authorization gateway
4. Configure sandbox environments (containers, resource limits)
5. Input validation: JSON schema, injection detection, size limits
6. Output validation: schema compliance, PHI scan, size check
7. Side effect tracking: classify, assess reversibility, notify
8. Audit trail: full request/response, immutable, 7-year retention
9. Secret management: per-tool API keys, rotation, no secrets in logs
10. Health monitoring: proactive checks, circuit breaker, failover
11. Rate limiting: per-tool, per-agent, per-team
12. GAIF-4: T1PR on side effects, CFR on permissions, GDR weekly
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
