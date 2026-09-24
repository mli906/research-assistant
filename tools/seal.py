#!/usr/bin/env python3
"""Seal / verify / use a held-out evaluation.

Layout (per project):
  experiments/sealed.staging/   built by the experiment designer before pre-registration:
      evaluate.py               owns the held-out data; runs the system under test on it and
                                prints ONLY aggregate metrics (JSON) to stdout
      data/ ...                 held-out items (never shown to the implementing agent)
  experiments/sealed/           after `seal.py seal`: read-only copy + SEAL.json (hashes)

  seal.py seal   <project>      staging -> sealed, chmod read-only, record hashes  (PI approval)
  seal.py check  <project>      verify hashes (tampering check)
  seal.py run    <project> -- <args for evaluate.py>
                                verify, run evaluate.py, append to sealed_access.log, print metrics.
                                Every call is logged. Repeated evaluation on the held-out set
                                is visible to the PI and must be reported in the paper.

Agents may not read or modify experiments/sealed/ (enforced by tools/hooks/guard.py);
`seal.py run` is the only allowed access. Unsealing is a PI-only action done by hand.
"""
import datetime
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path


def hashes(d):
    return {str(p.relative_to(d)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(d.rglob("*")) if p.is_file() and p.name != "SEAL.json"}


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("seal", "check", "run"):
        sys.exit(__doc__)
    cmd, proj = sys.argv[1], Path(sys.argv[2])
    staging, sealed = proj / "experiments" / "sealed.staging", proj / "experiments" / "sealed"
    if cmd == "seal":
        if sealed.exists():
            sys.exit("already sealed; unsealing is a manual PI action")
        if not (staging / "evaluate.py").exists():
            sys.exit(f"{staging}/evaluate.py missing")
        shutil.copytree(staging, sealed)
        seal = {"sealed_at": datetime.datetime.now().isoformat(timespec="seconds"), "files": hashes(sealed)}
        (sealed / "SEAL.json").write_text(json.dumps(seal, indent=1))
        for p in sealed.rglob("*"):
            os.chmod(p, (p.stat().st_mode | (stat.S_IXUSR if p.is_dir() else 0)) & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
        os.chmod(sealed, 0o555)
        shutil.rmtree(staging)
        print(f"sealed {len(seal['files'])} files; staging removed")
        return
    if not (sealed / "SEAL.json").exists():
        sys.exit("not sealed")
    seal = json.loads((sealed / "SEAL.json").read_text())
    now = hashes(sealed)
    if now != seal["files"]:
        changed = sorted(set(now.items()) ^ set(seal["files"].items()))
        sys.exit(f"TAMPERED: sealed files changed since {seal['sealed_at']}: {[c[0] for c in changed]}")
    if cmd == "check":
        print(f"ok: {len(now)} files match seal of {seal['sealed_at']}")
        return
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    log = proj / "experiments" / "sealed_access.log"
    n = sum(1 for _ in open(log)) + 1 if log.exists() else 1
    r = subprocess.run([sys.executable, str(sealed / "evaluate.py"), *args], capture_output=True, text=True)
    with open(log, "a") as f:
        f.write(json.dumps({"n": n, "time": datetime.datetime.now().isoformat(timespec="seconds"),
                            "args": args, "exit": r.returncode, "stdout": r.stdout[-2000:]}) + "\n")
    print(f"[held-out evaluation #{n}; all calls are logged and reported]", file=sys.stderr)
    sys.stdout.write(r.stdout)
    if r.returncode:
        sys.stderr.write(r.stderr[-2000:])
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
