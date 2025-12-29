#!/bin/bash
# Auto-generated rollback script for workflow migration
# Generated: 2025-12-29 10:03:46

set -e

echo "Starting rollback..."

echo 'Rolling back archive: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/Gemini_for_securityV2 -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Gemini_for_securityV2'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/Gemini_for_securityV2' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Gemini_for_securityV2'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/blogger_automation -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/bloger_automationV2'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/blogger_automation' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/bloger_automationV2'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/gemini_for_security -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/gemini_for_securityV2'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/gemini_for_security' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/gemini_for_securityV2'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/authentication/graph_authentications -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Graph_Authentications'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/authentication/graph_authentications' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Graph_Authentications'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/firecrawl_web_request -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/firecrawl_webrequst'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/firecrawl_web_request' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/firecrawl_webrequst'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/core_subject_vector -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/core_subject_vector'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/core_subject_vector' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/core_subject_vector'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/searxng_agent -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/searxng_agent'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/agents/searxng_agent' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/searxng_agent'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/alerts/unified_webhook_system -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/unified_webhook_system'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/alerts/unified_webhook_system' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/unified_webhook_system'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/alerts/alert_system -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Alert_System'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/alerts/alert_system' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Alert_System'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_update_subscription -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_update_subscription'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_update_subscription' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_update_subscription'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_recurring_tasks -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_recurring_tasks'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_recurring_tasks' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_recurring_tasks'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_expense_months_and_years_loop -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_expens_months_and_years_loop'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion/notion_expense_months_and_years_loop' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/notion_expens_months_and_years_loop'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/open_ticket_with_ai -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Open_ticket_with_ai'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/open_ticket_with_ai' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Open_ticket_with_ai'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/break_glass_account_automation -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Break Glass Account Automation for n8n'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/break_glass_account_automation' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Break Glass Account Automation for n8n'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/phishguard365 -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/phishguard365'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/security/phishguard365' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/phishguard365'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/ultimate_automation_solutions_for_it -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Ultimate_Automation_Solutions_for_IT'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/ultimate_automation_solutions_for_it' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Ultimate_Automation_Solutions_for_IT'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/web_clips_process -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/web_clips_process'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/web_clips_process' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/web_clips_process'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/web_clips_ai_agent -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/web_clips_ai_agent'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/blogging/web_clips_ai_agent' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/web_clips_ai_agent'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_notion -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_notion'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_notion' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_notion'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_homelab_rpo -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_homelab_rpo'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_homelab_rpo' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_homelab_rpo'

echo 'Rolling back move: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_github -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_github'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup/backup_flow_to_github' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/backup_flow_to_github'

echo 'Rolling back archive: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/blogger_automation_v1 -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/bloger_automation'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/blogger_automation_v1' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/bloger_automation'

echo 'Rolling back archive: /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/gemini_for_security_v1 -> /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Gemini_for_security'
mv '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/archived/workflows/gemini_for_security_v1' '/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/workflow_backups/Gemini_for_security'

echo "Rollback complete!"
