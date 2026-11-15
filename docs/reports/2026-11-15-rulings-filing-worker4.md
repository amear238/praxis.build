# 2026-11-15 rulings-filing, worker 4: adversarial review of draft D-2026-11-15-A v2

## Task

Unit `2026-11-15-rulings-filing`. Break the v2 draft of DECISIONS.md entry D-2026-11-15-A (scratch file `entry-v2-under-test.md`, 192 lines, sha256 a250690734db407af696911f969957ba5101f99e438b1541af2a7fe4f98a9bf9; command 01). Part 1: mark each of the prior reviewer's findings 1-9 (worker 2 report, "## Findings" only) CLOSED or OPEN in v2. Part 2: a fresh full attack against S2, S5, S6, S8, S13 and unit requirements (1)-(7). Read-only. No git index touched, no file edited except this report.

## Mode: ADVERSARIAL

The scripts used are printed in full by commands 02 and 04 (both kept in the session scratchpad, folder `w4`). Every command below was run by one bash runner that prints `$ <command>` with printf and then the untrimmed output. At-signs in ledger, brief and HEAD text are masked in the command itself (`tr '\100' '#'`). One HEAD at-sign is masked this way: ruleset :59 ("Stop # Opp. Band" in command 09; the HEAD byte is an at-sign).

## Commands and output

### Command 01

```
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse --short HEAD && shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md docs/reports/2026-11-15-voice-brief-open-questions.md && wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md docs/reports/2026-11-15-voice-notes-open-questions.md && git status --porcelain -- docs/reports/2026-11-15-voice-notes-open-questions.md docs/reports/2026-11-15-voice-brief-open-questions.md
d9fc5f0
a250690734db407af696911f969957ba5101f99e438b1541af2a7fe4f98a9bf9  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md
87aff631ed033adac2e23b0636c3e77ea51a05b82b9b71447925236ad68c683a  docs/reports/2026-11-15-voice-brief-open-questions.md
     192 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md
     131 docs/reports/2026-11-15-voice-notes-open-questions.md
     323 total
?? docs/reports/2026-11-15-voice-brief-open-questions.md
?? docs/reports/2026-11-15-voice-notes-open-questions.md
```

### Command 02

```
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4/fences.py
import re,subprocess,sys
A=sys.argv[1]; N=sys.argv[2]
L=open(A,encoding='utf-8').read().split('\n')
i=0
while i<len(L):
    if L[i]=='```text':
        hdr=L[i-1]
        j=i+1
        while L[j]!='```': j+=1
        body='\n'.join(L[i+1:j])+'\n'
        m=re.findall(r"`sed -n '([^']+)'`",hdr)
        if m:
            out=subprocess.run(['sed','-n',m[-1],N],capture_output=True).stdout.decode()
            src="sed -n '%s'"%m[-1]
        elif 'grep -F' in hdr:
            row=subprocess.run(['grep','-F','[2026-11-15T14:37:18Z]','DECISION_LOG.md'],capture_output=True).stdout.decode()
            out=subprocess.run(['sed','-e','s/.*Verbatim: "//','-e','s/" Left unanswered by him.*//'],input=row.encode(),capture_output=True).stdout.decode()
            src='T1 grep|sed'
        else:
            out=None; src='NO-SOURCE'
        print('entry %d-%d  %-28s %s'%(i+2,j,src,'IDENTICAL' if out==body else 'DIFFERENT'))
        i=j
    i+=1
```

### Command 03

```
$ cd /Volumes/Sensidine/Praxis.build && python3 -I -B /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4/fences.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md docs/reports/2026-11-15-voice-notes-open-questions.md
entry 9-11  sed -n '12,14p'              IDENTICAL
entry 15-17  sed -n '16,17p;19p'          IDENTICAL
entry 23-25  sed -n '23,25p'              IDENTICAL
entry 31-34  sed -n '29p;31,33p'          IDENTICAL
entry 40-42  sed -n '37,38p;40p'          IDENTICAL
entry 48-50  sed -n '44,45p;47p'          IDENTICAL
entry 56-57  sed -n '51p;53p'             IDENTICAL
entry 63-67  sed -n '57p;59p;61p;63,64p'  IDENTICAL
entry 75-79  sed -n '69,73p'              IDENTICAL
entry 85-85  sed -n '75p'                 IDENTICAL
entry 91-92  sed -n '77,78p'              IDENTICAL
entry 98-99  sed -n '81,82p'              IDENTICAL
entry 105-105  sed -n '86p'                 IDENTICAL
entry 109-109  sed -n '88p'                 IDENTICAL
entry 113-115  sed -n '91,93p'              IDENTICAL
entry 119-119  sed -n '95p'                 IDENTICAL
entry 125-125  sed -n '106p'                IDENTICAL
entry 131-131  T1 grep|sed                  IDENTICAL
entry 145-146  sed -n '110,111p'            IDENTICAL
entry 154-154  sed -n '120p'                IDENTICAL
```

### Command 04

```
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4/inline.py
import re,sys,glob,os
A,W=sys.argv[1],sys.argv[2]
corp={os.path.basename(p):open(p,encoding='utf-8').read() for p in glob.glob(W+'/HEAD_*')+[W+'/rows.txt',W+'/notes.md',W+'/brief.md']}
L=open(A,encoding='utf-8').read().split('\n'); inf=False
for n,l in enumerate(L,1):
    if l.startswith('```'): inf=not inf; continue
    if inf: continue
    s=re.sub(r'`[^`]*`','',l)
    for q in re.findall(r'"([^"]+)"',s):
        hits=[k for k,v in corp.items() if q in v]
        print('%3d %-9s %s | %s'%(n,'OK' if hits else 'NOTFOUND',q[:90],','.join(sorted(hits))[:80]))
```

### Command 05

```
$ cd /Volumes/Sensidine/Praxis.build && W=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4 && for f in DECISIONS.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-phase3-build-specification.md docs/specs/2026-07-16-b2-noise-area-ruleset.md specs/SPEC_RUBRIC.md docs/reports/2026-11-14-r3-recheck-manager.md; do git show HEAD:$f > $W/HEAD_$(basename $f); done && grep -F -e '[2026-11-15T13:30:00Z]' -e '[2026-11-15T14:37:18Z]' -e '[2026-11-15T14:38:00Z]' DECISION_LOG.md > $W/rows.txt && cp docs/reports/2026-11-15-voice-notes-open-questions.md $W/notes.md && cp docs/reports/2026-11-15-voice-brief-open-questions.md $W/brief.md && python3 -I -B $W/inline.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md $W
  3 OK        Read: | notes.md
  3 OK        Read: | notes.md
  3 OK        Okay, then that's what we use. | notes.md
  3 OK        Uh, yeah. | HEAD_DECISIONS.md,notes.md
  3 OK        Consequence (the agent's reading, not ruled) | notes.md
  3 OK        this channel's check, not Amear's rulings | notes.md
  3 OK        As the voice agent read it | notes.md
  3 OK        Filer's reading | HEAD_DECISIONS.md
 13 OK        He settled it for Noise-Area in section 9 | notes.md
 19 OK        in multiple ways | notes.md
 19 OK        Yeah, one at a time. | notes.md
 19 OK        Best candidate | notes.md
 19 OK        That's fine. Keep going. | notes.md
 19 OK        I want the uh, you know, the highest return one. | notes.md
 19 OK        I'm I'm looking for steady first. | notes.md
 19 OK        steady first | notes.md,rows.txt
 19 OK        steady first | notes.md,rows.txt
 19 OK        I still want the top three | notes.md
 27 OK        MNQ derived, not an MNQ run | HEAD_2026-11-14-r3-recheck-manager.md,notes.md
 36 OK        exhaustive enough so that this loop can actually be ran um, reliably | notes.md
 36 OK        Yeah. | notes.md
 38 OK        Read: | notes.md
 44 OK        Okay, then that's what we use. | notes.md
 44 OK        stop-market order, sitting at the broker, placed at entry | notes.md
 44 OK        a stop limit set order at a level | notes.md
 44 OK        Okay, then that's what we use. | notes.md
 44 OK        stop-market order, sitting at the broker and placed at entry | rows.txt
 46 OK        not ruled | HEAD_2026-11-05-walk-forward-spec.md,HEAD_DECISIONS.md,notes.md
 52 OK        as long as it's predetermined and calculated | notes.md
 52 OK        calculated | HEAD_2026-11-05-phase3-build-specification.md,notes.md
 59 OK        considering | notes.md
 59 OK        Whatever 1% is right now | notes.md
 61 OK        So prop firms stay out for now. | notes.md
 61 OK        Account size: | notes.md
 61 OK        (personal account, $10,000) | notes.md
 61 OK        MFFU written-confirmation follow-up: | notes.md
 61 OK        See section 12: MFFU had already answered. | notes.md
 73 OK        Read: | notes.md
 89 OK        Then: | HEAD_DECISIONS.md,notes.md
 94 OK        for now | HEAD_DECISIONS.md,brief.md,notes.md
 94 OK        from peak | notes.md
 94 OK        Fact given in the call | notes.md
 96 OK        The agent recorded: | notes.md
101 OK        I can't set these rules without backtesting | notes.md
111 OK        Uh, yeah. | HEAD_DECISIONS.md,notes.md
117 OK        Amear did not object. | notes.md
117 OK        Confirm the version name with him. | notes.md
121 OK        they should all be | notes.md
121 OK        And by the way, that's a question. | notes.md
121 OK        not compatible | notes.md
121 OK        I'm I'm looking for steady first. | notes.md
127 OK        at 1 MNQ | HEAD_2026-11-05-walk-forward-spec.md,HEAD_2026-11-06-walk-forward-values.md,HEAD
127 OK        MNQ derived, not an MNQ run | HEAD_2026-11-14-r3-recheck-manager.md,notes.md
129 OK        the combined reply for option 4 | rows.txt
133 OK        No loose or interval-checked exits. | rows.txt
136 OK        Uh, yeah. | HEAD_DECISIONS.md,notes.md
136 OK        keep the strategy's exit, add a hard stop-market order at entry | notes.md
136 OK        No loose or interval-checked exits. | rows.txt
136 OK        Evaluated only at semi-hourly stamps | HEAD_2026-07-16-b2-noise-area-ruleset.md
136 NOTFOUND  every  /  | 
136 OK        Position closes as soon as price crosses the current band **or** the VWAP. | HEAD_2026-07-16-b2-noise-area-ruleset.md
137 OK        they should all be | notes.md
137 OK        Retest depends on the original source spec | rows.txt
137 OK        the source spec has a stop and our test ran without one | rows.txt
138 OK        If a source spec has no stop, don't decide anything: bring it back to me. | rows.txt
139 OK        maybe test like another candidate that seems promising | notes.md
139 OK        One at a time, Noise-Area first. | rows.txt
139 OK        Yeah, one at a time. | notes.md
140 OK        each of the five | HEAD_2026-11-14-r3-recheck-manager.md,rows.txt
140 OK        For each of the five | HEAD_2026-11-14-r3-recheck-manager.md,rows.txt
140 OK        already retired | HEAD_DECISIONS.md,brief.md
141 OK        Noise-Area | HEAD_2026-07-16-b2-noise-area-ruleset.md,HEAD_2026-11-05-phase3-build-specificat
141 OK        steady first | notes.md,rows.txt
141 OK        Left unanswered by him | rows.txt
143 OK        No word to resume, so it **stays parked**. | notes.md
143 OK        No separate ruling. | notes.md
143 OK        Amear said | HEAD_DECISIONS.md,notes.md
148 OK        Okay. | notes.md
150 OK        not Amear's rulings | HEAD_DECISIONS.md,notes.md
150 OK        at 1 MNQ | HEAD_2026-11-05-walk-forward-spec.md,HEAD_2026-11-06-walk-forward-values.md,HEAD
156 OK        looks like | HEAD_2026-11-05-phase3-build-specification.md,notes.md
161 OK        steady first | notes.md,rows.txt
161 OK        Left unanswered by him | rows.txt
162 OK        they should all be | notes.md
164 OK        Left unanswered by him | rows.txt
168 OK        Read: | notes.md
169 OK        I still want the top three | notes.md
172 OK        best candidate | notes.md
172 OK        the highest return one | notes.md
172 OK        steady first | notes.md,rows.txt
172 OK        That's fine. Keep going. | notes.md
173 OK        Okay, then that's what we use. | notes.md
177 OK        walk-forward runs on existing strategies | HEAD_DECISIONS.md
177 OK        the top three | notes.md
178 OK        the three Noise-Area arms and Last-Half-Hour Momentum | HEAD_DECISIONS.md
178 OK        at 1 MNQ for at least one MFFU account size | HEAD_DECISIONS.md
181 OK        Revisit if a personal account is used. | HEAD_2026-11-05-walk-forward-spec.md,HEAD_DECISIONS.md
181 OK        evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2 | HEAD_2026-11-05-phase3-build-specification.md,HEAD_2026-11-05-walk-forward-spec.
181 OK        Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands. | HEAD_2026-11-05-walk-forward-spec.md,HEAD_DECISIONS.md
181 OK        1-minute bars cannot show where a real fill would have landed | notes.md
182 OK        none (the paper has no stop; §1) | HEAD_2026-11-06-walk-forward-values.md
182 OK        Max drawdown ≤ 4% of equity | HEAD_2026-11-05-phase3-build-specification.md,HEAD_2026-11-05-walk-forward-spec.
183 OK        stop-loss + take-profit | HEAD_2026-11-05-phase3-build-specification.md,HEAD_DECISIONS.md
183 OK        through Rithmic | HEAD_2026-11-05-phase3-build-specification.md
183 OK        Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96  | HEAD_2026-11-05-phase3-build-specification.md
183 OK        cancel all, flatten, disable for session | HEAD_2026-11-05-phase3-build-specification.md
183 OK        2 consecutive losers in one session → identical to max trades | HEAD_2026-11-05-phase3-build-specification.md,HEAD_DECISIONS.md
183 OK        MFFU’s $1,500 EOD trailing drawdown | HEAD_2026-11-05-phase3-build-specification.md,HEAD_2026-11-05-walk-forward-spec.
183 OK        Account drawdown exceeds 60% of MFFU trailing DD room | HEAD_2026-11-05-phase3-build-specification.md
183 OK        0.5% per trade | HEAD_2026-11-05-phase3-build-specification.md
183 OK        Max drawdown ≤ 4% of equity | HEAD_2026-11-05-phase3-build-specification.md,HEAD_2026-11-05-walk-forward-spec.
184 OK        Evaluated only at semi-hourly stamps | HEAD_2026-07-16-b2-noise-area-ruleset.md
184 OK        Before anything else | rows.txt
184 OK        No loose or interval-checked exits. | rows.txt
184 OK        as soon as | HEAD_2026-07-16-b2-noise-area-ruleset.md,HEAD_DECISIONS.md
186 OK        still worth chasing | HEAD_DECISIONS.md,brief.md,notes.md
190 NOTFOUND  WHEN:  14:37:18Z | 
190 NOTFOUND  WHEN:  13:25:51Z | 
190 OK        the voice channel | rows.txt
190 OK        the Claude.ai Praxis project channel | notes.md,rows.txt
```

### Command 06

```
$ awk 'NR==3||NR==13||NR==19||NR==44||NR==59||NR==94||NR==111||NR==121||NR==127||NR==133||NR==148||NR==163||NR==166||NR==173||NR==176||NR==181||NR==183||NR==184{printf "%d: %s\n",NR,$0}' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md
3: **Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, filed unchanged with this entry) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
13: Notes :16-:17 and :19 (`sed -n '16,17p;19p'`; the lead-in text on all three lines, and the sentence "He settled it for Noise-Area in section 9", are the channel's):
19: Filer's reading: testing is now one strategy at a time, not in bulk. The candidate is tested "in multiple ways", and every order is looked at. A second candidate waits for the first ("Yeah, one at a time."). Per the channel's lead-in (notes :17), "Best candidate" was asked twice (highest return, or best fit to his risk rules), and his reply was "That's fine. Keep going." That reply picks neither option; the filer does not read it as an answer. His own words point two ways: "I want the uh, you know, the highest return one." (notes :12) and "I'm I'm looking for steady first." (notes :95). By the channel's table (notes :101, the channel's figures, not re-derived here), OppBand has the highest net and Flat1559 the lowest. That tension is named, not resolved (item (l) below). That it was settled for Noise-Area as "steady first" is the channel's lead-in (notes :17). Which version "steady first" names is still open (item (a) below). His "I still want the top three" (notes :12) is recorded as said. How it fits with one-at-a-time testing and with the three-contender pause of D-2026-11-13-D is named under S6, not resolved.
44: Filer's reading: Q1 of D-2026-11-14-B is answered as wait-for-data. No daily-loss figure is set; he says it depends on a strategy proven with the broker he goes with. On order type, his "Okay, then that's what we use." answers the explanation of a stop-market order. The channel reads this as "stop-market order, sitting at the broker, placed at entry" (notes :40). The ruling sits in notes section 4, headed for the daily-loss cap (notes :35), and :37 speaks of "a stop limit set order at a level". Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick. T1 uses the same "stop-market order, sitting at the broker and placed at entry" wording for the retest stop; that is named, not read as settling it.
59: Filer's reading: Q3 of D-2026-11-14-B is answered: the percentage is taken on the current balance, "considering" the prop-firm drawdown limits if the account is through a prop firm. The 1% appears in his answer, "Whatever 1% is right now" (notes :51), to the example (notes :53). The filer does not read it as setting R3's percentage of D-2026-11-14-B, which that entry leaves TBD. Whether 1% per trade is now ruled is listed as open (item (g) below).
94: Filer's reading: 5% is Amear's placeholder "for now". He called the figure a guess and said it depends on the strategy. It is a placeholder while no money is at stake. The words "from peak" are the channel's reading (notes :78), not his words. Where the 5% is measured from is open (item (h) below). The losing-run facts on :78 ("Fact given in the call") are the voice agent's and the channel's. No breaker value is changed by this placeholder or by anything in this entry. Changing a breaker value while real money is at stake waits for Amear's explicit word (brief :15).
111: Notes :91-:93 (`sed -n '91,93p'`; :92's first sentence is the voice agent's answer and its note on the paper; :93's AGENT PROPOSAL sentence is the voice agent's proposal, and its "Uh, yeah." is his):
121: Filer's reading: the channel reads "they should all be" as retested, and flags it AMBIGUOUS (notes :88). Amear asked, as a question, whether the strategies should be specced from their source and retested with stop losses (notes :91, "And by the way, that's a question."). He said a design with no known maximum loss is "not compatible". He said yes to the voice agent's proposal to keep the strategy's exit, add a hard stop-market order at entry, and retest (notes :93). Noise-Area goes first. His words are "I'm I'm looking for steady first." (notes :95). That it names Flat1559 is the voice agent's mapping, and the version is open (item (a) below). His typed ruling T1, below, refines this section. Where the two differ, the differences are named after T1.
127: The channel's statement, not a filer's reading: per notes :106, the filed figures supersede the brief's UNVERIFIED net-profit figures (brief :40). That statement is the channel's; it is not re-derived or checked here. The brief is filed unchanged, with those figures still in it. Section 11 of the notes (the channel's check, :116) also says the brief labels its loss figures "at 1 MNQ" (brief :34), while the source labels them "MNQ derived, not an MNQ run". The difference is named here, not resolved. The brief is not edited.
133: Filer's reading: the retest of each of the five depends on its source spec. Where the source spec has a stop and our test ran without one, the strategy is retested with a stop-market order at the broker, placed at entry, so the maximum loss is known before the trade. T1's own words are "No loose or interval-checked exits."; what they exclude is D1 below, open (item (f)). One strategy at a time, Noise-Area first. Before any retest, the original paper is read for whether Noise-Area has a hard stop, and its exact wording is reported. A source spec with no stop goes back to Amear, and nothing is decided on it.
148: Filer's reading: the voice-brief skill (`Praxis_build-61o`) stays parked. He gave no word to resume it, and the park rule says a person resumes it (brief :46). The gap fade (`Praxis_build-vn4`) stays parked. His "Okay." accepts that it is retested with a real stop after Noise-Area under Q6. Under T1, whether and how it is retested depends on its source spec (D5 above). No bead is changed.
163: - (c) What the Noise-Area paper says about a stop, in its exact wording. T1 orders this read before any retest. Per row 14:38:00Z, the master dispatches that read only after this entry is committed. Answer: NONE.
166: - (f) (the filer's addition) Where T1 and notes section 9 differ (D1-D6 above), which governs. Answer: NONE.
173: - (m) (the filer's addition) Which order his "Okay, then that's what we use." (notes :40, in notes section 4, headed for the daily-loss cap, :35) covers: the per-trade stop, the daily-loss cap, or both. Answer: NONE.
176: - D-2026-11-14-B (DECISIONS.md :2527-:2615 at HEAD). These rulings answer its Q1-Q6 (:2595-:2600): Q1 by R4, Q2 by R5, Q3 by R6, Q4 by R7, Q5 by R8 and Q6 by R9 and T1. That entry is not edited. R2 (:2540, prop firms set aside for now) is kept by R7. R3 (heading :2546; the filer's reading at :2553) leaves the percentage TBD; R6 answers which balance it uses, and whether 1% is set is open (g). R7 (:2572, the max-trades number comes from backtest data) is untouched. R8 (:2580, the daily-loss cap waits for data) is confirmed by R4. Not amended.
181: - Walk-forward spec (`docs/specs/2026-11-05-walk-forward-spec.md`, HEAD text; the file is modified in the working tree and that text is not used). The gate base and the per-window drawdown are stated against MFFU (:31-:32; :31 says "Revisit if a personal account is used."), which R7 bears on. Arm (b)'s stop is "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (:36, quoted again at :74). R4 and T1 call for a stop-market order at the broker, placed at entry, with no interval-checked exits. The same :36 ends "Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands." R5 counts slippage past the stop in the cost of the trade once it is measured by enough testing, and the channel's check (notes :115) says "1-minute bars cannot show where a real fill would have landed". Named, not resolved. Arm (a) runs with no added stop (:67, marked INFERRED there). Not amended.
183: - Phase 3 spec (`docs/specs/2026-11-05-phase3-build-specification.md`, HEAD). Block 1 names a bracket "stop-loss + take-profit" with no sizing rule (:54). Block 2 takes historical data over the MFFU connection, "through Rithmic" (:64), and its backtest runs at "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract" (:76). R2 (real MNQ data, where :76 names NQ), R5 (stop slippage counted in the cost of the trade, where :76 names slippage on entries) and R7 (prop firms out, where :64 routes the data through the MFFU connection) bear on these. Named, not resolved. Breaker #1, daily loss (:97): R4 sets no value. Breaker #1 is a software action, "cancel all, flatten, disable for session" (:97), not a resting broker order. If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved. Breaker #2, max trades (:98): untouched. Breaker #3, "2 consecutive losers in one session → identical to max trades" (:99): R8(d)'s variable keeps trading after two losses at 0.5% risk. That is a direct tension with #3, named and not resolved; R8(d) is a variable to test, not a rule. Breaker #4 (imported :100, amended to a 16:00 ET session flat at :208-:212): R8(b) says the hard stop time depends on the strategy. Breaker #5, the afternoon session window (:101), is a fixed clock window; R8(b) bears on it the same way. Breaker #6, trailing drawdown proximity to "MFFU’s $1,500 EOD trailing drawdown" (:102), and the kill criterion "Account drawdown exceeds 60% of MFFU trailing DD room" (:145): R7 and R8(c) bear on both. Sizing: stages A and B size by a fixed contract (:138-:139), and stage C sizes at "0.5% per trade" (:140). R6's current balance and the 1% in his words (open (g)) bear on :140. Breaker #7, max position size (:103), rejects a quantity above plan; R6's current-balance sizing and R8(d)'s 1% to 0.5% variable change the quantity per trade, so what the plan is under them is not said. Named, not resolved. The Block 2 gate "Max drawdown ≤ 4% of equity" (:82) is as above. No breaker value is changed. All nine breakers stay SPECIFIED ONLY (:11). Not amended.
184: - Noise-Area ruleset (`docs/specs/2026-07-16-b2-noise-area-ruleset.md`, HEAD). Its exit section is marked PAPER-VERIFIED (:57). The base stop is a trailing stop at the opposite band, "Evaluated only at semi-hourly stamps" (:59). The improved stop trails at band-or-VWAP (:60-:61). The only time exit is 16:00 (:64), and there is no ATR stop anywhere in the paper (:50). T1 orders the paper read "Before anything else", with the exact wording reported, and says "No loose or interval-checked exits." (what that excludes is D1, open). The checkpoint grid (:48) and the "as soon as" wording of the improved stop (:61) are named under D1. Whether the ruleset's reading meets T1's order is not decided here; the master dispatches the read after this entry (row 14:38:00Z). Not amended.
```

### Command 07

```
$ cd /Volumes/Sensidine/Praxis.build && for t in '[2026-11-15T13:30:00Z]' '[2026-11-15T14:37:18Z]' '[2026-11-15T14:38:00Z]'; do grep -F "$t" DECISION_LOG.md | tr '\100' '#'; done; grep -c -F '[2026-11-15T' DECISION_LOG.md; git show HEAD:DECISION_LOG.md | grep -c -F '[2026-11-15T'; tail -c 120 DECISION_LOG.md
- [2026-11-15T13:30:00Z] WHO: praxis-master | WHAT: **Amear asked "check the inbox then give me handoff for voice man".** Inbox check, OBSERVED this turn: Gmail connector failed to connect this session (ENOTFOUND), so his mail was not read; Hermes gateway.log has no inbound Telegram message after 2026-11-13 20:21:51 ("Halt all runs until further notice"); newest `vm/replies/` file 20261111T172940Z; no commit on any branch since 59f5ce4; repo files changed since the park: DISPATCH_LOG.md and .claude/state/handoff-latest.md only. Loop state: `hermes cron list` printed "No scheduled jobs."; `~/.hermes/cron/jobs.json` shows praxis-search-loop (73d67fad7ec9) and praxis-build-loop (5be233e3ac6c) enabled False, state paused. Master writes voice brief `docs/reports/2026-11-15-voice-brief-open-questions.md` following the on-disk voice-brief skill (approved by Amear 2026-11-14T16:05:30Z; file parked on parked/Praxis_build-61o, not on main; used as a format guide, not claimed installed). Filter: Q1-Q6 of D-2026-11-14-B (rulings left open, HEAD DECISIONS.md :2593-:2600) pass test 3; resuming the search loop passes test 3 (his reserved word, row 2026-11-14T14:49:30Z); resuming parked `61o`/`vn4` passes as a park-rule human resume (rubric :264-:278). Settled and dropped: "Mac pre-screen acceptable" (HANDOFF :51), settled by R5 (HEAD DECISIONS.md :2562-:2570). No commit this act; the brief stays in the working tree for the next flush. | WHY: Amear's request; R9(a) | WHERE: docs/reports/2026-11-15-voice-brief-open-questions.md | WHEN: `date -u` 13:25:51Z | HOW: master writes report | STATE: written
- [2026-11-15T14:37:18Z] WHO: amear | WHAT: **Amear's typed Q6 ruling in the master session** (pasted by him as "the combined reply for option 4", after he declined the master's three-question prompt in order to clarify). Verbatim: "Retest depends on the original source spec. For each of the five, go back to where the strategy was found and check what it specified. If the source spec has a stop and our test ran without one, retest it and recheck it with a proper stop-market order, sitting at the broker and placed at entry, so the maximum loss is known before the trade. No loose or interval-checked exits. One at a time, Noise-Area first. / Before anything else, confirm from the original paper (Zarattini, Aziz and Barbon, "Beat the Market", Swiss Finance Institute 24-97) whether the Noise-Area strategy has a hard stop. The project's research summary says it uses a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss. Report what the paper actually says, with the exact wording, before any retest. If a source spec has no stop, don't decide anything: bring it back to me." Left unanswered by him in this session: whether "steady first" names Flat1559 (notes :95); how the MFFU email reaches the repo (Gmail connector failed to connect this session; F4 stays FROZEN). | WHY: S5 authorisation record | WHERE: master session | WHEN: `date -u` 14:37:18Z | HOW: typed | STATE: recorded
- [2026-11-15T14:38:00Z] WHO: praxis-master | WHAT: **Intake of `docs/reports/2026-11-15-voice-notes-open-questions.md` (128 lines, untracked, written by the Claude.ai Praxis project channel from Amear's voice call 08:30-09:27 ET) and dispatch of unit `2026-11-15-rulings-filing`.** One praxis-manager files the notes plus the 14:37:18Z typed ruling as DECISIONS.md entry D-2026-11-15-A, WHO: amear, REPORTED BY the voice channel, through a temp index at HEAD d9fc5f0. Sequencing for S4: the Noise-Area paper read that Amear ordered is NOT dispatched until this entry is committed. Decided by master under D-2026-11-08-D D1: (i) the notes carry the MFFU rep's first name and a support address on 1 line (:122; count only); the filer replaces both with bracketed placeholders before first commit and discloses the count, per the standing rule; (ii) the notes state P&L figures without the S13 sentence; the filer appends it once with a filer's note. Open and not answered: Flat1559 reading; MFFU email route. F3 and F4 stay FROZEN. | WHY: Amear's rulings; S4, S5, S8 | WHERE: DECISIONS.md; /tmp/praxis-r15/idx | WHEN: `date -u` 14:37:18Z | HOW: one praxis-manager, background | STATE: dispatched
3
0
DECISIONS.md; /tmp/praxis-r15/idx | WHEN: `date -u` 14:37:18Z | HOW: one praxis-manager, background | STATE: dispatched
```

### Command 08

```
$ cd /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4 && awk 'NR==907||NR==936||NR==970||(NR>=1735&&NR<=1740)||NR==2367||NR==2426||NR==2431||NR==2433||NR==2459||NR==2468||NR==2470||NR==2481||NR==2482||(NR>=2488&&NR<=2493)||NR==2527||NR==2540||NR==2546||NR==2553||NR==2572||NR==2580||(NR>=2595&&NR<=2600)||NR==2615{printf "%d: %s\n",NR,substr($0,1,330)}' HEAD_DECISIONS.md | tr '\100' '#'
907: - Ruling 1 (`2026-11-05T23:50:09Z`, typed): *"Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest."*
936: - **R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
970: - (iii) R-VN4-6 with the fee report (`docs/reports/2026-11-05-mffu-fee-check.md:7-10`): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM. The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear (DECISION_LOG `2026-11-05T23:59:40Z`, `2026-11-06T00:06:48Z`; fee report NEEDS AME
1735: A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
1736:     of the ruled limit, i.e. below the lower of 3.2% of the MFFU
1737:     account size and 80% of MFFU's trailing drawdown limit. This
1738:     amends D-2026-11-05-A item 3 with a safety buffer for model error.
1739:     Evaluated against every tier row; tier pick stays Q9. Closes the
1740:     notes-4 DD equity-base item.
2367: ## 2026-11-13 — D-2026-11-13-D: Amear's rulings of the 2026-11-13 evening (research screen, build pause, search loop in Claude Code, trade-count gap, in-VM rule). Filed WHO: amear, REPORTED BY the Claude.ai channel.
2426: **Ruling 2: builds paused.** The pause is defined at handoff :53-:55 (the channel's text). New build units stop: NinjaScript for the trading path, breakers, monitor, n8n workflows, and walk-forward runs on existing strategies. These carry on: the step 2 filing, the step 4 search loop and its backtests, ledger and close flushes, 
2431: The pause ends when the loop records its third contender (handoff :55). Which contender goes forward is a strategy decision and stays with Amear (handoff :55). By the same line, no agent decides it.
2433: **Ruling 3: the search loop runs in Claude Code.** Amear's words: "Have the loop run within Claude Code" (handoff :9). The handoff places it "in Claude Code on the Mac" (handoff :57) and sends its backtests to the VM bridge through Hermes over SSH (handoff :64). Finding, recorded and not repaired: handoff :64 says the runs are "
2459: ## 2026-11-13 — D-2026-11-13-E: Strategy search loop contender bar and overfitting guard (PROPOSED BY the Claude.ai channel; master under D-2026-11-08-D D1)
2468: **Skip** anything already backtested: the three Noise-Area arms and Last-Half-Hour Momentum. Ideas screened out earlier only because they lacked peer-reviewed evidence are back in scope, because that screen is gone. This includes gap fade, VWAP or Bollinger reversion, and opening-range breakout. The record of what came up before
2470: **Commission (hand step for Amear).** MFFU charges $4.68 round trip, but NT8 still has $2.96 set. Setting $4.68 is Amear's hand step. Send him one Telegram asking for it when the loop starts. Until it is set, label every result "screening, $2.96". **A candidate cannot become a contender until it has a $4.68 run.**
2481: 2. It has a full five-year backtest at $4.68 commission.
2482: 3. **It passes the drawdown gate at 1 MNQ for at least one MFFU account size.** The gate is in DECISIONS.md :1735-:1740: max drawdown stays below the lower of 3.2% of the account and 80% of MFFU's trailing limit. For a 50K account that is $1,600. Measure it the way the D6 check did (`docs/reports/2026-11-09-d6-drawdown-check-man
2488: **Overfitting guard (PROPOSED).** Without peer review, the main risk is finding a lucky fit. So:
2489: 
2490: - Each idea is tuned only on 2021-03-08 to 2024-12-31.
2491: - Its rules are then frozen and run once on 2025-01-01 to 2026-07-17.
2492: - Allow no more than three parameter variants per idea, and log every variant tried, including the failures.
2493: - Walk-forward testing under the existing spec comes later, for whichever contender Amear picks.
2527: ## 2026-11-14 — D-2026-11-14-B: Amear's restructure rulings of the 2026-11-14 voice session (R1-R9). Filed WHO: amear, REPORTED BY the voice-chat agent.
2540: **R2 — Prop firms set aside for now.** Notes :15:
2546: **R3 — "The cost of the trade" is the number one rule.** Notes :19-:21 and :23 (`sed -n '19,21p;23p'`; :22 is the voice agent's confirmation and is left out; :23's lead-in is the voice agent's):
2553: Filer's reading: every trade has a maximum loss defined before entry, as a percentage of the account, counted as the trade's cost once it executes. The percentage is TBD and is not picked here. The reach of the exception is Q2; the balance it uses is Q3.
2572: **R7 — Max trades per session: rule exists, number set from backtest data.** Notes :37-:39:
2580: **R8 — Daily loss cap: rule exists, number set later from data.** Notes :43 (:42 is the voice agent's question):
2595: - **Q1, R8 wording.** His "Yeah" could mean "wait for data" or agree to "a multiple of the cost of a trade." Recorded as wait-for-data. Confirm.
2596: - **Q2, the R3 exception.** Is a stop filled past its level by a news gap or slippage still "the cost of the trade", or a breach like a server crash? It decides how the stop is sized and tested.
2597: - **Q3, which balance R3 uses.** Starting balance, current balance, or high-water mark?
2598: - **Q4, the target account.** With prop firms out "for now", what account does testing assume: a personal cash account, and at what size? Is the MFFU F4 follow-up still worth chasing?
2599: - **Q5, the rest of the Floor Rule.** Hard stop time, the account drawdown kill switch, and the post-win protocol were not ruled on today.
2600: - **Q6, R4 outcome.** Once the recheck is done: is any of the five worth rerunning with a hard stop, or are they dropped?
2615: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

### Command 09

```
$ cd /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/w4 && { awk 'NR==11||NR==54||NR==64||NR==76||NR==82||(NR>=97&&NR<=103)||(NR>=138&&NR<=140)||NR==145||NR==208||NR==212{printf "phase3 %d: %s\n",NR,substr($0,1,300)}' HEAD_2026-11-05-phase3-build-specification.md && awk 'NR==31||NR==32||NR==36||NR==67||NR==74{printf "wfspec %d: %s\n",NR,$0}' HEAD_2026-11-05-walk-forward-spec.md && awk 'NR==51||NR==73||NR==124{printf "wfvalues %d: %s\n",NR,$0}' HEAD_2026-11-06-walk-forward-values.md && awk 'NR==48||NR==50||NR==57||(NR>=59&&NR<=61)||NR==64{printf "ruleset %d: %s\n",NR,$0}' HEAD_2026-07-16-b2-noise-area-ruleset.md && awk 'NR==19||NR==31||NR==33||NR==34||NR==35||NR==42{printf "rubric %d: %s\n",NR,$0}' HEAD_SPEC_RUBRIC.md && awk 'NR==15||NR==34||(NR>=38&&NR<=40)||(NR>=44&&NR<=48){printf "brief %d: %s\n",NR,$0}' brief.md && awk 'NR>=9&&NR<=11{printf "recheck %d: %s\n",NR,$0}' HEAD_2026-11-14-r3-recheck-manager.md; } | tr '\100' '#'
phase3 11: > **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ implemented ≠ tested ≠ tested under failure. Basis, checked 2026-11-05: `grep -rniE "breaker|circuit" ninjascript/` returns one hit, 
phase3 54: NinjaScript fundamentals. The NQ Noise-Area strategy is mechanically simple: at a fixed time, check if price has broken above or below a calculated noise band, place a stop-market entry with a bracket (stop-loss + take-profit). In NinjaScript, that’s an OnBarUpdate() method that checks the time, c
phase3 64: What you’re doing: Validating the NQ Noise-Area strategy against historical data using NinjaTrader’s Strategy Analyzer. This is where the MFFU connection becomes necessary — not for live trading, but for historical data access through Rithmic.
phase3 76: The backtest itself: NinjaTrader Strategy Analyzer with the configuration already specified in the research. Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract. Rolling walk-forward optimization: 252-day in-sample / 63-day 
phase3 82: - Max drawdown ≤ 4% of equity
phase3 97: 1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
phase3 98: 2. Max trades per day — trade count hits daily max → disable order submission
phase3 99: 3. Consecutive loss (“two and done”) — 2 consecutive losers in one session → identical to max trades
phase3 100: 4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
phase3 101: 5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
phase3 102: 6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
phase3 103: 7. Max position size — order quantity exceeds plan → reject
phase3 138: |A — Micro |1 MNQ ($2/point)                  |2 weeks + 10 triggered trades|Live metrics within 1 standard error of paper   |
phase3 139: |B — Single|1 NQ ($20/point)                  |4 weeks + 20 triggered trades|Stats within 0.5σ of backtest median, no DD > 2%|
phase3 140: |C — Full  |Risk-model sizing (0.5% per trade)|Indefinite                   |—                                               |
phase3 145: - Account drawdown exceeds 60% of MFFU trailing DD room
phase3 208: ### Breaker #4 — amended
phase3 212: > 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session o
wfspec 31: - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
wfspec 32: - *"4. Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."*
wfspec 36: > "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands."
wfspec 67: - Item 1 adds the stop for arm (b): "A stop is added to the strategy for (b) on its own branch; baseline file unchanged." (`:812`). — RULED (D-2026-11-05-A). Arm (a) therefore runs with no added stop. — INFERRED (from item 1).
wfspec 74: - Stop: "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (typed ruling 1). — RULED.
wfvalues 51: | Stop-ATR multiplier m | none (the paper has no stop; §1) | {1.5, 2.25, 3.0}; stop distance m × ATR(14) | SETTLED — see below |
wfvalues 73: - **Level** (WF spec NEEDS AMEAR 27) — SETTLED: fixed at entry. Long: entry fill price − m × ATR(14); short: entry fill price + m × ATR(14), where m = `StopAtrMult` (§3), never the noise multiplier k. ATR is the value at the entry bar. Not trailing. A reversal starts a new level from the new entry. Alternative: measured from the signal bar's close, or a trailing level. Changeable by him.
wfvalues 124:   3. Max drawdown ≤ 4% of equity
ruleset 48: | Checkpoint grid | every `HH:00` / `HH:30` | §3 p. 9 |
ruleset 50: | Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
ruleset 57: ## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)
ruleset 59: - **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop # Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
ruleset 60: - **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
ruleset 61:   `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
ruleset 64: - **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
rubric 19: ### F3 — Backtest fill resolution vs. acquired data granularity
rubric 31: **Blocks.** `4uu`. Everything downstream of `4uu`.
rubric 33: ### F4 — MFFU automation compliance
rubric 34: **Criterion.** Written confirmation from MFFU that this specific automation
rubric 35: pattern is permitted on a funded account.
rubric 42: **Blocks.** Block 4. Block 5.
brief 15: - Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
brief 34:   Facts for Q6, at 1 MNQ, restated from the same report, :9-:13 and :17-:21:
brief 38:   - Last-Half-Hour Momentum (already retired): no stop, time exit only. Largest loss $555.40.
brief 39:   - Gap fade V2: a gap-sized stop, but only in a Python test rule. Largest loss $472.90.
brief 40:   - Net profit, UNVERIFIED: baseline about $17,824, OppBand about $19,719, Momentum minus $9,692.60. These are the master's figures from yesterday's session, and no filed report contains them. Treat them as rough until they are re-run.
brief 44: ## Topic 3. Two parked items: pick them up, or leave them?
brief 45: 
brief 46: - **Voice-brief skill** (`Praxis_build-61o`). He approved it. Both audits passed the skill file itself. Both failed on the job report: one command was shortened and one pasted output was trimmed. The park rule says a person resumes it.
brief 47: - **Opening gap fade** (`Praxis_build-vn4`). It failed its pre-screen on Nov 14. Q6 may settle it.
brief 48: Options: A. Resume both. B. Resume the skill only. C. Leave both parked.
recheck 9: | Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
recheck 10: | Noise-Area OppBand | opposite-band level, same checkpoint check, market exit | NO | −$1,960.90 | 6 | −$1,894.80 | 2 (1 if same-timestamp reversals are merged) |
recheck 11: | Noise-Area Flat1559 | as baseline, plus a 15:59 flat | NO | −$542.40 | 10 | −$683.70 | 5 |
```

### Command 10

```
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | awk 'NR==58{printf "topology %d: %s\n",NR,$0}' && grep -c -E 'R-VN4-2|topology|907|936|968|23:50:09Z' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md; grep -n -o -E 'R-VN4-2|topology|:907|:936|:968|23:50:09Z|2488|2492|overfitting|three parameter' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md
topology 58: | 1 | Daily loss limit | n8n gate node, before Write Signal File: Redis flag `gate:daily_loss` (closed when realised + unrealised P&L ≤ −threshold, or when the P&L reading is stale). Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes, plus resting stops on every live position (R-VN4-2: "Until the account is live … resting stops.", REPORTED BY the voice agent; the reading "resting stops once live" is the voice agent's, Phase 3 import :24–25) [E27]. | The gate stops every new entry signal before the file is written, so no file reaches the consumer and no order is submitted. The flatten is an order itself; it is a risk-reducing exit, not a new entry, and must never be blocked by a closed gate (OPEN-T2). | Realised + unrealised P&L for the session, in real time, from the NT8 account; the threshold. | SPECIFIED. No numeric threshold exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65). | An account-state feed from NT8 to Redis (unbuilt); EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt; the consumer only knows BUY/SELL, :516–520, and only calls `EnterLong` / `EnterShort`, :660, :662 [E14]; under NT8's managed approach an `EnterShort` while long reverses into a short, `PraxisNoiseAreaBreakout.cs`:224, so an exit sent as SELL would open a position); a threshold value (R8 KEEP; value PROPOSED by a later unit; D2(c) once real money is at stake). |
1
181:R-VN4-2
```

### Command 11

```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '108,111p' docs/reports/2026-11-15-voice-notes-open-questions.md && grep -n -o -E 'stays parked|parked' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md; awk 'NR>=160&&NR<=173' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md | grep -c -i -E 'vn4|gap fade|park'
## 10. Topic 3, the parked items (W2)

- **Voice-brief skill (`Praxis_build-61o`).** Amear: "I don't fucking give a shit, to be honest." No word to resume, so it **stays parked**.
- **Gap fade (`Praxis_build-vn4`).** Told it gets retested with a real stop after Noise-Area under Q6, Amear said: "Okay." No separate ruling.
1:parked
143:parked
143:stays parked
145:stays parked
148:stays parked
148:stays parked
0
```

### Command 12

```
$ A=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/adv/entry-v2-under-test.md; tr -cd '\100' < "$A" | wc -c; grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' "$A"; grep -n -F 'Fills are optimistic' "$A"; tail -n 1 "$A"; grep -n -i -E 'before anything else|before any retest' "$A" | cut -c1-140; stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S%z' "$A"
       0
1
192:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
131:Retest depends on the original source spec. For each of the five, go back to where the strategy was found and check what it specified. I
133:Filer's reading: the retest of each of the five depends on its source spec. Where the source spec has a stop and our test ran without on
163:- (c) What the Noise-Area paper says about a stop, in its exact wording. T1 orders this read before any retest. Per row 14:38:00Z, the m
184:- Noise-Area ruleset (`docs/specs/2026-07-16-b2-noise-area-ruleset.md`, HEAD). Its exit section is marked PAPER-VERIFIED (:57). The base
2026-11-15T10:01:39-0500
```

## Prior findings 1-9: CLOSED or OPEN

1. **CLOSED.** v2 :19: `That reply picks neither option; the filer does not read it as an answer.` and `That tension is named, not resolved (item (l) below).` Item (l) is at v2 :172 (command 06). It names highest return, best fit and "steady first", says "picks none of them", and gives "Answer: NONE."
2. **CLOSED.** v2 :133: `T1's own words are "No loose or interval-checked exits."; what they exclude is D1 below, open (item (f)).` The settling sentence ("Loose and interval-checked exits are excluded.") is gone (command 06).
3. **CLOSED at the cited lines; partly regressed elsewhere.** v2 :44: `Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick.` Item (m) is at v2 :173. v2 :183 adds `If R4's stop-market order covers the daily-loss cap (open (m)), that is a tension with #1, named and not resolved.` But v2 :181 reads R4 as the per-trade stop again (new finding 1).
4. **CLOSED.** v2 :59: `The 1% appears in his answer, "Whatever 1% is right now" (notes :51), to the example (notes :53).`
5. **CLOSED.** v2 :121 has `"I'm I'm looking for steady first."`; v2 :184 has `"Before anything else"`; v2 :94 has `"from peak"`; v2 :183 has `"MFFU’s $1,500 EOD trailing drawdown"` with U+2019. Command 05 finds every one byte-exact in its source (rows 121, 184, 94, 183 marked OK).
6. **CLOSED.** v2 :183 names Phase 3 :64 and :76, breaker #5 (:101) and breaker #7 (:103). v2 :181 quotes the last three sentences of WF spec :36. v2 :179 names DECISIONS :970 (NQ $4.68, MNQ $1.90). All of these were checked at HEAD (commands 08, 09).
7. **CLOSED.** v2 :136 names ruleset :48 (checkpoint grid), :60-:61 and the :61 "as soon as" wording, and says the ruleset "can be read two ways". The same names appear at v2 :184.
8. **CLOSED.** v2 :127: `The channel's statement, not a filer's reading: per notes :106, the filed figures supersede ... That statement is the channel's; it is not re-derived or checked here.`
9. **CLOSED.** v2 :3 says the "Read:" sentence and lead-in on notes :40 are not his but `his quoted words on :40, among them "Okay, then that's what we use.", are his`. It also says `his "Uh, yeah." on :93 ... is his`. v2 :111: `:93's AGENT PROPOSAL sentence is the voice agent's proposal, and its "Uh, yeah." is his`. A new finding of the same class, on notes :33, is low finding 9 below.

Count: 9 CLOSED, 0 OPEN. Finding 3 is closed where it was raised, but the same reading comes back at v2 :181.

## New findings

1. **MED, S8 and requirement 1 (labelling). v2 :181 reads R4 as covering the per-trade stop, the reading that (m) leaves open. It also credits R4 with words that R4 does not contain.**
   Entry :181 (command 06): `R4 and T1 call for a stop-market order at the broker, placed at entry, with no interval-checked exits.` This sentence is set against arm (b)'s per-trade backtest stop (WF spec :36).
   Conflicting text: entry :44 says `Which order his "Okay, then that's what we use." covers (the per-trade stop, the daily-loss cap, or both) is open (item (m) below); the filer does not pick.` Entry :173 has item (m), "Answer: NONE". Notes :40 (command 05 source, notes.md): his words are only "Okay, then that's what we use."; "Read: stop-market order, sitting at the broker, placed at entry." is the channel's. Entry :44 itself labels it so: `The channel reads this as "stop-market order, sitting at the broker, placed at entry" (notes :40).` "No loose or interval-checked exits." exists only in T1 (row 14:37:18Z, command 07). Nothing in notes section 4 says anything about interval-checked exits.
   Why it breaks: setting R4 against a per-trade stop treats R4 as a per-trade-stop ruling. That picks one side of open item (m). By contrast, v2 :183 is written correctly, as a condition: "If R4's stop-market order covers ...". The sentence also lifts the channel's "placed at entry" into R4's content, and gives R4 T1's "no interval-checked exits". Fix: write "T1 calls for ...", and name R4 only conditionally, on (m).

2. **MED, S8. v2 :148 decides that the gap fade stays parked. Whether to pick it up was Amear's question, and his answer is not that clear.**
   Entry :148 (command 06): ``The gap fade (`Praxis_build-vn4`) stays parked. His "Okay." accepts that it is retested with a real stop after Noise-Area under Q6.``
   Conflicting text: brief :44 asks `Two parked items: pick them up, or leave them?`, brief :47 says `Q6 may settle it.`, and brief :48 gives `Options: A. Resume both. B. Resume the skill only. C. Leave both parked.` (command 09). Notes :111 says only `Amear said: "Okay." No separate ruling.` The channel writes "stays parked" for the skill (notes :110) but not for the gap fade (command 11). Row 13:30:00Z (command 07) says "resuming parked `61o`/`vn4` passes as a park-rule human resume".
   Why it breaks: his "Okay." to the gap fade being retested after Noise-Area can be read two ways. One reading is option C, parked until Noise-Area is done. The other is a resume, with the gap fade queued second. The entry picks C as a statement of fact. The Still-open list (v2 :160-:173) carries no gap-fade or park item: command 11's count of `vn4|gap fade|park` in those lines is 0. "No bead is changed" is right, but it is a separate point from whether the gap fade was resumed. Fix: record his "Okay." as said, and add an open item: is `vn4` resumed, queued after Noise-Area, or left parked?

3. **MED, S6 and S2. T1 conflicts with Amear's own earlier typed stop ruling. The entry reports that ruling only as spec text, cites no DECISIONS line for it, and carries no open item on which ruling governs.**
   Entry :181 (command 06): ``Arm (b)'s stop is "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (:36, quoted again at :74). R4 and T1 call for a stop-market order at the broker, placed at entry, with no interval-checked exits.``
   Conflicting text (command 08): HEAD DECISIONS :907 has `Ruling 1 (`2026-11-05T23:50:09Z`, typed): *"Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest."*` HEAD DECISIONS :936 has `**R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops."`. WF spec :74 (command 09) marks the same words `(typed ruling 1). — RULED.` Live-signal topology HEAD :58 (command 10) builds "resting stops on every live position (R-VN4-2 ...)" into breaker #1. T1 (command 07) says `retest it and recheck it with a proper stop-market order, sitting at the broker and placed at entry ... No loose or interval-checked exits.`
   Why it breaks: two typed rulings of Amear's now point opposite ways on how a Noise-Area backtest stop is modelled. The 2026-11-05 ruling says it is checked on bar close and is not resting. The 2026-11-15 ruling says it is a resting broker order with no interval-checked exits. The entry presents the older ruling only as walk-forward spec text. It does not call it Amear's typed ruling, and it cites neither DECISIONS :907 or :936 nor the topology spec. Command 10: the entry has 1 line matching `R-VN4-2|topology|907|936|968|23:50:09Z`, and that line holds only the :36 quotation. Under S2 this reports a RULED item at spec level. Under S6 it misses the DECISIONS touch and the topology touch. Under S8, which ruling governs is Amear's question, and it is missing from the Still-open list. Item (f) covers only T1 against notes section 9. Fix: name DECISIONS :907/:936 and topology :58, and add an open item for T1 against the 2026-11-05 ruling 1 / R-VN4-2.

4. **LOW, requirement 2 and S8. "Before anything else" is narrowed to "before any retest", and the sequencing tension is not named.**
   Entry :163: `T1 orders this read before any retest. Per row 14:38:00Z, the master dispatches that read only after this entry is committed.` Entry :133 also has "Before any retest". T1 (command 07) has `Before anything else, confirm from the original paper` and, separately, `Report what the paper actually says ... before any retest`. The master's sequencing (the read comes after this filing) sits against "Before anything else". The entry neither names that nor quotes his wording in (c). Entry :184 quotes "Before anything else" correctly.

5. **LOW, S8 and S2. v2 :176 says "These rulings answer its Q1-Q6 ... Q6 by R9 and T1", while (b) and (f) leave Q6's reading open.** In the same bullet, "R7" stands both for this entry's R7 (`is kept by R7`) and for D-2026-11-14-B's R7 (`R7 (:2572, ...) is untouched`). A reader cannot tell which one each instance means.

6. **LOW, S2. v2 :183: `R8(d)'s variable keeps trading after two losses at 0.5% risk. That is a direct tension with #3`.** Breaker #3 is `2 consecutive losers in one session → identical to max trades` (Phase 3 :99, command 09). His words (notes :81) are "after two after two losses". They say nothing about one session or about trading on the same day. "Keeps trading" in-session is the filer's reading, and "direct" overstates it.

7. **LOW, S6. Missing cross-block touches.** (a) D-2026-11-13-E overfitting guard, HEAD :2488-:2493 (command 08): `Allow no more than three parameter variants per idea, and log every variant tried` and the fixed tuning window. R1's "test it in multiple ways", R8(d)'s variable to test, and T1's added stop (a new variable, notes :92) all bear on it. The entry names only the skip list, :2470 and bar items 2 and 3. (b) D-2026-11-14-B R1 (:2533, loop held), R4 (:2555, the recheck T1 extends) and R5/R6 (:2562, Mac pre-screen and lighter research standard, which bear on how T1's retest runs). The v2 :176 bullet names only R2, R3, R7 and R8 of that entry. (c) The topology :58 breaker #1 resting-stop text (see new finding 3).

8. **LOW, requirement 7 (authority chain). The entry says the brief is "filed unchanged with this entry" (v2 :3). No ledger row dispatches filing the brief in this unit.** Row 14:38:00Z (command 07) dispatches filing "the notes plus the 14:37:18Z typed ruling". Row 13:30:00Z says `No commit this act; the brief stays in the working tree for the next flush.` The brief is byte-unchanged (command 01 hash matches), so the issue is the authority citation, not the content.

9. **LOW, requirement 1 (labelling, same class as prior finding 9).** The v2 :29 block header says `:33 is the channel's statement`. Notes :33 carries the quoted "Halt all runs until further notice". Row 13:30:00Z (command 07) identifies that as the inbound Telegram message of 2026-11-13 20:21:51. That it was Amear's message is UNVERIFIED here, but the row treats it as his halt. Either way, the quoted words are not the channel's.

10. **LOW, S8. v2 :156: `the MFFU email goes to the Praxis master through the handoff.`** Row 14:37:18Z lists "how the MFFU email reaches the repo" as "Left unanswered by him". Entry (d) at :164 repeats that correctly. His "add those to the handoff" (notes :120) uses "those", which is plural and has no stated referent. Naming the referent as "the MFFU email" is the filer's reading, and it is not labelled as one in that sentence. v2 :156 does open with "Filer's reading:", which softens this to LOW.

## What survived

- All 20 fenced blocks are byte-identical to their stated `sed -n` source, or for T1 to the grep and sed extraction (command 03: 20 IDENTICAL, 0 DIFFERENT).
- Every inline double-quoted string outside fences was found byte-exact in the notes, brief, ledger rows or HEAD files (command 05). The 3 NOTFOUND rows are artefacts of the script dropping backtick spans before it matches. v2 :136 "every `HH:00` / `HH:30`" matches ruleset :48 (command 09). The v2 :190 `WHEN: `date -u` ...` strings match rows 14:38:00Z and 13:30:00Z (command 07).
- Requirement 3, items (a)-(e): all present, each "Answer: NONE", with correct cites. (d) quotes no MFFU wording, keeps F4 FROZEN at rubric :34-:35 (command 09), and says notes :123 does not unfreeze it.
- Requirement 4: the 5% is called a placeholder "while no money is at stake" (v2 :94), and "No breaker value is changed" appears at v2 :94, :183 and :188. More than 20 HEAD citations were checked and all hold (commands 08, 09): DECISIONS :970, :1735-:1740, :2367, :2426, :2431, :2433, :2459, :2468, :2470, :2481, :2482, :2527, :2540, :2546, :2553, :2572, :2580, :2595-:2600, :2615; Phase 3 :11, :54, :64, :76, :82, :97-:103, :138-:140, :145, :208-:212; WF spec :31, :32, :36, :67, :74; WF values :51, :73, :124; ruleset :48, :50, :57, :59, :60, :61, :64; rubric :19, :31, :33-:35, :42; brief :15, :34, :38-:40, :46-:48; recheck :9-:11.
- Requirement 5: 0 at-signs in the entry (command 12). The only names are Amear and the paper's authors. Notes :122 is not quoted.
- Requirement 6 and S13: the sentence appears exactly once, at v2 :192, the last line (command 12).
- S5 and requirement 7: the ledger has 3 rows dated 2026-11-15, none at HEAD, and the file ends on row 14:38:00Z (command 07). The WHEN mismatches the entry reports (14:38:00Z carries 14:37:18Z; 13:30:00Z carries 13:25:51Z) are accurate. The T1 provenance note ("the combined reply for option 4") matches the row. The draft's mtime of 2026-11-15T10:01:39-0500 (15:01:39Z) matches "revised 2026-11-15T15:01:39Z" (command 12). The "Written 14:47:13Z" time was not checked (UNVERIFIED).
- S2 Limits: no run, change or lift is claimed anywhere.

## Result: FAIL

Three MED findings are open (new findings 1, 2 and 3), plus seven LOW. Prior findings 1-9 are all CLOSED. Prior finding 3 partly comes back as new finding 1.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
