#!/usr/bin/env bash
set -euo pipefail

# Initialize plan/ directory from plan-template/
# Usage: bash scripts/init_plan.sh [project_dir]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$SKILL_DIR/plan-template"

PROJECT_DIR="${1:-.}"
PLAN_DIR="$PROJECT_DIR/plan"

if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "Error: plan-template/ not found at $TEMPLATE_DIR"
  exit 1
fi

mkdir -p "$PLAN_DIR"

for file in "$TEMPLATE_DIR"/*.md; do
  filename="$(basename "$file")"
  target="$PLAN_DIR/$filename"
  if [[ -f "$target" ]]; then
    echo "Skip (exists): $target"
  else
    cp "$file" "$target"
    echo "Created: $target"
  fi
done

echo "Done. plan/ initialized at $PLAN_DIR"
