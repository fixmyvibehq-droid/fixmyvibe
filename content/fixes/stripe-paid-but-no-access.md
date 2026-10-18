---
title: "Customer paid but didn't get access"
error: "Payment succeeded but user not upgraded"
category: Payments
tools: [Stripe, Supabase, Next.js, Lovable, Bolt]
heading: 'Customer paid on Stripe but didn''t get access in your app'
last_checked: 2026-10-18
---


## What it means
Stripe took the money, but your app never found out, so the customer's account still looks unpaid. It's one of the most common complaints about vibe-coded apps, and the fastest way to get refund requests.

## Why AI tools cause it
- **The upgrade only happens on the "success" page.** If the customer closes the tab, or their connection drops, the code never runs. Anyone who finds that URL can also upgrade themselves for free.
- **No webhook**, or a webhook still pointing at `localhost` or a test-mode endpoint.
- **The webhook can't tell which user paid**, because no user id or email was attached to the checkout.
- **The webhook crashes** on a signature error or a database permission error, and nobody looks.

## The fix
1. Grant access from a Stripe webhook listening for `checkout.session.completed`, but only when the session's `payment_status` is `paid`. Also listen for `checkout.session.async_payment_succeeded` to catch slower payment methods like bank debits. For subscriptions, remove access on `customer.subscription.deleted`. Never grant access from the success page alone.
2. When creating the checkout, pass the user's id as `client_reference_id` (or in `metadata`) so the webhook knows who to upgrade.
3. In Stripe, open **Workbench → Webhooks** (in live mode), click your endpoint, check its URL is your live site, and open **Event deliveries**. Failed deliveries show the error, and you can click **Resend**.
4. The webhook writes to your database as a server, so use a server-side key there (for example Supabase's secret / service_role key), not the user's session. Keep that key only in server environment variables, never with a `NEXT_PUBLIC_` or `VITE_` prefix.
5. For anyone already stuck, upgrade them by hand and send a short apology.

## Paste this into your AI
> Customers pay with Stripe but sometimes don't get access. Move the "grant access" logic into a Stripe webhook for checkout.session.completed (only when payment_status is paid) and checkout.session.async_payment_succeeded that verifies the signature, finds the user from client_reference_id, and updates their account. Make it safe to receive the same event twice. The success page should only show a message, never grant access.

## Still broken?
If the webhook shows "No signatures found", see our fix for that error. If it shows a 307 or 308 redirect, your endpoint URL is missing or adding `www` or a trailing slash. Copy the exact final URL into Stripe.
