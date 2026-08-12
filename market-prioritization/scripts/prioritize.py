#!/usr/bin/env python3
"""Weighted market prioritization with sensitivity analysis.

Reads markets.json (schema: references/output-template.md), applies weights and
knockouts, ranks the markets, then stress-tests the ranking: each weight is perturbed
up and down, the ranking recomputed, and every pair that swaps order recorded. Markets
that never move are robust; markets that swap are contested, and the script names the
criterion whose weight decides each swap.

The point: a ranking that flips under a small, reasonable change in weights is not a
decision, it is a preference. This tells you which is which.

Usage:
  python3 prioritize.py markets.json [--delta 10] [--json out.json]

No dependencies beyond the standard library. No network.
"""

import argparse
import json
import sys
from itertools import combinations

MAX_SCORE = 5


def validate(model):
    problems = []
    crits = model.get("criteria", [])
    if not crits:
        problems.append("no criteria")
    total = sum(c.get("weight", 0) for c in crits)
    if round(total, 6) != 100:
        problems.append(f"weights sum to {total}, expected 100")
    for c in crits:
        if not c.get("rationale"):
            problems.append(f"criterion {c.get('id')!r} has no rationale (undefended weight)")
    for m in model.get("markets", []):
        for c in crits:
            v = m.get("scores", {}).get(c["id"])
            if v is None:
                problems.append(f"{m.get('name')!r} missing score for {c['id']!r}")
            elif not 1 <= v <= MAX_SCORE:
                problems.append(f"{m.get('name')!r} score for {c['id']!r} is {v}, expected 1-{MAX_SCORE}")
    return problems


def score_with(model, weights):
    """Return {market: normalized score} for a given {criterion_id: weight} mapping."""
    out = {}
    for m in model["markets"]:
        if m.get("knockouts_hit"):
            continue
        total = sum(m["scores"][cid] * w for cid, w in weights.items())
        out[m["name"]] = round(total / MAX_SCORE, 2)  # weights sum to 100, so max is 100
    return out


def rank_order(scores):
    return [n for n, _ in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))]


def sensitivity(model, base_weights, delta):
    """Perturb each weight up and down; record which pairs swap and what drives it."""
    base_rank = rank_order(score_with(model, base_weights))
    base_pos = {n: i for i, n in enumerate(base_rank)}
    swaps = {}  # (a, b) -> set of criteria whose reweighting flips them

    for cid in base_weights:
        for direction in (delta, -delta):
            new_w = dict(base_weights)
            target = new_w[cid] + direction
            if target < 0:
                continue
            new_w[cid] = target
            others = [k for k in new_w if k != cid]
            spare = sum(new_w[k] for k in others)
            if spare <= 0:
                continue
            # redistribute the difference proportionally across the other weights
            adjust = -direction
            for k in others:
                new_w[k] = max(0.0, new_w[k] + adjust * (new_w[k] / spare))

            order = rank_order(score_with(model, new_w))
            pos = {n: i for i, n in enumerate(order)}
            for a, b in combinations(base_rank, 2):
                if (base_pos[a] < base_pos[b]) != (pos[a] < pos[b]):
                    swaps.setdefault(tuple(sorted((a, b))), set()).add(cid)
    return base_rank, swaps


def main():
    ap = argparse.ArgumentParser(description="Rank markets and test how robust the ranking is.")
    ap.add_argument("model")
    ap.add_argument("--delta", type=float, default=10.0,
                    help="weight perturbation in points (default 10)")
    ap.add_argument("--json", dest="json_out", help="write the full result as JSON")
    args = ap.parse_args()

    model = json.load(open(args.model, encoding="utf-8"))
    problems = validate(model)
    if problems:
        print("model is invalid:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    weights = {c["id"]: float(c["weight"]) for c in model["criteria"]}
    scores = score_with(model, weights)
    base_rank, swaps = sensitivity(model, weights, args.delta)

    contested = {}
    for (a, b), crits in swaps.items():
        contested.setdefault(a, set()).update({(b, c) for c in crits})
        contested.setdefault(b, set()).update({(a, c) for c in crits})

    print(f"{model.get('brand', '?')}: {len(scores)} ranked, "
          f"{len(model['markets']) - len(scores)} knocked out, delta +/-{args.delta:g}\n")
    print("| # | Market | Score | Robustness |")
    print("|---|--------|-------|------------|")
    for i, name in enumerate(base_rank, 1):
        if name in contested:
            with_who = sorted({w for w, _ in contested[name]})
            note = "contested with " + ", ".join(with_who)
        else:
            note = "robust"
        print(f"| {i} | {name} | {scores[name]} | {note} |")

    knocked = [m for m in model["markets"] if m.get("knockouts_hit")]
    if knocked:
        print("\nKnocked out:")
        for m in knocked:
            print(f"  - {m['name']}: {', '.join(m['knockouts_hit'])}")

    if swaps:
        print("\nDecisive criteria (the questions worth settling with evidence):")
        for (a, b), crits in sorted(swaps.items()):
            print(f"  - {a} vs {b}: decided by {', '.join(sorted(crits))}")
    else:
        print("\nNo pair swapped under the tested weightings: the ranking is robust.")

    if args.json_out:
        result = {
            "scores": scores,
            "ranking": base_rank,
            "contested": {a: sorted({w for w, _ in v}) for a, v in contested.items()},
            "decisive_criteria": {f"{a} vs {b}": sorted(c) for (a, b), c in swaps.items()},
            "knocked_out": [m["name"] for m in knocked],
            "delta": args.delta,
        }
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"\nwrote {args.json_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
