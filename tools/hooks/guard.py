#!/usr/bin/env python3
"""PreToolUse guard: makes two integrity rules mechanical instead of prompt-only.

1. Sealed held-out evaluation: no tool may read, list or modify
   projects/*/experiments/sealed/ except `python3 tools/seal.py check|run`.
2. Pre-registered hypotheses (hypotheses/*.md with "Status: pre-registered"):
   content above "## Deviations log" is frozen. Allowed: appending deviations,
   and moving Status to supported/refuted/inconclusive (never back to draft).

Exit code 2 blocks the tool call and shows the reason to Claude.
"""
import json
import re
import sys
from pathlib import Path

SEALED = re.compile(r"experiments/sealed(?!\.staging)(/|\b)")
HYP = re.compile(r"(^|/)hypotheses/[^/]+\.md$")
FINAL = ("supported", "refuted", "inconclusive")


def block(msg):
    print(f"BLOCKED by research-assistant guard: {msg}", file=sys.stderr)
    sys.exit(2)


def frozen_part(text):
    body = text.split("## Deviations log")[0]
    return re.sub(r"^\*\*Status:\*\*.*$", "", body, flags=re.M).strip()


def status(text):
    m = re.search(r"^\*\*Status:\*\*\s*(.*)$", text, re.M)
    return m.group(1).strip().lower() if m else ""


def check_hypothesis(path, new_text):
    p = Path(path)
    if not p.exists():
        return
    old = p.read_text()
    if "pre-registered" not in status(old) and not status(old).startswith(FINAL):
        return
    if frozen_part(old) != frozen_part(new_text):
        block(f"{p.name} is pre-registered; only the Deviations log may change. "
              "Append a dated deviation entry instead of editing the hypothesis.")
    if not status(new_text).startswith(("pre-registered",) + FINAL):
        block(f"{p.name}: Status can move from pre-registered only to supported/refuted/inconclusive.")


def main():
    ev = json.load(sys.stdin)
    tool, ti = ev.get("tool_name", ""), ev.get("tool_input", {}) or {}
    paths = [str(ti.get(k)) for k in ("file_path", "path", "notebook_path", "pattern") if ti.get(k)]
    if tool == "Bash":
        cmd = ti.get("command", "")
        if SEALED.search(cmd) and not re.match(r"^\s*python3?\s+(\S*/)?tools/seal\.py\s+(check|run)\b", cmd):
            block("experiments/sealed/ is the held-out evaluation. Use `python3 tools/seal.py run <project> -- ...`.")
        if re.search(r"hypotheses/\S*\.md", cmd) and re.search(r"(sed\s+-i|>\s*\S*hypotheses/|\btee\b|\bmv\b|\brm\b|\bcp\b|truncate|perl\s+-[pi])", cmd):
            block("modify hypothesis files with the Edit tool (pre-registration is checked there), not via shell.")
        return
    for p in paths:
        if SEALED.search(p):
            block("experiments/sealed/ is the held-out evaluation and not readable by agents. "
                  "Use `python3 tools/seal.py run <project> -- ...` for aggregate metrics.")
    fp = ti.get("file_path", "")
    if tool in ("Edit", "Write", "MultiEdit") and HYP.search(fp):
        if tool == "Write":
            new = ti.get("content", "")
        else:
            new = Path(fp).read_text() if Path(fp).exists() else ""
            edits = ti.get("edits") or [{"old_string": ti.get("old_string", ""), "new_string": ti.get("new_string", ""),
                                         "replace_all": ti.get("replace_all", False)}]
            for e in edits:
                new = new.replace(e["old_string"], e["new_string"], -1 if e.get("replace_all") else 1)
        check_hypothesis(fp, new)


if __name__ == "__main__":
    main()
