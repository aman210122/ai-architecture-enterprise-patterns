# Pattern 05: LLMOps Pipeline

**End-to-end LLM lifecycle management. Experiment, evaluate, deploy, and monitor. 6 variants for every major cloud and platform.**

## Which Variant Should You Use?

| Your stack | Variant |
|-----------|---------|
| Microsoft / Azure | [Azure LLMOps](azure-llmops/) |
| Amazon Web Services | [AWS LLMOps](aws-llmops/) |
| Google Cloud | [GCP LLMOps](gcp-llmops/) |
| Databricks | [Databricks LLMOps](databricks-llmops/) |
| Self-hosted / no vendor | [Open Source LLMOps](open-source-llmops/) |
| Multiple clouds | [Hybrid LLMOps](hybrid-llmops/) |

## Architecture

**Development Pipeline:** Experiment -> Train/Fine-Tune -> Evaluate -> Register

**Operations Pipeline:** CI/CD -> Deploy (canary) -> Monitor -> Feedback Loop

## Service Mapping

| Stage | Azure | AWS | GCP | Databricks | Open Source |
|-------|-------|-----|-----|------------|-------------|
| Experiment | Azure ML | SageMaker | Vertex AI | MLflow | MLflow / W&B |
| Evaluate | AI Foundry Eval | Bedrock Eval | Vertex Eval | MLflow Evaluate | RAGAS / DeepEval |
| CI/CD | Azure DevOps | CodePipeline | Cloud Build | Asset Bundles | GitHub Actions |
| Deploy | Azure ML Endpoints | SageMaker Endpoints | Vertex Endpoints | Model Serving | ArgoCD / Helm |
| Monitor | Azure Monitor | CloudWatch | Cloud Monitoring | Lakehouse Monitor | Prometheus |
| IaC | Bicep / ARM | CDK / CFN | Terraform | Terraform | Terraform / Helm |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
