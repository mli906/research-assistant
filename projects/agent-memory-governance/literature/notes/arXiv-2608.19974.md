# ReguSim: Evaluating LLM agent rule grounding in financial compliance (arXiv:2608.19974)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core, finance.

- **Problem.** Trading agents cite rules yet submit violating orders. The paper separates stated reasoning, attempted action, execution enforcement and monitor evidence.
- **Design.** Market-inspired regimes (US, China A-share, Hong Kong) plus LAX/STRICT synthetic controls. Executable rules: price bands, short-sale availability, same-session resale limits, gross exposure caps. 5 manipulation types: wash trading, spoofing, pump-and-dump, churning, marking the close. ReguBench: 191 scenarios, 49,440 synthetic records.
- **Metrics.** Trader: rejected-attempt %, rule-breach %, activity, compliance-awareness. Monitor: macro F1/precision/recall. Bridge: false-accept rate, issue-type accuracy, evidence-hit rate.
- **Results.** Visible rules do not stop violations: 24.2% (DeepSeek) and 14.8% (Gemini) rejected submissions. Incentive framing shifts behavior by 30.9 pp. The LLM monitor (GPT-5.4 Mini, F1 63.8%) is worse than a logistic baseline (71.4%). Showing the trader's rationale raises monitor false-accepts from 25% to 46.9%.
- **Limitations (stated).** Stylized rules, synthetic records, few models, no legal validation.
- **Critique.** Its separation of stated vs enacted compliance is a key methodological point for audits: a rationale is not evidence. No memory component.
