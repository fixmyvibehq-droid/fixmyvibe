---
title: "Command \"npm run build\" exited with 1"
error: "Error: Command \"npm run build\" exited with 1"
category: Build
tools: [Vercel, Next.js, Vite, Lovable, Bolt, Cursor]
heading: 'Vercel deploy fails: Command "npm run build" exited with 1'
last_checked: 2026-10-18
---


## What it means
"Exited with 1" just means the build failed. It isn't the real error. The real one is a few lines higher up in the build log.

## Why AI tools cause it
- **Type errors.** TypeScript checks run during the build and stop it, even if the app looked fine in development.
- **Lint errors** stop some builds (older Next.js versions and some Vite setups run a linter during build).
- **A missing file or package**: see our "Module not found" fix.
- **A missing environment variable** that the code reads while building.
- **A different Node version** on Vercel than on your computer.

## The fix
1. In Vercel, open the failed deployment and scroll the **Build Logs** up from the bottom to the first red error. That's the one to fix.
2. Run `npm run build` on your own computer. It should fail the same way, so you can fix it faster.
3. Fix the error it names. Don't switch off type checking to get past it: those errors usually point at real bugs.
4. If it's about an environment variable, add it in **Settings → Environment Variables** and redeploy.
5. If it mentions Node, set the same major version in **Settings → Build and Deployment → Node.js Version**, or add `"engines": { "node": "24.x" }` to package.json (this overrides the setting). Vercel only supports recent Node versions, so if yours is older locally, upgrade it.

## Paste this into your AI
> My Vercel deploy fails with 'Command "npm run build" exited with 1'. Here is the first error in the build log: <paste it>. Fix the cause properly, without disabling TypeScript or lint checks, then run npm run build locally and confirm it passes.

## Still broken?
If it builds locally but not on Vercel, clear the build cache: redeploy and untick **Use existing Build Cache**.
