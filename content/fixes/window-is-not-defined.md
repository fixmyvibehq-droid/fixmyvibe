---
title: "ReferenceError: window is not defined"
error: "ReferenceError: window is not defined"
category: Frontend
tools: [Next.js, Remix, SvelteKit, Cursor, v0]
heading: '"window is not defined" (or "document" / "localStorage is not defined")'
last_checked: 2026-10-15
---


## What it means
Code that only exists in a browser ran on the server, where there's no `window`, `document` or `localStorage`.

## Why AI tools cause it
Frameworks like Next.js render pages on the server first. AI-generated code often reads `window` or `localStorage` at the top of a file or during render, which runs on the server too. Some browser-only libraries (maps, charts, rich text editors) do this internally.

## The fix
1. Move browser-only code into `useEffect`, which runs only in the browser.
2. For a quick check elsewhere, guard it: `if (typeof window !== 'undefined') { ... }`.
3. For a browser-only library or component, load it with `dynamic(() => import('./Map'), { ssr: false })` in Next.js.

## Paste this into your AI
> My app crashes with "window is not defined" during server rendering. Find every use of window, document, localStorage and browser-only libraries in this project and make each run only in the browser, without disabling server rendering for whole pages.

## Still broken?
The stack trace names the file. If it's inside `node_modules`, that library is browser-only: load it with `ssr: false`.
