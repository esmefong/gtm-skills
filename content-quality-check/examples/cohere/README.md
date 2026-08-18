# Worked example: QA pass on a Cohere announcement

> **Illustrative.** Both drafts were written for this example; neither is real Cohere copy. The
> Avoid list is taken from the Cohere voice guide elsewhere in this repo.

A before, a review, and an after, with the checker run on all of it.

| File | What it is |
|---|---|
| `draft-before.md` | A deliberately slop-ridden announcement: 23 flags, including a cross-line "isn't just X, it's Y", an em-dash chain, and three brand Avoid words. The one file in the repo allowed to contain what the standard bans |
| `before-findings.json` | The linter's structured output on it |
| `review.md` | The deliverable: verdict, the mechanical sweep verbatim, and the judgment findings no regex can see (throat-clearing opener, claims without proof, off-pillar frame) |
| `draft-after.md` | The same announcement in Cohere's actual voice; the linter passes it with zero flags |
| `cohere-avoid.txt` | The brand ban list, from `brand-voice-guide/examples/cohere/brand-voice/writing-standard.md` |

## Reproduce

```
python3 ../../scripts/check_content.py draft-before.md --avoid cohere-avoid.txt
python3 ../../scripts/check_content.py draft-after.md --avoid cohere-avoid.txt
```

## Why the pairing matters

The before shows the checker catching what a tired writer no longer sees. The after shows the
standard is passable: the fix was never "remove the banned words" but "change the frame from the
platform's magnificence to the customer's control," which is exactly the line between the linter's
job and the editor's.
