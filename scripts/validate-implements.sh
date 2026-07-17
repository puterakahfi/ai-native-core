#!/usr/bin/env bash
# Validate that all ai-native-core `implements` references in this repo
# point to contracts that actually exist and are version-compatible.
#
# Usage:
#   ./validate-implements.sh [path-to-core]
#
# Checks:
#   1. Path exists (contract file on disk or in manifest)
#   2. Version compatible (if adapter declares contract-version)
#
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

# ── Semver comparison helper ─────────────────────────────────────────────────
# Check if actual_version satisfies pin (^x.y.z or ~x.y)
check_semver() {
  local pin="$1"      # e.g. ^1.0.0 or ~0.1
  local actual="$2"   # e.g. 1.2.3

  # Strip quotes
  pin=$(echo "$pin" | tr -d '"' | tr -d "'")
  actual=$(echo "$actual" | tr -d '"' | tr -d "'")

  local prefix="${pin:0:1}"
  local pinver="${pin:1}"

  # Parse actual
  local a_major a_minor a_patch
  IFS='.' read -r a_major a_minor a_patch <<< "$actual"
  a_patch="${a_patch:-0}"

  # Parse pin version
  local p_major p_minor p_patch
  IFS='.' read -r p_major p_minor p_patch <<< "$pinver"
  p_patch="${p_patch:-0}"

  if [ "$prefix" = "^" ]; then
    # ^x.y.z: same major, >= minor.patch (for major > 0)
    # ^0.y.z: same major AND minor, >= patch
    if [ "$p_major" = "0" ]; then
      [ "$a_major" = "$p_major" ] && [ "$a_minor" = "$p_minor" ] && [ "$a_patch" -ge "$p_patch" ]
    else
      [ "$a_major" = "$p_major" ] && \
        ([ "$a_minor" -gt "$p_minor" ] || \
         ([ "$a_minor" = "$p_minor" ] && [ "$a_patch" -ge "$p_patch" ]))
    fi
  elif [ "$prefix" = "~" ]; then
    # ~x.y: same major.minor, any patch
    [ "$a_major" = "$p_major" ] && [ "$a_minor" = "$p_minor" ]
  else
    # Exact match
    [ "$actual" = "$pin" ]
  fi
}

# ── Build valid paths + version map from manifest ────────────────────────────
declare -A path_version_map
current_path=""
while IFS= read -r line; do
  if [[ "$line" =~ path:\ *(.*) ]]; then
    current_path="${BASH_REMATCH[1]}"
    current_path=$(echo "$current_path" | tr -d '"' | tr -d "'")
  elif [[ "$line" =~ version:\ *(.*) ]] && [ -n "$current_path" ]; then
    ver="${BASH_REMATCH[1]}"
    ver=$(echo "$ver" | tr -d '"' | tr -d "'")
    path_version_map["$current_path"]="$ver"
    current_path=""
  fi
done < "$MANIFEST"

# ── Scan all SKILL.md files ──────────────────────────────────────────────────
errors=0
warnings=0
checked=0

find . -name 'SKILL.md' -not -path '*/.git/*' | sort | while IFS= read -r skillfile; do
  # Extract implements path
  impl=$(grep -oP 'ai-native-skills\.implements:\s*ai-native-core/\K\S+' "$skillfile" 2>/dev/null || true)
  [ -z "$impl" ] && continue

  checked=$((checked + 1))

  # Check 1: Path exists
  if [ ! -f "$CORE/$impl" ]; then
    if [ -z "${path_version_map[$impl]+x}" ]; then
      echo "BROKEN: $skillfile"
      echo "  → ai-native-core/$impl"
      echo "  (not found in manifest or on disk)"
      echo ""
      errors=$((errors + 1))
      continue
    fi
  fi

  # Check 2: Version compatibility
  pinned=$(grep -oP 'ai-native-skills\.contract-version:\s*\K\S+' "$skillfile" 2>/dev/null | tr -d '"' | tr -d "'" || true)
  if [ -n "$pinned" ]; then
    actual_ver="${path_version_map[$impl]:-}"
    if [ -z "$actual_ver" ]; then
      # Try reading from file directly
      actual_ver=$(grep -m1 'version:' "$CORE/$impl" 2>/dev/null | sed 's/.*version:[[:space:]]*//' | tr -d '"' | tr -d "'" || true)
    fi
    if [ -n "$actual_ver" ]; then
      if ! check_semver "$pinned" "$actual_ver"; then
        echo "VERSION MISMATCH: $skillfile"
        echo "  → ai-native-core/$impl"
        echo "  pinned: $pinned, actual: $actual_ver"
        echo ""
        errors=$((errors + 1))
      fi
    fi
  else
    echo "WARN: $skillfile"
    echo "  → no contract-version pinned (add ai-native-skills.contract-version)"
    echo ""
    warnings=$((warnings + 1))
  fi
done

# Re-count since while loop runs in subshell
errors=$(find . -name 'SKILL.md' -not -path '*/.git/*' -exec grep -l 'ai-native-skills.implements' {} \; | while IFS= read -r skillfile; do
  impl=$(grep -oP 'ai-native-skills\.implements:\s*ai-native-core/\K\S+' "$skillfile" 2>/dev/null || true)
  [ -z "$impl" ] && continue

  # Path check
  if [ ! -f "$CORE/$impl" ] && [ -z "${path_version_map[$impl]+x}" ]; then
    echo "BROKEN"
    continue
  fi

  # Version check
  pinned=$(grep -oP 'ai-native-skills\.contract-version:\s*\K\S+' "$skillfile" 2>/dev/null | tr -d '"' | tr -d "'" || true)
  if [ -n "$pinned" ]; then
    actual_ver="${path_version_map[$impl]:-}"
    [ -z "$actual_ver" ] && actual_ver=$(grep -m1 'version:' "$CORE/$impl" 2>/dev/null | sed 's/.*version:[[:space:]]*//' | tr -d '"' | tr -d "'" || true)
    if [ -n "$actual_ver" ] && ! check_semver "$pinned" "$actual_ver"; then
      echo "VERSION"
    fi
  fi
done | wc -l)

checked=$(find . -name 'SKILL.md' -not -path '*/.git/*' -exec grep -l 'ai-native-skills.implements' {} \; | wc -l)

echo "────────────────────────────────────"
echo "Checked: $checked adapter skills"
echo "Errors:  $errors"
echo ""

if [ "$errors" -gt 0 ]; then
  echo "FAIL — $errors broken or incompatible contract reference(s)."
  exit 1
else
  echo "PASS — all contract references are valid and version-compatible."
  exit 0
fi
