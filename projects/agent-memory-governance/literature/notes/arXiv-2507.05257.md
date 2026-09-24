# MemoryAgentBench: Evaluating memory in LLM agents via incremental multi-turn interactions (arXiv:2507.05257)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Design.** Four competencies: Accurate Retrieval, Test-Time Learning, Long-Range Understanding and Selective Forgetting. Inputs are fed incrementally in chunks. 2,071 questions over 103K–1.44M-token contexts. Reuses existing datasets (LongMemEval, ∞-Bench, DetectiveQA, BANKING77, and others) plus new EventQA and FactConsolidation (counterfactual edit pairs, single- and multi-hop).
- **Metrics.** Accuracy, F1, Recall@5 depending on task.
- **Results.** RAG wins on retrieval (BM25 averages 60.5%); long context wins on TTL/LRU (GPT-4o 50.0/54.9). Selective forgetting is the critical gap: at most 28% on multi-hop FactConsolidation for every method; o4-mini drops to 14.0 at 32K context.
- **Limitations (stated).** Budget-limited set of memory agents.
- **Critique.** "Selective forgetting" here means overwrite with newer facts, not deletion on request. It is freshness, not erasure, and this conflation is common across memory benchmarks. Code MIT, data CC BY 4.0.
