# gemini_for_securityV2

A locally hosted, multi-tier SOC (Security Operations Center) incident management flow—built to replace expensive, closed "Copilot for Security" platforms with a transparent, customizable, and cost-effective solution.

---

### What This Is

- **Tiered agent workflow**: Mirrors real SOC ops—automated intake, triage, enrichment, investigation, and escalation.
- **Open integration**: Compatible with any API, enrichment tool, or case management system.
- **Privacy & control**: Runs locally or in your own cloud—no data sent offsite.

---

## How the Flow Works

1. **Ingestion**
   - Alerts/incidents arrive via SIEM, API, webhook, or manual input.

2. **Deduplication & Normalization**
   - Data is normalized to standard schema and deduplicated.
   - Each incident gets a unique `sessionId`.

3. **Tier 1 Analyst – Basic Triage**
   - Rapid intake and summary of core details (who, what, when, where).
   - Classifies as "resolved", "monitor", or "needs deeper investigation".
   - Outputs:  
     ```
     {
       "sessionId": "...",
       "tier1_analysis_summary": "...",
       "tier1_final_status": "...",
       "tier1_recommended_action": "..."
     }
     ```

4. **Escalation Logic**
   - Resolved/benign alerts are closed and logged.
   - Cases flagged for deeper investigation escalate to Tier 2.

5. **Enrichment Layer**
   - Tier 2 receives all previous context.
   - Queries enrichment tools (e.g., irecrawl-tool, SearXNG_http, threat intelligence APIs) for extra user, device, file, network info.

6. **Tier 2 Analyst – Deep Investigation**
   - Reviews incident, context, and evidence.
   - Decides: remediate, escalate, close, or mark as false positive.
   - Outputs:  
     ```
     {
       "sessionId": "...",
       "tier2_analysis": "...",
       "tier2_status": "...",
       "recommended_action": "..."
     }
     ```

7. **Final Escalation**
   - Cases still unresolved move to SOC Lead.

8. **SOC Lead – Final Decision**
   - Highest level review and operational decision (remediate, contain, report, close).
   - Outputs:  
     ```
     {
       "sessionId": "...",
       "soc_leader_summary": "...",
       "soc_leader_decision": "...",
       "final_action": "..."
     }
     ```

9. **Case Logging & Reporting**
   - Every case/action is logged by sessionId for audit and compliance.
   - Optional notifications or report generation for post-mortem.

---

## Features

- **Customizable agent prompts and logic**
- **Pluggable enrichment sources**
- **No vendor lock-in or SaaS fees**
- **Modular design for future additions (playbooks, integrations, reporting, automations)**

## Why Use This?

- **Adaptable:** Tune for your environment, risk, and SOC maturity.
- **Private:** Full control over your data—nothing leaves your infrastructure.
- **Transparent:** Every decision, action, and escalation is logged and auditable.
- **Cost effective:** Free from licensing fees, designed for real-world SOCs.

## Getting Started

- Clone/import the workflow to your n8n instance.
- Plug in your data sources (APIs, SIEM, threat feeds).
- Customize prompts and agent logic for your team/playbook.
- Set up outputs to your preferred notification, case management, or reporting channels.

---

## Next Steps

- Add new enrichment integrations as needed.
- Extend with custom playbooks or automated response actions.
- Document your own incident history for continuous improvement and compliance.

---

**Your SOC, your rules, your automation.  
Replace closed Copilot tools with a workflow that's open, local, and built for true security ops.**
```

