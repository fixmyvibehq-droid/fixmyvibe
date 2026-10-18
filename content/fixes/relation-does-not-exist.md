---
title: "relation does not exist"
error: "relation \"public.table_name\" does not exist"
category: Database & auth
tools: [Supabase, Postgres, Prisma, Drizzle, Lovable, Bolt]
heading: '"relation does not exist" (Postgres error 42P01)'
last_checked: 2026-10-18
---


## What it means
"Relation" is Postgres's word for a table. Your code asked for a table the database doesn't have. Through the Supabase client, the same problem usually shows up as `Could not find the table 'public.<name>' in the schema cache` (code PGRST205).

## Why AI tools cause it
- **The AI wrote the code but never ran the SQL** that creates the table. Or it wrote a migration file that was never applied.
- **Different databases.** The table exists in your local or test database but not in the production one your live site uses.
- **Spelling or capitals.** `Profiles` and `profiles` are different tables to Postgres if the name was created in quotes.
- **Wrong schema.** The table lives somewhere other than `public`.

## The fix
1. In Supabase, open the **Table Editor** and check the table is really there, with exactly that name.
2. If it's missing, find the `create table` SQL (often in a `supabase/migrations` folder) and run it in the **SQL Editor**, or ask your AI to write it.
3. If you use Prisma or Drizzle, run their migrate command against the production database URL.
4. Make your code use the exact name, ideally all lower case.

## Paste this into your AI
> My app fails with 'relation "<table name>" does not exist'. List every table my code reads from or writes to, compare it with the tables and migrations in this project, and give me one SQL script I can run in the Supabase SQL Editor to create anything missing, with row-level security switched on and sensible policies.

## Still broken?
If the table exists but the error remains, the user may not have permission to see it. Check grants and RLS policies, then reload the schema cache by running `notify pgrst, 'reload schema';` in the SQL Editor.
