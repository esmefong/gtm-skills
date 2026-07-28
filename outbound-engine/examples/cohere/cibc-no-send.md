# No-send verdict: Cohere to CIBC

**Verdict: do not send.** CIBC is the strongest-looking bank on the sourced list (tier 2, score 55,
A-tier evidence, Sales lane), and the engine still refuses it, which is the point.

The gate output, verbatim, on a deliberately drafted test touch (`cibc-draft-rejected.json`):

```
FAIL: Cohere -> CIBC (enterprise-abm)
  - signal is 420 days old (max 90): stale why-now, refuse or refresh
  - touch 1: slop phrase 'congrats on the'
  - touch 1: voice Avoid word 'revolutionary'
```

## Why it fails

- **The signal is 14 months stale.** The CAI enterprise-wide launch (2025-05-27) is excellent
  account evidence and a terrible opener. "Why now" cannot be last year's news; a recipient reads a
  14-month-old congratulation as exactly what it is, a list-generated email.
- **The test draft also demonstrates the copy checks.** "Congrats on the" is the signature slop
  opener of AI outbound, and "revolutionary" is on Cohere's own Avoid list from the voice guide.
  Both are caught mechanically, which means they are caught every time, not only when a reviewer is
  paying attention.

## Why this account still matters

Nothing about the refusal demotes CIBC: the platform-buyer logic (an enterprise-wide in-house AI
platform needs private model supply) is the strongest trigger mapping on the bank list. The account
stays tier 2 in the Sales lane. The problem is timing, not fit.

## What would change the verdict

A fresh dated signal that reopens the window: a CAI expansion or vendor announcement, an AI
leadership hire, a data-residency statement, or a procurement signal. Any one of these inside the
90-day window flips the verdict to send, with the platform logic as the middle of the message
instead of the opener.

## Next step

Put CIBC on the signal watch: the biweekly refresh from `account-sourcing` (press sweep plus the
hiring-signal check) is the mechanism. The sequence drafts itself the week the signal lands.
