# Trojan Hippo: weaponizing agent memory for data exfiltration (arXiv:2605.01970, 2026-05)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Threat.** A single untrusted tool result (e.g. an email) plants a dormant payload that fires only when the user later discusses finance, health, legal, tax or identity topics, and then exfiltrates data.
- **Memory backends.** Sliding window, RAG, explicit list (ChatGPT-style), Mem0. Models include Gemini 3.1 Pro and GPT-5-mini.
- **Results.** Up to 85-100% ASR undefended. Persists for **100+ benign sessions**. Defense trade-offs: user-prompt-only indexing 0-5% ASR (breaks recall of agent plans); no-untrusted-write 0-5% (no memory updates during inbox sessions); length limit to 80 characters 20-30%; IFC policy 0% (kills email-send workflows after inbox access).
- **Finance.** It includes a banking-details trigger scenario, but there is no sector-specific analysis.
- **Critique.** It gives unusually explicit utility costs for each defense, which fits a cost table well. Dormancy over 100+ sessions has implications for retention and audit windows.
