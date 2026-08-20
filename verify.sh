#!/usr/bin/env bash
# Reruns every deterministic pipeline in this repo and diffs the results against
# the checked-in outputs. If this passes, "same inputs, same output" is not a claim,
# it is a property. CI runs this on every push; run it locally with ./verify.sh
set -euo pipefail
cd "$(dirname "$0")"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
ok() { echo "ok: $1"; }

# 1. account-sourcing: scorer regenerates the scored account file exactly
python3 account-sourcing/scripts/score_accounts.py \
  account-sourcing/examples/cohere/accounts.json \
  account-sourcing/examples/cohere/rubric.yaml -o "$tmp/accounts.json" 2>/dev/null
diff -q "$tmp/accounts.json" account-sourcing/examples/cohere/accounts.json >/dev/null
ok "account-sourcing scorer regenerates accounts.json"

# 2. account-sourcing: briefing renderer regenerates the executive briefing exactly
python3 account-sourcing/scripts/render_briefing.py \
  account-sourcing/examples/cohere/accounts.json -o "$tmp/briefing.html" \
  --company "Cohere" --accent "#39594D" --prepared-by "Esme Fong (esmefong.com)" >/dev/null
diff -q "$tmp/briefing.html" account-sourcing/examples/cohere/briefing.html >/dev/null
ok "briefing renderer regenerates briefing.html"

# 3. outbound-engine: the gate passes the good sequence and refuses the bad one
(cd outbound-engine/examples/cohere && \
  python3 ../../scripts/sequence_gate.py telus-sequence.json \
    --as-of 2026-07-21 --avoid cohere-avoid.txt >/dev/null)
ok "outbound gate passes the TELUS sequence"
if (cd outbound-engine/examples/cohere && \
  python3 ../../scripts/sequence_gate.py cibc-draft-rejected.json \
    --as-of 2026-07-21 --avoid cohere-avoid.txt >/dev/null 2>&1); then
  echo "FAIL: the CIBC draft should be refused"; exit 1
fi
ok "outbound gate refuses the CIBC draft with reasons"

# 4. positioning-message-house: generated assets cannot drift from the house
python3 positioning-message-house/scripts/generate_assets.py \
  positioning-message-house/examples/cohere/house.json -o "$tmp" >/dev/null
diff -q "$tmp/battlecard.md" positioning-message-house/examples/cohere/battlecard.md >/dev/null
diff -q "$tmp/objection-handling.md" positioning-message-house/examples/cohere/objection-handling.md >/dev/null
ok "message-house battlecard and objection doc regenerate"

# 5. market-prioritization: ranking and sensitivity analysis regenerate
python3 market-prioritization/scripts/prioritize.py \
  market-prioritization/examples/cohere/markets.json --json "$tmp/sensitivity.json" >/dev/null 2>/dev/null
diff -q "$tmp/sensitivity.json" market-prioritization/examples/cohere/sensitivity.json >/dev/null
ok "market prioritization regenerates sensitivity.json"

# 6. content-quality-check: the linter flags the specimen and clears the revision
if python3 content-quality-check/scripts/check_content.py \
  content-quality-check/examples/cohere/draft-before.md \
  --avoid content-quality-check/examples/cohere/cohere-avoid.txt \
  --json "$tmp/before.json" >/dev/null 2>&1; then
  echo "FAIL: the specimen draft should be flagged"; exit 1
fi
diff -q "$tmp/before.json" content-quality-check/examples/cohere/before-findings.json >/dev/null
ok "content linter flags the specimen with the committed findings"
python3 content-quality-check/scripts/check_content.py \
  content-quality-check/examples/cohere/draft-after.md \
  --avoid content-quality-check/examples/cohere/cohere-avoid.txt >/dev/null
ok "content linter clears the revised draft"

# 7. the front door holds itself to the same standard
python3 content-quality-check/scripts/check_content.py README.md >/dev/null
ok "README clears the repo's own linter"

echo "verify: all checks passed"
