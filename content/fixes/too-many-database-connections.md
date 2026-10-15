---
title: "Too many database connections (serverless)"
error: "remaining connection slots are reserved / too many clients already"
category: Database & auth
tools: [Prisma, Drizzle, Postgres, Supabase, Neon, Vercel]
heading: '"Too many connections" after launch'
last_checked: 2026-10-15
---


## What it means
Your Postgres database ran out of connection slots. It worked fine with one user and starts failing as traffic grows. You may also see Prisma's "Can't reach database server" or "Timed out fetching a new connection".

## Why AI tools cause it
On serverless hosts, every function instance opens its own connections. AI-generated setups usually use the direct database URL with no pooling, and often create a new database client on every request.

## The fix
1. Use your provider's **pooled** connection string for the app (Supabase, Neon and others show it next to the direct one). Keep the direct URL for running migrations.
2. With Prisma on a pooled connection, follow your provider's Prisma instructions; Supabase's transaction pooler, for example, needs `?pgbouncer=true` on the URL.
3. Create the database client once and reuse it, rather than inside each request handler.

## Paste this into your AI
> My serverless app hits "too many connections" on Postgres. Check how the database client is created, make it a single reused instance, switch the app to a pooled connection string with the right settings for my ORM and provider, and keep the direct URL only for migrations.

## Still broken?
Look for code that opens a connection in a loop, or a background script running alongside the app and holding connections open.
