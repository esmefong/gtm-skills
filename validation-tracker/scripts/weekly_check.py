#!/usr/bin/env python3
"""Weekly operating-rhythm check for the validation-tracker skill.

Reads metrics.json (bands plus weekly actuals) and decisions.json (the append-only
decision log), then reports: each metric against its floor and target, the log's
integrity (unique ids, non-decreasing dates, supersession links that resolve), the
coverage rule (every below-floor week needs a decision dated inside the window), and
revisits due. Exit 0 when integrity and coverage hold, 1 otherwise.

Usage:
  python3 weekly_check.py metrics.json decisions.json [--as-of YYYY-MM-DD]

No dependencies beyond the standard library. No network.
"""

import argparse
import datetime
import json
import sys


def parse_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def check_log(decisions):
    problems, seen = [], {}
    prev_date = None
    for d in decisions:
        did, date = d.get("id"), parse_date(d.get("date"))
        if not did or did in seen:
            problems.append(f"decision id {did!r} missing or duplicated")
        if not date:
            problems.append(f"decision {did}: unparseable date {d.get('date')!r}")
        elif prev_date and date < prev_date:
            problems.append(f"decision {did}: date {date} precedes the prior entry (log is append-only)")
        sup = d.get("supersedes")
        if sup and sup not in seen:
            problems.append(f"decision {did}: supersedes {sup!r}, which does not appear earlier in the log")
        if did:
            seen[did] = d
        prev_date = date or prev_date
    superseded = {d.get("supersedes") for d in decisions if d.get("supersedes")}
    return problems, seen, superseded


def main():
    ap = argparse.ArgumentParser(description="Check weekly metrics against bands and validate the decision log.")
    ap.add_argument("metrics")
    ap.add_argument("decisions")
    ap.add_argument("--as-of", help="YYYY-MM-DD (default: metrics.json as_of, else today)")
    args = ap.parse_args()

    m = json.load(open(args.metrics, encoding="utf-8"))
    dlog = json.load(open(args.decisions, encoding="utf-8")).get("decisions", [])
    as_of = parse_date(args.as_of) or parse_date(m.get("as_of")) or datetime.date.today()
    window = int(m.get("miss_decision_window_days", 21))

    problems, seen, superseded = check_log(dlog)
    decision_dates = [parse_date(d.get("date")) for d in dlog if parse_date(d.get("date"))]

    print(f"{m.get('name', '?')}: week of {as_of}, {len(dlog)} decisions on record "
          f"({len(superseded)} superseded)\n")
    print("| Metric | Latest | Floor | Target | Status | Below-floor weeks |")
    print("|---|---|---|---|---|---|")

    miss_weeks = set()
    for metric in m.get("metrics", []):
        weekly = [w for w in metric.get("weekly", []) if w.get("value") is not None]
        floor, target = metric.get("floor"), metric.get("target")
        misses = [w["week_ending"] for w in weekly if floor is not None and w["value"] < floor]
        miss_weeks.update(misses)
        latest = weekly[-1] if weekly else None
        if latest is None:
            status = "no data"
        elif floor is not None and latest["value"] < floor:
            status = "BELOW FLOOR"
        elif target is not None and latest["value"] >= target:
            status = "at/above target"
        else:
            status = "in band"
        print(f"| {metric.get('id')} | {latest['value'] if latest else '-'} "
              f"| {floor} | {target} | {status} | {len(misses)} |")

    uncovered = []
    for week in sorted(miss_weeks):
        wend = parse_date(week)
        if not wend:
            continue
        covered = any(wend < d <= wend + datetime.timedelta(days=window) for d in decision_dates)
        if not covered:
            uncovered.append(week)
    for week in uncovered:
        problems.append(f"undocumented miss: week ending {week} went below floor with no "
                        f"decision logged within {window} days")

    due = [d for d in dlog if parse_date(d.get("revisit") or "") and parse_date(d["revisit"]) <= as_of
           and d.get("id") not in superseded]
    if due:
        print("\nrevisits due:")
        for d in due:
            print(f"  - {d['id']} ({d['revisit']}): {d.get('decision', '')}")

    if problems:
        print(f"\nFAIL: {len(problems)} problem(s)")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    if miss_weeks:
        print(f"\nPASS: log integrity holds; {len(miss_weeks)} below-floor week(s), all covered "
              "by logged decisions")
    else:
        print("\nPASS: log integrity holds; no below-floor weeks")


if __name__ == "__main__":
    main()
