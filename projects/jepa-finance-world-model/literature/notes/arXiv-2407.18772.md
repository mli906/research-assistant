# Learning Production Functions for Supply Chains with Graph Neural Networks (Chang et al., Stanford/Leskovec) - arXiv:2407.18772 (AAAI 2025)

Read: full text via arXiv HTML through WebFetch (summariser-extracted). Accessed 2026-10-01.

**Problem.** Transaction graph is observed; firms' internal production functions (which inputs make which outputs) and inventories are hidden. Infer them and forecast future transactions.
**Method.** Temporal GNNs (SC-TGN, SC-GraphMixer) extended to supplier-buyer-product hyperedges, plus an inventory module learning attention weights alpha(p1,p2) = units of input p1 per unit of output p2, with an inventory-debt loss. Also SupplySim, an open simulator (tiered products, preferential attachment, ARIO economic dynamics, shocks and missing data).
**Data.** TradeSparq customs/trade records (supplier, buyer, HS product, time, USD): Tesla ecosystem 2019-2022 (proprietary, not releasable) and an Industrial Equipment Dataset 2023 with estimated ground-truth parts lists.
**Results.** Production-function MAP 0.262 on real IED data, +6-50% over best baseline; edge-existence MRR 0.820 on Tesla (+11-62%); 7-step forecasts AUROC 0.936; synthetic with shocks hardest, inventory module +3-5 MRR points there; 20% firm dropout costs only 3.5% MAP.
**Limitations (stated).** Proprietary real data; domestic transactions missing; single production function per product; inventory constraints unreliable under systematic missingness; two real datasets only.
**Critique / relevance.** Best-in-class example of "hidden state + partial observability + network" and uses a simulator with known mechanisms (like FinStressTS, arXiv:2606.03184). It is a generative/discriminative link model, not JEPA, and ground truth exists only on one dataset. For us: supply-chain use case needs transaction-level or customs data; Compustat/Revere give only sparse, large-firm links.
