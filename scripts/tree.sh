#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
echo "Repository tree (top-level):"
find . -maxdepth 2 -mindepth 1 -not -path "*/.*" -print | sed 's|^./||' | sort