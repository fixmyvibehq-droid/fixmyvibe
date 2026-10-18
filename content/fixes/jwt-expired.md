---
title: "JWT expired"
error: "JWT expired"
category: Database & auth
tools: [Supabase, Next.js, Lovable, Bolt]
heading: '"JWT expired" errors from Supabase'
last_checked: 2026-10-18
---


## What it means
A JWT is the signed-in user's access pass. Supabase's expire after an hour by default and are meant to be swapped for a fresh one automatically. "JWT expired" means your app sent an old one.

## Why AI tools cause it
- **The token was copied and stored** (in a variable, React state or your own localStorage key) instead of letting the Supabase client manage it.
- **A new Supabase client is created on every request** on the server, without the refresh token, so it can't renew anything.
- **Next.js server code** reads the session but nothing refreshes the cookies on each request.
- The laptop was asleep, so the background refresh never ran, and the first request on waking fails.

## The fix
1. Use one Supabase client in the browser and let it handle tokens. Don't save the access token yourself.
2. In the browser, before making a request after a long idle period, call `supabase.auth.getSession()` so the client refreshes if needed. Never rely on `getSession()` in server code.
3. In Next.js, follow Supabase's server-side auth guide using `@supabase/ssr`. That includes the file that refreshes the session cookie on every request: `proxy.ts` on Next.js 16 and later, `middleware.ts` on Next.js 15 and earlier. In server code, check the user with `supabase.auth.getClaims()`, not `getSession()`.
4. If an error still slips through, catch it, refresh the session and retry once, or send the user to log in.

## Paste this into your AI
> My Supabase app throws "JWT expired" after the user has been signed in for a while. Find anywhere this project stores or passes the access token by hand and replace it with the Supabase client's own session handling. If this is Next.js, set up @supabase/ssr with a proxy.ts (Next.js 16+) or middleware.ts (Next.js 15 and earlier) file that refreshes the session cookie, following Supabase's official guide.

## Still broken?
Check your computer's clock is right. A clock that's off by more than a few minutes makes valid tokens look expired.
