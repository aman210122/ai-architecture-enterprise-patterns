# Governance Metrics Starter (GAIF-4)

Minimal implementation for collecting and calculating T1PR and CFR from your pipeline logs.

## What It Does

1. Reads safety gate logs and compliance routing logs
2. Calculates T1PR (Type-1 Pass Rate) and CFR (Compliance Failure Rate)
3. Compares against GAIF-4 thresholds
4. Outputs a governance health report

## Usage

```python
from governance_metrics import GovernanceMetrics

metrics = GovernanceMetrics(
    safety_log_path="./logs/safety_gate.jsonl",
    compliance_log_path="./logs/compliance_router.jsonl"
)

report = metrics.calculate()
print(report.summary())

# Check thresholds
if report.t1pr > 0.05:
    print(f"WARNING: T1PR {report.t1pr:.4f} exceeds safe threshold 0.05")
if report.cfr > 0.0:
    print(f"CRITICAL: CFR {report.cfr:.4f} exceeds safe threshold 0.00")
```

## Thresholds

| Metric | Safe | Warning | Critical |
|--------|------|---------|----------|
| T1PR | < 0.05 | 0.05 - 0.15 | > 0.15 |
| CFR | 0.00 | 0.001 - 0.01 | > 0.01 |
| EMR | < 0.05 | 0.05 - 0.15 | > 0.15 |
| GDR | < 0.03 | 0.03 - 0.05 | > 0.05 |
