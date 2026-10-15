# Flow 5: Welcome series (v3)

**Klaviyo:** draft flow `WXaimu` (https://www.klaviyo.com/flow/WXaimu/edit). Templates: WvL4NV, WsGNi4, VNzXxr, Yqpcvj, S5ztXF, VzMYDf.
The earlier draft `XaWmir` (v2, 5 emails over 8 days) is superseded. Delete it once v3 is approved.
**Trigger:** added to the newsletter list (`YxzPdw`), the same list as the live "Email Welcome Series Customer vs Non-Customer" flow.
**Flow filter:** Placed Order = 0 since starting this flow, so anyone who buys stops getting the series.
**Code:** `kystfortheveryfirsttime` (live in Shopify: 15% off, one use per customer, no end date). Every button applies it automatically through `/discount/<code>`.

## Inspiration
- **Mave & Chez** sent 3 emails in the first ~10 hours after signup: the offer, then an interactive "bend test" (~6h), then a founder story with a code reminder and customer reviews (~4h later). Emails 1–3 copy that order (offer → test → founder story), but at a slower pace that suits SOL KYST better: next morning, then day 3.
- **KENT** (days 2–6): ours-vs-theirs chart, curated "start here" picks, a code reminder in every email.

| # | When | Email | Subject | Preview | From |
|---|---|---|---|---|---|
| 1 | Right away | Offer + Dragons' Den | Welcome. Here's 15% off your first pair | Sunglasses built for wide faces | SOL KYST |
| 2 | +18 hours (next morning) | The 30-second test | Do your sunglasses pass the 30-second test? | Grab the pair you wore today. Bet we know how this ends. | SOL KYST |
| 3 | +2 days (day 3) | Founder story + reviews | Why I built SOL KYST (and why it matters to you) | Why I started SOL KYST. Plus, your 15% is still waiting. | Meghan at SOL KYST |
| 4 | +1 day (day 4) | Ours vs. theirs | Why your sunglasses pinch (it's not your face) | Standard frames come in one size. You don't. | SOL KYST |
| 5 | +2 days (day 6) | Start here | Not sure where to start? | Four pairs, four moods. Start with one. | SOL KYST |
| 6 | +3 days (day 9) | Note from Meghan (plain text) | still thinking it over? | Your 15% is still here. And a quick question. | Meghan at SOL KYST |

**Smart Sending** is off for email 1 only, so the code always arrives. Every later email is at least 16 hours after the one before.

**Klaviyo copies templates into the flow.** Editing the original templates won't change the flow emails; the flow's copies must be updated too.

## Copy rules
- No fake urgency: the code has no end date, so no "expires" language.
- Only sourced claims: sizes 135/145/158, acetate, polarized + UV400, free exchanges for 45 days, ReturnBear, free shipping and duty-free over $150, the Dragons' Den deal (two Dragons wanted in; Dragons not named), $10,000 pre-order in 24 hours.
- Reviews are real 5-star Loox reviews, quoted word for word from the product pages: Melina T. (Integrity), Mary H. (Monarch), Midori P. (Monarch), Jennifer K. (Integrity).

## Before switching on
- [ ] Decide what happens to the live welcome flow (`Xs46zf`, one email, no coupon). Two flows on the same list would double-send.
- [ ] Rewrite emails 3 and 6 in Meghan's real voice (waiting on writing samples).
- [ ] Optional: swap the email 3 photo for one of Meghan. It currently reuses the friends photo from email 5.
- [ ] Send yourself a test of each email.

Builders: `build_welcome.py` (email 1) and `build_welcome_flow.py` (emails 2–6). Previews: `welcome-flow-previews/`.
