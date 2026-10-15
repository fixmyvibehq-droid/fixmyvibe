---
title: "npm ERESOLVE unable to resolve dependency tree"
error: "npm ERR! ERESOLVE unable to resolve dependency tree"
category: Build
tools: [npm, Vercel, Netlify, Replit, Cursor]
heading: '"ERESOLVE unable to resolve dependency tree"'
last_checked: 2026-10-15
---


## What it means
Two of your packages want different versions of a shared package (often React), and npm refuses to guess.

## Why AI tools cause it
AI tools install packages from older tutorials alongside newer ones. A library that only supports React 18 meets a project on React 19, for example.

## The fix
1. Read the error. It names the package that wants the older version (look for "Could not resolve dependency" and "peer").
2. Best fix: upgrade that package to a version that supports your setup (`npm install <package>@latest`).
3. If there's no compatible version yet, install with `npm install --legacy-peer-deps`. To make your host do the same, add a `.npmrc` file containing `legacy-peer-deps=true` and commit it.

Treat option 3 as a workaround: it hides the warning, and the package may still misbehave.

## Paste this into your AI
> npm install fails with ERESOLVE. Here is the full error: <paste it>. Tell me which package conflicts with which, whether a newer compatible version exists, and the safest fix.

## Still broken?
Delete `node_modules` and `package-lock.json`, then run `npm install` again so the lock file is rebuilt cleanly. Commit the new lock file.
