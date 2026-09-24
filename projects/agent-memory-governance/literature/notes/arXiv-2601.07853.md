# FinVault: Benchmarking financial agent safety in execution-grounded environments (arXiv:2601.07853)
Read: abstract only (SciSpace/arXiv record; the arXiv HTML/PDF fetch returned 404 on 2026-09-24). Tags: evaluation, core, finance.

- **Design (per abstract).** 31 regulatory-case-driven sandbox scenarios with state-writable databases and explicit compliance constraints; 107 real-world vulnerabilities; 963 test cases covering prompt injection, jailbreaking, finance-adapted attacks, and benign inputs to measure false positives.
- **Results (per abstract).** Existing defenses are ineffective: average ASR up to 50.0% on SOTA models, and 6.7% even for the most robust system.
- **Critique.** It is execution-grounded (state changes, not text) and includes benign cases, both good practice. From the abstract, there is no persistent memory, cross-session or cross-client dimension. Code: github.com/aifinlab/FinVault. The full text should be read before relying on the metric definitions.
