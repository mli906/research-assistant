# AgentLeak: internal-channel privacy leakage in multi-agent LLM systems (arXiv:2602.11510)
Read: full text (arXiv HTML v3), accessed 2026-09-24. Tags: evaluation, core.

- **Problem.** Audits look at final outputs only; sensitive data also flows through inter-agent messages and shared memory.
- **Design.** 7 instrumented channels (C1 output, C2 inter-agent, C3 tool in, C4 tool out, C5 shared memory, C6 logs, C7 artifacts). 1,000 scenarios in 4 domains (healthcare, **finance**, legal, corporate; 250 each), 400 single-agent and 600 coordinator–worker. Attack levels A0–A2. 4,979 validated traces. Data is synthetic (Faker) plus curated HF data; expert annotation κ=0.75–0.82.
- **Metrics.** Exact Leakage Rate (any sensitive field leaked per scenario), Channel Leakage Rate, ASR (adversarial levels), Task Success Rate. A 3-tier detector: canaries, then structured-field regex, then an LLM judge (Qwen-2.5-7B; FPR 4.8%, FNR 7.4%).
- **Results.** Total exposure is 68.9% for multi-agent vs 43.2% for single-agent. Channel leakage: C1 27.2%, C2 68.8%, C5 (memory) 46.7%. 41.7% of traces look safe at the output but leak internally. Output sanitizers catch 98% on C1 and 0% on C2/C5.
- **Limitations (stated).** English only; coordinator–worker topology only; 4 frameworks; judge threshold calibrated in English.
- **Critique.** Shows that output-only privacy metrics are invalid for memory-bearing agents. Memory is treated as a leak channel, not as a governed store (no retention/erasure semantics). Venue: IEEE Access 2026 per the paper. License CC BY 4.0.
