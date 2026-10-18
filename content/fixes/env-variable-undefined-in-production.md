---
title: "Environment variable undefined in production"
error: "process.env.NEXT_PUBLIC_... is undefined"
category: Deploy & environment
tools: [Vercel, Netlify, Next.js, Vite, Lovable, Bolt]
heading: 'Environment variable is undefined after you deploy'
last_checked: 2026-10-18
---


## What it means
Your app reads a setting, like an API URL or a public key, from an environment variable. On your computer it's there; on the live site it comes back `undefined`.

## Why AI tools cause it
- **The `.env` file never leaves your computer** (it shouldn't), so the live host doesn't know the values until you add them there.
- **Missing prefix.** Browser code can only see variables that start with `NEXT_PUBLIC_` (Next.js) or `VITE_` (Vite). Anything else is hidden from the browser on purpose.
- **Added but not rebuilt.** These values are baked in when the site builds, so adding them later does nothing until you redeploy.
- **Set for the wrong environment**, e.g. Preview but not Production on Vercel.

## The fix
1. In your host's dashboard (Vercel: **Settings → Environment Variables**), add every variable from your `.env` file, spelled exactly the same.
2. Tick the **Production** environment as well as Preview.
3. Redeploy. On Vercel, open the latest deployment and choose **Redeploy**.
4. Only use the `NEXT_PUBLIC_` or `VITE_` prefix for values that are safe for anyone to see. Secret keys stay without the prefix and are used only in server code.

## Paste this into your AI
> An environment variable is undefined on my deployed site but works locally. List every environment variable this project uses, say whether each is needed in the browser or only on the server, check the browser ones have the right prefix for my framework, and flag any secret key that is wrongly exposed to the browser. Give me the exact list to paste into my host's settings.

## Still broken?
In Vite apps, use `import.meta.env.VITE_NAME`, not `process.env`. See our "process is not defined" fix.
