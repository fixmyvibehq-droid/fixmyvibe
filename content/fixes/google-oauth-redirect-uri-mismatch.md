---
title: "Google sign-in: redirect_uri_mismatch"
error: "Error 400: redirect_uri_mismatch"
category: Database & auth
tools: [Supabase, Google, Next.js, Lovable, Bolt]
heading: '"Error 400: redirect_uri_mismatch" on Google sign-in'
last_checked: 2026-10-18
---


## What it means
Google only sends users back to addresses you've approved in advance. The address your app asked to return to isn't on that list, so Google stops at an error page.

## Why AI tools cause it
- **Supabase's callback address was never added.** With Supabase Auth, Google returns users to Supabase first, not to your site.
- **Only `localhost` was added**, so it works in development but not live.
- **Tiny differences**: `http` vs `https`, `www` vs no `www`, or a trailing slash all count as different addresses.

## The fix
1. In Supabase, open **Authentication → Sign In / Providers → Google** and copy the **Callback URL**. It looks like `https://<your-project>.supabase.co/auth/v1/callback`.
2. In Google Cloud Console, open **Google Auth Platform → Clients** (also reachable via APIs & Services → Credentials), click your OAuth client, and paste that exact address into **Authorized redirect URIs**. Save.
3. Add your live site address (e.g. `https://yourapp.com`) under **Authorized JavaScript origins**.
4. Back in Supabase, add your live site to **Authentication → URL Configuration → Redirect URLs** so users land on your site afterwards.
5. Google says changes can take from 5 minutes to a few hours to apply. Try again in a private window.

## Paste this into your AI
> Google sign-in fails with "Error 400: redirect_uri_mismatch". My app uses <Supabase / NextAuth / other>. Tell me exactly which redirect URIs and JavaScript origins I need in Google Cloud Console for both local development and my live domain <your domain>, and check my sign-in code passes the right redirectTo.

## Still broken?
Google's error page has a "see error details" link showing the exact address that was rejected. Copy it character for character into Google Cloud.
