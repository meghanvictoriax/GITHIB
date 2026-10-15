# Theme changes (not yet live)

Signature Kyst Klip $20 upsell for the cart page and cart drawer.

- `snippets/sk-klip-upsell.liquid` (new): shows the Signature Kyst Klip at half price when the cart has a pair from the Sunglasses collection and no Klip yet. Hidden once the Klip is sold out.
- `snippets/cart-products.liquid`: the live file plus one line, `{% render 'sk-klip-upsell' %}`, after the cart form. Both the cart page and the cart drawer render this snippet.

The price comes from the Shopify automatic discount "Signature Kyst Klip $20 with sunglasses" (50% off one Klip per order, buy any sunglasses). That discount is already active.

To install: duplicate the live theme, upload these two files to the copy, preview, then publish.
