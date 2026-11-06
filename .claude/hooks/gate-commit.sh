#!/bin/bash
# PreToolUse gate (matcher: Bash). Denies `git commit` in an ARMED repo unless a
# fresh single-use audit token exists for the CURRENT staged diff AND a matching
# AUDIT_LOG PASS row proves the orchestrator-auditor minted it. Armed only while
# .claude/state/orchestrator-active exists — normal sessions are unaffected.
#
# Hardened 2026-07-10 (bead v6y) after a parallel session polluted the shared
# .git/index between token-mint and commit:
#   1. staged-TREE binding — token carries `tree=<git write-tree>` from mint time;
#      commit is denied unless the index still produces that exact tree.
#   2. single-session rule — commit is denied while any OTHER live claude
#      process (outside this session's own process tree) has its cwd inside
#      this repo. Check errors fail CLOSED.
#   3. orphaned-token sweep — tokens >30 min old are deleted even if their hash
#      never matches again (previously they lingered forever).
#
# The commit match anchors on a real `git ... commit` invocation in COMMAND
# POSITION (bead 587, 2026-07-12; the previous bare `*git*commit*` glob also
# fired on quoted free text that merely MENTIONED the words — two live false
# denials in session 6). Within that anchor it stays broad: `git -C <dir>
# commit`, `git --work-tree=... commit`, chained (`cd x && git commit`), piped,
# subshell, VAR=... prefixes, common wrappers, and nested `sh -c`/eval strings
# are all still gated. Over-match inside a gated segment remains intentional
# and fail-closed — a non-commit command that trips it just gets re-issued
# clean; a `cd otherrepo && git commit` burns THIS armed repo's token
# (fail-safe for the armed repo, not a bypass).
#
# D-2026-11-04-B (R-1104-1, 2026-11-04): two additions, every check above kept.
#   a. temp-index commit — the WHOLE command may be `GIT_INDEX_FILE=<abs path>
#      git commit ...` (path unquoted, existing regular file, no shell
#      metacharacters outside quotes); any other appearance of INDEX_FILE, or
#      GIT_INDEX_FILE set in this hook's own env, denies. Hash + write-tree run
#      under THAT index; the token's index= line (absent = REAL) must match.
#   b. praxis-auditor tokens (minter=praxis-auditor, written by auditor-mint.sh)
#      are re-verified via audit-provenance.sh ap_verify, and their
#      parent_transcript must equal this payload's transcript_path. A main-thread
#      praxis-master caller is accepted ONLY with such a token; a legacy
#      audit-approve.sh token is refused for it (not deleted). Legacy route is
#      unchanged for every other caller.
#
# W8 fixes (2026-11-04, adversarial attacks A2/A8/A10/A14/A1/A3):
#   A. HASH is sha256 of `git diff --cached --no-ext-diff --no-textconv
#      --no-color --text --ignore-submodules=none --no-relative` (W13; was
#      --binary; W15 added --no-relative, attack D1) under
#      the selected index — the canonical command the
#      minter and auditor use; a repo-local diff.external/textconv cannot hide
#      the real diff from the hash (A10).
#   B. both whole-command parsers strip ONLY ASCII space/tab, and outside quotes
#      accept ONLY [A-Za-z0-9 \t._/+=,:@%-] plus ' and ". Any other byte (VT, FF,
#      CR, NBSP, any non-ASCII) outside quotes denies — Python strip() used to
#      drop a trailing NBSP/VT that the shell then passed as a pathspec (A14).
#   C. stack master: payload .cwd must be present and realpath(.cwd) ==
#      realpath(ROOT), else deny before token lookup — the gate hashes ROOT, so
#      a commit run from another worktree commits a different index (A2).
#   D. praxis-auditor tokens: after ap_verify, the parent transcript must hold
#      the HARNESS-WRITTEN result of the auditor's Agent call: a user record with
#      a tool_result for the meta.json toolUseId whose text has a column-0
#      `agentId: <agent_id>` line (binds the id to that spawn), AND a line that
#      trims to `COMMIT-DIFF-SHA256: <HASH>` either in that tool_result
#      (synchronous Agent call) or inside the column-0 `<agent-message
#      from="<agent_id>">` ... `</agent-message>` frame of a user hand-back record
#      (background Agent call — observed shape in this repo's session
#      transcripts, where the tool_result is only the "Async agent launched"
#      stub) or (W-TN 2026-11-06, ruling 3b) inside the `<result>` span of the
#      FIRST block of a user record with origin.kind=="task-notification" whose
#      content BEGINS with `<task-notification>`, whose first `<task-id>` is
#      <agent_id> and whose status is completed (async hand-back; captured
#      2026-11-06 from this repo's main transcript, agents a9d35d34f3b18e943 and
#      a66e2698ac35ce15f). Its first `<status>` and first `<summary>` lines
#      decide, and the summary must be exactly `<summary>Agent "<description>"
#      finished</summary>` with the description read from the harness-written
#      tool_use <toolUseId> and free of newline/CR/</>/"/&. Defeats a forged meta.json reusing a genuine earlier
#      toolUseId (A8) unless the forger also edits the live parent transcript.
#   E. at ALLOW the gate writes .claude/state/last-allowed (tree, index, hash,
#      head_before, ts, cmd_sha256); scripts/commit-tree-verify.sh (PostToolUse)
#      compares the landed HEAD^{tree} with it. Detection only (A1/A3: a git
#      pre-commit hook or background job can still change the index after allow).
set -uo pipefail
INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)
case "$CMD" in
  *git*commit*) ;;   # cheap pre-filter only; precise command-position check below
  *) exit 0 ;;
esac
# --- Precise form matcher (bead 587). Gate only when `git ... commit` is a real
# invocation in COMMAND POSITION: start of string/line, or right after a command
# separator (; & | pipe, subshell "(", backtick — "$(" is covered by "("),
# optionally behind VAR=... assignments and/or one common wrapper (env, sudo,
# xargs, ...), with the binary itself allowed in path (/usr/bin/git) or
# backslash-escaped (\git) form. Quoted regions are stripped FIRST so free text
# can never anchor a match; an unbalanced leftover quote merely over-matches
# (fail closed). A nested `sh -c '...'`/eval in command position keeps the old
# broad gating — nested command strings are not introspected, they deny by
# default. This narrows only WHERE the pattern may match, never WHAT is gated:
# every downstream form, single-session, and token/tree check is unchanged.
SCRUB=$(printf '%s' "$CMD" | sed -e "s/'[^']*'//g" -e 's/"[^"]*"//g')
ANCHOR='(^|[;&|(`])[[:space:]]*'
PRE='([A-Za-z_][A-Za-z_0-9]*=[^[:space:]]*[[:space:]]+)*((command|builtin|exec|env|sudo|nohup|nice|time|xargs)([[:space:]]+[^;&|`]*)?[[:space:]]+)?'
# BINPRE: the binary name may be invoked backslash-escaped (\git) or via any
# path ending in "/" (/usr/bin/git, ../bin/git) — same tip-write, still gated.
BINPRE='(\\|[^[:space:];&|`]*/)?'
GITCOMMIT="${BINPRE}"'git[[:space:]]+([^;&|`]*[[:space:]])?commit([[:space:];&|)`]|$)'
NESTSHELL="${BINPRE}"'(sh|bash|zsh|dash|ksh|eval)([[:space:]]|$)'
if ! printf '%s' "$SCRUB" | grep -Eq "${ANCHOR}${PRE}${GITCOMMIT}" \
   && ! printf '%s' "$SCRUB" | grep -Eq "${ANCHOR}${PRE}${NESTSHELL}"; then
  exit 0
fi
ROOT="${CLAUDE_PROJECT_DIR:-.}"
STATE="$ROOT/.claude/state"
[ -f "$STATE/orchestrator-active" ] || exit 0

# --- Form checks: run BEFORE token lookup so a form denial never consumes the
# token. Fail-closed; the model just re-issues a clean commit. ---
deny_form() {
  echo "Commit denied: $1" >&2
  echo "Commit exactly the staged diff with a plain \`git commit -m \"...\"\` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call." >&2
  exit 2
}
# short-flag cluster containing 'a' ( -a, -am, -sam, ... ) sweeps the working tree
if printf '%s' "$CMD" | grep -Eq '(^|[[:space:]])-[A-Za-z]*a[A-Za-z]*([[:space:]]|$)'; then
  deny_form "a '-a'-style short flag sweeps unstaged working-tree changes into the commit"
fi
if printf '%s' "$CMD" | grep -Eq '(^|[[:space:]])--(all|include|amend)([[:space:]]|=|$)'; then
  deny_form "--all/--include/--amend changes the committed set out from under the audit"
fi
if printf '%s' "$CMD" | grep -Eq '[[:space:]]--[[:space:]]'; then
  deny_form "a pathspec after ' -- ' commits a different set than what was audited"
fi
# one git commit per Bash call — no staging in the same call, no double commit
if printf '%s' "$CMD" | grep -Eq 'git[[:space:]]+add'; then
  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
  exit 2
fi
if [ "$(printf '%s' "$CMD" | grep -oE 'git[[:space:]]+commit' | wc -l | tr -d ' ')" -gt 1 ]; then
  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
  exit 2
fi

# caller identity from the payload (D-2026-11-04-B item 4)
pj() { printf '%s' "$INPUT" | python3 -c 'import json,sys
v=json.load(sys.stdin).get(sys.argv[1],"")
print(v if isinstance(v,str) else "")' "$1" 2>/dev/null || true; }
CALLER_TYPE=$(pj agent_type)
CALLER_ID=$(pj agent_id)
STACK_MASTER=0
[ "$CALLER_TYPE" = "praxis-master" ] && [ -z "$CALLER_ID" ] && STACK_MASTER=1

# --- Stack-master exact form (W4 fix, 2026-11-04). `git commit -m x somefile`
# (a pathspec WITHOUT ' -- ') commits somefile's WORKING-TREE content, not the
# audited index, and none of the checks above catch it. For the stack master
# only (both the REAL and the temp-index route) the WHOLE trimmed command must be
#     [GIT_INDEX_FILE=<abs path> ]git commit -m <msg> [-m <msg> ...]
# where the args, tokenised with python3 shlex.split(posix=True), are a
# non-empty run of `-m <message>` pairs and nothing else (no other flag, no
# positional, no joined `-mfoo`). Refused anywhere: `$(` and backtick. Refused
# outside quotes: ; & | < > ( ) backslash newline, and the expansion characters
# $ * ? [ ] { } ~ # ^ (glob/brace/variable expansion could turn one shlex token
# into several shell words, i.e. a pathspec). `$` is refused inside double
# quotes too ("$@" / "${a[@]}" expand to several words) — put a literal $ in
# single quotes. Runs BEFORE token lookup so a form denial never consumes the
# token. Non-stack callers are NOT narrowed by this block.
if [ "$STACK_MASTER" = 1 ]; then
  _sm=$(printf '%s' "$CMD" | python3 -c '
import re, shlex, sys
# Fix B: strip ONLY ASCII space/tab (str.strip() also drops VT/FF/NBSP/...,
# which the shell keeps as a word, i.e. a pathspec).
s = sys.stdin.read().strip(" \t")
# outside quotes: ONLY these characters (plus the two quote characters)
SAFE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \t._/+=,:@%-")
def bad(r):
    print("ERR " + r); sys.exit(0)
if "$(" in s: bad("$( appears in the command")
if "`" in s: bad("a backtick appears in the command")
m = re.match(r"(?:GIT_INDEX_FILE=/[A-Za-z0-9._/+-]+[ \t]+)?git[ \t]+commit(?:[ \t]+(.*))?\Z", s, re.S)
if not m:
    bad("the command is not [GIT_INDEX_FILE=<abs path> ]git commit ... as the whole command (no cd/&&/;/git -C/other prefix)")
rest = m.group(1) or ""
st = None; i = 0; n = len(s)
while i < n:
    c = s[i]
    if st is None:
        if c == "\x27": st = "s"
        elif c == "\"": st = "d"
        elif c not in SAFE: bad("character %r (U+%04X) outside quotes is not in [A-Za-z0-9 \\t._/+=,:@%%-]" % (c, ord(c)))
    elif st == "s":
        if c == "\x27": st = None
    else:
        if c == "\"": st = None
        elif c == "\\": i += 1
        elif c == "$": bad("$ inside double quotes (use single quotes for a literal $)")
    i += 1
if st is not None:
    bad("unterminated quote")
try:
    a = shlex.split(rest, posix=True)
except ValueError as e:
    bad("cannot tokenise the arguments (%s)" % e)
if not a:
    bad("no -m <message> argument")
if len(a) % 2:
    bad("arguments are not -m <message> pairs (odd count %d)" % len(a))
for k in range(0, len(a), 2):
    if a[k] != "-m":
        bad("argument %r is not -m (only -m <message> pairs are allowed)" % a[k])
print("OK")
' 2>/dev/null) || _sm="ERR stack-master form parser failed"
  if [ "$_sm" != "OK" ]; then
    echo "Commit denied: the stack master commits with exactly \`git commit -m \"<message>\"\` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — ${_sm#ERR }. No pathspec, no other flags, no cd/&&/;, no git -C, no \$(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no \$ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form." >&2
    exit 2
  fi
  # Fix C (A2): the gate hashes and write-trees ROOT; the Bash call runs in the
  # payload's cwd. A different cwd (another worktree of the same repo, a
  # subdirectory with its own repo) would commit a different index. Require
  # cwd present and identical to ROOT. Before token lookup: token NOT consumed.
  _pcwd=$(pj cwd)
  _pcwd_rp=$( [ -n "$_pcwd" ] && /bin/realpath "$_pcwd" 2>/dev/null )
  _root_rp=$(/bin/realpath "$ROOT" 2>/dev/null)
  if [ -z "$_pcwd_rp" ] || [ -z "$_root_rp" ] || [ "$_pcwd_rp" != "$_root_rp" ]; then
    echo "Commit denied: the stack master must commit from the repo root — payload cwd '${_pcwd:-missing}' (resolved '${_pcwd_rp:-unresolvable}') is not the project root '${_root_rp:-$ROOT}'. The gate checks the root's index; a commit from another directory or worktree would record a different one. Run \`cd \"$ROOT\"\` in its own Bash call, then re-issue the commit. Token NOT consumed." >&2
    exit 2
  fi
  # W15 Fix (attack D1, 2026-11-04): core.worktree=<parent of ROOT> plus
  # diff.relative=true made the canonical diff at ROOT cover only ROOT's
  # subtree, so a staged file outside it was never hashed yet was committed.
  # --no-relative is now in the canonical command; additionally require git's
  # toplevel at ROOT to BE ROOT. Before token lookup: token NOT consumed.
  _top=$(env -u GIT_INDEX_FILE git -C "$ROOT" rev-parse --show-toplevel 2>/dev/null)
  _top_rp=$( [ -n "$_top" ] && /bin/realpath "$_top" 2>/dev/null )
  if [ -z "$_top_rp" ] || [ -z "$_root_rp" ] || [ "$_top_rp" != "$_root_rp" ]; then
    echo "Commit denied: repo toplevel '${_top_rp:-${_top:-unresolvable}}' is not the project root '${_root_rp:-$ROOT}' (core.worktree or similar config moves the work tree; the audited diff would not cover the whole commit). Remove the override in its own Bash call, then re-issue the commit. Token NOT consumed." >&2
    exit 2
  fi
  # W13 Fix 3 (A4/A4b): a git hook runs INSIDE the commit, after this gate
  # allows, and can stage extra content and rewrite last-allowed so the
  # PostToolUse detector stays silent. Resolve the EFFECTIVE hooks dir
  # (`rev-parse --git-path hooks` honours core.hooksPath; this repo sets it to
  # .beads/hooks) and require it to be unchanged from what was committed:
  #   inside ROOT (and not inside the git dir): deny when
  #     `git status --porcelain --untracked-files=all --ignored -- <dir>` is
  #     non-empty (modified / staged / untracked / ignored hook files), and,
  #     belt-and-braces against assume-unchanged/skip-worktree, deny when any
  #     non-directory entry directly in it is a symlink, has no HEAD blob,
  #     differs from its HEAD blob (hash-object --no-filters), or is
  #     executable while HEAD's mode is not 100755.
  #   outside ROOT, or inside the git dir (e.g. .git/hooks): deny when any
  #     non-directory entry directly in it is executable and not *.sample.
  # A missing hooks dir means no hooks run: pass. Any probe failure denies.
  # git status runs with GIT_OPTIONAL_LOCKS=0 so it never refreshes/writes the index.
  # Before token lookup: token NOT consumed.
  deny_hooks() {
    echo "Commit denied: git hooks dir '${_hd_rp:-${_hd:-unresolved}}' — $1. A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed." >&2
    exit 2
  }
  _hd=$(env -u GIT_INDEX_FILE git -C "$ROOT" rev-parse --git-path hooks 2>/dev/null) || deny_hooks "cannot resolve the effective hooks dir"
  [ -n "$_hd" ] || deny_hooks "effective hooks dir resolved to empty"
  case "$_hd" in /*) ;; *) _hd="$ROOT/$_hd" ;; esac
  if [ -e "$_hd" ] || [ -L "$_hd" ]; then
    _hd_rp=$(/bin/realpath "$_hd" 2>/dev/null) || deny_hooks "cannot resolve its realpath"
    [ -d "$_hd_rp" ] || deny_hooks "it is not a directory"
    _gd=$(env -u GIT_INDEX_FILE git -C "$ROOT" rev-parse --absolute-git-dir 2>/dev/null) || deny_hooks "cannot resolve the git dir"
    _gd_rp=$(/bin/realpath "$_gd" 2>/dev/null) || deny_hooks "cannot resolve the git dir realpath"
    _gc=$(cd "$ROOT" && env -u GIT_INDEX_FILE git rev-parse --git-common-dir 2>/dev/null) || deny_hooks "cannot resolve the git common dir"
    case "$_gc" in /*) ;; *) _gc="$ROOT/$_gc" ;; esac
    _gc_rp=$(/bin/realpath "$_gc" 2>/dev/null) || deny_hooks "cannot resolve the git common dir realpath"
    _hk_in=0
    case "$_hd_rp/" in "$_root_rp"/*) _hk_in=1 ;; esac
    case "$_hd_rp/" in "$_gd_rp"/*|"$_gc_rp"/*) _hk_in=0 ;; esac
    if [ "$_hk_in" = 1 ]; then
      _hrel=${_hd_rp#"$_root_rp"}; _hrel=${_hrel#/}; [ -n "$_hrel" ] || _hrel=.
      _hst=$(env -u GIT_INDEX_FILE GIT_OPTIONAL_LOCKS=0 git --literal-pathspecs -C "$_root_rp" status --porcelain --untracked-files=all --ignored -- "$_hrel" 2>/dev/null) \
        || deny_hooks "git status on it failed"
      [ -z "$_hst" ] || deny_hooks "it is inside the repo and differs from HEAD (git status: $(printf '%s' "$_hst" | head -n 5 | tr '\n' ';'))"
      for _hf in "$_hd_rp"/* "$_hd_rp"/.[!.]* "$_hd_rp"/..?*; do
        [ -e "$_hf" ] || [ -L "$_hf" ] || continue
        [ -L "$_hf" ] && deny_hooks "entry '${_hf##*/}' is a symlink"
        [ -d "$_hf" ] && continue
        _hrf="$_hrel/${_hf##*/}"; [ "$_hrel" = . ] && _hrf="${_hf##*/}"
        _hlt=$(env -u GIT_INDEX_FILE git --literal-pathspecs -C "$_root_rp" ls-tree HEAD -- "$_hrf" 2>/dev/null)
        [ -n "$_hlt" ] || deny_hooks "entry '${_hf##*/}' is not in HEAD"
        _hmode=${_hlt%% *}; _hsha=$(printf '%s' "$_hlt" | awk '{print $3}')
        _hnow=$(env -u GIT_INDEX_FILE git -C "$_root_rp" hash-object --no-filters -- "$_hf" 2>/dev/null) || deny_hooks "cannot hash entry '${_hf##*/}'"
        [ "$_hnow" = "$_hsha" ] || deny_hooks "entry '${_hf##*/}' content differs from HEAD"
        if [ -x "$_hf" ] && [ "$_hmode" != 100755 ]; then deny_hooks "entry '${_hf##*/}' is executable but HEAD mode is $_hmode"; fi
      done
    else
      for _hf in "$_hd_rp"/* "$_hd_rp"/.[!.]* "$_hd_rp"/..?*; do
        [ -e "$_hf" ] || [ -L "$_hf" ] || continue
        [ -d "$_hf" ] && continue
        case "${_hf##*/}" in *.sample) continue ;; esac
        [ -x "$_hf" ] && deny_hooks "it is outside the work tree (or in the git dir) and holds an executable non-.sample hook '${_hf##*/}'"
      done
    fi
  fi
fi

# --- Index selection (D-2026-11-04-B item 4). Runs BEFORE token lookup so a
# denial here never consumes a token. IDX=REAL means the repo's own index,
# hashed with GIT_INDEX_FILE removed from the environment. ---
deny_index() {
  echo "Commit denied: $1" >&2
  echo "A temp-index commit must be the WHOLE Bash command, exactly: GIT_INDEX_FILE=/absolute/path/to/index git commit -m \"...\" — path unquoted ([A-Za-z0-9._/+-] only) and an existing regular file, INDEX_FILE appearing nowhere else, no env/export/;/&&/|/redirection/\$(...)/backticks/backslashes outside quotes. Otherwise commit the real index with a plain git commit and no GIT_INDEX_FILE." >&2
  exit 2
}
if [ -n "${GIT_INDEX_FILE:-}" ]; then
  deny_index "GIT_INDEX_FILE is set in the gate's own environment ('$GIT_INDEX_FILE') — the hashed index would not be the one the commit uses"
fi
IDX=REAL
case "$CMD" in
  *INDEX_FILE*)
    # Whole-string parse (python: grep/sed are line-based and would let a
    # newline smuggle a second command). Prints the index path on success, or
    # "ERR <reason>" on failure.
    _ix=$(printf '%s' "$CMD" | python3 -c '
import re, sys
# Fix B: strip ONLY ASCII space/tab; outside quotes allow ONLY SAFE (+ quotes)
s = sys.stdin.read().strip(" \t")
SAFE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \t._/+=,:@%-")
def bad(r):
    print("ERR " + r); sys.exit(0)
if s.count("INDEX_FILE") != 1:
    bad("INDEX_FILE appears %d times in the command (exactly one allowed)" % s.count("INDEX_FILE"))
m = re.match(r"GIT_INDEX_FILE=(/[A-Za-z0-9._/+-]+)[ \t]+git[ \t]+commit(?=[ \t]|$)", s)
if not m:
    bad("command is not of the form GIT_INDEX_FILE=<absolute unquoted path> git commit ... (env/export/prefix/quoted/relative forms are refused)")
# Quote-aware scan: outside quotes allow ONLY SAFE (so ; & | < > ( ) backtick $
# backslash newline CR VT NBSP non-ASCII ... all refuse); inside double quotes
# refuse backtick and $( (they execute).
st = None; i = 0; n = len(s)
while i < n:
    c = s[i]
    if st is None:
        if c == "\x27": st = "s"
        elif c == "\"": st = "d"
        elif c not in SAFE: bad("character %r (U+%04X) outside quotes is not in [A-Za-z0-9 \\t._/+=,:@%%-]" % (c, ord(c)))
    elif st == "s":
        if c == "\x27": st = None
    else:
        if c == "\"": st = None
        elif c == "\\": i += 1
        elif c == "`": bad("backtick inside double quotes")
        elif c == "$" and s[i+1:i+2] == "(": bad("$( inside double quotes")
    i += 1
if st is not None:
    bad("unterminated quote")
print(m.group(1))
' 2>/dev/null) || _ix="ERR index-form parser failed"
    case "$_ix" in
      ""|ERR*) deny_index "${_ix#ERR }" ;;
    esac
    # belt-and-braces: the brief's SCRUB check (sed-scrubbed, line-based)
    if printf '%s' "$SCRUB" | grep -Eq '[;&|`<>]|\$\('; then
      deny_index "shell metacharacter outside the quoted message"
    fi
    [ -f "$_ix" ] || deny_index "index path '$_ix' is not an existing regular file"
    # normalise exactly as the minter does (ap_index_norm) when the lib loads;
    # otherwise fall back to realpath + the same REAL comparison.
    _lib="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)/audit-provenance.sh"
    [ -f "$_lib" ] && . "$_lib" 2>/dev/null
    if type ap_index_norm >/dev/null 2>&1; then
      IDX=$(ap_index_norm "$ROOT" "$_ix") || deny_index "ap_index_norm rejected index path '$_ix'"
    else
      _rp=$(/bin/realpath "$_ix" 2>/dev/null) || deny_index "cannot resolve index path '$_ix'"
      _real=$(cd "$ROOT" && env -u GIT_INDEX_FILE git rev-parse --git-path index 2>/dev/null) || deny_index "cannot locate the repo's real index"
      case "$_real" in /*) ;; *) _real="$ROOT/$_real" ;; esac
      _realrp=$(/bin/realpath "$_real" 2>/dev/null) || _realrp="$_real"
      if [ "$_rp" = "$_realrp" ]; then IDX=REAL; else IDX="$_rp"; fi
    fi
    [ -n "$IDX" ] || deny_index "index path normalised to empty"
    ;;
esac
# git under the selected index (REAL => GIT_INDEX_FILE removed from env)
git_idx() {
  if [ "$IDX" = "REAL" ]; then
    (cd "$ROOT" && env -u GIT_INDEX_FILE git "$@")
  else
    (cd "$ROOT" && GIT_INDEX_FILE="$IDX" git "$@")
  fi
}

# --- Fix D helper (A8). handback_check <agent_id> <agent_transcript>
# <parent_transcript_realpath> <hash>: 0 iff the parent transcript holds the
# harness-written result of the Agent call that spawned agent_id, and it
# carries `COMMIT-DIFF-SHA256: <hash>`. Prints a one-line reason on failure.
#   1. toolUseId := agent-<id>.meta.json beside the agent transcript.
#   2. a `type=="user"` record with a `.message.content[]` block
#      {type:"tool_result", tool_use_id:<toolUseId>} whose text (string, or the
#      joined text of {type:"text"} blocks) has a line matching
#      ^agentId: <id>([^A-Za-z0-9_-]|$) — the harness writes it at column 0;
#      a forged meta.json reusing a genuine earlier toolUseId names a
#      DIFFERENT agentId there.
#   3. a line that trims to `COMMIT-DIFF-SHA256: <hash>`, EITHER in that same
#      tool_result text (synchronous Agent call: the report is in the result,
#      every line indented) OR between a column-0 `<agent-message
#      from="<id>">` line and the next column-0 `</agent-message>` line of a
#      `type=="user"` record (background Agent call: the tool_result is only
#      the "Async agent launched ... agentId: <id>" stub and the report arrives
#      as a separate hand-back record; the harness indents every report line,
#      so a column-0 frame inside a report cannot occur). W13: OR the same
#      frame scan over a `type=="attachment"` record with
#      .attachment.type=="queued_command" whose .attachment.prompt BEGINS with
#      that frame line (hand-back arriving while the main thread is mid-turn;
#      no type:"user" record is written — observed 2026-11-04 in this repo's
#      main transcript for agents a68b1edece72d2bf9 and a1c957a9dde5a9900).
#      W-TN (2026-11-06, ruling 3b): OR inside the `<result>` span of the
#      FIRST block of a `type=="user"` record (not isMeta) with
#      .origin.kind=="task-notification" whose content BEGINS with
#      "<task-notification>\n": only that block's FIRST `<task-id>` line counts
#      (must be <id>), its `<status>` must be `completed`, and the hash line must
#      lie between `<result>` and the line that ends in `</result>` (the harness
#      puts `</result>` on the hash line itself). Result lines are NOT indented,
#      so any later or nested block (forgeable by whoever controls another
#      agent's report) is never read. The `<summary>` line repeats the
#      master-chosen description, so the description is bound from the
#      harness-written assistant tool_use with id <toolUseId> (one non-empty
#      string, no newline/CR/</>/"/&), the block's first `<summary>` must equal
#      `<summary>Agent "<description>" finished</summary>` exactly (partial-result
#      and "waiting" notifications fail), and a second `<status>` or `<summary>`
#      ends the scan. Captured 2026-11-06 from this repo's main
#      transcript (agents a9d35d34f3b18e943, a66e2698ac35ce15f).
# The sync and agent-message shapes were captured from this repo's real session
# transcripts on 2026-11-04 (sync: a praxis-manager subagent's transcript;
# background: the main-thread transcript). Pre-filter with /usr/bin/grep -F, then jq.
handback_check() {
  local aid="${1:-}" at="${2:-}" pt="${3:-}" hash="${4:-}" at_rp meta tuid line trs v
  [[ "$aid" =~ ^[A-Za-z0-9_-]{1,64}$ ]] || { echo "agent_id malformed"; return 1; }
  [[ "$hash" =~ ^[0-9a-f]{64}$ ]] || { echo "hash malformed"; return 1; }
  { [ -n "$pt" ] && [ -f "$pt" ]; } || { echo "parent transcript missing"; return 1; }
  at_rp=$(/bin/realpath "$at" 2>/dev/null) || { echo "agent transcript does not resolve"; return 1; }
  meta="$(dirname "$at_rp")/agent-$aid.meta.json"
  tuid=$(jq -r '(.toolUseId // "") | strings' "$meta" 2>/dev/null)
  [ -n "$tuid" ] || { echo "meta.json toolUseId missing"; return 1; }
  line="COMMIT-DIFF-SHA256: $hash"
  trs=$(/usr/bin/grep -F -- "$tuid" "$pt" 2>/dev/null | jq -R -c --arg id "$tuid" '
      fromjson? | select(type == "object" and .type == "user")
      | .message.content? | select(type == "array") | .[]
      | select(type == "object" and .type == "tool_result" and .tool_use_id == $id)
      | .content
      | if type == "string" then .
        elif type == "array" then ([.[] | select(type == "object" and .type == "text") | .text | strings] | join("\n"))
        else empty end' 2>/dev/null)
  [ -n "$trs" ] || { echo "parent transcript has no tool_result for $tuid"; return 1; }
  v=$(printf '%s\n' "$trs" | jq -s -r --arg aid "$aid" --arg line "$line" '
      [ .[] | strings | select(split("\n") | any(.[]; test("^agentId: " + $aid + "([^A-Za-z0-9_-]|$)"))) ] as $b
      | if ($b | length) == 0 then "NOBIND"
        elif any($b[]; split("\n") | any(.[]; gsub("^\\s+|\\s+$"; "") == $line)) then "SYNC"
        else "BOUND" end' 2>/dev/null)
  case "$v" in
    SYNC) return 0 ;;
    BOUND) ;;
    NOBIND) echo "the tool_result for $tuid does not name agentId: $aid (that toolUseId spawned a different agent)"; return 1 ;;
    *) echo "tool_result check could not be evaluated"; return 1 ;;
  esac
  v=$(/usr/bin/grep -F -- "agent-message from=\\\"$aid\\\"" "$pt" 2>/dev/null | jq -R -r --arg aid "$aid" --arg line "$line" '
      fromjson? | select(type == "object")
      | if .type == "user" then
          (.message.content?
           | if type == "string" then .
             elif type == "array" then ([.[] | select(type == "object" and .type == "text") | .text | strings] | join("\n"))
             else empty end)
        elif .type == "attachment" then
          # W13 (b-attach): mid-turn hand-back = attachment/queued_command whose
          # .prompt BEGINS with the frame line. Only .prompt is read (the
          # unindented .origin.body/.handbackReportText copies are ignored).
          (.attachment? | select(type == "object" and .type == "queued_command")
           | .prompt | strings
           | select(startswith("<agent-message from=\"" + $aid + "\">\n")))
        else empty end
      | reduce (split("\n")[]) as $l ({in: false, hit: false};
          if .in then
            (if $l == "</agent-message>" then .in = false
             elif ($l | gsub("^\\s+|\\s+$"; "")) == $line then .hit = true
             else . end)
          elif $l == ("<agent-message from=\"" + $aid + "\">") then .in = true
          else . end)
      | select(.hit) | "HIT"' 2>/dev/null | head -n 1)
  [ "$v" = "HIT" ] && return 0
  # W-TN 2026-11-06 (ruling 3b) BEGIN
  # Async hand-back as a task-notification: a type=="user" record, origin.kind
  # "task-notification", content (a string) BEGINS "<task-notification>\n";
  # header lines <task-id>/<tool-use-id>/<output-file>/<status>/<summary>/<note>,
  # then "<result>" + the report's first line, report lines at COLUMN 0, and
  # "</result>" on the same line as the last report line (the hash line). Only
  # the FIRST block and its FIRST <task-id> line count; status must be
  # completed; the hash must sit inside that block's <result> span.
  # The <summary> line repeats the master-chosen Agent description, so the
  # description is read from the harness-written assistant tool_use whose id is
  # <toolUseId> (never meta.json) and must be one non-empty string free of
  # newline/CR/</>/"/&. The FIRST <status> and FIRST <summary> lines decide (a
  # second of either ends the scan), and that summary must equal
  # `<summary>Agent "<description>" finished</summary>` exactly.
  local dsc desc
  dsc=$(/usr/bin/grep -F -- "$tuid" "$pt" 2>/dev/null | jq -R -s -r --arg id "$tuid" '
      [ split("\n")[] | fromjson? | select(type == "object" and .type == "assistant")
        | .message.content? | select(type == "array") | .[]
        | select(type == "object" and .type == "tool_use" and .id == $id)
        | .input.description? ] as $d
      | if ($d | length) == 0 then "NONE"
        elif ($d | all(.[]; type == "string" and length > 0 and (test("[\\n\\r<>\"&]") | not)))
             and ($d | unique | length) == 1 then "OK " + $d[0]
        else "BAD" end' 2>/dev/null)
  case "$dsc" in
    "OK "*) desc=${dsc#OK } ;;
    *) echo "no hand-back carries the line '$line', and the task-notification check cannot run: the Agent call $tuid has no single plain description (missing, or contains newline/CR/</>/\"/&)"; return 1 ;;
  esac
  v=$(/usr/bin/grep -F -- "<task-id>$aid</task-id>" "$pt" 2>/dev/null | jq -R -r --arg aid "$aid" --arg line "$line" --arg sum "<summary>Agent \"$desc\" finished</summary>" '
      fromjson? | select(type == "object" and .type == "user"
                         and (.origin? | type == "object" and .kind == "task-notification")
                         and (.isMeta? != true))
      | (.message.content?
         | if type == "string" then .
           elif type == "array" then ([.[] | select(type == "object" and .type == "text") | .text | strings] | join("\n"))
           else empty end)
      | select(startswith("<task-notification>\n"))
      | reduce (split("\n")[]) as $l ({st: "open", id: false, seen: false, done: false, sseen: false, sm: false, mseen: false, hit: false};
          if .st == "open" then .st = (if $l == "<task-notification>" then "head" else "end" end)
          elif .st == "head" then
            (if $l == "</task-notification>" then .st = "end"
             elif ($l | startswith("<task-id>")) then
               (if .seen then .st = "end"
                else .seen = true | .id = (($l | gsub("^\\s+|\\s+$"; "")) == ("<task-id>" + $aid + "</task-id>")) end)
             elif ($l | startswith("<status>")) then
               (if .sseen then .st = "end"
                else .sseen = true | .done = (($l | gsub("^\\s+|\\s+$"; "")) == "<status>completed</status>") end)
             elif ($l | startswith("<summary>")) then
               (if .mseen then .st = "end" else .mseen = true | .sm = ($l == $sum) end)
             elif ($l | startswith("<result>")) then
               (if (.id and .done and .sm) then
                  ($l | ltrimstr("<result>")) as $b
                  | (if ($b | endswith("</result>")) then .st = "end" else .st = "result" end)
                  | (if (($b | rtrimstr("</result>") | gsub("^\\s+|\\s+$"; "")) == $line) then .hit = true else . end)
                else .st = "end" end)
             else . end)
          elif .st == "result" then
            (if (($l | rtrimstr("</result>") | gsub("^\\s+|\\s+$"; "")) == $line) then .hit = true else . end)
            | (if ($l | endswith("</result>")) then .st = "end" else . end)
          else . end)
      | select(.hit) | "HIT"' 2>/dev/null | head -n 1)
  [ "$v" = "HIT" ] && return 0
  # W-TN 2026-11-06 (ruling 3b) END
  echo "neither the tool_result for $tuid nor a hand-back frame from $aid carries the line '$line'"
  return 1
}

# --- Single-session check: deny while another live claude process (outside this
# session's own process tree) is cwd'd inside this repo. Runs BEFORE token lookup
# so it never consumes the token — close the other session and retry. Any failure
# of the check itself denies (fail CLOSED); the trader can rerun. ---
deny_session() {
  echo "Commit denied: $1" >&2
  echo "Single-session rule: exactly ONE Claude session per repo working tree (docs/runbooks/2026-07-10-single-session-rule.md). Close the other session (or move it to its own git worktree) and re-run the commit." >&2
  exit 2
}
REPO=$(cd "$ROOT" 2>/dev/null && pwd -P) || deny_session "cannot resolve repo root '$ROOT' for the single-session check"
# argv[0] basename starts with "claude" → it is a claude session process
is_claude_pid() {
  _c=$(ps -o command= -p "$1" 2>/dev/null) || return 1
  _first=${_c%% *}
  case "${_first##*/}" in claude*) return 0 ;; *) return 1 ;; esac
}
# our own claude ancestor: walk PPID up from this hook shell
MY_CLAUDE=""
_p=$$
while [ -n "$_p" ] && [ "$_p" != "0" ] && [ "$_p" != "1" ]; do
  if is_claude_pid "$_p"; then MY_CLAUDE="$_p"; break; fi
  _p=$(ps -o ppid= -p "$_p" 2>/dev/null | tr -d ' ')
done
# is pid our own session's process (== our claude ancestor, or descends from it)?
descends_from_mine() {
  [ -n "$MY_CLAUDE" ] || return 1
  _q=$1 _hops=0
  while [ -n "$_q" ] && [ "$_q" != "0" ] && [ "$_q" != "1" ] && [ "$_hops" -lt 64 ]; do
    [ "$_q" = "$MY_CLAUDE" ] && return 0
    _q=$(ps -o ppid= -p "$_q" 2>/dev/null | tr -d ' ')
    _hops=$((_hops + 1))
  done
  return 1
}
# every process with a cwd, as -Fpn records (p<pid> / n<path>); command names are
# NOT trusted here — lsof truncates/mangles them (observed "claude.ex", "2.1.206")
LSOF_OUT=$(lsof -a -d cwd -Fpn 2>/dev/null)
[ -n "$LSOF_OUT" ] || deny_session "single-session check failed: lsof produced no data"
FOREIGN=""
CUR=""
while IFS= read -r LINE; do
  case "$LINE" in
    p*) CUR="${LINE#p}" ;;
    n*) DIR="${LINE#n}"
        case "$DIR" in
          "$REPO"|"$REPO"/*)
            [ -n "$CUR" ] || continue
            descends_from_mine "$CUR" && continue
            is_claude_pid "$CUR" && FOREIGN="$FOREIGN $CUR"
            ;;
        esac ;;
  esac
done <<EOF_LSOF
$LSOF_OUT
EOF_LSOF
if [ -n "$FOREIGN" ]; then
  deny_session "another live claude session (pid$FOREIGN) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)"
fi

# --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
# PASS row in AUDIT_LOG.md is honored (a bare `touch`ed token is forgery). ---
# Sweep orphaned tokens first: a token whose staged diff drifted (re-audit minted
# a new hash) previously lingered forever; anything >30 min old is dead either way.
find "$STATE" -name 'audit-pass-*' -mmin +30 -exec rm -f {} + 2>/dev/null
# Fix A (A10): canonical diff command — no external diff driver, no textconv,
# no colour — identical bytes to what the minter hashes. W13 (A1a/A1b/A2a-e):
# --text replaces --binary (an attribute/bigFileThreshold can no longer turn a
# file into an opaque base85 patch) and --ignore-submodules=none (a repo
# diff.ignoreSubmodules=all can no longer hide a gitlink).
HASH=$(git_idx diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256 | awk '{print $1}')
TOKEN="$STATE/audit-pass-$HASH"
# (caller identity / STACK_MASTER is computed above, before the form checks)
if [ -f "$TOKEN" ]; then
  NOW=$(date +%s)
  MT=$(stat -f %m "$TOKEN")
  if [ $((NOW - MT)) -gt 1800 ]; then
    rm -f "$TOKEN"
    echo "Commit denied: audit token expired (>30 min old). Re-dispatch the auditor (praxis-auditor for the stack master, orchestrator-auditor otherwise) to re-grade the staged diff." >&2
    exit 2
  fi
  tok() { sed -n "s/^$1=//p" "$TOKEN" | head -1; }
  T_MINTER=$(tok minter)
  T_INDEX=$(tok index)
  [ -n "$T_INDEX" ] || T_INDEX=REAL          # legacy token: real index
  [ -n "$T_MINTER" ] || T_MINTER=legacy      # legacy token: audit-approve.sh
  # stack master: only a praxis-auditor PASS. A legacy token is NOT deleted — it
  # may belong to the orchestrator route; running audit-approve.sh by hand does
  # not let the master commit.
  if [ "$STACK_MASTER" = 1 ] && [ "$T_MINTER" != "praxis-auditor" ]; then
    echo "Commit denied: the stack master (main-thread praxis-master) needs a praxis-auditor PASS token for this exact diff; this token was minted by '$T_MINTER' (audit-approve.sh/orchestrator route), which is not accepted for praxis-master. Dispatch praxis-auditor with COMMIT-INDEX/COMMIT-DIFF-SHA256 lines. Never run audit-approve.sh yourself." >&2
    exit 2
  fi
  case "$T_MINTER" in
    legacy|praxis-auditor) ;;
    *) rm -f "$TOKEN"
       echo "Commit denied: token names an unknown minter '$T_MINTER' — forged or corrupted; re-dispatch the auditor." >&2
       exit 2 ;;
  esac
  if [ "$T_INDEX" != "$IDX" ]; then
    rm -f "$TOKEN"
    echo "Commit denied: token was minted for index '$T_INDEX' but this commit uses index '$IDX'. Re-audit the index you are committing." >&2
    exit 2
  fi
  if ! grep -q "$HASH PASS" "$ROOT/AUDIT_LOG.md" 2>/dev/null; then
    rm -f "$TOKEN"
    echo "Commit denied: token has no AUDIT_LOG PASS row — forged or corrupted; re-dispatch the auditor." >&2
    exit 2
  fi
  if [ "$T_MINTER" = "praxis-auditor" ]; then
    # provenance re-check via the shared lib; missing/unsourceable lib fails
    # CLOSED (token kept: infrastructure fault, not a forgery verdict).
    _lib="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)/audit-provenance.sh"
    if ! type ap_verify >/dev/null 2>&1; then
      { [ -f "$_lib" ] && . "$_lib"; } 2>/dev/null
    fi
    if ! type ap_verify >/dev/null 2>&1; then
      echo "Commit denied: provenance library '$_lib' is missing or failed to source — cannot verify the praxis-auditor token (fail closed)." >&2
      exit 2
    fi
    T_AID=$(tok agent_id)
    T_AT=$(tok agent_transcript)
    T_PT=$(tok parent_transcript)
    if ! _why=$(ap_verify "$T_AID" "$T_AT" "$T_PT" "$HASH" 2>&1); then
      rm -f "$TOKEN"
      echo "Commit denied: praxis-auditor token failed provenance verification (${_why:-no reason}). Re-dispatch praxis-auditor." >&2
      exit 2
    fi
    P_TP=$(pj transcript_path)
    P_TP_RP=$( [ -n "$P_TP" ] && /bin/realpath "$P_TP" 2>/dev/null )
    T_PT_RP=$( [ -n "$T_PT" ] && /bin/realpath "$T_PT" 2>/dev/null )
    if [ -z "$P_TP_RP" ] || [ -z "$T_PT_RP" ] || [ "$P_TP_RP" != "$T_PT_RP" ]; then
      rm -f "$TOKEN"
      echo "Commit denied: praxis-auditor token was minted for session transcript '${T_PT:-missing}', but this commit comes from '${P_TP:-missing}'. Only the session that dispatched the auditor may use its PASS." >&2
      exit 2
    fi
    # Fix D (A8): the parent transcript must carry the harness-written result
    # of THIS auditor's Agent call, naming this agent_id and this HASH.
    if ! _why=$(handback_check "$T_AID" "$T_AT" "$T_PT_RP" "$HASH" 2>&1); then
      rm -f "$TOKEN"
      echo "Commit denied: praxis-auditor token failed the parent-transcript hand-back check (${_why:-no reason}). The session transcript must hold the Agent result for this auditor (agentId line) carrying 'COMMIT-DIFF-SHA256: $HASH'. Re-dispatch praxis-auditor." >&2
      exit 2
    fi
  fi
  # staged-TREE binding: the index must still produce the exact tree the token
  # was minted against — extra/missing/changed paths in the mint→commit gap deny.
  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
  NOW_TREE=$(git_idx write-tree 2>/dev/null)
  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
    rm -f "$TOKEN"
    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MINT_TREE:-missing/legacy-token}, current tree=${NOW_TREE:-unresolvable}). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor." >&2
    exit 2
  fi
  # Fix E (A1/A3): record what was allowed, for scripts/commit-tree-verify.sh
  # (PostToolUse) to compare against the landed HEAD^{tree}. Written atomically
  # BEFORE the token is consumed; a write failure denies (token kept).
  _hb=$(cd "$ROOT" && git rev-parse -q --verify HEAD 2>/dev/null) || _hb=none
  [ -n "$_hb" ] || _hb=none
  _csha=$(printf '%s' "$CMD" | shasum -a 256 | awk '{print $1}')
  _la="$STATE/last-allowed"
  if ! { printf 'tree=%s\nindex=%s\nhash=%s\nhead_before=%s\nts=%s\ncmd_sha256=%s\n' \
           "$MINT_TREE" "$IDX" "$HASH" "$_hb" "$(date +%s)" "$_csha" > "$_la.tmp.$$" \
         && mv -f "$_la.tmp.$$" "$_la"; } 2>/dev/null; then
    rm -f "$_la.tmp.$$" 2>/dev/null
    echo "Commit denied: cannot write $_la (post-commit tree verification record). Token NOT consumed; fix .claude/state and retry." >&2
    exit 2
  fi
  rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
  exit 0
fi
echo "Commit denied: no audit PASS token for this exact staged diff under index '$IDX' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself." >&2
exit 2
