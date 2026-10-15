---
title: "process is not defined (Vite)"
error: "Uncaught ReferenceError: process is not defined"
category: Deploy & environment
tools: [Vite, React, Lovable, Bolt]
heading: '"process is not defined" in a Vite app'
last_checked: 2026-10-15
---


## What it means
Your browser code uses `process.env.SOMETHING`, which works in Node and older React setups, but Vite doesn't provide it in the browser.

## Why AI tools cause it
AI models have seen far more Create React App and Next.js code than Vite code, so they reach for `process.env` by habit.

## The fix
1. Replace `process.env.X` with `import.meta.env.VITE_X` in your frontend code.
2. Rename the variables in `.env` (and on your host) to start with `VITE_`. Vite only exposes variables with that prefix to the browser.
3. Restart the dev server, and redeploy so the build picks up the new names.

Anything starting with `VITE_` is public. Keep secret keys out of it and call those APIs from a server or edge function instead.

## Paste this into your AI
> My Vite app throws "process is not defined". Replace every process.env use in browser code with the Vite equivalent, list the .env variables I need to rename with the VITE_ prefix, and flag any secret keys that shouldn't be in the browser at all.

## Still broken?
If a third-party library uses `process.env`, ask your AI how to add a `define` entry for it in `vite.config`.
