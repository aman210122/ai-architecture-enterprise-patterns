# Pattern 03: Multi-Agent Pipeline with Safety Gates

**Chain specialized LLM agents with safety checkpoints. 11 variants covering every orchestration topology.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Sequential decomposition | [Linear Chain](linear-chain/) |
| Parallel with merge validation | [DAG Orchestration](dag-orchestration/) |
| Supervisor coordinates workers | [Hierarchical](hierarchical/) |
| Human approval per risk tier | [Human-in-the-Loop](human-in-the-loop/) |
| Multiple independent opinions | [Consensus](consensus/) |
| Output must withstand challenge | [Adversarial Red/Blue](adversarial-red-blue/) |
| For/against structured arguments | [Debate](debate/) |
| Iterative self-improvement | [Reflection Loop](reflection-loop/) |
| Many agents, no coordinator | [Swarm](swarm/) |
| Non-blocking safety observer | [Parallel Monitor](parallel-monitor/) |
| Deterministic regulated workflows | [State Machine Agent](state-machine-agent/) |

## GAIF-4 Metrics for Multi-Agent

| Metric | Multi-Agent Application |
|--------|------------------------|
| T1PR | Contaminated outputs passing inter-agent gates |
| CFR | Policy violations in agent communication |
| EMR | Emergent dangerous content at pipeline level (EMG paper) |
| GDR | Gate effectiveness degrading over time |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Agent Framework | Semantic Kernel | Bedrock Agents | Agent Builder | Mosaic AI | LangGraph / CrewAI |
| Safety Gates | Content Safety | Guardrails | Model Armor | Mosaic GW | NeMo Guardrails |
| Orchestration | AI Agent Service | Step Functions | Vertex Pipelines | Workflows | LangGraph |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
