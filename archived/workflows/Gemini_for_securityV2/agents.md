## Tier 1 Analyst – Basic Triage

**Purpose:**  
Rapidly evaluate new alerts/incidents, deduplicate incoming records, assign initial context (type, status, severity), and recommend next action (resolve, investigate, escalate).

**Key Focus Areas:**  
- Normalize and deduplicate alerts/incidents.
- Assign unique sessionId for every alert/incident.
- Summarize relevant details (what, who, where, severity).
- Classify as benign, resolved, or needing deeper investigation.

**Tools Used:**  
- n8n normalization logic (deduplication, sessionId generation)
- Custom mappings for context extraction

**Output:**  
- `sessionId` — unique per alert/incident
- `tier1_analysis_summary`
- `tier1_final_status` (`resolved`, `false_positive`, `needs deeper investigation`)
- `tier1_recommended_action` (`close`, `escalate to Tier 2`, `monitor`)


---

## Tier 2 Analyst – Deep Investigation

**Purpose:**  
Investigate complex or ambiguous cases escalated from Tier 1. Perform deep context enrichment (host/user lookups, threat intelligence), determine actual severity, and recommend remediation or further escalation.

**Key Focus Areas:**  
- Review incident, Tier 1 summary, all enrichment data.
- Analyze via enrichment tools; reference findings by tool.
- Decide and recommend next steps (remediation, escalation, closure).

**Tools Used:**  
- irecrawl-tool: Deep web crawling/context lookup
- SearXNG_http: IOC, web search, threat intelligence
- Internal enrichment APIs (if present)

**Output:**  
- `sessionId`  
- `tier2_analysis` (must cite enrichment findings)
- `tier2_status` (`resolved`, `needs remediation`, `false positive`, `needs escalation`)
- `recommended_action` (`remediate`, `escalate to SOC Lead`, `close`)


---

## SOC Lead – Final Authority

**Purpose:**  
Handle the most critical/complex incidents (escalated by Tier 2). Decide on urgent actions: contain, remediate, escalate outside SOC, or close.

**Key Focus Areas:**  
- Review all prior analysis, evidence, and referenced tool findings.
- Approve/deny escalation, order operational or management actions (e.g., quarantine device, notify leadership).

**Tools Used:**  
- Workflow context aggregation (all prior outputs)
- Review of enrichment tool results, analyst notes, evidence files

**Output:**  
- `sessionId`
- `soc_leader_summary`
- `soc_leader_decision`
- `final_action`
```



