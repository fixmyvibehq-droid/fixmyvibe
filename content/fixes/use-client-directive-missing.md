---
title: "This React Hook only works in a Client Component"
error: "You're importing a component that needs useState. This React Hook only works in a Client Component."
category: Frontend
tools: [Next.js, React, v0, Cursor]
heading: '"needs useState... only works in a Client Component" in Next.js'
last_checked: 2026-10-18
---


## What it means
In the Next.js App Router, components run on the server by default. Server components can't use things that need a browser, like `useState`, `useEffect`, `onClick` or `window`. To use them, the file must be marked as a client component.

## Why AI tools cause it
AI tools mix code from the old Pages Router (where everything could use hooks) with the newer App Router, or add a button with `onClick` to a server page without marking it.

## The fix
1. Open the file named in the error.
2. Add `'use client'` as the very first line, above the imports.
3. Keep it small: put the interactive part (the button, the form) in its own client component and import it into the server page, rather than marking the whole page as client.
4. Don't add `'use client'` to files that use `async` components or read secrets on the server.

## Paste this into your AI
> Next.js says "You're importing a component that needs useState. This React Hook only works in a Client Component." Find the components that need browser features, move the interactive parts into small client components with 'use client' at the top, and keep data loading and secrets in server components.

## Still broken?
If the error mentions `next/router`, switch to `next/navigation`, which is what the App Router uses.
