# Banking Done Right: Ryt AI, an LLM-native agentic retail bank interface (arXiv:2510.07645)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core.

- **Deployment.** Ryt Bank, a licensed Malaysian digital bank (Bank Negara Malaysia). The authors call it the first regulator-approved deployment with conversational AI as the *primary* banking interface. It serves more than 50K users and about 80K transactions per month (per paper, Oct 2025). The model (ILMU) is in-house and closed-source, with LoRA adapters per agent, hosted in the bank.
- **Architecture.** Four agents: Guardrails, Intent, Payment (field extraction plus OCR), FAQ (RAG).
- **Memory.** Explicitly a **"stateless, session-bound memory design"**. At session end, prompts, inferences, extracted fields and decisions are discarded (data minimisation). Human-in-the-loop Approve/Decline/Edit on every transfer; 2FA above RM250.
- **Evaluation.** 2,000 conversational cases. Hallucination <1.5% on FAQ and <0.5% on transactional flows.
- **Limitations.** Regulator-driven in-house model; language and regional specificity; update cadence.
- **Critique.** This is real deployment evidence that a regulated bank chose **no persistent agent memory**, the design-space endpoint opposite to personalised memory. It leaves open how audit is kept without state; the "stateless audit architecture" is not detailed in the extraction. It pairs with arXiv:2604.20158.
