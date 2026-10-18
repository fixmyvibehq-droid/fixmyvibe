---
title: "Objects are not valid as a React child"
error: "Objects are not valid as a React child"
category: Frontend
tools: [React, Next.js, Lovable, Bolt, v0]
heading: '"Objects are not valid as a React child"'
last_checked: 2026-10-18
---


## What it means
React can show text, numbers and other components on the page, but not a whole object. Somewhere you've put `{something}` in your JSX where `something` is an object, like `{user}` instead of `{user.name}`.

## Why AI tools cause it
- **An error object shown directly**: `{error}` instead of `{error.message}`.
- **A date object** from the database shown without formatting.
- **The API's shape changed** and a field that used to be text is now an object (e.g. `author` became `{ id, name }`).
- **An async component or a Promise** dropped into regular React code.

## The fix
1. The error message lists the object's keys, e.g. "found: object with keys {id, name}". Search your code for where that object is rendered.
2. Show the specific field instead: `{author.name}`, `{error.message}`.
3. Format dates first: `{new Date(created_at).toLocaleDateString()}`.
4. To show a whole object while debugging, use `{JSON.stringify(obj)}`.

## Paste this into your AI
> React throws "Objects are not valid as a React child (found: object with keys {<paste keys>})". Find where this object is rendered in JSX and change it to show the right field as text. Check other places in the same component for the same mistake.

## Still broken?
If the message says `found: [object Promise]`, you're rendering a Promise (often an `async` component used inside client code). Load the data in an effect or a server component and render the result once it arrives.
