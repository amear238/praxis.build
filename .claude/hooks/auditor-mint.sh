#!/bin/bash
# auditor-mint.sh — SubagentStop hook (matcher ^praxis-auditor$). D-2026-11-04-B item 2.
# Mints a single-use commit token .claude/state/audit-pass-<hash> when a
# praxis-auditor's final message ends with these as its LAST THREE lines:
#     VERDICT: PASS
#     COMMIT-INDEX: REAL | <absolute index path>
#     COMMIT-DIFF-SHA256: <64 hex>
# with no other line anywhere in the message containing VERDICT, COMMIT-INDEX
# or COMMIT-DIFF-SHA256 (case-insensitive), and the named index's cached diff
# (canonical command, see ap_diff_hash) hashes to exactly that value, and the
# transcript provenance checks in audit-provenance.sh hold.
# D-2026-11-04-B addendum 2 (R-VN4-10, 2026-11-05): word filter removed; PASS signal = exact three-line contract
# D-2026-11-04-B addendum 3 (W18 B1/B3, 2026-11-06): last three lines pure printable ASCII; exactly one look-alike-folded verdict line, and it is VERDICT: PASS
# ALWAYS exits 0 — it must never block a subagent stop. Every invocation
# appends one line to $ROOT/.claude/state/mint-log (MINTED or REFUSED).
set -u
# D-2026-11-04-B addendum 3 (W18 B3): fixed locale, so the [[:space:]] strip below
# does not depend on the caller's locale (NBSP minted under UTF-8, refused under C).
export LC_ALL=C

PAYLOAD=$(cat 2>/dev/null || true)
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)
[ -n "$TS" ] || TS="0000-00-00T00:00:00Z"

field() { printf '%s' "$PAYLOAD" | jq -r --arg k "$1" '.[$k] // empty | if type == "string" then . else tostring end' 2>/dev/null; }

ROOT="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$ROOT" ]; then
  CWD=$(field cwd)
  [ -n "$CWD" ] && ROOT=$(git -C "$CWD" rev-parse --show-toplevel 2>/dev/null)
fi
[ -n "$ROOT" ] && [ -d "$ROOT" ] || exit 0
STATE="$ROOT/.claude/state"
mkdir -p "$STATE" 2>/dev/null || exit 0
MLOG="$STATE/mint-log"

refuse() {
  local why
  why=$(printf '%s' "$*" | tr '\n\r\t' '   ')
  printf '%s REFUSED %s\n' "$TS" "$why" >> "$MLOG" 2>/dev/null
  exit 0
}

LIB="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)/audit-provenance.sh"
[ -f "$LIB" ] || refuse "provenance library missing"
# shellcheck source=audit-provenance.sh
. "$LIB" || refuse "provenance library failed to load"

printf '%s' "$PAYLOAD" | jq -e 'type == "object"' >/dev/null 2>&1 || refuse "payload is not a JSON object"

EVENT=$(field hook_event_name)
[ "$EVENT" = "SubagentStop" ] || refuse "hook_event_name=$EVENT not SubagentStop"
ATYPE=$(field agent_type)
[ "$ATYPE" = "praxis-auditor" ] || refuse "agent_type=$ATYPE not praxis-auditor"
AID=$(field agent_id)
[[ "$AID" =~ ^[A-Za-z0-9_-]{1,64}$ ]] || refuse "agent_id malformed"
ATRANS=$(field agent_transcript_path)
PTRANS=$(field transcript_path)
NL=$'\n'
case "$ATRANS$PTRANS" in *"$NL"*) refuse "transcript path contains newline" ;; esac
[ -n "$ATRANS" ] || refuse "agent_transcript_path missing"
[ -n "$PTRANS" ] || refuse "transcript_path missing"

# Final message. A NUL byte would be silently dropped by bash and could splice
# a line together, so it is refused outright.
printf '%s' "$PAYLOAD" | jq -e '(.last_assistant_message | type == "string") and ((.last_assistant_message | explode | any(. == 0)) | not)' >/dev/null 2>&1 \
  || refuse "last_assistant_message missing, not a string, or contains NUL"
# Trailing CR/whitespace stripped per line; trailing empty lines dropped (the
# command substitution removes the trailing newlines the empty lines leave).
MSG=$(printf '%s' "$PAYLOAD" | jq -r '.last_assistant_message' 2>/dev/null \
  | sed -e 's/\r$//' -e 's/[[:space:]]*$//')
[ -n "$MSG" ] || refuse "last_assistant_message empty"

# Attack A7 (W6, 2026-11-04): a FAIL verdict written as `**VERDICT: FAIL**` or
# indented, followed by a quoted column-0 PASS block, used to mint. Rule now:
#  (a) across the WHOLE message, exactly one line contains VERDICT (any case,
#      anywhere in the line), and exactly one each contains COMMIT-INDEX and
#      COMMIT-DIFF-SHA256 (any case, anywhere);
#  (b) the LAST THREE lines are exactly, in order: `VERDICT: PASS`,
#      `COMMIT-INDEX: <REAL|/abs/path>`, `COMMIT-DIFF-SHA256: <64 hex>`.
VCOUNT=$(printf '%s\n' "$MSG" | /usr/bin/grep -ci -- 'VERDICT')
[ "$VCOUNT" = "1" ] || refuse "expected exactly one line containing VERDICT (any case, anywhere), found $VCOUNT"
ICOUNT=$(printf '%s\n' "$MSG" | /usr/bin/grep -ci -- 'COMMIT-INDEX')
[ "$ICOUNT" = "1" ] || refuse "expected exactly one line containing COMMIT-INDEX (any case, anywhere), found $ICOUNT"
HCOUNT=$(printf '%s\n' "$MSG" | /usr/bin/grep -ci -- 'COMMIT-DIFF-SHA256')
[ "$HCOUNT" = "1" ] || refuse "expected exactly one line containing COMMIT-DIFF-SHA256 (any case, anywhere), found $HCOUNT"

NLINES=$(printf '%s\n' "$MSG" | wc -l | tr -d ' ')
[ "${NLINES:-0}" -ge 3 ] 2>/dev/null || refuse "message has fewer than three lines"
VLINE=$(printf '%s\n' "$MSG" | tail -n 3 | sed -n 1p)
ILINE=$(printf '%s\n' "$MSG" | tail -n 3 | sed -n 2p)
HLINE=$(printf '%s\n' "$MSG" | tail -n 3 | sed -n 3p)
[ "$VLINE" = "VERDICT: PASS" ] || refuse "third-from-last line is not exactly VERDICT: PASS"
[[ "$ILINE" =~ ^COMMIT-INDEX:\ (REAL|/[^[:space:]]+)$ ]] || refuse "second-from-last line is not exactly COMMIT-INDEX: <REAL|/abs/path>"
[[ "$HLINE" =~ ^COMMIT-DIFF-SHA256:\ [0-9a-f]{64}$ ]] || refuse "last line is not exactly COMMIT-DIFF-SHA256: <64 lowercase hex>"
CLAIM_INDEX="${ILINE#COMMIT-INDEX: }"
CLAIM_HASH="${HLINE#COMMIT-DIFF-SHA256: }"

# W18 fix (B1/B3, D-2026-11-04-B addendum 3): rule (a) above counts only the
# ASCII word. On the RAW message: (1) after dropping trailing empty/space-only
# lines, the last three lines must be bytes 0x20-0x7E only; (2) every line is
# folded (format chars and U+00AD deleted, NFKC, combining marks deleted, any
# non-ASCII letter = stand-in for any letter, 1/l/| = stand-in for I) and the
# only line containing V-E-R-D-I-C-T anywhere must be the raw third-from-last
# line `VERDICT: PASS`. Python failure of any kind refuses (fail closed).
_LA=$(printf '%s' "$PAYLOAD" | python3 -I -c '
import sys, json, re, unicodedata
msg = json.loads(sys.stdin.buffer.read().decode("utf-8"))["last_assistant_message"]
if not isinstance(msg, str):
    print("message not a string"); sys.exit(1)
lines = msg.split("\n")
while lines and lines[-1].strip(" ") == "":
    lines.pop()
if len(lines) < 3:
    print("fewer than three lines"); sys.exit(1)
for k in (-3, -2, -1):
    if not re.fullmatch(r"[\x20-\x7e]*", lines[k]):
        print("last three lines not pure printable ASCII (line %d from end)" % -k); sys.exit(1)
DROP = set(range(0x200B, 0x2010)) | set(range(0x2060, 0x2065)) | {0xFEFF, 0x00AD}
def fold(s):
    s = "".join(c for c in s if ord(c) not in DROP and unicodedata.category(c) != "Cf")
    s = unicodedata.normalize("NFKC", s)
    s = "".join(c for c in s if unicodedata.category(c) not in ("Mn", "Me"))
    return "".join(c if ord(c) < 128 or not unicodedata.category(c).startswith("L") else "\x01" for c in s)
PAT = re.compile("".join("[%s%s\x01]" % (x, x.lower()) if x != "I" else "[Ii1l|\x01]" for x in "VERDICT"), re.IGNORECASE)
hits = [i for i, l in enumerate(lines) if PAT.search(fold(l))]
want = len(lines) - 3
if hits != [want] or lines[want] != "VERDICT: PASS":
    print("expected exactly one folded verdict line, the third-from-last VERDICT: PASS; found %d at %s" % (len(hits), hits[:5])); sys.exit(1)
print("OK")
' 2>&1)
_LARC=$?
{ [ "$_LARC" = 0 ] && [ "$_LA" = "OK" ]; } || refuse "lookalike: $(printf '%s' "${_LA:-python3 failed rc=$_LARC}" | tail -n 1)"

# W15 Fix (attack D1, 2026-11-04): core.worktree pointed above ROOT moves the
# work tree; refuse unless git's toplevel at ROOT is ROOT itself.
_TOP=$(env -u GIT_INDEX_FILE git -C "$ROOT" rev-parse --show-toplevel 2>/dev/null)
_TOP_RP=$( [ -n "$_TOP" ] && _ap_realpath "$_TOP" 2>/dev/null )
_ROOT_RP=$(_ap_realpath "$ROOT" 2>/dev/null)
{ [ -n "$_TOP_RP" ] && [ -n "$_ROOT_RP" ] && [ "$_TOP_RP" = "$_ROOT_RP" ]; } \
  || refuse "toplevel mismatch: git toplevel '${_TOP_RP:-${_TOP:-unresolvable}}' != ROOT '${_ROOT_RP:-$ROOT}'"
INDEX=$(ap_index_norm "$ROOT" "$CLAIM_INDEX") || refuse "COMMIT-INDEX not REAL and not an existing absolute index file"
REAL_HASH=$(ap_diff_hash "$ROOT" "$INDEX") || refuse "cached diff empty or git failed under index=$INDEX"
[ "$REAL_HASH" = "$CLAIM_HASH" ] || refuse "claimed hash $CLAIM_HASH != actual $REAL_HASH index=$INDEX"
# `mint`: skip ap_verify check 6 (transcript may not be flushed yet at
# SubagentStop); the gate re-runs ap_verify with check 6 at commit time.
VERR=$(ap_verify "$AID" "$ATRANS" "$PTRANS" "$CLAIM_HASH" mint 2>&1 >/dev/null) || refuse "provenance: ${VERR:-ap_verify failed}"
TREE=$(ap_tree "$ROOT" "$INDEX") || refuse "git write-tree failed under index=$INDEX"

AT_RP=$(_ap_realpath "$ATRANS") || AT_RP="$ATRANS"
PT_RP=$(_ap_realpath "$PTRANS") || PT_RP="$PTRANS"
TOKEN="$STATE/audit-pass-$CLAIM_HASH"
TMP="$TOKEN.tmp.$$"
{
  printf 'tree=%s\n' "$TREE"
  printf 'index=%s\n' "$INDEX"
  printf 'minter=praxis-auditor\n'
  printf 'agent_id=%s\n' "$AID"
  printf 'agent_transcript=%s\n' "$AT_RP"
  printf 'parent_transcript=%s\n' "$PT_RP"
} > "$TMP" 2>/dev/null && mv -f "$TMP" "$TOKEN" 2>/dev/null || { rm -f "$TMP" 2>/dev/null; refuse "could not write token"; }
printf '%s praxis-auditor:%s %s PASS index=%s\n' "$TS" "$AID" "$CLAIM_HASH" "$INDEX" >> "$ROOT/AUDIT_LOG.md" 2>/dev/null \
  || { rm -f "$TOKEN" 2>/dev/null; refuse "could not append AUDIT_LOG row"; }
printf '%s MINTED %s %s\n' "$TS" "$CLAIM_HASH" "$AID" >> "$MLOG" 2>/dev/null
exit 0
