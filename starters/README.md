# Starter Templates

Minimal working configurations to get started with the most common patterns. These are not production-ready. They are starting points that you should customize for your environment, security requirements, and scale.

## Available Starters

| Starter | Pattern | Platform | What It Does |
|---------|---------|----------|-------------|
| [gateway-databricks](gateway-databricks/) | P01 | Databricks | Mosaic AI Gateway with rate limits and content filter |
| [gateway-azure](gateway-azure/) | P01 | Azure | API Management policy for LLM routing |
| [gateway-opensource](gateway-opensource/) | P01 | Kong | Kong gateway config with AI plugin |
| [safety-gate](safety-gate/) | P03 | Python | Lightweight safety gate between two agents |
| [compliance-router](compliance-router/) | P08 | Python | Basic PHI detection and routing logic |
| [governance-metrics](governance-metrics/) | GAIF-4 | Python | Metric collection for T1PR and CFR |

## How to Use

1. Pick the starter that matches your pattern and platform
2. Read the starter's README for prerequisites
3. Copy the files into your project
4. Customize the configuration for your environment
5. Test in a non-production environment first

## Contributing Starters

If you have a working configuration for a pattern on a platform not covered here, contributions are welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md).
