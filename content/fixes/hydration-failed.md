---
title: "Hydration failed"
error: "Hydration failed because the server rendered HTML didn't match the client"
category: Frontend
tools: [Next.js, React, Cursor, v0]
heading: '"Hydration failed" in Next.js'
last_checked: 2026-10-15
---


## What it means
Next.js renders your page on the server, then React takes it over in the browser. The two versions came out different, so React complained. Older versions word it as "the initial UI does not match what was rendered on the server".

## Why AI tools cause it
AI code often uses things that differ between server and browser while the page first renders:
- the current time or date (`new Date()`), or random values (`Math.random()`)
- browser-only things like `window`, `localStorage` or screen size
- invalid HTML nesting, such as a `<div>` inside a `<p>`, or a link inside a link

Browser extensions that edit the page can also trigger it. Test in a private window to rule them out.

## The fix
1. Move browser-only or changing values into `useEffect`, so they're set after the page loads.
2. For a component that can only work in the browser, load it with `dynamic(() => import('./Thing'), { ssr: false })`.
3. Fix any invalid nesting the error points to.

## Paste this into your AI
> My Next.js page throws a hydration error. Find anything in this component and its children that renders differently on the server and in the browser (dates, random values, window or localStorage, invalid HTML nesting), and fix it without turning off server rendering for the whole page.

## Still broken?
In development, the error overlay shows the exact element that differed. Start there.
