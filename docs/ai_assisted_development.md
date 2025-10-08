# AI-Assisted n8n Workflow Development

This document outlines the methods and best practices for using a CLI agent to assist in the development and management of n8n workflows within this repository.

## 1. Natural Language to Workflow

The CLI agent can generate n8n workflow JSON files from a natural language description.

**Example:**
> "Create a workflow that triggers every morning at 8 AM, fetches the top 5 articles from the Hacker News RSS feed, and then sends them to my Telegram chat."

The agent will then generate a new workflow file (e.g., `development/hacker-news-telegram.json`) with the necessary nodes and connections.

## 2. AI-Powered Workflow Modification

The agent can modify or enhance existing workflows based on your requests.

**Example:**
> "Take the `bloger_automation` workflow and add an error-handling path. If any step fails, it should send a notification to a Slack channel."

The agent will read the existing workflow, add the required nodes, and update the file with the new logic.

## 3. Workflow Optimization and Best Practices

The agent can analyze your workflows and suggest improvements.

**Example:**
> "Review my `Gemini_for_security` workflow and suggest any optimizations."

The agent will analyze the workflow for:
*   Inefficient looping or data handling.
*   Missing error handling.
*   Opportunities to use more efficient nodes or expressions.
*   Adherence to n8n best practices.

## 4. Data Transformation and Mapping

For complex data transformations, the agent can generate the necessary JavaScript code for a "Code" or "Set" node based on examples of input and desired output data.

**Example:**
> "I have a JSON object with a user's full name. I need to split it into `firstName` and `lastName` fields."

The agent will provide the JavaScript code to perform this transformation.

## Integration with this Repository

This AI-assisted development process integrates seamlessly with the existing structure of this repository:

1.  **Development:** The agent will create and modify all new workflows in the `development/` directory.
2.  **Linting:** You can use the `scripts/lint_workflows.py` script to check the quality of the AI-generated workflows.
3.  **Promotion:** Once a workflow is ready, you can use the `scripts/sync_workflows.sh` script to promote it to the `projects/` directory.
