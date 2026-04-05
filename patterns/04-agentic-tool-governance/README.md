# Pattern 04: Agentic AI with Tool Governance

**Governance on what agents can DO, not just what they say. 8 variants covering every tool integration and governance model.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Standardized tool servers with typed schemas | [MCP Protocol](mcp-protocol/) |
| Agent-to-agent collaboration across services | [A2A Protocol](a2a-protocol/) |
| Simplest tool integration, provider-native | [Function Calling](function-calling/) |
| Tools that chain other tools | [Compound Tools](compound-tools/) |
| Agent generates and runs code | [Sandboxed Execution](sandboxed-execution/) |
| Agent needs dynamic permission elevation | [Tool Escalation](tool-escalation/) |
| Shared tools across multiple tenants/BUs | [Multi-Tenant Isolation](multi-tenant-isolation/) |
| Agent discovers tools at runtime from registry | [Tool Discovery](tool-discovery/) |

## Platform Mapping

| Component | Azure | AWS | GCP | Databricks | Open Source |
|-----------|-------|-----|-----|------------|-------------|
| Tool Framework | Semantic Kernel | Bedrock Actions | Vertex Extensions | UC Functions | MCP SDK / LangChain |
| Execution | Azure Functions | Lambda | Cloud Functions | Serverless | Docker containers |
| Auth | Managed Identity | IAM Roles | Service Accounts | UC ACLs | Keycloak / OAuth |
| Sandbox | Container Apps | Fargate | Cloud Run | Cluster Policies | gVisor / Firecracker |
| Audit | App Insights | CloudTrail | Cloud Audit | MLflow | OpenTelemetry |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
