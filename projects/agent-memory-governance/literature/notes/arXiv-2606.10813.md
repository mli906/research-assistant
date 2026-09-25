# RedAct: redacting agent traces to protect procedural skills (arXiv:2606.10813)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core.

- **Threat.** Released execution traces let downstream parties recover proprietary procedures ("formulas, thresholds, tool choices, workflow dependencies, and validation routines").
- **Benchmark.** CapTraceBench: 75 long-horizon tasks, 154 skills, 7 domains including finance. Metrics: normalised skill transfer (NST) and recovered protected information (RPI).
- **Method.** An LLM locator abstracts protected items while preserving audit evidence (final outputs, tool-use evidence, order). Four behavioural watermark families support provenance.
- **Results.** Raw traces give NST 44.7–67.1%. RedAct drives NST below the no-skill baseline. Watermarks detect 93.6–100% with ≤1.9% false alarms. 91.0–96.6% of audit evidence is retained.
- **Limitations (stated).** Controlled tasks with automatic verifiers; contextual watermarks are fragile.
- **Critique.** The protected asset is the firm's IP, not client personal data. The technique still transfers: "redact while preserving verifier-critical evidence" is the audit-vs-minimisation trade-off (GP6) in trace form. Watermarking is a candidate provenance primitive linking a skill to its sources.
