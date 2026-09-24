#!/usr/bin/env python3
"""Literature toolkit for the research assistant (stdlib only).

Complements the SciSpace MCP (broad semantic search) with sources that are
fresher or more structured:

  lit.py arxiv   "query" [--since 2026-06-01] [--max 30] [--cat cs.LG]
  lit.py openalex "query" [--since 2026-01-01] [--max 30]
  lit.py s2      "query" [--max 30]            # Semantic Scholar
  lit.py cites   <doi|arXiv:id> [--max 30]      # who cites this paper (forward snowball)
  lit.py add     <project_dir> < records.jsonl  # merge records into literature/papers.jsonl
  lit.py bib     <doi|arXiv:id> [...]           # fetch real BibTeX (never hand-write it)
  lit.py verify  <paper_dir>                    # check every \\cite resolves to a real, fetched entry

Search commands print JSON lines: {id, title, authors, year, date, venue,
doi, arxiv, url, abstract, citations, source}. Pipe into `add` to store.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

UA = "research-assistant/0.1 (mailto:research-assistant@example.org)"


def get(url, accept=None, retries=4):
    headers = {"User-Agent": UA}
    if "semanticscholar" in url and os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]
    if accept:
        headers["Accept"] = accept
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < retries - 1:
                time.sleep(5 * (i + 1))
                continue
            raise
        except urllib.error.URLError:
            if i < retries - 1:
                time.sleep(2)
                continue
            raise


def emit(rec):
    print(json.dumps(rec, ensure_ascii=False))


def rec_id(doi=None, arxiv=None, fallback=None):
    if arxiv:
        return f"arXiv:{arxiv}"
    if doi:
        return f"doi:{doi.lower()}"
    return fallback


# ---------------------------------------------------------------- search ---

def cmd_arxiv(a):
    q = a.query
    terms = " AND ".join(f'all:"{t}"' if " " in t else f"all:{t}"
                         for t in re.findall(r'"[^"]+"|\S+', q))
    terms = terms.replace('""', '"')
    if a.cat:
        terms = f"({terms}) AND cat:{a.cat}"
    url = ("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": terms, "start": 0, "max_results": a.max,
        "sortBy": "submittedDate", "sortOrder": "descending"}))
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(get(url))
    for e in root.findall("a:entry", ns):
        date = e.findtext("a:published", "", ns)[:10]
        if a.since and date < a.since:
            continue
        aid = e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid)
        doi = e.findtext("x:doi", None, ns)
        emit({
            "id": rec_id(doi, aid), "title": " ".join(e.findtext("a:title", "", ns).split()),
            "authors": [n.findtext("a:name", "", ns) for n in e.findall("a:author", ns)],
            "year": int(date[:4]) if date else None, "date": date,
            "venue": e.findtext("x:journal_ref", "arXiv", ns), "doi": doi, "arxiv": aid,
            "url": f"https://arxiv.org/abs/{aid}",
            "abstract": " ".join(e.findtext("a:summary", "", ns).split()),
            "citations": None, "source": "arxiv"})


def _openalex_abstract(inv):
    if not inv:
        return ""
    pos = [(i, w) for w, idx in inv.items() for i in idx]
    return " ".join(w for _, w in sorted(pos))


def _openalex_rec(w):
    doi = (w.get("doi") or "").replace("https://doi.org/", "") or None
    arxiv = None
    for loc in w.get("locations") or []:
        m = re.search(r"arxiv\.org/(?:abs|pdf)/([\d.]+)", (loc.get("landing_page_url") or ""))
        if m:
            arxiv = m.group(1)
    src = ((w.get("primary_location") or {}).get("source") or {})
    return {
        "id": rec_id(doi, arxiv, w.get("id")), "title": w.get("title"),
        "authors": [x["author"]["display_name"] for x in w.get("authorships", [])],
        "year": w.get("publication_year"), "date": w.get("publication_date"),
        "venue": src.get("display_name"), "doi": doi, "arxiv": arxiv,
        "url": (w.get("primary_location") or {}).get("landing_page_url") or w.get("id"),
        "abstract": _openalex_abstract(w.get("abstract_inverted_index")),
        "citations": w.get("cited_by_count"), "source": "openalex"}


def cmd_openalex(a):
    params = {"search": a.query, "per-page": min(a.max, 200), "sort": "relevance_score:desc"}
    if a.since:
        params["filter"] = f"from_publication_date:{a.since}"
    data = json.loads(get("https://api.openalex.org/works?" + urllib.parse.urlencode(params)))
    for w in data.get("results", []):
        emit(_openalex_rec(w))


S2_FIELDS = "title,authors,year,publicationDate,venue,externalIds,url,abstract,citationCount"


def _s2_rec(p):
    ext = p.get("externalIds") or {}
    doi, arxiv = ext.get("DOI"), ext.get("ArXiv")
    return {
        "id": rec_id(doi, arxiv, f"s2:{p.get('paperId')}"), "title": p.get("title"),
        "authors": [x.get("name") for x in p.get("authors") or []],
        "year": p.get("year"), "date": p.get("publicationDate"), "venue": p.get("venue"),
        "doi": doi, "arxiv": arxiv, "url": p.get("url"), "abstract": p.get("abstract") or "",
        "citations": p.get("citationCount"), "source": "semanticscholar"}


def cmd_s2(a):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": a.query, "limit": min(a.max, 100), "fields": S2_FIELDS}))
    for p in json.loads(get(url)).get("data", []):
        emit(_s2_rec(p))


def _s2_key(ident):
    ident = ident.strip()
    if ident.lower().startswith("arxiv:"):
        return "ARXIV:" + ident.split(":", 1)[1]
    if ident.lower().startswith("doi:"):
        ident = ident[4:]
    return "DOI:" + ident


def cmd_cites(a):
    url = (f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(_s2_key(a.ident))}"
           f"/citations?" + urllib.parse.urlencode({"limit": min(a.max, 100), "fields": S2_FIELDS}))
    for c in json.loads(get(url)).get("data", []):
        emit(_s2_rec(c["citingPaper"]))


# --------------------------------------------------------------- imports ---

def cmd_scispace(a):
    """Convert a saved SciSpace search-papers JSON response (stdin) to records."""
    data = json.load(sys.stdin)
    for p in data.get("papers", []):
        doi = p.get("doi")
        m = re.search(r"arxiv\.(\d{4}\.\d{4,5})", (doi or "").lower())
        arxiv = m.group(1) if m else None
        emit({
            "id": rec_id(doi, arxiv, f"scispace:{p.get('unique_id')}"), "title": p.get("title"),
            "authors": [x.get("display_name") for x in (p.get("authors") or {}).get("data", [])],
            "year": int(p["date"][:4]) if p.get("date") else None,
            "date": (p.get("date") or "")[:10] or None,
            "venue": (p.get("journal") or {}).get("display_name"), "doi": doi, "arxiv": arxiv,
            "url": f"https://scispace.com/papers/{p.get('full_slug')}",
            "abstract": p.get("abstract") or "", "tldr": p.get("tldr"),
            "citations": ((p.get("metrics") or {}).get("citations") or {}).get("total"),
            "source": "scispace"})


def _bib_fields(entry):
    f = {k.lower(): v.strip() for k, v in
         re.findall(r"(\w+)\s*=\s*[{\"]((?:[^{}]|\{[^{}]*\})*)[}\"]", entry)}
    return {k: re.sub(r"[{}]", "", v) for k, v in f.items()}


def cmd_import(a):
    """Import an export file (CSV, RIS, BibTeX) from SciSpace/Zotero/etc. into records."""
    path = Path(a.file)
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    rows = []
    if path.suffix.lower() == ".csv":
        import csv
        for r in csv.DictReader(text.splitlines()):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items() if k}
            pick = lambda *ks: next((r[k] for k in ks if r.get(k)), "")
            rows.append({"title": pick("title", "paper title"), "authors": pick("authors", "author"),
                         "year": pick("year", "publication year"), "doi": pick("doi"),
                         "venue": pick("journal", "venue", "source"), "abstract": pick("abstract"),
                         "extra": {k: v for k, v in r.items() if v and k not in
                                   ("title", "paper title", "authors", "author", "year", "doi", "abstract")}})
    elif path.suffix.lower() == ".ris":
        cur = {}
        for line in text.splitlines():
            m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line)
            if not m:
                continue
            tag, val = m.groups()
            if tag == "ER":
                rows.append(cur); cur = {}
            elif tag in ("TI", "T1"): cur["title"] = val
            elif tag in ("AU", "A1"): cur["authors"] = (cur.get("authors", "") + "; " + val).strip("; ")
            elif tag in ("PY", "Y1", "DA"): cur.setdefault("year", val[:4])
            elif tag == "DO": cur["doi"] = val
            elif tag in ("JO", "JF", "T2"): cur.setdefault("venue", val)
            elif tag == "AB": cur["abstract"] = val
    else:  # BibTeX
        for m in re.finditer(r"@\w+\s*\{.*?(?=\n@|\Z)", text, re.S):
            f = _bib_fields(m.group(0))
            rows.append({"title": f.get("title"), "authors": f.get("author", "").replace(" and ", "; "),
                         "year": f.get("year"), "doi": f.get("doi"), "venue": f.get("journal") or f.get("booktitle"),
                         "abstract": f.get("abstract", "")})
    for r in rows:
        if not r.get("title"):
            continue
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", r.get("doi") or "") or None
        m = re.search(r"arxiv\.(\d{4}\.\d{4,5})", (doi or "").lower())
        rec = {"id": rec_id(doi, m.group(1) if m else None, "title:" + re.sub(r"\W+", "", r["title"].lower())[:60]),
               "title": r["title"], "authors": [x.strip() for x in re.split(r";|\n", r.get("authors") or "") if x.strip()],
               "year": int(r["year"]) if str(r.get("year") or "").isdigit() else None, "date": None,
               "venue": r.get("venue"), "doi": doi, "arxiv": m.group(1) if m else None,
               "url": f"https://doi.org/{doi}" if doi else None, "abstract": r.get("abstract") or "",
               "citations": None, "source": a.source}
        if r.get("extra"):
            rec["extracted"] = r["extra"]  # e.g. SciSpace table columns: Methods, Limitations...
        emit(rec)


# ----------------------------------------------------------------- store ---

def cmd_add(a):
    path = Path(a.project) / "literature" / "papers.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                existing[r["id"]] = r
    titles = {re.sub(r"\W+", "", (r.get("title") or "").lower()): k for k, r in existing.items()}
    added = 0
    for line in sys.stdin:
        if not line.strip():
            continue
        r = json.loads(line)
        tkey = re.sub(r"\W+", "", (r.get("title") or "").lower())
        key = r.get("id") if r.get("id") in existing else titles.get(tkey)
        if key:  # merge: keep non-empty fields, record all sources
            old = existing[key]
            for k, v in r.items():
                if v and not old.get(k):
                    old[k] = v
            srcs = set(str(old.get("source", "")).split("+")) | {r.get("source", "")}
            old["source"] = "+".join(sorted(s for s in srcs if s))
        else:
            existing[r["id"]] = r
            titles[tkey] = r["id"]
            added += 1
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in existing.values()))
    print(f"{added} new, {len(existing)} total -> {path}", file=sys.stderr)


# ------------------------------------------------------------- citations ---

def fetch_bib(ident):
    ident = ident.strip()
    if ident.lower().startswith("arxiv:") or re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", ident):
        aid = re.sub(r"v\d+$", "", ident.split(":", 1)[-1])
        ident = f"10.48550/arXiv.{aid}"  # arXiv's DataCite DOI
    doi = ident[4:] if ident.lower().startswith("doi:") else ident
    return get(f"https://doi.org/{doi}", accept="application/x-bibtex; charset=utf-8")


STOP = {"a", "an", "the", "on", "of", "for", "towards", "toward", "to", "in", "and", "with"}


def rekey(bib):
    """Replace publisher keys (e.g. 'https://doi.org/...') with lastnameYEARword."""
    au = re.search(r"author\s*=\s*\{([^,}]+)", bib, re.I)
    yr = re.search(r"year\s*=\s*\{?(\d{4})", bib, re.I)
    ti = re.search(r"title\s*=\s*\{+([^}]+)", bib, re.I)
    last = re.sub(r"[^a-z]", "", (au.group(1).split()[-1] if au and " " in au.group(1).split(",")[0] and "," not in au.group(1) else (au.group(1) if au else "anon")).lower())
    word = next((w for w in re.findall(r"[a-z]+", (ti.group(1) if ti else "").lower()) if w not in STOP), "")
    key = f"{last or 'anon'}{yr.group(1) if yr else ''}{word}"
    return re.sub(r"^(\s*@\w+\s*\{)\s*[^,]+,", rf"\g<1>{key},", bib, count=1)


def cmd_bib(a):
    for ident in a.ids:
        try:
            print(rekey(fetch_bib(ident).strip()) + "\n")
        except Exception as e:
            print(f"% FAILED {ident}: {e}", file=sys.stderr)
            sys.exit(1)


def cmd_verify(a):
    d = Path(a.paper_dir)
    tex = "".join(p.read_text() for p in d.rglob("*.tex"))
    keys = set()
    for m in re.finditer(r"\\(?:no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", tex):
        keys |= {k.strip() for k in m.group(1).split(",") if k.strip()}
    bib = "".join(p.read_text() for p in d.rglob("*.bib"))
    entries = {m.group(1).strip(): m.group(0) for m in
               re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=\n@|\Z)", bib, re.S)}
    problems = []
    for k in sorted(keys - entries.keys()):
        problems.append(f"MISSING  \\cite{{{k}}} has no bib entry")
    for k in sorted(entries.keys() - keys):
        print(f"unused   {k}")
    for k in sorted(keys & entries.keys()):
        e = entries[k]
        doi = re.search(r"doi\s*=\s*[{\"]([^}\"]+)", e, re.I)
        arx = re.search(r"(?:eprint\s*=\s*[{\"]|arxiv\.org/abs/)([\d.]+)", e, re.I)
        if not (doi or arx):
            problems.append(f"UNVERIFIABLE {k}: no DOI or arXiv id")
            continue
        if a.offline:
            continue
        try:
            fetch_bib(f"arXiv:{arx.group(1)}" if arx else doi.group(1))
            print(f"ok       {k}")
        except Exception as ex:
            problems.append(f"UNRESOLVED {k}: {ex}")
    for p in problems:
        print(p)
    print(f"\n{len(keys)} cited, {len(entries)} in bib, {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in [("arxiv", cmd_arxiv), ("openalex", cmd_openalex), ("s2", cmd_s2)]:
        p = sp.add_parser(name)
        p.add_argument("query")
        p.add_argument("--max", type=int, default=25)
        p.add_argument("--since", help="YYYY-MM-DD")
        if name == "arxiv":
            p.add_argument("--cat", help="arXiv category, e.g. cs.LG")
        p.set_defaults(fn=fn)
    p = sp.add_parser("cites"); p.add_argument("ident"); p.add_argument("--max", type=int, default=25); p.set_defaults(fn=cmd_cites)
    p = sp.add_parser("scispace"); p.set_defaults(fn=cmd_scispace)
    p = sp.add_parser("import"); p.add_argument("file"); p.add_argument("--source", default="scispace-export"); p.set_defaults(fn=cmd_import)
    p = sp.add_parser("add"); p.add_argument("project"); p.set_defaults(fn=cmd_add)
    p = sp.add_parser("bib"); p.add_argument("ids", nargs="+"); p.set_defaults(fn=cmd_bib)
    p = sp.add_parser("verify"); p.add_argument("paper_dir"); p.add_argument("--offline", action="store_true"); p.set_defaults(fn=cmd_verify)
    a = ap.parse_args()
    try:
        a.fn(a)
    except urllib.error.HTTPError as e:
        hint = " (rate-limited; set S2_API_KEY or retry later)" if e.code == 429 else ""
        sys.exit(f"{a.cmd}: HTTP {e.code} from {e.url.split('?')[0]}{hint}")


if __name__ == "__main__":
    main()
