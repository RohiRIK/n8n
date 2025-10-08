# enrichment.md

## Purpose

This document explains how to enhance and supercharge your local SOC automation workflow with additional context, actionable insights, and improved case outcomes. The enrichment layer is where data, intelligence, and automation combine to take your security response beyond simple triage.

---

## What is Enrichment?

**Enrichment** means automatically gathering and attaching extra context to every alert or incident, allowing agents (both human and automated) to make faster, smarter decisions. It’s the bridge from basic “event received” to deep understanding and action.

---

## Enhancement Strategies

### 1. Integrate More HTTP Requests

- Use additional HTTP nodes to query:
  - User and asset databases (AD, asset search)
  - Threat intelligence feeds (domain/IP/file lookup)
  - Email/message logs for context
  - Cloud APIs for device/user info
- Every query adds more perspective on whether an alert is legitimate, a false positive, or a serious issue.

### 2. Add Real-time Alerting

- Build custom webhook triggers (Slack, Teams, email, SIEM update) within the flow.
- Automatically notify the right analyst or team when high-risk events or critical decisions occur.
- Tie notifications to sessionId and include summarized context and direct links to evidence.

### 3. Advanced Playbook Automation

- Create playbook nodes for routine checks (block IP, reset password, kick off forensics).
- Use enrichment results to trigger automated SOAR actions, not just recommendations.

### 4. Evidence & Artifact Aggregation

- Append links to relevant files, logs, screenshots, and investigation artifacts.
- Store them for every case and propagate across escalation tiers.

### 5. Contextual Linking

- Correlate alerts, check if involved users/devices appeared in past incidents.
- Flag recurring patterns, link similar cases, and pass that data to analysts.

### 6. Flexible Tooling

- Add new tools as needed: custom scripts, local ML models, proprietary feeds.
- Build enrichment nodes modular so you can easily swap out or upgrade sources.

---

## Example: Typical Tier 2 Enrichment Flow

1. **Input:** Escalated alert from Tier 1  
2. **HTTP Queries:** Threat feed search, asset ownership lookup, user log history request  
3. **Artifact Attach:** Add file hashes, screenshot URLs, related ticket IDs  
4. **Context Merge:** Structure all results as `enrichment` or `toolResults` object  
5. **Agent Decision:** Tier 2 analysis now includes both the original incident and all evidence/artifact context

---

## Benefits

- Faster investigation and reduced manual lookup
- Deeper, richer findings for each case
- Fewer missed links, more “closed on first review” incidents
- Prepared evidence trail for post-mortem, reporting, or compliance review
- Ability to tune/expand sources as threats evolve

---

## Looking Ahead

- Keep adding new sources—every useful API, DB, or log can be tapped.
- Integrate automation triggers for repetitive response actions.
- Modularize enrichment logic for easy upgrades and maintenance.
- Share your best queries and playbooks for others in your SOC or community.

---

Start supercharging your SOC flow today—every new HTTP request, notification, or enrichment node adds value, context, and real-world effectiveness!
```

