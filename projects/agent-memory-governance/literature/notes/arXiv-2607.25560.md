# SigLeak: inferring proprietary skills from execution trajectories (arXiv:2607.25560)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core.

- **Definition.** Skill Leakage is "the unauthorized inference of proprietary skill content from execution trajectories observed through black-box interactions", using benign queries only.
- **Method.** A generator creates diagnostic probes; a synthesizer contrasts skill-enabled and skill-disabled trajectories to extract recurring "skill signatures", refined over 2 rounds.
- **Results.** +6.88 pp downstream success over the skill-disabled reference on average (+1.62 on ALFWorld to +13.09 on Spreadsheet). Fine-grained F1 22.8%. A prompt defence (SkillGuard) stops direct black-box stealing but **not** SigLeak.
- **Limitations (stated).** Fixed prompts and budgets; local environments only.
- **Critique.** Implication for the PI: if a promoted skill embeds client-specific content, **other clients' sessions can surface it behaviourally even when the skill text is hidden**. Leakage must therefore be measured at the behaviour level, not only by scanning the skill text.
