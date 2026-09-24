# Isolated but Exposed: persistence-based memory extraction via tools (SPORE) (arXiv:2607.23444, 2026-07-26)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Threat.** A malicious third-party tool (e.g. from an API marketplace). Per-user memory isolation holds, but agents put memory-retrieved data into tool arguments.
- **Method.** 3 stages: plant a persistent command in short-term memory; iterate semantic anchors to cover the embedding space; plant a dormant reactivation payload.
- **Results.** Record extraction rate 80.0% vs MEXTRA 3.0%, RAG-Thief 30.0%, IKEA 12.5%. Also works on Dify and Coze with Mem0, at lower rates. Response filtering cuts it to 54.0%; prompt hardening to 32.5%.
- **Recommendation.** Scope memory access per *tool*, not only per user.
- **Limitations.** 200-record memories; system-level defenses untested.
- **Critique.** For banks this is a vendor/third-party risk issue (DORA ICT third-party, outsourcing). Per-user isolation is necessary but not sufficient.
