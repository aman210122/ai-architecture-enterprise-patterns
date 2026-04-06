# Pattern 12: Enterprise AI Platform
**Infrastructure stack building upward. 15 variants. Data -> Compute -> Platform -> API. Multi-cloud mapping table. BSC Pillar 4 reference architecture.**

Unique layout: vertical stack building UPWARD. Bottom (widest): Data Foundation (lakehouse, feature store, vector, semantic layer). Middle: Compute (GPU, inference, training, batch). Upper: Platform Services (workspaces, MLflow, CI/CD, monitoring). Top (narrowest): API Gateway. Right side: multi-cloud mapping table (Databricks, Azure, AWS).

| Platform Layer | Variant |
|---------------|---------|
| Delta/Iceberg | [Lakehouse](lakehouse-architecture/) |
| Multi-tenant | [Workspaces](workspace-management/) |
| Domain products | [Data Mesh](data-mesh-for-ai/) |
| Feature lifecycle | [Feature Store](feature-store/) |
| GPU scheduling | [GPU Cluster](gpu-cluster-management/) |
| vLLM/TGI | [Inference](inference-serving/) |
| Private endpoints | [Networking](networking-architecture/) |
| Distributed training | [Compute](compute-orchestration/) |
| MLflow/W&B | [Experiments](experiment-tracking/) |
| DAG pipelines | [ML Pipelines](ml-pipeline-orchestration/) |
| AI monitoring | [Monitoring](platform-monitoring/) |
| Eval in pipeline | [CI/CD](ci-cd-for-ai/) |
| Business glossary | [Semantic Layer](semantic-layer/) |
| Entity relationships | [Knowledge Graph](knowledge-graph-context/) |
| Real-time metadata | [Active Metadata](active-metadata/) |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
