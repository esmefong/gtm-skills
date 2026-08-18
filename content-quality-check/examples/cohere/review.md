# QA review: Cohere announcement draft

**Verdict: rework.** 23 flags across both passes on a 145-word draft. The mechanical sweep alone
is disqualifying; the judgment pass explains why a word-level fix would not be enough.

> Specimen note: `draft-before.md` is deliberately slop-ridden to exercise the checker, and it is
> the one file in this repo allowed to contain the patterns the standard bans. The revision that
> passes is `draft-after.md`.

## Mechanical sweep (verbatim)

```
REVISE: draft-before.md (8 high, 14 medium, 1 low)
  [HIGH] line 3: opener asks the reader a question: open with a claim instead
  [HIGH] line 6: the 'not just X, it's Y' construction: make one specific claim instead
  [HIGH] line 6: 'thrilled to announce' family: the most template opener there is
  [HIGH] line 6: brand Avoid-list word 'game-changing'
  [HIGH] line 6: 3 em dashes in one paragraph: restructure with periods
  [HIGH] line 7: brand Avoid-list word 'cutting-edge'
  [HIGH] line 10: 'let's dive in' family: telegraphs a generated answer
  [HIGH] line 10: brand Avoid-list word 'revolutionary'
  [MEDIUM] 14 flags: hollow hedges, over-represented words (unlock, seamless, robust, leverage,
           transformative, harness, testament), intensifier density, two closer formulas
  [LOW] line 17: exclamation in the final line
```

The brand Avoid words scan at HIGH because Cohere's own writing standard already banned them; the
linter just remembers.

## Editorial judgment pass

1. **The opener throat-clears twice** (checklist C1): a rhetorical question, then stage-setting
   ("in today's rapidly evolving landscape"). Delete the whole first paragraph and the piece
   improves. Fix: open on the claim (what shipped, where).
2. **No claim carries proof** (C3): "Leading enterprises everywhere trust our technology" names
   nobody; "the results truly speak for themselves" shows no results. Flagged as needs-proof.
3. **Nothing is specific** (C4): no regions, no deployment modes, no named capability. The draft
   could announce any product from any vendor, which is also a distinctiveness-test failure.
4. **Off-pillar** (C6): the draft centers the platform's magnificence. Cohere's voice centers the
   customer's ownership and the security review. Avoiding the banned words would not fix this;
   the frame itself is wrong.
5. **Template shape** (C5): question-then-answer scaffolding ("What does this mean for your
   business? It means...") and a recap close. The outline is showing through the prose.

## The revision

`draft-after.md` rewrites the same announcement in Cohere's voice: opens on the claim, makes the
security review the point, replaces every superlative with a specific (deployment modes, data
commitments, in-country infrastructure), and lands the possessive-contrast close. The linter
passes it clean:

```
PASS: draft-after.md (0 high, 0 medium, 0 low)
```
