# MedMemoryBench: benchmarking agent memory in personalized healthcare (arXiv:2605.11814)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps (transfer source), core.

- **Data.** 20 synthetic patient archetypes derived from de-identified real cases, about 100 sessions each (about 2,000 sessions, 16k turns, 20.7M tokens). Temporal event graphs of disease progression. **"Trap events"** (allergies, contraindications, economic constraints) require zero-fault retention. Six query types, including a State Update Accuracy query. "Mixed mode" injects noise (general health chat, **proxy family-member questions**). Streaming evaluation with a checkpoint every 10 sessions.
- **Systems.** 12 memory systems (BM25, embedding RAG, GraphRAG, HippoRAG-v2, Mem0, A-Mem, MemOS, LightMem, Letta, MIRIX, ...).
- **Results.** Best is Letta at 51.2% (efficient mode) vs 41.6% (mixed); noise costs 15–30%. Retrieval failure is the main bottleneck.
- **Release.** CC BY 4.0, github.com/AQ-MedAI/MedMemoryBench. No forgetting or deletion evaluation.
- **Critique.** Healthcare is ahead of finance on memory benchmarks (compare FinPerMA). Three ideas transfer directly: "trap events" (for finance: sanctions hits, vulnerability flags, stated exclusions/ESG constraints, power-of-attorney), proxy-speaker noise (which in finance becomes a *third-party / authorised-user* confidentiality test), and streaming checkpoints. Privacy and erasure are absent, as they are in the finance benchmarks.
