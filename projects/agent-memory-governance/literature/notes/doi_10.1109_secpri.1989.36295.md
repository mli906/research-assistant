# The Chinese Wall security policy, Brewer & Nash (IEEE S&P 1989; record year 2003 is the Xplore date)
Read: abstract only. Facet: regulation (information barriers).
- Formal access-control model in which a subject's permitted accesses depend on its *history* of accesses (conflict-of-interest classes). Motivated by financial-services Chinese walls.
- Relevance: the natural formal baseline for barrier-aware shared agent memory. An agent, or a memory shard, that has "read" client A's MNPI should be blocked from recalling into a conflicting client B context. Note the difference from Bell-LaPadula: history-dependent, not static labels.
- Gap: I found no agent-memory paper that implements or evaluates Brewer-Nash-style history-dependent recall control (observation; see regulation.md gaps).
