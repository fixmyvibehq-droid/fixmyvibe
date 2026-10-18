---
title: "Email not confirmed"
error: "AuthApiError: Email not confirmed"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Cursor]
heading: '"Email not confirmed" when logging in with Supabase'
last_checked: 2026-10-18
---


## What it means
The account exists, but the user hasn't clicked the link in their confirmation email yet. Supabase won't let them log in until they do.

## Why AI tools cause it
The AI built a sign-up form but never told the user to check their inbox. Often the email never arrived at all: Supabase's built-in email service only sends to members of your Supabase team and only 2 emails an hour, so real users don't get them.

## The fix
1. After sign-up, show a clear "Check your email to confirm your account" message instead of sending the user straight to the login page.
2. For real users, set up your own email sender: **Authentication → Emails → SMTP Settings** (any provider such as Resend, Postmark or Brevo works).
3. Check the confirmation link points at your live site, not `localhost` (set **Site URL** under **Authentication → URL Configuration**).
4. To unblock one person now, run this in the **SQL Editor**: `update auth.users set email_confirmed_at = now() where email = 'their@email.com';`

Only switch off **Confirm email** if you're happy for anyone to sign up with an address they don't own.

## Paste this into your AI
> Users see "Email not confirmed" when logging in to my Supabase app. After sign-up, show a "check your email" screen with a button that resends the confirmation using supabase.auth.resend. On the login page, catch this error and show a friendly message with the same resend button.

## Still broken?
If emails still don't arrive after adding SMTP, check your email provider's logs and spam folders, and make sure your sending domain is verified with them.
