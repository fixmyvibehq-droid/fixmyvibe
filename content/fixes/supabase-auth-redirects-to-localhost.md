---
title: "Supabase login redirects to localhost"
error: "Magic link or OAuth login sends users to localhost:3000"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Vercel]
heading: 'Supabase login or magic link sends users to localhost'
last_checked: 2026-10-15
---


## What it means
After signing in, users land on `localhost:3000` (or another dev address) and see an error page. Supabase is sending them to the address in its settings, which is still your development one.

## Why AI tools cause it
Supabase's **Site URL** defaults to localhost while you build, and AI tools rarely remind you to change it when you go live.

## The fix
1. In Supabase, open **Authentication → URL Configuration**.
2. Set **Site URL** to your live address, e.g. `https://yourapp.com`.
3. Under **Redirect URLs**, add your live address and keep `http://localhost:3000/**` for local testing.
4. In your code, pass `emailRedirectTo` (magic links) or `redirectTo` (OAuth) using your site's current address rather than a hard-coded localhost.

## Paste this into your AI
> After deploying, Supabase auth redirects users to localhost. Find every place this project sets a redirect URL for sign-in, sign-up, magic links or password reset, and change them to use the current site's origin. Then tell me exactly what to set as Site URL and Redirect URLs in Supabase.

## Still broken?
Old magic-link emails still contain the old address. Request a new link after changing the settings.
