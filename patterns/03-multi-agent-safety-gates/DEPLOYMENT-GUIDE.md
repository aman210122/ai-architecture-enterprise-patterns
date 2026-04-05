# Deployment Guide: Multi-Agent Safety Gates
## Prerequisites: Pattern 01 (Gateway), Pattern 04 (Tools) if agents need tools
## Steps
1. Define agent roles, system prompts (versioned), model per agent
2. Configure orchestrator: task planning, state management, memory
3. Set safety gate rules: T1PR thresholds, routing, escalation
4. Configure inter-agent communication: format, isolation
5. Per-agent monitoring: latency budget, token budget, cost
6. Model failover per agent: primary + backup
7. Checkpoint/resume: save state after each agent
8. Conditional routing: confidence thresholds, human escalation
9. Circuit breakers: timeout, retries, backoff
10. Deploy staging, contamination test suite
11. GAIF-4: T1PR per gate, EMR pipeline, CFR per agent, GDR weekly
12. Promote with per-agent dashboards
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
