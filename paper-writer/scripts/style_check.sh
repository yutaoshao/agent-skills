#!/usr/bin/env bash
set -euo pipefail

# De-AI Style Checker for academic papers
# Scans markdown/tex files for common AI writing patterns
# Usage: bash scripts/style_check.sh <file>

FILE="${1:-}"
if [[ -z "$FILE" ]]; then
  echo "Usage: bash scripts/style_check.sh <markdown_or_tex_file>"
  exit 1
fi
if [[ ! -f "$FILE" ]]; then
  echo "File not found: $FILE"
  exit 1
fi

echo "=== De-AI Style Check: $FILE ==="
ISSUES=0

printf "\n[1] Bold-label paragraph openers (\\textbf or **):\n"
if rg -n '\\textbf\{[^}]+\}\.' "$FILE" 2>/dev/null || rg -n '^\*\*[^*]+\*\*[.:]' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[2] High-frequency AI transition words (EN):\n"
if rg -ni '^\s*(Furthermore|Moreover|Additionally|Notably|Importantly|Interestingly|Crucially|Specifically|Consequently|Nevertheless)[,.]' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[3] Filler phrases (EN):\n"
if rg -ni 'It is worth noting that|It should be noted that|It is important to mention|plays a crucial role|in a comprehensive manner|a wide range of|state-of-the-art' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[4] Overused AI vocabulary (EN):\n"
if rg -ni '\b(leverage[ds]?|utilize[ds]?|harness|delve|paradigm|seamless|landscape|plethora|synergy|holistic|elucidate|pivotal|myriad)\b' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[5] Banned Chinese transitions:\n"
if rg -n '首先|其次|最后|此外|另外|接下来|值得注意的是|需要指出的是|重要的是|必须强调的是' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[6] Subjective first-person phrases:\n"
if rg -ni '我认为|我觉得|我个人|我的研究|in my opinion|i believe' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[7] Superlative claims without evidence:\n"
if rg -ni 'significantly (outperform|improve|better|superior)|dramatically improve|perfectly handle' "$FILE" 2>/dev/null; then
  ISSUES=$((ISSUES + 1))
else
  echo "  OK"
fi

printf "\n[8] List lines in body text (review manually):\n"
if rg -n '^\s*([-*+]\s+|[0-9]+\.\s+)' "$FILE" 2>/dev/null | head -10; then
  echo "  (Review above: lists are OK in methods/appendix, not in body prose)"
else
  echo "  OK"
fi

printf "\n=== Summary: %d category/categories flagged ===\n" "$ISSUES"
if [[ $ISSUES -eq 0 ]]; then
  echo "Paper passes de-AI style check."
else
  echo "Review flagged items above."
fi
