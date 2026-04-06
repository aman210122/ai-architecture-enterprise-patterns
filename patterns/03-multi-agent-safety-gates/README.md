# Pattern 03: Multi-Agent Pipeline with Safety Gates

Orchestrator + agent chain + hexagonal safety gates. Per-agent model badges, cost tracking, conditional routing, checkpoint/resume.

**Unique Layout:** Orchestrator bar (Task Planner, State, Memory, Config) + agent chain with hexagonal gate barriers.

---

## Variants

| Variant | Focus | Demo |
|---------|-------|------|
| Linear Chain | Sequential with checkpoints | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/linear-chain/index.html) |
| DAG Orchestration | Parallel branches, merge validation | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/dag-orchestration/index.html) |
| Hierarchical | Supervisor delegates to workers | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/hierarchical/index.html) |
| Human-in-the-Loop | Human approval per risk tier | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/human-in-the-loop/index.html) |
| Consensus | Multiple agents vote | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/consensus/index.html) |
| Adversarial Red/Blue | Generator + critic red team | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/adversarial-red-blue/index.html) |
| Debate | For/against + judge | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/debate/index.html) |
| Reflection Loop | Generate, evaluate, revise | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/reflection-loop/index.html) |
| Swarm | No coordinator, handoff-based | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/swarm/index.html) |
| Parallel Monitor | Non-blocking safety observer | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/parallel-monitor/index.html) |
| State Machine | Deterministic transitions | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/state-machine-agent/index.html) |
| Memory Governance | Agent memory access, GDPR | [Launch Demo](https://aman210122.github.io/ai-architecture-enterprise-patterns/patterns/03-multi-agent-safety-gates/memory-governance/index.html) |

**Research:** EMG paper (74 drug interactions at pipeline level) | GAIF-4: T1PR per gate, EMR at final gate

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
