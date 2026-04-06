# Deployment Guide: Tool Governance
## Prerequisites: Pattern 01 (Gateway), tool endpoints deployed
## Steps
1. Register tools: name, version, schema (MCP/A2A/JSON), health endpoint, timeout
2. Classify tools: read-only, read-write, side-effect, compound
3. Set permission policies: RBAC + ABAC per tool, rate limits
4. Configure authorization gateway (shield): check agent role + scope before execution
5. Set up input validation: JSON schema, injection scan, size limits
6. Deploy sandbox: isolated containers, CPU/mem limits, no-network default
7. Configure output validation: schema check, PHI/PII scan, size limits
8. Implement side effect tracking: classify, reversibility, notification rules
9. Set up immutable audit trail: full request/response, 7-year retention
10. Configure tool result cache: hash input -> cache output, TTL per tool
11. Deploy health monitoring: proactive checks, circuit breaker on failure
12. GAIF-4: T1PR on unauthorized side effects, CFR on permission violations
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
