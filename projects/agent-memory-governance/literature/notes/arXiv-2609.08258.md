# Revoked but Still Authoritative: revocation enforcement in agent-memory systems (arXiv:2609.08258, 2026-09-08)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Setup.** Five systems (Graphiti, Zep, mem0, langmem, cognee) that use *soft revocation* (mark invalid, retain). 9 policy scenarios (including "compliance log deletion"), 9 models from 6 vendors, 6 defense conditions.
- **Results.** **No system enforces revocation at retrieval by default.** Where the revoked fact is returned (Graphiti; mem0 with flag override) it ranks first, and agents take the unsafe action in 44.2% / 42.1% of trials. Without a prompt rule the unsafe-action rate is 81.0%; with an explicit prohibition it is 12.9% (up to 46.1%). Prompt hardening alone gives 37.2%. Store-level filtering gives **0.0%** over 1,620 trials. The proposed read-time guard also withholds the older fact of a conflicting pair when the backend exposes no validity flags.
- **Limitations.** Single-read design. If agents journal their unsafe decision, that note becomes a new "current" fact the filter cannot catch.
- **Critique.** This connects directly to regulation: policy supersession, withdrawn advice and GDPR rectification all rely on revocation that is not enforced by default. It is a cheap, deterministic control with a large effect.
