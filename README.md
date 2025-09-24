# n8n Workflows Repository

This repository contains a collection of n8n workflows that automate various tasks. Each workflow is stored in its own directory as a JSON file.

## Available Workflows

- **Alert_System**: A system for sending alerts.
- **backup_flow_to_github**: Backs up n8n workflows to GitHub.
- **backup_flow_to_notion**: Backs up n8n workflows to Notion.
- **bloger_automation**: Automates blog posting.
- **bloger_automationV2**: An improved version of the blog posting automation.
- **core_subject_vector**: A workflow for handling core subject vectors.
- **firecrawl_webrequst**: Makes web requests using Firecrawl.
- **Gemini_for_security**: A workflow related to Gemini for security.
- **notion_expens_months_and_years_loop**: Loops through months and years for Notion expenses.
- **notion_recurring_tasks**: Creates recurring tasks in Notion.
- **notion_update_subscription**: Updates subscriptions in Notion.
- **Open_ticket_with_ai**: Opens a ticket with AI.
- **searxng_agent**: An agent for searching with SearxNG.
- **unified_webhook_system**: A unified system for handling webhooks.
- **web_clips_ai_agent**: An AI agent for web clips.
- **web_clips_process**: Processes web clips.

## How to Use

To use these workflows, you can import them into your n8n instance.

1.  Navigate to the workflow you want to use in the `workflow_backups` directory.
2.  Download the JSON file for that workflow.
3.  In your n8n instance, go to **Workflows** and click on **Import from File**.
4.  Select the downloaded JSON file to import the workflow.

## Contributing

Contributions to this repository are welcome. If you have a workflow that you would like to add, please follow these steps:

1.  Fork the repository.
2.  Create a new directory for your workflow under the `workflow_backups` directory.
3.  Add your workflow as a JSON file in the new directory.
4.  Create a pull request with a description of your workflow.
