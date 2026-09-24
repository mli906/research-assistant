#!/usr/bin/env python3
"""Literature toolkit for the research assistant (stdlib only).

Complements the SciSpace MCP (broad semantic search) with sources that are
fresher or more structured:

  lit.py arxiv    'memory (poisoning OR injection) "LLM agent"' [--since 2026-06-01] [--sort relevance|date] [--cat cs.CR]
  lit.py openalex "query" [--since 2026-01-01] [--sort relevance|cited]
  lit.py s2       "query"                        # Semantic Scholar (needs S2_API_KEY in practice)
  lit.py cites    <doi|arXiv:id>                 # who cites this paper (forward snowball)
  lit.py fetch    <doi|arXiv:id> ... [--source scispace]   # authoritative metadata for known ids
  lit.py import   <export.csv|.ris|.bib> [--source ...]    # SciSpace/Zotero/other exports
  lit.py zotero   collections | items [--collection X|--tag T|--q text] | fulltext <itemKey>
  lit.py add      <project_dir> [--tag core] < records.jsonl   # merge into literature/papers.jsonl
  lit.py tag      <project_dir> <id> ... [--add X] [--remove Y]
  lit.py export-ris <project_dir> [--tag core]   # for File > Import in Zotero
  lit.py bib      <doi|arXiv:id> [...]           # fetch real BibTeX (never hand-write it)
  lit.py verify   <paper_dir> [--offline]        # citation integrity against the project library

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

ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def arxiv_query(q):
    """'memory (poisoning OR injection) "LLM agent"' -> arXiv search_query syntax.

    Words and "quoted phrases" become all: terms, joined by AND unless an explicit
    OR / AND / ANDNOT operator sits between them; parentheses group.
    """
    out, prev_term = [], False
    for tok in re.findall(r'"[^"]+"|\(|\)|[^\s()]+', q):
        if tok.upper() in ("OR", "AND", "ANDNOT"):
            out.append(tok.upper()); prev_term = False
        elif tok == "(":
            if prev_term:
                out.append("AND")
            out.append("("); prev_term = False
        elif tok == ")":
            out.append(")"); prev_term = True
        else:
            if prev_term:
                out.append("AND")
            out.append(f"all:{tok}" if tok.startswith('"') else f"all:{tok}")
            prev_term = True
    return " ".join(out).replace("( ", "(").replace(" )", ")")


def cmd_arxiv(a):
    terms = arxiv_query(a.query)
    if a.cat:
        terms = f"({terms}) AND cat:{a.cat}"
    # relevance sort + date filter: over-fetch so the --since filter leaves enough
    n = a.max * 4 if (a.since and a.sort == "relevance") else a.max
    url = ("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": terms, "start": 0, "max_results": min(n, 200),
        "sortBy": "relevance" if a.sort == "relevance" else "submittedDate",
        "sortOrder": "descending"}))
    shown = 0
    for rec in _arxiv_entries(get(url)):
        if a.since and rec["date"] < a.since:
            continue
        emit(rec)
        shown += 1
        if shown >= a.max:
            break


def _arxiv_entries(xml):
    ns = ARXIV_NS
    root = ET.fromstring(xml)
    for e in root.findall("a:entry", ns):
        if e.find("a:title", ns) is None or e.findtext("a:title", "", ns) == "Error":
            continue
        date = e.findtext("a:published", "", ns)[:10]
        aid = e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid)
        doi = e.findtext("x:doi", None, ns)
        yield ({
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
    # title_and_abstract.search matches all words in title/abstract; the bare
    # `search` param also matches full text and ranks famous off-topic papers high.
    filt = [f"title_and_abstract.search:{a.query.replace(',', ' ')}"]
    if a.since:
        filt.append(f"from_publication_date:{a.since}")
    params = {"filter": ",".join(filt), "per-page": min(a.max, 200),
              "sort": "cited_by_count:desc" if a.sort == "cited" else "relevance_score:desc"}
    data = json.loads(get("https://api.openalex.org/works?" + urllib.parse.urlencode(params)))
    for w in data.get("results", []):
        emit(_openalex_rec(w))


def cmd_fetch(a):
    """Fetch authoritative metadata for known ids (e.g. DOIs from SciSpace hits).

    arXiv ids via the arXiv API; DOIs via OpenAlex, falling back to Crossref.
    Records keep `source` = --source so provenance of the *finding* is preserved.
    """
    ids = a.ids or [l.strip() for l in sys.stdin if l.strip()]
    arx, dois = [], []
    for i in ids:
        i = re.sub(r"^https?://(dx\.)?doi\.org/", "", i.strip())
        m = re.search(r"(?:arxiv[:.]|arxiv\.org/abs/)(\d{4}\.\d{4,5})", i, re.I)
        if m or re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", i):
            arx.append(re.sub(r"v\d+$", "", m.group(1) if m else i))
        else:
            dois.append(i[4:] if i.lower().startswith("doi:") else i)
    for k in range(0, len(arx), 50):
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(arx[k:k + 50]), "max_results": 50})
        for rec in _arxiv_entries(get(url)):
            rec["source"] = a.source
            emit(rec)
    for d in dois:
        try:
            w = json.loads(get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(d)}"))
            rec = _openalex_rec(w)
        except urllib.error.HTTPError:
            try:
                m = json.loads(get(f"https://api.crossref.org/works/{urllib.parse.quote(d)}"))["message"]
            except urllib.error.HTTPError as e:
                print(f"fetch: {d} not found ({e.code})", file=sys.stderr)
                continue
            dp = (m.get("issued") or {}).get("date-parts", [[None]])[0]
            rec = {"id": rec_id(d), "title": (m.get("title") or [""])[0],
                   "authors": [f"{x.get('given', '')} {x.get('family', '')}".strip() for x in m.get("author", [])],
                   "year": dp[0], "date": "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(dp) if p),
                   "venue": (m.get("container-title") or [None])[0], "doi": d, "arxiv": None,
                   "url": f"https://doi.org/{d}", "abstract": re.sub(r"<[^>]+>", "", m.get("abstract", "")),
                   "citations": m.get("is-referenced-by-count")}
        rec["source"] = a.source
        emit(rec)


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

def _norm_title(t):
    return re.sub(r"\W+", "", (t or "").lower())


def load_library(project):
    path = Path(project) / "literature" / "papers.jsonl"
    recs = []
    if path.exists():
        recs = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    return recs


def cmd_add(a):
    import fcntl
    path = Path(a.project) / "literature" / "papers.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    incoming = [json.loads(l) for l in sys.stdin if l.strip()]
    # parallel lit-scout agents write here: hold an exclusive lock for read-modify-write
    with open(path.with_suffix(".lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        existing = {r["id"]: r for r in load_library(a.project)}
        titles = {_norm_title(r.get("title")): k for k, r in existing.items()}
        added = 0
        for r in incoming:
            if a.tag:
                r["tags"] = sorted(set(r.get("tags", [])) | set(a.tag))
            tkey = _norm_title(r.get("title"))
            key = r.get("id") if r.get("id") in existing else titles.get(tkey)
            if key:  # merge: keep non-empty fields, union sources and tags
                old = existing[key]
                for k, v in r.items():
                    if v and not old.get(k):
                        old[k] = v
                srcs = set(str(old.get("source", "")).split("+")) | set(str(r.get("source", "")).split("+"))
                old["source"] = "+".join(sorted(s for s in srcs if s))
                if r.get("tags"):
                    old["tags"] = sorted(set(old.get("tags", [])) | set(r["tags"]))
            else:
                existing[r["id"]] = r
                titles[tkey] = r["id"]
                added += 1
        tmp = path.with_suffix(".tmp")
        tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in existing.values()))
        tmp.replace(path)
    print(f"{added} new, {len(existing)} total -> {path}", file=sys.stderr)


def cmd_tag(a):
    """Add/remove tags on existing records (lock-safe)."""
    import fcntl
    path = Path(a.project) / "literature" / "papers.jsonl"
    with open(path.with_suffix(".lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        recs = load_library(a.project)
        n = 0
        for r in recs:
            if r["id"] in a.ids:
                r["tags"] = sorted((set(r.get("tags", [])) | set(a.add or [])) - set(a.remove or []))
                n += 1
        tmp = path.with_suffix(".tmp")
        tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs))
        tmp.replace(path)
    missing = set(a.ids) - {r["id"] for r in recs}
    print(f"retagged {n}" + (f"; not found: {sorted(missing)}" if missing else ""), file=sys.stderr)


def cmd_export_ris(a):
    """Write the project library as RIS (for File > Import in Zotero/EndNote/Mendeley)."""
    for r in load_library(a.project):
        if a.tag and not set(a.tag) & set(r.get("tags", [])):
            continue
        ty = "JOUR" if r.get("venue") and "arxiv" not in str(r.get("venue")).lower() else "PREPRINT" if r.get("arxiv") else "GEN"
        print(f"TY  - {ty}\nTI  - {r.get('title', '')}")
        for au in r.get("authors") or []:
            print(f"AU  - {au}")
        for k, tag in (("year", "PY"), ("venue", "JO"), ("doi", "DO"), ("url", "UR")):
            if r.get(k):
                print(f"{tag}  - {r[k]}")
        if r.get("abstract"):
            print(f"AB  - {r['abstract']}")
        print(f"N1  - research-assistant id: {r['id']}; source: {r.get('source', '')}")
        for t in r.get("tags", []):
            print(f"KW  - {t}")
        print("ER  - \n")


# ---------------------------------------------------------------- zotero ---

ZOTERO = "http://localhost:23119/api/users/0"


def _zget(path, **params):
    url = f"{ZOTERO}{path}" + ("?" + urllib.parse.urlencode(params) if params else "")
    try:
        return json.loads(get(url, retries=1))
    except urllib.error.HTTPError as e:
        if e.code == 403:
            sys.exit("zotero: local API disabled. In Zotero: Settings > Advanced > "
                     "'Allow other applications on this computer to communicate with Zotero'.")
        raise
    except urllib.error.URLError:
        sys.exit("zotero: Zotero is not running (start the desktop app).")


def _zpaged(path, **params):
    start = 0
    while True:
        page = _zget(path, start=start, limit=100, **params)
        yield from page
        if len(page) < 100:
            break
        start += 100


def _zrec(it):
    d = it["data"]
    doi = d.get("DOI") or (re.search(r"DOI:\s*(\S+)", d.get("extra", "")) or [None, None])[1]
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})|arXiv:\s*(\d{4}\.\d{4,5})",
                  " ".join([d.get("url", ""), d.get("extra", ""), d.get("archiveID", "")]))
    arxiv = (m.group(1) or m.group(2)) if m else None
    authors = [c.get("name") or f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
               for c in d.get("creators", []) if c.get("creatorType") in ("author", None)]
    y = re.search(r"\d{4}", d.get("date", ""))
    return {"id": rec_id(doi, arxiv, f"zotero:{d['key']}"), "title": d.get("title"), "authors": authors,
            "year": int(y.group(0)) if y else None, "date": d.get("date"),
            "venue": d.get("publicationTitle") or d.get("proceedingsTitle") or d.get("repository"),
            "doi": doi, "arxiv": arxiv, "url": d.get("url"), "abstract": d.get("abstractNote", ""),
            "citations": None, "source": "zotero", "zotero_key": d["key"],
            "tags": sorted({t["tag"] for t in d.get("tags", [])} | {"pi-library"})}


def cmd_zotero(a):
    if a.action == "collections":
        cols = {c["key"]: c["data"] for c in _zpaged("/collections")}
        def path(k):
            c = cols[k]
            return (path(c["parentCollection"]) + " / " if c.get("parentCollection") else "") + c["name"]
        for k in sorted(cols, key=path):
            print(f"{k}  {path(k)}")
    elif a.action == "items":
        if a.collection:
            cols = {c["data"]["name"].lower(): c["key"] for c in _zpaged("/collections")}
            key = a.collection if a.collection in cols.values() else cols.get(a.collection.lower())
            if not key:
                sys.exit(f"zotero: no collection named {a.collection!r} (try `lit.py zotero collections`)")
            src = _zpaged(f"/collections/{key}/items/top")
        else:
            params = {"q": a.q} if a.q else {}
            if a.tag:
                params["tag"] = a.tag
            src = _zpaged("/items/top", **params)
        for it in src:
            if it["data"].get("itemType") in ("attachment", "note", "annotation"):
                continue
            emit(_zrec(it))
    elif a.action == "fulltext":
        # full text of an item's PDF, as indexed by Zotero (for close reading)
        for ch in _zget(f"/items/{a.key}/children"):
            if ch["data"].get("contentType") == "application/pdf":
                try:
                    print(_zget(f"/items/{ch['key']}/fulltext").get("content", ""))
                except SystemExit:
                    raise
                except Exception:
                    p = Path.home() / "Zotero" / "storage" / ch["key"] / ch["data"].get("filename", "")
                    print(f"(not indexed; PDF at {p})")
                return
        sys.exit(f"zotero: item {a.key} has no PDF attachment")


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


def _title_sim(a, b):
    ta, tb = set(re.findall(r"[a-z0-9]+", (a or "").lower())), set(re.findall(r"[a-z0-9]+", (b or "").lower()))
    return len(ta & tb) / max(1, len(ta | tb))


def cmd_verify(a):
    """Citation integrity: every \\cite has a bib entry with a DOI/arXiv id, that
    entry's paper is in the project library (literature/papers.jsonl) with a
    matching title, and (online) the id still resolves to the same title."""
    d = Path(a.paper_dir)
    tex = "".join(p.read_text() for p in d.rglob("*.tex"))
    tex = re.sub(r"(?<!\\)%.*", "", tex)  # ignore commented-out cites
    keys = set()
    for m in re.finditer(r"\\(?:no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", tex):
        keys |= {k.strip() for k in m.group(1).split(",") if k.strip()}
    bib = "".join(p.read_text() for p in d.rglob("*.bib"))
    entries = {m.group(1).strip(): m.group(0) for m in
               re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=\n\s*@|\Z)", bib, re.S)}
    lib = load_library(d.parent)
    by_doi = {(r.get("doi") or "").lower(): r for r in lib if r.get("doi")}
    by_arx = {r["arxiv"]: r for r in lib if r.get("arxiv")}
    problems = []
    for k in sorted(keys - entries.keys()):
        problems.append(f"MISSING      \\cite{{{k}}} has no bib entry")
    for k in sorted(entries.keys() - keys):
        print(f"unused       {k}")
    for k in sorted(keys & entries.keys()):
        e = entries[k]
        doi = re.search(r"doi\s*=\s*[{\"]([^}\"]+)", e, re.I)
        arx = re.search(r"(?:eprint\s*=\s*[{\"]|arxiv\.org/abs/|10\.48550/arxiv\.)(\d{4}\.\d{4,5})", e, re.I)
        title = re.search(r"\btitle\s*=\s*[{\"]((?:[^{}]|\{[^{}]*\})*)[}\"]", e, re.I)
        title = re.sub(r"[{}]", "", title.group(1)) if title else ""
        if not (doi or arx):
            problems.append(f"UNVERIFIABLE {k}: no DOI or arXiv id")
            continue
        rec = (by_arx.get(arx.group(1)) if arx else None) or (by_doi.get(doi.group(1).lower()) if doi else None)
        if not rec and lib:
            problems.append(f"NOT-IN-LIB   {k}: not in literature/papers.jsonl (cite only papers the review stored)")
        elif rec and _title_sim(title, rec.get("title")) < 0.6:
            problems.append(f"TITLE-DIFF   {k}: bib '{title[:60]}' vs library '{(rec.get('title') or '')[:60]}'")
        if a.offline:
            continue
        try:
            fresh = fetch_bib(f"arXiv:{arx.group(1)}" if arx else doi.group(1))
            ft = re.search(r"\btitle\s*=\s*[{\"]((?:[^{}]|\{[^{}]*\})*)[}\"]", fresh, re.I)
            if ft and _title_sim(title, re.sub(r"[{}]", "", ft.group(1))) < 0.6:
                problems.append(f"ALTERED      {k}: id resolves to a different title: '{ft.group(1)[:60]}'")
            else:
                print(f"ok           {k}")
        except Exception as ex:
            problems.append(f"UNRESOLVED   {k}: {ex}")
    for p in problems:
        print(p)
    if not lib:
        print("note: no literature/papers.jsonl next to the paper dir; library checks skipped")
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
            p.add_argument("--sort", choices=["relevance", "date"], default="relevance")
        if name == "openalex":
            p.add_argument("--sort", choices=["relevance", "cited"], default="relevance")
        p.set_defaults(fn=fn)
    p = sp.add_parser("fetch"); p.add_argument("ids", nargs="*"); p.add_argument("--source", default="fetch"); p.set_defaults(fn=cmd_fetch)
    p = sp.add_parser("cites"); p.add_argument("ident"); p.add_argument("--max", type=int, default=25); p.set_defaults(fn=cmd_cites)
    p = sp.add_parser("scispace"); p.set_defaults(fn=cmd_scispace)
    p = sp.add_parser("import"); p.add_argument("file"); p.add_argument("--source", default="scispace-export"); p.set_defaults(fn=cmd_import)
    p = sp.add_parser("zotero"); p.add_argument("action", choices=["collections", "items", "fulltext"])
    p.add_argument("key", nargs="?", help="item key (fulltext)"); p.add_argument("--collection"); p.add_argument("--tag"); p.add_argument("--q")
    p.set_defaults(fn=cmd_zotero)
    p = sp.add_parser("add"); p.add_argument("project"); p.add_argument("--tag", action="append", help="tag records (repeatable)"); p.set_defaults(fn=cmd_add)
    p = sp.add_parser("tag"); p.add_argument("project"); p.add_argument("ids", nargs="+")
    p.add_argument("--add", action="append"); p.add_argument("--remove", action="append"); p.set_defaults(fn=cmd_tag)
    p = sp.add_parser("export-ris"); p.add_argument("project"); p.add_argument("--tag", action="append"); p.set_defaults(fn=cmd_export_ris)
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
