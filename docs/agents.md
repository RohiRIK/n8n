# AI Agent Workflows (n8n)

Purpose:
- Define standards and patterns for multi-step AI agent workflows in n8n.
- Keep ai-blogger/ intact; use this doc to guide future agent directories.

Core principles:
- Clear agent roles (planner, researcher, writer, reviewer, publisher)
- Deterministic entry points (HTTP Trigger, Cron, Webhook, Event)
- Robust error handling (Error Trigger + notify)
- Observability (Execution data enabled; minimal PII in logs)
- Idempotency and retry-safe nodes
- Secrets via environment variables only (never commit secrets)

Folder usage:
- ai-blogger/: Existing AI agent workflow (unchanged)
- templates/: Base templates to create new agents
- development/: Draft/work-in-progress agent workflows
- projects/: Stable, versioned agent workflows per project
- archived/: Retired agents and old versions

Naming:
- Use kebab-case for workflow names and files
- Prefix by project if helpful (e.g., ai-blogger-content-writer)

Versioning:
- Keep version info in README or metadata; commit messages should include changes
- Optional: suffix file with vX.Y.Z before promotion to projects

Required nodes (suggested for agents):
- Trigger: HTTP Trigger or Cron
- Context: Code/Function to assemble request context
- LLM Steps: Tool selection / writing / reviewing (LLM or external APIs)
- Persistence: Drive/DB/Notion/GCS/S3 as needed
- Error: Error Trigger → Notify (Slack/Email/HTTP Request)

Security:
- No secrets in repo; use environment or n8n credentials
- Avoid logging personal or sensitive content

Example pipeline (ai-blogger):
- Trigger → Plan → Research → Draft → Review → Publish → Notify