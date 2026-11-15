# Adversarial check: D-2026-11-15-B and the safe-space rule filing report, after Cure 1

## Task

ADVERSARIAL, read-only. Try to break criteria C1-C6 against: (A) DECISIONS.md entry D-2026-11-15-B; (B) docs/reports/2026-11-15-safe-space-rule-filing.md; (C) the pre-cure copy of B in the session scratchpad (report-before-cure1.md). The only file written is this report. Nothing was staged, edited or committed. The live voice-call files were not opened. The only command run on the voice-notes file was `stat`.

Paste conventions. Every block below is real command output, produced by a bash runner script whose output passes through one sed filter. That filter replaces the whole standing limitation sentence with `[standing sentence, redacted in paste]`, the MFFU rep's first name with `[rep name]`, and the at-sign with `[at]`. The at-sign rule fired 0 times. The sentence and name replacements fired where shown.

## Criteria

- C1. DECISIONS.md lines 1-2904 are unchanged (sha256 d2030ce9...adea), numstat shows 0 deletions, and the file is 2918 lines.
- C2. The entry's Limits paragraph and new S4 timing paragraph match the exact text in the brief. "before the next voice call" is gone. Paragraphs are separated by single blank lines, there are no trailing spaces, the file ends with a newline, and its last line is the standing sentence.
- C3. Three facts are true: the v3 brief's mtime is 13:16:25-0500, the voice-notes file's mtime is 13:18:14-0500, and DECISION_LOG has exactly 1 row `2026-11-15T18:15:44Z WHO: amear`.
- C4. `diff C B` differs only at lines 10, 28, 66, 99 and 112, with the required content on each, and B has 0 rep-name hits.
- C5. The standing sentence is a whole line exactly once in B, and it is B's last line.
- C6. The staged set is only the pre-existing evidence PNG.

## Evidence

```
$ head -n 2904 DECISIONS.md | shasum -a 256
d2030ce9f0e6e4dc04d5669453a274f116910b28e65971d9f6bf8b5ab246adea  -
$ git diff --numstat -- DECISIONS.md
303	0	DECISIONS.md
$ wc -l < DECISIONS.md
    2918
$ tail -c 1 DECISIONS.md | od -c | head -1
0000000   \n                                                            
$ grep -n -F "D-2026-11-15-B" DECISIONS.md | cut -c1-40
2906:## 2026-11-15 — D-2026-11-15-B: eve
$ awk "NR>=2905{printf \"%d:%s\n\", NR, (length(\$0)==0?\"BLANK\":substr(\$0,1,22))}" DECISIONS.md
2905:BLANK
2906:## 2026-11-15 — D-20
2907:BLANK
2908:**Status:** RULED by A
2909:BLANK
2910:**The rule.** Every vo
2911:BLANK
2912:**Where it applies.** 
2913:BLANK
2914:**Limits.** No other r
2915:BLANK
2916:**S4 timing.** Amear's
2917:BLANK
2918:Fills are optimistic; 
$ sed -n 2914p DECISIONS.md
**Limits.** No other rule, spec, rubric line or code file is changed. Text fixed by praxis-master at 2026-11-15T18:16:32Z (`date -u`) and appended by praxis-manager (DECISIONS.md mtime 18:17:09Z). Uncommitted; it goes into the close flush and its audit.
$ sed -n 2916p DECISIONS.md
**S4 timing.** Amear's ruling is DECISION_LOG row 2026-11-15T18:15:44Z (WHO: amear). The master's version 3 voice brief (`docs/reports/2026-11-15-voice-brief-restructure-v3.md`, last written 18:16:25Z) applied this rule and cited this entry's id before this entry's text was fixed and appended; at that moment its only authority was the ruling row. That order is the master's defect. It is recorded here, not cured. The voice call governed by the rule opened at 13:18 ET (18:18Z), after the entry was appended.
$ sed -n 2918p DECISIONS.md
[standing sentence, redacted in paste]
$ sed -n 2906,2918p DECISIONS.md | grep -c -F "before the next voice call"
0
$ grep -c -F "Text fixed by praxis-master at 2026-11-15T18:16:32Z (\`date -u\`) and appended by praxis-manager (DECISIONS.md mtime 18:17:09Z)." DECISIONS.md
1
$ sed -n 2914p DECISIONS.md | grep -c -F "No other rule, spec, rubric line or code file is changed."
1
$ sed -n 2914p DECISIONS.md | grep -c -F "Uncommitted; it goes into the close flush and its audit."
1
$ sed -n 2905,2918p DECISIONS.md | grep -c "[[:space:]]$"
0
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S%z" docs/reports/2026-11-15-voice-brief-restructure-v3.md
2026-11-15T13:16:25-0500
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S%z" docs/reports/2026-11-15-voice-notes-restructure.md
2026-11-15T13:18:14-0500
$ stat -f "%SB" -t "%Y-%m-%dT%H:%M:%S%z" docs/reports/2026-11-15-voice-notes-restructure.md
2026-11-15T13:18:14-0500
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S%z" DECISIONS.md
2026-11-15T13:23:08-0500
$ date -u
Sun 15 Nov 2026 18:26:10 UTC
$ grep -c '^- \[2026-11-15T18:15:44Z\] WHO: amear' DECISION_LOG.md
1
$ grep -n '^- \[2026-11-15T18:1[56]' DECISION_LOG.md | cut -c1-200
1023:- [2026-11-15T18:15:44Z] WHO: amear | WHAT: **Amear's typed rulings on the v2 brief, verbatim:** "1. Safe-space opener: yes, standing rule for every voice call on this project. Log it in DECISION
1024:- [2026-11-15T18:16:32Z] WHO: praxis-master | WHAT: **v3 brief written; DECISIONS.md append dispatched.** OBSERVED: the master's Edit to DECISIONS.md was DENIED by the write hook ("praxis-master 
$ grep -n -E "18:17|13:17" "$B" DECISION_LOG.md | wc -l
       6
$ diff "$C" "$B"
10c10
< - **S4** (specs/SPEC_RUBRIC.md:136): the entry is written after Amear's ruling (DECISION_LOG row 2026-11-15T18:15:44Z, WHO: amear, HOW: typed) and before any act under it. No voice brief or skill file was written or edited by this unit.
---
> - **S4** (specs/SPEC_RUBRIC.md:136): the entry is written after Amear's ruling (DECISION_LOG row 2026-11-15T18:15:44Z, WHO: amear, HOW: typed) and before any act under it. No voice brief or skill file was written or edited by this unit. [Corrected in Cure 1: false; see Cure 1 item d.]
28c28
< [standing sentence, redacted in paste]
---
> [standing limitation sentence; it appears once, as this report's last line]
66c66
< [standing sentence, redacted in paste]
---
> [standing limitation sentence; it appears once, as this report's last line]
99c99
< docs/reports/evidence/2026-10-28-mffu-[rep name]-reply.png
---
> docs/reports/evidence/2026-10-28-mffu-[rep name]-reply.png
112c112
< - C5 HOLDS: staged set is only `docs/reports/evidence/2026-10-28-mffu-[rep name]-reply.png`.
---
> - C5 HOLDS: staged set is only `docs/reports/evidence/2026-10-28-mffu-[rep name]-reply.png`.
$ grep -c -i "d[a]vi" "$B"
0
$ grep -n -x -F "$SS" "$B"
136:[standing sentence, redacted in paste]
$ grep -c -F "Fills are optimistic" "$B"
1
$ wc -l < "$B"; tail -c 1 "$B" | od -c | head -1
     136
0000000   \n                                                            
$ grep -n -i "^#.*cure" "$B" | wc -l
       0
$ git diff --cached --name-only | sed "s/d[a]vi/[rep name]/"
docs/reports/evidence/2026-10-28-mffu-[rep name]-reply.png
```

Extra check: is there an independent source for the append time "DECISIONS.md mtime 18:17:09Z"? (The 6 hits above for 18:17 or 13:17 all come from DECISION_LOG.md. B has none.)

```
$ grep -n -o -E ".{60}(18:17|13:17).{40}" DECISION_LOG.md
586:d together. | WHY: loop step 5 | WHERE: STATUS.md:7 | WHEN: 18:17:30Z | HOW: praxis-auditor | STATE: PASS
612:lines, read by the master this turn, OBSERVED).** R-VN3-1 (~13:17Z): *"So first things first, the strateg
612:ion | WHERE: notes-3 lines 9–16 | WHEN: rulings 2026-11-02 ~13:17Z/~13:20Z; entered 21:23:45Z | HOW: quot
914:reports/2026-11-13-o4-reduce3-manager.md` | WHEN: `date -u` 13:17:27Z | HOW: praxis-manager, foreground |
916:ra` ended at 1. Closes the 13:02:03Z, 13:07:54Z, 13:13:15Z, 13:17:27Z and 13:24:23Z rows. **Decided by ma
921:: (a) "MANIFEST line numbers and one report line" where the 13:17:27Z row names two report lines (:13 and
1026:text was fixed (18:16:32Z) and appended (DECISIONS.md mtime 13:17:09 ET); manager report :10 says "before
```

## Findings

- C1 HOLDS. The first-2904-line sha256 matches. Numstat is `303 0` (0 deletions). The file is 2918 lines.
- C2 HOLDS. Line 2914 contains each of the three required Limits sentences (each grep -c gives 1). Line 2916 matches the S4 timing paragraph as an exact whole line. "before the next voice call" has 0 hits in the entry and 0 in the file. Lines 2905-2918 alternate text and single blank lines. There are 0 trailing-whitespace lines. The file ends with a newline, and line 2918 is the standing sentence.
- C3 HOLDS. The v3 brief's mtime is 2026-11-15T13:16:25-0500 and the voice-notes file's mtime is 2026-11-15T13:18:14-0500 (its birth time is the same). The DECISION_LOG row count is 1. DECISIONS.md's mtime is now 13:23:08-0500 (18:23:08Z), later than 18:17:09Z, which is expected after the cure.
- C4 HOLDS. `diff C B` shows only 10c10, 28c28, 66c66, 99c99 and 112c112. Line 10 keeps its original words and ends with the Cure 1 marker. Lines 28 and 66 are the placeholder. Lines 99 and 112 have `[rep name]` in the PNG path. `grep -c -i` for the rep name on B gives 0.
- C5 HOLDS. The whole-line grep has 1 hit, at :136. B is 136 lines and ends with a newline. B has no Cure section yet (0 headings containing "cure").
- C6 HOLDS. The staged set is only the 2026-10-28 MFFU evidence PNG.

Observations. None of these breaks a criterion as worded.
1. B:10 now ends "see Cure 1 item d", but B has no Cure 1 section (0 matching headings at the time of this check). The cross-reference is dangling until that section is added.
2. The append time 18:17:09Z in the Limits paragraph cannot be re-measured now, because DECISIONS.md's mtime has moved to 18:23:08Z. The only other place it appears is the master's own DECISION_LOG row :1026 ("13:17:09 ET"). B does not record it. UNVERIFIED by me this session.
3. "The voice call ... opened at 13:18 ET (18:18Z)" rests on the voice-notes file's birth time, 13:18:14-0500. That is when the file was created, not a record that the call opened. "after the entry was appended" holds only if observation 2 is right: 18:17:09Z comes before 18:18:14Z, but 18:17:09Z is the unverified figure. The timezone conversion is correct: the offset is -0500 (EST), so 13:18 ET is 18:18Z.
4. B:113 still reads numstat `301 0`. It is now `303 0`, because the cure added 2 lines (the S4 paragraph and a blank line), which matches 2916 becoming 2918. This is stale pre-cure evidence inside B, not a contradiction.

## Result: PASS

NO BREAK FOUND on C1-C6. Cases tried: the head-2904 hash; numstat deletions; line count; trailing byte; exact fixed-string and whole-line matches for both paragraphs; the forbidden phrase in the entry and in the whole file; trailing whitespace; the blank-line pattern; stat mtime and birth time; the DECISION_LOG row count; a search for independent evidence of the 18:17:09Z time; the full diff of C against B; a case-insensitive rep-name grep; the standing-sentence count, position and trailing newline; a Cure section heading in B; the staged set.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
