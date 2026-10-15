---
title: "No signatures found matching the expected signature for payload"
error: "No signatures found matching the expected signature for payload"
category: Payments
tools: [Stripe, Next.js, Express, Vercel]
heading: 'Stripe webhook: "No signatures found matching the expected signature"'
last_checked: 2026-10-15
---


## What it means
Stripe signs every webhook so you know it's genuine. Your check failed, so your code rejected the event. Result: people pay, but your app never hears about it ("charged but no access").

## Why AI tools cause it
Two causes cover almost every case:
- **The body was changed before checking.** Signature checks need the exact raw request body. Frameworks often parse it into JSON first, which breaks the check.
- **Wrong signing secret.** The `whsec_...` secret from the Stripe CLI (local testing) is different from the one for your live webhook endpoint in the Stripe dashboard.

## The fix
1. Pass the raw body to `stripe.webhooks.constructEvent`. In Next.js App Router, use `await req.text()`, not `req.json()`. In Express, use `express.raw({ type: 'application/json' })` on the webhook route.
2. Copy the signing secret from the specific endpoint in **Stripe → Developers → Webhooks** and set it as an environment variable on your host. Redeploy.
3. Test and live mode each have their own secret. Use the one that matches.

## Paste this into your AI
> My Stripe webhook fails with "No signatures found matching the expected signature for payload". Rewrite the handler so it verifies the signature using the raw request body for this framework, reads the signing secret from an environment variable, and returns 400 on failure and 200 on success.

## Still broken?
In the Stripe dashboard, open the endpoint and look at a failed delivery. It shows exactly what your server replied.
