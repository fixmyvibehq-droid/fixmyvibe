---
title: "Unexpected token '<' ... is not valid JSON"
error: "SyntaxError: Unexpected token '<', \"<!DOCTYPE \"... is not valid JSON"
category: APIs
tools: [React, Next.js, Vite, Vercel, Lovable, Bolt]
heading: '"Unexpected token ''<'', "<!DOCTYPE"... is not valid JSON"'
last_checked: 2026-10-18
---


## What it means
Your code expected JSON data back from a request, but got a web page instead (web pages start with `<!DOCTYPE` or `<html`, hence the `<`). Usually that page is a 404 or error page.

## Why AI tools cause it
- **The API route doesn't exist at that address**, so the host sent back its 404 page or your app's `index.html`.
- **A relative URL like `/api/thing`** that worked in development but on the live site points at a static host with no API behind it.
- **The server crashed** and returned an HTML error page.
- **A login wall or redirect** in front of the API.

## The fix
1. Open DevTools → **Network**, find the failing request and click **Response**. Read the page you actually got back. The title usually says what happened (404, 500, a login page).
2. Check the request URL is right, and that the API is actually deployed. A Vite or React app doesn't have an `/api` folder unless you added server functions.
3. If it's a 500 error, check your host's function logs for the real crash.
4. Make your code check `response.ok` before calling `response.json()`.

## Paste this into your AI
> My app fails with 'Unexpected token "<", "<!DOCTYPE"... is not valid JSON' when calling <the URL>. Check that this API route exists and is deployed with my app, and update the fetch code to check response.ok and the content type before parsing JSON, showing a clear error message if it isn't JSON.

## Still broken?
If you added a catch-all rewrite to `index.html` for page refreshes, make sure it doesn't also catch your `/api` routes.
