# Deployment Guide: AI Product Architecture
## Prerequisites: Underlying patterns deployed (varies by product type)
## General Steps (adapt per product type)
1. Identify product type and map to required underlying patterns
2. Deploy prerequisite patterns: gateway (P01), RAG (P02), agents (P03) as needed
3. Build product frontend: conversation UI, search UI, copilot widget
4. Configure intent routing: classify user requests, route to appropriate backend
5. Set up context management: session handling, history, personalization
6. Configure multi-channel delivery: web, mobile, API, embedded
7. Implement human handoff/escalation rules (confidence thresholds)
8. Set up persona/brand voice for response generation
9. Configure product-level guardrails (on top of pattern-level guardrails)
10. Deploy product analytics: task completion, resolution rate, CSAT, adoption
11. Implement feedback loop: user signals improve routing and responses
12. Configure product-level observability (P13): quality, latency, cost per product
13. Set up A/B testing for product features (not just model versions)
14. Product-level GAIF-4: aggregate underlying pattern metrics per product
15. Launch to pilot users, iterate based on feedback, then scale
*[Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
