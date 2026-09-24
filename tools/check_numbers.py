#!/usr/bin/env python3
"""Fail if the paper contains hand-typed result numbers.

Result numbers must come from files that analysis scripts write into
paper/generated/ (tables and \\newcommand macros), each starting with a header
line `% generated-by: <script path> from: <results path>`.

  check_numbers.py <paper_dir>

Flags, outside paper/generated/: decimals (0.83, 12.5), percentages (12%, 12\\%),
and ± values. Integers alone are allowed (years, counts in prose). Silence a
line that legitimately has such a number (a hyperparameter from the pre-registered
plan, a number quoted from a cited paper) with a trailing `% num-ok: <reason>`.
"""
import re
import sys
from pathlib import Path

NUM = re.compile(r"(?<![\w\\{.])(\d+\.\d+|\d+(?:\.\d+)?\s*\\?%|\\pm|±)")
SKIP_ENVS = ("equation", "align", "eqnarray")  # math is not a results claim by itself


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = Path(sys.argv[1])
    root = d.parent
    problems = []
    for f in sorted(d.rglob("*.tex")):
        if "generated" in f.relative_to(d).parts:
            continue
        env = None
        for i, line in enumerate(f.read_text().splitlines(), 1):
            if "% num-ok" in line:
                continue
            m = re.search(r"\\begin\{(\w+)\*?\}", line)
            if m and m.group(1) in SKIP_ENVS:
                env = m.group(1)
            if env:
                if re.search(rf"\\end\{{{env}\*?\}}", line):
                    env = None
                continue
            code = re.sub(r"(?<!\\)%.*", "", line)
            code = re.sub(r"\\(cite\w*|ref|cref|Cref|label|includegraphics|input|url|href)(\[[^\]]*\])?\{[^}]*\}", "", code)
            code = re.sub(r"\\(vspace|hspace|resizebox|scalebox)\{[^}]*\}", "", code)
            code = re.sub(r"\[\s*width=[^\]]*\]", "", code)
            for n in NUM.finditer(code):
                problems.append(f"{f.relative_to(d)}:{i}: hand-typed number '{n.group(0).strip()}' -> "
                                f"generate it into paper/generated/ or mark '% num-ok: <reason>'")
    gen = d / "generated"
    for g in sorted(gen.rglob("*.tex")) if gen.exists() else []:
        head = g.read_text().splitlines()[:1]
        m = re.match(r"%\s*generated-by:\s*(\S+)\s+from:\s*(.+)", head[0]) if head else None
        if not m:
            problems.append(f"generated/{g.name}: missing '% generated-by: <script> from: <results>' header")
            continue
        script = root / m.group(1)
        if not script.exists():
            problems.append(f"generated/{g.name}: generating script {m.group(1)} not found (paths relative to project dir)")
        for src in m.group(2).split(","):
            src = src.strip()
            if src and not any(root.glob(src)):
                problems.append(f"generated/{g.name}: results source {src} not found")
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
