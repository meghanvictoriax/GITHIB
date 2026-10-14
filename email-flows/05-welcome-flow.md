# Flow 5: Welcome series (v2)

**Klaviyo:** draft flow `XaWmir` (https://www.klaviyo.com/flow/XaWmir/edit). Templates: WvL4NV, Yqpcvj, WsGNi4, S5ztXF, VzMYDf.
**Trigger:** added to the newsletter list (`YxzPdw`), the same list as the live "Email Welcome Series Customer vs Non-Customer" flow.
**Flow filter:** Placed Order = 0 since starting this flow, so anyone who buys stops getting the series.
**Code:** `kystfortheveryfirsttime` (live in Shopify: 15% off, one use per customer, no end date). Every button applies it automatically through `/discount/<code>`.
**Inspiration:** Mave & Chez (email 1 layout) and KENT's welcome series (emails 2–4: ours-vs-theirs chart, fit guarantee, curated "start here" picks, code reminder in every email).

| # | When | Email | Subject (A / B) | Preview | Job |
|---|---|---|---|---|---|
| 1 | Right away | Offer + Dragons' Den | Welcome. Here's 15% off your first pair / You're in. 15% off is inside | Sunglasses built for wide faces | Deliver the code, prove it with the Den |
| 2 | +1 day | Ours vs. theirs | Why your sunglasses pinch (it's not your face) / Standard sunglasses vs. ours | Standard frames come in one size. You don't. | Comparison chart: the reason to buy |
| 3 | +2 days | Find your fit | Which size are you? (30-second test) / Mini, Midi or Wide? | A 30-second test with a pair you already own | Remove size anxiety + "not in love? no sweat" exchange promise |
| 4 | +2 days | Start here | Not sure where to start? / The pairs everyone starts with | Four pairs, four moods. Start with one. | Curated picks by vibe + what's in the box |
| 5 | +3 days | Note from Meghan | still thinking it over? / a quick question from me | Your 15% is still here. And a quick question. | Plain-text founder note, asks for replies |

Email 5 sends from **Meghan at SOL KYST**. The rest send from **SOL KYST** (`customer@solkyst.ca`).

## Copy rules
- No fake urgency: the code has no end date, so no "expires" language.
- Only sourced claims: sizes 135/145/158, acetate, polarized + UV400, free exchanges for 45 days, ReturnBear, free shipping and duty-free over $150, Dragons' Den deal (two Dragons wanted in, Dragons not named), Sweet Heart #2 by net sales.

## Before switching on
- [ ] Decide what happens to the live welcome flow (`Xs46zf`, one email, no coupon). Two flows on the same list would double-send.
- [ ] Send yourself a test of each email.
- [ ] Optional: Instagram/TikTok links in the footer (handles needed).

Builders: `build_welcome.py` (email 1) and `build_welcome_flow.py` (emails 2–5). Previews: `welcome-flow-previews/`.
