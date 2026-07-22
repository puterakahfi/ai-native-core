#!/usr/bin/env bash
# Generate contracts/manifest.yaml from declared contract schema identities.
# Run from repo root: ./scripts/generate-manifest.sh
set -euo pipefail

CORE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$CORE_ROOT/scripts/generate-manifest.py"
