# Flow 6: Abandoned Checkout (rebuild)

**Klaviyo:** flow `SJaAJJ` (**live since Oct 15, 2026**), "[DRAFT] Abandoned Checkout 2026 (replaces Abandoned Cart)". Built by `build_abandoned_cart.py`.
**Replaces:** flow `Y7eYv5` "Abandoned Cart", set to manual on Oct 15, 2026.
**Trigger:** Checkout Started (`TcjaQA`)
**Flow filters:** Placed Order = 0 since flow start, Checkout Started = 0 since flow start, re-entry after 3 days
**From / reply-to:** SOL KYST <info@solkyst.ca> / info@solkyst.ca

## Why rebuild

- The old "Return to Cart" buttons went to the homepage, not the shopper's checkout.
- Email 1 sent about 30 seconds after checkout started, sometimes while the shopper was still paying.
- Shopify also sends its own abandoned checkout email about 1 hour in, so shoppers got two emails in the first hour.
- The copy had unsourced urgency ("bestsellers sell out… in this economy").
- The old email 3 was a draft and never sent.

**Old flow, last 90 days:** 370 recipients, $7,388 revenue. Email 1 converted at 9.7%.

## Timing

| Step | When | Template | Subject | Preview |
|---|---|---|---|---|
| Email 1 | 1 hour after checkout started | `Wk67QW` | Still thinking about {{ event.Items.0\|title\|default:'your pair' }}? | Your checkout is saved, exactly how you left it. |
| Email 2 | 1 day later | `UhxdgQ` | Wrong size? Swap it, free | Exchanges are free for 45 days, no restocking fee. |
| Email 3 | 2 days later | `XaJFjM` | A free Signature Kyst Klip with your pair | Our last note about your checkout. Use code KYSTKLIP. |

Every email shows the shopper's own items: the variant photo, or the product photo if there's no variant photo. The button links to `{{ event.extra.checkout_url }}`.

## Offer (email 3)

- **Code:** `KYSTKLIP`, a Shopify Buy X Get Y discount.
- **How it works:** buy any item from the Sunglasses collection and get one Signature Kyst Klip (`sol-kyst-signature-kyst-klip`, $40) free.
- **Limits:** one use per customer. It combines with shipping discounts only.
- **Inventory:** 13 Signature Klips in stock (Oct 15), and it stops selling at zero. Once they're gone, the code can't be used.

## Still to do

- Turn off Shopify's own abandoned checkout email. That's in Shopify admin, under Settings → Notifications or Marketing → Automations.
- Rename the flow in Klaviyo to drop "[DRAFT]" (the API can't rename flows).
