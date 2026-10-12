# SOL KYST — Email Flow Drafts

Draft copy for the Klaviyo flows that are missing from the account. They fill the gaps around the flows that already exist.

## What already exists in Klaviyo

| Flow | Trigger | Status |
|---|---|---|
| Email Welcome Series Customer vs Non-Customer | Added to List | Live |
| Abandoned Cart | Checkout Started | Live |
| Browse Abandonment | Viewed Product | Live |
| Winback final | Added to List | Live |
| Review request | Metric | Draft |

## New drafts (this folder)

| # | Flow | Trigger (Klaviyo metric) | Emails | File |
|---|---|---|---|---|
| 1 | Added to Cart Abandonment | Added to Cart (`YpmNaq`) | 2 | [01-added-to-cart.md](01-added-to-cart.md) |
| 2 | Post-Purchase Thank You | Placed Order (`Y3d36N`) | 3 | [02-post-purchase.md](02-post-purchase.md) |
| 3 | Back in Stock | Subscribed to Back in Stock (`UYK4m5`) | 2 | [03-back-in-stock.md](03-back-in-stock.md) |
| 4 | Sunset / Unengaged | Segment (build it first, see file) | 2 | [04-sunset.md](04-sunset.md) |

## Voice notes (from Klaviyo brand voice)

- Approachable, playful, empowering and grateful. Write like a friend texting, not a corporation.
- Use emojis in subject lines (one or two at most) and use exclamation points sparingly.
- Every email gets one clear, direct CTA.
- Return to the brand's core idea in every email: **sunnies designed for wide faces**, in a choice of sizes (Mini / Midi / Wide / Oversized).

## Before going live

- [ ] Swap `{{ placeholders }}` for real links and discount codes.
- [ ] Add product imagery / dynamic product blocks in the Klaviyo editor.
- [ ] Confirm the discount amounts. The drafts use **10% off** only in the cart and sunset flows.
- [ ] Add flow filters as noted in each file (e.g. "Placed Order zero times since starting this flow").
- [ ] Send previews to yourself and check them on mobile.
