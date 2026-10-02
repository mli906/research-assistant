# arXiv:2607.05238 Branch-JEPA: finite-support predictive distributions for JEPA world models
Read: HTML full text via WebFetch extraction (2026-10-01).
- **Method:** encode context once; router gives K weighted latent successors ("atoms", never averaged); each decoded by a shared decoder. Two training regimes: specialisation (hard assignment, update closest branch) and full-set (Energy Score = observation term + pairwise dispersion).
- **Results:** matched K=6 on AV2 validation, 5 seeds: full-set trajectory Energy Score 2.0766 vs 2.2201 (specialisation), -6.46%; latent branching beats output-only branching (2.0766 vs 2.1142), 95% CIs exclude zero; OGBench AntMaze: transition precision 49-56% vs 14-21%. Baselines: K=1 JEPA, MDN, soft-WTA, Sinkhorn.
- **Authors' limits:** targets the predictive-distribution interface not forecasting SOTA; no closed-loop control.
- **Relevance:** the cleanest published recipe for sampling multiple plausible futures from JEPA latents *and* a proper scoring rule (Energy Score) that can be used for scenario evaluation. Finite K is coarse for continuous financial paths (speculation). Driving/navigation domain only.
