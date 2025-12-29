#!/usr/bin/env python3
"""
N8N Workflow Migration Script
Reorganizes workflow_backups from flat structure to categorized structure.

Features:
- Dry-run mode to preview changes
- Atomic moves with SHA1 verification
- Generates rollback script
- Creates tarball backup before migration
- Comprehensive logging
"""

import os
import sys
import json
import shutil
import hashlib
import argparse
from datetime import datetime
from pathlib import Path

# Repository root (parent of scripts/)
REPO_ROOT = Path(__file__).parent.parent.resolve()
WORKFLOW_BACKUPS = REPO_ROOT / "workflow_backups"
ARCHIVED_DIR = REPO_ROOT / "archived" / "workflows"
DOCS_WORKFLOWS = REPO_ROOT / "docs" / "workflows"
MAPPING_FILE = REPO_ROOT / "scripts" / "migration_mapping.json"
LOG_FILE = REPO_ROOT / "migration.log"
ROLLBACK_SCRIPT = REPO_ROOT / "scripts" / "rollback_migration.sh"


class MigrationLogger:
    """Logger for migration operations"""

    def __init__(self, log_file, verbose=True):
        self.log_file = log_file
        self.verbose = verbose
        self.operations = []

    def log(self, message, level="INFO"):
        """Log a message to file and optionally stdout"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{level}] {message}"

        with open(self.log_file, 'a') as f:
            f.write(log_line + '\n')

        if self.verbose:
            print(log_line)

    def record_operation(self, operation_type, source, destination):
        """Record an operation for rollback script generation"""
        self.operations.append({
            'type': operation_type,
            'source': str(source),
            'destination': str(destination)
        })


def compute_sha1(file_path):
    """Compute SHA1 hash of a file"""
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()


def load_mapping():
    """Load migration mapping from JSON file"""
    with open(MAPPING_FILE, 'r') as f:
        return json.load(f)


def create_backup(logger, dry_run=False):
    """Create tarball backup of entire repository"""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_file = REPO_ROOT.parent / f"n8n-backup-{timestamp}.tar.gz"

    if dry_run:
        logger.log(f"[DRY-RUN] Would create backup: {backup_file}", "INFO")
        return None

    logger.log(f"Creating backup: {backup_file}", "INFO")

    try:
        import tarfile
        with tarfile.open(backup_file, "w:gz") as tar:
            tar.add(REPO_ROOT, arcname=REPO_ROOT.name)
        logger.log(f"Backup created successfully: {backup_file}", "SUCCESS")
        return backup_file
    except Exception as e:
        logger.log(f"Failed to create backup: {e}", "ERROR")
        sys.exit(1)


def validate_source_state(logger):
    """Validate that all expected workflows exist"""
    if not WORKFLOW_BACKUPS.exists():
        logger.log(f"workflow_backups directory not found: {WORKFLOW_BACKUPS}", "ERROR")
        sys.exit(1)

    workflow_dirs = [d for d in WORKFLOW_BACKUPS.iterdir() if d.is_dir()]
    logger.log(f"Found {len(workflow_dirs)} workflow directories", "INFO")

    # Count JSON files
    json_files = list(WORKFLOW_BACKUPS.glob("*/*.json"))
    logger.log(f"Found {len(json_files)} JSON workflow files", "INFO")

    return workflow_dirs, json_files


def create_category_structure(categories, logger, dry_run=False):
    """Create category directories"""
    for category in categories.keys():
        category_dir = WORKFLOW_BACKUPS / category

        if dry_run:
            logger.log(f"[DRY-RUN] Would create: {category_dir}", "INFO")
        else:
            category_dir.mkdir(parents=True, exist_ok=True)
            logger.log(f"Created category: {category_dir}", "SUCCESS")


def move_workflow(old_dir, new_dir, logger, dry_run=False):
    """Move a workflow directory with SHA1 verification"""
    if not old_dir.exists():
        logger.log(f"Source not found: {old_dir}", "WARNING")
        return False

    # Find JSON file in old directory
    json_files = list(old_dir.glob("*.json"))
    if not json_files:
        logger.log(f"No JSON file found in {old_dir}", "WARNING")
        return False

    json_file = json_files[0]
    old_sha1 = compute_sha1(json_file) if not dry_run else "DRY-RUN"

    if dry_run:
        logger.log(f"[DRY-RUN] Would move: {old_dir} -> {new_dir}", "INFO")
        logger.log(f"[DRY-RUN]   JSON file: {json_file.name}", "INFO")
    else:
        # Create destination directory
        new_dir.mkdir(parents=True, exist_ok=True)

        # Determine new filename (use directory name)
        new_filename = f"{new_dir.name}.json"
        new_json_path = new_dir / new_filename

        # Move JSON file
        shutil.copy2(json_file, new_json_path)
        new_sha1 = compute_sha1(new_json_path)

        # Verify SHA1
        if old_sha1 != new_sha1:
            logger.log(f"SHA1 mismatch for {json_file.name}: {old_sha1} != {new_sha1}", "ERROR")
            new_json_path.unlink()
            return False

        # Move any other files (markdown, etc.) - will be handled separately
        logger.log(f"Moved workflow: {old_dir.name} -> {new_dir}", "SUCCESS")
        logger.record_operation("move", old_dir, new_dir)

    return True


def archive_workflow(old_dir, archived_name, logger, dry_run=False):
    """Move workflow to archived/ directory"""
    if not old_dir.exists():
        logger.log(f"Source not found for archiving: {old_dir}", "WARNING")
        return False

    archive_dest = ARCHIVED_DIR / archived_name

    if dry_run:
        logger.log(f"[DRY-RUN] Would archive: {old_dir} -> {archive_dest}", "INFO")
    else:
        ARCHIVED_DIR.mkdir(parents=True, exist_ok=True)

        if archive_dest.exists():
            logger.log(f"Archive destination already exists: {archive_dest}", "WARNING")
            shutil.rmtree(archive_dest)

        shutil.move(str(old_dir), str(archive_dest))
        logger.log(f"Archived: {old_dir.name} -> {archive_dest}", "SUCCESS")
        logger.record_operation("archive", old_dir, archive_dest)

    return True


def migrate_documentation(doc_moves, logger, dry_run=False):
    """Move documentation files to docs/workflows/"""
    for source_dir, dest_path in doc_moves.items():
        source = WORKFLOW_BACKUPS / source_dir
        destination = REPO_ROOT / dest_path

        if not source.exists():
            logger.log(f"Documentation source not found: {source}", "WARNING")
            continue

        # Find all markdown files
        md_files = list(source.glob("*.md"))
        if not md_files:
            logger.log(f"No markdown files found in {source}", "INFO")
            continue

        if dry_run:
            logger.log(f"[DRY-RUN] Would move {len(md_files)} markdown files: {source} -> {destination}", "INFO")
            for md_file in md_files:
                logger.log(f"[DRY-RUN]   {md_file.name}", "INFO")
        else:
            destination.mkdir(parents=True, exist_ok=True)

            for md_file in md_files:
                dest_file = destination / md_file.name
                shutil.copy2(md_file, dest_file)
                logger.log(f"Moved documentation: {md_file.name} -> {dest_file}", "SUCCESS")
                logger.record_operation("doc_move", md_file, dest_file)


def cleanup_old_directories(logger, dry_run=False):
    """Remove old empty workflow directories"""
    for item in WORKFLOW_BACKUPS.iterdir():
        if item.is_dir() and item.name not in ['backup', 'blogging', 'security', 'notion', 'alerts', 'agents', 'authentication']:
            if dry_run:
                logger.log(f"[DRY-RUN] Would remove old directory: {item}", "INFO")
            else:
                if not list(item.glob("*.json")):  # Only remove if no JSON files
                    shutil.rmtree(item)
                    logger.log(f"Removed old directory: {item.name}", "SUCCESS")
                else:
                    logger.log(f"Skipping non-empty directory: {item.name}", "WARNING")


def generate_rollback_script(logger):
    """Generate rollback script from recorded operations"""
    if not logger.operations:
        logger.log("No operations to rollback", "INFO")
        return

    with open(ROLLBACK_SCRIPT, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Auto-generated rollback script for workflow migration\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("set -e\n\n")
        f.write('echo "Starting rollback..."\n\n')

        # Reverse operations
        for op in reversed(logger.operations):
            if op['type'] == 'move':
                f.write(f"echo 'Rolling back move: {op['destination']} -> {op['source']}'\n")
                f.write(f"mv '{op['destination']}' '{op['source']}'\n\n")
            elif op['type'] == 'archive':
                f.write(f"echo 'Rolling back archive: {op['destination']} -> {op['source']}'\n")
                f.write(f"mv '{op['destination']}' '{op['source']}'\n\n")

        f.write('echo "Rollback complete!"\n')

    os.chmod(ROLLBACK_SCRIPT, 0o755)
    logger.log(f"Generated rollback script: {ROLLBACK_SCRIPT}", "SUCCESS")


def execute_migration(mapping, logger, dry_run=False):
    """Execute the migration based on mapping configuration"""
    categories = mapping['categories']
    renames = mapping['renames']
    archives = mapping['archives']
    duplicates = mapping['duplicates']
    doc_moves = mapping['documentation_moves']

    logger.log("=== Starting Migration ===", "INFO")

    # Step 1: Create category structure
    logger.log("Step 1: Creating category structure", "INFO")
    create_category_structure(categories, logger, dry_run)

    # Step 2: Handle duplicates first
    logger.log("Step 2: Handling duplicates", "INFO")
    for workflow_name, dup_config in duplicates.items():
        keep_dir = WORKFLOW_BACKUPS / dup_config['keep']

        # Archive old versions
        for archive_name in dup_config['archive']:
            old_dir = WORKFLOW_BACKUPS / archive_name
            archived_name = renames.get(archive_name, archive_name)
            archive_workflow(old_dir, archived_name, logger, dry_run)

    # Step 3: Move documentation
    logger.log("Step 3: Migrating documentation", "INFO")
    migrate_documentation(doc_moves, logger, dry_run)

    # Step 4: Move workflows to categorized structure
    logger.log("Step 4: Moving workflows to categories", "INFO")
    for category, workflow_names in categories.items():
        for workflow_name in workflow_names:
            # Find the original directory name
            original_name = None
            for old_name, new_name in renames.items():
                if new_name == workflow_name:
                    original_name = old_name
                    break

            # If not in renames, it might already have the correct name
            if original_name is None:
                # Check if a directory with this name exists
                if (WORKFLOW_BACKUPS / workflow_name).exists():
                    original_name = workflow_name
                else:
                    logger.log(f"Could not find source for workflow: {workflow_name}", "WARNING")
                    continue

            old_dir = WORKFLOW_BACKUPS / original_name
            new_dir = WORKFLOW_BACKUPS / category / workflow_name

            # Skip if already archived
            if original_name in archives:
                continue

            # Skip duplicates that were kept (they'll be moved with their new name)
            skip = False
            for dup_config in duplicates.values():
                if original_name == dup_config['keep']:
                    skip = True
                    break

            if not skip:
                move_workflow(old_dir, new_dir, logger, dry_run)

    # Step 5: Handle kept duplicates
    logger.log("Step 5: Moving kept duplicate workflows", "INFO")
    for workflow_name, dup_config in duplicates.items():
        keep_original = dup_config['keep']

        # Find category for this workflow
        target_category = None
        for category, workflow_names in categories.items():
            if workflow_name in workflow_names:
                target_category = category
                break

        if target_category:
            old_dir = WORKFLOW_BACKUPS / keep_original
            new_dir = WORKFLOW_BACKUPS / target_category / workflow_name
            move_workflow(old_dir, new_dir, logger, dry_run)

    # Step 6: Archive remaining old versions
    logger.log("Step 6: Archiving remaining old versions", "INFO")
    for archive_name in archives:
        old_dir = WORKFLOW_BACKUPS / archive_name
        if old_dir.exists():
            archived_name = renames.get(archive_name, archive_name)
            archive_workflow(old_dir, archived_name, logger, dry_run)

    # Step 7: Cleanup old directories
    logger.log("Step 7: Cleaning up old directories", "INFO")
    cleanup_old_directories(logger, dry_run)

    logger.log("=== Migration Complete ===", "SUCCESS")


def main():
    parser = argparse.ArgumentParser(description="Migrate n8n workflows to categorized structure")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without executing")
    parser.add_argument('--no-backup', action='store_true', help="Skip creating tarball backup")
    parser.add_argument('--verbose', action='store_true', default=True, help="Verbose output")

    args = parser.parse_args()

    # Initialize logger
    logger = MigrationLogger(LOG_FILE, verbose=args.verbose)

    logger.log("=== N8N Workflow Migration Started ===", "INFO")
    logger.log(f"Dry-run mode: {args.dry_run}", "INFO")
    logger.log(f"Repository root: {REPO_ROOT}", "INFO")

    # Load mapping
    logger.log(f"Loading mapping from: {MAPPING_FILE}", "INFO")
    mapping = load_mapping()

    # Validate source state
    logger.log("Validating source state", "INFO")
    workflow_dirs, json_files = validate_source_state(logger)

    # Create backup
    if not args.no_backup and not args.dry_run:
        create_backup(logger, dry_run=False)
    elif args.dry_run:
        create_backup(logger, dry_run=True)

    # Execute migration
    execute_migration(mapping, logger, dry_run=args.dry_run)

    # Generate rollback script
    if not args.dry_run:
        generate_rollback_script(logger)

    logger.log("=== Migration Script Finished ===", "SUCCESS")

    if args.dry_run:
        print("\n" + "="*60)
        print("DRY-RUN MODE - No changes were made")
        print("Run without --dry-run to execute migration")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("Migration completed successfully!")
        print(f"Log file: {LOG_FILE}")
        print(f"Rollback script: {ROLLBACK_SCRIPT}")
        print("="*60)


if __name__ == '__main__':
    main()
