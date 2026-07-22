#!/usr/bin/env bash
# Validate ai-native-skills implements references through the schema-aware manifest
# and active compatibility path aliases.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/validate-implements.py" "$@"
