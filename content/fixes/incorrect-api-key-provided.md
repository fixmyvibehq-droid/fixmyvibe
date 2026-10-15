---
title: "401 Incorrect API key provided"
error: "401 Incorrect API key provided"
category: AI APIs
tools: [OpenAI, Anthropic, Vercel, Replit]
heading: '"401 Incorrect API key" / "invalid x-api-key" from an AI API'
last_checked: 2026-10-15
---


## What it means
The AI provider rejected your key. It's missing, mistyped, revoked, or the wrong one.

## Why AI tools cause it
- The key is in your local `.env` but was never added to your host.
- The variable name in code doesn't match the name you set (`OPENAI_KEY` vs `OPENAI_API_KEY`).
- The key was pasted with a space, a line break or quote marks around it.
- The key was leaked on GitHub and the provider automatically revoked it.

## The fix
1. Create a fresh key in your provider's dashboard.
2. Set it as a server-only environment variable on your host, with no quotes or spaces, then redeploy.
3. Call the API only from server code. Never put the key in a variable that starts with `NEXT_PUBLIC_` or `VITE_`; those are visible to anyone.

## Paste this into your AI
> My AI API calls fail with a 401 invalid key error in production. Show me exactly which environment variable the code reads, confirm the call happens only on the server, and make sure the key never reaches the browser bundle.

## Still broken?
If the key works on your machine but not live, it's almost always the host's environment variables. Check them again and redeploy.
