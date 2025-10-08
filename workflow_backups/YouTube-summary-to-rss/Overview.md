# YouTube-summary-to-rss
#projects 


## Option 1 Notion based:
### YouTube Subscriptions Summary to RSS with Notion Storage - n8n Workflow Step Titles

### Notion Database Setup

Create **two Notion databases** with these properties:[1][2]

**Database 1: "YouTube Videos"**
- Title (Title field)
- Video ID (Text)
- Channel ID (Text)
- Channel Name (Text)
- Video URL (URL)
- Published Date (Date)
- Transcript (Text - Long)
- AI Summary (Text - Long)
- Status (Select: New, Processed, Published)
- Processed At (Date)

**Database 2: "Processed Videos Tracker"**
- Video ID (Title field)
- Channel Name (Text)
- Processed Date (Date)
- Summary Generated (Checkbox)

### Workflow Step Titles

**Step 1:** Schedule Trigger (Every 15 Minutes)[3][4]

**Step 2:** Get YouTube Subscriptions List (YouTube OAuth2 API)[5][6]

**Step 3:** Extract Channel IDs from Subscriptions[6][5]

**Step 4:** Loop Through Each Channel RSS Feed[3][5]

**Step 5:** Parse Video Details from All Channels[7][5]

**Step 6:** Search Notion Processed Videos Database[2][1]

**Step 7:** Filter Only Unprocessed Videos (If/Else Node)[8][9]

**Step 8:** Get YouTube Video Transcript[10][5]

**Step 9:** Generate AI Summary with GPT[11][10]

**Step 10:** Create Database Page in YouTube Videos (Notion)[1][8]

**Step 11:** Create Entry in Processed Videos Tracker (Notion)[2][1]

**Step 12:** Update Video Status to "Processed" (Notion)[12][8]

**Step 13:** Get Many Recent Videos from Notion Database[1][2]

**Step 14:** Structure RSS Feed Items from Notion Data[13][5]

**Step 15:** Build Consolidated RSS XML Feed[14][13]

**Step 16:** Serve RSS Feed via Webhook Response[15][7]

### Notion Node Configurations

**Step 6** uses `Database Page` → `Get Many` operation with filter: `{{ $json.videoId }}` matches property "Video ID".[2][1]

**Step 10** uses `Database Page` → `Create` operation with property mapping:
```javascript
Title: {{ $json.title }}
Video ID: {{ $json.videoId }}
Channel Name: {{ $json.channelTitle }}
Video URL: {{ $json.link }}
Transcript: {{ $json.transcript }}
AI Summary: {{ $json.aiSummary }}
Status: "Processed"
```


**Step 11** uses `Database Page` → `Create` operation with simplified tracking data.[1][2]

**Step 13** uses `Database Page` → `Get Many` with filter by Status = "Processed" and sort by "Processed At" descending, limit 50.[8][1]

This architecture provides **visual management** in Notion with full search capabilities, collaborative access, and no database hosting required while maintaining production-grade deduplication.[16][17][18]

Sources
[1] Notion integrations | Workflow automation with n8n https://n8n.io/integrations/notion/
[2] Notion node documentation https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/
[3] How to Use the RSS Node in n8n (Complete Beginners ... https://www.youtube.com/watch?v=J7qDQW8nfdI
[4] RSS Feed trigger node - Questions https://community.n8n.io/t/rss-feed-trigger-node/116454
[5] Automated YouTube Subscription Notifications with RSS ... https://n8n.io/workflows/3216-automated-youtube-subscription-notifications-with-rss-and-email/
[6] Subscriptions: list | YouTube Data API https://developers.google.com/youtube/v3/docs/subscriptions/list
[7] N8N Fast Track Tutorial - Create an RSS Feed Collector https://www.youtube.com/watch?v=Ri3D1wLpYsQ
[8] Overview of Notion nodes in n8n - Notion API/Automation https://www.simonesmerilli.com/business/notion-n8n-nodes
[9] No code Update or Create operations - Questions https://community.n8n.io/t/no-code-update-or-create-operations/31222
[10] AI-Powered YouTube Video Summarization & Analysis https://n8n.io/workflows/2679-ai-powered-youtube-video-summarization-and-analysis/
[11] YouTube Video Summaries with GPT-4o, Slack Approvals ... https://n8n.io/workflows/4581-youtube-video-summaries-with-gpt-4o-slack-approvals-and-reddit-posting/
[12] Cannot update a database item on Notion since 11/09 https://community.n8n.io/t/cannot-update-a-database-item-on-notion-since-11-09/54562
[13] Create YouTube Video RSS Feed with Redis Caching and ... https://n8n.io/workflows/6646-create-youtube-video-rss-feed-with-redis-caching-and-embedded-video-player/
[14] [n8n] YouTube Channel Advanced RSS Feeds Generator https://n8nworkflow.net/workflow/e5008e95-751c-5fc1-6e80-b7076035768c
[15] How to add RSS feeds to n8n https://help.rss.app/en/articles/11434018-how-to-add-rss-feeds-to-n8n
[16] How To Connect Your Notion Database With n8n (Step-By- ... https://www.youtube.com/watch?v=sGIKj1Y-ugU
[17] Backup n8n Workflows with Versioning and Notion Tracking https://n8n.io/workflows/6947-backup-n8n-workflows-with-versioning-and-notion-tracking/
[18] How to automate Notion databases using n8n https://www.youtube.com/watch?v=up2Wi3Y9a-4
[19] Customer Datastore (n8n training) and Notion integration https://n8n.io/integrations/customer-datastore-n8n-training/and/notion/
[20] Best Data & Storage apps & software integrations https://n8n.io/integrations/categories/data-and-storage/
[21] Notion to Pinecone Vector Store Integration https://n8n.io/workflows/2797-notion-to-pinecone-vector-store-integration/
[22] Azure Storage and Notion integration https://n8n.io/integrations/azure-storage/and/notion/
[23] Automated Financial Tracker: Telegram Invoices to Notion ... https://n8n.io/workflows/3960-automated-financial-tracker-telegram-invoices-to-notion-with-gemini-ai-reports/
[24] New to n8n and trying to use it and an API to update ... https://www.reddit.com/r/n8n/comments/1iuivpk/new_to_n8n_and_trying_to_use_it_and_an_api_to/
[25] Sync Notion Content to Webflow CMS as Draft Items with ... https://n8n.io/workflows/7935-sync-notion-content-to-webflow-cms-as-draft-items-with-status-tracking/
[26] Notion and Search And Save integration https://n8n.io/integrations/notion/and/search-and-save/
[27] Notion Node Create vs Update - Feature Requests https://community.n8n.io/t/notion-node-create-vs-update/30917
[28] Create Workflow Inventory Dashboard with n8n API and ... https://n8n.io/workflows/9113-create-workflow-inventory-dashboard-with-n8n-api-and-google-sheets/
[29] Notion and HasData integration - Automate Workflows with ... https://n8n.io/integrations/notion/and/scrape-itcloud/
[30] Building an AI assistant that connects to Notion using GPT ... https://community.latenode.com/t/building-an-ai-assistant-that-connects-to-notion-using-gpt-and-n8n-has-anyone-done-this/2095


## Option 2 Postgres based:<!-- {"fold":true} -->
### YouTube Subscriptions Summary to RSS with PostgreSQL Storage - n8n Workflow Step Titles

### Database Schema Setup

First, create PostgreSQL tables using this schema:[1][2]

```sql
-- Table 1: Track processed videos
CREATE TABLE processed_videos (
    video_id VARCHAR(20) PRIMARY KEY,
    channel_id VARCHAR(50),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 2: Store video metadata and summaries
CREATE TABLE youtube_videos (
    id SERIAL PRIMARY KEY,
    video_id VARCHAR(20) UNIQUE NOT NULL,
    channel_id VARCHAR(50),
    channel_title VARCHAR(255),
    title TEXT,
    description TEXT,
    published_at TIMESTAMP,
    video_url TEXT,
    transcript TEXT,
    ai_summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 3: Store RSS feed items
CREATE TABLE rss_feed_items (
    id SERIAL PRIMARY KEY,
    video_id VARCHAR(20) REFERENCES youtube_videos(video_id),
    rss_entry XML,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Workflow Step Titles

**Step 1:** Schedule Trigger (Every 15 Minutes)[3][4]

**Step 2:** Get YouTube Subscriptions List (YouTube OAuth2 API)[5][6]

**Step 3:** Extract Channel IDs from Subscriptions[6][5]

**Step 4:** Loop Through Each Channel RSS Feed[3][5]

**Step 5:** Parse Video Details from All Channels[7][5]

**Step 6:** Check If Video Already Processed (Postgres SELECT)[2][1]

**Step 7:** Filter Only Unprocessed Videos[8][9]

**Step 8:** Get YouTube Video Transcript[10][5]

**Step 9:** Generate AI Summary with GPT[11][10]

**Step 10:** Insert Video Metadata to Postgres (youtube_videos table)[1][2]

**Step 11:** Mark Video as Processed (Postgres INSERT to processed_videos)[2][1]

**Step 12:** Structure RSS Feed Item[12][5]

**Step 13:** Insert RSS Entry to Postgres (rss_feed_items table)[1][2]

**Step 14:** Aggregate All Recent Summaries from Postgres[2][1]

**Step 15:** Build Consolidated RSS XML Feed[13][12]

**Step 16:** Serve RSS Feed via Webhook Response[14][7]

### PostgreSQL Node Configurations

**Step 6** uses `SELECT` operation with query: `SELECT video_id FROM processed_videos WHERE video_id = $1` with Query Parameters set to `{{ $json.videoId }}`.[1][2]

**Step 10** uses `Insert or Update` operation with Mapping Column Mode set to "Map Automatically" for upsert functionality, matching on `video_id` column.[15][1]

**Step 11** uses `Insert` operation with "Skip on Conflict" enabled to prevent duplicate processing errors.[16][2]

**Step 14** uses `Execute Query` operation with: `SELECT * FROM youtube_videos ORDER BY published_at DESC LIMIT 50` to retrieve the latest 50 summarized videos for RSS feed generation.[2][1]

This architecture provides **durable storage**, **transactional integrity**, and **production-grade deduplication** using PostgreSQL as the single source of truth for all workflow data.[17][18][19]

Sources
[1] Postgres integrations | Workflow automation with n8n https://n8n.io/integrations/postgres/
[2] Postgres node documentation https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/
[3] How to Use the RSS Node in n8n (Complete Beginners ... https://www.youtube.com/watch?v=J7qDQW8nfdI
[4] RSS Feed trigger node - Questions https://community.n8n.io/t/rss-feed-trigger-node/116454
[5] Automated YouTube Subscription Notifications with RSS ... https://n8n.io/workflows/3216-automated-youtube-subscription-notifications-with-rss-and-email/
[6] Subscriptions: list | YouTube Data API https://developers.google.com/youtube/v3/docs/subscriptions/list
[7] N8N Fast Track Tutorial - Create an RSS Feed Collector https://www.youtube.com/watch?v=Ri3D1wLpYsQ
[8] Remove Duplicates node documentation https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/
[9] How to prevent a workflow from processing the same item ... https://www.skool.com/ai-automation-society/how-to-prevent-a-workflow-from-processing-the-same-item-multiple-times?p=8ef400a5
[10] AI-Powered YouTube Video Summarization & Analysis https://n8n.io/workflows/2679-ai-powered-youtube-video-summarization-and-analysis/
[11] YouTube Video Summaries with GPT-4o, Slack Approvals ... https://n8n.io/workflows/4581-youtube-video-summaries-with-gpt-4o-slack-approvals-and-reddit-posting/
[12] Create YouTube Video RSS Feed with Redis Caching and ... https://n8n.io/workflows/6646-create-youtube-video-rss-feed-with-redis-caching-and-embedded-video-player/
[13] [n8n] YouTube Channel Advanced RSS Feeds Generator https://n8nworkflow.net/workflow/e5008e95-751c-5fc1-6e80-b7076035768c
[14] How to add RSS feeds to n8n https://help.rss.app/en/articles/11434018-how-to-add-rss-feeds-to-n8n
[15] Postgres Node has error on Composite Key "Insert or ... https://github.com/n8n-io/n8n/issues/12394
[16] Postgres Node: Effective way to Upsert (Insert or Update) https://community.n8n.io/t/postgres-node-effective-way-to-upsert-insert-or-update/4315
[17] N8N + Postgres Event-Driven Workflows https://www.youtube.com/watch?v=dcuxyPuwV7k
[18] How to set up durable data storage for n8n workflows? https://community.latenode.com/t/how-to-set-up-durable-data-storage-for-n8n-workflows/10014
[19] How To Build An n8n Workflow To Manage Different ... https://hackernoon.com/how-to-build-an-n8n-workflow-to-manage-different-databases-and-scheduling-workflows-sq8h35ld
[20] Postgres and Search And Save integration https://n8n.io/integrations/postgres/and/search-and-save/
[21] Postgres and Solve Data integration https://n8n.io/integrations/postgres/and/solve-data/
[22] Generate and insert data into a Postgres database https://n8n.io/workflows/356-generate-and-insert-data-into-a-postgres-database/
[23] How to loop over items in n8n workflows? https://www.hostinger.com/tutorials/how-to-loop-over-items-in-n8n
[24] Postgres Node - errors inserting data using Execute Query ... https://community.n8n.io/t/postgres-node-errors-inserting-data-using-execute-query-as-well-as-using-upsert/27955
[25] N8N Postgres: CONNECT | INSERT | AUTOMATE (Step‑by ... https://www.youtube.com/watch?v=dAPKYlnBImQ
[26] Integrate Postgres PGVector Store with https://n8n.io/integrations/postgres-pgvector-store/
[27] Update & Insert data in PostgreSQL - Questions https://community.n8n.io/t/update-insert-data-in-postgresql/21219
[28] Where to store data? : r/n8n https://www.reddit.com/r/n8n/comments/1khqb1z/where_to_store_data/
[29] ParsePrompt and Postgres integration https://n8n.io/integrations/parseprompt/and/postgres/
[30] Chat with Postgresql Database | n8n workflow template https://n8n.io/workflows/2859-chat-with-postgresql-database/
[31] Active Trail and Postgres integration https://n8n.io/integrations/active-trail/and/postgres/
[32] UPSERT query in postgres - Questions https://community.n8n.io/t/upsert-query-in-postgres/50444
