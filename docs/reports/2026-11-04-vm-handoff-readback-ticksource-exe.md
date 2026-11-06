# VM handoff — 2026-11-04 — per-contract readback, tick-source research, .exe upload

**From:** Code (Mac). **To:** the VM agent, with Amear at the screen.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Limits that apply to every task below (R-VN3-2, Amear)

No purchases. No NT8 imports. No runs (no Strategy Analyzer, no backtest, no optimisation) without Amear's approval. No changes to NT8 settings or to files under the NT8 `db` folder. If a step needs any of these, stop and ask Amear on screen. Don't work around it.

Grade every claim: OBSERVED (you saw the output this session), REPORTED BY AMEAR, INFERRED, or UNVERIFIED.

## Task 1 — Read-only readback of the per-contract NQ minute folders

Amear approved this on 2026-11-03 ("yes"). **Why:** to check whether the 1-minute file is NT's back-adjusted series, before any data is bought.

Your 11-02 notes say `db\minute` contains per-contract folders **NQ 03-20 through NQ 12-26**, plus `NQ`, `NQCONT`, `NQCONT ##-##`, `NQCONTROW ##-##` and `NQCONTROW 09-25`. Only the folder names were read.

Do:
1. For each per-contract NQ folder, and for `NQCONTROW 09-25`, list every file with its name, size in bytes and last-modified time. Use `Get-ChildItem` or `dir`.
2. Record a SHA-256 for every file in those folders (`Get-FileHash`). This is the baseline from the High-res plan §3 step 1. It is also safe to do now.
3. Note the file type (extension) you see. Our guess is NT binary `.ncd` files: INFERRED, UNVERIFIED.
4. Report which contract folders cover which months. Base this on file names or dates if they show it. Otherwise say "not visible from a listing".

Don't:
- Open, export or convert the files through NinjaTrader (Historical Data → Export, or anything similar). Export writes new files and changes what NT does. If you can't answer the back-adjustment question without reading the contents, **stop and ask Amear**, and say exactly which NT action would be needed.
- Copy, move, rename or touch anything inside `db`.

Return: the listing plus hashes as a text file in the Drive `praxis-tickprep` folder (name: `2026-11-04-vm-minute-readback.txt`). Then send a short summary saying what the listing does and doesn't show about the 1-minute file's source.

## Task 2 — Research a cheaper or free NQ tick source (research only)

Amear's rulings:
- 2026-11-03: Portara at $695: "no, not paying that."
- 2026-11-03: look for a cheaper or free source: "yes".
- 2026-11-04 (R-1104-3): "if the high fill resolution costs $700 for the data, I'm not going to pay that right now until there's proof of concept."

Scope, set by Code under R-VN3-2: **research and report only**. No purchase. No sign-up that costs money. No download into NT8. No import. No run. Any price or licence is a question back to Amear.

Find and compare up to five sources of historical NQ **tick** (trade) data covering 2021-03 to 2026-07. Include free options and options that come with an existing account, such as a Rithmic or NT data-feed tick history. For each one, give:
- name, plus a link to the page you read
- price as stated on that page, with the date you read it
- date range and per-contract vs continuous
- format, and whether NT8 can import it as Last ticks (say what the page states; mark it UNVERIFIED unless the page says it outright)
- licence limits, if shown
- grade for each fact (what the page states is REPORTED BY <vendor>)

Return: `2026-11-04-vm-tick-sources.md` in the Drive folder. Don't recommend a purchase. Just put the options side by side.

## Task 3 — Upload the two .exe files via Drive

Amear, 2026-11-03: "commit to repo" (binaries too).

Upload `TickPrep.exe` and `MakeSynth.exe` **unchanged** to the Drive `praxis-tickprep` folder, plus a fresh `SHA256SUMS-exe.txt` (`Get-FileHash -Algorithm SHA256`). The Mac will match them against your 11-02 values:

| File | Bytes | SHA-256 |
|---|---|---|
| TickPrep.exe | 22,016 | `72f237468758f8c053a93a9d8ed4ad3805a5b8353afa0eb640d6a1ef9f2cce88` |
| MakeSynth.exe | 7,168 | `3d81495ffe060ffffd71ca4f5993e9f8c312df8d76a1d34818d6c9062a7763a0` |

If a hash on the VM no longer matches these, don't rebuild. Report the mismatch.

## With Amear at the screen (his list, carried forward)

These are Amear's screen tasks. The VM agent can guide them but doesn't run them:
- **C6.** Save the Strategy Analyzer settings as the default.
- **C7.** NQCONTROW readback.
- **Log tab.** Read out the "ignored" messages so Code can file them.

## Not in this handoff

No High-resolution run. When the High measurement runs happen is deferred by Amear ("when the time comes ask agaian"). No tick data is held, and none will be bought before proof of concept.

## Clarifications (appended after audit, 2026-11-04)

- Task 2 "yes": Amear answered "yes" to an either/or question. Reading it as "look for a source" is Code's reading, not his words.
- Runs: approval on screen does not cover a High-resolution run. Code must re-ask Amear before any High run is planned.
- C6 is a settings change. Only Amear makes it, with his own hands. It is the one exception to "no changes to NT8 settings", and only for him.
