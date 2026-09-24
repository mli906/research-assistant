# MINJA: memory injection attacks via query-only interaction (arXiv:2503.03704, 2025-03)
Read: arXiv HTML full text via fetch tool. Tags: threats, core. Foundation.

- **Threat.** The attacker is an ordinary user who only sends queries; memory is shared across users. Bridging steps, an indication prompt and progressive shortening plant records that are retrieved for *other* users' queries.
- **Setup.** EHRAgent (MIMIC-III, eICU), RAP (Webshop), QA agent (MMLU); GPT-4/4o.
- **Results.** Injection success rate about 98.2%, ASR about 76.8%, utility drop under 2% (about 10% on MMLU). Prompt-level detection generalizes poorly (general prompts reach up to 68% false positives).
- **Critique.** This is the canonical cross-user threat. A realistic replication (arXiv:2601.05504) finds much lower effectiveness when a memory already holds legitimate records. Shared memory across clients is the enabling design decision, which gives a clear governance lever.
