# Pattern 12: Enterprise AI Platform
**The infrastructure all AI patterns run on. 12 variants. Data foundation, compute, platform services, networking. Multi-cloud: Databricks, Azure AI Foundry, Snowflake, GCP Vertex, AWS Bedrock.**

| Platform Layer | Variant |
|---------------|---------|
| Unified AI storage | [Lakehouse Architecture](lakehouse-architecture/) |
| Multi-tenant isolation | [Workspace Management](workspace-management/) |
| Domain data products | [Data Mesh for AI](data-mesh-for-ai/) |
| Feature lifecycle | [Feature Store](feature-store/) |
| GPU scheduling | [GPU Cluster Management](gpu-cluster-management/) |
| Model serving at scale | [Inference Serving](inference-serving/) |
| Private connectivity | [Networking Architecture](networking-architecture/) |
| Training + batch | [Compute Orchestration](compute-orchestration/) |
| MLflow/W&B | [Experiment Tracking](experiment-tracking/) |
| DAG pipelines | [ML Pipeline Orchestration](ml-pipeline-orchestration/) |
| AI-specific monitoring | [Platform Monitoring](platform-monitoring/) |
| Eval in CI/CD | [CI/CD for AI](ci-cd-for-ai/) |

## Platform Stack (BSC reference)
| Layer | Databricks | Azure | AWS | GCP |
|-------|-----------|-------|-----|-----|
| Data | Unity Catalog | ADLS | S3/Glue | BigQuery |
| Compute | Serverless | AI Foundry | SageMaker | Vertex |
| Models | Mosaic AI | Azure OpenAI | Bedrock | Gemini |
| Gateway | Mosaic GW | API Mgmt | API GW | Apigee |
| Vector | Vector Search | AI Search | OpenSearch | Vertex Search |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
