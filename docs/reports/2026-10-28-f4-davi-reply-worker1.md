# Worker report — F4: filing the MFFU "Davi" support-reply screenshot as evidence

## Task
1. Copy the Desktop screenshot of the MFFU support reply into the repo as evidence. Prove the copy is byte-identical to the source and that the source is still on the Desktop.
2. Write a verbatim transcription of the screenshot.
3. Write this report.

## Mode
BUILD. Nothing was committed and nothing was staged (`git add` was not run, because the manager stages). Nothing under `.claude/` was touched. No URLs were fetched and no email was read.

## Criterion
From the brief: the copy's sha256 must equal `15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992` and its size must be 254350 bytes. `cmp` must report the copy and source identical. The source must still exist afterwards. The transcript must be verbatim, line for line, with quirks kept. (The brief did not cite a specific SPEC_RUBRIC line.)

## Process log
1. Checked that `docs/reports/evidence/` did not yet exist, so nothing would be overwritten. Found the source using the glob.
2. Ran `mkdir -p docs/reports/evidence`, then `cp -p <glob> docs/reports/evidence/2026-10-28-mffu-davi-reply.png`. This was a copy, not a move.
3. Ran shasum, `ls -l` and `cmp` on both files (output below). Confirmed that the filename byte before `PM` is `e2 80 af` (U+202F) using an xxd dump.
4. Viewed the copy with Read. `sips` reports it as 2866x930.
5. Copied the image to the scratchpad as `scratch.png` and made zoom crops of that copy (commands below). Read each crop.
6. Wrote the transcript. Confirmed with xxd that the em dash in the transcript file is stored as `e2 80 94` (U+2014).
7. Re-checked that the source is still present after all the steps.

## Verification evidence (raw output)

```
--- shasum
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
--- ls -l
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
--- cmp
IDENTICAL
--- source still present
0000000    /   U   s   e   r   s   /   a   d   m   i   n   /   D   e   s
0000020    k   t   o   p   /   S   c   r   e   e   n   s   h   o   t    
0000040    2   0   2   6   -   1   0   -   2   8       a   t       4   .
0000060    5   3   .   2   3      **  **   P   M   .   p   n   g  \n    
0000077
/usr/bin/sips
/Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-10-28-mffu-davi-reply.png
  pixelWidth: 2866
  pixelHeight: 930
```

Hex dump of the source filename (shows the U+202F):
```
00000030: 3533 2e32 33e2 80af 504d 2e70 6e67 0a    53.23...PM.png.
```

Source re-checked after the transcription was written:
```
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
```

Em-dash bytes in the transcript file:
```
00000000: 4672 616e 6b20 e280 9420 7468 616e 6b73  Frank ... thanks
```

Git status of the new paths (untracked, not staged):
```
?? docs/reports/evidence/
```

## Crop commands run
All commands were run in the scratchpad `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/`, on `scratch.png`, which is a copy of the evidence file.
```
sips -c 50 760 --cropOffset 35 125 scratch.png --out preview_a.png
sips -c 50 760 --cropOffset 35 860 scratch.png --out preview_b.png
sips -c 90 800 --cropOffset 125 125 scratch.png --out sender.png
sips -c 50 460 --cropOffset 197 125 scratch.png --out greeting.png
sips -c 50 600 --cropOffset 317 125 scratch.png --out hi.png
sips -c 50 900 --cropOffset 587 1090 scratch.png --out url.png
sips -c 40 330 --cropOffset 40 125 scratch.png --out dash.png && sips -z 160 1320 dash.png --out dash_x4.png
sips -c 40 260 --cropOffset 40 1380 scratch.png --out tail.png && sips -z 160 1040 tail.png --out tail_x4.png
sips -c 40 300 --cropOffset 262 600 scratch.png --out ill.png && sips -z 160 1200 ill.png --out ill_x4.png
sips -c 40 300 --cropOffset 682 125 scratch.png --out sig.png && sips -z 160 1200 sig.png --out sig_x4.png
sips -c 40 200 --cropOffset 40 330 scratch.png --out thats.png && sips -z 160 800 thats.png --out thats_x4.png
sips -c 360 1500 --cropOffset 420 125 scratch.png --out bullets_a.png
sips -c 360 1300 --cropOffset 420 1580 scratch.png --out bullets_b.png
sips -c 140 500 --cropOffset 650 125 scratch.png --out signoff.png
sips -c 40 120 --cropOffset 422 155 scratch.png --out bulletglyph.png && sips -z 160 480 bulletglyph.png --out bulletglyph_x4.png   (made but not Read)
sips -c 40 340 --cropOffset 10 125 scratch.png --out name.png && sips -z 160 1360 name.png --out name_x4.png
sips -c 40 200 --cropOffset 40 760 scratch.png --out im.png && sips -z 160 800 im.png --out im_x4.png
```
Crops that were Read: preview_a, preview_b, sender, greeting, hi, url, dash_x4, thats_x4, tail_x4, ill_x4, sig_x4, bullets_a, bullets_b, signoff, name_x4, im_x4.

What the crops confirmed:
- Greeting: `Hello amear,i hope this mail meets you well.` (no space after the comma).
- `Hi ! Thank you...`, with a space before `!`.
- The preview ends `...1. Does this specific is f`, cut mid-word with no ellipsis.
- Sender address: `<eda.daniel.david@myfundedfutures.intercom-mail.com>`.
- URL text: `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices`.

## Glyphs I was unsure of
- **Preview dash** (`Frank — thanks`): it is clearly a long dash, not a hyphen, so it is transcribed as an em dash (U+2014). A horizontal bar (U+2015) would look the same, so the codepoint is UNVERIFIED.
- **Hyphens** (`Bani-Ahmad`, `Davi-MyFundedFutures`, `simulated-funded`, `High-frequency`, and in the URL): all short, transcribed as ASCII `-`. The codepoint is UNVERIFIED.
- **Apostrophes** (`that's`, `I'm`, `I'll`): drawn as straight ticks, transcribed as ASCII `'`. The codepoint is UNVERIFIED.
- **Bullet marker**: written as `•`. It may be an HTML list marker rather than a literal character.
- Nothing was illegible.

## Files written (NOT staged)
- `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`
- `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md`
- `docs/reports/2026-10-28-f4-davi-reply-worker1.md` (this report)

MANIFEST.md was not updated, because the brief said not to touch any other file. The manager should update it.

## Result: PASS
