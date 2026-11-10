# Review note: Praxis nightly checks, five problems re-checked against the committed plan

**From:** the Praxis build side. **Date:** 2026-10-28. **Target:** hermes-ops
`docs/plans/2026-10-21-praxis-loop-plan.md` and `bin/{heartbeat,praxis-check}.sh`, all committed in
`1d0fdf1`; hermes-ops HEAD is `4209004`. Working-tree copies of these files match HEAD (`git diff HEAD --stat`
lists none of them). It replaces an undelivered draft that reviewed the superseded 2026-10-20 spec request.
All captures are read-only. Every output below was re-run on 2026-10-28 between 17:15 and 17:24 EDT (−04:00);
quoted source lines were re-checked after that.
**STATIC READ** means the file was read and not run. `heartbeat.sh`, `praxis-check.sh` and `notify.sh` were
not run, because they send alerts.

| # | Problem | Status at `4209004` |
|---|---|---|
| 1 | Skipped nights are invisible to the heartbeat | **OPEN** |
| 2 | The checks are not named | **RESOLVED** |
| 3 | Praxis's `b2data-watch` daemon can confound the `find -newer` guard | **CHANGED** (latent; one-off step only) |
| 4 | The ruling citation `2026-10-20T13:20` is ambiguous | **PARTLY RESOLVED** (file named, no time zone) |
| 5 | The `66n` commit rule vs Praxis's carried staged set | **CHANGED, still open** (H3 unmet) |

## 1. Skipped nights — OPEN
STATIC READ, `bin/praxis-check.sh` @ `4209004`. A SKIP writes a line, then exits before any alert:
```
    46	if [ "$brc" -eq 0 ]; then logline all 4 SKIP; exit 4; fi
```
STATIC READ, `bin/heartbeat.sh:50,52` @ `4209004`. A night counts as missed only if it has no line at all:
```
    50	    have="$(awk -v d="$day" 'substr($0,1,10) == d { n++ } END { print n+0 }' "$check_log")"
    52	  [ "$have" -gt 0 ] || missed=$((missed + 1))
```
**Observed.** We ran heartbeat's own awk programs (lines 50 and 40) on the real `logs/PRAXIS_CHECK_LOG.md`.
The script itself was not run:
```
$ L=logs/PRAXIS_CHECK_LOG.md; m=$(sed -n 50p bin/heartbeat.sh | cut -d"'" -f2); c=$(sed -n 40p bin/heartbeat.sh | cut -d"'" -f2)
$ for d in 2026-10-25 2026-10-26 2026-10-27 2026-10-28; do echo "day $d have=$(awk -v d=$d "$m" $L)"; done; echo "checks=$(awk -v c=2026-10-22 "$c" $L)"
day 2026-10-25 have=0
day 2026-10-26 have=2
day 2026-10-27 have=3
day 2026-10-28 have=3
checks=8
```
The log's only 10-26 lines are two SKIPs (log lines 1–2, 07:29:43 and 07:31:43 −04:00, each
`check=all  rc=4  SKIP`). Line 46 writes one SKIP per run, so these are two runs, neither the 03:00 (−04:00)
timer (`docs/reports/2026-10-26-praxis-check.md:33`: "two real SKIP lines (07:29, 07:31)"). So 10-26 is
not counted as missed, and both SKIP lines are included in `checks=8`. The message the heartbeat sends has no skip
field (`bin/heartbeat.sh:62`):
```
exec bash "$here/notify.sh" "hermes-ops heartbeat $today: ticks=$ticks checks=$checks last-fail=$lastfail missed-nights=$missed spend-today=$spend"
```
The heartbeat job (`ai.hermes.heartbeat`) has not run yet. `launchctl print` shows `runs = 0` and
`last exit code = (never exited)`, with a schedule of `Weekday 0, Hour 9`, Sunday 09:00 local EDT/EST.
Your own Task 7 report (`docs/reports/2026-10-26-praxis-check.md:27`) already says a SKIP "does not alert".
That is the design. The gap is that the weekly summary also cannot show a skipped night.

**Options (not chosen):** (a) add a `skipped-nights=<n>` field to the heartbeat (nights whose only lines are
`SKIP`); (b) count a SKIP-only night as missed; (c) alert on SKIP.
**Question for Amear, left open:** should a skipped night alert, be counted in the weekly summary, or stay
silent?

## 2. Checks named — RESOLVED
The plan names all three checks with exact commands (`docs/plans/2026-10-21-praxis-loop-plan.md:335-341`
@ `4209004`):
```
- The three checks, fixed in the script (ruling 2026-10-21T09:45; probe v2 for invocations):
  1. `python3 -I scripts/tests/b2-stitch-selftest.py` — PASS iff rc 0.
  2. `python3 -I scripts/b2data_raw_validate.py --root "$V"` where `$V=$tmp/v` holds
  3. `bash scripts/tests/b2data-watch-selftest.sh` with `TMPDIR=$tmp/watch` exported,
```
(Excerpt: lines 335, 336, 337 and 340.) The real log shows those three names on 10-27 and 10-28, for example
`2026-10-28T03:00:11-0400  praxis=efcf690f3f7c  check=b2data-watch-selftest  rc=0  PASS`.

## 3. Daemon vs the `find -newer` guard — CHANGED
The guard now appears only in the plan's one-off Step 5 (`plan:353`, quoted: `` `find ~/praxis-signals/b2-data -newer "$exp" | wc -l` → `0`. ``).
`bin/praxis-check.sh` has no `find` at all (`grep -n 'newer\|find '` → no output, rc=1). Your Task 7 report,
line 15, records the guard at `0 before and 0 after`.
**STATIC READ** of the Praxis watcher `~/Library/Application Support/Praxis/bin/praxis-b2data-watch.sh`
(mtime Jul 20 11:59:27 2026 EDT). It appends to `b2-data/reports/` on data events:
```
    48	REPORTS="$ROOT/reports"
    51	LOG="$REPORTS/landing-log.txt"
    65	log_line() { printf '%s %s\n' "$(ts)" "$*" >> "$LOG" 2>/dev/null || true; }
   182	while :; do
   183	  sweep || true
```
Observed today (times are local EDT; first line from
`launchctl print gui/$(id -u)/build.praxis.b2data-watch`; then `stat -f "%Sm %z %N"` in `~/.praxis/state/`; the
counts from `cd ~/praxis-signals/b2-data && find . -newermt '2026-10-26 00:00' | wc -l`, then with `'2026-07-01'`):
```
	state = running
Oct 28 17:24:09 2026 934 b2data-seen.txt
Oct 28 17:24:11 2026 1100 b2data-sizes.txt
since 2026-10-26 00:00 local:        0
positive control, since 2026-07-01:       94
Wed 28 Oct 2026 17:24:17 EDT
```
The sweep is live: its state files (in `~/.praxis/state/`, outside `b2-data`) were written 6–8 s before
`date`. Nothing under `b2-data` changed since 10-26 00:00 EDT, and the same `find -newermt` with an older date returns
94, so the counter is not blind. These counts use a date reference, not the guard's `-newer "$exp"` file. The last `landing-log.txt` line is `2026-07-21T18:05:25Z`, which matches
its mtime of `Jul 21 14:05:25` EDT.
The daemon can also write `reports/raw-landing-validation.md` (STATIC READ). Watcher line 136 runs its copy of
the raw validator on the live tree (excerpt: `python3 "$VALIDATOR" --root "$ROOT"`), and `b2data_raw_validate.py:298`
(same directory) reads `report_path = os.path.join(reports, "raw-landing-validation.md")`. It runs once per
new complete `raw/` state (line 133: `[ "$sig" = "$prevsig" ] && return 0`). The last run logged
`2026-07-21T18:05:25Z raw-landing validation complete: …`.
Your three checks run under `sandbox-exec`, and `bin/praxis-check.sb:4-5` reads `(deny file-write*)` /
`(allow file-write* (subpath (param "TMP")))`. **Our inference** (the plan states no purpose for the guard): it is
there to show that the sandboxed run wrote nothing under `b2-data`. The daemon is a writer there that the sandbox
does not cover, so a non-zero count would not, on its own, show a leak.
**Limits:** all write paths above are static reads, and the daemon was not stopped or toggled. We have shown
only that it has the code to cause a guard hit on data events, not that it does.
**Option (not chosen):** in any re-run of that guard, print paths and mtimes (`find … -newer "$exp" -ls`), not
`wc -l`, and read `reports/landing-log.txt` for the window. A daemon validation run appends a
`raw-landing validation complete` line there (STATIC READ, watcher line 137).

## 4. Citation — PARTLY RESOLVED
`plan:29` @ `4209004` names the file:
```
**Spec:** rulings in `ledgers/DECISION_LOG.md` rows `2026-10-20T13:20`, `2026-10-21T09:45` and
```
Praxis has no `ledgers/` path (`git -C Praxis.build ls-files ledgers | wc -l` → `0`), so the file name is no
longer ambiguous. The time still has no zone. Your row (at `4209004`) is 13:20 **−04:00**, which is 17:20Z. In the rows below,
"…" marks text we omitted:
```
160:- [2026-10-20T13:20:00-04:00] WHO: Amear | WHAT: **(1) jdy containment build HELD** — not built now; …
```
Praxis's own `DECISION_LOG.md` has two 13:20 rows, both in **Z**, 4 hours earlier. They are in Praxis's
uncommitted working tree, not in commit `fc77f36`:
```
411:- [2026-10-20T13:20:00Z (approximate)] WHO: praxis-master …
412:- [2026-10-20T13:20:44Z] WHO: praxis-master (new seat) | …
```
The plan contains no zone-suffixed timestamps at all:
```
$ P='T[0-9]{2}:[0-9]{2}(:[0-9]{2})?(Z|[-+][0-9]{2}:?[0-9]{2})'
$ git show 4209004:docs/plans/2026-10-21-praxis-loop-plan.md | grep -c -E "$P"   → 0
$ git show 4209004:ledgers/DECISION_LOG.md | grep -c -E "$P"                    → 114   (control)
```
**Option (not chosen):** write `2026-10-20T13:20-04:00` at `plan:29`.

## 5. `66n` and Praxis's carried staged set — CHANGED, still open
`66n` is a hermes-ops bead (`Hemres_Planner-66n`, `STATE.md:8`). Its rule (`STATE.md:10` @ `4209004`) is
stated for "this repo", i.e. hermes-ops:
```
**`git commit -m "..." -- <paths>` silently commits NOTHING in this repo.**
```
Whether the same behaviour exists in Praxis is **UNOBSERVED**. We did not test it.
What changed in the committed plan:
```
8:> **stage**, never commit. Amear commits.
40:- No script under `bin/` runs `git commit`, `git push`, `merge`, `rebase` or `tag`.
401:  by Amear (H2), delivered to `from-code/`; Praxis clean (H3); Task 8 PASS.
424:- [ ] **Step 5 · Amear:** commit by hand (the Praxis `gate-commit.sh` is a Claude hook and does
427:  cd /Volumes/Sensidine/Hemres.Planner/worktrees/Praxis_build-c2t-<stamp> && git commit
428:  git -C /Volumes/Sensidine/Praxis.build merge --ff-only dispatch/Praxis_build-c2t-<stamp>
457:- `66n`: a pathspec commit lands nothing here. Plain `git commit`, then
```
`plan:40` says no `bin/` script commits, but at `4209004` one does (STATIC READ, not run): `bin/commit-gate.sh:295`
runs `git -C "$top" commit`. It ships `enabled=no` (`config/commit-gate.conf:2`) and is written to refuse Praxis
(`:129`: `# Praxis is refused by toplevel OR common dir: …`). The job's output is audited as a staged diff
(`plan:422`: `` `git -C <wt> diff --cached` ``). The Task 9 Step 5 commit is Amear's, by hand (`plan:424`; `plan:8`: "Amear
commits"). He commits in the worktree (`plan:427`), then fast-forwards the main Praxis checkout (`plan:428`),
where he also lands the dirty tree (`plan:98`). So the risk is in Amear's manual steps, not an automated job.
The conclusion is unchanged: the fast-forward still lands in the main checkout, which is not clean today.
"Praxis clean" is required earlier, before Task 8 (the plan, @ `4209004`):
```
98:**Amear's own steps, outside the tasks:** land the Praxis dirty tree (H3) before Task 8;
370:- Gate before queueing (read-only, recorded): `git -C /Volumes/Sensidine/Praxis.build status
371:  --porcelain | wc -l` → `0` and `rev-list --left-right --count origin/main...HEAD` → `0 0`
```
That requirement comes from your H3 row
(`ledgers/DECISION_LOG.md:172` @ `4209004`, `2026-10-21T12:52:48-04:00`): "land the Praxis dirty tree before
the first loop job" and "Amear lands it in his Praxis session".
Praxis at 17:16 EDT (HEAD `fc77f36`, committed 2026-10-28 16:40:01 −04:00; ahead/behind is against the
local `origin/main` ref, no fetch run). Counts are `git diff --cached --name-only`, `git diff --name-only` and
`git ls-files --others --exclude-standard`, each piped to `wc -l`. Staged = the 9 carried paths + this note and
its working report:
```
staged       11 | unstaged-tracked        9 | untracked       65 | ahead/behind origin: 0	0
```
`git status --porcelain | wc -l` → `80`, so the H3 precondition (porcelain → `0`) is not met. **Not tested:** whether `merge --ff-only` at `plan:428` succeeds in a
Praxis checkout that has staged paths, and what happens to those paths if it does. Our seat's guard blocks
`commit`/`merge` commands, and no Praxis worktree exists to observe.
**Questions for Amear, left open:** (a) Does the `66n` no-pathspec rule apply in Praxis, or only in
hermes-ops? (b) How and when is Praxis's dirty tree landed, as H3 requires, before
Task 8?

Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
