#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKUPS="$ROOT/workflow_backups"
DEV="$ROOT/development"
PROJ="$ROOT/projects"
ARCH="$ROOT/archived"

# Category directories
BACKUP_BACKUP="$BACKUPS/backup"
BACKUP_BLOGGING="$BACKUPS/blogging"
BACKUP_SECURITY="$BACKUPS/security"
BACKUP_NOTION="$BACKUPS/notion"
BACKUP_ALERTS="$BACKUPS/alerts"
BACKUP_AGENTS="$BACKUPS/agents"
BACKUP_AUTH="$BACKUPS/authentication"

usage() {
  cat <<USAGE
Usage:
  $(basename "$0") import-backups              # Copy .json from workflow_backups/ -> development/imported/ (read-only source)
  $(basename "$0") import-from-category <cat>  # Import .json from specific category to development/imported/<category>/
  $(basename "$0") promote-dev <file> <project>  # Promote a dev JSON to projects/<project>/
  $(basename "$0") list                        # Summarize counts by folder
  $(basename "$0") list-categories             # List workflows by category
USAGE
}

cmd="${1:-}"
case "$cmd" in
  import-backups)
    mkdir -p "$DEV/imported"
    if [ ! -d "$BACKUPS" ]; then
      echo "Backups folder not found at: $BACKUPS" >&2
      exit 1
    fi
    rsync -av --include '*/' --include '*.json' --exclude '*' "$BACKUPS"/ "$DEV/imported"/
    echo "Imported backups into $DEV/imported (no changes to workflow_backups/)."
    ;;
  promote-dev)
    src="${2:-}"; project="${3:-}"
    [ -n "$src" ] && [ -n "$project" ] || { usage; exit 1; }
    [ -f "$src" ] || { echo "File not found: $src" >&2; exit 1; }
    dest="$PROJ/$project"
    mkdir -p "$dest"
    cp -v "$src" "$dest/"
    echo "Promoted $(basename "$src") to $dest"
    ;;
  import-from-category)
    category="${2:-}"
    [ -n "$category" ] || { usage; exit 1; }
    src="$BACKUPS/$category"
    [ -d "$src" ] || { echo "Category not found: $category" >&2; exit 1; }
    dest="$DEV/imported/$category"
    mkdir -p "$dest"
    rsync -av --include '*/' --include '*.json' --exclude '*' "$src"/ "$dest"/
    echo "Imported $category workflows into $dest (no changes to workflow_backups/)."
    ;;
  list)
    for d in "workflow_backups" "development" "projects" "archived"; do
      path="$ROOT/$d"
      if [ -d "$path" ]; then
        count=$(find "$path" -type f -name '*.json' | wc -l | tr -d ' ')
        echo "$d: $count JSON files"
      else
        echo "$d: (missing)"
      fi
    done
    ;;
  list-categories)
    if [ ! -d "$BACKUPS" ]; then
      echo "Backups folder not found at: $BACKUPS" >&2
      exit 1
    fi
    echo "Workflows by category:"
    for category in backup blogging security notion alerts agents authentication; do
      cat_path="$BACKUPS/$category"
      if [ -d "$cat_path" ]; then
        count=$(find "$cat_path" -type f -name '*.json' | wc -l | tr -d ' ')
        echo "  $category: $count workflows"
      fi
    done
    ;;
  *)
    usage
    exit 1
    ;;
esac