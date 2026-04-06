# Pattern 03: Multi-Agent Pipeline with Safety Gates
**Orchestrator + agent chain + hexagonal safety gates. 12 variants covering every orchestration topology. Per-agent cost/latency, conditional routing, checkpoint/resume, model failover.**

| Topology | Variant | When to Use |
|----------|---------|-------------|
| Sequential + checkpoints | [Linear Chain](linear-chain/) | Default for most pipelines. Simple, debuggable. |
| Parallel + merge validation | [DAG Orchestration](dag-orchestration/) | Independent branches can run concurrently. |
| Supervisor delegates | [Hierarchical](hierarchical/) | Clear authority hierarchy needed. |
| Human approval per risk | [Human-in-the-Loop](human-in-the-loop/) | Regulated workflows needing sign-off. |
| Multiple agents vote | [Consensus](consensus/) | High-stakes decisions (clinical, legal). |
| Generator + critic | [Adversarial Red/Blue](adversarial-red-blue/) | Content that needs adversarial hardening. |
| For/against + judge | [Debate](debate/) | Decisions with strong tradeoffs. |
| Generate, eval, revise | [Reflection Loop](reflection-loop/) | Quality must exceed threshold before delivery. |
| No coordinator, handoff | [Swarm](swarm/) | Horizontal scale, dynamic routing. |
| Non-blocking observer | [Parallel Monitor](parallel-monitor/) | Safety monitoring without latency cost. |
| Deterministic transitions | [State Machine](state-machine-agent/) | Regulated workflows with audit requirements. |
| Memory access control | [Memory Governance](memory-governance/) | GDPR compliance, memory isolation. |

## Research Connection
- EMG paper: 74 critical drug interaction events emerged at pipeline level (Final Gate catches what per-agent gates miss)
- ContamPerc: contamination percolation through shared agent context
- GAIF-4: T1PR per gate, EMR at final gate only

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
