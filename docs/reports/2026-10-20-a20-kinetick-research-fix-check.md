# a20 Kinetick research — narrow fix check on N1–N6 (W6)

## Task
Check that the N1–N6 fixes (from `docs/reports/2026-10-20-a20-kinetick-research-final-check.md`) are actually in the body of `docs/reports/2026-10-20-a20-kinetick-research.md`, and that the fixes did not add new defects.

## Mode
ADVERSARIAL (narrow).

## Criterion
S1/S2 (`specs/SPEC_RUBRIC.md:107-108`), S8 (`:114`).

## Process log
1. Created this file as PENDING.
2. Read the artifact (485 lines) and the final-check file (125 lines) in full.
3. Re-ran E1 (both greps plus comm), every new Redemtion citation, `INSTRUCTIONS.md:93-95` and its mtime, E12 plus a broader false-null search, E5, E6, and the E7 extra-term arm. Checked the gitignore status of the files E1 missed, and the mtime (only) of a new `.claude/` file. I did not read Config.xml lines 1-14, and I did not read the content of any agent-memory file.
4. All greps used `/usr/bin/grep`, except the wrapper arm of E1.

## Per-finding check (N1–N6)

| N | Fix in body? (current line) | Adequate? |
|---|---|---|
| N1 | :193-214 corrected E1 (`/usr/bin/grep` 34, wrapper 30, comm lists the 4 missed files). :50 Q1 Redemtion bullet and :70 Q2 row, both REPORTED. :110 plus E12 cover the monitor. :66 "29 files … 25 … plus 4 gitignored" | **Yes.** Redemtion :56, :206, :101, :511, :564 and Round 3 :109 all match verbatim (below). Both representative files are gitignored (`.gitignore:7`, `:26`). Arithmetic: 25+4=29, and 29+5=34. Leftovers: F2 and F6 |
| N2 | :15 "No search found anything in PRAXIS that needs it connected … Concluding 'no mention = no need' is INFERRED. One exception: a stale planning step…" | **Yes.** Matches the proposed fix |
| N3 | :14 "(value VERIFIED…; that this means … is INFERRED…)"; "No old connection log mentions it. NT8's licence trace lists it…"; "master's migration plan carried it over as 'configured'" | **Yes** on (a), (b) and (c). The rewrite brought in F1 |
| N4 | :125/:126 "Likely conflicts … (INFERRED)… If Amear reads D-071 as covering it"; :455 "*if* … That reading is INFERRED … Amear's to say"; :462 "does your D-071 condition … cover connecting Kinetick…? If it does, does it stand, or do you amend it?" | **Yes.** The third answer ("doesn't reach this") is now open to him |
| N5 | E5 commands at :311/:320/:327 (filter disclosed). E6 command and line at :343-346. E7 extra-term null and positive arm at :362-367 | **Yes.** All three re-runs match byte-for-byte (below) |
| N6 | :77 Q2 07-24 row; :93 C3 "first appears in the 07-24 VM-agent instructions (`…INSTRUCTIONS.md:94`)" | **Mostly.** mtime 2026-07-24_09:54:17 matches. C2 still omits it (F7). The citation spans :94-95 (F3) |

## New defects introduced by the fixes (all MINOR)

**F1. Summary :14 is stronger than body 1.4.** MINOR (S2).
- Claim: "NT8's licence trace lists it as a free provider (both VERIFIED)."
- Evidence: the trace line has `subscription=Free` as a field of the licence-check line, and Kinetick is one name inside `licensedProviders='…'`:
  ```
  23:subscription=Free licensedProviders='Playback Simulator NinjaTrader NinjaTrader Continuum … Barchart.com K
  eractive Brokers Barchart.com Kinetick FXCM Coinbase cTrader Schwab Rithmic for NinjaTrader Broker
  ```
  Body :41 words it correctly: "lists `Kinetick` among licensed providers, `subscription=Free`". The free tier itself is VERIFIED elsewhere (`<Free>true</Free>`, Config :47), but not by the trace.
- Fix: change it to "lists it among its licensed providers".

**F2. The header at :5 is contradicted by the new :50.** MINOR (S2).
- Claim: :5 says "every product fact about Kinetick is general knowledge, labelled UNVERIFIED". :50 now gives product facts labelled REPORTED: "DTN-rebadged", "180 days tick, multi-year minute", "~$65/mo".
- Fix: "every product fact is general knowledge (UNVERIFIED) or record/pre-PRAXIS research (REPORTED); none vendor-checked".

**F3. `INSTRUCTIONS.md:94` cites one line; the quote runs over two.** MINOR (citation).
- Evidence:
  ```
  94: **Definitive check** — open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick
  95: data) and the imported **`NQCONT`**, and confirm the RTH open lines up bar-for-bar. In our
  ```
- Fix: cite `:94-95` at :77 and :93.

**F4. E12's pasted output no longer reproduces, and there is no observer-effect note.** MINOR (S1).
- E1 has such a note; E12 does not.
- Evidence: a re-run of the exact E12 command now returns the two pasted hits plus seven hits in the artifact itself:
  ```
  ./docs/reports/2026-10-20-a20-kinetick-research.md:50: …
  …:110: …   …:209: …   …:346: …   …:420: …   …:421: …   …:427: …
  ./DECISIONS.md:208: …   (match "NinjaTrader Continuum feed", beyond the 260-char cut, as the artifact says)
  ```
- The conclusion still holds. A broader search found nothing outside `Redemtion/` and the unit files: `quote freshness|last-tick-age|tick age|stale (data|quote|feed)|data feed (health|loss|stale)` → no output. Within `docs/specs`, `stale|freshness|tick.age|last tick|data feed|heartbeat` → no output, while the `circuit breaker` positive arm fires.
- Fix: add "(observer effect: this report now also matches)" or `--exclude='*kinetick-research*'`.

**F5. :477 "No … `.claude/` file was written" is now stale.** MINOR (S2).
- Evidence:
  ```
  -rw-r--r--@ 1 admin staff 1484 2026-10-20_12:32:09 .claude/agent-memory/praxis-manager/project_grep_wrapper_skips_ignored.md
  -rw-r--r--@ 1 admin staff 4902 2026-10-20_12:32:11 .claude/agent-memory/praxis-manager/MEMORY.md
  artifact mtime 2026-10-20_12:31:45
  ```
  The new file mentions kinetick: E1 now gives `36` (`/usr/bin/grep`) and `31` (wrapper), and comm lists it. 36 = 34 + this file + the memory file. 31 = 30 + this file. I read mtimes only, not content.
- Fix: list the memory write under "Files created", or state that it is outside the unit.

**F6. The Q2 row date at :70 is wrong for one of its files.** MINOR (label).
- The row says "2026-05-05", but it also cites the Round 3 file, whose mtime is `2026-05-06_12:15:05`.
- Fix: "2026-05-05/06".

**F7. The N6 fix is partial: C2 at :92 still lacks the 07-24 origin.** MINOR.
- N6's smallest fix asked for the citation "under C2/C3". Only C3 at :93 got it. Q2 at :77 does call it the earliest source of the label.
- Fix: add `INSTRUCTIONS.md:94-95` to C2's list.

**F8. :50 puts an inference under REPORTED.** MINOR (label).
- Claim: "which was not carried into any current spec (Q3) … These are REPORTED". Q3 at :110 labels "not adopted" INFERRED.
- Fix: add "(INFERRED, E12)" after "current spec".

## Survived
1. **E1 corrected block reproduces**, allowing for the two files written after it (F5):
   ```
   36 / 31; comm: audit_evidence_standards.md, project_grep_wrapper_skips_ignored.md, 3 × Redemtion
   ```
   Gitignore check: `.gitignore:26:.claude/agent-memory/` and `.gitignore:7:Redemtion/`, both untracked. Same count on `.claude` with either grep (2/2), so the wrapper's miss is down to ignore rules, not hidden directories. The mechanism stated at :193 holds.
2. **Every new Redemtion citation holds verbatim:**
   - `ROUND_2…:56` "Kinetick (NinjaTrader's own data service) — cost, quality, history depth"; `:206`
   - `2nd round…:101` "| **Kinetick** (NinjaTrader's own DTN-rebadged service) | Native NT adapter; 180 days tick, multi-year minute | Standalone (no broker required) |"
   - `:511` "| Kinetick/Continuum data feed quote freshness | TCP probe of NT data port + last-tick-age check | 60 sec | Critical |"
   - `:564` "… pass-through, not Kinetick |"
   - `Round 3…:109`
   - The 2nd-round file mtime is `2026-05-05_17:28:01`, matching :50's "file dated 2026-05-05". Labelling it the **paid** tier is supported by "$65/mo".
3. **E5 re-run matches exactly:** 8 × `:0`; the 6 auto-connect/Connected lines; `26`.
4. **E6 re-run matches exactly:** `0/1/0/0/0/0/0/1/1`; line 23 truncated at the same character.
5. **E7 extra-term re-run matches exactly:** `44`; `exit=1`; positive arm `PraxisNoiseAreaBreakout.cs`, `PraxisSignalConsumer.cs`, `exit=0`.
6. **E12 conclusion** ("no spec carries quote freshness / last-tick-age") survives a broader false-null search (F4 evidence).
7. **Summary lines 1, 3, 4, 5 and 6 are not stronger than the body.** :15 matches Q3 :99/:105. :17 labels the D-071 reading INFERRED. :18 keeps the PRAXIS view separate.
8. **S8 holds.** Open Q1 ends "Your call". Q2 is now gated "Only if you want it connected" and offers cover / stand / amend. The PRAXIS view at :136 is "reasoning only — not a decision … **Amear decides.**" Nothing is chosen for him.
9. **Earlier-closed findings (A-F1..F8, B-F1..F5) were not broken by the fixes.** :108, :125 and :126 still carry the corrected labels.

## Verification evidence
All of it is pasted inline above, from this session's runs of `/usr/bin/grep`, `sed -n`, `ls -l -D`, `git check-ignore` and `comm`.

## Files staged
None. This is one new untracked file. No `git add`, and no edits to existing files.

## Result
N1–N6 are all in the body and adequate (N6 is partial, see F7). The fixes introduced 8 MINOR defects (F1–F8) and no BLOCKER or MAJOR.

VERDICT: SURVIVES
