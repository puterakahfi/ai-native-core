#!/usr/bin/env bash
# Generate contracts/manifest.yaml from actual contract files.
# Run from repo root: ./scripts/generate-manifest.sh
set -euo pipefail

CORE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$CORE_ROOT/contracts/manifest.yaml"
CONTRACTS_DIR="$CORE_ROOT/contracts"

timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > "$MANIFEST" <<HEADER
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

  echo "    $cat:" >> "$MANIFEST"
  for f in "$catdir"*.contract.yaml; do
    [ -f "$f" ] || continue
    name=$(basename "$f" .contract.yaml)
    relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
    sha=$(sha256sum "$f" | cut -c1-16)
    version=$(grep -m1 'version:' "$f" | sed 's/.*version:[[:space:]]*//' | tr -d '"' | tr -d "'")
    echo "      - id: $name" >> "$MANIFEST"
    echo "        path: $relpath" >> "$MANIFEST"
    echo "        version: \"${version:-0.0.0}\"" >> "$MANIFEST"
    echo "        sha256: $sha" >> "$MANIFEST"
    total=$((total + 1))
  done
done

# Workflows
echo "  workflows:" >> "$MANIFEST"
for f in "$CONTRACTS_DIR"/workflows/*.contract.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .contract.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$MANIFEST"
  echo "      path: $relpath" >> "$MANIFEST"
  echo "      sha256: $sha" >> "$MANIFEST"
  total=$((total + 1))
done

# Tests
echo "  tests:" >> "$MANIFEST"
for f in "$CONTRACTS_DIR"/tests/*.test.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .test.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$MANIFEST"
  echo "      path: $relpath" >> "$MANIFEST"
  echo "      sha256: $sha" >> "$MANIFEST"
  total=$((total + 1))
done

# Runtime
echo "  runtime:" >> "$MANIFEST"
for f in "$CONTRACTS_DIR"/runtime/*.contract.yaml; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .contract.yaml)
  relpath=$(realpath --relative-to="$CORE_ROOT" "$f")
  sha=$(sha256sum "$f" | cut -c1-16)
  echo "    - id: $name" >> "$MANIFEST"
  echo "      path: $relpath" >> "$MANIFEST"
  echo "      sha256: $sha" >> "$MANIFEST"
  total=$((total + 1))
done

# Patch total
sed -i "s/total_contracts: PLACEHOLDER/total_contracts: $total/" "$MANIFEST"

echo "✓ Generated $MANIFEST ($total contracts)"
