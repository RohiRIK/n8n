# Gemini Code Assistant Context

This document provides context for the Gemini Code Assistant to understand and effectively assist with the n8n-workflows project.

## Project Overview

This repository is a comprehensive system for managing and versioning n8n workflows. It provides a structured environment for developing, testing, and deploying workflows, moving beyond simple backups to a full workflow lifecycle management system. The project includes conventions, templates, and scripts to ensure consistency and quality.

## Directory Structure

The repository is organized into the following key directories:

*   `workflow_backups/`: Contains automated, read-only backups of n8n workflows. This directory should not be manually edited.
*   `development/`: A workspace for creating and experimenting with new workflows.
*   `projects/`: Stores stable, versioned workflows organized by project.
*   `archived/`: For retired workflows and older versions.
*   `templates/`: Contains starter templates for various workflow types (e.g., cron jobs, HTTP triggers) and metadata.
*   `docs/`: Project documentation, including conventions, structure, and information on AI agent patterns.
*   `scripts/`: A collection of Python and shell scripts for managing workflows, including linting, cataloging, and synchronization.

## Workflow Lifecycle

The typical lifecycle of a workflow is as follows:

1.  **Creation:** A new workflow is created in the `development/` directory, often starting from a template in `templates/`.
2.  **Linting:** The workflow is checked for basic quality and standards using the `scripts/lint_workflows.py` script.
3.  **Cataloging:** The workflow is added to the project catalog using `scripts/catalog_workflows.py`, which generates `docs/catalog.json` and `docs/catalog.md`.
4.  **Promotion:** Once a workflow is considered stable, it is promoted to a specific project in the `projects/` directory using the `scripts/sync_workflows.sh` script.

## Key Scripts

The `scripts/` directory contains several important tools for managing workflows:

*   `lint_workflows.py`: Lints workflow `.json` files in the `development/` and `projects/` directories to ensure they meet basic standards, such as having a name and a valid node structure.
*   `catalog_workflows.py`: Scans the `workflow_backups/`, `projects/`, and `development/` directories for `.json` files and creates a catalog in both JSON and Markdown formats (`docs/catalog.json` and `docs/catalog.md`).
*   `sync_workflows.sh`: A shell script with several functions:
    *   `import-backups`: Copies workflows from `workflow_backups/` to `development/imported/`.
    *   `promote-dev`: Promotes a workflow from `development/` to a `projects/` subdirectory.
    *   `list`: Shows the number of workflow files in each main directory.
*   `tree.sh`: Generates a tree view of the directory structure.

## Conventions

The project follows a set of conventions to maintain consistency:

*   **Filenames:** Use kebab-case for workflow files (e.g., `my-new-workflow.json`).
*   **Tags:** Utilize n8n's tagging feature to categorize workflows by project, environment, and purpose.
*   **Metadata:** An optional `templates/metadata.yml` file can be used to provide additional information about a workflow.
*   **Immutability of Backups:** The `workflow_backups/` directory is treated as a read-only source of truth for automated backups.

## AI Agent Workflows

The repository has a specific focus on creating and managing multi-step AI agent workflows. The `docs/agents.md` file outlines the core principles for these workflows:

*   **Clear Roles:** Agents should have distinct roles (e.g., planner, researcher, writer).
*   **Deterministic Entry Points:** Workflows should be triggered by predictable events (e.g., HTTP request, cron schedule).
*   **Robust Error Handling:** Implement error handling to catch and manage failures.
*   **Observability:** Enable execution data to be saved for monitoring, while being mindful of sensitive information.
*   **Security:** Secrets should be managed through environment variables or n8n credentials, never committed to the repository.

The `ai-blogger/` directory serves as an example of an AI agent workflow, and the `Gemini_for_securityV2/` project demonstrates a more complex, multi-tier security-focused agent.
