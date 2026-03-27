#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$SKILL_DIR/.." && pwd)"

CLAUDE_FILE="$REPO_ROOT/CLAUDE.md"
AGENTS_FILE="$REPO_ROOT/AGENTS.md"
CONTEXT_FILE="$REPO_ROOT/CONTEXT.md"

required_sections=(
  "## Project Overview"
  "## Architecture Decisions"
  "## Current Status"
  "## Known Issues"
  "## Conventions"
  "## Important Files"
  "## Open Questions"
)

print_usage() {
  printf 'Usage: %s <sync|check>\n' "$0"
}

require_file() {
  local path="$1"
  if [[ ! -f "$path" ]]; then
    printf 'Missing required file: %s\n' "$path" >&2
    return 1
  fi
}

check_context_sections() {
  local missing=0
  local section
  for section in "${required_sections[@]}"; do
    if ! grep -Fqx "$section" "$CONTEXT_FILE"; then
      printf 'Missing required section in CONTEXT.md: %s\n' "$section" >&2
      missing=1
    fi
  done
  return "$missing"
}

sync_agents() {
  require_file "$CLAUDE_FILE"
  cp "$CLAUDE_FILE" "$AGENTS_FILE"
  printf 'Synced %s -> %s\n' "$CLAUDE_FILE" "$AGENTS_FILE"
}

check_sync() {
  require_file "$CONTEXT_FILE"
  require_file "$CLAUDE_FILE"
  require_file "$AGENTS_FILE"
  check_context_sections
  if ! cmp -s "$CLAUDE_FILE" "$AGENTS_FILE"; then
    printf 'AGENTS.md is out of sync with CLAUDE.md\n' >&2
    printf 'Run: "%s" sync\n' "$0" >&2
    return 1
  fi
  printf 'Context sync check passed.\n'
}

main() {
  local command="${1:-}"
  case "$command" in
    sync)
      sync_agents
      ;;
    check)
      check_sync
      ;;
    *)
      print_usage >&2
      exit 1
      ;;
  esac
}

main "$@"
