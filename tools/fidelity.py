#!/usr/bin/env python3
"""Experimental-fidelity audit: did what ran match what was planned?

Every run writes experiments/results/<run-id>/manifest.json:
  {"run_id": "...", "experiment": "E1", "git_sha": "...", "config": "configs/e1.yaml",
   "seed": 0, "started": "...", "finished": "...",
   "planned": {"n_test_items": 500, "model": "claude-sonnet-5", "baselines": ["mem0", "no-memory"], ...},
   "actual":  {"n_test_items": 500, "model": "claude-sonnet-5", "baselines": ["mem0", "no-memory"], ...},
   "deviations": [{"field": "...", "reason": "...", "approved_by": "PI|pending", "date": "..."}]}

`planned` is copied from experiments/plan.md when the run is set up. `actual` is
measured by the code (len(dataset), the model string actually sent, etc.), never
copied from `planned`.

  fidelity.py <project_dir> [--run RUN_ID]

Exit 1 if any planned field is missing from or different in `actual` without a
deviation entry, or if provenance fields are missing. Deviations with
approved_by "pending" are listed as warnings for the PI.
"""
import argparse
import json
import sys
from pathlib import Path

REQUIRED = ("run_id", "experiment", "git_sha", "config", "seed", "planned", "actual")


def audit(man):
    errs, warns = [], []
    for k in REQUIRED:
        if k not in man:
            errs.append(f"missing field '{k}'")
    planned, actual = man.get("planned", {}), man.get("actual", {})
    dev = {d.get("field"): d for d in man.get("deviations", [])}
    for k, pv in planned.items():
        av = actual.get(k, "<missing>")
        same = (sorted(map(str, pv)) == sorted(map(str, av))) if isinstance(pv, list) and isinstance(av, list) else pv == av
        if isinstance(pv, (int, float)) and isinstance(av, (int, float)) and not isinstance(pv, bool):
            same = abs(pv - av) <= 1e-9 * max(1, abs(pv))
        if not same:
            if k in dev and dev[k].get("approved_by") in (None, "", "pending"):
                warns.append(f"deviation '{k}': planned {pv!r} vs actual {av!r} "
                             f"({dev[k].get('reason', '')}) awaiting PI approval")
            elif k not in dev:
                errs.append(f"UNDECLARED deviation '{k}': planned {pv!r} vs actual {av!r}")
    if actual and set(actual) - set(planned):
        warns.append(f"actual has unplanned fields: {sorted(set(actual) - set(planned))}")
    return errs, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("--run")
    a = ap.parse_args()
    res = Path(a.project) / "experiments" / "results"
    mans = sorted(res.glob(f"{a.run or '*'}/manifest.json"))
    runs = [p for p in res.iterdir() if p.is_dir()] if res.exists() else []
    bad = 0
    for r in runs:
        if a.run and r.name != a.run:
            continue
        if not (r / "manifest.json").exists():
            print(f"{r.name}: ERROR no manifest.json")
            bad += 1
    for m in mans:
        try:
            errs, warns = audit(json.loads(m.read_text()))
        except json.JSONDecodeError as e:
            errs, warns = [f"invalid JSON: {e}"], []
        for e in errs:
            print(f"{m.parent.name}: ERROR {e}")
        for w in warns:
            print(f"{m.parent.name}: WARN  {w}")
        if not errs and not warns:
            print(f"{m.parent.name}: ok")
        bad += bool(errs)
    print(f"{len(mans)} manifest(s), {bad} with errors")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
