#!/usr/bin/env python3
"""Deterministic audience segmenter for the reengagement-segmenter skill.

Reads audience.json (schema: references/output-template.md), applies the exclusion
gates, assigns each surviving record a blocker segment by taxonomy precedence over its
evidence tags, and flags conflicts where the CRM's stated reason disagrees with the
evidence. Writes segment, lane, and flags back per record and prints the map.

Judgment (resolving conflicts, deciding what changed on your side, drafting) is the
skill's reasoning work; this script does the bookkeeping so it is repeatable.

Usage:
  python3 segment_audience.py audience.json [-o segmented.json] [--table]

No dependencies beyond the standard library. No network.
"""

import argparse
import datetime
import json
import sys

# taxonomy precedence: first match with evidence wins
BLOCKER_PRECEDENCE = [
    ("trust_damage", "trust"),
    ("stalled_gate", "stalled-gate"),
    ("lost_to_incumbent", "lost-to-incumbent"),
    ("price_objection", "price"),
    ("timing_deferral", "timing"),
    ("never_activated", "never-activated"),
]

STATED_MAP = {
    "price": "price", "cost": "price", "budget": "timing", "timing": "timing",
    "paused": "timing", "security": "stalled-gate", "compliance": "stalled-gate",
    "legal": "stalled-gate", "procurement": "stalled-gate",
    "competitor": "lost-to-incumbent", "incumbent": "lost-to-incumbent",
    "no activation": "never-activated", "support": "trust",
}

TOO_WARM_DAYS = 90


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except (ValueError, TypeError):
            continue
    return None


def stated_blocker(reason):
    low = (reason or "").lower()
    for key, seg in STATED_MAP.items():
        if key in low:
            return seg
    return None


def segment_record(rec, as_of, horizon_days):
    flags = []

    # exclusions, in order
    if rec.get("unsubscribed"):
        return "leave-alone", "opted out: permanent exit from this motion", flags
    if rec.get("complaint"):
        return "leave-alone", "complaint history: human-sponsored motion or nothing", flags
    until = parse_date(rec.get("competitor_contract_until"))
    if until and until > as_of:
        return "leave-alone", f"active competitor contract until {until}", flags
    if rec.get("icp_disqualifiers"):
        return "leave-alone", f"ICP disqualifier: {', '.join(rec['icp_disqualifiers'])}", flags

    last = parse_date(rec.get("last_meaningful_activity"))
    if not last:
        flags.append("no last-activity date")
        return "drifted", "reengage", flags
    age = (as_of - last).days
    if age > horizon_days:
        return "archive", f"beyond dormancy horizon ({age} days)", flags
    if age < TOO_WARM_DAYS:
        return "active", f"active {age} days ago: not lapsed", flags

    # blocker from evidence, by precedence
    tags = {ev.get("field") for ev in rec.get("evidence", [])}
    evidenced = next((seg for tag, seg in BLOCKER_PRECEDENCE if tag in tags), None)
    stated = stated_blocker(rec.get("stated_reason"))

    if evidenced and stated and stated != evidenced:
        flags.append(f"stated reason maps to '{stated}', evidence to '{evidenced}': resolve by judgment")
        return "conflict", "reengage-after-resolution", flags
    if evidenced:
        return evidenced, "reengage", flags
    if stated:
        flags.append("stated reason only, no supporting evidence")
        return stated, "reengage", flags
    return "drifted", "reengage", flags


def main():
    ap = argparse.ArgumentParser(description="Segment a lapsed audience by blocker, deterministically.")
    ap.add_argument("audience", help="audience.json (schema: references/output-template.md)")
    ap.add_argument("-o", "--output", help="write segmented JSON here (default: in place)")
    ap.add_argument("--table", action="store_true", help="print the segment map as a markdown table")
    args = ap.parse_args()

    doc = json.load(open(args.audience, encoding="utf-8"))
    as_of = parse_date(doc.get("as_of")) or datetime.date.today()
    horizon_days = int(doc.get("dormancy_horizon_months", 24) * 30.44)

    counts, conflicts = {}, []
    for rec in doc.get("records", []):
        segment, lane, flags = segment_record(rec, as_of, horizon_days)
        rec["segment"], rec["lane"], rec["flags"] = segment, lane, flags
        counts[segment] = counts.get(segment, 0) + 1
        if segment == "conflict":
            conflicts.append(rec)

    out = args.output or args.audience
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    total = len(doc.get("records", []))
    reengage = sum(1 for r in doc.get("records", []) if r["lane"] == "reengage")
    print(f"segmented {total} records: {reengage} to reengage, "
          f"{counts.get('conflict', 0)} conflicts to resolve, "
          f"{total - reengage - counts.get('conflict', 0)} held back -> {out}")
    for seg in sorted(counts, key=lambda s: -counts[s]):
        print(f"  {seg}: {counts[seg]}")
    if conflicts:
        print("conflicts (resolve by judgment, log the call):")
        for rec in conflicts:
            print(f"  - {rec.get('account', '?')}: {'; '.join(rec['flags'])}")

    if args.table:
        print("\n| Account | Segment | Lane | Flags |")
        print("|---|---|---|---|")
        for rec in doc.get("records", []):
            print(f"| {rec.get('account', '?')} | {rec['segment']} | {rec['lane']} "
                  f"| {'; '.join(rec['flags']) or '-'} |")


if __name__ == "__main__":
    main()
