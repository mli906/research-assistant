# The Price of Safety: benign-case utility and token overhead of memory-poisoning defenses (arXiv:2609.22818, 2026-09-19)
Read: arXiv HTML full text via fetch tool (tool-extracted summary, not a line-by-line read). Tags: threats, core.

- **Problem.** Memory-poisoning defenses are scored on attack traffic only; their cost is paid on every benign turn.
- **Method.** Controlled harness: fixed vector store (text-embedding-3-small), backbone Gemini-3.1-flash-lite, Claude-Haiku judge (kappa 0.909). Only the defense changes. 6 conditions x 5 LoCoMo conversations (150 turns) x 3 replicates; 255 core questions.
- **Defenses.** Write-time: lexical input sanitization, provenance-based trust weighting, LLM anomaly detection. Read-time: consistency reranker with quarantine. Plus all four stacked.
- **Results.** Accuracy deltas vs undefended: sanitize +1.8 [-1.7,+5.6], provenance +1.9 [-2.2,+6.0], anomaly +3.1 [-0.9,+7.1], rerank **-4.4 [-9.0,-0.05]** (McNemar p=0.064), stacked -3.1 [-7.4,+1.0]. False-quarantine rate on benign traffic: rerank **33.6%**, stacked 30.3%, write-time 0%. Token overhead: anomaly 1.2%, rerank 2.7%, stacked 4.1% (roughly additive).
- **Stated limitations.** Resolution about +/-4.5 pp; one backbone; judge calibrated on its own runs; act-time defenses not measured; no attacks, so it cannot trade off prevented attacks against false positives.
- **Critique.** It is the only paper found that isolates benign-traffic cost, which is the question a bank's model-risk function would ask first. But n=5 conversations is tiny, and "no detectable cost" at +/-4.5 pp is far too coarse for regulated use. Latency is not reported. It needs pairing with an attack-side evaluation on the same harness (e.g. MemGauge, arXiv:2608.30177).
