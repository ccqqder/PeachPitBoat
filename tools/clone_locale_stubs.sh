#!/bin/bash
# clone_locale_stubs.sh — copy English content as stub for new locales.
#
# Each target language gets a copy of every *.en.md as *.<lang>.md
# (only when the target file does NOT already exist — never overwrites
# real translations). Pair with isStub=true in the locale's
# config/_default/languages.<lang>.toml so canonical/banner logic
# in baseof.html knows to flag the page as English placeholder.
#
# Usage:
#   ./tools/clone_locale_stubs.sh fr ko de es pt-BR vi id ru
#
# Re-run safely after adding new English content — script skips any
# *.<lang>.md that already exists.

set -euo pipefail

SRC_LANG=en
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONTENT_DIR="$ROOT/content"

if [ "$#" -eq 0 ]; then
  echo "usage: $0 <lang> [<lang> ...]" >&2
  echo "       e.g. $0 fr ko de es pt-BR vi id ru" >&2
  exit 1
fi

cd "$ROOT"

for lang in "$@"; do
  cfg="config/_default/languages.${lang}.toml"
  if [ ! -f "$cfg" ]; then
    echo "⚠ $cfg missing — declare the language first or stub URLs won't be generated" >&2
  fi

  created=0
  skipped=0
  while IFS= read -r f; do
    target="${f%.${SRC_LANG}.md}.${lang}.md"
    if [ ! -f "$target" ]; then
      cp "$f" "$target"
      # Inject isStub: true after the first --- line (frontmatter open).
      # baseof.html canonical override sees this and points the page's
      # canonical at the English equivalent at root, preventing Google
      # duplicate-content penalty until a real translation lands.
      sed -i '' '1a\
isStub: true
' "$target"
      created=$((created + 1))
    else
      skipped=$((skipped + 1))
    fi
  done < <(find "$CONTENT_DIR" -name "*.${SRC_LANG}.md")

  echo "[$lang] +${created} created · ${skipped} kept (real translations)"
done
