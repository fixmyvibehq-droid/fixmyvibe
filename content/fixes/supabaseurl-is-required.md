---
title: "supabaseUrl is required"
error: "Error: supabaseUrl is required."
category: Deploy & environment
tools: [Supabase, Vercel, Netlify, Lovable, Bolt, Cursor]
heading: '"supabaseUrl is required" — works locally, broken after deploy'
last_checked: 2026-10-15
---


## What it means
Your app tried to connect to Supabase, but the project URL was empty. The code is fine. The value it needs never reached the live site.

## Why AI tools cause it
Your AI put the Supabase URL and key in a `.env` file. That file stays on your computer (it should never be committed), so your host never sees it.

## The fix
1. Open your host's project settings and find **Environment Variables**.
2. Add the same names and values that are in your local `.env`, for example `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` (Next.js) or `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` (Vite).
3. **Redeploy.** Public variables are baked in when the app is built, so adding them without a new build changes nothing.

## Paste this into your AI
> My app throws "supabaseUrl is required" in production but works locally. List every environment variable this project reads, show the exact name each one must have on my host, and check the code reads them with the correct prefix for this framework.

## Still broken?
Check for typos in the variable names. One wrong letter gives you the same error.
