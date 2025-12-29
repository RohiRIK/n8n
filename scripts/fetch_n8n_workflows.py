#!/usr/bin/env python3
"""
N8N Workflow Fetcher
Fetches workflows from n8n API and saves them to categorized structure.

Uses environment variables:
- N8N_API_URL: Full URL to n8n instance (e.g., https://n8n.homelab.example.com)
- N8N_API_TOKEN: n8n API authentication token

Features:
- Content-based change detection using SHA256 hashing
- Auto-categorization based on workflow names
- Only writes changed workflows to reduce git noise
- Category override support via category_overrides.json
"""

import os
import sys
import json
import hashlib
import requests
from pathlib import Path
from datetime import datetime


# Repository root (parent of scripts/)
REPO_ROOT = Path(__file__).parent.parent.resolve()
WORKFLOW_BACKUPS = REPO_ROOT / "workflow_backups"
CATEGORY_OVERRIDES_FILE = REPO_ROOT / "scripts" / "category_overrides.json"


def slugify(text):
    """Convert text to snake_case slug"""
    import re

    # Convert to lowercase
    text = text.lower()

    # Replace spaces and hyphens with underscores
    text = re.sub(r'[\s\-]+', '_', text)

    # Remove non-alphanumeric characters (except underscores)
    text = re.sub(r'[^a-z0-9_]', '', text)

    # Remove duplicate underscores
    text = re.sub(r'_+', '_', text)

    # Strip leading/trailing underscores
    text = text.strip('_')

    return text


def categorize_workflow(workflow_name, overrides=None):
    """Auto-categorize workflow based on name"""
    if overrides and workflow_name in overrides:
        return overrides[workflow_name]

    name_lower = workflow_name.lower()

    if 'backup' in name_lower:
        return 'backup'
    elif any(x in name_lower for x in ['blog', 'youtube', 'web_clips', 'web clips', 'content']):
        return 'blogging'
    elif any(x in name_lower for x in ['security', 'phish', 'break_glass', 'break glass', 'ticket', 'gemini']):
        return 'security'
    elif 'notion' in name_lower:
        return 'notion'
    elif any(x in name_lower for x in ['alert', 'webhook']):
        return 'alerts'
    elif any(x in name_lower for x in ['agent', 'searxng', 'firecrawl', 'vector']):
        return 'agents'
    elif 'auth' in name_lower or 'graph' in name_lower:
        return 'authentication'
    else:
        return 'utilities'


def compute_workflow_hash(workflow_data):
    """Compute SHA256 hash of workflow content (excluding volatile metadata)"""
    # Extract only stable fields for hashing
    stable_data = {
        'name': workflow_data.get('name', ''),
        'nodes': workflow_data.get('nodes', []),
        'connections': workflow_data.get('connections', {}),
        'settings': workflow_data.get('settings', {}),
    }

    # Sort keys for deterministic hashing
    content = json.dumps(stable_data, sort_keys=True)
    return hashlib.sha256(content.encode()).hexdigest()


def load_existing_workflow(file_path):
    """Load existing workflow and compute its hash"""
    if not file_path.exists():
        return None, None

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data, compute_workflow_hash(data)
    except Exception as e:
        print(f"Error loading existing workflow {file_path}: {e}", file=sys.stderr)
        return None, None


def fetch_workflows_from_n8n(api_url, api_token):
    """Fetch all workflows from n8n API"""
    headers = {'X-N8N-API-KEY': api_token}

    try:
        response = requests.get(f"{api_url}/api/v1/workflows", headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()

        if 'data' in data:
            return data['data']
        else:
            print(f"Unexpected API response format: {data}", file=sys.stderr)
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching workflows from n8n API: {e}", file=sys.stderr)
        sys.exit(1)


def load_category_overrides():
    """Load category overrides from JSON file"""
    if not CATEGORY_OVERRIDES_FILE.exists():
        return {}

    try:
        with open(CATEGORY_OVERRIDES_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load category overrides: {e}", file=sys.stderr)
        return {}


def sync_workflows():
    """Main sync function"""
    # Get environment variables
    api_url = os.environ.get('N8N_API_URL')
    api_token = os.environ.get('N8N_API_TOKEN')

    if not api_url or not api_token:
        print("Error: N8N_API_URL and N8N_API_TOKEN environment variables must be set", file=sys.stderr)
        sys.exit(1)

    # Remove trailing slash from API URL
    api_url = api_url.rstrip('/')

    print(f"Fetching workflows from: {api_url}")

    # Load category overrides
    category_overrides = load_category_overrides()
    if category_overrides:
        print(f"Loaded {len(category_overrides)} category overrides")

    # Fetch workflows
    workflows = fetch_workflows_from_n8n(api_url, api_token)
    print(f"Fetched {len(workflows)} workflows from n8n")

    if not workflows:
        print("No workflows found")
        return

    # Track statistics
    new_count = 0
    updated_count = 0
    unchanged_count = 0

    # Process each workflow
    for workflow in workflows:
        workflow_name = workflow.get('name', 'unnamed_workflow')

        # Generate snake_case slug
        workflow_slug = slugify(workflow_name)

        # Determine category
        category = categorize_workflow(workflow_name, category_overrides)

        # Determine file path
        workflow_dir = WORKFLOW_BACKUPS / category / workflow_slug
        workflow_file = workflow_dir / f"{workflow_slug}.json"

        # Check if workflow exists and has changed
        existing_data, existing_hash = load_existing_workflow(workflow_file)
        new_hash = compute_workflow_hash(workflow)

        if existing_hash is None:
            # New workflow
            action = "NEW"
            new_count += 1
        elif existing_hash != new_hash:
            # Workflow changed
            action = "UPDATED"
            updated_count += 1
        else:
            # No change, skip
            unchanged_count += 1
            continue

        # Create directory if needed
        workflow_dir.mkdir(parents=True, exist_ok=True)

        # Write workflow to file
        with open(workflow_file, 'w') as f:
            json.dump(workflow, f, indent=2)

        print(f"[{action}] {category}/{workflow_slug}")

    # Print summary
    print("\n" + "="*60)
    print("Sync Summary:")
    print(f"  New workflows:       {new_count}")
    print(f"  Updated workflows:   {updated_count}")
    print(f"  Unchanged workflows: {unchanged_count}")
    print(f"  Total workflows:     {len(workflows)}")
    print("="*60)

    # Exit with non-zero if no changes (for CI/CD workflows)
    if new_count == 0 and updated_count == 0:
        sys.exit(0)
    else:
        sys.exit(0)  # Exit successfully even if there are changes


if __name__ == '__main__':
    sync_workflows()
