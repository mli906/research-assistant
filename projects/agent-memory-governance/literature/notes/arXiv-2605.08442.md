# Injection-Execution Dissociation in persistent memory attacks (arXiv:2605.08442, 2026-05-08)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Design.** 5,040-run factorial experiment: 9 open models x 6 defenses plus baseline, N=40 per cell. Sessions: inject (S1), two benign sessions, trigger (S4). Temperature 0. A loaded-corpus frontier study adds 21 models.
- **Result.** Malicious instructions are **stored at over 97.5%**, but execution ranges **0-95%** and is uncorrelated with storage. Input filters and RAG sanitizer/judge fail. Prompt hardening leaves 77.8% success. A memory "sandbox" (no recall) gives 0% for 8 models but *inverts* on qwq:32b (0% goes to 100%). Vendor patterns: Anthropic blocks at injection (storage at most 17.5%, 0% ASR); OpenAI stores nearly everything and blocks at execution; Gemini 3.1 Pro Preview reaches 95% ASR.
- **Limitations.** Simulated tools; results tied to model snapshots.
- **Critique.** This is strong evidence that write-time filtering alone is not a control. Governance should put authority boundaries between memory and action (cf. arXiv:2606.24322). The vendor comparisons will age quickly.
