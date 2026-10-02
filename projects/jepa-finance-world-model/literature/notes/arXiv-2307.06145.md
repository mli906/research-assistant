# Robust Impulse Responses using External Instruments: the Role of Information (Brignone, Franconi, Mazzali) - arXiv:2307.06145

Read: full text via arXiv HTML through WebFetch (summariser-extracted). Accessed 2026-10-01.

**Problem.** External-instrument (proxy) SVARs give biased impulse responses when the shock is non-invertible given the VAR's small information set, or when instruments/measurement are noisy.
**Method.** Proxy DFM: apply external-instrument identification inside a dynamic factor model (hundreds of series -> few latent factors), so the information set is large.
**Data/design.** Simulations from an RBC model with fiscal foresight (T=200, N=102, 1,000 reps); FRED-MD (1963-2018, N=100); five monetary instruments (Gertler-Karadi, Romer-Romer, Miranda-Agrippino-Ricco, Jarocinski-Karadi, Bauer-Swanson).
**Results.** Proxy VAR cannot recover the non-fundamental shock even without noise; DFM does, at all noise levels. Empirically Proxy VAR shows price and output puzzles for most instruments, Proxy DFM none: tightening lowers IP (peak about -2%), raises unemployment (about 0.5pp), equity -10%+; policy shocks explain ~30% of real-variable variance by year 2 and >50% of equity/credit/FX variance on impact.
**Assumptions/limits.** Invertibility (tested with Forni et al. 2022), weak cross-correlation of idiosyncratic components, instrument relevance and exogeneity.
**Relevance.** Closest econometric analogue to "latent state + identified action": a latent-factor state is what makes the shock identifiable. Any action-conditioned JEPA claiming policy counterfactuals must meet the same invertibility and instrument-validity bar; this paper shows the bar is information-set size, which a rich latent state helps with. Single paper, simulation + one application: confidence medium.
