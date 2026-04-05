# Pattern 04: Agentic AI with Tool Governance

**Governance on what agents can DO. 9 variants covering every tool protocol and governance model.**

## Which Variant Should You Use?

| Your situation | Variant |
|---------------|---------|
| Typed tool schemas, server-side | [MCP Protocol](mcp-protocol/) |
| Agent-to-agent collaboration | [A2A Protocol](a2a-protocol/) |
| Provider-native, simplest | [Function Calling](function-calling/) |
| Tools chaining other tools | [Compound Tools](compound-tools/) |
| Agent generates and runs code | [Sandboxed Execution](sandboxed-execution/) |
| Dynamic permission elevation | [Tool Escalation](tool-escalation/) |
| Shared tools, tenant boundaries | [Multi-Tenant Isolation](multi-tenant-isolation/) |
| Runtime tool discovery | [Tool Discovery](tool-discovery/) |
| Tool v1/v2 coexist, migration | [Tool Versioning](tool-versioning/) |

## GAIF-4 Metrics for Tools

| Metric | Tool Governance Application |
|--------|---------------------------|
| T1PR | Unauthorized side-effects passing checks |
| CFR | Tool calls violating permission policies |
| EMR | Dangerous tool chains at pipeline level |
| GDR | Authorization effectiveness degrading |

*Governance: [GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | Designed by [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
