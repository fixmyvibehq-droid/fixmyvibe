---
title: "Invalid login credentials"
error: "AuthApiError: Invalid login credentials"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Cursor]
heading: '"Invalid login credentials" in Supabase Auth'
last_checked: 2026-10-18
---


## What it means
Supabase couldn't match the email and password to an account. Either the password is wrong, or no account with that email exists in this project.

## Why AI tools cause it
- **Wrong project.** Your app points at one Supabase project (say, a test one) but you signed up in another. Check the URL in your environment variables.
- **The user signed up with Google or a magic link**, so there is no password to log in with.
- **The sign-up never actually finished**, often because the AI's sign-up form swallowed an error.
- **Stray spaces or capital letters** in the email from the form.

## The fix
1. In Supabase, open **Authentication → Users** and search for the email. If it isn't there, the account doesn't exist in this project.
2. Compare the project URL in your app's environment variables with the one in your browser's address bar on the Supabase dashboard.
3. If the user exists but signed up another way, have them use that method, or send a password reset.
4. Trim spaces from the email before calling `signInWithPassword`.

## Paste this into your AI
> Supabase login fails with "Invalid login credentials". Check my sign-up and login code: trim and lowercase the email, show any error from sign-up to the user instead of hiding it, and confirm both forms use the same Supabase client and environment variables. Add a "Forgot password" link using resetPasswordForEmail.

## Still broken?
If the account exists and the password is definitely right, check whether email confirmation is switched on. Unconfirmed accounts give a different error: "Email not confirmed".
