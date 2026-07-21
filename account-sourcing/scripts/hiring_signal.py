#!/usr/bin/env python3
"""Live hiring-signal detector for the account-sourcing skill.

Checks public ATS job boards (Greenhouse, Lever, Ashby JSON endpoints, no keys) for
postings whose titles match ICP-relevant keywords. A matching posting is a dated,
sourced why-now signal in the exact shape the accounts.json schema expects.

Usage:
  python3 hiring_signal.py --company greenhouse:gitlab --keywords "gtm engineer,marketing"
  python3 hiring_signal.py --companies companies.json --keywords "head of ai" --json signals.json

companies.json: [{"name": "Cohere", "ats": "ashby", "slug": "cohere"}, ...]
--company takes ats:slug or ats:slug:Display Name, repeatable.

Endpoints (public, read-only, no auth):
  greenhouse  https://boards-api.greenhouse.io/v1/boards/{slug}/jobs
  lever       https://api.lever.co/v0/postings/{slug}?mode=json
  ashby       https://api.ashbyhq.com/posting-api/job-board/{slug}

Some companies disable their public Ashby board; failures are reported per company and
never stop the run.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

UA = {"User-Agent": "account-sourcing-skill/1.0 (public job-board check)"}
TIMEOUT = 15

ENDPOINTS = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}",
}


def fetch_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _date_from_ms(ms):
    try:
        return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).date().isoformat()
    except (TypeError, ValueError, OSError):
        return None


def normalize(ats, slug, data):
    """Yield {title, location, url, date} per posting, tolerating missing fields."""
    if ats == "greenhouse":
        for job in data.get("jobs", []):
            yield {
                "title": job.get("title", ""),
                "location": (job.get("location") or {}).get("name"),
                "url": job.get("absolute_url"),
                "date": (job.get("updated_at") or "")[:10] or None,
            }
    elif ats == "lever":
        for job in data if isinstance(data, list) else []:
            yield {
                "title": job.get("text", ""),
                "location": (job.get("categories") or {}).get("location"),
                "url": job.get("hostedUrl"),
                "date": _date_from_ms(job.get("createdAt")),
            }
    elif ats == "ashby":
        for job in data.get("jobs", []):
            date = job.get("publishedAt") or job.get("publishedDate") or ""
            yield {
                "title": job.get("title", ""),
                "location": job.get("location"),
                "url": job.get("jobUrl") or job.get("applyUrl"),
                "date": str(date)[:10] or None,
            }


def check_company(name, ats, slug, keywords):
    url = ENDPOINTS[ats].format(slug=slug)
    data = fetch_json(url)
    matches = []
    for post in normalize(ats, slug, data):
        title_low = post["title"].lower()
        if any(kw in title_low for kw in keywords):
            detail = post["title"] + (f" ({post['location']})" if post.get("location") else "")
            matches.append({
                "type": "hiring",
                "company": name,
                "detail": detail,
                "source": post.get("url") or url,
                "date": post.get("date"),
            })
    return matches


def parse_company_arg(value):
    parts = value.split(":", 2)
    if len(parts) < 2 or parts[0] not in ENDPOINTS:
        raise argparse.ArgumentTypeError(
            f"expected ats:slug (ats one of {', '.join(ENDPOINTS)}), got {value!r}")
    ats, slug = parts[0], parts[1]
    name = parts[2] if len(parts) == 3 else slug
    return {"name": name, "ats": ats, "slug": slug}


def main():
    ap = argparse.ArgumentParser(description="Check public ATS boards for ICP-relevant postings.")
    ap.add_argument("--company", action="append", type=parse_company_arg, default=[],
                    help="ats:slug or ats:slug:Display Name (repeatable)")
    ap.add_argument("--companies", help="JSON file: [{name, ats, slug}, ...]")
    ap.add_argument("--keywords", required=True,
                    help="comma-separated, case-insensitive title keywords")
    ap.add_argument("--json", dest="json_out", help="write matches as signal records here")
    args = ap.parse_args()

    companies = list(args.company)
    if args.companies:
        companies.extend(json.load(open(args.companies, encoding="utf-8")))
    if not companies:
        ap.error("no companies given; use --company or --companies")

    keywords = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]

    all_matches, failures = [], []
    for c in companies:
        try:
            found = check_company(c["name"], c["ats"], c["slug"], keywords)
            all_matches.extend(found)
            print(f"{c['name']}: {len(found)} matching posting(s)", file=sys.stderr)
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError,
                KeyError, TimeoutError, OSError) as exc:
            failures.append(c["name"])
            print(f"{c['name']}: board unreachable or disabled ({exc})", file=sys.stderr)

    if all_matches:
        print("| Company | Role | Date | Source |")
        print("|---------|------|------|--------|")
        for m in all_matches:
            print(f"| {m['company']} | {m['detail']} | {m['date'] or '?'} | {m['source']} |")
    else:
        print("no matching postings found", file=sys.stderr)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(all_matches, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {len(all_matches)} signal record(s) -> {args.json_out}", file=sys.stderr)

    if failures:
        print(f"unreachable boards: {', '.join(failures)}", file=sys.stderr)


if __name__ == "__main__":
    main()
