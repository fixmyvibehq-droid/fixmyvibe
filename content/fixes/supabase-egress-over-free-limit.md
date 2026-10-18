---
title: "Supabase egress over the free limit"
error: "Service for this project is restricted due to the following violations: exceed_egress_quota"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Cursor]
heading: 'Supabase egress over the free limit ("exceed_egress_quota")'
last_checked: 2026-10-18
---


## What it means
Egress is the data Supabase sends out of your project: database rows, files from Storage, auth and realtime traffic. The free plan includes 5 GB of uncached egress and 5 GB of cached egress a month. Go over it and Supabase emails you, gives you a grace period, and can then restrict the project. Once restricted, API requests fail with a 402 error and a message like `exceed_egress_quota`.

## Why AI tools cause it
AI-written code tends to fetch far more than the screen needs:
- **`select('*')` with no limit**, so every page load downloads every row and every column.
- **Full-size images** from Storage shown in small thumbnails.
- **Polling**: a timer that refetches the same data every few seconds, in every open tab.
- **Writes ending in `.select()`**, which send the whole row back when you only needed the id.

## The fix
1. In Supabase, open your organisation's **Usage** page and look at **Egress**. Hover over a day to see which service (Database, Storage, Realtime) used it.
2. If it's Database: select only the columns you show, and add `.limit()` or pagination to every list.
3. If it's Storage: resize images before upload, or serve smaller versions for thumbnails.
4. Remove polling timers, or slow them right down. Filter any Realtime subscriptions to the rows the user actually needs.
5. The restriction lifts at the start of your next billing cycle, or straight away if you upgrade.

## Paste this into your AI
> My Supabase project went over the free egress limit. Find every Supabase query, Storage download and Realtime subscription in this project. For each one, tell me how much data it could pull, then change it to select only the columns the UI uses, add pagination or a limit to lists, remove or slow any polling, and stop inserts and updates returning full rows unless the code needs them.

## Still broken?
If usage still climbs, check whether a bot or a loop is hitting your API. In **Logs**, look for the same request repeating many times a minute.
