# Worker 7 — F4 Davi-reply addendum fix

## Task
Apply seven brief-specified wording fixes inside the 2026-10-28 addendum of
`docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` (line 541+). Lines 1–537
byte-identical. No verdict changed.

## Mode
BUILD (fix). Nothing staged or committed (brief: do not git add).

## Criterion
head-537 sha256 == ffda2e09…cb1; 0 deletions in `git diff --numstat`; every
`> ` quote after line 537 is a substring of the transcript fence; stale phrases
and forbidden terms absent after line 537.

## Process log
1. Read the addendum (lines 535–770); baseline head-537 hash matched.
2. Edit 1 (provenance para): replaced with the brief's text verbatim.
3. Edit 2 (URL para): replaced with the brief's text verbatim.
4. Edit 3 (C framing para): replaced with the brief's text verbatim.
5. Edit 4: "on a funded account" row — "On the most natural reading … (S8)." replaced
   with the brief's row-2 text verbatim; retroactivity row — "On the most natural
   reading … (S8)." replaced with the brief's row-4 text verbatim. Rest of both rows untouched.
6. Edit 5: effective-date row — "anywhere in the reply" → "anywhere in the visible text of the reply".
7. Edit 6: added the brief's bullet as the last item of A's UNVERIFIED list.
   Side effect, disclosed: the previously-last bullet's terminal `is f`. was changed to
   `is f`; so list punctuation stays consistent (inside the addendum).
8. Edit 7: E item 2 opener and thank-you sentence replaced per brief; fragments are
   backtick spans, both verified byte-exact in the fence (count 1 each).
9. Verdict column untouched in all four rows.

## Verification evidence
Note on numstat: the index holds only lines 1–537 of the target (cached diff 537/0);
the whole addendum is unstaged, so the worktree diff is pure additions (241/0).
Quote check covers every line after 537 matching `^ *> `, prefix stripped; the bare
`>` separator line (610) has no text and is not checked.

```text
$ head -n 537 <target> | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git diff --numstat -- <target>
241	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ git diff --cached --numstat -- <target>
537	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ extract fence
      25
$ quote-line substring check (lines >537 starting with optional indent + "> ")
L605 count=1
L606 count=1
L607 count=1
L608 count=1
L609 count=1
L611 count=1
L644 count=1
L713 count=1
L714 count=1
L716 count=1
L732 count=1
L735 count=1
L737 count=1
L740 count=1
L742 count=1
L744 count=1
L756 count=1
$ backtick fragments
Thank you for contacting	1
Thank you so much for reaching out	1
$ stale-phrase grep (expect empty)
$ forbidden sweep (expect empty)
$ end
```

## Files staged
None (brief forbids git add). Modified in worktree:
- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md (addendum only)
- docs/reports/2026-10-28-f4-davi-reply-worker7-fix.md (this report, new, untracked)

## Result: PASS
