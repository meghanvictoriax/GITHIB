# Theme changes (on preview theme, not yet live)

Half-price add-ons in the cart page and cart drawer: Signature Kyst Klip ($40 → $20) and Kyst Kit ($22 → $11).

- `snippets/sk-klip-upsell.liquid` (new): when the cart has a pair from the Sunglasses collection, shows each add-on at half price unless it's already in the cart or sold out.
- `snippets/cart-products.liquid`: the live file plus one line, `{% render 'sk-klip-upsell' %}`, after the cart form. Both the cart page and the cart drawer render this snippet.

Prices come from two Shopify automatic discounts, both already active:
- "Signature Kyst Klip $20 with sunglasses": buy any sunglasses, get one Klip 50% off.
- "Kyst Kit half price": 50% off the Kyst Kit when the cart subtotal is $100 or more. The first version was also "buy any sunglasses" but never applied when the Klip discount was in the same cart (Shopify lets one pair count toward only one buy-X-get-Y), so it was replaced.

Installed on the preview theme "Klip upsell preview (Oct 15)" (id 200518140064). Preview: https://www.solkyst.ca/?preview_theme_id=200518140064. Goes live when that theme is published.
