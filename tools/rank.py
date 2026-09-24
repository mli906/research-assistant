#!/usr/bin/env python3
"""Pairwise idea tournament (Bradley-Terry), replacing self-assigned 1-5 scores.

  rank.py pairs <idea_id> <idea_id> ... [--per-idea 4] [--seed 0]
      -> JSON lines {"a","b"}: a schedule where every pair is judged in both
         orders (position-bias control), or a random balanced subset for many ideas.
  rank.py score <judgments.jsonl> [--criterion X]
      judgments: {"a": id, "b": id, "winner": id|"tie", "criterion": "...", "judge": "...", "why": "..."}
      -> ranking with Bradley-Terry strength, wins/losses, and position-consistency.

Judges must be agents other than the one that wrote the ideas.
"""
import argparse
import itertools
import json
import math
import random
import sys
from collections import defaultdict


def cmd_pairs(a):
    ids = a.ids
    pairs = list(itertools.combinations(ids, 2))
    if len(ids) > 8:  # balanced random subset: each idea in ~per_idea comparisons
        rng = random.Random(a.seed)
        rng.shuffle(pairs)
        count, chosen = defaultdict(int), []
        for x, y in pairs:
            if count[x] < a.per_idea or count[y] < a.per_idea:
                chosen.append((x, y)); count[x] += 1; count[y] += 1
        pairs = chosen
    for x, y in pairs:
        print(json.dumps({"a": x, "b": y}))
        print(json.dumps({"a": y, "b": x}))


def cmd_score(a):
    js = [json.loads(l) for l in open(a.file) if l.strip()]
    if a.criterion:
        js = [j for j in js if j.get("criterion") == a.criterion]
    ids = sorted({j["a"] for j in js} | {j["b"] for j in js})
    w = defaultdict(float)  # w[(i,j)] = wins of i over j (ties = 0.5 each)
    rec = defaultdict(lambda: [0, 0, 0])
    for j in js:
        x, y, win = j["a"], j["b"], j["winner"]
        if win == "tie":
            w[(x, y)] += .5; w[(y, x)] += .5; rec[x][2] += 1; rec[y][2] += 1
        else:
            lose = y if win == x else x
            w[(win, lose)] += 1; rec[win][0] += 1; rec[lose][1] += 1
    p = {i: 1.0 for i in ids}
    for _ in range(200):  # MM algorithm (Hunter 2004) with a weak prior to handle unbeaten items
        new = {}
        for i in ids:
            wins = sum(w[(i, j)] for j in ids if j != i) + .1
            den = sum((w[(i, j)] + w[(j, i)] + .2) / (p[i] + p[j]) for j in ids if j != i)
            new[i] = wins / den if den else p[i]
        s = sum(new.values())
        p = {i: v * len(ids) / s for i, v in new.items()}
    # position consistency: same winner when order is swapped
    by_pair = defaultdict(list)
    for j in js:
        by_pair[(frozenset((j["a"], j["b"])), j.get("criterion"), j.get("judge"))].append(j["winner"])
    both = [v for v in by_pair.values() if len(v) >= 2]
    consistent = sum(1 for v in both if len(set(v)) == 1)
    print(f"{'rank':<5}{'idea':<24}{'BT-strength':>12}{'W-L-T':>10}")
    for r, i in enumerate(sorted(ids, key=lambda i: -p[i]), 1):
        print(f"{r:<5}{i:<24}{math.log(p[i]):>12.2f}{'-'.join(map(str, rec[i])):>10}")
    if both:
        print(f"\nposition consistency: {consistent}/{len(both)} pairs judged the same in both orders"
              + ("  <- low: judgments unreliable, add judges/criteria" if consistent / len(both) < .7 else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("pairs"); p.add_argument("ids", nargs="+"); p.add_argument("--per-idea", type=int, default=4)
    p.add_argument("--seed", type=int, default=0); p.set_defaults(fn=cmd_pairs)
    p = sp.add_parser("score"); p.add_argument("file"); p.add_argument("--criterion"); p.set_defaults(fn=cmd_score)
    a = ap.parse_args(); a.fn(a)


if __name__ == "__main__":
    main()
