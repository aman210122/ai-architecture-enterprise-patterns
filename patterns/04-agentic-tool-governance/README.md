# Pattern 04: Agentic AI with Tool Governance
**Tool registry grid + shield authorization gate + 8-stage invocation chain. 9 variants. Per-tool cost, health monitoring, side effect tracking.**

| Protocol/Model | Variant | When to Use |
|----------------|---------|-------------|
| Anthropic MCP | [MCP Protocol](mcp-protocol/) | Multi-tool, multi-provider. Standard. |
| Google A2A | [A2A Protocol](a2a-protocol/) | Agent-to-agent delegation. |
| Provider JSON | [Function Calling](function-calling/) | Single-provider, simple integration. |
| Tool chains | [Compound Tools](compound-tools/) | Tool A calls Tool B with cascading perms. |
| Agent code | [Sandboxed Execution](sandboxed-execution/) | Agent-generated code in isolated VMs. |
| Dynamic privilege | [Tool Escalation](tool-escalation/) | Runtime permission elevation with approval. |
| Tenant boundaries | [Multi-Tenant Isolation](multi-tenant-isolation/) | Shared tools, strict data separation. |
| Runtime discovery | [Tool Discovery](tool-discovery/) | Dynamic capability expansion. |
| v1/v2 coexist | [Tool Versioning](tool-versioning/) | Gradual migration with quality comparison. |

## Side Effect Classification
| Type | Example | Governance |
|------|---------|-----------|
| None | DB SELECT, calculator | Auto-approve |
| Reversible | Status change, soft delete | Log + notify |
| Irreversible | Email sent, payment processed | Require human approval |
| Cascading | Triggers downstream changes | Notify all system owners |

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
