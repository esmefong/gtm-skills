# Worked example: a second-touch ABM asset for TELUS

> **Real company, real public facts, illustrative.** The one-pager's customer-specific lines all
> trace to cited public sources; the state file's one internal-style correction is labeled
> illustrative. A demonstration of the skill, not an official Cohere document.

The composition demo: this asset is the **second** touch in the TELUS thread, and the state file
remembers the first. The outbound sequence's documented judgment call ("Bell is never named in
writing") arrived here as a `do_not_say` entry, its opening line is logged so it cannot be
reused, and a correction ("60,000+ GPUs, not 60,000") supersedes the original fact everywhere.

| File | What it shows |
|---|---|
| `telus-state.json` | The durable memory: the logged sequence, approved language, the inherited do-not-say rule with its reason, one correction |
| `brief.json` | The structured input: goal, audience, and cited facts only |
| `telus-abm-onepager.md` | The asset: Cohere's voice, every personalized line traceable, the approved line reused deliberately, a fresh opening |
| `telus-draft-rejected.md` | The refusal demo: reuses the sequence's opening, names the banned precedent, leaves a merge token |
| `cohere-avoid.txt` | The brand ban list for the content linter |

## Reproduce both gates

```
python3 ../../../content-quality-check/scripts/check_content.py telus-abm-onepager.md --avoid cohere-avoid.txt
python3 ../../scripts/state_guard.py telus-abm-onepager.md telus-state.json --brief brief.json --as-of 2026-09-04
python3 ../../scripts/state_guard.py telus-draft-rejected.md telus-state.json --as-of 2026-09-04
```

The asset passes both; the rejected draft fails with three reasons, the first of which echoes the
judgment call made in a different skill weeks earlier:

```
FAIL: TELUS <- telus-draft-rejected.md
  - do-not-say phrase 'Bell AI Fabric': Documented judgment call from the outbound sequence: never
    name a rival's partnership in written first-line materials; surfaces on calls only
  - opening repeats the 2026-07-21 outbound-sequence: the customer reads everything you send
  - unfilled merge token in draft
```

That first line is the skill's whole argument: a judgment call made once, remembered by the
system, enforced mechanically ever after.
