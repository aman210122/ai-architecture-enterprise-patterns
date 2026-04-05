# Pattern 05: LLMOps Pipeline

**End-to-end LLM lifecycle management. 10 variants covering every cloud, platform, and specialized pipeline.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Azure ecosystem | [Azure LLMOps](azure-llmops/) |
| AWS ecosystem | [AWS LLMOps](aws-llmops/) |
| Google Cloud ecosystem | [GCP LLMOps](gcp-llmops/) |
| Databricks ecosystem | [Databricks LLMOps](databricks-llmops/) |
| Self-hosted, no vendor | [Open Source LLMOps](open-source-llmops/) |
| Multiple clouds | [Hybrid LLMOps](hybrid-llmops/) |
| Prompt iteration without model changes | [Prompt Engineering Pipeline](prompt-engineering/) |
| Comparing models with real traffic | [Model A/B Testing](model-ab-testing/) |
| Regulatory approval required | [Compliance-Gated Deployment](compliance-gated/) |
| Managing training data lifecycle | [Data Pipeline for LLMs](data-pipeline/) |

## Service Mapping

| Stage | Azure | AWS | GCP | Databricks | Open Source |
|-------|-------|-----|-----|------------|-------------|
| Experiment | Azure ML | SageMaker | Vertex AI | MLflow | MLflow / W&B |
| Evaluate | AI Foundry | Bedrock Eval | Vertex Eval | MLflow Evaluate | RAGAS / DeepEval |
| CI/CD | Azure DevOps | CodePipeline | Cloud Build | Asset Bundles | GitHub Actions |
| Deploy | ML Endpoints | SM Endpoints | Vertex Endpoints | Model Serving | ArgoCD |
| Monitor | Azure Monitor | CloudWatch | Cloud Monitor | Lakehouse Monitor | Prometheus |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
