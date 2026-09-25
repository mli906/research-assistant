# OBLIVION: operational skill unlearning (arXiv:2608.08264)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). This upgrades the earlier abstract-only reading in gaps.md N4. Tags: evaluation, threats, gaps-check, skills, core.

- **Problem.** After a skill is removed from the registry, an agent can **rebuild it** from residual carriers ("transcripts, cached files, vector memory entries, local schemas, and registry drafts") through source-to-sink tool workflows. The paper calls this revoked-skill resurrection.
- **Method.**
  - Cross-Surface Coherent Erasure: a transaction across 6 surfaces (behaviour gate, registry, vector memory, filesystem, transcript, MCP schema) with tombstones and audit logging.
  - Anti-ReDerivation Guard: taint-labels material derived from revoked sources, propagates the label through transforms, and blocks dangerous sinks.
- **Data.** AgentForgetBench: 160 locked cases (88 attack, 8 near-miss, 64 utility).
- **Results.** With no defence, ASR = 1.0. With OBLIVION, ASR = 0.114, IWE = 0.115, utility pass = 1.0 and benign block rate = 0. In the skill-attack sandbox, ASR = 0.2.
- **Scope.** The motivation is **capability revocation, not personal-data erasure**. The paper has no GDPR framing (checked).
- **Limitations (stated).** 10 of the 88 attacks still succeed.
- **Critique.** Its taint propagation is the right primitive for the reverse direction the PI needs. OBLIVION goes from skill to carriers; the PI needs client trace → derived skill, so erasure of a client's data reaches every skill it shaped. Neither the benchmark nor the method covers trace-to-skill lineage under a data-subject request.
