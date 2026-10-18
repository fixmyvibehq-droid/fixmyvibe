---
title: "Supabase project paused"
error: "Project is paused"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Vercel]
heading: 'App suddenly dead because your Supabase project was paused'
last_checked: 2026-10-18
---


## What it means
Supabase pauses free projects that have very little activity over 7 days. While paused, your app can't reach the database, so logins and data loading fail, often with "Failed to fetch" or a connection error rather than a clear message.

## Why AI tools cause it
Nothing in your code is wrong. This hits side projects and demos that you built, launched and then didn't use for a week.

## The fix
1. Open the Supabase dashboard, pick the project, and click **Resume project**. It comes back with your data and settings.
2. Wait a few minutes for it to finish starting, then reload your app.
3. You can restore a paused project for up to a year, but don't leave it that long.
4. If real users rely on the app, upgrade to a paid plan, which doesn't pause.

Don't rely on "keep-alive" scripts that ping the database to dodge the pause. If the app matters, it's worth the paid plan.

## Paste this into your AI
> My Supabase project was paused, so my app showed broken errors to users. Add friendly error handling around my Supabase calls so that if the database can't be reached, users see "We're having trouble connecting, please try again shortly" instead of a blank page or a raw error.

## Still broken?
If the project says it's active but the app still fails, check your environment variables still point at this project's URL and keys.
