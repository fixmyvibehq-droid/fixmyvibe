---
title: "Mixed Content blocked"
error: "Mixed Content: The page at '...' was loaded over HTTPS, but requested an insecure resource '...'"
category: Deploy & environment
tools: [Vercel, Netlify, Replit, React, Lovable, Bolt]
heading: '"Mixed Content: ... requested an insecure resource" after deploying'
last_checked: 2026-10-18
---


## What it means
Your live site is secure (`https://`), but it's trying to load something over an insecure `http://` address: an API, an image or a script. Browsers block that, so the request silently fails.

## Why AI tools cause it
- **The API address was hard-coded** as `http://localhost:...` or `http://` some server, which worked in development where everything was plain http.
- **An image or script URL** copied from somewhere with `http://`.
- **Your backend doesn't have https set up**, e.g. a server on a bare IP address.

## The fix
1. Open DevTools → **Console**. The warning names the exact `http://` address being blocked.
2. Change it to `https://`. If it's your own API, put the address in an environment variable so live and local can differ.
3. If that server doesn't support https, host it somewhere that does (Vercel, Render, Railway, Fly.io and Replit deployments all give you https), or put it behind a service like Cloudflare.
4. Redeploy and hard-refresh the page.

## Paste this into your AI
> My live site shows "Mixed Content: The page at <my site> was loaded over HTTPS, but requested an insecure resource '<paste URL>'". Find every hard-coded http:// URL in this project, move API addresses into environment variables, and switch everything else to https.

## Still broken?
If the address is already https but still blocked, check for a redirect from https back to http on the server side.
