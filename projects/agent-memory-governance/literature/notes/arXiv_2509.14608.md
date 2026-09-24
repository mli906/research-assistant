# arXiv:2509.14608 — Enterprise AI Must Enforce Participant-Aware Access Control (Bhatt et al., Microsoft, 2025-09-18)
Tags: mechanisms, core. Read: full text via arXiv HTML (WebFetch-assisted), 2026-09-24.

- **Problem:** Fine-tuned models and RAG leak data to unauthorised users. Prompt sanitisation, output filtering and isolation (e.g., CaMeL) are probabilistic and beaten by steganographic exfiltration.
- **Method:** Position plus framework. Anything used in training, retrieval or generation must be authorised for **all participants** in the interaction (e.g., drafting a reply from Alice to Bob may only retrieve content both can read). For fine-tuning, this is posed as maximal-biclique selection on the document–user ACL bipartite graph (heuristic, about O(|D|² log|E|)).
- **Results:** Attacks shown as case studies (cross-prompt injection via email). **No quantitative evaluation** of utility or overhead. The authors state the approach ships in Microsoft Copilot Tuning.
- **Stated limitations:** dynamic ACLs, ACL misconfiguration, weighting, multi-model settings. With fine-grained ACLs, possibly no user may be allowed to use the resulting model.
- **Critique:** The "all participants" rule is the right primitive for *shared* agent memory in finance (e.g., a relationship manager's assistant drafting to a client must not recall other clients' data). It extends naturally from RAG to memory writes: a memory derived in a session inherits the intersection of participants' rights. The paper does not treat memory explicitly.
