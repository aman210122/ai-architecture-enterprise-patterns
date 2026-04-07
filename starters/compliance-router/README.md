# Compliance Router Starter (Pattern 08)

Basic PHI detection and routing logic. Routes queries containing PHI to compliant endpoints and non-sensitive queries to standard endpoints.

## What It Does

1. Receives a query from the gateway
2. Classifies whether the query contains PHI
3. Routes to the appropriate endpoint based on classification
4. Logs the routing decision for CFR calculation

## Prerequisites
- Python 3.9+
- No external dependencies for basic regex-based detection

## Usage

```python
from compliance_router import ComplianceRouter, RouterConfig

config = RouterConfig(
    compliant_endpoint="https://compliant-openai.internal/v1/chat",
    standard_endpoint="https://standard-openai.internal/v1/chat",
    log_path="./logs/compliance_router.jsonl"
)

router = ComplianceRouter(config)
result = router.route("What medications is patient John Smith taking?")

print(f"Routed to: {result.endpoint}")
print(f"PHI detected: {result.phi_detected}")
print(f"CFR so far: {router.cfr:.4f}")
```
