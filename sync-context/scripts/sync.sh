#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$SKILL_DIR/.." && pwd)"

CONTEXT_FILE="$REPO_ROOT/CONTEXT.md"
CONTEXT_DIR="$REPO_ROOT/context"

STALE_HOURS="${SYNC_CONTEXT_STALE_HOURS:-24}"
MAX_LINES="${SYNC_CONTEXT_MAX_LINES:-200}"

# Sections that must be updated every session
handoff_sections=(
  "## In Progress"
  "## Recent Changes"
  "## Next Steps"
  "## Blockers & Open Questions"
)

# Sections that serve as long-lived references
reference_sections=(
  "## Project Overview"
  "## Architecture"
  "## Conventions"
  "## Key Files"
)

print_usage() {
  cat <<EOF
Usage: $0 <command>

Commands:
  init    Create a template CONTEXT.md in the project root
  check   Validate CONTEXT.md structure and freshness
  inject  Output CONTEXT.md formatted for a new AI session
EOF
}

# --- helpers ---

require_file() {
  if [[ ! -f "$1" ]]; then
    printf 'ERROR: Missing required file: %s\n' "$1" >&2
    return 1
  fi
}

check_sections() {
  local file="$1"
  shift
  local section
  for section in "$@"; do
    if ! grep -Fq "$section" "$file"; then
      ERRORS+=("Missing section in $(basename "$file"): $section")
    fi
  done
}

check_freshness() {
  local ts
  ts=$(sed -n 's/^> Last Updated: //p' "$CONTEXT_FILE" 2>/dev/null || true)
  if [[ -z "$ts" ]]; then
    WARNINGS+=("No 'Last Updated' timestamp found in CONTEXT.md")
    return 0
  fi
  # Strip timezone suffix for parsing (e.g. "2026-03-27 19:25 CST" -> "2026-03-27 19:25")
  local ts_clean="${ts% *}"
  local epoch_ts epoch_now diff_hours
  # macOS date
  epoch_ts=$(date -j -f "%Y-%m-%d %H:%M" "$ts_clean" +%s 2>/dev/null || true)
  # Linux fallback
  if [[ -z "$epoch_ts" ]]; then
    epoch_ts=$(date -d "$ts_clean" +%s 2>/dev/null || true)
  fi
  if [[ -z "$epoch_ts" ]]; then
    WARNINGS+=("Could not parse 'Last Updated' timestamp: $ts")
    return 0
  fi
  epoch_now=$(date +%s)
  diff_hours=$(( (epoch_now - epoch_ts) / 3600 ))
  if (( diff_hours > STALE_HOURS )); then
    WARNINGS+=("CONTEXT.md last updated $diff_hours hours ago (threshold: $STALE_HOURS h)")
  fi
}

check_size() {
  local lines
  lines=$(wc -l < "$CONTEXT_FILE" | tr -d ' ')
  if (( lines > MAX_LINES )); then
    WARNINGS+=("CONTEXT.md is $lines lines (threshold: $MAX_LINES). Consider moving reference sections to context/ subdirectory.")
  fi
}

# --- commands ---

cmd_init() {
  if [[ -f "$CONTEXT_FILE" ]]; then
    printf 'CONTEXT.md already exists at %s — skipping.\n' "$CONTEXT_FILE"
    return 0
  fi
  local now
  now=$(date "+%Y-%m-%d %H:%M %Z")
  cat > "$CONTEXT_FILE" <<TMPL
# Project Context

> Last Updated: $now

## In Progress

_Nothing in progress._

## Recent Changes

_No recent changes._

## Next Steps

- [ ] Define initial tasks

## Blockers & Open Questions

_None._

## Project Overview

_Describe the project here._

## Architecture

_Describe the high-level architecture here._

## Conventions

_List coding conventions here._

## Key Files

_List important file paths here._
TMPL
  printf 'Created %s\n' "$CONTEXT_FILE"
}

cmd_check() {
  ERRORS=()
  WARNINGS=()

  if ! require_file "$CONTEXT_FILE"; then
    ERRORS+=("Missing CONTEXT.md at $CONTEXT_FILE")
  else
    check_sections "$CONTEXT_FILE" "${handoff_sections[@]}" "${reference_sections[@]}"
    check_freshness
    check_size
  fi

  if (( ${#WARNINGS[@]} > 0 )); then
    echo "--- WARNINGS ---" >&2
    for w in "${WARNINGS[@]}"; do
      printf ' * %s\n' "$w" >&2
    done
    printf '\n' >&2
  fi

  if (( ${#ERRORS[@]} > 0 )); then
    echo "--- ERRORS ---" >&2
    for e in "${ERRORS[@]}"; do
      printf ' * %s\n' "$e" >&2
    done
    printf '\nContext check FAILED. Please fix the above issues before continuing.\n' >&2
    return 1
  fi

  printf 'Context check passed.\n'
}

cmd_inject() {
  if ! require_file "$CONTEXT_FILE"; then
    return 1
  fi
  cat <<'EOF'
[SYSTEM: Project state loaded from CONTEXT.md]
Read the following context carefully before taking any action. It represents the state left by the previous session.

EOF
  cat "$CONTEXT_FILE"

  # List available detail files in context/ if the directory exists
  if [[ -d "$CONTEXT_DIR" ]]; then
    local detail_files=()
    while IFS= read -r -d '' f; do
      detail_files+=("$(basename "$f")")
    done < <(find "$CONTEXT_DIR" -maxdepth 1 -name '*.md' -print0 2>/dev/null | sort -z)

    if (( ${#detail_files[@]} > 0 )); then
      printf '\n---\n'
      printf '[SYSTEM: Detail files available in context/ directory]\n'
      printf 'The following reference documents are available. Read them when you need deeper understanding for the area you are working on:\n\n'
      for f in "${detail_files[@]}"; do
        printf ' - context/%s\n' "$f"
      done
    fi
  fi
}

# --- main ---

main() {
  local command="${1:-}"
  case "$command" in
    init)   cmd_init   ;;
    check)  cmd_check  ;;
    inject) cmd_inject ;;
    *)
      print_usage >&2
      exit 1
      ;;
  esac
}

main "$@"
