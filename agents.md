# AI Agent Workflows

This document provides a guide to developing and managing AI agent workflows within this repository. For detailed technical standards and conventions, please see [docs/agents.md](./docs/agents.md).

## Getting Started with a New AI Agent

This repository is set up to help you create, test, and deploy new AI agents. Here’s how to get started:

### 1. Create Your Workflow from a Template

Start by copying one of the templates from the `templates/` directory to the `development/` directory. For example, to create a new agent that is triggered by an HTTP request:

```bash
cp templates/http_trigger.json development/my-new-agent.json
```

### 2. Develop and Test Your Agent

Now you can open `development/my-new-agent.json` in n8n and build out your agent's logic. The `development/` directory is your workspace for experimentation.

### 3. Lint Your Workflow

Before promoting your agent, make sure it meets the project's standards by running the linter:

```bash
python3 scripts/lint_workflows.py
```

This will check for common issues and ensure your workflow is ready for the next step.

### 4. Add to the Catalog

Once your agent is working, add it to the project catalog:

```bash
python3 scripts/catalog_workflows.py
```

This script will update the `docs/catalog.json` and `docs/catalog.md` files, making your agent discoverable.

### 5. Promote Your Agent to a Project

When your agent is stable and ready for production use, you can promote it to a project. This will move it to the `projects/` directory, indicating that it is a stable, versioned workflow.

```bash
scripts/sync_workflows.sh promote-dev development/my-new-agent.json my-project
```

Replace `my-project` with the name of the project your agent belongs to.

## Existing Agent Examples

This repository contains a few examples of AI agent workflows that you can use as a reference:

*   **ai-blogger:** A multi-step agent that automates the process of writing and publishing blog posts. You can find more information in the [AI Blogger Workflow Documentation](./ai-blogger/docs/AI_Blogger_Automation_Workflow.md).
*   **Gemini_for_securityV2:** A more complex, multi-tier agent for security operations. See the [Gemini for SecurityV2 README](./Gemini_for_securityV2/README.md) for details.

## Core Principles

When developing AI agents, please keep the following principles in mind:

*   **Clear Roles:** Define clear roles for your agents (e.g., planner, researcher, writer).
*   **Deterministic Entry Points:** Use clear and predictable triggers for your workflows.
*   **Robust Error Handling:** Implement error handling to make your agents more reliable.
*   **Observability:** Ensure that you can monitor your agents' behavior.
*   **Security:** Do not commit secrets to the repository. Use n8n credentials or environment variables.

For more details on these principles, please refer to the [AI Agent Workflows documentation](./docs/agents.md).
