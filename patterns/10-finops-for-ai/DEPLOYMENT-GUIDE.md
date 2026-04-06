# Deployment Guide: FinOps for AI
## Prerequisites: Pattern 01 (Gateway) for centralized metering, cost database
## Steps
1. Deploy token metering: count input/output tokens per call at gateway
2. Calculate per-query cost: tokens x price per model per provider
3. Set up team chargeback: allocate costs to business units
4. Configure budget policies: daily, monthly limits per team
5. Deploy cost anomaly detection: baseline daily spend, alert on deviation
6. Set up semantic cache: hash queries, cache responses, measure hit rate
7. Configure smart model routing: simple -> cheap model, complex -> expensive
8. Deploy batch processing: queue non-urgent work for off-peak
9. Build cost dashboard: real-time spend, trends, forecasts
10. Set up budget alerts: 80%/90%/100% of daily/monthly limit
11. Configure cost forecasting: project monthly spend from daily trends
12. Invoice reconciliation: match provider bills against internal metering
13. GAIF-4: T1PR on untracked spend, CFR on budget violations
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
