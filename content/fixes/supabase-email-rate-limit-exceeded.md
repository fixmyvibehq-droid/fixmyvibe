---
title: "Email rate limit exceeded"
error: "AuthApiError: email rate limit exceeded"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Cursor]
heading: '"email rate limit exceeded" in Supabase Auth'
last_checked: 2026-10-18
---


## What it means
Supabase has sent as many auth emails (sign-up confirmations, magic links, password resets) as it's allowed to in this window, so it refuses to send more for now.

## Why AI tools cause it
Supabase's built-in email service is only for testing: it allows 2 emails an hour for your whole project. A couple of test sign-ups use it up. Paying for a bigger Supabase plan doesn't raise it. Code that sends a magic link on every keystroke or retry burns through it even faster.

## The fix
1. Set up your own email sender in **Authentication → Emails → SMTP Settings**. Any SMTP provider works (Resend, Postmark, Brevo and others have free tiers).
2. Once that's saved, raise the limit if you need to under **Authentication → Rate Limits**.
3. Make sure your code only sends one email per button press, and disable the button while it's sending.
4. There is also a 60-second wait per user between resends, so tell the user to wait a minute rather than letting them hammer the button.

## Paste this into your AI
> Supabase gives "email rate limit exceeded". Check my sign-up, magic link and password reset code: make sure each sends exactly one email per click, disable the button while the request runs, and show a friendly "please wait a minute and try again" message when this error comes back.

## Still broken?
While you set up SMTP, test with accounts you create by hand in **Authentication → Users** (tick auto-confirm) so you don't need emails at all.
