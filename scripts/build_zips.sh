#!/usr/bin/env bash
# Build one upload-ready zip per skill, plus an all-skills pack, into dist/.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name=$(basename "$dir")
  (cd skills && zip -qr "../dist/${name}.zip" "$name")
done
(cd skills && zip -qr ../dist/applyready-all-skills.zip .)
echo "Built $(ls dist | wc -l) zips in dist/"
