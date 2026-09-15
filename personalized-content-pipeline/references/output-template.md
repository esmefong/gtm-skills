# Output template

Three artifacts per customer: the brief (input), the state file (the durable memory), and the
asset (output). The state file is the one that matters most; assets are disposable, state is not.

## `brief.json` (per asset)

```json
{
  "customer": "TELUS",
  "asset_type": "abm-onepager",
  "goal": "Second-touch leave-behind for the platform-partner conversation",
  "audience": "VP AI infrastructure / enterprise AI product (role-level)",
  "voice_dir": "brand-voice-guide/examples/cohere/brand-voice/",
  "facts": [
    {
      "fact": "Sovereign AI Factory expansion: Kamloops plus two Vancouver sites",
      "source": "https://www.rcrwireless.com/20260512/carriers/telus-ai-data-centers",
      "date": "2026-05-12"
    }
  ],
  "must_cover": ["what changed in June", "the private-deployment guarantee"],
  "constraints": ["one page", "no pricing"]
}
```

Facts carry sources and dates or they are not facts. `must_cover` is content, not copy; the voice
directory decides how anything sounds.

## `state.json` (per customer, opens and closes every run)

```json
{
  "customer": "TELUS",
  "created": "2026-07-21",
  "fact_freshness_days": 120,
  "assets": [
    {
      "date": "2026-07-21",
      "type": "outbound-sequence",
      "ref": "outbound-engine/examples/cohere/telus-sequence.json",
      "opening": "Your AI Factory expansion is public: Kamloops, two new Vancouver sites, a target of 60,000 GPUs by 2032.",
      "facts_used": ["AI Factory expansion (rcrwireless 2026-05-12)"]
    }
  ],
  "approved_language": [
    "Your factory. Your customers' data. Our models, running inside both."
  ],
  "do_not_say": [
    {
      "phrase": "Bell AI Fabric",
      "reason": "Documented judgment call from the outbound sequence: never name a rival's partnership in written first-line materials; surfaces on calls only",
      "since": "2026-07-21"
    }
  ],
  "corrections": [
    {
      "was": "60,000 GPUs by 2032",
      "now": "60,000+ GPUs by 2032 (their own materials say 60,000+)",
      "source": "internal: prospect call",
      "date": "2026-08-02"
    }
  ]
}
```

Rules: `assets[]` is append-only (the guard's `--log` mode appends; nothing edits history);
`do_not_say` entries change only with a reason; `corrections` supersede facts everywhere,
including facts arriving fresh in a brief; `approved_language` is copy that already survived
review and should be reused deliberately.

## What the state guard checks

`scripts/state_guard.py draft.md state.json [--brief brief.json]`:

- **Do-not-say**: any listed phrase in the draft fails it, with the recorded reason echoed back.
- **Repetition**: a draft whose opening sentence matches any logged asset's opening fails; the
  customer reads everything you send.
- **Unfilled tokens**: any `{{merge}}` remnant fails.
- **Stale facts** (with `--brief`): brief facts older than `fact_freshness_days` are flagged.
- **Corrections** (with `--brief`): a brief fact matching a correction's `was` string fails until
  the brief is updated; superseded facts do not regress.

`--log` appends the shipped asset (date, type, opening, facts used) to the state, so the next
run's repetition check includes this one.

## The asset

Any format the brief names. Two universal rules: every customer-specific line traces to a cited
fact from the brief or state, and the asset passes both gates (content-quality-check's linter
with the brand Avoid file, then the state guard) before it ships.
