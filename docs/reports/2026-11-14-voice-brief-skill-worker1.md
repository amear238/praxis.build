# Voice-brief skill, worker 1 (2026-11-14)

**Task:** unit `2026-11-14-voice-brief-skill`, Amear's ruling R9(b) in D-2026-11-14-B, for praxis-manager. HEAD d9fc5f0.
**Mode:** BUILD.
**Criterion:** R-a to R-e of the brief. Rubric S8 (specs/SPEC_RUBRIC.md :140) and S13 (:145).

## Files written
- `.claude/skills/voice-brief/SKILL.md` (new, untracked, NOT staged: the brief forbids `git add` on the real index).
- This report.
No other file touched. Nothing installed, enabled or registered.

## Process log
- Read DECISIONS.md :2619-:2694 (D-2026-11-14-B, R9, Q1-Q6), :1891-:1958 (D1, D2, D5, D10).
- Read notes `docs/reports/2026-11-14-voice-notes-pivot.md` :46-:59; model brief (49 lines); praxis-build-manager SKILL.md :1-:4.
- Checked labels exist: HANDOFF.md :20 "Questions that are Amear's"; STATUS.md :9 "Waiting on Amear".
- Checked `hermes` is at /Users/admin/.local/bin/hermes and `~/.hermes/cron/jobs.json` exists. Did not run `hermes cron list`; the "No scheduled jobs." fact is from the brief, UNVERIFIED by me.
- Choice for R-b step 3e: no clock item means leave the section out AND add "No time-bound item." to the provenance line.

## Verification evidence
```text
$ wc -l SKILL.md
      95 SKILL.md
$ grep -nP '[^\x00-\x7F]' SKILL.md ; grep -nE '[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.' SKILL.md ; echo rc=$?
rc=1
$ git status --short .claude/skills/voice-brief
?? .claude/skills/voice-brief/
```
Requirement to line map (from `grep -nE` on SKILL.md, line numbers only):
```text
R-a frontmatter      1:---  2:name: voice-brief  3:description: "...two or more topics... voice chat... ambiguous..."  4:---
R-a cite R9          12:**Authority.** Amear's ruling R9 in D-2026-11-14-B (DECISIONS.md, from :2619).
R-b1 gather          24 (Questions that are Amear's), 25 (Q-lists), 26 (Waiting on Amear), 27-29 (hermes cron list AND jobs.json, each reported)
R-b2 re-verify       32, 34 (UNVERIFIED)
R-b3 sections        35 path; 37 title+provenance; 39 What Amear wants; 41-51 How to run (42 tenth; 43-44 labels; 46 ONE notes file; 48-51 four items); 53 neutral, master's view; 54-55 clock; 56 read more; 58 S13 line
R-b4 length          59:4. **Keep it short.** Under about 80 lines. It is read aloud.
R-b5 answer nothing  60 (S8 quoted), 62 (master's view only)
R-b6 after           64 DECISION_LOG row; 65 path; 67-68 REPORTED BY, unit, manager, auditor, gated commit
R-c                  72 ONLY questions; 78-84 filter test; 85-87 D1 log line and D5; 91-95 What this skill does not do
R-d                  3 (DRAFT), 8-10 (DRAFT, :59 quote, binds no one until approved)
R-e                  95 lines; no non-ASCII; no email (rc=1 above)
```
Quote check: `sed -n 59p` of the notes file contains "Propose it to Amear for approval; do not self-certify" (grep -o matched).

## Not satisfied or flagged
- Not staged, by instruction. The manager decides staging.
- Filter items 2-3 (waivers, reserved choices) go wider than rubric :470's reading that "what belongs to Amear is the D2 list". The brief asked for them. The tension is named, not resolved.
- Q1-Q6 are named, not answered.

Result: PASS (staging left to the manager).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
