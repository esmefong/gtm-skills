#!/usr/bin/env python3
"""Deterministic send/no-send gate for the outbound-engine skill.

Reads a sequence.json (schema: references/output-template.md) and verifies it
mechanically: signal freshness, motion touch caps, per-channel word counts, one ask
per touch with a call ask up front, annotation coverage, universal slop phrases, the
brand voice's own Avoid words, and role-level targeting. Prints PASS or FAIL with
every reason. Exit code 0 on pass, 1 on fail.

Judgment (whether the signal truly maps to an ICP trigger) is reasoning work done in
the skill; this script enforces everything a machine can check, so a weak sequence
cannot ship by charm alone.

Usage:
  python3 sequence_gate.py telus-sequence.json --as-of 2026-07-21 \
      --avoid cohere-avoid.txt [--max-signal-age 90]

No dependencies beyond the standard library. No network.
"""

import argparse
import datetime
import json
import re
import sys

SLOP_PHRASES = [
    "i hope this finds you well",
    "quick question",
    "just following up",
    "just checking in",
    "touching base",
    "i hope you're doing well",
    "congrats on the",
    "i've been following your",
    "i have been following your",
]

WORD_LIMITS = {"email": 150, "linkedin": 70}
TOUCH_CAPS = {"enterprise-abm": 5, "velocity": 8}
EM_DASH = "\u2014"


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except (ValueError, TypeError):
            continue
    return None


def words(text):
    return len(re.findall(r"\S+", text or ""))


def check(seq, as_of, avoid_words, max_age):
    problems = []

    motion = seq.get("motion")
    if motion not in TOUCH_CAPS:
        problems.append(f"motion must be one of {sorted(TOUCH_CAPS)}, got {motion!r}")

    if not seq.get("target_role"):
        problems.append("target_role missing (role-level targeting is required)")

    sig = seq.get("signal") or {}
    if not sig.get("source"):
        problems.append("signal.source missing: an unsourced signal does not pass")
    sig_date = parse_date(sig.get("date"))
    if not sig_date:
        problems.append("signal.date missing or unparseable: an undated signal does not pass")
    else:
        age = (as_of - sig_date).days
        if age > max_age:
            problems.append(f"signal is {age} days old (max {max_age}): stale why-now, refuse or refresh")

    tm = seq.get("trigger_mapping", "")
    if not tm.strip():
        problems.append("trigger_mapping missing: write the signal-to-trigger logic out")
    elif tm.count(".") > 3:
        problems.append("trigger_mapping runs past two sentences: if it needs this much justifying, it is weak")

    touches = seq.get("touches", [])
    if not touches:
        problems.append("no touches")
    cap = TOUCH_CAPS.get(motion)
    if cap and len(touches) > cap:
        problems.append(f"{len(touches)} touches exceeds the {motion} cap of {cap}")

    call_asks = 0
    for t in touches:
        n = t.get("n", "?")
        body = t.get("body", "")
        channel = t.get("channel", "email")

        limit = WORD_LIMITS.get(channel, WORD_LIMITS["email"])
        wc = words(body)
        if wc > limit:
            problems.append(f"touch {n}: {wc} words exceeds the {channel} limit of {limit}")

        if not t.get("ask", "").strip():
            problems.append(f"touch {n}: no ask (one clear ask per touch)")
        if t.get("ask_type") == "call":
            call_asks += 1

        if not t.get("annotations"):
            problems.append(f"touch {n}: no provenance annotations")

        low = body.lower()
        for phrase in SLOP_PHRASES:
            if phrase in low:
                problems.append(f"touch {n}: slop phrase {phrase!r}")
        for w in avoid_words:
            if re.search(rf"\b{re.escape(w)}\b", low):
                problems.append(f"touch {n}: voice Avoid word {w!r}")
        if EM_DASH in body or EM_DASH in t.get("subject", ""):
            problems.append(f"touch {n}: em dash in copy")
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", body):
            problems.append(f"touch {n}: contains an email address; targeting stays role-level")
        if re.search(r"\{\{?\s*first[_ ]?name", low):
            problems.append(f"touch {n}: unfilled merge token")

    if touches and touches[0].get("ask_type") != "call" and motion == "enterprise-abm":
        problems.append("touch 1 ask_type must be 'call' in the enterprise-abm motion")
    if touches and call_asks == 0:
        problems.append("sequence contains no call ask")

    return problems


def main():
    ap = argparse.ArgumentParser(description="Mechanically gate an outbound sequence.")
    ap.add_argument("sequence")
    ap.add_argument("--as-of", help="send date YYYY-MM-DD (default: today)")
    ap.add_argument("--avoid", help="file of banned voice words, one per line")
    ap.add_argument("--max-signal-age", type=int, default=90)
    args = ap.parse_args()

    seq = json.load(open(args.sequence, encoding="utf-8"))
    as_of = parse_date(args.as_of) or datetime.date.today()
    avoid = []
    if args.avoid:
        avoid = [w.strip().lower() for w in open(args.avoid, encoding="utf-8")
                 if w.strip() and not w.startswith("#")]

    problems = check(seq, as_of, avoid, args.max_signal_age)
    label = f"{seq.get('brand', '?')} -> {seq.get('account', '?')} ({seq.get('motion', '?')})"
    if problems:
        print(f"FAIL: {label}")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"PASS: {label}")
    print(f"  signal dated {seq['signal']['date']}, {len(seq.get('touches', []))} touches, "
          f"checks: freshness, caps, word counts, asks, annotations, slop, voice, role-level")
    sys.exit(0)


if __name__ == "__main__":
    main()
