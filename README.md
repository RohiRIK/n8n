# n8n Workflows Repo

Purpose:
- Evolve from backups-only to a full workflow management system.
- Keep workflow_backups/ automation intact and read-only.

Top-level layout:
- workflow_backups/   (EXISTING) automated n8n backups (do not edit)
- ai-blogger/         (EXISTING) AI agent workflow
- docs/               docs (agents, structure, conventions, catalog)
- templates/          starter workflow JSONs and metadata
- projects/           stable, versioned workflows per project
- development/        drafts and experiments
- archived/           retired workflows and old README
- scripts/            management scripts (catalog, sync, lint, tree)

Quick start:
1) Create a workflow from a template:
   - cp templates/http_trigger.json development/my-new-workflow.json
2) Lint:
   - python3 scripts/lint_workflows.py
3) Catalog:
   - python3 scripts/catalog_workflows.py
4) Promote to a project:
   - scripts/sync_workflows.sh promote-dev development/my-new-workflow.json my-project

Notes:
- Never write into workflow_backups/; it is owned by automation.
- Store secrets in environment or n8n credentials; never commit them.

See docs/agents.md for AI agent patterns (e.g., ai-blogger).
