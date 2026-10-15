# Theme changes (on preview theme, not yet live)

Half-price add-ons in the cart page and cart drawer: Signature Kyst Klip ($40 → $20) and Kyst Kit ($22 → $11).

- `snippets/sk-klip-upsell.liquid` (new): when the cart has a pair from the Sunglasses collection, shows each add-on at half price unless it's already in the cart or sold out.
- `snippets/cart-products.liquid`: the live file plus one line, `{% render 'sk-klip-upsell' %}`, after the cart form. Both the cart page and the cart drawer render this snippet.

Prices come from two Shopify automatic discounts, "Signature Kyst Klip $20 with sunglasses" and "Kyst Kit half price with sunglasses" (50% off one of each per order with any sunglasses). Both are already active.

Installed on the preview theme "Klip upsell preview (Oct 15)" (id 200518140064). Preview: https://www.solkyst.ca/?preview_theme_id=200518140064. Goes live when that theme is published.
