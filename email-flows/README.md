# SOL KYST: Email Flow Drafts (v2)

Four new flows to fill the gaps around the ones already live in Klaviyo.

## Already live (not touched)

| Flow | Trigger |
|---|---|
| Email Welcome Series Customer vs Non-Customer | Added to List |
| Abandoned Cart ("We saw you checking us out 🤭" → "Final offer miss playing hard to get 😆") | Checkout Started |
| Browse Abandonment | Viewed Product |
| Winback final | Added to List |
| Review request | *draft* |

## New flows

| # | Flow | Trigger | The one job | File |
|---|---|---|---|---|
| 1 | Added to Cart | Added to Cart | Remove fit uncertainty, then justify the price. **No discount.** | [01](01-added-to-cart.md) |
| 2 | Post-Purchase | Placed Order | Founder thank-you → stop fit returns → sell pair #2 by size | [02](02-post-purchase.md) |
| 3 | Back in Stock | Back in Stock | Speed + "your size goes first" | [03](03-back-in-stock.md) |
| 4 | Sunset | Unengaged segment | Ask honestly, offer a "launches only" option, then clean the list | [04](04-sunset.md) |

## What changed from v1 (and why)

v1 was generic template copy with "wide faces" dropped in. v2 is built on what makes SOL KYST different and on why your customers actually hesitate:

- **Fit is the real objection, so the emails sell fit.** They use real frame widths (Mini 135 / Midi 145 / Wide 158 / Oversized up to 161mm), give a measure-your-own-pair test, and offer to size people from a selfie.
- **Price gets justified with specs from your own product pages:** acetate, polarized lenses, UV400, the hard case and the sliding gift box.
- **The emails use your real language** ("Let's get you Kyst", "wide-face babe", 🤭) instead of "The SOL KYST Crew" filler.
- **Discounts are rare.** The cart flow doesn't discount (your checkout flow already closes with an offer). Only the very last sunset email has one.
- **Each email has one idea and one button.** Fewer exclamation points and emojis, so the ones that are left actually land.
- **A plain-text founder email follows the first order.** It lands in Primary, earns replies (good for deliverability) and asks "what made you buy?" (free attribution data).
- **A returns-prevention email** ("the 3-day rule" for acetate settling) goes out before customers decide the frames don't fit.
- **Cross-sells use the size they already know** ("you've done the hard part"), including Blue Light RX ↔ sunnies.

## Facts pulled from the store (v2.1)

| Used in copy | Source |
|---|---|
| Founder Meghan: ex-makeup artist, started in 2020, Kyst Eye on TikTok March 2021, $10,000+ launch day | Meghan (`../BRAND.md`) |
| "Standard" sunglasses = one size, ~140mm | SOL KYST sizing copy |
| Free exchanges for 45 days, no restocking fee · refunds within 30 days ($10 fee) · ReturnBear drop-off in Canada | Refund policy |
| Petite, clearance and RX orders are final sale | Refund policy |
| Ships from Hamilton in 3–5 business days · free shipping over $150 · always duty-free to CA/US | Shipping policy |
| KIN #1, Sweet Heart #2 by net sales | Shopify analytics, last 365 days |

The unverified "Sweet Heart sold out" line has been cut.

## Live in Klaviyo (all draft)

| Flow | Klaviyo ID | Emails with bodies |
|---|---|---|
| [DRAFT v2] Added to Cart | `U3P5sY` | 2 (trigger excludes `Product Type = LensAdvizor`) |
| [DRAFT v2] Post-Purchase | `SjYqK2` | 6 (1A, 1B, then 2 and 3 on each branch) |
| [DRAFT v2] Back in Stock | `SaHU4e` | 2 |

HTML lives in `templates/`. To change copy, edit `build_templates.py`, run `python3 build_templates.py templates`, then re-upload to Klaviyo. `preview.html` is a local preview of every email with sample data (rebuild it with `python3 build_preview.py templates preview.html`).

## Still to do

- [ ] Point the "Start an exchange" button (Post-Purchase 2) at your return portal. It currently goes to /account.
- [ ] Meghan: read Post-Purchase Email 1A and edit it so it sounds like you
- [ ] Exclude RX and Petite orders from the exchange messaging (final sale)
- [ ] Discount code `STAYKYST10` (Sunset Email 2 only)
- [ ] A/B test the subject lines (A/B pairs are provided for every email)
- Post-purchase PP 1A now uses template `TPAPaW` (launch-day fact fix).
