# CRMArena-Pro: holistic assessment of LLM agents across business scenarios (arXiv:2505.18878)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core. Salesforce AI Research.

- **Design.** A real Salesforce org populated with synthetic data (29,101 B2B / 54,569 B2C records, 25 objects). 19 tasks; simulated users with sampled personas, multi-turn. **Confidentiality awareness** is tested with 2,140 queries per org asking for customer PII, internal operational data or confidential company knowledge; a GPT-4o judge checks for refusal.
- **Results.** About 58% single-turn success, about 35% multi-turn. **Near-zero inherent confidentiality awareness.** Adding confidentiality guidelines to the prompt helps but lowers task performance.
- **License.** CC BY-SA 4.0 (HF and GitHub).
- **Critique.** This is the only mainstream enterprise agent benchmark with a confidentiality axis, and it runs on the CRM platform most wealth managers use (Morgan Stanley Debrief writes notes to Salesforce). The confidentiality test is refusal-to-external-request, not *cross-client* or *cross-session* leakage via memory. Extending it to a multi-client memory setting is an obvious experiment.
