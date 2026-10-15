---
title: "FUNCTION_INVOCATION_TIMEOUT on Vercel"
error: "504: GATEWAY_TIMEOUT — FUNCTION_INVOCATION_TIMEOUT"
category: Deploy & environment
tools: [Vercel, Next.js, OpenAI, Anthropic]
heading: 'Vercel "FUNCTION_INVOCATION_TIMEOUT"'
last_checked: 2026-10-15
---


## What it means
A server function took longer than your Vercel plan allows, so Vercel stopped it and returned a 504.

## Why AI tools cause it
- Waiting for a long AI response to finish before replying.
- Doing several slow jobs one after another (scraping, image generation, big database queries).
- A request that never returns, such as a database call that hangs or a missing `return` in a route.

## The fix
1. **Stream AI responses** instead of waiting for the whole answer. The user sees text straight away and the function stays responsive.
2. Run independent slow calls at the same time with `Promise.all`.
3. If a job really is long, raise the function's maximum duration within your plan's limit (`export const maxDuration = ...` in Next.js), or move it to a background job and let the page check back.
4. Add timeouts to outside calls so a hung request fails fast with a clear error.

## Paste this into your AI
> This Vercel function times out with FUNCTION_INVOCATION_TIMEOUT. Find what's slow, stream any AI responses, run independent calls in parallel, add timeouts to external requests, and tell me if this job should be moved to a background task.

## Still broken?
Check Vercel's function logs for the request. If it times out even on tiny inputs, something is hanging rather than slow.
