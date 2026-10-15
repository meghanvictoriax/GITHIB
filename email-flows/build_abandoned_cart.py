"""Abandoned checkout flow (drag-and-drop), replacing the live "Abandoned Cart" flow Y7eYv5 emails.

Trigger: Checkout Started (Shopify). Every email shows the shopper's own items from the event and
links back to their saved checkout ({{ event.extra.checkout_url }}), not the homepage.

Facts come from the store, not memory:
- Sizes Mini 135 / Midi 145 / Wide 158mm, acetate, polarized, UV400, box contents: Shopify product pages
- 45-day free exchanges, no restocking fee, ReturnBear in Canada, final-sale items: Shopify refund policy
- Free shipping over $150; duty-free to Canada and the US: Shopify shipping policy
- Nearly 900 reviews, 4.7 stars: Loox store stats, October 2026
- Jennifer K. review: Loox, used in the welcome flow
- Signature Kyst Klip description: Shopify product sol-kyst-signature-kyst-klip
- KYSTKLIP: Shopify BXGY code, buy any sunglasses + get one Signature Kyst Klip free, one use per customer

Run:  python3 build_abandoned_cart.py   -> templates/dnd/dnd-ac-{1,2,3}.json
"""
import json, pathlib
from build_dnd import (section, text, button, rule, logo, eyebrow, headline, small, quote, footer, styles,
                       SANS, SERIF, SAND, D, K)
from build_welcome import SITE, COCOA, IVORY, LINEN, INK, MUTED
from mobile_fix import walk

CHECKOUT = "{{ event.extra.checkout_url|default:'" + SITE + "/cart' }}"
KLIP_IMG = ("384502325", K + "04758446-83ca-4517-b686-395238873a96.jpeg")
KLIP = f"{SITE}/products/sol-kyst-signature-kyst-klip"


def body(s, color=INK, align="center"):
    return f'<p style="text-align:{align};color:{color};font-size:16px;line-height:1.6;margin:0 0 16px">{s}</p>'


# The shopper's cart, straight from the Checkout Started event. Variant photo first, product photo as fallback.
CART = text(
    '{% for item in event.extra.line_items %}'
    f'<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;border-bottom:1px solid {LINEN}"><tr>'
    '<td width="120" style="padding:14px 16px 14px 0;vertical-align:middle">'
    '{% if item.product.variant.images.0.src %}<img src="{{ item.product.variant.images.0.src }}" width="120" alt="{{ item.product.title }}" style="display:block;width:120px;height:auto;border:0">'
    '{% else %}<img src="{{ item.product.images.0.src }}" width="120" alt="{{ item.product.title }}" style="display:block;width:120px;height:auto;border:0">{% endif %}</td>'
    '<td style="padding:14px 0;vertical-align:middle">'
    f'<p style="text-align:left;font-family:{SANS};font-size:13px;font-weight:600;letter-spacing:2px;color:{INK};margin:0 0 4px">{{{{ item.product.title }}}}</p>'
    f'<p style="text-align:left;font-family:{SERIF};font-style:italic;font-size:15px;color:{MUTED};margin:0">{{{{ item.variant_title }}}}{{% if item.quantity > 1 %}} &middot; Qty {{{{ item.quantity }}}}{{% endif %}}</p>'
    '</td></tr></table>'
    '{% endfor %}', (0, 0, 8, 0))


def cart_section(label="Back to my checkout"):
    return section([text(eyebrow("Saved for you")), CART, button(label, CHECKOUT)], IVORY, (8, 32, 32, 32))


def img(asset, href, alt, pad=(0, 0, 0, 0)):
    t, r, b, l = pad
    return {"content_type": "block", "type": "image", "data": {
        "properties": {"dynamic": False, "asset_id": asset[0], "src": asset[1], "href": href, "alt_text": alt},
        "display_options": D, "styles": {"align": "center", "full_width_mobile": False, "width": 260,
                                         "block_padding_top": t, "block_padding_right": r, "block_padding_bottom": b, "block_padding_left": l}}}


FOOT = footer(third="Duty-free<br>CA &amp; US")

# ---------- Email 1 (1 hour): your checkout is saved + the size question ----------
AC1 = ([logo(),
        section([text(headline("Still thinking it over?")
                      + body("Your checkout is saved exactly how you left it. Pick up right where you were."))], IVORY, (16, 40, 0, 40)),
        cart_section(),
        section([text(eyebrow("Not sure about the size?") + headline("Three widths, one for your face.", INK, 26)
                      + body("<b>Mini 135, Midi 145 and Wide 158mm.</b> Most sunglasses come in one size, about 140mm.")
                      + body("Measure a pair you own straight across the front, hinge to hinge. If they pinch, go one size up. Still torn? Hit reply and we&#39;ll help you pick."))],
                SAND, (36, 40, 28, 40))]
       + FOOT)

# ---------- Email 2 (+1 day): take the risk out of it ----------
AC2 = ([logo(),
        section([text(headline("Wrong size? Swap it.")
                      + body("If the fit isn&#39;t right when they arrive, <b>exchanges are free for 45 days</b>, with no restocking fee. In Canada, drop them at any ReturnBear location. No box, no label."))],
                IVORY, (16, 40, 8, 40)),
        section([text(quote("I had ordered the wide pair initially and felt they were too big so I exchanged them for a midi and they fit perfectly. The exchange process was painless and very easy.", "Jennifer K. &middot; Integrity")
                      + small("Nearly 900 reviews &middot; 4.7 stars"))], SAND, (36, 40, 20, 40)),
        section([text(eyebrow("What you get") + body("Acetate frames, polarized lenses, UV400. A hard protective case, a microfibre cloth and our sliding gift box.")
                      + small("Petite sizes, clearance and RX orders are final sale."))], IVORY, (32, 40, 0, 40)),
        cart_section("Finish my order")]
       + FOOT)

# ---------- Email 3 (+2 days): free Signature Kyst Klip ----------
AC3 = ([logo(),
        section([text(eyebrow("A little something from us") + headline("Your pair comes with<br>a free Signature Kyst Klip.")
                      + body("Our last note about your checkout, then we&#39;ll leave you be. Finish your order with code <b>KYSTKLIP</b> and our Signature Kyst Klip is on us."))],
                IVORY, (16, 40, 0, 40)),
        section([img(KLIP_IMG, KLIP, "The Signature Kyst Klip", (8, 0, 8, 0)),
                 text(body("Our glasses are big, our bags are small. Don&#39;t choose between gloss and sunnies. Clip your pair to your bag and keep both.")
                      + f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:0 0 4px;padding-top:16px;border-top:1px dashed {COCOA}">Your code</p>'
                        f'<p style="text-align:center;font-family:{SANS};font-size:14px;font-weight:600;letter-spacing:2px;color:{INK};margin:0;padding-bottom:16px;border-bottom:1px dashed {COCOA}">KYSTKLIP</p>'
                      + small("Add the Signature Kyst Klip to your cart with any sunglasses and enter the code at checkout. One per customer.", MUTED), (8, 0, 0, 0))],
                SAND, (28, 40, 28, 40)),
        cart_section("Finish my order"),
        section([text(body("Something stopped you? Size, shipping, anything. Hit reply and tell us. A real person reads every email.", MUTED))], IVORY, (0, 40, 0, 40))]
       + FOOT)

EMAILS = {"dnd-ac-1": ("[DnD] SOL KYST | Abandoned checkout 1 – saved for you", AC1),
          "dnd-ac-2": ("[DnD] SOL KYST | Abandoned checkout 2 – free exchanges", AC2),
          "dnd-ac-3": ("[DnD] SOL KYST | Abandoned checkout 3 – free Signature Kyst Klip", AC3)}

if __name__ == "__main__":
    out = pathlib.Path("templates/dnd"); out.mkdir(parents=True, exist_ok=True)
    for slug, (name, secs) in EMAILS.items():
        walk(secs)
        req = {"data": {"type": "template", "attributes": {"name": name, "editor_type": "SYSTEM_DRAGGABLE",
                                                           "definition": {"body": {"properties": {}, "styles": {"background_color": IVORY, "width": 600}, "sections": secs}, "styles": styles(IVORY)}}}}
        s = json.dumps(req, separators=(",", ":"), ensure_ascii=False)
        (out / f"{slug}.json").write_text(s)
        print(slug, len(s))
