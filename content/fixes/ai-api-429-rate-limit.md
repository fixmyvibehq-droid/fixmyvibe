---
title: "429 Too Many Requests from an AI API"
error: "429 Rate limit reached / You exceeded your current quota"
category: AI APIs
tools: [OpenAI, Anthropic, Gemini]
heading: '"429 Too Many Requests" or "exceeded your current quota"'
last_checked: 2026-10-15
---


## What it means
The AI provider turned your request away. Either you're sending requests too fast (rate limit), or your account has no credit or has hit its spending cap (quota). The message tells you which.

## Why AI tools cause it
- Code that fires a request on every keystroke, or retries instantly in a loop.
- A new account on a low usage tier, or one with no credit added.
- No caching, so the same question is paid for again and again.

## The fix
1. **Quota message:** add credit or raise your spending limit in the provider's billing settings.
2. **Rate limit message:** retry with a growing wait between tries (exponential backoff), and respect any `retry-after` header.
3. Stop extra calls at the source: debounce inputs, and cache answers to repeated prompts.
4. Add a per-user limit in your own app so one user (or bot) can't burn through your budget.

## Paste this into your AI
> My app gets 429 errors from the AI API. Add retries with exponential backoff that respect retry-after, debounce any calls triggered by typing, cache repeated requests, and add a simple per-user rate limit on the route that calls the API.

## Still broken?
Check your provider's usage page. A sudden spike usually means a loop in your code or someone abusing an open endpoint.
