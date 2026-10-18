---
title: "Cannot read properties of undefined"
error: "TypeError: Cannot read properties of undefined (reading 'map')"
category: Frontend
tools: [React, Next.js, Lovable, Bolt, v0, Cursor]
heading: '"Cannot read properties of undefined (reading ''map'')"'
last_checked: 2026-10-18
---


## What it means
Your code tried to use something, like a list it wanted to loop through with `.map`, before it existed. The word in brackets (`'map'`, `'length'`, `'name'`) is what it was trying to read.

## Why AI tools cause it
- **Data hasn't loaded yet.** The page draws before the database or API answers, so on the first render the list is `undefined`.
- **The data has a different shape** than the AI assumed: it expected `data.items` but the API returns the list directly, or an error object.
- **Nothing came back** because a request failed or the user isn't signed in.

## The fix
1. Start lists as empty, not undefined: `useState([])` rather than `useState()`.
2. Use optional chaining for data that might be missing: `items?.map(...)`, `user?.name`.
3. Show a loading state until the data has arrived, and an error message if it fails.
4. `console.log` the data right after you fetch it and check its real shape matches what your code expects.

## Paste this into your AI
> My page crashes with "Cannot read properties of undefined (reading '<word>')". Find where this value comes from, log the real shape of the data, and fix the component so it shows a loading state while data loads, an error message if it fails, and an empty state if the list is empty. Don't just hide the error with optional chaining everywhere.

## Still broken?
If it only happens on the live site, the request is probably failing there. Check the browser console for an error just before this one.
