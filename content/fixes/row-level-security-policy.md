---
title: "new row violates row-level security policy"
error: "new row violates row-level security policy for table"
category: Database & auth
tools: [Supabase, Lovable, Bolt, Cursor]
heading: '"new row violates row-level security policy" in Supabase'
last_checked: 2026-10-15
---


## What it means
Row Level Security (RLS) is switched on for the table, which is good. But no policy says this user is allowed to insert this row, so Supabase blocks it.

## Why AI tools cause it
AI tools often turn RLS on (or you did, after a security warning) without writing the matching policies. Or the insert doesn't include the `user_id` the policy checks for.

## The fix
1. In Supabase, open **Authentication → Policies** and find the table.
2. Add an **INSERT** policy that lets signed-in users add rows they own, for example `with check (auth.uid() = user_id)`.
3. Make sure your insert sends the user's id in the `user_id` column, and that the user is actually signed in when it runs.

**Don't** fix this by turning RLS off. That makes the table readable and writable by anyone with your public key.

## Paste this into your AI
> Inserting into my Supabase table fails with "new row violates row-level security policy". Show me the RLS policies this table needs so users can create, read, update and delete only their own rows, as SQL I can run, and check my insert code sends user_id from the signed-in session.

## Still broken?
If it fails on a server route, check whether that code is using a signed-in client or an anonymous one. An anonymous client has no `auth.uid()`.
