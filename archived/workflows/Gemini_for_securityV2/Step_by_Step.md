## SOC Automation Flow – Step by Step

1. **Ingestion/Trigger — Start of Flow**
   - New security alerts/incidents are ingested from detection systems (e.g., API, SIEM, webhook).
   - Raw data is normalized and sent to the workflow.

2. **Deduplication/Normalization**
   - Alerts are deduplicated.
   - Relevant fields are mapped to a standard schema.
   - Each incident receives a unique `sessionId`.

3. **Tier 1 Agent – Basic Triage**
   - Reviews and summarizes basic alert details.
   - Assigns classification: resolve/close, monitor, or escalate to Tier 2.
   - Outputs structured JSON with summary, status, and recommendation.

4. **Routing (Switch/IF Node)**
   - Routes alerts based on Tier 1 recommendation.
   - "Needs deeper investigation" goes to Tier 2.
   - Resolved cases exit (with audit log).

5. **(Optional) Enrichment Layer**
   - Enrichment tools (e.g., irecrawl-tool, SearXNG_http) are run.
   - Adds further context: threat intel, user/device data, file/IP evidence.

6. **Tier 2 Agent – Deep Investigation**
   - Reviews incident, all prior context, enrichment results.
   - Performs deeper analysis, identifies links and threats.
   - Recommends: remediate/close, mark as false positive, or escalate to SOC Lead.

7. **Routing (Switch/IF Node)**
   - If resolved/remediated, ends flow and logs result.
   - If needs escalation, passes case to SOC Lead.

8. **SOC Lead (Tier 3) – Final Authority**
   - Final review of all evidence, prior outputs.
   - Makes critical decisions: remediation, escalation, closure.
   - Outputs final structured decision for audit and action.

9. **Post-Incident/Case Management**
   - All actions and outcomes are logged (SIEM, Notion, database, notifications as needed).
   - (Optional) Trigger reporting, knowledge base updates, or automated feedback for workflow improvement.
```

