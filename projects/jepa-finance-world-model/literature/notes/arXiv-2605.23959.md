# When Alpha Disappears: one-switch benchmark for decision-time leakage in financial backtests (arXiv:2605.23959)
May 2026. Read: arXiv HTML via summarising fetch tool (2026-10-01).
- **Idea:** hold data panel, walk-forward splits, model, portfolio rule, horizon and costs fixed; flip one protocol rule at a time; report paired "Leakage Gain" (LG) in Sharpe.
- **Violations tested:** centered rolling features (TEMP_CENTER), full-sample normalisation, symmetric correlation graph from future returns, same-day close execution, using the full day-t bar while assuming open fills (EXEC_OPEN).
- **Data:** S&P 500 (439 tickers, 2010-2024) and CSI 300 (186 tickers); yearly walk-forward 2016-2024; momentum, ridge, LightGBM, graph-MLP, LSTM, Transformer; top-decile long-only; 0/5/10 bps.
- **Results:** TEMP_CENTER LG-SR@5bps ~4.7-25.2; EXEC_OPEN ~4.3-29.8; the other three violations ~<0.1 on average; effects positive in 8-9 of 9 test years.
- **Limits (authors):** no point-in-time universe, no capacity/impact, no intraday execution, no interacting leaks. A diagnostic, not evidence of alpha.
- **Use for us:** a ready unit-test suite for our data pipeline (inject each leak into a synthetic panel and verify the harness detects it). Also warns that centred windows (common in masked/JEPA-style context-target sampling!) are a major leak when target windows overlap context in time. Confidence: medium.
