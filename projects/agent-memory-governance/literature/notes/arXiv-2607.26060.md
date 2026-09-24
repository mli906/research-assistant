# Large-scale chatbot validation through customer digital-twin simulations (arXiv:2607.26060)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core. The extraction attributes it to NatWest AI Research (UK bank). **Verify the affiliation on the PDF before citing it.**

- **Method.** Synthetic customer agents (SCAs) conditioned on real, *anonymised* historical conversations and transaction context (PII/PAN masked), with scaffolding and personality interventions. Validation combines an LLM judge (9 dimensions), SME testing, and red- and green-teaming.
- **Results.** 0.852 semantic similarity to real customers; 3.2% fidelity misclassification (24/750); Big-Five trait reproduction within 0.5 on a 1–5 scale.
- **Memory.** Single-session only.
- **License.** CC BY 4.0 (the paper). Data is not released.
- **Critique.** This is evidence of how a UK bank validates customer-facing chatbots pre-deployment. It is reusable as a method for building **synthetic multi-session customers** (see the brief's constraint that there is no real customer data). There are no persistent-memory tests. Twins tend to be too polite, so adversarial and vulnerable-customer behaviour needs explicit conditioning (FCA Consumer Duty relevance).
