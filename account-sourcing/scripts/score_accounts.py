#!/usr/bin/env python3
"""Deterministic account scorer for the account-sourcing skill.

Reads accounts.json and rubric.yaml (formats defined in references/output-template.md),
applies weights, hard disqualifiers, and tier thresholds, and writes the results back:
score, tier, status, and disqualifiers_hit per account. Same inputs, same output, every run.

The division of labor is deliberate: judgment (does this account meet a criterion, on what
evidence) is authored into the accounts file by a human or an agent. This script only
aggregates: points are granted when an account's evidence array contains a Tier A or B
entry whose field matches a criterion id.

Usage:
  python3 score_accounts.py accounts.json rubric.yaml [-o scored.json] [--table]

No dependencies beyond the standard library. rubric may be .yaml (restricted subset,
or full YAML when PyYAML happens to be installed) or .json.
"""

import argparse
import json
import sys

LOAD_BEARING_TIERS = {"A", "B"}


# ---------- rubric loading ----------

def _scalar(s):
    s = s.strip()
    if len(s) >= 2 and s[0] in "\"'" and s.endswith(s[0]):
        return s[1:-1]
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "~", ""):
        return None
    for cast in (int, float):
        try:
            return cast(s)
        except ValueError:
            pass
    return s


def _parse_block(lns, i, _min_indent):
    ind = lns[i][0]
    if lns[i][1].startswith("- "):
        out = []
        while i < len(lns) and lns[i][0] == ind and lns[i][1].startswith("- "):
            body = lns[i][1][2:].strip()
            if ":" in body:
                key, _, val = body.partition(":")
                item = {}
                i += 1
                if val.strip():
                    item[key.strip()] = _scalar(val)
                elif i < len(lns) and lns[i][0] > ind:
                    child, i = _parse_block(lns, i, ind + 1)
                    item[key.strip()] = child
                if i < len(lns) and lns[i][0] > ind and not lns[i][1].startswith("- "):
                    rest, i = _parse_block(lns, i, ind + 1)
                    item.update(rest)
                out.append(item)
            else:
                out.append(_scalar(body))
                i += 1
        return out, i
    out = {}
    while i < len(lns) and lns[i][0] == ind and not lns[i][1].startswith("- "):
        key, _, val = lns[i][1].partition(":")
        key = key.strip()
        if val.strip():
            out[key] = _scalar(val)
            i += 1
        else:
            i += 1
            if i < len(lns) and lns[i][0] > ind:
                child, i = _parse_block(lns, i, ind + 1)
                out[key] = child
            else:
                out[key] = None
    return out, i


def load_rubric(path):
    text = open(path, encoding="utf-8").read()
    if path.endswith(".json"):
        return json.loads(text)
    try:  # full YAML when available; never required
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except ImportError:
        pass
    lns = []
    for raw in text.splitlines():
        if raw.lstrip().startswith("#") or not raw.strip():
            continue
        lns.append((len(raw) - len(raw.lstrip(" ")), raw.strip()))
    obj, i = _parse_block(lns, 0, 0)
    if i != len(lns):
        raise ValueError(f"rubric parse stopped at line entry {i}; check indentation")
    return obj


# ---------- scoring ----------

def evidenced_ids(account):
    ids = set()
    for ev in account.get("evidence", []):
        if ev.get("evidence_tier") in LOAD_BEARING_TIERS and ev.get("field"):
            ids.add(ev["field"])
    return ids


def score_account(account, rubric):
    ids = evidenced_ids(account)

    hits = []
    for disq in rubric.get("disqualifiers", []):
        did = disq.get("id")
        if did in ids or (did == "existing_customer" and account.get("suppressed")):
            hits.append(did)
    if hits:
        account.update(status="disqualified", score=0, tier=None,
                       scores={}, disqualifiers_hit=hits)
        return account

    weights = rubric.get("weights", {})
    per_category = {}
    for category, criteria in rubric.get("criteria", {}).items():
        earned = sum(c.get("points", 0) for c in criteria if c.get("id") in ids)
        per_category[category] = min(earned, weights.get(category, earned))
    total = sum(per_category.values())

    tiers = rubric.get("tiers", {})
    verify_below = rubric.get("verify_below", 0)
    if total < verify_below:
        status, tier = "verify", None
    else:
        status = "qualified"
        if total >= tiers.get("tier1", 101):
            tier = 1
        elif total >= tiers.get("tier2", 101):
            tier = 2
        else:
            tier = 3

    account.update(status=status, score=total, tier=tier,
                   scores=per_category, disqualifiers_hit=[])
    return account


def rank_key(account):
    return (-account.get("score", 0), account.get("name", "").lower())


def render_table(accounts):
    order = {"qualified": 0, "verify": 1, "disqualified": 2}
    rows = sorted(accounts, key=lambda a: (order.get(a["status"], 3), rank_key(a)))
    lines = [
        "| # | Account | Score | Tier | Status | Disqualifiers | Suppressed |",
        "|---|---------|-------|------|--------|---------------|------------|",
    ]
    for n, a in enumerate(rows, 1):
        lines.append(
            f"| {n} | {a.get('name', '?')} | {a.get('score', 0)} | {a.get('tier') or '-'} "
            f"| {a['status']} | {', '.join(a.get('disqualifiers_hit', [])) or '-'} "
            f"| {'yes' if a.get('suppressed') else 'no'} |"
        )
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Score accounts against an ICP rubric, deterministically.")
    ap.add_argument("accounts", help="accounts.json (schema: references/output-template.md)")
    ap.add_argument("rubric", help="rubric.yaml or rubric.json")
    ap.add_argument("-o", "--out", help="write updated accounts JSON here (default: overwrite input)")
    ap.add_argument("--table", action="store_true", help="print the ranked markdown table")
    args = ap.parse_args()

    doc = json.load(open(args.accounts, encoding="utf-8"))
    rubric = load_rubric(args.rubric)

    accounts = doc.get("accounts", [])
    for account in accounts:
        score_account(account, rubric)
    accounts.sort(key=rank_key)

    out_path = args.out or args.accounts
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    counts = {}
    for a in accounts:
        counts[a["status"]] = counts.get(a["status"], 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    print(f"scored {len(accounts)} accounts: {summary} -> {out_path}", file=sys.stderr)
    if args.table:
        print(render_table(accounts))


if __name__ == "__main__":
    main()
