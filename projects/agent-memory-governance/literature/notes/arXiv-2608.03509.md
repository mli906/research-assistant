# SkillJack: persistent skill backdoors in self-evolving agents (arXiv:2608.03509)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core.

- **Threat model.** Poisoned experience records enter the corpus via indirect injection, a shared experience pool, or a compromised trajectory dataset. The attacker cannot edit the skill library or the extraction code.
- **Systems.** SkillX (trajectory to plan-skills) and Anything2Skill.
- **Properties.** (1) *Sanitisation whitewashing*: extraction lowers detectability. (2) *Cross-layer promotion*: transient experience becomes a stored, routed skill. (3) *Persistence isolation*: Pr[derived skill ∈ S | source ∉ E] > 0.
- **Results.**
  - Detection falls from 98.5% on poisoned trajectories to 11.4% on the extracted skills.
  - Trigger rates: SkillX 56.2%, A2S 89.2%; 20% collateral triggering on clean tasks.
  - **80.0% of skill-mediated attacks persist after deleting the original poisoned records.**
- **Defences.** Extraction-time LLM review lowers triggering to 6.7%. Runtime regex monitoring reaches 0% (n=15). Combining the two does worse (13.3%).
- **Limitations (stated).** Single model; proxy triggering detectors; small defence samples.
- **Critique.** This is **direct evidence that deleting a source does not propagate to derived skills**. That is the security twin of the PI's erasure-propagation problem: replace "poisoned record" with "client's erased data". The "whitewashing" finding also implies that PII *abstracted* into a procedure may evade detectors that work on raw traces.
