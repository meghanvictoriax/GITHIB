# Flow 5: Welcome series (v3)

**Klaviyo:** draft flow `WXaimu` (https://www.klaviyo.com/flow/WXaimu/edit).
**Templates (drag-and-drop, used by the flow):** WkxUsh, UNmMYT, TdzrkC, Usxwx9, SAUnJU, TJbdxi (emails 1–6). Built by `build_dnd.py`; photos live in Klaviyo's image library.
The older coded versions (WvL4NV, WsGNi4, VNzXxr, Yqpcvj, S5ztXF, VzMYDf) are kept for reference only.

**Editing:** open the flow, click an email, then Edit content. Everything is drag-and-drop now: click text to change it, swap photos, drag sections. Once you edit in Klaviyo, Klaviyo is the source of truth; re-running `build_dnd.py` would overwrite your edits.
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
| 3 | +2 days (day 3) | Founder story + reviews | the pair I couldn't find | Why I started SOL KYST, and your 15% is still here. | Meghan at SOL KYST |
| 4 | +1 day (day 4) | Ours vs. theirs | Why your sunglasses pinch (it's not your face) | Standard frames come in one size. You don't. | SOL KYST |
| 5 | +2 days (day 6) | Start here | Not sure where to start? | Four pairs, four moods. Start with one. | SOL KYST |
| 6 | +3 days (day 9) | Note from Meghan (plain text) | still thinking it over? | Your 15% is still here. And a quick question. | Meghan at SOL KYST |

**Smart Sending** is off for email 1 only, so the code always arrives. Every later email is at least 16 hours after the one before.

**Klaviyo copies templates into the flow.** After editing an original template, re-attach it to the flow email (update its template_id) so the flow gets a fresh copy.

## Copy rules
- No fake urgency: the code has no end date, so no "expires" language.
- Only sourced claims: sizes 135/145/158, acetate, polarized + UV400, free exchanges for 45 days, ReturnBear, free shipping over $150, always duty-free to CA & US, the Dragons' Den deal (two Dragons wanted in; Dragons not named), $10,000+ launch day after the March 2021 TikTok. Full fact sheet: `../BRAND.md`.
- Reviews are real 5-star Loox reviews, quoted word for word from the product pages: Melina T. (Integrity), Mary H. (Monarch), Midori P. (Monarch), Jennifer K. (Integrity).

## Before switching on
- [ ] Decide what happens to the live welcome flow (`Xs46zf`, one email, no coupon). Two flows on the same list would double-send.
- [ ] Meghan to read emails 3 and 6 (rewritten using `VOICE.md`) and flag anything that doesn't sound like her.
- [ ] Optional: swap the email 3 photo for one of Meghan. It currently reuses the friends photo from email 5.
- [ ] Send yourself a test of each email.

Builders: `build_welcome.py` (email 1) and `build_welcome_flow.py` (emails 2–6). Previews: `welcome-flow-previews/`.

## Mobile formatting (Oct 15)
Klaviyo forces body text to 14px / 1.3 line-height on phones, which made the emails look squished. `mobile_fix.py` takes the flow versions (with Meghan's edits) and:
- sets inline `line-height:1.6; font-size:16px` on paragraphs that didn't specify them,
- caps section side padding at 24px (was up to 56px),
- stops table cells breaking words mid-way ("FRAM-E", "Oversi-zed") and tightens cell padding,
- eases letter-spacing on the 3-column trust row.
Fixed versions were pushed to the standalone templates and re-attached to flow WXaimu. Flow copies now: UgMeNB, RwPhhV, WS5VER, SS5SUV, TZtHEg, UJzxCg (email 6 unchanged).
