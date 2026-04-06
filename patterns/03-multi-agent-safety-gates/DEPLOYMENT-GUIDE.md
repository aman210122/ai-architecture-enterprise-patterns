# Deployment Guide: Multi-Agent Safety Gates
## Prerequisites: Pattern 01 (Gateway) for model access, Pattern 04 (Tools) if agents use tools
## Steps
1. Select topology: linear (default), DAG, hierarchical, consensus, or other variant
2. Define agent roles: system prompts (versioned in git), model per agent, token limits
3. Configure orchestrator: task planner, state management, agent memory, failure handling
4. Set hexagonal gate rules: T1PR thresholds, content policies, confidence routing
5. Configure inter-agent message bus: structured JSON, isolation, audit logging
6. Set up per-agent monitoring: latency budget, token budget, cost tracking per agent
7. Configure model failover: primary + backup model per agent, auto-switch on 503
8. Implement checkpoint/resume: save state after each gate pass, resume on failure
9. Configure conditional routing: confidence < threshold routes to human queue
10. Set up circuit breakers: timeout per agent, max retries, exponential backoff
11. Deploy to staging, run contamination test suite (known bad inputs through pipeline)
12. GAIF-4: T1PR per gate, EMR at final gate, CFR per agent, GDR weekly trending
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
