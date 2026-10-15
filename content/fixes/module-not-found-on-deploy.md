---
title: "Module not found: Can't resolve"
error: "Module not found: Can't resolve"
category: Build
tools: [Vercel, Netlify, Next.js, Vite, Cursor]
heading: '"Module not found: Can''t resolve" — builds locally, fails on deploy'
last_checked: 2026-10-15
---


## What it means
The build can't find a file or package your code imports.

## Why AI tools cause it
Three usual suspects:
- **Letter case.** Your import says `./components/Button` but the file is `button.tsx`. Mac and Windows ignore case; the Linux servers your host builds on don't.
- **A package that isn't installed.** The AI wrote an import but never added the package to `package.json`.
- **A file that was never committed**, so it exists on your machine but not in your repo.

## The fix
1. Read the error: it names the exact import that failed.
2. Check the file name's capital letters match the import exactly. To rename only the case in git, use `git mv button.tsx Button.tsx`.
3. If it's a package, install it (`npm install <name>`) and commit `package.json` and the lock file.
4. Run `git status` to check nothing important is uncommitted.

## Paste this into your AI
> My deploy fails with "Module not found: Can't resolve <paste the path>". Check every import in this project matches the real file name, including capital letters, and list any imported packages missing from package.json.

## Still broken?
Clear your host's build cache and redeploy.
