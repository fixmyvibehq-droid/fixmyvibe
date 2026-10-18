---
title: "404 when you refresh a page"
error: "404: NOT_FOUND"
category: Deploy & environment
tools: [Vercel, Netlify, Vite, React, Lovable, Bolt]
heading: 'Page works until you refresh it, then shows 404 NOT_FOUND'
last_checked: 2026-10-18
---


## What it means
Your app is a single-page app: one `index.html` file, with the browser switching "pages" itself. Clicking links works. But when you refresh `/dashboard` or open it from a link, the host looks for a real `dashboard` file, finds nothing and shows a 404.

## Why AI tools cause it
Lovable, Bolt and most Vite + React projects are single-page apps using React Router. Their preview servers handle this for you, so it only breaks once you deploy somewhere else and nobody told the host to send every path to `index.html`.

## The fix
**On Vercel:** add a file called `vercel.json` in the project root:
```
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }
```

**On Netlify:** add a file called `_redirects` in your `public` folder:
```
/*  /index.html  200
```

**On Cloudflare Pages:** this usually works with no setup, as long as there is no `404.html` in your build. On Cloudflare Workers with static assets, set `not_found_handling = "single-page-application"` under `[assets]` in your wrangler config.

Then commit and redeploy.

## Paste this into your AI
> My React single-page app shows 404 when I refresh any page except the home page after deploying to <your host>. Add the correct rewrite config for that host so every route serves index.html, without breaking real files like images, and add a proper "page not found" route inside React Router.

## Still broken?
This fix is for Vite or Create React App projects. If you're using Next.js, a 404 on refresh usually means that page file doesn't exist in `app/` or `pages/`.
