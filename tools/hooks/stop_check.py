#!/usr/bin/env python3
"""Stop / SubagentStop gate: before Claude finishes, re-run deterministic checks
on any project whose paper or results changed since the last passing check.

  - lit.py verify --offline   (citations exist, are in the library, titles match)
  - check_numbers.py          (no hand-typed result numbers in the paper)
  - fidelity.py               (every run has a manifest; planned == actual or declared deviation)
  - seal.py check             (held-out evaluation untampered), if sealed

On failure, emits {"decision": "block", "reason": ...} so Claude keeps working on
the fix. Never blocks twice in a row (stop_hook_active), so it cannot loop.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))
T = ROOT / "tools"


def newest(paths):
    return max((p.stat().st_mtime for p in paths if p.exists()), default=0)


def run(args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode, [l for l in out if l and not l.startswith(("ok", "unused"))][-15:]


def main():
    ev = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    if ev.get("stop_hook_active"):
        return
    failures = []
    for proj in sorted((ROOT / "projects").glob("*/")):
        stamp = proj / ".checks_passed"
        last = stamp.stat().st_mtime if stamp.exists() else 0
        paper = [p for p in (proj / "paper").rglob("*") if p.suffix in (".tex", ".bib")] if (proj / "paper").exists() else []
        results = list((proj / "experiments" / "results").rglob("manifest.json")) if (proj / "experiments" / "results").exists() else []
        sealed = proj / "experiments" / "sealed"
        if max(newest(paper), newest(results), newest([sealed])) <= last:
            continue
        checks = []
        if any(p.suffix == ".tex" and p.stat().st_size > 50 for p in paper):
            checks += [("citations", [T / "lit.py", "verify", proj / "paper", "--offline"]),
                       ("numbers", [T / "check_numbers.py", proj / "paper"])]
        if (proj / "experiments" / "results").exists() and any((proj / "experiments" / "results").iterdir()):
            checks.append(("fidelity", [T / "fidelity.py", proj]))
        if sealed.exists():
            checks.append(("seal", [T / "seal.py", "check", proj]))
        bad = []
        for name, args in checks:
            code, out = run(args)
            if code:
                bad.append(f"[{name}] " + " | ".join(out))
        if bad:
            failures.append(f"{proj.name}: " + "\n  ".join(bad))
        else:
            stamp.touch()
    if failures:
        print(json.dumps({"decision": "block", "reason":
            "Integrity checks failed. Fix these, or if a fix needs the PI, report them plainly:\n"
            + "\n".join(failures)}))


if __name__ == "__main__":
    main()
