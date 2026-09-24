---
name: radar
description: Scan for new papers and industry developments since the last check and write a digest; can be scheduled.
argument-hint: [project-slug | "all"] [since YYYY-MM-DD]
---
Arguments: $ARGUMENTS (default since: `last_radar` in `STATE.md`, else 14 days ago).

For each project:
1. Re-run the key queries from `literature/review.md` (the query plan) with
   `python3 tools/lit.py arxiv ... --since <date>`, SciSpace, and WebSearch for industry news.
2. Add new records to `papers.jsonl`. For each genuinely relevant new item, say
   *why it matters to this project*: does it scoop an idea in `ideas.md`, provide a new
   baseline, contradict an assumption, or open a new gap?
3. Write `literature/radar-<date>.md`. Put **scoop alerts** first (anything that overlaps
   with the chosen idea).
4. Update `last_radar` in `STATE.md`. Keep the digest short: signal only.

To run this automatically, the PI can set it up with `/schedule` (e.g. weekly on Monday mornings).
