---
title: "No such price"
error: "No such price: 'price_...'"
category: Payments
tools: [Stripe, Next.js, Lovable, Bolt, Vercel]
heading: '"No such price" when creating a Stripe Checkout'
last_checked: 2026-10-18
---


## What it means
Your code asked Stripe to sell a price id that Stripe can't find with the key you're using.

## Why AI tools cause it
- **Test and live mix-up.** By far the most common one. Prices made in test mode don't exist in live mode, and the other way round. A live key plus a test price (or a test key plus a live price) gives this error.
- **A made-up id.** The AI wrote a placeholder like `price_123` and it was never replaced.
- **Wrong Stripe account**, if you have more than one.
- **A product id (`prod_...`) used where a price id (`price_...`) is needed.**

## The fix
1. In Stripe, open **Product catalog**, click the product, and copy the price id. It starts with `price_`.
2. Check the account and environment picker at the top of the Stripe dashboard: are you in a sandbox, test mode or live mode? Your secret key must come from the same place. Test and sandbox keys start `sk_test_`, live keys `sk_live_`. A price made in one doesn't exist in the others.
3. When you go live, recreate the product in live mode (or copy it from test mode) and put the new live price id in your live environment variables.
4. Keep price ids in environment variables, not in code, so test and live can differ.

## Paste this into your AI
> My Stripe Checkout fails with "No such price". Move every Stripe price id out of the code into environment variables, check each one starts with price_ (not prod_), and add a startup check that warns me if a live secret key (sk_live_) is used with prices from test mode.

## Still broken?
If you sell with Stripe Payment Links instead, there are no price ids in your code at all. Just check the link was made in live mode.
