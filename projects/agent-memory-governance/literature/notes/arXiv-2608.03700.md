# AntiSkillBench: privacy leakage in persona skills (arXiv:2608.03700)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: threats, skills, core.

- **Setting.** Persona skills distil **one person's** interaction histories into portable skill artifacts. The study is single-user, not cross-user promotion.
- **Data.** 7,500 persona-grounded dialogue traces from 50 profiles: demographics, background, Big Five personality, communication style. Three-round dialogues in general-assistance, math and tool-design scenarios.
- **Metrics.**
  - Skill Coverage: private or identity-revealing information encoded in the skill artifact.
  - Field QA Accuracy: attribute disclosure when the agent is queried.
  - VocabGain: impersonation.
- **Results (GPT 5.4).** Skill Coverage 55.2–66.2%; communication coverage 88–92%; Field QA 54.2–56.0%. VocabGain up to 40% (Gemini 3.6). These hold across three distillation protocols.
- **Defences.** Privacy sanitisation cuts communication VocabGain from 87.3 to 6.5 (Direct Distill) but "leaves personality information exposed". Adversarial obfuscation gives smaller reductions. Backdoor watermarking ranges from 98% to 30–40% depending on the distillation method. Overall, defences show "limited and distillation-dependent effectiveness".
- **Critique.** This is the **best available measurement that distillation into skills does *not* strip personal data**. It is directly relevant to the PI's promotion step. It has no cross-user setting, no finance attributes, no k-threshold or DP, and no erasure.
