#!/usr/bin/env python3
"""Executive briefing renderer for the account-sourcing skill.

Reads accounts.json and emits a self-contained HTML briefing: accounts grouped into
lanes by owning team, each card leading with the next action, rejects at the bottom
with reasons. The data layer (json) and working doc (md) stay canonical; this is the
human layer for the first five minutes of an executive's attention.

Brand-flavored, never brand-cloned: an accent color is the only theming, and the
"prepared by / not affiliated" line is always rendered.

Usage:
  python3 render_briefing.py accounts.json -o briefing.html \
      --company "Cohere" --accent "#39594D" --prepared-by "Esme Fong"

No dependencies beyond the standard library. No network.
"""

import argparse
import html
import json

TIER_STYLE = {
    1: ("Tier 1", "#ffffff", "var(--accent)"),
    2: ("Tier 2", "#4a4127", "#f4e9c8"),
    3: ("Tier 3", "#444444", "#e4e4e4"),
}

CSS = """
:root { --accent: ACCENT; }
* { box-sizing: border-box; margin: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
       Arial, sans-serif; color: #1c1c1c; background: #faf9f6; line-height: 1.45; }
.wrap { max-width: 980px; margin: 0 auto; padding: 40px 24px 64px; }
header { border-bottom: 3px solid var(--accent); padding-bottom: 20px; margin-bottom: 8px; }
h1 { font-size: 26px; font-weight: 700; }
.sub { color: #555; margin-top: 6px; font-size: 14px; }
.disclaimer { display: inline-block; margin-top: 10px; padding: 4px 10px; font-size: 12px;
  background: #fff3e6; border: 1px solid #e8c9a0; border-radius: 4px; color: #6b4a1b; }
.stats { display: flex; gap: 28px; margin: 22px 0 6px; flex-wrap: wrap; }
.stat b { font-size: 22px; display: block; color: var(--accent); }
.stat span { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: .05em; }
h2 { font-size: 15px; text-transform: uppercase; letter-spacing: .08em; color: #333;
     margin: 34px 0 4px; }
.lane-note { font-size: 13px; color: #666; margin-bottom: 12px; }
.card { background: #fff; border: 1px solid #e3e0d8; border-radius: 8px; padding: 16px 18px;
        margin-bottom: 12px; }
.row1 { display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; }
.name { font-size: 17px; font-weight: 700; }
.pill { font-size: 11px; font-weight: 700; padding: 2px 9px; border-radius: 99px; }
.score { font-size: 12px; color: #777; }
.why { font-size: 13.5px; color: #333; margin-top: 8px; }
.why b, .now b { color: #555; font-size: 11px; text-transform: uppercase; letter-spacing: .06em;
  margin-right: 6px; }
.now { font-size: 13.5px; color: #333; margin-top: 4px; }
.next { margin-top: 10px; padding: 9px 12px; background: #f5f8f6; border-left: 3px solid
        var(--accent); font-size: 14px; border-radius: 0 6px 6px 0; }
.next b { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--accent); }
table { width: 100%; border-collapse: collapse; margin-top: 10px; background: #fff;
        border: 1px solid #e3e0d8; border-radius: 8px; overflow: hidden; font-size: 13.5px; }
th { text-align: left; padding: 9px 12px; background: #f1efe9; font-size: 11px;
     text-transform: uppercase; letter-spacing: .06em; color: #555; }
td { padding: 9px 12px; border-top: 1px solid #eeece5; vertical-align: top; }
footer { margin-top: 40px; font-size: 12px; color: #777; border-top: 1px solid #e3e0d8;
         padding-top: 14px; }
"""


def esc(s):
    return html.escape(str(s or ""))


def pick_why(account):
    # Within the same evidence tier, richer detail beats boilerplate firmographics.
    evs = sorted(account.get("evidence", []),
                 key=lambda e: ({"A": 0, "B": 1}.get(e.get("evidence_tier"), 2),
                                -len(e.get("value", ""))))
    return "; ".join(e.get("value", "") for e in evs[:2])


def pick_now(account):
    sigs = account.get("signals", [])
    if not sigs:
        return None
    s = sigs[0]
    date = f" ({s['date']})" if s.get("date") else ""
    return f"{s.get('detail', '')}{date}"


def card(account):
    label, fg, bg = TIER_STYLE.get(account.get("tier"), ("Unranked", "#444", "#e4e4e4"))
    parts = [
        '<div class="card">',
        '<div class="row1">',
        f'<span class="name">{esc(account["name"])}</span>',
        f'<span class="pill" style="color:{fg};background:{bg}">{label}</span>',
        f'<span class="score">score {account.get("score", 0)}</span>',
        "</div>",
        f'<div class="why"><b>Why</b>{esc(pick_why(account))}</div>',
    ]
    now = pick_now(account)
    if now:
        parts.append(f'<div class="now"><b>Why now</b>{esc(now)}</div>')
    if account.get("next_action"):
        parts.append(f'<div class="next"><b>Next</b><br>{esc(account["next_action"])}</div>')
    parts.append("</div>")
    return "\n".join(parts)


def reject_reason(account):
    hits = ", ".join(account.get("disqualifiers_hit", []))
    ev = account.get("evidence", [])
    detail = ev[0].get("value", "") if ev else ""
    return f"{hits}: {detail}" if detail else hits


def render(doc, company, accent, prepared_by):
    accounts = doc.get("accounts", [])
    qualified = [a for a in accounts if a.get("status") == "qualified"]
    rejected = [a for a in accounts if a.get("status") == "disqualified"]

    lanes = {}
    for a in qualified:
        lanes.setdefault(a.get("owner_team") or "Unassigned", []).append(a)
    ordered = sorted(lanes.items(), key=lambda kv: -max(x.get("score", 0) for x in kv[1]))

    tier1 = sum(1 for a in qualified if a.get("tier") == 1)
    out = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>Target account briefing: {esc(company)}</title>",
        f"<style>{CSS.replace('ACCENT', accent)}</style></head><body><div class='wrap'>",
        "<header>",
        f"<h1>Target account briefing: {esc(company)}</h1>",
        f"<div class='sub'>Generated {esc(doc.get('generated', ''))} by the account-sourcing "
        f"skill, from public evidence. Every claim is sourced and dated in accounts.json.</div>",
        f"<div class='disclaimer'>Prepared by {esc(prepared_by)}. Independent work product, "
        f"not affiliated with or endorsed by {esc(company)}.</div>",
        "</header>",
        "<div class='stats'>",
        f"<div class='stat'><b>{len(qualified)}</b><span>qualified</span></div>",
        f"<div class='stat'><b>{tier1}</b><span>tier 1</span></div>",
        f"<div class='stat'><b>{len(rejected)}</b><span>ruled out</span></div>",
        "</div>",
    ]

    for team, members in ordered:
        members.sort(key=lambda a: (-a.get("score", 0), a.get("name", "")))
        out.append(f"<h2>{esc(team)}</h2>")
        out.append(f"<div class='lane-note'>{len(members)} account(s) routed to this lane</div>")
        out.extend(card(a) for a in members)

    if rejected:
        out.append("<h2>Ruled out, with reasons</h2>")
        out.append("<div class='lane-note'>Deliberate exclusions; each saves a wasted "
                   "sequence or an awkward call.</div>")
        out.append("<table><tr><th>Account</th><th>Owner</th><th>Reason</th></tr>")
        for a in sorted(rejected, key=lambda x: x.get("name", "")):
            out.append(f"<tr><td><b>{esc(a['name'])}</b></td>"
                       f"<td>{esc(a.get('owner_team') or '')}</td>"
                       f"<td>{esc(reject_reason(a))}</td></tr>")
        out.append("</table>")

    out.append("<footer>Data layer: accounts.json (evidence, sources, dates, scoring). "
               "Working doc: account-list.md (method, self-audit, gaps, refresh cadence). "
               "This page is generated; edit the data, not the page.</footer>")
    out.append("</div></body></html>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Render an executive briefing from accounts.json.")
    ap.add_argument("accounts")
    ap.add_argument("-o", "--out", default="briefing.html")
    ap.add_argument("--company", required=True)
    ap.add_argument("--accent", default="#2f5d50", help="accent color, brand-flavored")
    ap.add_argument("--prepared-by", default="the account-sourcing skill")
    args = ap.parse_args()

    doc = json.load(open(args.accounts, encoding="utf-8"))
    page = render(doc, args.company, args.accent, args.prepared_by)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
