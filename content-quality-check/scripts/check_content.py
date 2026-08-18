#!/usr/bin/env python3
"""Deterministic content linter for the content-quality-check skill.

Scans a draft for the mechanical tells in references/detection-checklist.md section A:
slop phrases, LLM-overrepresented words, "not just X, it's Y" reframes, generated-answer
openers, announcement cliches, em-dash chaining, rhetorical-question openers, empty-
intensifier density, weak closers, and (with --avoid) the brand's own banned words.

Reports findings by severity with line numbers. Verdict: REVISE if any HIGH finding,
PASS WITH FLAGS if only MEDIUM/LOW, PASS if clean. Exit 1 on REVISE, else 0.

Judgment checks (openers that throat-clear, closers that restate, claims without proof,
template shape, voice conformance) are the skill's editorial pass, not this script's.

Usage:
  python3 check_content.py draft.md [--avoid brand-avoid.txt] [--json out.json]

No dependencies beyond the standard library. No network.
"""

import argparse
import json
import re
import sys

EM = "\u2014"

REFRAME = [re.compile(r"(?:\bnot|n'?t)\s+(?:just|only|merely)\b[^.!?]{0,80}?\b(?:it'?s|it\s+is|but)\b", re.I),
           re.compile(r"\bmore\s+than\s+just\b", re.I)]
OPENER_TELLS = re.compile(r"\blet'?s\s+(?:dive|explore|unpack|delve|jump|break|take\s+a)\b|"
                          r"\blet\s+me\s+(?:break|explain|walk|show)\b", re.I)
ANNOUNCE = re.compile(r"\b(?:thrilled|excited|proud|delighted)\s+to\s+(?:announce|share|introduce)\b", re.I)
TRICOLON = re.compile(r"\b\w+er?\b,\s+\b\w+er?\b,\s+and\s+\b\w+er?\b|\b\w+\b,\s+\b\w+\b,\s+and\s+\b\w+\b")
INTENSIFIERS = ["truly", "genuinely", "absolutely", "incredibly", "really"]

STAGE_SETTING = ["in today's fast-paced world", "in today's rapidly evolving",
                 "in the ever-evolving landscape", "in the realm of", "in the world of",
                 "navigating the complexities of", "it's important to note", "it's worth noting",
                 "at the end of the day", "when it comes to", "in an era of"]
LLM_WORDS = ["delve", "delving", "leverage", "seamless", "seamlessly", "robust", "unlock",
             "unleash", "empower", "elevate", "harness", "transformative", "revolutionize",
             "game-changer", "game-changing", "cutting-edge", "testament", "tapestry", "beacon",
             "pivotal", "supercharge"]
WEAK_CLOSERS = ["in conclusion", "in summary", "to sum up", "ultimately, ", "is here"]


def body_lines(text):
    """(line_no, line) for non-empty, non-heading lines."""
    return [(i, ln) for i, ln in enumerate(text.splitlines(), 1)
            if ln.strip() and not ln.lstrip().startswith("#")]


def check(text, avoid_words):
    findings = []
    lines = text.splitlines()
    body = body_lines(text)
    words_total = len(re.findall(r"\S+", text)) or 1

    def add(sev, line, code, msg):
        findings.append({"severity": sev, "line": line, "code": code, "msg": msg})

    flat = text.replace("\n", " ")
    for rx in REFRAME:
        for m in rx.finditer(flat):
            line = text.count("\n", 0, m.start()) + 1
            add("HIGH", line, "reframe", "the 'not just X, it's Y' construction: make one specific claim instead")

    for i, ln in enumerate(lines, 1):
        low = ln.lower()
        if OPENER_TELLS.search(ln):
            add("HIGH", i, "generated-opener", "'let's dive in' family: telegraphs a generated answer")
        if ANNOUNCE.search(ln):
            add("HIGH", i, "announcement-cliche", "'thrilled to announce' family: the most template opener there is")
        for w in avoid_words:
            if re.search(rf"\b{re.escape(w)}\b", low):
                add("HIGH", i, "brand-avoid", f"brand Avoid-list word {w!r}")
        for p in STAGE_SETTING:
            if p in low:
                add("MEDIUM", i, "stage-setting", f"hollow hedge {p!r}: cut, or replace with the point")
        for w in LLM_WORDS:
            if re.search(rf"\b{re.escape(w)}\b", low):
                add("MEDIUM", i, "llm-word", f"over-represented word {w!r}")

    if body:
        first = body[0][1].strip()
        first_sentence = re.split(r"(?<=[.!?])\s", first)[0]
        if first_sentence.endswith("?"):
            add("HIGH", body[0][0], "rhetorical-opener", "opener asks the reader a question: open with a claim instead")

    para, start = [], 1
    for i, ln in enumerate(lines + [""], 1):
        if ln.strip():
            if not para:
                start = i
            para.append(ln)
        elif para:
            dashes = sum(p.count(EM) for p in para)
            if dashes >= 3:
                add("HIGH", start, "emdash-chain", f"{dashes} em dashes in one paragraph: restructure with periods")
            para = []

    hits = sum(len(re.findall(rf"\b{w}\b", text, re.I)) for w in INTENSIFIERS)
    if hits / words_total > 1 / 200:
        add("MEDIUM", 0, "intensifier-density", f"{hits} empty intensifiers in {words_total} words (cap: 1 per 200)")

    tail = " ".join(ln for _, ln in body[-4:]).lower() if body else ""
    for p in WEAK_CLOSERS:
        if p in tail:
            add("MEDIUM", body[-1][0], "weak-closer", f"closer formula {p!r}: end forward, not with a recap")
    if body and body[-1][1].rstrip().endswith("!"):
        add("LOW", body[-1][0], "hype-close", "exclamation in the final line: the flat close lands harder")

    tri = TRICOLON.findall(text)
    if len(tri) >= 2:
        add("LOW", 0, "tricolon", f"{len(tri)} comma triads: verify each is a real list, not rhythm filler")
    q = len(re.findall(r"\?\s", text))
    if q >= 3:
        add("LOW", 0, "question-scaffold", f"{q} questions in the piece: outline showing through the prose")

    return findings


def main():
    ap = argparse.ArgumentParser(description="Lint a draft for AI tells and template language.")
    ap.add_argument("draft")
    ap.add_argument("--avoid", help="brand Avoid words, one per line (from its writing-standard)")
    ap.add_argument("--json", dest="json_out")
    args = ap.parse_args()

    text = open(args.draft, encoding="utf-8").read()
    avoid = []
    if args.avoid:
        avoid = [w.strip().lower() for w in open(args.avoid, encoding="utf-8")
                 if w.strip() and not w.startswith("#")]

    findings = check(text, avoid)
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    findings.sort(key=lambda f: (order[f["severity"]], f["line"]))
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in order}

    if counts["HIGH"]:
        verdict = "REVISE"
    elif counts["MEDIUM"] or counts["LOW"]:
        verdict = "PASS WITH FLAGS"
    else:
        verdict = "PASS"

    print(f"{verdict}: {args.draft} ({counts['HIGH']} high, {counts['MEDIUM']} medium, {counts['LOW']} low)")
    for f in findings:
        loc = f"line {f['line']}" if f["line"] else "whole piece"
        print(f"  [{f['severity']}] {loc}: {f['msg']}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"verdict": verdict, "counts": counts, "findings": findings}, fh, indent=2)
            fh.write("\n")

    sys.exit(1 if verdict == "REVISE" else 0)


if __name__ == "__main__":
    main()
