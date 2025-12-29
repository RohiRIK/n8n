#!/bin/bash
#
# N8N Workflow Auto-Backup Script
# Fetches workflows from local n8n instance and commits changes to git
#
# Usage:
#   ./auto_backup.sh           # Run backup with default settings
#   ./auto_backup.sh --dry-run # Preview changes without committing
#

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_FILE="$REPO_ROOT/auto_backup.log"
N8N_API_URL="${N8N_API_URL:-http://localhost:5678}"
N8N_API_TOKEN="${N8N_API_TOKEN:-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4OWM4NjI5OC1jOTA2LTQ2YjQtOWFlZC0wYzExYjZhYThjNjEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzY2OTk1Nzg2fQ.Pnf4Ae0hJA-cfW2MvtF03RTpFMfKveYyLen4cigSv8A}"
DRY_RUN=false

# Parse arguments
for arg in "$@"; do
  case $arg in
    --dry-run)
      DRY_RUN=true
      shift
      ;;
  esac
done

# Logging function
log() {
  local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
  echo "[$timestamp] $*" | tee -a "$LOG_FILE"
}

# Error handler
error_exit() {
  log "ERROR: $1"
  exit 1
}

# Check if n8n is running
check_n8n() {
  log "Checking n8n connectivity..."
  if ! curl -sf "${N8N_API_URL}/healthz" > /dev/null 2>&1; then
    error_exit "n8n is not responding at ${N8N_API_URL}. Is it running?"
  fi
  log "n8n is running and accessible"
}

# Fetch workflows
fetch_workflows() {
  log "Fetching workflows from n8n..."
  cd "$REPO_ROOT"

  export N8N_API_URL
  export N8N_API_TOKEN

  if python3 scripts/fetch_n8n_workflows.py >> "$LOG_FILE" 2>&1; then
    log "Workflows fetched successfully"
    return 0
  else
    error_exit "Failed to fetch workflows"
  fi
}

# Update catalog
update_catalog() {
  log "Updating workflow catalog..."
  cd "$REPO_ROOT"

  if python3 scripts/catalog_workflows.py >> "$LOG_FILE" 2>&1; then
    log "Catalog updated successfully"
    return 0
  else
    log "WARNING: Failed to update catalog (non-fatal)"
    return 0
  fi
}

# Check for changes
check_changes() {
  cd "$REPO_ROOT"

  # Check if there are any changes
  git add workflow_backups/ docs/ 2>/dev/null || true

  if git diff --staged --quiet; then
    log "No changes detected"
    return 1
  else
    local changed_count=$(git diff --staged --name-only | wc -l)
    log "Changes detected: $changed_count files modified"
    return 0
  fi
}

# Commit and push changes
commit_changes() {
  cd "$REPO_ROOT"

  local changed_count=$(git diff --staged --name-only | wc -l)
  local changed_files=$(git diff --staged --name-only | head -20)

  log "Creating commit for $changed_count changed file(s)"

  # Create commit message
  local commit_msg="Auto-backup: Updated $changed_count workflow(s)

Changed workflows:
$changed_files

Triggered by: local cron job
Timestamp: $(date -u '+%Y-%m-%d %H:%M:%S UTC')
Hostname: $(hostname)"

  if $DRY_RUN; then
    log "[DRY-RUN] Would commit with message:"
    echo "$commit_msg"
    log "[DRY-RUN] Skipping commit and push"
    git reset HEAD workflow_backups/ docs/ 2>/dev/null || true
    return 0
  fi

  # Commit changes
  if git commit -m "$commit_msg"; then
    log "Commit created successfully"
  else
    error_exit "Failed to create commit"
  fi

  # Push to remote
  log "Pushing changes to remote repository..."
  if git push origin main; then
    log "Changes pushed successfully"
  else
    error_exit "Failed to push changes"
  fi
}

# Main execution
main() {
  log "=== N8N Auto-Backup Started ==="
  log "Repository: $REPO_ROOT"
  log "n8n URL: $N8N_API_URL"
  log "Dry-run: $DRY_RUN"

  # Check n8n connectivity
  check_n8n

  # Fetch workflows
  fetch_workflows

  # Update catalog
  update_catalog

  # Check for changes
  if check_changes; then
    # Commit and push
    commit_changes
    log "=== Backup completed successfully ==="
  else
    log "=== Backup completed (no changes) ==="
  fi
}

# Run main function
main "$@"
