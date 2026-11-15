# 2026-11-15 rulings filing, worker 7: fixes for the eleven worker 6 findings

## Task

I fixed the eleven "New findings" in `docs/reports/2026-11-15-rulings-filing-worker6.md`. They apply to the draft DECISIONS.md entry D-2026-11-15-A in the scratchpad file `entry.md`. The full path is `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md`. Before the fix it had 195 lines and sha256 114c05a60bf6d0b678ed831fac3ee9a23261786da4bcb6d051038c40a752e606, the same bytes as the frozen `entry-v3.md`. Unit `2026-11-15-rulings-filing`, HEAD `d9fc5f0`. I edited only `entry.md` and wrote this report. I made no commit and touched no git index. I did not edit `entry-v3.md` or any fenced ```text block. Items (a)-(o) are kept. The one new item is (p), labelled "(the filer's addition)".

## Mode: BUILD (fix)

## Defects and fixes

Before writing anything, I checked each finding against its source. The source lines are printed under "Commands and output" below. Each finding held as stated. All edits were made by two `python3 -I` scripts. Each script does exact-string replacement and asserts that every old string occurs exactly once (the second script asserts exactly twice, for one string that occurs twice).

1. (MED) Typed ruling 1 and "No tick purchase".
   - Before: the walk-forward bullet called only the first two sentences of spec :36 "Amear's typed words". It gave "No tick purchase. R-VN4-7 stands." as what ":36 ends" with and linked it to R5 alone. Item (k) cited neither.
   - Change: the bullet now says that all of :36, headed "**Typed ruling 1** — RULED" at :35, is his typed ruling 1 (DECISION_LOG row `2026-11-05T23:50:09Z`, WHO: amear, typed). It quotes R-VN4-7 (HEAD DECISIONS.md :947): "We're just gonna proceed without that [historical tick data]." It names R2, item (k) ("a purchase or a build") and R5 (with notes :115) as bearing on "No tick purchase" and R-VN4-7. It says that whether real MNQ data must be tick data is not said in the notes, in T1, in ruling 1 or in R-VN4-7, and that spending money waits for Amear's explicit word (brief :15). The bullet still reads "Named, not resolved." Item (k) gets the same cross-reference, the same quotes and the brief :15 line.
   - After: entry :184 (walk-forward bullet) and :171 (item (k)).
2. (MED) Topology bullet.
   - Before: "is built with".
   - Change: now "is specified with". Added: the row's status is "SPECIFIED. No numeric threshold exists anywhere" (:58), and the pieces it depends on are marked unbuilt in the same row: "An account-state feed from NT8 to Redis (unbuilt)" and "EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt".
   - After: entry :185. `grep -c -F 'is built with'` gives 0.
3. (LOW) "personal" labels and the R12 heading.
   - Before: "$10,000 personal account" appeared unlabelled in the R7 heading, in item (j) and in the A4 bullet. The R12 heading read "The MFFU email" as his.
   - Change: the R7 heading now reads "$10,000 account (personal per the channel's parenthetical, notes :63)". Item (j) reads "a $10,000 account (R7; personal per the channel's parenthetical, notes :63)". The A4 bullet reads "R7 (a $10,000 account, personal per the channel's parenthetical)". The R12 heading adds: ""MFFU email" as the referent is the channel's heading, notes :118, and the filer's reading below".
   - Citation corrected during the work: my first script cited "notes :59" for the parenthetical. The first verification run printed 0 for `(personal account, $10,000)` on notes :59. The parenthetical is on notes :63, so the second script corrected both citations to :63. Both runs are pasted below.
   - Other "personal" hits, now all labelled or quoted: :61 (the heading and the fence lead-in, which already names the parenthetical as the channel's), :66 (fenced quote), :69 (already labelled), :184 (the quoted ruled item and the labelled R7 mention).
   - After: entry :61, :152, :170, :183.
4. (LOW) Walk-forward spec :31 is a ruled item.
   - Before: the entry presented ":31 says "Revisit if a personal account is used."" as spec text.
   - Change: the bullet now says that :31 quotes D-2026-11-05-A item 3, a ruled item (heading DECISIONS.md :803 at HEAD; item 3 at :814). That entry marks the item REPORTED BY the voice agent (:806, :811). Its words include "Revisit if a personal account is used." The bullet adds that R7's $10,000 account (personal per the channel's parenthetical) may meet that revisit clause, and ends "Named, not resolved."
   - After: entry :184.
5. (LOW) D-2026-11-14-B R9 was missing.
   - Change: added to the D-2026-11-14-B bullet: R9 (:2586, "Process instructions"), with its filer's reading at :2591 quoted: "(a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48)." The bullet says this bears on this entry's R10 (the skill `Praxis_build-61o` stays parked by the park rule's default; item (p)) and on T1's "If a source spec has no stop, don't decide anything: bring it back to me." Named, not resolved.
   - After: entry :179.
6. (LOW) Status :3, the brief's filing authority.
   - Before: "filed with this entry at the master's dispatch of this unit;".
   - Change: now "filed with this entry at the master's direction in its dispatch to this unit's manager, which no ledger row records;". The quotes from rows 14:38:00Z and 13:30:00Z that follow are kept unchanged.
   - After: entry :3.
7. (LOW) "answered" and "confirmed" for Q1 / R8.
   - Before: :44 read "Q1 of D-2026-11-14-B is answered as wait-for-data". The D-2026-11-14-B bullet read "is confirmed by this entry's R4".
   - Change at :44: "the filer reads Q1 of D-2026-11-14-B as answered wait-for-data; "confirmed" is the channel's heading (notes :35), not his word. His words reject a number now ("I can't set a number right now", notes :38) and do not address Q1's other form, "a multiple of the cost of a trade" (DECISIONS.md :2595 at HEAD)."
   - Change in the bullet: R8 "is, on the filer's reading, kept by this entry's R4", plus the same labels.
   - I added no new answer.
   - After: entry :44 and :179.
8. (LOW) The $2.96 qualifier.
   - Before: "and the cost model stays $2.96."
   - Change: now "and "The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear" (:970, which marks the fee report "NEEDS AMEAR")."
   - After: entry :182.
9. (LOW) "not compatible".
   - Before: 'He said a design with no known maximum loss is "not compatible".'
   - Change: now 'His words are "Then that's not compatible." (notes :92); that "that" is a design with no known maximum loss comes from the channel's lead-in on notes :92 ("On the design having no known max loss:").' The word "refines" is left as it was, per the brief.
   - After: entry :121.
10. (LOW) The voice-brief skill had no open item.
    - Change: added item (p) (the filer's addition): whether his "I don't fucking give a shit, to be honest." (notes :110) leaves `Praxis_build-61o` parked, or leaves the pick to the master among the brief's options (brief :48, quoted; the master's view at brief :49, "the skill fix is paperwork only", quoted). Until a person resumes it, the park rule's default holds. Answer: NONE.
    - Also added a pointer "(item (p) below)" at the end of the R10 sentence about the brief's options, so that R10 points to (p) the same way it points to (n).
    - After: entry :176 and :148.
11. (LOW) The Phase 3 :54 bracket.
    - Before: 'Block 1 names a bracket "stop-loss + take-profit" with no sizing rule (:54).'
    - Change: now 'Block 1 names "a stop-market entry with a bracket (stop-loss + take-profit)" with no sizing rule (:54). That bracket stop bears on T1's stop "sitting at the broker and placed at entry" and on item (o) (ruling 1's "Not a resting stop in the backtest."). Named, not resolved.'
    - After: entry :187.

S4 timing: the existing times are kept, and ", revised a third time 2026-11-15T15:31:08Z" is added after them. That time is the UTC time my first fix script wrote with `datetime.now(timezone.utc)`; the script printed it. The second script ran shortly after that and changed only the two "notes :59" citations.

Not fixed: none of the eleven.

Seen but outside my scope, so not changed: the R7 fence lead-in (entry :61) names ":59's lead-in" and then lists "So prop firms stay out for now.", "Account size:" and the parenthetical. Those three strings are on notes :63, not :59 (see the `sed -n '63p'` output below). The lead-in gives no line for them, so this is a reader-trap at most. I did not edit that sentence.

## Commands and output

### Fix script 1, in full (`w7-fix.py`)

Command: `python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w7-fix.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md`

Output:
~~~~
applied 18 replacements; revised a third time 2026-11-15T15:31:08Z
~~~~

Script text:
~~~~python
import sys, datetime
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
R = [
# 1a WF bullet: all of :36 is typed ruling 1
("These are Amear's typed words, not spec text only: D-2026-11-05-C records them as",
 "All of :36, headed \"**Typed ruling 1** — RULED\" at :35, is Amear's typed ruling 1 (DECISION_LOG row `2026-11-05T23:50:09Z`, WHO: amear, typed), not only these two sentences and not spec text only: D-2026-11-05-C records it as"),
# 1b WF bullet: tick-purchase touch
("The same :36 ends \"Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands.\" R5 counts slippage past the stop in the cost of the trade once it is measured by enough testing, and the channel's check (notes :115) says \"1-minute bars cannot show where a real fill would have landed\". Named, not resolved.",
 "The same :36, still his typed ruling 1, ends \"Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands.\" R-VN4-7 (DECISIONS.md :947 at HEAD) carries \"We're just gonna proceed without that [historical tick data].\" R2 (test the single candidate on real MNQ data), open item (k) (whether that testing is \"a purchase or a build\") and R5 (slippage past the stop counted in the cost of the trade once it is measured by enough testing, where the channel's check, notes :115, says \"1-minute bars cannot show where a real fill would have landed\") bear on \"No tick purchase\" and on R-VN4-7. Whether real MNQ data must be tick data is not said in the notes, in T1, in ruling 1 or in R-VN4-7. Spending money waits for Amear's explicit word (brief :15). Named, not resolved."),
# 1c item (k)
("whether testing on it is a purchase or a build. No source is named in the notes. Answer: NONE.",
 "whether testing on it is a purchase or a build. No source is named in the notes. His typed ruling 1 (`2026-11-05T23:50:09Z`; walk-forward spec :36 at HEAD) says \"No tick purchase. R-VN4-7 stands.\", and R-VN4-7 (DECISIONS.md :947 at HEAD) carries \"We're just gonna proceed without that [historical tick data].\" R5 bears on it too (S6 below, walk-forward spec). Whether real MNQ data must be tick data is not said. Spending money waits for Amear's explicit word (brief :15). Answer: NONE."),
# 2 topology
("action is built with \"resting stops on every live position\", citing R-VN4-2 as \"Until the account is live … resting stops.\", and marks the reading \"resting stops once live\" as the voice agent's.",
 "action is specified with \"resting stops on every live position\", citing R-VN4-2 as \"Until the account is live … resting stops.\", and marks the reading \"resting stops once live\" as the voice agent's. The row's status is \"SPECIFIED. No numeric threshold exists anywhere\" (:58), and the pieces it depends on are marked unbuilt in the same row: \"An account-state feed from NT8 to Redis (unbuilt)\" and \"EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt\"."),
# 3a R7 heading
("prop firms stay out; $10,000 personal account; the MFFU follow-up",
 "prop firms stay out; $10,000 account (personal per the channel's parenthetical, notes :59); the MFFU follow-up"),
# 3b item (j)
("applies to a $10,000 personal account (R7).",
 "applies to a $10,000 account (R7; personal per the channel's parenthetical, notes :59)."),
# 3c A4 bullet
("R7 (a $10,000 personal account) and R8(c)",
 "R7 (a $10,000 account, personal per the channel's parenthetical) and R8(c)"),
# 3d R12 heading
("**R12 — The MFFU email: hand it to the master (notes section 12, W2).**",
 "**R12 — The MFFU email: hand it to the master (notes section 12, W2; \"MFFU email\" as the referent is the channel's heading, notes :118, and the filer's reading below).**"),
# 4 WF :31
("(:31-:32; :31 says \"Revisit if a personal account is used.\"), which R7 bears on.",
 "(:31-:32). :31 quotes D-2026-11-05-A item 3, a ruled item (heading DECISIONS.md :803 at HEAD; item 3 at :814), which that entry marks REPORTED BY the voice agent (:806, :811); its words include \"Revisit if a personal account is used.\" R7 bears on it: R7's $10,000 account (personal per the channel's parenthetical) may meet that revisit clause. Named, not resolved."),
# 5 + 7b D-2026-11-14-B bullet
("D-2026-11-14-B R8 (:2580, the daily-loss cap waits for data) is confirmed by this entry's R4. Named, not resolved.",
 "D-2026-11-14-B R8 (:2580, the daily-loss cap waits for data) is, on the filer's reading, kept by this entry's R4; \"confirmed\" is the channel's heading (notes :35), and his words reject a number now but do not address Q1's \"a multiple of the cost of a trade\" form (:2595). D-2026-11-14-B R9 (:2586, \"Process instructions\"; its filer's reading at :2591: \"(a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48).\") bears on this entry's R10 (the voice-brief skill `Praxis_build-61o` stays parked by the park rule's default; item (p)) and on T1's \"If a source spec has no stop, don't decide anything: bring it back to me.\" Named, not resolved."),
# 6 status
("filed with this entry at the master's dispatch of this unit;",
 "filed with this entry at the master's direction in its dispatch to this unit's manager, which no ledger row records;"),
# 7a :44
("Filer's reading: Q1 of D-2026-11-14-B is answered as wait-for-data. No daily-loss figure",
 "Filer's reading: the filer reads Q1 of D-2026-11-14-B as answered wait-for-data; \"confirmed\" is the channel's heading (notes :35), not his word. His words reject a number now (\"I can't set a number right now\", notes :38) and do not address Q1's other form, \"a multiple of the cost of a trade\" (DECISIONS.md :2595 at HEAD). No daily-loss figure"),
# 8 :970
("MFFU's page gives NQ $4.68 round trip (MNQ $1.90), and the cost model stays $2.96.",
 "MFFU's page gives NQ $4.68 round trip (MNQ $1.90), and \"The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear\" (:970, which marks the fee report \"NEEDS AMEAR\")."),
# 9 :121
("He said a design with no known maximum loss is \"not compatible\".",
 "His words are \"Then that's not compatible.\" (notes :92); that \"that\" is a design with no known maximum loss comes from the channel's lead-in on notes :92 (\"On the design having no known max loss:\")."),
# 10a R10 pointer
("That fact does not answer the brief's options (brief :48), which also turn on the gap fade.",
 "That fact does not answer the brief's options (brief :48), which also turn on the gap fade (item (p) below)."),
# 10b item (p)
("whether it reaches T1's retest is part of this item. Answer: NONE.\n",
 "whether it reaches T1's retest is part of this item. Answer: NONE.\n- (p) (the filer's addition) Whether his \"I don't fucking give a shit, to be honest.\" (notes :110), on the voice-brief skill (`Praxis_build-61o`), leaves it parked, or leaves the pick to the master among the brief's options (brief :48, \"Options: A. Resume both. B. Resume the skill only. C. Leave both parked.\"; the master's view at brief :49 is \"the skill fix is paperwork only\"). Until a person resumes it, the park rule's default holds (R10 above). Answer: NONE.\n"),
# 11 Phase 3 :54
("Block 1 names a bracket \"stop-loss + take-profit\" with no sizing rule (:54).",
 "Block 1 names \"a stop-market entry with a bracket (stop-loss + take-profit)\" with no sizing rule (:54). That bracket stop bears on T1's stop \"sitting at the broker and placed at entry\" and on item (o) (ruling 1's \"Not a resting stop in the backtest.\"). Named, not resolved."),
# S4
("revised again 2026-11-15T15:16:31Z, before",
 "revised again 2026-11-15T15:16:31Z, revised a third time %s, before" % now),
]
for i,(a,b) in enumerate(R):
    c = s.count(a)
    assert c == 1, (i, c, a[:60])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print("applied", len(R), "replacements; revised a third time", now)
~~~~

### Fix script 2, in full (`w7-fix2.py`)

Command: `python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w7-fix2.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md`

Output:
~~~~
replaced 2 occurrences of the notes :59 citation with notes :63
~~~~

Script text:
~~~~python
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
a = "personal per the channel's parenthetical, notes :59"
b = "personal per the channel's parenthetical, notes :63"
assert s.count(a) == 2, s.count(a)
s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print("replaced 2 occurrences of the notes :59 citation with notes :63")
~~~~

### Runner

All checks below ran through `/bin/bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w7-run.sh <command file>`. The runner prints each command after `$ `, then its output, then its exit status. Runner text:
~~~~bash
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
while IFS= read -r c; do printf '$ %s\n' "$c"; bash -c "$c" 2>&1; printf '[exit %s]\n\n' "$?"; done < "$1"
~~~~

### Run 1: source checks and byte checks, after fix script 1 and before fix script 2

The `wc -l` and `shasum` results in this run are from before fix script 2 and are superseded by run 2. The notes :59 check prints 0, which is the citation error that fix script 2 corrected. Output, untrimmed:
~~~~
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/mgr/qcheck.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md docs/reports/2026-11-15-voice-notes-open-questions.md DECISION_LOG.md
block  1 entry :9-:11  sed -n '12,14p'              IDENTICAL
block  2 entry :15-:17  sed -n '16,17p;19p'          IDENTICAL
block  3 entry :23-:25  sed -n '23,25p'              IDENTICAL
block  4 entry :31-:34  sed -n '29p;31,33p'          IDENTICAL
block  5 entry :40-:42  sed -n '37,38p;40p'          IDENTICAL
block  6 entry :48-:50  sed -n '44,45p;47p'          IDENTICAL
block  7 entry :56-:57  sed -n '51p;53p'             IDENTICAL
block  8 entry :63-:67  sed -n '57p;59p;61p;63,64p'  IDENTICAL
block  9 entry :75-:79  sed -n '69,73p'              IDENTICAL
block 10 entry :85-:85  sed -n '75p'                 IDENTICAL
block 11 entry :91-:92  sed -n '77,78p'              IDENTICAL
block 12 entry :98-:99  sed -n '81,82p'              IDENTICAL
block 13 entry :105-:105  sed -n '86p'                 IDENTICAL
block 14 entry :109-:109  sed -n '88p'                 IDENTICAL
block 15 entry :113-:115  sed -n '91,93p'              IDENTICAL
block 16 entry :119-:119  sed -n '95p'                 IDENTICAL
block 17 entry :125-:125  sed -n '106p'                IDENTICAL
block 18 entry :131-:131  T1 row extraction            IDENTICAL
block 19 entry :145-:146  sed -n '110,111p'            IDENTICAL
block 20 entry :154-:154  sed -n '120p'                IDENTICAL
blocks 20, differ 0
[exit 0]

$ tr -cd '\100' < /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md | wc -c
       0
[exit 0]

$ grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
1
[exit 0]

$ tail -1 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
[exit 0]

$ wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
     196 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
[exit 0]

$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
4165ce48f491ac297da6cf7a2e4cc43cf1e1c9fb50b2cdd7260974658227ebb7  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
[exit 0]

$ grep -c -F 'is built with' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
0
[exit 1]

$ grep -n -o -F 'personal' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
61:personal
61:personal
66:personal
69:personal
170:personal
183:personal
184:personal
184:personal
[exit 0]

$ grep -c -F '```text' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v3.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v3.md:20
/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md:20
[exit 0]

$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '31p;35p;36p'
- *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
**Typed ruling 1** — RULED (DECISION_LOG `[2026-11-05T23:50:09Z] WHO: amear`, "typed, verbatim"):
> "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands."
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '803p;806p;811p;814p'
## 2026-11-05 — D-2026-11-05-A: Walk-forward design rulings (Amear, voice 2026-11-05)
**Status:** RULED by Amear — items 1–5, graded REPORTED BY the voice agent. The text is the voice agent's record of his rulings, pasted by Amear with "file as WHO: amear". Ledger authorisation (S5): DECISION_LOG `2026-11-05T23:40:21Z` (WHO: amear). Appended 2026-11-05 by praxis-manager, unit `2026-11-05-addendum-filing`.
**The five items, verbatim from the row (REPORTED BY the voice agent, pasted by Amear with "file as WHO: amear"):**
- *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '947p'
- **R-VN4-7** — proof of concept: "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." / "We're just gonna proceed without that [historical tick data]."
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '970p'
- (iii) R-VN4-6 with the fee report (`docs/reports/2026-11-05-mffu-fee-check.md:7-10`): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM. The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear (DECISION_LOG `2026-11-05T23:59:40Z`, `2026-11-06T00:06:48Z`; fee report NEEDS AMEAR at `:131`).
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '2586p;2591p;2595p'
**R9 — Process instructions.** Notes :47-:48:
Filer's reading: two instructions. (a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48). That it is proposed to Amear, not self-certified, is the voice agent's handoff (notes :59), not his words.
- **Q1, R8 wording.** His "Yeah" could mean "wait for data" or agree to "a multiple of the cost of a trade." Recorded as wait-for-data. Confirm.
[exit 0]

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '58p'
| 1 | Daily loss limit | n8n gate node, before Write Signal File: Redis flag `gate:daily_loss` (closed when realised + unrealised P&L ≤ −threshold, or when the P&L reading is stale). Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes, plus resting stops on every live position (R-VN4-2: "Until the account is live … resting stops.", REPORTED BY the voice agent; the reading "resting stops once live" is the voice agent's, Phase 3 import :24–25) [E27]. | The gate stops every new entry signal before the file is written, so no file reaches the consumer and no order is submitted. The flatten is an order itself; it is a risk-reducing exit, not a new entry, and must never be blocked by a closed gate (OPEN-T2). | Realised + unrealised P&L for the session, in real time, from the NT8 account; the threshold. | SPECIFIED. No numeric threshold exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65). | An account-state feed from NT8 to Redis (unbuilt); EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt; the consumer only knows BUY/SELL, :516–520, and only calls `EnterLong` / `EnterShort`, :660, :662 [E14]; under NT8's managed approach an `EnterShort` while long reverses into a short, `PraxisNoiseAreaBreakout.cs`:224, so an exit sent as SELL would open a position); a threshold value (R8 KEEP; value PROPOSED by a later unit; D2(c) once real money is at stake). |
[exit 0]

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '54p'
NinjaScript fundamentals. The NQ Noise-Area strategy is mechanically simple: at a fixed time, check if price has broken above or below a calculated noise band, place a stop-market entry with a bracket (stop-loss + take-profit). In NinjaScript, that’s an OnBarUpdate() method that checks the time, computes the band from the day’s range, and calls EnterLongStopMarket() or EnterShortStopMarket() with SetStopLoss() and SetProfitTarget(). Claude writes the code. You read it, understand what each block does, and can explain it back. That’s the bar.
[exit 0]

$ sed -n '35p;38p;59p;92p;110p;115p;118p' docs/reports/2026-11-15-voice-notes-open-questions.md
## 4. Q1, daily-loss cap: wait-for-data, confirmed (W1)
> "As far as the actual figure on what that is, that entirely depends on whether we have a strategy that has been proven to work with MFFU or whatever, um, whatever, whatever like uh, brokerage I'm going to go with, okay, um, so I, I can't set a number right now."
then, told this reverses yesterday's ruling:
The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. On the design having no known max loss: "Then that's not compatible. What kind of, who the fuck wants to trade like that?"
- **Voice-brief skill (`Praxis_build-61o`).** Amear: "I don't fucking give a shit, to be honest." No word to resume, so it **stays parked**.
1. The gap fade's $472.90 largest loss is likely understated: the test books every stop at level + 0.5 pt, yet the bar traded past the stop on 273 of 286 stop exits (max 45.5 pt). 1-minute bars cannot show where a real fill would have landed. The voice agent first gave a "$91 extra" figure and then retracted it as overstated.
## 12. MFFU email: hand to the master (W2)
[exit 0]

$ sed -n '15p;48p;49p' docs/reports/2026-11-15-voice-brief-open-questions.md
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
Options: A. Resume both. B. Resume the skill only. C. Leave both parked.
The master's view: the skill fix is paperwork only. Re-running two commands and pasting their full output would clear it.
[exit 0]

$ grep -F '[2026-11-05T23:50:09Z] WHO: amear' DECISION_LOG.md | grep -c -F 'Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands.'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | grep -c -F '**Typed ruling 1** — RULED'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '947p' | grep -c -F "We're just gonna proceed without that [historical tick data]."
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '58p' | grep -c -F 'SPECIFIED. No numeric threshold exists anywhere'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '58p' | grep -c -F 'An account-state feed from NT8 to Redis (unbuilt)'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '58p' | grep -c -F 'EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '58p' | grep -c -F 'resting stops on every live position'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '31p' | grep -c -F 'Revisit if a personal account is used.'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '814p' | grep -c -F 'Revisit if a personal account is used.'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '806p;811p' | grep -c -F 'REPORTED BY the voice agent'
2
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '2586p' | grep -c -F 'Process instructions'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '2591p' | grep -c -F '(a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48).'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '2595p' | grep -c -F 'a multiple of the cost of a trade'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '970p' | grep -c -F 'The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '970p' | grep -c -F 'NEEDS AMEAR'
1
[exit 0]

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '54p' | grep -c -F 'a stop-market entry with a bracket (stop-loss + take-profit)'
1
[exit 0]

$ sed -n '35p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F 'confirmed'
1
[exit 0]

$ sed -n '38p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F "I can't set a number right now"
1
[exit 0]

$ sed -n '59p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F '(personal account, $10,000)'
0
[exit 1]

$ sed -n '92p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F "Then that's not compatible."
1
[exit 0]

$ sed -n '92p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F 'On the design having no known max loss:'
1
[exit 0]

$ sed -n '110p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F "I don't fucking give a shit, to be honest."
1
[exit 0]

$ sed -n '115p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F '1-minute bars cannot show where a real fill would have landed'
1
[exit 0]

$ sed -n '118p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F 'MFFU email: hand to the master'
1
[exit 0]

$ sed -n '48p' docs/reports/2026-11-15-voice-brief-open-questions.md | grep -c -F 'Options: A. Resume both. B. Resume the skill only. C. Leave both parked.'
1
[exit 0]

$ sed -n '49p' docs/reports/2026-11-15-voice-brief-open-questions.md | grep -c -F 'the skill fix is paperwork only'
1
[exit 0]

$ sed -n '15p' docs/reports/2026-11-15-voice-brief-open-questions.md | grep -c -F 'spending money'
1
[exit 0]

$ grep -F '[2026-11-15T14:37:18Z]' DECISION_LOG.md | grep -c -F "If a source spec has no stop, don't decide anything: bring it back to me."
1
[exit 0]

$ grep -F '[2026-11-15T14:37:18Z]' DECISION_LOG.md | grep -c -F 'sitting at the broker and placed at entry'
1
[exit 0]

$ grep -c -F 'revised a third time 2026-11-15T15:31:08Z' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
1
[exit 0]

~~~~

### Run 2: final checks, after fix script 2

Output, untrimmed:
~~~~
$ sed -n '63p' docs/reports/2026-11-15-voice-notes-open-questions.md
So prop firms stay out for now. Account size: **"Uh, I don't know, let's do 10 grand, I guess."** (personal account, $10,000)
[exit 0]

$ sed -n '63p' docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F '(personal account, $10,000)'
1
[exit 0]

$ git show HEAD:DECISIONS.md | sed -n '970p' | grep -c -F 'The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear'
1
[exit 0]

$ grep -c -F "notes :59" /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
0
[exit 1]

$ grep -c -F "personal per the channel's parenthetical, notes :63" /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
2
[exit 0]

$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/mgr/qcheck.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md docs/reports/2026-11-15-voice-notes-open-questions.md DECISION_LOG.md
block  1 entry :9-:11  sed -n '12,14p'              IDENTICAL
block  2 entry :15-:17  sed -n '16,17p;19p'          IDENTICAL
block  3 entry :23-:25  sed -n '23,25p'              IDENTICAL
block  4 entry :31-:34  sed -n '29p;31,33p'          IDENTICAL
block  5 entry :40-:42  sed -n '37,38p;40p'          IDENTICAL
block  6 entry :48-:50  sed -n '44,45p;47p'          IDENTICAL
block  7 entry :56-:57  sed -n '51p;53p'             IDENTICAL
block  8 entry :63-:67  sed -n '57p;59p;61p;63,64p'  IDENTICAL
block  9 entry :75-:79  sed -n '69,73p'              IDENTICAL
block 10 entry :85-:85  sed -n '75p'                 IDENTICAL
block 11 entry :91-:92  sed -n '77,78p'              IDENTICAL
block 12 entry :98-:99  sed -n '81,82p'              IDENTICAL
block 13 entry :105-:105  sed -n '86p'                 IDENTICAL
block 14 entry :109-:109  sed -n '88p'                 IDENTICAL
block 15 entry :113-:115  sed -n '91,93p'              IDENTICAL
block 16 entry :119-:119  sed -n '95p'                 IDENTICAL
block 17 entry :125-:125  sed -n '106p'                IDENTICAL
block 18 entry :131-:131  T1 row extraction            IDENTICAL
block 19 entry :145-:146  sed -n '110,111p'            IDENTICAL
block 20 entry :154-:154  sed -n '120p'                IDENTICAL
blocks 20, differ 0
[exit 0]

$ tr -cd '\100' < /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md | wc -c
       0
[exit 0]

$ grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
1
[exit 0]

$ tail -1 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
[exit 0]

$ wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
     196 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
[exit 0]

$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
ba25de69adbefae5d88494c8c45c202bafc91114b231ac737d6e5c81ee166392  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
[exit 0]

$ grep -c -F 'is built with' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
0
[exit 1]

$ grep -n -o -F 'personal' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
61:personal
61:personal
66:personal
69:personal
170:personal
183:personal
184:personal
184:personal
[exit 0]

$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v3.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md | wc -l
      54
[exit 0]

~~~~

### Run 3: the whole diff, frozen v3 against the fixed entry

The diff is 57 lines including the runner's command and exit lines, so I did not split it. Output, untrimmed:
~~~~
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v3.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry.md
3c3
< **Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, unchanged, filed with this entry at the master's dispatch of this unit; row 14:38:00Z names only the notes and the typed ruling for filing ("files the notes plus the 14:37:18Z typed ruling"), and row 13:30:00Z says "No commit this act; the brief stays in the working tree for the next flush."; that difference is named, not resolved) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
---
> **Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, unchanged, filed with this entry at the master's direction in its dispatch to this unit's manager, which no ledger row records; row 14:38:00Z names only the notes and the typed ruling for filing ("files the notes plus the 14:37:18Z typed ruling"), and row 13:30:00Z says "No commit this act; the brief stays in the working tree for the next flush."; that difference is named, not resolved) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
44c44
< Filer's reading: Q1 of D-2026-11-14-B is answered as wait-for-data. No daily-loss figure is set; he says it depends on a strategy proven with the broker he goes with. On order type, his "Okay, then that's what we use." answers the explanation of a stop-market order. The channel reads this as "stop-market order, sitting at the broker, placed at entry" (notes :40). The ruling sits in notes section 4, headed for the daily-loss cap (notes :35), and :37 speaks of "a stop limit set order at a level". Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick. T1 uses the same "stop-market order, sitting at the broker and placed at entry" wording for the retest stop; that is named, not read as settling it.
---
> Filer's reading: the filer reads Q1 of D-2026-11-14-B as answered wait-for-data; "confirmed" is the channel's heading (notes :35), not his word. His words reject a number now ("I can't set a number right now", notes :38) and do not address Q1's other form, "a multiple of the cost of a trade" (DECISIONS.md :2595 at HEAD). No daily-loss figure is set; he says it depends on a strategy proven with the broker he goes with. On order type, his "Okay, then that's what we use." answers the explanation of a stop-market order. The channel reads this as "stop-market order, sitting at the broker, placed at entry" (notes :40). The ruling sits in notes section 4, headed for the daily-loss cap (notes :35), and :37 speaks of "a stop limit set order at a level". Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick. T1 uses the same "stop-market order, sitting at the broker and placed at entry" wording for the retest stop; that is named, not read as settling it.
61c61
< **R7 — Q4, the target account: prop firms stay out; $10,000 personal account; the MFFU follow-up is still worth chasing (notes section 7, W1).** Notes :57, :59, :61 and :63-:64 (`sed -n '57p;59p;61p;63,64p'`; :59's lead-in, "So prop firms stay out for now.", "Account size:", the parenthetical "(personal account, $10,000)", the "MFFU written-confirmation follow-up:" lead-in and "See section 12: MFFU had already answered." are the channel's):
---
> **R7 — Q4, the target account: prop firms stay out; $10,000 account (personal per the channel's parenthetical, notes :63); the MFFU follow-up is still worth chasing (notes section 7, W1).** Notes :57, :59, :61 and :63-:64 (`sed -n '57p;59p;61p;63,64p'`; :59's lead-in, "So prop firms stay out for now.", "Account size:", the parenthetical "(personal account, $10,000)", the "MFFU written-confirmation follow-up:" lead-in and "See section 12: MFFU had already answered." are the channel's):
121c121
< Filer's reading: the channel reads "they should all be" as retested, and flags it AMBIGUOUS (notes :88). Amear asked, as a question, whether the strategies should be specced from their source and retested with stop losses (notes :91, "And by the way, that's a question."). He said a design with no known maximum loss is "not compatible". He said yes to the voice agent's proposal to keep the strategy's exit, add a hard stop-market order at entry, and retest (notes :93). Noise-Area goes first. His words are "I'm I'm looking for steady first." (notes :95). That it names Flat1559 is the voice agent's mapping, and the version is open (item (a) below). His typed ruling T1, below, refines this section. Where the two differ, the differences are named after T1.
---
> Filer's reading: the channel reads "they should all be" as retested, and flags it AMBIGUOUS (notes :88). Amear asked, as a question, whether the strategies should be specced from their source and retested with stop losses (notes :91, "And by the way, that's a question."). His words are "Then that's not compatible." (notes :92); that "that" is a design with no known maximum loss comes from the channel's lead-in on notes :92 ("On the design having no known max loss:"). He said yes to the voice agent's proposal to keep the strategy's exit, add a hard stop-market order at entry, and retest (notes :93). Noise-Area goes first. His words are "I'm I'm looking for steady first." (notes :95). That it names Flat1559 is the voice agent's mapping, and the version is open (item (a) below). His typed ruling T1, below, refines this section. Where the two differ, the differences are named after T1.
148c148
< Filer's reading: on the voice-brief skill (`Praxis_build-61o`), his words are "I don't fucking give a shit, to be honest." (notes :110). "No word to resume, so it **stays parked**." is the channel's text (notes :110), not his ruling. As a fact of the record: no resume word of his is recorded, and the brief says "The park rule says a person resumes it." (brief :46), so the park rule's default holds and the bead is as it was. That fact does not answer the brief's options (brief :48), which also turn on the gap fade. On the gap fade (`Praxis_build-vn4`), told it gets retested with a real stop after Noise-Area under Q6, he said "Okay." (notes :111); "No separate ruling." is the channel's (notes :111). The brief asked "Two parked items: pick them up, or leave them?" (brief :44), said of the gap fade "Q6 may settle it." (brief :47), and gave "Options: A. Resume both. B. Resume the skill only. C. Leave both parked." (brief :48). His "Okay." can be read as option C, left parked until Noise-Area is done, or as a resume with the gap fade queued after Noise-Area; the filer does not pick (item (n) below). Under T1, whether and how it is retested depends on its source spec (D5 above). No bead is changed.
---
> Filer's reading: on the voice-brief skill (`Praxis_build-61o`), his words are "I don't fucking give a shit, to be honest." (notes :110). "No word to resume, so it **stays parked**." is the channel's text (notes :110), not his ruling. As a fact of the record: no resume word of his is recorded, and the brief says "The park rule says a person resumes it." (brief :46), so the park rule's default holds and the bead is as it was. That fact does not answer the brief's options (brief :48), which also turn on the gap fade (item (p) below). On the gap fade (`Praxis_build-vn4`), told it gets retested with a real stop after Noise-Area under Q6, he said "Okay." (notes :111); "No separate ruling." is the channel's (notes :111). The brief asked "Two parked items: pick them up, or leave them?" (brief :44), said of the gap fade "Q6 may settle it." (brief :47), and gave "Options: A. Resume both. B. Resume the skill only. C. Leave both parked." (brief :48). His "Okay." can be read as option C, left parked until Noise-Area is done, or as a resume with the gap fade queued after Noise-Area; the filer does not pick (item (n) below). Under T1, whether and how it is retested depends on its source spec (D5 above). No bead is changed.
152c152
< **R12 — The MFFU email: hand it to the master (notes section 12, W2).** Notes :120 (`sed -n '120p'`):
---
> **R12 — The MFFU email: hand it to the master (notes section 12, W2; "MFFU email" as the referent is the channel's heading, notes :118, and the filer's reading below).** Notes :120 (`sed -n '120p'`):
170,171c170,171
< - (j) (the filer's addition) Which drawdown gate applies to a $10,000 personal account (R7). The A4 gate, contender bar item 3 and the walk-forward gate base are all stated against MFFU (S6 below). Answer: NONE.
< - (k) (the filer's addition) Where the real MNQ data for R2 comes from, and whether testing on it is a purchase or a build. No source is named in the notes. Answer: NONE.
---
> - (j) (the filer's addition) Which drawdown gate applies to a $10,000 account (R7; personal per the channel's parenthetical, notes :63). The A4 gate, contender bar item 3 and the walk-forward gate base are all stated against MFFU (S6 below). Answer: NONE.
> - (k) (the filer's addition) Where the real MNQ data for R2 comes from, and whether testing on it is a purchase or a build. No source is named in the notes. His typed ruling 1 (`2026-11-05T23:50:09Z`; walk-forward spec :36 at HEAD) says "No tick purchase. R-VN4-7 stands.", and R-VN4-7 (DECISIONS.md :947 at HEAD) carries "We're just gonna proceed without that [historical tick data]." R5 bears on it too (S6 below, walk-forward spec). Whether real MNQ data must be tick data is not said. Spending money waits for Amear's explicit word (brief :15). Answer: NONE.
175a176
> - (p) (the filer's addition) Whether his "I don't fucking give a shit, to be honest." (notes :110), on the voice-brief skill (`Praxis_build-61o`), leaves it parked, or leaves the pick to the master among the brief's options (brief :48, "Options: A. Resume both. B. Resume the skill only. C. Leave both parked."; the master's view at brief :49 is "the skill fix is paperwork only"). Until a person resumes it, the park rule's default holds (R10 above). Answer: NONE.
178c179
< - D-2026-11-14-B (DECISIONS.md :2527-:2615 at HEAD). These rulings respond to its Q1-Q6 (:2595-:2600): Q1 by this entry's R4, Q2 by this entry's R5, Q3 by this entry's R6, Q4 by this entry's R7, Q5 by this entry's R8, and Q6 by this entry's R9 and T1. Q6's reading stays open ((b), (f)). That entry is not edited. D-2026-11-14-B R1 (:2533, the noon search loop held) bears on this entry's R3 (the loop stays paused). D-2026-11-14-B R2 (:2540, prop firms set aside for now) is kept by this entry's R7. D-2026-11-14-B R3 (heading :2546; the filer's reading at :2553) leaves the percentage TBD; this entry's R6 answers which balance it uses, and whether 1% is set is open (g). D-2026-11-14-B R4 (:2555, the recheck of the tested strategies against D-2026-11-14-B R3): its filer's reading says "What follows from it is Q6." (:2560), and T1 is his typed Q6 ruling. D-2026-11-14-B R5 and R6 (:2562, options C and D accepted: a quick Python screen on the Mac with NinjaTrader kept for finalists, and a lighter evidence standard for research screens) bear on how T1's retest runs, which is not said. D-2026-11-14-B R7 (:2572, the max-trades number comes from backtest data) is untouched. D-2026-11-14-B R8 (:2580, the daily-loss cap waits for data) is confirmed by this entry's R4. Named, not resolved. Not amended.
---
> - D-2026-11-14-B (DECISIONS.md :2527-:2615 at HEAD). These rulings respond to its Q1-Q6 (:2595-:2600): Q1 by this entry's R4, Q2 by this entry's R5, Q3 by this entry's R6, Q4 by this entry's R7, Q5 by this entry's R8, and Q6 by this entry's R9 and T1. Q6's reading stays open ((b), (f)). That entry is not edited. D-2026-11-14-B R1 (:2533, the noon search loop held) bears on this entry's R3 (the loop stays paused). D-2026-11-14-B R2 (:2540, prop firms set aside for now) is kept by this entry's R7. D-2026-11-14-B R3 (heading :2546; the filer's reading at :2553) leaves the percentage TBD; this entry's R6 answers which balance it uses, and whether 1% is set is open (g). D-2026-11-14-B R4 (:2555, the recheck of the tested strategies against D-2026-11-14-B R3): its filer's reading says "What follows from it is Q6." (:2560), and T1 is his typed Q6 ruling. D-2026-11-14-B R5 and R6 (:2562, options C and D accepted: a quick Python screen on the Mac with NinjaTrader kept for finalists, and a lighter evidence standard for research screens) bear on how T1's retest runs, which is not said. D-2026-11-14-B R7 (:2572, the max-trades number comes from backtest data) is untouched. D-2026-11-14-B R8 (:2580, the daily-loss cap waits for data) is, on the filer's reading, kept by this entry's R4; "confirmed" is the channel's heading (notes :35), and his words reject a number now but do not address Q1's "a multiple of the cost of a trade" form (:2595). D-2026-11-14-B R9 (:2586, "Process instructions"; its filer's reading at :2591: "(a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48).") bears on this entry's R10 (the voice-brief skill `Praxis_build-61o` stays parked by the park rule's default; item (p)) and on T1's "If a source spec has no stop, don't decide anything: bring it back to me." Named, not resolved. Not amended.
181,184c182,185
< - R-VN4-6 fee record (DECISIONS.md :970 at HEAD): MFFU's page gives NQ $4.68 round trip (MNQ $1.90), and the cost model stays $2.96. R2 calls for testing on real MNQ data, while bar item 2's $4.68 (:2481) is the NQ figure. Which commission an MNQ run uses is not said. Named, not resolved. Not amended.
< - The A4 drawdown gate (DECISIONS.md :1735-:1740 at HEAD) is set as a share of the MFFU account size and MFFU's trailing limit. R7 (a $10,000 personal account) and R8(c) (a 5% placeholder kill switch) bear on it. Not amended.
< - Walk-forward spec (`docs/specs/2026-11-05-walk-forward-spec.md`, HEAD text; the file is modified in the working tree and that text is not used). The gate base and the per-window drawdown are stated against MFFU (:31-:32; :31 says "Revisit if a personal account is used."), which R7 bears on. Arm (b)'s stop is "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (:36, quoted again at :74, where it is marked "(typed ruling 1). — RULED."). These are Amear's typed words, not spec text only: D-2026-11-05-C records them as "Ruling 1 (`2026-11-05T23:50:09Z`, typed)" (DECISIONS.md :907 at HEAD). The R-VN4-2 they cite reads "Until the account is live … resting stops." (DECISIONS.md :936 at HEAD), REPORTED BY the voice agent (:908); the reading "Bar-close checks (market-order flatten) in the backtest; resting stop orders once live." is the voice agent's (:937). T1 calls for "a proper stop-market order, sitting at the broker and placed at entry, so the maximum loss is known before the trade" and says "No loose or interval-checked exits." Ruling 1 says the backtest stop is evaluated on bar close and is not a resting stop; T1's retest stop sits at the broker. That conflict between two typed rulings of his is named, not resolved; which governs is Amear's (item (o)). R4 bears on arm (b)'s stop only if his "Okay, then that's what we use." covers the per-trade stop (open (m)); the filer does not pick. The same :36 ends "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands." R5 counts slippage past the stop in the cost of the trade once it is measured by enough testing, and the channel's check (notes :115) says "1-minute bars cannot show where a real fill would have landed". Named, not resolved. Arm (a) runs with no added stop (:67, marked INFERRED there). Not amended.
< - Live-signal topology (`docs/specs/2026-11-10-live-signal-topology.md` :58 at HEAD). Breaker #1's "cancel all, flatten" action is built with "resting stops on every live position", citing R-VN4-2 as "Until the account is live … resting stops.", and marks the reading "resting stops once live" as the voice agent's. Ruling 1 (DECISIONS.md :907) cites the same R-VN4-2. T1's stop at the broker, placed at entry, in a retest, bears on that split between backtest and live (item (o)). If his "Okay, then that's what we use." covers the daily-loss cap (open (m)), R4 bears on breaker #1 here too. Named, not resolved. Not amended.
---
> - R-VN4-6 fee record (DECISIONS.md :970 at HEAD): MFFU's page gives NQ $4.68 round trip (MNQ $1.90), and "The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear" (:970, which marks the fee report "NEEDS AMEAR"). R2 calls for testing on real MNQ data, while bar item 2's $4.68 (:2481) is the NQ figure. Which commission an MNQ run uses is not said. Named, not resolved. Not amended.
> - The A4 drawdown gate (DECISIONS.md :1735-:1740 at HEAD) is set as a share of the MFFU account size and MFFU's trailing limit. R7 (a $10,000 account, personal per the channel's parenthetical) and R8(c) (a 5% placeholder kill switch) bear on it. Not amended.
> - Walk-forward spec (`docs/specs/2026-11-05-walk-forward-spec.md`, HEAD text; the file is modified in the working tree and that text is not used). The gate base and the per-window drawdown are stated against MFFU (:31-:32). :31 quotes D-2026-11-05-A item 3, a ruled item (heading DECISIONS.md :803 at HEAD; item 3 at :814), which that entry marks REPORTED BY the voice agent (:806, :811); its words include "Revisit if a personal account is used." R7 bears on it: R7's $10,000 account (personal per the channel's parenthetical) may meet that revisit clause. Named, not resolved. Arm (b)'s stop is "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (:36, quoted again at :74, where it is marked "(typed ruling 1). — RULED."). All of :36, headed "**Typed ruling 1** — RULED" at :35, is Amear's typed ruling 1 (DECISION_LOG row `2026-11-05T23:50:09Z`, WHO: amear, typed), not only these two sentences and not spec text only: D-2026-11-05-C records it as "Ruling 1 (`2026-11-05T23:50:09Z`, typed)" (DECISIONS.md :907 at HEAD). The R-VN4-2 they cite reads "Until the account is live … resting stops." (DECISIONS.md :936 at HEAD), REPORTED BY the voice agent (:908); the reading "Bar-close checks (market-order flatten) in the backtest; resting stop orders once live." is the voice agent's (:937). T1 calls for "a proper stop-market order, sitting at the broker and placed at entry, so the maximum loss is known before the trade" and says "No loose or interval-checked exits." Ruling 1 says the backtest stop is evaluated on bar close and is not a resting stop; T1's retest stop sits at the broker. That conflict between two typed rulings of his is named, not resolved; which governs is Amear's (item (o)). R4 bears on arm (b)'s stop only if his "Okay, then that's what we use." covers the per-trade stop (open (m)); the filer does not pick. The same :36, still his typed ruling 1, ends "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands." R-VN4-7 (DECISIONS.md :947 at HEAD) carries "We're just gonna proceed without that [historical tick data]." R2 (test the single candidate on real MNQ data), open item (k) (whether that testing is "a purchase or a build") and R5 (slippage past the stop counted in the cost of the trade once it is measured by enough testing, where the channel's check, notes :115, says "1-minute bars cannot show where a real fill would have landed") bear on "No tick purchase" and on R-VN4-7. Whether real MNQ data must be tick data is not said in the notes, in T1, in ruling 1 or in R-VN4-7. Spending money waits for Amear's explicit word (brief :15). Named, not resolved. Arm (a) runs with no added stop (:67, marked INFERRED there). Not amended.
> - Live-signal topology (`docs/specs/2026-11-10-live-signal-topology.md` :58 at HEAD). Breaker #1's "cancel all, flatten" action is specified with "resting stops on every live position", citing R-VN4-2 as "Until the account is live … resting stops.", and marks the reading "resting stops once live" as the voice agent's. The row's status is "SPECIFIED. No numeric threshold exists anywhere" (:58), and the pieces it depends on are marked unbuilt in the same row: "An account-state feed from NT8 to Redis (unbuilt)" and "EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt". Ruling 1 (DECISIONS.md :907) cites the same R-VN4-2. T1's stop at the broker, placed at entry, in a retest, bears on that split between backtest and live (item (o)). If his "Okay, then that's what we use." covers the daily-loss cap (open (m)), R4 bears on breaker #1 here too. Named, not resolved. Not amended.
186c187
< - Phase 3 spec (`docs/specs/2026-11-05-phase3-build-specification.md`, HEAD). Block 1 names a bracket "stop-loss + take-profit" with no sizing rule (:54). Block 2 takes historical data over the MFFU connection, "through Rithmic" (:64), and its backtest runs at "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract" (:76). R2 (real MNQ data, where :76 names NQ), R5 (stop slippage counted in the cost of the trade, where :76 names slippage on entries) and R7 (prop firms out, where :64 routes the data through the MFFU connection) bear on these. Named, not resolved. Breaker #1, daily loss (:97): R4 sets no value. Breaker #1 is a software action, "cancel all, flatten, disable for session" (:97), not a resting broker order. If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved. Breaker #2, max trades (:98): untouched. Breaker #3, "2 consecutive losers in one session → identical to max trades" (:99): R8(d)'s variable sets risk at 0.5% after two losses (notes :81). Whether trading continues within the same session after two losses is not said in his words. The tension with breaker #3 (:99) is named, not resolved; R8(d) is a variable to test, not a rule. Breaker #4 (imported :100, amended to a 16:00 ET session flat at :208-:212): R8(b) says the hard stop time depends on the strategy. Breaker #5, the afternoon session window (:101), is a fixed clock window; R8(b) bears on it the same way. Breaker #6, trailing drawdown proximity to "MFFU’s $1,500 EOD trailing drawdown" (:102), and the kill criterion "Account drawdown exceeds 60% of MFFU trailing DD room" (:145): R7 and R8(c) bear on both. Sizing: stages A and B size by a fixed contract (:138-:139), and stage C sizes at "0.5% per trade" (:140). R6's current balance and the 1% in his words (open (g)) bear on :140. Breaker #7, max position size (:103), rejects a quantity above plan; R6's current-balance sizing and R8(d)'s 1% to 0.5% variable change the quantity per trade, so what the plan is under them is not said. Named, not resolved. The Block 2 gate "Max drawdown ≤ 4% of equity" (:82) is as above. No breaker value is changed. All nine breakers stay SPECIFIED ONLY (:11). Not amended.
---
> - Phase 3 spec (`docs/specs/2026-11-05-phase3-build-specification.md`, HEAD). Block 1 names "a stop-market entry with a bracket (stop-loss + take-profit)" with no sizing rule (:54). That bracket stop bears on T1's stop "sitting at the broker and placed at entry" and on item (o) (ruling 1's "Not a resting stop in the backtest."). Named, not resolved. Block 2 takes historical data over the MFFU connection, "through Rithmic" (:64), and its backtest runs at "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract" (:76). R2 (real MNQ data, where :76 names NQ), R5 (stop slippage counted in the cost of the trade, where :76 names slippage on entries) and R7 (prop firms out, where :64 routes the data through the MFFU connection) bear on these. Named, not resolved. Breaker #1, daily loss (:97): R4 sets no value. Breaker #1 is a software action, "cancel all, flatten, disable for session" (:97), not a resting broker order. If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved. Breaker #2, max trades (:98): untouched. Breaker #3, "2 consecutive losers in one session → identical to max trades" (:99): R8(d)'s variable sets risk at 0.5% after two losses (notes :81). Whether trading continues within the same session after two losses is not said in his words. The tension with breaker #3 (:99) is named, not resolved; R8(d) is a variable to test, not a rule. Breaker #4 (imported :100, amended to a 16:00 ET session flat at :208-:212): R8(b) says the hard stop time depends on the strategy. Breaker #5, the afternoon session window (:101), is a fixed clock window; R8(b) bears on it the same way. Breaker #6, trailing drawdown proximity to "MFFU’s $1,500 EOD trailing drawdown" (:102), and the kill criterion "Account drawdown exceeds 60% of MFFU trailing DD room" (:145): R7 and R8(c) bear on both. Sizing: stages A and B size by a fixed contract (:138-:139), and stage C sizes at "0.5% per trade" (:140). R6's current balance and the 1% in his words (open (g)) bear on :140. Breaker #7, max position size (:103), rejects a quantity above plan; R6's current-balance sizing and R8(d)'s 1% to 0.5% variable change the quantity per trade, so what the plan is under them is not said. Named, not resolved. The Block 2 gate "Max drawdown ≤ 4% of equity" (:82) is as above. No breaker value is changed. All nine breakers stay SPECIFIED ONLY (:11). Not amended.
193c194
< **S4 timing.** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, before any act under these rulings. In DECISION_LOG.md the 2026-11-15 rows are 13:30:00Z (the master's inbox check and voice brief), 14:37:18Z (T1) and 14:38:00Z (intake and dispatch of this unit). No row follows 14:38:00Z. No retest, paper read, loop restart, question set, bead change or breaker change appears in the ledger. The paper read is held until this entry is committed (row 14:38:00Z). Chain: Amear (voice call, notes :4) → the notes, written by the Claude.ai Praxis project channel (notes :3) → DECISION_LOG 2026-11-15T14:37:18Z (WHO: amear, typed) → 2026-11-15T14:38:00Z (master intake and dispatch). Observed in the rows, not fixed: row 14:38:00Z carries "WHEN: `date -u` 14:37:18Z", which does not match its own timestamp and equals the previous row's. Row 13:30:00Z carries "WHEN: `date -u` 13:25:51Z". Row 14:37:18Z's WHEN matches its timestamp. Row 14:38:00Z names the reporter as "the voice channel"; this entry uses "the Claude.ai Praxis project channel", the notes' own name for it (notes :3). Also observed, not fixed: the working-tree DECISIONS.md carries an uncommitted entry whose heading names D-2026-11-12-B (working-tree :2280; not at HEAD), so working-tree line numbers after it differ from HEAD's. All DECISIONS.md line numbers in this entry are HEAD's.
---
> **S4 timing.** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, revised a third time 2026-11-15T15:31:08Z, before any act under these rulings. In DECISION_LOG.md the 2026-11-15 rows are 13:30:00Z (the master's inbox check and voice brief), 14:37:18Z (T1) and 14:38:00Z (intake and dispatch of this unit). No row follows 14:38:00Z. No retest, paper read, loop restart, question set, bead change or breaker change appears in the ledger. The paper read is held until this entry is committed (row 14:38:00Z). Chain: Amear (voice call, notes :4) → the notes, written by the Claude.ai Praxis project channel (notes :3) → DECISION_LOG 2026-11-15T14:37:18Z (WHO: amear, typed) → 2026-11-15T14:38:00Z (master intake and dispatch). Observed in the rows, not fixed: row 14:38:00Z carries "WHEN: `date -u` 14:37:18Z", which does not match its own timestamp and equals the previous row's. Row 13:30:00Z carries "WHEN: `date -u` 13:25:51Z". Row 14:37:18Z's WHEN matches its timestamp. Row 14:38:00Z names the reporter as "the voice channel"; this entry uses "the Claude.ai Praxis project channel", the notes' own name for it (notes :3). Also observed, not fixed: the working-tree DECISIONS.md carries an uncommitted entry whose heading names D-2026-11-12-B (working-tree :2280; not at HEAD), so working-tree line numbers after it differ from HEAD's. All DECISIONS.md line numbers in this entry are HEAD's.
[exit 1]

~~~~

## Result: PASS

- qcheck: 20 of 20 fenced blocks IDENTICAL.
- Zero at-signs.
- The S13 sentence appears exactly once, and it is the last line.
- `is built with` appears 0 times.
- Final file: 196 lines, sha256 ba25de69adbefae5d88494c8c45c202bafc91114b231ac737d6e5c81ee166392.
- All eleven findings are fixed. Every new inline quote is checked with `grep -c -F` against its source. Each check prints 1, except the REPORTED BY check, which prints 2 because it spans the two lines :806 and :811.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
