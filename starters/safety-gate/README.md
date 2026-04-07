# Safety Gate Starter (Pattern 03)

A lightweight safety gate that sits between two agents in a multi-agent pipeline. Checks the output of Agent A before passing it to Agent B.

## What It Does

1. Receives output from upstream agent
2. Runs configurable safety checks (toxicity, PHI detection, hallucination markers)
3. If all checks pass, forwards to downstream agent
4. If any check fails, logs the failure, increments T1PR counter, and either blocks or flags the output

## Prerequisites

- Python 3.9+
- No external dependencies for the basic gate (uses regex and keyword matching)
- Optional: `transformers` library for model-based classification

## Usage

```python
from safety_gate import SafetyGate, SafetyConfig

config = SafetyConfig(
    gate_id="gate-agent-a-to-b",
    checks=["phi_detection", "toxicity_keywords", "confidence_floor"],
    action_on_fail="block",  # or "flag" to pass with warning
    confidence_threshold=0.3,
    log_path="./logs/safety_gate.jsonl"
)

gate = SafetyGate(config)

# In your pipeline
agent_a_output = agent_a.run(query)
result = gate.evaluate(agent_a_output)

if result.passed:
    agent_b_input = result.content
else:
    print(f"Blocked by {gate.gate_id}: {result.failed_checks}")
```

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| gate_id | required | Unique identifier for this gate |
| checks | all | List of checks to run |
| action_on_fail | "block" | "block" stops pipeline, "flag" passes with warning |
| confidence_threshold | 0.3 | Minimum confidence score to pass |
| log_path | "./logs" | Where to write gate decision logs |

## Available Checks

| Check | Method | What It Catches |
|-------|--------|----------------|
| phi_detection | Regex + patterns | SSN, MRN, DOB, phone, email patterns |
| toxicity_keywords | Keyword list | Known harmful terms and phrases |
| confidence_floor | Score threshold | Outputs with suspiciously low confidence |
| contradiction_check | Semantic comparison | Output contradicts the input query |
| length_anomaly | Statistical | Output length far outside normal range |

## Metrics Output

The gate logs every decision in JSONL format for T1PR calculation:

```json
{
  "timestamp": "2026-04-06T10:30:00Z",
  "gate_id": "gate-agent-a-to-b",
  "passed": false,
  "failed_checks": ["phi_detection"],
  "action": "block",
  "t1pr_increment": true
}
```

Aggregate these logs to calculate T1PR:
`T1PR = (outputs that passed with failures) / (total outputs evaluated)`
