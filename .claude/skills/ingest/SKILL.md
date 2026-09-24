---
name: ingest
description: Catalog the PI's own materials (SciSpace/AI-generated reviews, method surveys, notes, papers, slides, exploratory code) in a project's inputs/ folder so every agent can use them as context.
argument-hint: [project-slug]
---
Arguments: $ARGUMENTS (default: most recently modified project).

For each file in `projects/<slug>/inputs/` not yet listed in `inputs/INDEX.md`:
1. Read it. PDFs: use the Read tool (pages) or `pdftotext`. DOCX/PPTX: the docx/pptx skills or
   `pandoc`. Code: README plus the entry points. Notebooks: cells and outputs.
2. Classify it: `ai-generated-review` (e.g. SciSpace, Deep Research), `pi-survey`, `pi-notes`,
   `paper`, `slides`, `prototype-code`, `data`, `other`. Record provenance (who or what made it, date)
   and sensitivity. Ask the PI once if a file might be confidential. Confidential files are never
   sent to web searches or published.
3. Extract into `inputs/INDEX.md` (one section per file): a 3–5 line summary; key claims (each
   marked "cited: <ref>" or "uncited"); methods/systems surveyed; ideas or hypotheses the PI holds;
   for code: what it does, how to run it, and its state.
4. References it cites: resolve to DOIs/arXiv ids and add them with
   `python3 tools/lit.py fetch <ids> --source pi-input | python3 tools/lit.py add projects/<slug> --tag pi-input`.
   Don't retype metadata. For AI-generated reviews, spot-check 3 of their claims against the
   primary papers and note the result (they are context, not evidence).
5. Update `STATE.md` (decisions/open questions if the materials change the scope), and tell the PI
   what you learned about their prior thinking in 5 bullets, including where it already disagrees
   with the literature review.
