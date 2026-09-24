# MEXTRA: privacy risks in LLM agent memory (arXiv:2502.13172, 2025-02)
Read: arXiv HTML full text via fetch tool. Tags: threats, core. Foundation.

- **Threat.** Black-box extraction of stored user queries from memory used as demonstrations.
- **Setup.** EHRAgent (edit-distance retrieval, k=4) and RAP (cosine, k=3); GPT-4o; 200-record memory.
- **Results.** With 30 prompts: 50 unique queries extracted from EHRAgent, 26 from RAP. Leakage grows with memory size (50 to 500) and with retrieval depth k. Edit-distance retrieval leaks more than embeddings. Attacker knowledge of the implementation helps a lot.
- **Limitations.** Single-agent; session isolation not studied.
- **Critique.** Foundational. It has since been superseded in strength (SPORE 80% vs MEXTRA 3% in a tool setting). It shows that design knobs (k, memory size) are privacy knobs.
