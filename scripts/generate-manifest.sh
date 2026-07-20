#!/usr/bin/env bash
# Generate contracts/manifest.yaml from actual contract files.
# Run from repo root: ./scripts/generate-manifest.sh
set -euo pipefail

CORE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$CORE_ROOT/contracts/manifest.yaml"
CONTRACTS_DIR="$CORE_ROOT/contracts"
TEMP_MANIFEST=$(mktemp)
TEMP_EXISTING_NORMALIZED=$(mktemp)
TEMP_GENERATED_NORMALIZED=$(mktemp)

cleanup() {
  rm -f "$TEMP_MANIFEST" "$TEMP_EXISTING_NORMALIZED" "$TEMP_GENERATED_NORMALIZED"
}
trap cleanup EXIT

existing_timestamp=""
if [ -f "$MANIFEST" ]; then
  existing_timestamp=$(sed -n 's/^generated_at: "\(.*\)"$/\1/p' "$MANIFEST" | head -n1)
fi

timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > "$TEMP_MANIFEST" <<HEADER
version: "1.0.0"
generated_at: "$timestamp"
description: "Auto-generated contract manifest. Regenerate with: scripts/generate-manifest.sh"
total_contracts: PLACEHOLDER
contracts:
  skills:
HEADER

total=0

# Skills — grouped by category
for catdir in "$CONTRACTS_DIR"/skills/*/; do
  [ -d "$catdir" ] || continue
  cat=$(basename "$catdir")
  has_files=false
  for f in "$catdir"*.contract.yaml; do
    [ -f "$f" ] || continue
    has_files=true
    break
  done
  $has_files || continue

  echo "    $cat:" >> "$TEMP_MANIFEST"
  for f in "$catdir"*.contract.yaml; do
    [ -f "$f" ] || continue
    name=$(basename "$f" .contract.yaml)
    relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
    sha=$(sha256sum "$f" | cut -c1-16)
    version=$(grep -m1 'version:' "$f" | sed 's/.*version:[[:space:]]*//' | tr -d '"' | tr -d "'")
    echo "      - id: $name" >> "$TEMP_MANIFEST"
    echo "        path: $relpath" >> "$TEMP_MANIFEST"
    echo "        version: \"${version:-0.0.0}\"" >> "$TEMP_MANIFEST"
    echo "        sha256: $sha" >> "$TEMP_MANIFEST"
    total=$((total + 1))
  done
done

# Workflows
echo "  workflows:" >> "$TEMP_MANIFEST"
for f in "$CONTRACTS_DIR"/workflows/*.contract.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .contract.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$TEMP_MANIFEST"
  echo "      path: $relpath" >> "$TEMP_MANIFEST"
  echo "      sha256: $sha" >> "$TEMP_MANIFEST"
  total=$((total + 1))
done

# Tests
echo "  tests:" >> "$TEMP_MANIFEST"
for f in "$CONTRACTS_DIR"/tests/*.test.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .test.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$TEMP_MANIFEST"
  echo "      path: $relpath" >> "$TEMP_MANIFEST"
  echo "      sha256: $sha" >> "$TEMP_MANIFEST"
  total=$((total + 1))
done

# Runtime
echo "  runtime:" >> "$TEMP_MANIFEST"
for f in "$CONTRACTS_DIR"/runtime/*.contract.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .contract.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$TEMP_MANIFEST"
  echo "      path: $relpath" >> "$TEMP_MANIFEST"
  echo "      sha256: $sha" >> "$TEMP_MANIFEST"
  total=$((total + 1))
done

sed -i "s/total_contracts: PLACEHOLDER/total_contracts: $total/" "$TEMP_MANIFEST"

# Preserve generated_at when the generated registry is otherwise unchanged.
# This keeps repeated generation idempotent while still refreshing the timestamp
# for real ID, path, version, checksum, category, or count changes.
if [ -f "$MANIFEST" ] && [ -n "$existing_timestamp" ]; then
  sed 's/^generated_at: .*/generated_at: "<normalized>"/' "$MANIFEST" > "$TEMP_EXISTING_NORMALIZED"
  sed 's/^generated_at: .*/generated_at: "<normalized>"/' "$TEMP_MANIFEST" > "$TEMP_GENERATED_NORMALIZED"
  if cmp -s "$TEMP_EXISTING_NORMALIZED" "$TEMP_GENERATED_NORMALIZED"; then
    sed -i "s|^generated_at: .*|generated_at: \"$existing_timestamp\"|" "$TEMP_MANIFEST"
  fi
fi

mv "$TEMP_MANIFEST" "$MANIFEST"

echo "✓ Generated $MANIFEST ($total contracts)"
