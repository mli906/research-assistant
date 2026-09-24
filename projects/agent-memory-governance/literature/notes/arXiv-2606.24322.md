# Non-malleable, origin-bound authority against memory poisoning (TMA-NM) (arXiv:2606.24322, 2026-06-23)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Insight.** Content- and lineage-based trust are *malleable*. Three laundering channels: the agent's own summarization, a trusted-tool echo, and manufactured corroboration.
- **Mechanism.** Authority to act is bound at write time to the origin channel. Anything derived from untrusted input inherits untrust. Elevation needs 2 or more independent trusted principals or a fresh user authorization. A hash-chained verdict log records decisions.
- **Formal.** TLA+/TLC model checking. Content and lineage defenses have reachable violations; TMA-NM is safe on all 3,270 states of a bounded model. The unbounded proof is future work.
- **Results.** 8 models. Undefended ASR 84% direct / 68% laundered. Content detection 0% / 68%. Lineage 0% / 47%. **TMA-NM 0% / 0%** with 100% legitimate-action authorization. Blocks MemMorph, MemoryGraft, Trojan Hippo and a conversational trojan. Gate latency 1.3 microseconds vs about 2 s for detector calls.
- **Limitations.** Free-text answer bias is not covered; trust moves to origin labelling; user confirmations are needed when corroborators are scarce.
- **Critique.** It is the most "governance-shaped" defense found: it amounts to maker-checker / four-eyes for agent memory. The user-confirmation burden in a realistic advisory workflow is not measured.
