#!/usr/bin/env bash
# Validate that all ai-native-core `implements` references in this repo
# point to contracts that actually exist in the core manifest.
#
# Usage:
#   ./validate-implements.sh [path-to-core]
#
# If path-to-core is omitted, looks for ../ai-native-core or ./core (submodule).
# Exit code 0 = all valid, 1 = broken references found.
set -euo pipefail

# ── Locate core ──────────────────────────────────────────────────────────────
CORE="${1:-}"
if [ -z "$CORE" ]; then
  SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
  REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
  for candidate in "$REPO_ROOT/../ai-native-core" "$REPO_ROOT/core" "$REPO_ROOT/../native-ai-engineering/ai-native-core"; do
    if [ -f "$candidate/contracts/manifest.yaml" ]; then
      CORE="$(cd "$candidate" && pwd)"
      break
    fi
  done
fi

if [ -z "$CORE" ] || [ ! -f "$CORE/contracts/manifest.yaml" ]; then
  echo "ERROR: Cannot find ai-native-core with contracts/manifest.yaml"
  echo "Usage: $0 [path-to-ai-native-core]"
  exit 1
fi

MANIFEST="$CORE/contracts/manifest.yaml"
echo "Core: $CORE"
echo "Manifest: $MANIFEST"
echo ""

# ── Extract all valid paths from manifest ────────────────────────────────────
valid_paths=$(grep '^\s*path:' "$MANIFEST" | sed 's/.*path:[[:space:]]*//' | tr -d '"' | tr -d "'")

# ── Find all implements references in current repo ───────────────────────────
errors=0
checked=0
broken_files=""

while IFS= read -r line; do
  [ -z "$line" ] && continue
  # Extract file path and the reference
  file=$(echo "$line" | cut -d: -f1)
  ref=$(echo "$line" | sed 's/.*ai-native-core\///' | tr -d '"' | tr -d "'" | xargs)

  checked=$((checked + 1))

  # Check if this path exists in manifest
  if ! echo "$valid_paths" | grep -qF "$ref"; then
    # Double-check: maybe the file exists on disk even if not in manifest
    if [ ! -f "$CORE/$ref" ]; then
      echo "BROKEN: $file"
      echo "  → ai-native-core/$ref"
      echo "  (not found in manifest or on disk)"
      echo ""
      errors=$((errors + 1))
      broken_files="$broken_files $file"
    else
      echo "WARN:   $file"
      echo "  → ai-native-core/$ref"
      echo "  (exists on disk but missing from manifest — run generate-manifest.sh)"
      echo ""
    fi
  fi
done < <(grep -r 'ai-native-core/' --include='*.md' --include='*.yaml' --include='*.yml' -h . 2>/dev/null \
  | grep -oP 'ai-native-core/contracts/\S+\.yaml' \
  | sort -u \
  | while read -r ref; do
      # Find which file contains this reference
      grep -rl "$ref" --include='*.md' --include='*.yaml' --include='*.yml' . 2>/dev/null | while read -r f; do
        echo "$f:$ref"
      done
    done)

echo "────────────────────────────────────"
echo "Checked: $checked references"
echo "Broken:  $errors"

if [ "$errors" -gt 0 ]; then
  echo ""
  echo "FAIL — $errors broken contract reference(s) found."
  echo "Fix the implements paths or regenerate the core manifest."
  exit 1
else
  echo ""
  echo "PASS — all contract references are valid."
  exit 0
fi
