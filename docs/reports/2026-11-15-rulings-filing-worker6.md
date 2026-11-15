# 2026-11-15 rulings filing: worker 6 (ADVERSARIAL review of entry v3)

## Task

Unit `2026-11-15-rulings-filing`. Try to break the draft DECISIONS.md entry D-2026-11-15-A, version 3 (`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md`, 195 lines, sha256 `114c05a60bf6d0b678ed831fac3ee9a23261786da4bcb6d051038c40a752e606`, checked in command 01). Part 1: mark each of the 19 earlier findings (worker 2 items 1-9, worker 4 new items 1-10) CLOSED or OPEN in v3. Part 2: attack v3 from scratch, with most weight on the text added in this revision. Criteria: rubric S2, S5, S6, S8, S13, and unit requirements 1-7. Working directory `/Volumes/Sensidine/Praxis.build`, HEAD `d9fc5f0`. Read-only. The only file written is this report. No git index was touched, nothing was committed, and nothing was staged.

## Mode: ADVERSARIAL

I was given the artifact and the criteria, not the reasoning behind them. I did not edit the artifact.

## Commands and output

Every command below ran through one bash runner (`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w6/run.sh`). The runner prints each command line as given, then the output of `bash -c` on it, unchanged. Its full text:

~~~~
#!/bin/bash
n=0
while IFS= read -r c; do n=$((n+1)); printf '### Command %02d\n\n~~~~\n$ %s\n' "$n" "$c"; bash -c "$c" 2>&1; printf '~~~~\n\n'; done < "$1"
~~~~

Masking: one HEAD line (ruleset :59) contains an at-sign. Command 12 masks it inside the pasted command with `sed -e 's/\x40/<AT-MASKED>/g'`. Nothing else is masked. Command 04 prints the quote-checker script that command 05 runs. In command 05, the one NOT-FOUND row (entry :129) is a false positive: the "quote" it matched is a piece of the extraction command that entry :129 cites, not a quoted string.

### Command 01

~~~~
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse --short HEAD && shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md docs/reports/2026-11-15-voice-brief-open-questions.md && wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md docs/reports/2026-11-15-voice-notes-open-questions.md
d9fc5f0
114c05a60bf6d0b678ed831fac3ee9a23261786da4bcb6d051038c40a752e606  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md
87aff631ed033adac2e23b0636c3e77ea51a05b82b9b71447925236ad68c683a  docs/reports/2026-11-15-voice-brief-open-questions.md
     195 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md
     131 docs/reports/2026-11-15-voice-notes-open-questions.md
     326 total
~~~~

### Command 02

~~~~
$ cd /Volumes/Sensidine/Praxis.build && W=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w6/e2 && mkdir -p $W && awk -v d=$W '/^```text$/{n++; f=sprintf("%s/blk%02d.txt",d,n); inb=1; next} /^```$/{inb=0; next} inb{print > f}' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md && i=0 && for spec in '12,14p' '16,17p;19p' '23,25p' '29p;31,33p' '37,38p;40p' '44,45p;47p' '51p;53p' '57p;59p;61p;63,64p' '69,73p' '75p' '77,78p' '81,82p' '86p' '88p' '91,93p' '95p' '106p' T1 '110,111p' '120p'; do i=$((i+1)); b=$(printf '%s/blk%02d.txt' $W $i); if [ "$spec" = T1 ]; then grep -F '[2026-11-15T14:37:18Z]' DECISION_LOG.md | sed -e 's/.*Verbatim: "//' -e 's/" Left unanswered by him.*//' > $W/src$i.txt; else sed -n "$spec" docs/reports/2026-11-15-voice-notes-open-questions.md > $W/src$i.txt; fi; if cmp -s $b $W/src$i.txt; then r=IDENTICAL; else r=DIFFER; fi; printf 'block %02d spec %-22s %s\n' $i "$spec" $r; done; ls $W | grep -c '^blk'
block 01 spec 12,14p                 IDENTICAL
block 02 spec 16,17p;19p             IDENTICAL
block 03 spec 23,25p                 IDENTICAL
block 04 spec 29p;31,33p             IDENTICAL
block 05 spec 37,38p;40p             IDENTICAL
block 06 spec 44,45p;47p             IDENTICAL
block 07 spec 51p;53p                IDENTICAL
block 08 spec 57p;59p;61p;63,64p     IDENTICAL
block 09 spec 69,73p                 IDENTICAL
block 10 spec 75p                    IDENTICAL
block 11 spec 77,78p                 IDENTICAL
block 12 spec 81,82p                 IDENTICAL
block 13 spec 86p                    IDENTICAL
block 14 spec 88p                    IDENTICAL
block 15 spec 91,93p                 IDENTICAL
block 16 spec 95p                    IDENTICAL
block 17 spec 106p                   IDENTICAL
block 18 spec T1                     IDENTICAL
block 19 spec 110,111p               IDENTICAL
block 20 spec 120p                   IDENTICAL
20
~~~~

### Command 03

~~~~
$ grep -n -F -e "(\`sed -n '" -e 'Extracted by script' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md | sed -E "s/^([0-9]+):.*(\(\`sed -n '[^']*'\`|Extracted by script).*/\1: \2/"
7: (`sed -n '12,14p'`
13: (`sed -n '16,17p;19p'`
21: (`sed -n '23,25p'`
29: (`sed -n '29p;31,33p'`
38: (`sed -n '37,38p;40p'`
46: (`sed -n '44,45p;47p'`
54: (`sed -n '51p;53p'`
61: (`sed -n '57p;59p;61p;63,64p'`
73: (`sed -n '69,73p'`
83: (`sed -n '75p'`
89: (`sed -n '77,78p'`
96: (`sed -n '81,82p'`
103: (`sed -n '86p'`
107: (`sed -n '88p'`
111: (`sed -n '91,93p'`
117: (`sed -n '95p'`
123: (`sed -n '106p'`
129: Extracted by script
143: (`sed -n '110,111p'`
152: (`sed -n '120p'`
~~~~

### Command 04

~~~~
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w6/q.py
import sys,re,glob,os
S=sys.argv[1]; A=sys.argv[2]
srcs={os.path.basename(f):open(f,encoding='utf-8').read() for f in glob.glob(S+'/head_*')+[S+'/rows.txt',S+'/notes.md',S+'/brief.md']}
inb=False
for n,l in enumerate(open(A,encoding='utf-8'),1):
    if l.startswith('```'):
        inb=not inb if l.strip() in ('```text','```') else inb; continue
    if inb: continue
    for m in re.finditer(r'"([^"]+)"',l):
        q=m.group(1)
        hits=[k for k,v in srcs.items() if q in v]
        if not hits:
            # try ellipsis-free match
            print(f'{n}: NOT-FOUND "{q}"')
        else:
            print(f'{n}: OK [{",".join(sorted(hits))[:80]}] "{q[:70]}"')
~~~~

### Command 05

~~~~
$ cd /Volumes/Sensidine/Praxis.build && S=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w6 && for p in DECISIONS.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-phase3-build-specification.md docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md specs/SPEC_RUBRIC.md docs/reports/2026-11-14-r3-recheck-manager.md; do git show HEAD:$p > $S/head_$(basename $p); done && grep -F -e '[2026-11-15T13:30:00Z]' -e '[2026-11-15T14:37:18Z]' -e '[2026-11-15T14:38:00Z]' DECISION_LOG.md > $S/rows.txt && cp docs/reports/2026-11-15-voice-notes-open-questions.md $S/notes.md && cp docs/reports/2026-11-15-voice-brief-open-questions.md $S/brief.md && python3 -I -B $S/q.py $S /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md | sed -e 's/head_//g'
3: OK [rows.txt] "files the notes plus the 14:37:18Z typed ruling"
3: OK [rows.txt] "No commit this act; the brief stays in the working tree for the next f"
3: OK [notes.md] "Read:"
3: OK [notes.md] "Read:"
3: OK [notes.md] "Okay, then that's what we use."
3: OK [DECISIONS.md,notes.md] "Uh, yeah."
3: OK [notes.md] "Consequence (the agent's reading, not ruled)"
3: OK [notes.md] "this channel's check, not Amear's rulings"
3: OK [notes.md] "As the voice agent read it"
3: OK [DECISIONS.md] "Filer's reading"
13: OK [notes.md] "He settled it for Noise-Area in section 9"
19: OK [notes.md] "in multiple ways"
19: OK [notes.md] "Yeah, one at a time."
19: OK [notes.md] "Best candidate"
19: OK [notes.md] "That's fine. Keep going."
19: OK [notes.md] "I want the uh, you know, the highest return one."
19: OK [notes.md] "I'm I'm looking for steady first."
19: OK [notes.md,rows.txt] "steady first"
19: OK [notes.md,rows.txt] "steady first"
19: OK [notes.md] "I still want the top three"
27: OK [2026-11-14-r3-recheck-manager.md,notes.md] "MNQ derived, not an MNQ run"
29: OK [brief.md,notes.md,rows.txt] "Halt all runs until further notice"
36: OK [notes.md] "exhaustive enough so that this loop can actually be ran um, reliably"
36: OK [notes.md] "Yeah."
38: OK [notes.md] "Read:"
44: OK [notes.md] "Okay, then that's what we use."
44: OK [notes.md] "stop-market order, sitting at the broker, placed at entry"
44: OK [notes.md] "a stop limit set order at a level"
44: OK [notes.md] "Okay, then that's what we use."
44: OK [rows.txt] "stop-market order, sitting at the broker and placed at entry"
46: OK [2026-11-05-walk-forward-spec.md,DECISIONS.md,notes.md] "not ruled"
52: OK [notes.md] "as long as it's predetermined and calculated"
52: OK [2026-11-05-phase3-build-specification.md,notes.md] "calculated"
59: OK [notes.md] "considering"
59: OK [notes.md] "Whatever 1% is right now"
61: OK [notes.md] "So prop firms stay out for now."
61: OK [notes.md] "Account size:"
61: OK [notes.md] "(personal account, $10,000)"
61: OK [notes.md] "MFFU written-confirmation follow-up:"
61: OK [notes.md] "See section 12: MFFU had already answered."
73: OK [notes.md] "Read:"
89: OK [DECISIONS.md,notes.md] "Then:"
94: OK [brief.md,DECISIONS.md,notes.md] "for now"
94: OK [notes.md] "from peak"
94: OK [notes.md] "Fact given in the call"
96: OK [notes.md] "The agent recorded:"
101: OK [notes.md] "I can't set these rules without backtesting"
111: OK [DECISIONS.md,notes.md] "Uh, yeah."
117: OK [notes.md] "Amear did not object."
117: OK [notes.md] "Confirm the version name with him."
121: OK [notes.md] "they should all be"
121: OK [notes.md] "And by the way, that's a question."
121: OK [notes.md] "not compatible"
121: OK [notes.md] "I'm I'm looking for steady first."
127: OK [brief.md,2026-11-05-walk-forward-spec.md,2026-11-06-walk-forward-value] "at 1 MNQ"
127: OK [2026-11-14-r3-recheck-manager.md,notes.md] "MNQ derived, not an MNQ run"
129: OK [2026-07-16-b2-noise-area-ruleset.md,2026-11-06-walk-forward-values.md,] "` and `"
129: NOT-FOUND "//' -e 's/"
129: OK [rows.txt] "the combined reply for option 4"
133: OK [rows.txt] "No loose or interval-checked exits."
133: OK [rows.txt] "Before anything else, confirm from the original paper"
133: OK [rows.txt] "before any retest"
136: OK [DECISIONS.md,notes.md] "Uh, yeah."
136: OK [notes.md] "keep the strategy's exit, add a hard stop-market order at entry"
136: OK [rows.txt] "No loose or interval-checked exits."
136: OK [2026-07-16-b2-noise-area-ruleset.md] "Evaluated only at semi-hourly stamps"
136: OK [2026-07-16-b2-noise-area-ruleset.md] "every `HH:00` / `HH:30`"
136: OK [2026-07-16-b2-noise-area-ruleset.md] "Position closes as soon as price crosses the current band **or** the V"
137: OK [notes.md] "they should all be"
137: OK [rows.txt] "Retest depends on the original source spec"
137: OK [rows.txt] "the source spec has a stop and our test ran without one"
138: OK [rows.txt] "If a source spec has no stop, don't decide anything: bring it back to "
139: OK [notes.md] "maybe test like another candidate that seems promising"
139: OK [rows.txt] "One at a time, Noise-Area first."
139: OK [notes.md] "Yeah, one at a time."
140: OK [2026-11-14-r3-recheck-manager.md,rows.txt] "each of the five"
140: OK [2026-11-14-r3-recheck-manager.md,rows.txt] "For each of the five"
140: OK [brief.md,DECISIONS.md] "already retired"
141: OK [brief.md,2026-07-16-b2-noise-area-ruleset.md,2026-11-05-phase3-build-s] "Noise-Area"
141: OK [notes.md,rows.txt] "steady first"
141: OK [rows.txt] "Left unanswered by him"
143: OK [notes.md] "No word to resume, so it **stays parked**."
143: OK [notes.md] "No separate ruling."
143: OK [DECISIONS.md,notes.md] "Amear said"
148: OK [notes.md] "I don't fucking give a shit, to be honest."
148: OK [notes.md] "No word to resume, so it **stays parked**."
148: OK [brief.md] "The park rule says a person resumes it."
148: OK [notes.md] "Okay."
148: OK [notes.md] "No separate ruling."
148: OK [brief.md] "Two parked items: pick them up, or leave them?"
148: OK [brief.md] "Q6 may settle it."
148: OK [brief.md] "Options: A. Resume both. B. Resume the skill only. C. Leave both parke"
148: OK [notes.md] "Okay."
150: OK [DECISIONS.md,notes.md] "not Amear's rulings"
150: OK [brief.md,2026-11-05-walk-forward-spec.md,2026-11-06-walk-forward-value] "at 1 MNQ"
156: OK [2026-07-16-b2-noise-area-ruleset.md,2026-11-05-walk-forward-spec.md,he] "those"
156: OK [2026-07-16-b2-noise-area-ruleset.md,2026-11-05-walk-forward-spec.md,he] "those"
156: OK [notes.md] "MFFU email: hand to the master"
156: OK [2026-11-05-phase3-build-specification.md,notes.md] "looks like"
161: OK [notes.md,rows.txt] "steady first"
161: OK [rows.txt] "Left unanswered by him"
162: OK [notes.md] "they should all be"
163: OK [rows.txt] "Before anything else, confirm from the original paper"
163: OK [rows.txt] "before any retest"
163: OK [rows.txt] "the Noise-Area paper read that Amear ordered is NOT dispatched until t"
163: OK [rows.txt] "Before anything else"
164: OK [rows.txt] "Left unanswered by him"
168: OK [notes.md] "Read:"
169: OK [notes.md] "I still want the top three"
172: OK [notes.md] "best candidate"
172: OK [notes.md] "the highest return one"
172: OK [notes.md,rows.txt] "steady first"
172: OK [notes.md] "That's fine. Keep going."
173: OK [notes.md] "Okay, then that's what we use."
174: OK [notes.md] "Okay."
175: OK [rows.txt] "a proper stop-market order, sitting at the broker and placed at entry"
175: OK [rows.txt] "No loose or interval-checked exits."
175: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "evaluated on bar close, exit by market order next bar"
175: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "Not a resting stop in the backtest."
178: OK [DECISIONS.md] "What follows from it is Q6."
179: OK [DECISIONS.md] "walk-forward runs on existing strategies"
179: OK [notes.md] "the top three"
180: OK [DECISIONS.md] "the three Noise-Area arms and Last-Half-Hour Momentum"
180: OK [DECISIONS.md] "at 1 MNQ for at least one MFFU account size"
180: OK [DECISIONS.md] "**Overfitting guard (PROPOSED).**"
180: OK [DECISIONS.md] "Allow no more than three parameter variants per idea, and log every va"
180: OK [notes.md] "test it in multiple ways"
183: OK [2026-11-05-walk-forward-spec.md,DECISIONS.md] "Revisit if a personal account is used."
183: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "evaluated on bar close, exit by market order next bar — same rule as t"
183: OK [2026-11-05-walk-forward-spec.md] "(typed ruling 1). — RULED."
183: OK [DECISIONS.md] "Ruling 1 (`2026-11-05T23:50:09Z`, typed)"
183: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "Until the account is live … resting stops."
183: OK [DECISIONS.md] "Bar-close checks (market-order flatten) in the backtest; resting stop "
183: OK [rows.txt] "a proper stop-market order, sitting at the broker and placed at entry,"
183: OK [rows.txt] "No loose or interval-checked exits."
183: OK [notes.md] "Okay, then that's what we use."
183: OK [2026-11-05-walk-forward-spec.md,DECISIONS.md] "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stand"
183: OK [notes.md] "1-minute bars cannot show where a real fill would have landed"
184: OK [2026-11-05-phase3-build-specification.md,2026-11-10-live-signal-topolo] "cancel all, flatten"
184: OK [2026-11-10-live-signal-topology.md] "resting stops on every live position"
184: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "Until the account is live … resting stops."
184: OK [2026-11-05-phase3-build-specification.md,2026-11-10-live-signal-topolo] "resting stops once live"
184: OK [notes.md] "Okay, then that's what we use."
185: OK [2026-11-06-walk-forward-values.md] "none (the paper has no stop; §1)"
185: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "Max drawdown ≤ 4% of equity"
186: OK [2026-11-05-phase3-build-specification.md,DECISIONS.md] "stop-loss + take-profit"
186: OK [2026-11-05-phase3-build-specification.md] "through Rithmic"
186: OK [2026-11-05-phase3-build-specification.md] "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippag"
186: OK [2026-11-05-phase3-build-specification.md] "cancel all, flatten, disable for session"
186: OK [2026-11-05-phase3-build-specification.md,DECISIONS.md] "2 consecutive losers in one session → identical to max trades"
186: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "MFFU’s $1,500 EOD trailing drawdown"
186: OK [2026-11-05-phase3-build-specification.md] "Account drawdown exceeds 60% of MFFU trailing DD room"
186: OK [2026-11-05-phase3-build-specification.md] "0.5% per trade"
186: OK [2026-11-05-phase3-build-specification.md,2026-11-05-walk-forward-spec.] "Max drawdown ≤ 4% of equity"
187: OK [2026-07-16-b2-noise-area-ruleset.md] "Evaluated only at semi-hourly stamps"
187: OK [rows.txt] "Before anything else"
187: OK [rows.txt] "No loose or interval-checked exits."
187: OK [2026-07-16-b2-noise-area-ruleset.md,DECISIONS.md] "as soon as"
189: OK [brief.md,DECISIONS.md,notes.md] "still worth chasing"
193: OK [rows.txt] "WHEN: `date -u` 14:37:18Z"
193: OK [rows.txt] "WHEN: `date -u` 13:25:51Z"
193: OK [rows.txt] "the voice channel"
193: OK [notes.md,rows.txt] "the Claude.ai Praxis project channel"
~~~~

### Command 06

~~~~
$ cd /Volumes/Sensidine/Praxis.build && grep -F -e '[2026-11-15T13:30:00Z]' -e '[2026-11-15T14:37:18Z]' -e '[2026-11-15T14:38:00Z]' DECISION_LOG.md | fold -w 300 && git show HEAD:DECISION_LOG.md | grep -c '2026-11-15T'; tail -n 4 DECISION_LOG.md | sed -E 's/^(- \[[^]]*\] WHO: [a-z-]+).*/\1/'
- [2026-11-15T13:30:00Z] WHO: praxis-master | WHAT: **Amear asked "check the inbox then give me handoff for voice man".** Inbox check, OBSERVED this turn: Gmail connector failed to connect this session (ENOTFOUND), so his mail was not read; Hermes gateway.log has no inbound Telegram message after 20
26-11-13 20:21:51 ("Halt all runs until further notice"); newest `vm/replies/` file 20261111T172940Z; no commit on any branch since 59f5ce4; repo files changed since the park: DISPATCH_LOG.md and .claude/state/handoff-latest.md only. Loop state: `hermes cron list` printed "No scheduled jobs."; `~/.h
ermes/cron/jobs.json` shows praxis-search-loop (73d67fad7ec9) and praxis-build-loop (5be233e3ac6c) enabled False, state paused. Master writes voice brief `docs/reports/2026-11-15-voice-brief-open-questions.md` following the on-disk voice-brief skill (approved by Amear 2026-11-14T16:05:30Z; file park
ed on parked/Praxis_build-61o, not on main; used as a format guide, not claimed installed). Filter: Q1-Q6 of D-2026-11-14-B (rulings left open, HEAD DECISIONS.md :2593-:2600) pass test 3; resuming the search loop passes test 3 (his reserved word, row 2026-11-14T14:49:30Z); resuming parked `61o`/`vn4
` passes as a park-rule human resume (rubric :264-:278). Settled and dropped: "Mac pre-screen acceptable" (HANDOFF :51), settled by R5 (HEAD DECISIONS.md :2562-:2570). No commit this act; the brief stays in the working tree for the next flush. | WHY: Amear's request; R9(a) | WHERE: docs/reports/2026
-11-15-voice-brief-open-questions.md | WHEN: `date -u` 13:25:51Z | HOW: master writes report | STATE: written
- [2026-11-15T14:37:18Z] WHO: amear | WHAT: **Amear's typed Q6 ruling in the master session** (pasted by him as "the combined reply for option 4", after he declined the master's three-question prompt in order to clarify). Verbatim: "Retest depends on the original source spec. For each of the five, g
o back to where the strategy was found and check what it specified. If the source spec has a stop and our test ran without one, retest it and recheck it with a proper stop-market order, sitting at the broker and placed at entry, so the maximum loss is known before the trade. No loose or interval-che
cked exits. One at a time, Noise-Area first. / Before anything else, confirm from the original paper (Zarattini, Aziz and Barbon, "Beat the Market", Swiss Finance Institute 24-97) whether the Noise-Area strategy has a hard stop. The project's research summary says it uses a trailing stop at the band
 or VWAP, checked at set times, which would mean no fixed maximum loss. Report what the paper actually says, with the exact wording, before any retest. If a source spec has no stop, don't decide anything: bring it back to me." Left unanswered by him in this session: whether "steady first" names Flat
1559 (notes :95); how the MFFU email reaches the repo (Gmail connector failed to connect this session; F4 stays FROZEN). | WHY: S5 authorisation record | WHERE: master session | WHEN: `date -u` 14:37:18Z | HOW: typed | STATE: recorded
- [2026-11-15T14:38:00Z] WHO: praxis-master | WHAT: **Intake of `docs/reports/2026-11-15-voice-notes-open-questions.md` (128 lines, untracked, written by the Claude.ai Praxis project channel from Amear's voice call 08:30-09:27 ET) and dispatch of unit `2026-11-15-rulings-filing`.** One praxis-manage
r files the notes plus the 14:37:18Z typed ruling as DECISIONS.md entry D-2026-11-15-A, WHO: amear, REPORTED BY the voice channel, through a temp index at HEAD d9fc5f0. Sequencing for S4: the Noise-Area paper read that Amear ordered is NOT dispatched until this entry is committed. Decided by master 
under D-2026-11-08-D D1: (i) the notes carry the MFFU rep's first name and a support address on 1 line (:122; count only); the filer replaces both with bracketed placeholders before first commit and discloses the count, per the standing rule; (ii) the notes state P&L figures without the S13 sentence
; the filer appends it once with a filer's note. Open and not answered: Flat1559 reading; MFFU email route. F3 and F4 stay FROZEN. | WHY: Amear's rulings; S4, S5, S8 | WHERE: DECISIONS.md; /tmp/praxis-r15/idx | WHEN: `date -u` 14:37:18Z | HOW: one praxis-manager, background | STATE: dispatched
0
- [2026-11-14T16:26:00Z] WHO: praxis-master
- [2026-11-15T13:30:00Z] WHO: praxis-master
- [2026-11-15T14:37:18Z] WHO: amear
- [2026-11-15T14:38:00Z] WHO: praxis-master
~~~~

### Command 07

~~~~
$ cd /Volumes/Sensidine/Praxis.build && grep -c -F -e 'voice-brief-open-questions' -e '2026-11-15-rulings-filing' DISPATCH_LOG.md; grep -c -F 'voice-brief-open-questions' DECISION_LOG.md
0
1
~~~~

### Command 08

~~~~
$ cd /Volumes/Sensidine/Praxis.build && grep -F '[2026-11-05T23:50:09Z] WHO: amear' DECISION_LOG.md | sed -e 's/.*typed, verbatim:\*\* "Rulings //' -e 's/ 2\. Summary v2.*//'
1. Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands.
~~~~

### Command 09

~~~~
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:DECISIONS.md | awk 'NR==803||NR==814||NR==881||NR==907||NR==908||NR==924||NR==936||NR==937||NR==947||NR==970||(NR>=1735&&NR<=1740){print NR": "$0}'
803: ## 2026-11-05 — D-2026-11-05-A: Walk-forward design rulings (Amear, voice 2026-11-05)
814: - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
881: ## 2026-11-05 — D-2026-11-05-C: Phase 3 spec import (r8j) and walk-forward spec
907: - Ruling 1 (`2026-11-05T23:50:09Z`, typed): *"Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest."*
908: - From `2026-11-05T23:51:21Z` (REPORTED BY the voice agent): R-VN4-2, R-VN4-3, R-VN4-5 and R-VN4-7.
924: ## 2026-11-05 — D-2026-11-05-B: R-VN4-1..14 — voice session 2026-11-04 (filed 2026-11-06)
936: - **R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
937:   - reading (voice agent, notes-4): Bar-close checks (market-order flatten) in the backtest; resting stop orders once live. Claude noted the gap: the backtest then does not test live stop fills; paper trading (Block 4) covers it.
947: - **R-VN4-7** — proof of concept: "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." / "We're just gonna proceed without that [historical tick data]."
970: - (iii) R-VN4-6 with the fee report (`docs/reports/2026-11-05-mffu-fee-check.md:7-10`): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM. The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear (DECISION_LOG `2026-11-05T23:59:40Z`, `2026-11-06T00:06:48Z`; fee report NEEDS AMEAR at `:131`).
1735: A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
1736:     of the ruled limit, i.e. below the lower of 3.2% of the MFFU
1737:     account size and 80% of MFFU's trailing drawdown limit. This
1738:     amends D-2026-11-05-A item 3 with a safety buffer for model error.
1739:     Evaluated against every tier row; tier pick stays Q9. Closes the
1740:     notes-4 DD equity-base item.
~~~~

### Command 10

~~~~
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:DECISIONS.md | awk 'NR==2367||NR==2426||NR==2431||NR==2433||NR==2459||NR==2468||NR==2470||NR==2481||NR==2482||(NR>=2488&&NR<=2493)||NR==2527||NR==2533||NR==2540||NR==2546||NR==2555||NR==2560||NR==2562||NR==2572||NR==2580||(NR>=2586&&NR<=2592)||NR==2593||NR==2595||NR==2600{print NR": "$0}'
2367: ## 2026-11-13 — D-2026-11-13-D: Amear's rulings of the 2026-11-13 evening (research screen, build pause, search loop in Claude Code, trade-count gap, in-VM rule). Filed WHO: amear, REPORTED BY the Claude.ai channel.
2426: **Ruling 2: builds paused.** The pause is defined at handoff :53-:55 (the channel's text). New build units stop: NinjaScript for the trading path, breakers, monitor, n8n workflows, and walk-forward runs on existing strategies. These carry on: the step 2 filing, the step 4 search loop and its backtests, ledger and close flushes, and pushes. The 4-hour build timer is stated as paused in the master's plan in DECISION_LOG.md:942 ("The 4-hour build timer stays paused."). That is REPORTED BY the master, and this unit did not observe the timer. The open beads it touches are listed below. This is the filer's reading of each bead's title and text (`bd list --status open`, `--status in_progress`, `--status blocked`, `bd ready`, `bd show`). No bead is closed or changed by this entry.
2431: The pause ends when the loop records its third contender (handoff :55). Which contender goes forward is a strategy decision and stays with Amear (handoff :55). By the same line, no agent decides it.
2433: **Ruling 3: the search loop runs in Claude Code.** Amear's words: "Have the loop run within Claude Code" (handoff :9). The handoff places it "in Claude Code on the Mac" (handoff :57) and sends its backtests to the VM bridge through Hermes over SSH (handoff :64). Finding, recorded and not repaired: handoff :64 says the runs are "dispatched by Hermes over SSH as on 2026-11-13". The record of the 2026-11-13 runs names their source as "the VM Claude Code session's own report" (`docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md`:5). No record shows Hermes dispatching them. The same file also says, at :29, that the `claude` command "is not installed on the VM". The filer reads that as in tension with :5's "VM Claude Code session". A missing command does not by itself show that no session ran (INFERRED).
2459: ## 2026-11-13 — D-2026-11-13-E: Strategy search loop contender bar and overfitting guard (PROPOSED BY the Claude.ai channel; master under D-2026-11-08-D D1)
2468: **Skip** anything already backtested: the three Noise-Area arms and Last-Half-Hour Momentum. Ideas screened out earlier only because they lacked peer-reviewed evidence are back in scope, because that screen is gone. This includes gap fade, VWAP or Bollinger reversion, and opening-range breakout. The record of what came up before is in `docs/reports/2026-11-13-strategy-review-index-worker2.md` :25-:79.
2470: **Commission (hand step for Amear).** MFFU charges $4.68 round trip, but NT8 still has $2.96 set. Setting $4.68 is Amear's hand step. Send him one Telegram asking for it when the loop starts. Until it is set, label every result "screening, $2.96". **A candidate cannot become a contender until it has a $4.68 run.**
2481: 2. It has a full five-year backtest at $4.68 commission.
2482: 3. **It passes the drawdown gate at 1 MNQ for at least one MFFU account size.** The gate is in DECISIONS.md :1735-:1740: max drawdown stays below the lower of 3.2% of the account and 80% of MFFU's trailing limit. For a 50K account that is $1,600. Measure it the way the D6 check did (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`), on the four-measure basis.
2488: **Overfitting guard (PROPOSED).** Without peer review, the main risk is finding a lucky fit. So:
2489: 
2490: - Each idea is tuned only on 2021-03-08 to 2024-12-31.
2491: - Its rules are then frozen and run once on 2025-01-01 to 2026-07-17.
2492: - Allow no more than three parameter variants per idea, and log every variant tried, including the failures.
2493: - Walk-forward testing under the existing spec comes later, for whichever contender Amear picks.
2527: ## 2026-11-14 — D-2026-11-14-B: Amear's restructure rulings of the 2026-11-14 voice session (R1-R9). Filed WHO: amear, REPORTED BY the voice-chat agent.
2533: **R1 — Noon search loop held.** Notes :10-:11:
2540: **R2 — Prop firms set aside for now.** Notes :15:
2546: **R3 — "The cost of the trade" is the number one rule.** Notes :19-:21 and :23 (`sed -n '19,21p;23p'`; :22 is the voice agent's confirmation and is left out; :23's lead-in is the voice agent's):
2555: **R4 — Recheck the tested strategies against R3.** Notes :27 and :29 (`sed -n '27p;29p'`; both lead-ins are the voice agent's):
2560: Filer's reading: the recheck is queued. The master dispatched unit `2026-11-14-r3-recheck` (row 15:08:00Z) for the strategies listed at notes :28. What follows from it is Q6.
2562: **R5 and R6 — Options C and D accepted.** Notes :33, then the options as `docs/reports/2026-11-14-voice-brief-pivot.md` :34-:35 stated them (the brief, staged with this entry):
2572: **R7 — Max trades per session: rule exists, number set from backtest data.** Notes :37-:39:
2580: **R8 — Daily loss cap: rule exists, number set later from data.** Notes :43 (:42 is the voice agent's question):
2586: **R9 — Process instructions.** Notes :47-:48:
2587: ```text
2588: > "if anything seems ambiguous or not well defined, I want it to put together another brief ... that I can come back here to the voice session to answer the questions."
2589: > "I also want you to mention to it to create a skill ... if there's like multiple topics to be discussed, decisions ... where it would automatically give me a brief for a voice message. Or voice chat."
2590: ```
2591: Filer's reading: two instructions. (a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48). That it is proposed to Amear, not self-certified, is the voice agent's handoff (notes :59), not his words.
2592: 
2593: **Open questions (Amear's, unanswered, S8).** Copied by script from notes :64-:69. None is answered here.
2595: - **Q1, R8 wording.** His "Yeah" could mean "wait for data" or agree to "a multiple of the cost of a trade." Recorded as wait-for-data. Confirm.
2600: - **Q6, R4 outcome.** Once the recheck is done: is any of the five worth rerunning with a hard stop, or are they dropped?
~~~~

### Command 11

~~~~
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | awk 'NR==31||NR==35||NR==36||NR==67||NR==74{print NR": "$0}'; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | awk 'NR==58{print NR": "$0}'
31: - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
35: **Typed ruling 1** — RULED (DECISION_LOG `[2026-11-05T23:50:09Z] WHO: amear`, "typed, verbatim"):
36: > "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands."
67: - Item 1 adds the stop for arm (b): "A stop is added to the strategy for (b) on its own branch; baseline file unchanged." (`:812`). — RULED (D-2026-11-05-A). Arm (a) therefore runs with no added stop. — INFERRED (from item 1).
74: - Stop: "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (typed ruling 1). — RULED.
58: | 1 | Daily loss limit | n8n gate node, before Write Signal File: Redis flag `gate:daily_loss` (closed when realised + unrealised P&L ≤ −threshold, or when the P&L reading is stale). Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes, plus resting stops on every live position (R-VN4-2: "Until the account is live … resting stops.", REPORTED BY the voice agent; the reading "resting stops once live" is the voice agent's, Phase 3 import :24–25) [E27]. | The gate stops every new entry signal before the file is written, so no file reaches the consumer and no order is submitted. The flatten is an order itself; it is a risk-reducing exit, not a new entry, and must never be blocked by a closed gate (OPEN-T2). | Realised + unrealised P&L for the session, in real time, from the NT8 account; the threshold. | SPECIFIED. No numeric threshold exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65). | An account-state feed from NT8 to Redis (unbuilt); EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt; the consumer only knows BUY/SELL, :516–520, and only calls `EnterLong` / `EnterShort`, :660, :662 [E14]; under NT8's managed approach an `EnterShort` while long reverses into a short, `PraxisNoiseAreaBreakout.cs`:224, so an exit sent as SELL would open a position); a threshold value (R8 KEEP; value PROPOSED by a later unit; D2(c) once real money is at stake). |
~~~~

### Command 12

~~~~
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | awk 'NR==11||NR==54||NR==64||NR==76||NR==82||(NR>=97&&NR<=103)||(NR>=138&&NR<=140)||NR==145{print NR": "$0}'
11: > **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ implemented ≠ tested ≠ tested under failure. Basis, checked 2026-11-05: `grep -rniE "breaker|circuit" ninjascript/` returns one hit, a source comment in `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` (line 31) that names breakers #4/#5 only to say that variant does not decide rubric F2 — a comment, not breaker code; `grep -rnilE "breaker" scripts/` returns nothing; there is no `n8n/` directory in the repository; across all tracked `.cs`/`.py`/`.js`/`.ts`/`.json`/`.sh`/`.ps1` files the only file mentioning "breaker" is that same `.cs` file. Scope of that basis: it is a keyword search. `ninjascript/PraxisSignalConsumer.cs` rejects any order whose qty exceeds a `MaxQty` sim sanity cap (default 5; lines 94 and 527–528), which resembles breaker #7's behaviour; it is not the specified n8n breaker and has not been tested as a breaker. Nothing in this document is evidence that any circuit breaker — or any other component described below — exists in working form. The body text is the source author's design language; where it speaks in the present tense (for example, that the system "blocks violations before they reach the order engine"), it is describing intent, not a built system. That wording is preserved verbatim because this is an import; it is not a status claim.
54: NinjaScript fundamentals. The NQ Noise-Area strategy is mechanically simple: at a fixed time, check if price has broken above or below a calculated noise band, place a stop-market entry with a bracket (stop-loss + take-profit). In NinjaScript, that’s an OnBarUpdate() method that checks the time, computes the band from the day’s range, and calls EnterLongStopMarket() or EnterShortStopMarket() with SetStopLoss() and SetProfitTarget(). Claude writes the code. You read it, understand what each block does, and can explain it back. That’s the bar.
64: What you’re doing: Validating the NQ Noise-Area strategy against historical data using NinjaTrader’s Strategy Analyzer. This is where the MFFU connection becomes necessary — not for live trading, but for historical data access through Rithmic.
76: The backtest itself: NinjaTrader Strategy Analyzer with the configuration already specified in the research. Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract. Rolling walk-forward optimization: 252-day in-sample / 63-day out-of-sample / 63-day step. Four parameters optimized (lookback, noise multiplier, stop ATR multiplier, exit policy). Session window and clock times held fixed.
82: - Max drawdown ≤ 4% of equity
97: 1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
98: 2. Max trades per day — trade count hits daily max → disable order submission
99: 3. Consecutive loss (“two and done”) — 2 consecutive losers in one session → identical to max trades
100: 4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
101: 5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
102: 6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
103: 7. Max position size — order quantity exceeds plan → reject
138: |A — Micro |1 MNQ ($2/point)                  |2 weeks + 10 triggered trades|Live metrics within 1 standard error of paper   |
139: |B — Single|1 NQ ($20/point)                  |4 weeks + 20 triggered trades|Stats within 0.5σ of backtest median, no DD > 2%|
140: |C — Full  |Risk-model sizing (0.5% per trade)|Indefinite                   |—                                               |
145: - Account drawdown exceeds 60% of MFFU trailing DD room
~~~~

### Command 13

~~~~
$ (cd /Volumes/Sensidine/Praxis.build && git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | awk 'NR==51||NR==73||NR==124{print "VAL "NR": "$0}'; git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | awk 'NR==48||NR==50||NR==57||(NR>=59&&NR<=61)||NR==64{print "RS "NR": "$0}'; git show HEAD:specs/SPEC_RUBRIC.md | awk 'NR==19||NR==33||NR==34||NR==35||NR==42{print "RUB "NR": "$0}'; git show HEAD:docs/reports/2026-11-14-r3-recheck-manager.md | awk 'NR>=9&&NR<=11{print "RCK "NR": "$0}') | sed -e 's/\x40/<AT-MASKED>/g'
VAL 51: | Stop-ATR multiplier m | none (the paper has no stop; §1) | {1.5, 2.25, 3.0}; stop distance m × ATR(14) | SETTLED — see below |
VAL 73: - **Level** (WF spec NEEDS AMEAR 27) — SETTLED: fixed at entry. Long: entry fill price − m × ATR(14); short: entry fill price + m × ATR(14), where m = `StopAtrMult` (§3), never the noise multiplier k. ATR is the value at the entry bar. Not trailing. A reversal starts a new level from the new entry. Alternative: measured from the signal bar's close, or a trailing level. Changeable by him.
VAL 124:   3. Max drawdown ≤ 4% of equity
RS 48: | Checkpoint grid | every `HH:00` / `HH:30` | §3 p. 9 |
RS 50: | Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
RS 57: ## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)
RS 59: - **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop <AT-MASKED> Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
RS 60: - **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
RS 61:   `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
RS 64: - **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
RUB 19: ### F3 — Backtest fill resolution vs. acquired data granularity
RUB 33: ### F4 — MFFU automation compliance
RUB 34: **Criterion.** Written confirmation from MFFU that this specific automation
RUB 35: pattern is permitted on a funded account.
RUB 42: **Blocks.** Block 4. Block 5.
RCK 9: | Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
RCK 10: | Noise-Area OppBand | opposite-band level, same checkpoint check, market exit | NO | −$1,960.90 | 6 | −$1,894.80 | 2 (1 if same-timestamp reversals are merged) |
RCK 11: | Noise-Area Flat1559 | as baseline, plus a 15:59 flat | NO | −$542.40 | 10 | −$683.70 | 5 |
~~~~

### Command 14

~~~~
$ cd /Volumes/Sensidine/Praxis.build && awk 'NR==15||NR==16||(NR>=26&&NR<=34)||(NR>=38&&NR<=40)||(NR>=44&&NR<=49){print NR": "$0}' docs/reports/2026-11-15-voice-brief-open-questions.md
15: - Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
16: - Inbox result, checked this morning: nothing new. No Telegram message since Nov 13 at 8:21 PM ("Halt all runs until further notice"). No new VM reply since Nov 11. No new commits since yesterday's park. His email was not checked, because the Gmail connector failed to connect.
26: Quoted from the committed rulings, DECISIONS.md :2595-:2600 at HEAD.
27: - **Q1, the daily-loss cap wording.** His "Yeah" could mean "wait for data", or agreement to "a multiple of the cost of a trade". It is recorded as wait-for-data. Confirm.
28: - **Q2, the exception to the cost-of-the-trade rule.** If a news gap or slippage fills a stop past its level, is that still "the cost of the trade", or a breach like a server crash? The answer decides how stops are sized and tested.
29:   Fact for Q2, restated from `docs/reports/2026-11-14-r3-recheck-manager.md` :115: in the gap-fade test, price traded past the stop on 273 of 286 stop exits, by up to 45.5 points.
30: - **Q3, which balance the percentage uses.** Starting balance, current balance, or high-water mark?
31: - **Q4, the target account.** With prop firms out "for now", what account does testing assume? A personal cash account, and at what size? Is the MFFU written-confirmation follow-up still worth chasing?
32: - **Q5, the rest of the Floor Rule.** Hard stop time, the account drawdown kill switch, and the after-a-win protocol.
33: - **Q6, the five rechecked strategies.** Rerun any of them with a hard stop, or drop them?
34:   Facts for Q6, at 1 MNQ, restated from the same report, :9-:13 and :17-:21:
38:   - Last-Half-Hour Momentum (already retired): no stop, time exit only. Largest loss $555.40.
39:   - Gap fade V2: a gap-sized stop, but only in a Python test rule. Largest loss $472.90.
40:   - Net profit, UNVERIFIED: baseline about $17,824, OppBand about $19,719, Momentum minus $9,692.60. These are the master's figures from yesterday's session, and no filed report contains them. Treat them as rough until they are re-run.
44: ## Topic 3. Two parked items: pick them up, or leave them?
45: 
46: - **Voice-brief skill** (`Praxis_build-61o`). He approved it. Both audits passed the skill file itself. Both failed on the job report: one command was shortened and one pasted output was trimmed. The park rule says a person resumes it.
47: - **Opening gap fade** (`Praxis_build-vn4`). It failed its pre-screen on Nov 14. Q6 may settle it.
48: Options: A. Resume both. B. Resume the skill only. C. Leave both parked.
49: The master's view: the skill fix is paperwork only. Re-running two commands and pasting their full output would clear it.
~~~~

### Command 15

~~~~
$ cd /Volumes/Sensidine/Praxis.build && awk 'NR==3||NR==4||NR==17||NR==35||NR==38||NR==40||NR==63||NR==78||NR==81||NR==88||NR==92||NR==95||NR==110||NR==111||NR==115||NR==118||NR==120||NR==123||NR==127||NR==128{print NR": "$0}' docs/reports/2026-11-15-voice-notes-open-questions.md
3: Written by the Claude.ai Praxis project channel (Claude chat, linked to the Mac), 2026-11-15 about 09:30 ET, for the PRAXIS master.
4: Source: Amear's voice call that worked through `docs/reports/2026-11-15-voice-brief-open-questions.md`. The call ran between about 08:30 and 09:27 ET. The voice agent had no repo access, so it kept a list and this channel wrote it here at Amear's request ("when we close the chat, then you then write to the repo").
17: "Best candidate" was asked twice (highest return, or best fit to his risk rules). He answered "That's fine. Keep going." (W1). He settled it for Noise-Area in section 9: "I'm I'm looking for steady first." (W2)
35: ## 4. Q1, daily-loss cap: wait-for-data, confirmed (W1)
38: > "As far as the actual figure on what that is, that entirely depends on whether we have a strategy that has been proven to work with MFFU or whatever, um, whatever, whatever like uh, brokerage I'm going to go with, okay, um, so I, I can't set a number right now."
40: Order type. He first said "stop limit". After the trade-off was explained: "Whichever, whichever is going to get me closest to the price that I want to stop at." Then, after being told a stop-market fires automatically at the broker: **"Okay, then that's what we use."** Read: stop-market order, sitting at the broker, placed at entry.
63: So prop firms stay out for now. Account size: **"Uh, I don't know, let's do 10 grand, I guess."** (personal account, $10,000)
78: Read: 5% from peak is a **placeholder** until a strategy's data sets it. Fact given in the call: four of the five rechecked strategies had a 10-trade losing run (OppBand's longest was 6); at 1% risk, all five would trip 5%.
81: > "Which is after two after two losses, the risk goes from 1% risk to 0.5% risk. Once a win occurs, scaled back to 1%."
88: AMBIGUOUS: the question was "retested with a real stop, or all thrown out?" "they should all be" reads as retested, given the rest of the sentence. Confirm with Amear.
92: The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. On the design having no known max loss: "Then that's not compatible. What kind of, who the fuck wants to trade like that?"
95: **Which version first:** "I'm I'm looking for steady first." The agent mapped that to **Flat1559** (steadiest per this channel's read of the filed figures, below). Amear did not object. Confirm the version name with him.
110: - **Voice-brief skill (`Praxis_build-61o`).** Amear: "I don't fucking give a shit, to be honest." No word to resume, so it **stays parked**.
111: - **Gap fade (`Praxis_build-vn4`).** Told it gets retested with a real stop after Noise-Area under Q6, Amear said: "Okay." No separate ruling.
115: 1. The gap fade's $472.90 largest loss is likely understated: the test books every stop at level + 0.5 pt, yet the bar traded past the stop on 273 of 286 stop exits (max 45.5 pt). 1-minute bars cannot show where a real fill would have landed. The voice agent first gave a "$91 extra" figure and then retracted it as overstated.
118: ## 12. MFFU email: hand to the master (W2)
120: > "Okay, still still add those to the handoff though." / "For the Praxis Master to go for those."
123: As the voice agent read it: unattended automated strategies are allowed on Evaluation and Sim Funded accounts (Rapid, Pro, Builder), provided the strategy does not exploit favourable simulated fills; T1 news trading is allowed on Builder plans, in the evaluation and in Sim Funded. **Read MFFU's exact words in the thread before filing; this channel did not quote them.** This looks like it answers the Q4 follow-up ("still worth chasing").
127: - Email this morning: Amear said to disregard everything outside the Praxis repo.
128: - The master owes the exhaustive question set (section 3) before any loop restart.
~~~~

### Command 16

~~~~
$ awk 'NR==3||NR==19||NR==29||NR==44||NR==59||NR==61||NR==69||NR==94||NR==111||NR==121||NR==136||NR==152||NR==127||NR==133||NR==135||NR==148||NR==156||(NR>=161&&NR<=175){print NR": "$0}' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md
3: **Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, unchanged, filed with this entry at the master's dispatch of this unit; row 14:38:00Z names only the notes and the typed ruling for filing ("files the notes plus the 14:37:18Z typed ruling"), and row 13:30:00Z says "No commit this act; the brief stays in the working tree for the next flush."; that difference is named, not resolved) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
19: Filer's reading: testing is now one strategy at a time, not in bulk. The candidate is tested "in multiple ways", and every order is looked at. A second candidate waits for the first ("Yeah, one at a time."). Per the channel's lead-in (notes :17), "Best candidate" was asked twice (highest return, or best fit to his risk rules), and his reply was "That's fine. Keep going." That reply picks neither option; the filer does not read it as an answer. His own words point two ways: "I want the uh, you know, the highest return one." (notes :12) and "I'm I'm looking for steady first." (notes :95). By the channel's table (notes :101, the channel's figures, not re-derived here), OppBand has the highest net and Flat1559 the lowest. That tension is named, not resolved (item (l) below). That it was settled for Noise-Area as "steady first" is the channel's lead-in (notes :17). Which version "steady first" names is still open (item (a) below). His "I still want the top three" (notes :12) is recorded as said. How it fits with one-at-a-time testing and with the three-contender pause of D-2026-11-13-D is named under S6, not resolved.
29: **R3 — The search loop stays paused; the master writes the exhaustive question set (notes section 3, W1).** Notes :29 and :31-:33 (`sed -n '29p;31,33p'`; :31 is the voice agent's proposal; the sentence on :33 is the channel's, and the quoted words in it, "Halt all runs until further notice", are the 2026-11-13 halt message as the channel quotes it; row 13:30:00Z ties those words to an inbound Telegram message of 2026-11-13 20:21:51, and who sent it is not verified here):
44: Filer's reading: Q1 of D-2026-11-14-B is answered as wait-for-data. No daily-loss figure is set; he says it depends on a strategy proven with the broker he goes with. On order type, his "Okay, then that's what we use." answers the explanation of a stop-market order. The channel reads this as "stop-market order, sitting at the broker, placed at entry" (notes :40). The ruling sits in notes section 4, headed for the daily-loss cap (notes :35), and :37 speaks of "a stop limit set order at a level". Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick. T1 uses the same "stop-market order, sitting at the broker and placed at entry" wording for the retest stop; that is named, not read as settling it.
59: Filer's reading: Q3 of D-2026-11-14-B is answered: the percentage is taken on the current balance, "considering" the prop-firm drawdown limits if the account is through a prop firm. The 1% appears in his answer, "Whatever 1% is right now" (notes :51), to the example (notes :53). The filer does not read it as setting R3's percentage of D-2026-11-14-B, which that entry leaves TBD. Whether 1% per trade is now ruled is listed as open (item (g) below).
61: **R7 — Q4, the target account: prop firms stay out; $10,000 personal account; the MFFU follow-up is still worth chasing (notes section 7, W1).** Notes :57, :59, :61 and :63-:64 (`sed -n '57p;59p;61p;63,64p'`; :59's lead-in, "So prop firms stay out for now.", "Account size:", the parenthetical "(personal account, $10,000)", the "MFFU written-confirmation follow-up:" lead-in and "See section 12: MFFU had already answered." are the channel's):
69: Filer's reading: he first said testing was for prop firms. Told this reversed the 2026-11-14 ruling, he kept that ruling (R2 of D-2026-11-14-B, prop firms set aside for now). Testing assumes an account of $10,000; that it is a personal account is the channel's parenthetical. The MFFU written-confirmation follow-up is still worth chasing. F4 (SPEC_RUBRIC.md :34-:35) stays FROZEN.
94: Filer's reading: 5% is Amear's placeholder "for now". He called the figure a guess and said it depends on the strategy. It is a placeholder while no money is at stake. The words "from peak" are the channel's reading (notes :78), not his words. Where the 5% is measured from is open (item (h) below). The losing-run facts on :78 ("Fact given in the call") are the voice agent's and the channel's. No breaker value is changed by this placeholder or by anything in this entry. Changing a breaker value while real money is at stake waits for Amear's explicit word (brief :15).
111: Notes :91-:93 (`sed -n '91,93p'`; :92's first sentence is the voice agent's answer and its note on the paper; :93's AGENT PROPOSAL sentence is the voice agent's proposal, and its "Uh, yeah." is his):
121: Filer's reading: the channel reads "they should all be" as retested, and flags it AMBIGUOUS (notes :88). Amear asked, as a question, whether the strategies should be specced from their source and retested with stop losses (notes :91, "And by the way, that's a question."). He said a design with no known maximum loss is "not compatible". He said yes to the voice agent's proposal to keep the strategy's exit, add a hard stop-market order at entry, and retest (notes :93). Noise-Area goes first. His words are "I'm I'm looking for steady first." (notes :95). That it names Flat1559 is the voice agent's mapping, and the version is open (item (a) below). His typed ruling T1, below, refines this section. Where the two differ, the differences are named after T1.
127: The channel's statement, not a filer's reading: per notes :106, the filed figures supersede the brief's UNVERIFIED net-profit figures (brief :40). That statement is the channel's; it is not re-derived or checked here. The brief is filed unchanged, with those figures still in it. Section 11 of the notes (the channel's check, :116) also says the brief labels its loss figures "at 1 MNQ" (brief :34), while the source labels them "MNQ derived, not an MNQ run". The difference is named here, not resolved. The brief is not edited.
133: Filer's reading: the retest of each of the five depends on its source spec. Where the source spec has a stop and our test ran without one, the strategy is retested with a stop-market order at the broker, placed at entry, so the maximum loss is known before the trade. T1's own words are "No loose or interval-checked exits."; what they exclude is D1 below, open (item (f)). One strategy at a time, Noise-Area first. The original paper is read for whether Noise-Area has a hard stop, and its exact wording is reported. T1 places that read twice: "Before anything else, confirm from the original paper" and, for the report of the exact wording, "before any retest". The master's hold on the read is open item (c). A source spec with no stop goes back to Amear, and nothing is decided on it.
135: Timing fact, not a ruling on precedence: the call ran until about 09:27 ET, 14:27Z (notes :4). T1's row is 2026-11-15T14:37:18Z. This entry does not read T1 as replacing notes section 9, or section 9 as limiting T1. Where they differ, which one governs is Amear's (item (f) below). The differences named (not resolved):
136: - D1, the exit. Notes :93 (the voice agent's proposal, his "Uh, yeah."): "keep the strategy's exit, add a hard stop-market order at entry". T1: "No loose or interval-checked exits." The tested Noise-Area exits are checked at HH:00/HH:30 bar closes (`docs/reports/2026-11-14-r3-recheck-manager.md` :9-:11 at HEAD), and the ruleset records the paper's trailing stop as "Evaluated only at semi-hourly stamps" (`docs/specs/2026-07-16-b2-noise-area-ruleset.md` :59 at HEAD). The same ruleset's checkpoint grid is "every `HH:00` / `HH:30`" (:48), and its improved band-or-VWAP stop (:60-:61) says "Position closes as soon as price crosses the current band **or** the VWAP." (:61). The ruleset can be read two ways on whether the exit is interval-checked (only at the :48 stamps, per :59, or as soon as price crosses, per :61); that bears on T1 and on open item (c), and is not resolved. Whether T1 excludes keeping that exit alongside the hard stop, or only describes the stop itself, is not decided.
148: Filer's reading: on the voice-brief skill (`Praxis_build-61o`), his words are "I don't fucking give a shit, to be honest." (notes :110). "No word to resume, so it **stays parked**." is the channel's text (notes :110), not his ruling. As a fact of the record: no resume word of his is recorded, and the brief says "The park rule says a person resumes it." (brief :46), so the park rule's default holds and the bead is as it was. That fact does not answer the brief's options (brief :48), which also turn on the gap fade. On the gap fade (`Praxis_build-vn4`), told it gets retested with a real stop after Noise-Area under Q6, he said "Okay." (notes :111); "No separate ruling." is the channel's (notes :111). The brief asked "Two parked items: pick them up, or leave them?" (brief :44), said of the gap fade "Q6 may settle it." (brief :47), and gave "Options: A. Resume both. B. Resume the skill only. C. Leave both parked." (brief :48). His "Okay." can be read as option C, left parked until Noise-Area is done, or as a resume with the gap fade queued after Noise-Area; the filer does not pick (item (n) below). Under T1, whether and how it is retested depends on its source spec (D5 above). No bead is changed.
152: **R12 — The MFFU email: hand it to the master (notes section 12, W2).** Notes :120 (`sed -n '120p'`):
156: Filer's reading: his "those" (notes :120) has no stated referent. Reading "those" as the MFFU email is the filer's reading, matching the channel's placement of the quote under its section 12 heading, "MFFU email: hand to the master" (notes :118). On that reading, the MFFU email goes to the Praxis master through the handoff. Notes :122 names the thread. It is cited by line only; the rep's first name and the support address on it were replaced with bracketed placeholders at filing (Authority, (i)). The thread has not been read in this repo: the Gmail connector failed to connect this session (rows 2026-11-15T13:30:00Z and 2026-11-15T14:37:18Z). No MFFU wording is quoted. Notes :123 is the voice agent's reading of the email, and the channel's own instruction there is to read MFFU's exact words before filing. That reading does NOT unfreeze F4 (SPEC_RUBRIC.md :34-:35), which stays FROZEN. Its remark that the email "looks like" it answers the Q4 follow-up is the channel's, not a finding.
161: - (a) Whether "steady first" (notes :95) names Flat1559. The mapping is the voice agent's. The 14:37:18Z row lists it as "Left unanswered by him". Answer: NONE.
162: - (b) The Q6 reading of "they should all be" (notes :86, flagged AMBIGUOUS at :88), as T1 refines it (D2). Answer: NONE.
163: - (c) What the Noise-Area paper says about a stop, in its exact wording. T1 says "Before anything else, confirm from the original paper" and asks for the exact wording "before any retest". Row 14:38:00Z holds the read: "the Noise-Area paper read that Amear ordered is NOT dispatched until this entry is committed". The master's hold sits against his "Before anything else"; that is named, not resolved. Answer: NONE.
164: - (d) The MFFU email. The thread is named at notes :122. It has not been read in this repo, because the Gmail connector failed this session. No MFFU wording is quoted here. F4 (SPEC_RUBRIC.md :34-:35) stays FROZEN, and the notes' description of the email (:123, the voice agent's reading) does NOT unfreeze it. How the email reaches the repo is listed as "Left unanswered by him" in the 14:37:18Z row. Answer: NONE.
165: - (e) The exhaustive question set the master owes before any loop restart (notes section 3, :29 and :31; :128). Not written yet. Answer: NONE.
166: - (f) (the filer's addition) Where T1 and notes section 9 differ (D1-D6 above), which governs. Answer: NONE.
167: - (g) (the filer's addition) Whether 1% per trade is now ruled. His words use 1% in the Q3 example (notes :51) and in the variable to test (notes :81). R3 of D-2026-11-14-B leaves the percentage TBD. Answer: NONE.
168: - (h) (the filer's addition) Where the 5% placeholder is measured from: from peak (the channel's "Read:", notes :78), the current balance (Q3), or the starting balance. Answer: NONE.
169: - (i) (the filer's addition) How "I still want the top three" (notes :12) fits with one-at-a-time testing (R1) and with the pause until three contenders exist (D-2026-11-13-D ruling 2). Answer: NONE.
170: - (j) (the filer's addition) Which drawdown gate applies to a $10,000 personal account (R7). The A4 gate, contender bar item 3 and the walk-forward gate base are all stated against MFFU (S6 below). Answer: NONE.
171: - (k) (the filer's addition) Where the real MNQ data for R2 comes from, and whether testing on it is a purchase or a build. No source is named in the notes. Answer: NONE.
172: - (l) (the filer's addition) Whether "best candidate" (notes :13) means highest return ("the highest return one", notes :12), best fit to his risk rules (the channel's framing of the question, notes :17), or "steady first" (notes :95). His "That's fine. Keep going." (notes :17) picks none of them. By the channel's table (notes :101), OppBand has the highest net and Flat1559 the lowest. Answer: NONE.
173: - (m) (the filer's addition) Which order his "Okay, then that's what we use." (notes :40, in notes section 4, headed for the daily-loss cap, :35) covers: the per-trade stop, the daily-loss cap, or both. Answer: NONE.
174: - (n) (the filer's addition) Whether the gap fade (`Praxis_build-vn4`) is resumed, queued after Noise-Area, or left parked. His "Okay." (notes :111) answers being told it gets retested with a real stop after Noise-Area under Q6; the brief's options are at brief :48 (R10 above). Answer: NONE.
175: - (o) (the filer's addition) Which governs the retest stop: T1 ("a proper stop-market order, sitting at the broker and placed at entry"; "No loose or interval-checked exits."), or his typed ruling 1 of `2026-11-05T23:50:09Z` (DECISIONS.md :907 at HEAD: "evaluated on bar close, exit by market order next bar" and "Not a resting stop in the backtest.") with R-VN4-2 (DECISIONS.md :936 at HEAD), which ruling 1 cites (S6 below). Ruling 1 is worded for arm (b)'s stop; whether it reaches T1's retest is part of this item. Answer: NONE.
~~~~

### Command 17

~~~~
$ awk '(NR>=177&&NR<=189)||NR==193{print NR": "$0}' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md
177: **S6 cross-block** (the filer's readings; the greps, run at HEAD `d9fc5f0`, are in `docs/reports/2026-11-15-rulings-filing-worker1.md`; the HEAD lines added in revision are shown in `docs/reports/2026-11-15-rulings-filing-worker3.md`). Every tension is named; none is resolved; no other file is changed.
178: - D-2026-11-14-B (DECISIONS.md :2527-:2615 at HEAD). These rulings respond to its Q1-Q6 (:2595-:2600): Q1 by this entry's R4, Q2 by this entry's R5, Q3 by this entry's R6, Q4 by this entry's R7, Q5 by this entry's R8, and Q6 by this entry's R9 and T1. Q6's reading stays open ((b), (f)). That entry is not edited. D-2026-11-14-B R1 (:2533, the noon search loop held) bears on this entry's R3 (the loop stays paused). D-2026-11-14-B R2 (:2540, prop firms set aside for now) is kept by this entry's R7. D-2026-11-14-B R3 (heading :2546; the filer's reading at :2553) leaves the percentage TBD; this entry's R6 answers which balance it uses, and whether 1% is set is open (g). D-2026-11-14-B R4 (:2555, the recheck of the tested strategies against D-2026-11-14-B R3): its filer's reading says "What follows from it is Q6." (:2560), and T1 is his typed Q6 ruling. D-2026-11-14-B R5 and R6 (:2562, options C and D accepted: a quick Python screen on the Mac with NinjaTrader kept for finalists, and a lighter evidence standard for research screens) bear on how T1's retest runs, which is not said. D-2026-11-14-B R7 (:2572, the max-trades number comes from backtest data) is untouched. D-2026-11-14-B R8 (:2580, the daily-loss cap waits for data) is confirmed by this entry's R4. Named, not resolved. Not amended.
179: - D-2026-11-13-D (heading :2367). Ruling 2 (:2426) pauses new build units, "walk-forward runs on existing strategies" included, and says the step 4 search loop and its backtests carry on. The pause ends at the third contender (:2431). R1 (one at a time, and "the top three") and T1 (retest Noise-Area first, an existing strategy) do not say whether the retest is a paused build or a research screen. R3 keeps the loop of ruling 3 (:2433) paused. Not amended.
180: - D-2026-11-13-E (heading :2459). Its skip list (:2468) skips "the three Noise-Area arms and Last-Half-Hour Momentum" for the loop; T1 retests Noise-Area first, outside or inside the loop, which is not said. Bar item 3 (:2482) requires the drawdown gate "at 1 MNQ for at least one MFFU account size", and bar item 2 (:2481) requires a backtest at $4.68, which :2470 names as MFFU's round-trip commission. R7 keeps prop firms out and sets a $10,000 account. Its overfitting guard (:2488-:2493, headed "**Overfitting guard (PROPOSED).**" at :2488) says "Allow no more than three parameter variants per idea, and log every variant tried" (:2492), with a fixed tuning window and a single frozen run (:2490-:2491). R1's "test it in multiple ways", R8(d)'s variable to test and T1's added stop (a new variable, per the voice agent's note at notes :92) bear on that cap; whether the guard binds the retest, and how these count against it, is not said. Named, not resolved. Not amended.
181: - R-VN4-6 fee record (DECISIONS.md :970 at HEAD): MFFU's page gives NQ $4.68 round trip (MNQ $1.90), and the cost model stays $2.96. R2 calls for testing on real MNQ data, while bar item 2's $4.68 (:2481) is the NQ figure. Which commission an MNQ run uses is not said. Named, not resolved. Not amended.
182: - The A4 drawdown gate (DECISIONS.md :1735-:1740 at HEAD) is set as a share of the MFFU account size and MFFU's trailing limit. R7 (a $10,000 personal account) and R8(c) (a 5% placeholder kill switch) bear on it. Not amended.
183: - Walk-forward spec (`docs/specs/2026-11-05-walk-forward-spec.md`, HEAD text; the file is modified in the working tree and that text is not used). The gate base and the per-window drawdown are stated against MFFU (:31-:32; :31 says "Revisit if a personal account is used."), which R7 bears on. Arm (b)'s stop is "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (:36, quoted again at :74, where it is marked "(typed ruling 1). — RULED."). These are Amear's typed words, not spec text only: D-2026-11-05-C records them as "Ruling 1 (`2026-11-05T23:50:09Z`, typed)" (DECISIONS.md :907 at HEAD). The R-VN4-2 they cite reads "Until the account is live … resting stops." (DECISIONS.md :936 at HEAD), REPORTED BY the voice agent (:908); the reading "Bar-close checks (market-order flatten) in the backtest; resting stop orders once live." is the voice agent's (:937). T1 calls for "a proper stop-market order, sitting at the broker and placed at entry, so the maximum loss is known before the trade" and says "No loose or interval-checked exits." Ruling 1 says the backtest stop is evaluated on bar close and is not a resting stop; T1's retest stop sits at the broker. That conflict between two typed rulings of his is named, not resolved; which governs is Amear's (item (o)). R4 bears on arm (b)'s stop only if his "Okay, then that's what we use." covers the per-trade stop (open (m)); the filer does not pick. The same :36 ends "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands." R5 counts slippage past the stop in the cost of the trade once it is measured by enough testing, and the channel's check (notes :115) says "1-minute bars cannot show where a real fill would have landed". Named, not resolved. Arm (a) runs with no added stop (:67, marked INFERRED there). Not amended.
184: - Live-signal topology (`docs/specs/2026-11-10-live-signal-topology.md` :58 at HEAD). Breaker #1's "cancel all, flatten" action is built with "resting stops on every live position", citing R-VN4-2 as "Until the account is live … resting stops.", and marks the reading "resting stops once live" as the voice agent's. Ruling 1 (DECISIONS.md :907) cites the same R-VN4-2. T1's stop at the broker, placed at entry, in a retest, bears on that split between backtest and live (item (o)). If his "Okay, then that's what we use." covers the daily-loss cap (open (m)), R4 bears on breaker #1 here too. Named, not resolved. Not amended.
185: - Walk-forward values (`docs/specs/2026-11-06-walk-forward-values.md`, HEAD text; modified in the working tree, not used). Arm (b)'s stop is an ATR multiple on a grid, with the anchor "none (the paper has no stop; §1)" (:51), fixed at entry (:73), not a percentage of the account. That anchor is one more HEAD statement about the paper's stop; T1's paper read (open (c)) bears on it. The Block 2 gate still reads "Max drawdown ≤ 4% of equity" (:124). R6, R8(c) and T1 bear on these. Not amended.
186: - Phase 3 spec (`docs/specs/2026-11-05-phase3-build-specification.md`, HEAD). Block 1 names a bracket "stop-loss + take-profit" with no sizing rule (:54). Block 2 takes historical data over the MFFU connection, "through Rithmic" (:64), and its backtest runs at "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract" (:76). R2 (real MNQ data, where :76 names NQ), R5 (stop slippage counted in the cost of the trade, where :76 names slippage on entries) and R7 (prop firms out, where :64 routes the data through the MFFU connection) bear on these. Named, not resolved. Breaker #1, daily loss (:97): R4 sets no value. Breaker #1 is a software action, "cancel all, flatten, disable for session" (:97), not a resting broker order. If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved. Breaker #2, max trades (:98): untouched. Breaker #3, "2 consecutive losers in one session → identical to max trades" (:99): R8(d)'s variable sets risk at 0.5% after two losses (notes :81). Whether trading continues within the same session after two losses is not said in his words. The tension with breaker #3 (:99) is named, not resolved; R8(d) is a variable to test, not a rule. Breaker #4 (imported :100, amended to a 16:00 ET session flat at :208-:212): R8(b) says the hard stop time depends on the strategy. Breaker #5, the afternoon session window (:101), is a fixed clock window; R8(b) bears on it the same way. Breaker #6, trailing drawdown proximity to "MFFU’s $1,500 EOD trailing drawdown" (:102), and the kill criterion "Account drawdown exceeds 60% of MFFU trailing DD room" (:145): R7 and R8(c) bear on both. Sizing: stages A and B size by a fixed contract (:138-:139), and stage C sizes at "0.5% per trade" (:140). R6's current balance and the 1% in his words (open (g)) bear on :140. Breaker #7, max position size (:103), rejects a quantity above plan; R6's current-balance sizing and R8(d)'s 1% to 0.5% variable change the quantity per trade, so what the plan is under them is not said. Named, not resolved. The Block 2 gate "Max drawdown ≤ 4% of equity" (:82) is as above. No breaker value is changed. All nine breakers stay SPECIFIED ONLY (:11). Not amended.
187: - Noise-Area ruleset (`docs/specs/2026-07-16-b2-noise-area-ruleset.md`, HEAD). Its exit section is marked PAPER-VERIFIED (:57). The base stop is a trailing stop at the opposite band, "Evaluated only at semi-hourly stamps" (:59). The improved stop trails at band-or-VWAP (:60-:61). The only time exit is 16:00 (:64), and there is no ATR stop anywhere in the paper (:50). T1 orders the paper read "Before anything else", with the exact wording reported, and says "No loose or interval-checked exits." (what that excludes is D1, open). The checkpoint grid (:48) and the "as soon as" wording of the improved stop (:61) are named under D1. Whether the ruleset's reading meets T1's order is not decided here; the master dispatches the read after this entry (row 14:38:00Z). Not amended.
188: - F3 (SPEC_RUBRIC.md :19-:31, FROZEN). R5 counts slippage past the stop in the cost of the trade, once it is measured by enough testing. The channel's check (notes :115) says 1-minute bars cannot show where a stopped fill lands. T1's retests would run under F3's limits. F3 is not claimed cleared.
189: - F4 (SPEC_RUBRIC.md :33-:42, FROZEN; criterion :34-:35). R7 keeps the MFFU follow-up "still worth chasing", and R12 hands the email to the master. The notes' reading of the email (:123) is the voice agent's. F4 is not lifted, and no ruling here opens Block 4 or Block 5.
193: **S4 timing.** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, before any act under these rulings. In DECISION_LOG.md the 2026-11-15 rows are 13:30:00Z (the master's inbox check and voice brief), 14:37:18Z (T1) and 14:38:00Z (intake and dispatch of this unit). No row follows 14:38:00Z. No retest, paper read, loop restart, question set, bead change or breaker change appears in the ledger. The paper read is held until this entry is committed (row 14:38:00Z). Chain: Amear (voice call, notes :4) → the notes, written by the Claude.ai Praxis project channel (notes :3) → DECISION_LOG 2026-11-15T14:37:18Z (WHO: amear, typed) → 2026-11-15T14:38:00Z (master intake and dispatch). Observed in the rows, not fixed: row 14:38:00Z carries "WHEN: `date -u` 14:37:18Z", which does not match its own timestamp and equals the previous row's. Row 13:30:00Z carries "WHEN: `date -u` 13:25:51Z". Row 14:37:18Z's WHEN matches its timestamp. Row 14:38:00Z names the reporter as "the voice channel"; this entry uses "the Claude.ai Praxis project channel", the notes' own name for it (notes :3). Also observed, not fixed: the working-tree DECISIONS.md carries an uncommitted entry whose heading names D-2026-11-12-B (working-tree :2280; not at HEAD), so working-tree line numbers after it differ from HEAD's. All DECISIONS.md line numbers in this entry are HEAD's.
~~~~

### Command 18

~~~~
$ grep -n -o -F -e 'R4 and T1 call for' -e 'is built with' -e 'R-VN4-7' -e 'No tick purchase' -e 'purchase' -e 'personal account' -e 'pending Amear' -e 'R9 of D-2026-11-14-B' -e 'D-2026-11-14-B R9' -e 'refines' -e 'not compatible' -e 'stays parked' -e 'bracket' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md
5:bracket
61:personal account
61:personal account
66:personal account
69:personal account
114:not compatible
121:not compatible
121:refines
143:stays parked
145:stays parked
148:stays parked
156:bracket
162:refines
170:personal account
171:purchase
182:personal account
183:personal account
183:No tick purchase
183:R-VN4-7
184:is built with
186:bracket
~~~~

### Command 19

~~~~
$ cd /Volumes/Sensidine/Praxis.build && LC_ALL=C grep -c $'\x40' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md docs/reports/2026-11-15-voice-notes-open-questions.md; grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md; tail -n 1 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md; git status --porcelain -- docs/reports/2026-11-15-voice-notes-open-questions.md docs/reports/2026-11-15-voice-brief-open-questions.md DECISIONS.md
/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v3-under-test.md:0
docs/reports/2026-11-15-voice-notes-open-questions.md:0
1
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
 M DECISIONS.md
?? docs/reports/2026-11-15-voice-brief-open-questions.md
?? docs/reports/2026-11-15-voice-notes-open-questions.md
~~~~

## Prior findings (19): CLOSED or OPEN

v3 line numbers below. The v3 text is in commands 16 and 17.

Worker 2, items 1-9:

1. **CLOSED.** v3 :19: `That reply picks neither option; the filer does not read it as an answer.` The conflict between his two statements is named and carried as item (l) at v3 :172: `His "That's fine. Keep going." (notes :17) picks none of them. ... Answer: NONE.`
2. **CLOSED.** v3 :133: `T1's own words are "No loose or interval-checked exits."; what they exclude is D1 below, open (item (f)).` The settling sentence is gone. Command 18 finds no line with "Loose and interval-checked exits are excluded".
3. **CLOSED.** v3 :44: `Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick.` Item (m) is at v3 :173. The daily-loss tension with breaker #1 is named at v3 :186: `If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved.`
4. **CLOSED.** v3 :59: `The 1% appears in his answer, "Whatever 1% is right now" (notes :51), to the example (notes :53).`
5. **CLOSED.** Command 05 finds each of these strings byte-exact in its source: v3 :121 `"I'm I'm looking for steady first."` (notes.md), v3 :187 `"Before anything else"` (rows.txt), v3 :94 `"from peak"` (notes.md), and v3 :186 `"MFFU’s $1,500 EOD trailing drawdown"` (Phase 3 spec, with U+2019).
6. **CLOSED.** v3 :186 names Phase 3 :64, :76, breaker #5 (:101) and breaker #7 (:103). v3 :183 quotes the end of WF spec :36. v3 :181 names DECISIONS :970. Commands 09, 11 and 12 show the HEAD text.
7. **CLOSED.** v3 :136 names ruleset :48, :59, :60-:61 and the :61 "as soon as" wording, and says the ruleset `can be read two ways`.
8. **CLOSED.** v3 :127: `The channel's statement, not a filer's reading: per notes :106, the filed figures supersede ... That statement is the channel's; it is not re-derived or checked here.`
9. **CLOSED.** v3 :3: `his quoted words on :40, among them "Okay, then that's what we use.", are his` and `his "Uh, yeah." on :93, like his replies on :24 and :32, is his`. v3 :111 makes the same split.

Worker 4, new items 1-10:

1. **CLOSED.** Command 18 finds no line with "R4 and T1 call for". v3 :183 is now conditional: `R4 bears on arm (b)'s stop only if his "Okay, then that's what we use." covers the per-trade stop (open (m)); the filer does not pick.`
2. **CLOSED.** v3 :148: `His "Okay." can be read as option C, left parked until Noise-Area is done, or as a resume with the gap fade queued after Noise-Area; the filer does not pick (item (n) below).` Item (n) is at v3 :174. (The skill half of the same question is new finding 10.)
3. **CLOSED.** v3 :183 now names DECISIONS :907 ("Ruling 1 (`2026-11-05T23:50:09Z`, typed)"), :936, :908 and :937. v3 :184 names topology :58. v3 :175 adds item (o), "Answer: NONE". Commands 08 and 09 confirm that the :907 words are Amear's typed words (row `[2026-11-05T23:50:09Z] WHO: amear`). The rest of the same typed ruling is new finding 1.
4. **CLOSED.** v3 :163: `T1 says "Before anything else, confirm from the original paper" and asks for the exact wording "before any retest". ... The master's hold sits against his "Before anything else"; that is named, not resolved.`
5. **CLOSED.** v3 :178: `These rulings respond to its Q1-Q6 ... Q6's reading stays open ((b), (f)).` Every R number is qualified as "D-2026-11-14-B R7" or "this entry's R7".
6. **CLOSED.** v3 :186: `Whether trading continues within the same session after two losses is not said in his words.`
7. **CLOSED.** (a) v3 :180 names the guard at :2488-:2493 and quotes :2492. (b) v3 :178 names D-2026-11-14-B R1 (:2533), R4 (:2555, :2560) and R5/R6 (:2562). (c) v3 :184 names topology :58. (D-2026-11-14-B R9 is still missing; see new finding 5.)
8. **CLOSED (named).** v3 :3: `row 14:38:00Z names only the notes and the typed ruling for filing ... that difference is named, not resolved`. A part of the same sentence that is still asserted without a row is new finding 6.
9. **CLOSED.** The v3 :29 header: `the quoted words in it, "Halt all runs until further notice", are the 2026-11-13 halt message as the channel quotes it; row 13:30:00Z ties those words to an inbound Telegram message of 2026-11-13 20:21:51, and who sent it is not verified here`. Command 06 (row 13:30:00Z) confirms the tie.
10. **CLOSED.** v3 :156: `his "those" (notes :120) has no stated referent. Reading "those" as the MFFU email is the filer's reading`.

Count: 19 CLOSED, 0 OPEN.

## New findings

1. **MED, S6 (missed touch on ruled text) and S2. Amear's typed ruling 1 also says "No tick purchase. R-VN4-7 stands." The entry never tests R2, open item (k) or R5 against those words or against R-VN4-7.**
   v3 :183: `The same :36 ends "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands." R5 counts slippage past the stop in the cost of the trade once it is measured by enough testing, and the channel's check (notes :115) says "1-minute bars cannot show where a real fill would have landed". Named, not resolved.`
   v3 :171, item (k): `Where the real MNQ data for R2 comes from, and whether testing on it is a purchase or a build. No source is named in the notes. Answer: NONE.`
   Conflicting source text: command 08, DECISION_LOG `[2026-11-05T23:50:09Z] WHO: amear`, typed: `1. Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands.` Command 10, WF spec :35 heads all of :36 `**Typed ruling 1** — RULED`. Command 09, DECISIONS :947: `**R-VN4-7** — proof of concept: ... / "We're just gonna proceed without that [historical tick data]."` Brief :15 (command 13): spending money waits for his explicit word.
   Why it breaks: v3 :183 calls only the first two sentences of :36 "Amear's typed words". It then gives the last three as what ":36 ends" with, and links them to R5 alone. Command 18 shows that "R-VN4-7" and "No tick purchase" appear only on v3 :183, inside that quotation. Item (k) asks whether getting real MNQ data is "a purchase", but it cites neither his standing "No tick purchase" nor R-VN4-7, which is his decision to proceed without historical tick data. R5 asks for real stop slippage to be measured, which the channel says 1-minute bars cannot show. That pushes toward tick data, against those two rulings. These are ruled texts, and the touch is missed. Whether MNQ data must be tick data is not settled anywhere, so this is a missed touch, not a proven conflict. That is why it is MED, not HIGH.

2. **MED, S2. v3 :184 says breaker #1's action "is built with" resting stops. The topology spec marks that row SPECIFIED, and the pieces it depends on are unbuilt.**
   v3 :184: `Breaker #1's "cancel all, flatten" action is built with "resting stops on every live position", citing R-VN4-2 as "Until the account is live … resting stops."`
   Conflicting source text: command 10, topology HEAD :58, same row: `| SPECIFIED. No numeric threshold exists anywhere` and `An account-state feed from NT8 to Redis (unbuilt); EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt; ...)`. Phase 3 HEAD :11 (command 11): `zero implemented, zero tested, zero tested under failure.`
   Why it breaks: S2 says "Specified ≠ implemented". "Is built with" reports breaker #1's flatten action at a level above SPECIFIED. The topology bullet never gives the row's status. Two bullets later, v3 :186 says "All nine breakers stay SPECIFIED ONLY (:11)", which lessens the harm but does not fix the sentence. The fix is one word: "is specified with".

3. **LOW, requirement 1 (labelling). Two ruling headings state as his ruling what the reading below them assigns to the channel or the filer.** v3 :61: `**R7 — Q4, the target account: prop firms stay out; $10,000 personal account; ...` against v3 :69: `that it is a personal account is the channel's parenthetical.` The same unlabelled "personal" also appears in v3 :170 (`a $10,000 personal account (R7)`) and v3 :182 (`R7 (a $10,000 personal account)`). v3 :152 heads R12 `The MFFU email: hand it to the master`, while v3 :156 says the referent of "those" is the filer's reading. This is LOW, not MED: brief :31 (command 13) put Q4 to him as "A personal cash account, and at what size?", and the R12 heading follows notes :118.

4. **LOW, S6 / S2. WF spec :31's "Revisit if a personal account is used." is D-2026-11-05-A item 3, a ruled item, but v3 :183 presents it as spec text.** v3 :183: `(:31-:32; :31 says "Revisit if a personal account is used."), which R7 bears on.` Command 09: DECISIONS :803 heads D-2026-11-05-A, "Walk-forward design rulings (Amear, voice 2026-11-05)". Its :814 carries the same item 3 words, which the entry marks as REPORTED BY the voice agent. R7's account may be the very trigger of that clause. The touch is named, so this is LOW. The source is understated.

5. **LOW, S6. D-2026-11-14-B R9 (HEAD :2586, "Process instructions") is missing from the v3 :178 bullet.** Command 10 prints :2586. Its readings, (a) anything ambiguous goes back as a voice brief and (b) a voice-brief skill is created (HEAD :2591, command 10), bear on this entry's R10 (the skill `Praxis_build-61o` stays parked) and on T1's "If a source spec has no stop, don't decide anything: bring it back to me." Command 18 finds 0 matches for "R9 of D-2026-11-14-B" or "D-2026-11-14-B R9".

6. **LOW, requirement 7 / S5 (filer authority). v3 :3 says the brief was `filed with this entry at the master's dispatch of this unit`, and no row records that dispatch.** Command 07: DISPATCH_LOG has 0 rows that name `voice-brief-open-questions` or `2026-11-15-rulings-filing`. DECISION_LOG has 1 row, 13:30:00Z, and that is the row that wrote the brief. Row 14:38:00Z (command 06), which is the dispatch, lists only "the notes plus the 14:37:18Z typed ruling". The entry names the difference, but it still states the dispatch instruction as fact, without a ledger row for it. The authority is the master's, not Amear's, so this is LOW.

7. **LOW, S8. v3 :44 says "Q1 of D-2026-11-14-B is answered as wait-for-data", and v3 :178 says D-2026-11-14-B R8 "is confirmed by this entry's R4".** "Confirmed" is the channel's heading (notes :35, command 14: `## 4. Q1, daily-loss cap: wait-for-data, confirmed (W1)`). Q1 (DECISIONS :2595, brief :27) set "wait for data" against "a multiple of the cost of a trade". His words (notes :38, "I can't set a number right now", the figure "depends on" a proven strategy) reject a number now. They do not address the multiple-of-cost form. This is a likely reading and close to what he said, so it is LOW. But it should be labelled as the filer's reading.

8. **LOW, S2. v3 :181: `and the cost model stays $2.96`.** HEAD :970 (command 09) ends that clause with "pending Amear" (and "fee report NEEDS AMEAR"). Leaving that out makes the $2.96 read as settled.

9. **LOW, requirement 1 (attribution).** v3 :121: `He said a design with no known maximum loss is "not compatible".` What "not compatible" refers to comes from the channel's lead-in (notes :92: "On the design having no known max loss:"). His words are only "Then that's not compatible. ...". Also, v3 :121 (`His typed ruling T1, below, refines this section.`) and v3 :162 (`as T1 refines it (D2)`) use "refines", while v3 :135 says `This entry does not read T1 as replacing notes section 9, or section 9 as limiting T1.` "Refines" leans toward T1 governing, a little. Requirement 3(b) uses the same verb, which is why this is LOW.

10. **LOW, S8. The skill half of the brief's Topic 3 has no open item.** v3 :148: `no resume word of his is recorded ... so the park rule's default holds and the bead is as it was. That fact does not answer the brief's options (brief :48)`. His answer, "I don't fucking give a shit, to be honest." (notes :110), picks none of A, B or C. The brief (:49) gives the master's view that the skill fix is "paperwork only". One reading of his indifference is that he leaves it to the master. Item (n) covers only the gap fade. The park-rule default is a true statement of record, so this is LOW. An open item for `61o` would match how (n) handles `vn4`.

11. **LOW, S6. Phase 3 Block 1 :54 places "a stop-market entry with a bracket (stop-loss + take-profit)", a resting broker stop at entry.** That fits T1's stop "sitting at the broker and placed at entry", and it sits against ruling 1's "Not a resting stop in the backtest." v3 :186 cites :54 only for having "no sizing rule". Item (o) already carries the T1-versus-ruling-1 question, so the effect is small.

## What survived

- All 20 fenced blocks are byte-identical to their cited sources: 19 against the cited `sed -n` lines of the notes, and T1 against the 14:37:18Z extraction (command 02). The block specs match the citations in the entry (command 03).
- All inline double-quoted strings were found byte-exact in a source (command 05; the one NOT-FOUND is a false positive). I spot-checked the attribution of each to its named source: rows, notes, brief, DECISIONS, the WF spec, the values spec, the Phase 3 spec, the topology spec and the ruleset. They match.
- HEAD citations checked (commands 09-12): DECISIONS :803, :814, :881, :907, :908, :924, :936, :937, :947, :970, :1735-:1740, :2367, :2426, :2431, :2433, :2459, :2468, :2470, :2481, :2482, :2488-:2493, :2527, :2533, :2540, :2546, :2555, :2560, :2562, :2572, :2580, :2586, :2593, :2595, :2600; topology :58; WF spec :31, :35, :36, :67, :74; values :51, :73, :124; Phase 3 :11, :54, :64, :76, :82, :97-:103, :138-:140, :145; ruleset :48, :50, :57, :59-:61, :64; rubric :19, :33-:35, :42; recheck :9-:11. Every one new in v3 matches: DECISIONS :907, :908, :936, :937, :2488-:2493, :2533, :2555, :2560, :2562; topology :58; WF spec :74.
- Status, authority and timing: row 14:37:18Z is WHO: amear, HOW: typed. Rows 13:30:00Z, 14:37:18Z and 14:38:00Z are absent at HEAD (count 0) and are the last rows in the working copy (command 06). The WHEN mismatches the entry names are real. The notes are 131 lines, which is 128 at intake plus the 3 lines the entry discloses. Notes :122 holds the two bracketed placeholders.
- S8 items (a)-(e) are present and say "Answer: NONE". (d) keeps F4 FROZEN and says the notes' reading does not unfreeze it. (c) quotes the row's hold byte-exact.
- The 5% is a placeholder "while no money is at stake". No breaker value is changed. The entry claims nothing as run, changed or lifted. No at-sign appears in the artifact or the notes, and no MFFU person is named (command 19). The S13 sentence appears once and is the last line (command 19).
- The brief's hash is unchanged.

## Result: FAIL

Two MED findings are open: new finding 1 (S6: typed ruling 1's "No tick purchase. R-VN4-7 stands." is not tested against R2, (k) or R5) and new finding 2 (S2: "is built with" against a SPECIFIED breaker row). There are 9 LOW findings and no HIGH. All 19 prior findings are CLOSED.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
