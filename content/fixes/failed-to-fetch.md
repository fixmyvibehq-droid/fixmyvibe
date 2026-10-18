---
title: "Failed to fetch"
error: "TypeError: Failed to fetch"
category: APIs
tools: [React, Next.js, Supabase, Lovable, Bolt, Cursor]
heading: '"TypeError: Failed to fetch" in the browser'
last_checked: 2026-10-18
---


## What it means
The browser tried to call a server and got no usable answer. It's a vague error because the browser hides the details from your code. The real reason is almost always in the browser's DevTools.

## Why AI tools cause it
- **The URL points at `localhost`**, which only exists on your computer, not your users'.
- **CORS**: the server didn't allow your site's address. DevTools will say "blocked by CORS policy".
- **http vs https**: a secure site calling an `http://` address is blocked.
- **The server is down, asleep or paused** (a free Supabase project, or a Replit or Render server that sleeps).
- **A browser extension** like an ad blocker blocked the request.

## The fix
1. Open DevTools (F12 or right-click → Inspect), go to **Console** and **Network**, and repeat the action. The red line names the real problem.
2. Check the URL being called. If it says `localhost` or `127.0.0.1` on your live site, move it into an environment variable and set the live address on your host.
3. If the console mentions CORS, see our CORS fix.
4. Open the API address directly in a new tab. If it doesn't load, the server is the problem, not your code.
5. Try a private window with extensions off.

## Paste this into your AI
> My app shows "TypeError: Failed to fetch". Here's what the browser console and Network tab say: <paste them>. Find every fetch call in this project, make sure none use a hard-coded localhost URL, and wrap them so users see a helpful message instead of a crash.

## Still broken?
If it fails only on some phones or networks, check that the API uses https and a valid certificate.
