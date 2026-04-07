# Gateway Starter - Databricks Mosaic AI Gateway (Pattern 01)

Minimal configuration for routing LLM traffic through Databricks Mosaic AI Gateway.

## Prerequisites
- Databricks workspace with Unity Catalog enabled
- Mosaic AI Gateway feature enabled
- Databricks CLI configured

## Setup

### 1. Create a gateway route

```python
import mlflow.gateway

# Define a route to an external model
mlflow.gateway.create_route(
    name="clinical-gpt4o",
    route_type="llm/v1/chat",
    model={
        "name": "gpt-4o",
        "provider": "openai",
        "openai_config": {
            "openai_api_key": "{{secrets/ai-gateway/openai-key}}",
        }
    },
    rate_limits=[
        {"calls": 100, "key": "user", "renewal_period": "minute"},
        {"calls": 5000, "key": "route", "renewal_period": "minute"},
    ],
    guardrails={
        "input": {
            "safety": True,
            "pii": {"behavior": "BLOCK"},
        },
        "output": {
            "safety": True,
            "pii": {"behavior": "BLOCK"},
        }
    }
)
```

### 2. Query through the gateway

```python
import mlflow.gateway

response = mlflow.gateway.query(
    route="clinical-gpt4o",
    data={
        "messages": [
            {"role": "user", "content": "What are the contraindications for metformin?"}
        ]
    }
)
print(response)
```

### 3. View usage metrics

Gateway automatically logs token usage, latency, and guardrail decisions to Unity Catalog system tables.

```sql
SELECT
  request_timestamp,
  route_name,
  input_tokens,
  output_tokens,
  total_tokens,
  latency_ms,
  guardrail_pii_detected
FROM system.serving.gateway_logs
WHERE route_name = 'clinical-gpt4o'
ORDER BY request_timestamp DESC
LIMIT 100
```

## GAIF-4 Integration

Calculate T1PR from guardrail logs:

```sql
SELECT
  COUNT(CASE WHEN guardrail_output_blocked = TRUE THEN 1 END) * 1.0 / COUNT(*) as t1pr
FROM system.serving.gateway_logs
WHERE route_name = 'clinical-gpt4o'
  AND request_timestamp > CURRENT_DATE - INTERVAL 7 DAYS
```
