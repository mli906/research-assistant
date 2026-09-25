# ASG-SI: audited skill-graph self-improvement (arXiv:2512.23760)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). This upgrades the earlier abstract-only reading in gaps.md N4. Tags: gaps-check, skills, core. DistributedApps.ai/OWASP and Kleiner Perkins.

- **Mechanism.** Candidate improvements are extracted from successful trajectories, normalised into skills with explicit interfaces, and "promoted only after passing verifier-backed replay and contract checks." Each promotion is tied to an evidence bundle (tool schemas and arguments, output hashes, contract checks, deterministic tests, verifier identity and version). Audit traces are written as append-only JSON.
- **Threat model.** The attacker influences task inputs and distribution to induce reward hacking. Goals: auditability, integrity, controlled generalisation, measurement reliability.
- **Evaluation.** **None**: a reference implementation only; the metrics are proposed, not run.
- **Privacy / multi-user / deletion.** Not addressed. The one relevant sentence: "Evidence bundles may contain sensitive data in realistic deployments, requiring access control, retention policies."
- **Critique.** This is the clearest articulation of a **model-risk-style promotion record** (evidence bundle, verifier versioning, append-only audit). It is a design position, not evidence. Note the tension it raises but does not resolve: the evidence bundle that makes promotion auditable is itself a copy of client data, which is the retention-vs-erasure problem again (GP1).
