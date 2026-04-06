# Pattern 14: AI Product Architecture
**Complete product architectures showing how patterns P02-P13 compose into real products. 12 variants. Each variant is a product type enterprises actually build.**

| Product Type | Variant | Patterns Used |
|-------------|---------|---------------|
| Chatbot/Assistant | [Conversational AI](conversational-ai/) | P02, P03, P04, P06, P08 |
| Knowledge search | [Enterprise Search](enterprise-search/) | P02, P08, P10, P13 |
| Form/invoice processing | [Document Intelligence](document-intelligence/) | P02, P08, P09, P13 |
| Content/product recs | [Recommendation Engine](recommendation-engine/) | P02, P09, P10, P13 |
| In-app AI assistant | [Copilot Architecture](copilot-architecture/) | P02, P03, P04, P06, P11 |
| Clinical CDSS | [Clinical Decision Support](clinical-decision-support/) | P02, P07, P08, P09 |
| Insurance automation | [Claims Processing](claims-processing/) | P02, P03, P08, P09 |
| Agent assist + QA | [Contact Center AI](contact-center-ai/) | P02, P03, P09, P13 |
| Internal wiki + AI | [Knowledge Management](knowledge-management/) | P02, P05, P09, P13 |
| IDE integration | [Code Assistant](code-assistant/) | P03, P04, P05, P11 |
| Automated reports | [Report Generation](report-generation/) | P02, P03, P09, P10 |
| Process automation | [Workflow Automation](workflow-automation/) | P03, P04, P06, P09 |

## Pattern Composition
Each AI product is not a single pattern. It is a composition of multiple patterns:
- **Conversational AI** = RAG (P02) for knowledge + Agents (P03) for tasks + Tools (P04) for actions + Governance (P06) for safety + Compliance (P08) for PHI
- **Copilot** = Agents (P03) for orchestration + Tools (P04) for actions + LLMOps (P05) for deployment + Security (P11) for access control
- **Clinical CDSS** = RAG (P02) for evidence + Contamination (P07) for safety + Compliance (P08) for PHI + Evaluation (P09) for clinical validation

*[GAIF Observatory](https://github.com/aman210122/gaif-governance-observatory) | [Aman Sharma](https://linkedin.com/in/amansharmaarchitect)*
