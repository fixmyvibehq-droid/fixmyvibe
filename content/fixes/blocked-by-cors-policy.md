---
title: "blocked by CORS policy"
error: "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource"
category: APIs
tools: [Any frontend, Supabase Edge Functions, Express, FastAPI]
heading: '"Blocked by CORS policy" when calling an API'
last_checked: 2026-10-15
---


## What it means
Your browser refused the response because the server didn't say your site is allowed to call it. The request may have worked; the browser just won't hand you the result.

## Why AI tools cause it
The AI built a frontend and a backend on different addresses (say `localhost:5173` and `localhost:3000`, or your site and a function URL) without setting up the server to allow it. Sometimes it's calling a third-party API straight from the browser, which that API doesn't allow.

## The fix
- **Your own backend:** set it to send `Access-Control-Allow-Origin` with your site's exact address. Answer `OPTIONS` (preflight) requests too.
- **A third-party API** (OpenAI, Stripe, etc.): don't call it from the browser. Call your own server route, and have that call the API. This also keeps your secret key off the browser.
- Avoid `*` in production. List your real domains instead.

## Paste this into your AI
> My frontend gets a CORS error calling <paste URL>. Tell me whether this request should go through my own server instead. If it's my API, add CORS handling that allows only my local dev address and my production domain, including OPTIONS preflight requests.

## Still broken?
Open the browser's Network tab. If the request shows a 404 or 500, fix that first; a crashing server also sends no CORS header.
