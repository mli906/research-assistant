# STALE: Can LLM agents know when their memories are no longer valid? (arXiv:2605.06527)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Problem.** Implicit invalidation: new observations make old memories stale without explicit negation. Type I is a co-referential update; Type II is propagated invalidation of dependent beliefs.
- **Data.** 400 expert-validated scenarios, 1,200 queries, 100+ everyday topics, contexts up to 150K tokens. Synthetic, built from a 104-attribute ontology.
- **Metrics.** Accuracy on State Resolution (recognize the stale state), Premise Resistance (reject queries that presuppose a stale state) and Implicit Policy Adaptation (act on the updated state). LLM judge with 95.8% human agreement.
- **Results.** The best model (Gemini-3.1-pro) reaches 55.2% overall; premise resistance is near zero for most systems; Type II is much harder. Memory frameworks tested: LightMem, Zep, LiCoMemory, A-mem, mem0. The authors' CUPMem (write-side state adjudication) goes from 8.7% to 68.0%.
- **Limitations (stated).** One conflict pair per instance; synthetic dialogues; LLM judge; CUPMem needs a schema.
- **Critique.** Directly operationalizes the "freshness" property. In finance, stale KYC/suitability facts (risk tolerance, employment, sanctions status) fit Type II exactly. License CC BY 4.0.
