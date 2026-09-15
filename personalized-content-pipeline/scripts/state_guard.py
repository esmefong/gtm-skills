#!/usr/bin/env python3
"""Deterministic per-customer content gate for the personalized-content-pipeline skill.

Checks a draft against the customer's state file: do-not-say phrases (with the recorded
reason echoed back), openings repeated from previously logged assets, unfilled merge
tokens, and, when the brief is supplied, stale facts and facts a correction superseded.
Prints PASS or FAIL with every reason. Exit 0 on pass, 1 on fail.

With --log, appends the shipped asset to the state's append-only asset log instead of
checking, so the next run's repetition check includes it.

Usage:
  python3 state_guard.py draft.md state.json [--brief brief.json] [--as-of YYYY-MM-DD]
  python3 state_guard.py draft.md state.json --log --asset-type abm-onepager

No dependencies beyond the standard library. No network.
"""

import argparse
import datetime
import json
import re
import sys


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except (ValueError, TypeError):
            continue
    return None


def first_sentence(text):
    para = []
    for line in text.splitlines():
        stripped = line.strip()
        if para and not stripped:
            break
        if stripped and not stripped.startswith("#") and not stripped.startswith(">"):
            para.append(stripped)
        elif para:
            break
    joined = " ".join(para)
    return re.split(r"(?<=[.!?])\s", joined)[0].strip() if joined else ""


def check(draft, state, brief, as_of):
    problems = []
    low = draft.lower()

    for entry in state.get("do_not_say", []):
        phrase = entry.get("phrase", "")
        if phrase and phrase.lower() in low:
            problems.append(f"do-not-say phrase {phrase!r}: {entry.get('reason', 'no reason recorded')}")

    opening = first_sentence(draft)
    if opening:
        for asset in state.get("assets", []):
            prev = (asset.get("opening") or "").strip()
            if prev and prev.lower() == opening.lower():
                problems.append(f"opening repeats the {asset.get('date', '?')} {asset.get('type', 'asset')}: "
                                "the customer reads everything you send")

    if re.search(r"\{\{[^}]*\}\}", draft):
        problems.append("unfilled merge token in draft")

    if brief:
        window = int(state.get("fact_freshness_days", 120))
        corrections = state.get("corrections", [])
        for f in brief.get("facts", []):
            d = parse_date(f.get("date"))
            if not d:
                problems.append(f"brief fact undated: {f.get('fact', '?')[:60]!r}")
            elif (as_of - d).days > window:
                problems.append(f"brief fact is {(as_of - d).days} days old (window {window}): "
                                f"{f.get('fact', '?')[:60]!r}: re-verify before reuse")
            for c in corrections:
                was = c.get("was", "")
                if was and was.lower() in f.get("fact", "").lower():
                    problems.append(f"brief fact matches superseded value {was!r}: "
                                    f"corrected {c.get('date', '?')} to {c.get('now', '?')!r}")
    return problems


def main():
    ap = argparse.ArgumentParser(description="Gate a per-customer draft against its state file.")
    ap.add_argument("draft")
    ap.add_argument("state")
    ap.add_argument("--brief")
    ap.add_argument("--as-of", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--log", action="store_true", help="append the draft to the state's asset log")
    ap.add_argument("--asset-type", default="asset", help="type recorded with --log")
    args = ap.parse_args()

    draft = open(args.draft, encoding="utf-8").read()
    state = json.load(open(args.state, encoding="utf-8"))
    as_of = parse_date(args.as_of) or datetime.date.today()

    if args.log:
        state.setdefault("assets", []).append({
            "date": str(as_of), "type": args.asset_type, "ref": args.draft,
            "opening": first_sentence(draft), "facts_used": [],
        })
        with open(args.state, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"logged {args.draft} to {args.state} ({len(state['assets'])} assets on record)")
        return

    brief = json.load(open(args.brief, encoding="utf-8")) if args.brief else None
    problems = check(draft, state, brief, as_of)
    label = f"{state.get('customer', '?')} <- {args.draft}"
    if problems:
        print(f"FAIL: {label}")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"PASS: {label}")
    print(f"  checks: do-not-say, opening repetition ({len(state.get('assets', []))} logged assets), "
          f"merge tokens{', fact freshness, corrections' if brief else ''}")


if __name__ == "__main__":
    main()
