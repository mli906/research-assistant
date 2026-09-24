# MemGauge: stage-wise utility-risk trade-offs in LLM agent memory (arXiv:2608.30177, 2026-08-31)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Problem.** Utility and poisoning risk are usually measured separately and at fixed configurations.
- **Method.** Varies one stage at a time under matched clean/poisoned conditions: write admission coverage theta_w, management policy (4 policies), retrieval exposure theta_r. 11 LLMs (incl. GPT-5.4, Gemini, DeepSeek); LongMemEval and LoCoMo; attacks MINJA and Sleeper (interaction-based).
- **Results.** Write stage: ASR stays near 0 below theta_w of about 0.3, then jumps to 37-64% at full coverage (a threshold). Management: ASR varies by up to 62 pp across policies while clean utility moves only 3-5 pp, so this is the cheapest control point. Retrieval: utility and ASR rise together (utility 43-70%, ASR 34-64%). Real systems (Mem0, Hindsight, LangMem, A-MEM): write retention 36.5% (Mem0) to 74.5% (LangMem); native management lowers ASR by 10.6-24.8 pp; raising top-K from 1 to 7 lifts utility about 25-29% to 53-64% and ASR about 5-12% to 36-54%.
- **Limitations (stated).** Small memory banks (50-500 records); two attack families; interaction-based poisoning only.
- **Critique.** It is the best design-space map available. Its central governance point is that management (consolidation/dedup) is where risk can be cut without losing utility. It has no privacy or leakage axis and no cost/latency axis.
