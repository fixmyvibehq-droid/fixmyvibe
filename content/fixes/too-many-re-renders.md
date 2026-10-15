---
title: "Too many re-renders"
error: "Too many re-renders. React limits the number of renders to prevent an infinite loop."
category: Frontend
tools: [React, Next.js, Lovable, v0]
heading: '"Too many re-renders" in React'
last_checked: 2026-10-15
---


## What it means
A component updates its own state every time it renders, which makes it render again, forever. React stops it and throws this error.

## Why AI tools cause it
Two patterns cause nearly all of these:
- **Calling a function instead of passing it.** `onClick={setOpen(true)}` runs immediately on every render. It should be `onClick={() => setOpen(true)}`.
- **Setting state directly in the component body** instead of inside an event or `useEffect`.

## The fix
1. Look at every `onClick`, `onChange` and similar prop. If it has `(...)` right after a function name, wrap it in `() => ...`.
2. Move any `setSomething(...)` that sits loose in the component body into an event handler or a `useEffect` with the right dependencies.

## Paste this into your AI
> My React component crashes with "Too many re-renders". Find any state update that runs during render, including event props that call a function instead of passing one, and fix them.

## Still broken?
If it's a `useEffect` that keeps firing, check its dependency list. An object or array created during render counts as "changed" every time.
