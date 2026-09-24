# Benchmarking LLM agents for wealth-management workflows (arXiv:2512.02230)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core.

- **Design.** Extends TheAgentCompany: 12 task pairs (high- vs low-autonomy prompts) at 3 difficulty tiers (retrieval, computation such as FIFO capital gains, synthesis and communication). Dockerised EspoCRM, OwnCloud, Rocket.Chat (Sotopia NPCs), Plane and OpenHands. Five synthetic client profiles. Checkpoint-based deterministic grading.
- **Results (GPT-4o only).** High autonomy: 2/12 resolved, 49.0% of checkpoints. Low autonomy: 4/12 resolved, 69.4%. About $0.12 per task.
- **License.** CC BY 4.0 (paper). The benchmark repo is not stated in the extraction.
- **Critique.** This is a realistic *advisor-assistant* environment with a CRM as the system of record, and useful infrastructure for memory-governance experiments (CRM = authoritative memory; agent memory = shadow copy). The scale is tiny (5 clients) and there is no cross-session memory or confidentiality test.
