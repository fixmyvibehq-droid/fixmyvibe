---
title: "duplicate key value violates unique constraint"
error: "duplicate key value violates unique constraint"
category: Database & auth
tools: [Supabase, Postgres, Prisma, Lovable, Bolt]
heading: '"duplicate key value violates unique constraint" (Postgres error 23505)'
last_checked: 2026-10-18
---


## What it means
You tried to add a row with a value that must be unique, like an id, email or username, and a row with that value already exists. The error message names the constraint, which tells you which column it is.

## Why AI tools cause it
- **The insert runs twice**: a double click, or a React effect firing twice in development.
- **A "create profile" step on every login**, not just the first, so the second login fails.
- **A database trigger already created the row** (common with Supabase profile tables), then your code tries to insert it again.
- **Ids typed in by hand** in seed data, so the automatic counter later hands out an id that's already taken.

## The fix
1. Read the constraint name in the error, e.g. `profiles_pkey` or `users_email_key`, to see which column clashed.
2. If the row might already exist, use an upsert instead of an insert: `.upsert(row, { onConflict: 'id' })` in Supabase.
3. Disable submit buttons while saving so one click means one insert.
4. If you have a trigger that creates profiles, remove the duplicate insert from your app code.

## Paste this into your AI
> My insert fails with 'duplicate key value violates unique constraint "<constraint name>"'. Find where this row is created, check whether a database trigger or a second code path also creates it, and change the code to an upsert or a check-then-insert so it can safely run more than once. Also stop double submits on the form.

## Still broken?
If it's the primary key on a table you seeded by hand, the id counter is behind. Ask your AI for the `setval` SQL to move the sequence past your highest id.
