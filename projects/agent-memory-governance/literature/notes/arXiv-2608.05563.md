# PoisonedEvolution: trajectory poisoning in self-evolving skill systems (arXiv:2608.05563)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core.

- **Threat model.** A skill-visible black-box attacker contributes a bounded share of trajectories (main setting 3 of 30, i.e. 10%). The attacker cannot see private pools or evolver prompts and cannot edit the bank.
- **Targets.** SkillClaw (multi-user sessions, accepted skills synced to all users) and Trace2Skill.
- **Results.**
  - Skill embedding rate is 546/600 = **91.0%** on SkillClaw across 6 evolvers (range 70–100%) and 369/600 = 61.5% on Trace2Skill.
  - **Recurrence matters**: k=1 poisoned record gives 5/25, k=2 gives 21/25, k=3 gives 25/25 at n=30. At n=100, k=3 still gives 22/25.
  - Causal framing reaches 25/25, versus 8–11/25 for fragmented insertion.
- **Defence (pilot).** A **provenance-diversity gate** "requiring three users and clusters, rejects majority dominance, and penalizes high text overlap" cut post-gate embedding from 25/25 to 0/25. It is "preliminary: candidate grouping is assumed ... coordinated Sybils may mimic diversity."
- **Limitations (stated).** One evolution cycle only; inert canary payloads; no full utility–security Pareto frontier.
- **Critique.** This is the first published instance of a **"≥k distinct users" promotion threshold**, motivated by integrity, not privacy. The PI's idea of promoting only if a pattern is seen across ≥k clients has the same shape, but it serves the opposite purpose: k-anonymity versus Sybil resistance. The two objectives can be analysed jointly, since a single threshold could serve both. The paper also shows that recurrence (what skill induction rewards) is exactly what attackers fake.
