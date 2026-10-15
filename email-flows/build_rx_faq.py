"""Prescription FAQ campaign email (drag-and-drop), incl. the Breast Cancer Blue Light readers.

Facts come from the store, not memory:
- RX steps, lens types, materials, timing, PD, 20% frame perk, final sale: theme templates/page.rx-page.json
- Change/cancel, damaged/defective (48 h): theme templates/page.faq.json
- Final sale wording: Shopify refund policy
- Breast Cancer Blue Light sizes, lenses, prices: Shopify product breast-cancer-blue-light-frame
- Free Kyst Klip with the frame: Shopify product breast-cancer-kyst-klip-1
- Giving line: Shopify page breast-cancer (verbatim)
- "Lenses from" prices: LensAdvizor lens products (CR39 S1 $140, CR39 P1 $240, non-RX CR39 $140)

Run:  python3 build_rx_faq.py   -> templates/dnd/dnd-rx-faq.json
"""
import json, pathlib
from build_dnd import (section, text, button, rule, logo, eyebrow, headline, small, table, styles,
                       SANS, SERIF, SAND, D, K)
from build_welcome import SITE, COCOA, IVORY, LINEN, INK, MUTED
from mobile_fix import walk

RX = f"{SITE}/pages/rx"
BC = f"{SITE}/products/breast-cancer-blue-light-frame"
EMAIL = "customer@solkyst.ca"
BC_IMG = ("384469683", K + "7f3264e3-fc70-4d04-896f-e9dfd7093449.png")
BC_PHOTO = ("384469702", K + "d29e13e6-f81b-49b4-85fc-2c2e4ac5f124.jpeg")


def img(asset, href, alt, pad=(0, 0, 0, 0)):
    t, r, b, l = pad
    return {"content_type": "block", "type": "image", "data": {
        "properties": {"dynamic": False, "asset_id": asset[0], "src": asset[1], "href": href, "alt_text": alt},
        "display_options": D, "styles": {"align": "center", "full_width_mobile": True,
                                         "block_padding_top": t, "block_padding_right": r, "block_padding_bottom": b, "block_padding_left": l}}}


def body(s, color=INK, align="center"):
    return f'<p style="text-align:{align};color:{color};font-size:16px;line-height:1.6;margin:0 0 16px">{s}</p>'


STEP = lambda n, s: (f'<p style="text-align:left;font-family:{SANS};font-size:16px;line-height:1.6;color:{INK};margin:0 0 14px">'
                     f'<span style="font-family:{SERIF};font-style:italic;font-size:24px;color:{COCOA};padding-right:14px">{n}</span>{s}</p>')


def qa(q, a):
    return (f'<p style="text-align:left;font-family:{SERIF};font-style:italic;font-size:19px;line-height:1.3;color:{INK};margin:0 0 6px">{q}</p>'
            f'<p style="text-align:left;font-family:{SANS};font-size:16px;line-height:1.6;color:{INK};margin:0 0 24px">{a}</p>')


def trust_row(cells):
    cell = lambda s: text(f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:1px;text-transform:uppercase;line-height:1.5;color:{MUTED};margin:0">{s}</p>', (16, 4, 16, 4))
    return [section([rule()], IVORY, (40, 0, 0, 0)),
            {"content_type": "section", "type": "section", "data": {"properties": {}, "display_options": D, "styles": {"background_color": IVORY, "stack_on_mobile": False}},
             "rows": [{"data": {"styles": {"column_layout": "3-columns-equal-width"}}, "columns": [{"blocks": [cell(c)]} for c in cells]}]},
            section([rule()], IVORY)]


MAIL = f'<a href="mailto:{EMAIL}" style="color:{COCOA}">{EMAIL}</a>'

RX_FAQ = ([logo(),
    # Hero
    section([text(eyebrow("Prescription &middot; Readers &middot; Custom")
                  + headline("Your prescription,<br>in frames that fit.")
                  + body("You ask us a lot about prescription lenses. So here&#39;s everything in one place: how it works, what it costs, and what happens if something isn&#39;t right."))],
            IVORY, (16, 24, 8, 24)),

    # Breast Cancer Blue Light / readers
    section([img(BC_IMG, BC, "Breast Cancer Blue Light frame")], IVORY, (24, 24, 0, 24)),
    section([text(eyebrow("October &middot; Breast Cancer Awareness Month")
                  + headline("The Breast Cancer<br>Blue Light")
                  + body("A clear acetate frame with pink stainless steel wire and a ribbon charm.")
                  + body("Choose a <b>blue light filter</b> lens ($200) or make them <b>readers in +1, +2 or +3</b> ($280). In Mini 135, Midi 145 or Wide 158mm.")
                  + body("Every pair comes with a <b>free Kyst Klip</b>.")
                  + small("A portion of every purchase goes to breast cancer research and support organizations.", italic=True)),
             button("Shop the pink pair", BC)], IVORY, (24, 24, 36, 24)),

    # How prescription works
    section([text(eyebrow("How prescription works") + headline("Four steps.")
                  + STEP(1, "<b>Choose your frame</b> from our prescription styles.")
                  + STEP(2, "<b>Build your lenses:</b> single vision, readers or progressive, with blue light, tints, polarized or Transitions.")
                  + STEP(3, "<b>Add your prescription.</b> Upload a photo, type it in, or email it after you order. You&#39;ll need your PD (pupillary distance).")
                  + STEP(4, "<b>Check out.</b> We check your prescription, our lab makes your lenses, and your order ships in 3&ndash;4 business days.")),
             text(f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:0 0 4px;padding-top:16px;border-top:1px dashed {COCOA}">The prescription perk</p>'
                  f'<p style="text-align:center;font-family:{SANS};font-size:15px;line-height:1.5;color:{INK};margin:0;padding-bottom:16px;border-bottom:1px dashed {COCOA}">Add prescription lenses to any frame and get <b>20% off the frame</b>. No code needed.</p>', (8, 0, 8, 0)),
             button("Build my glasses", RX)], SAND, (40, 24, 36, 24)),

    # Lens guide
    section([text(eyebrow("Lens guide") + headline("What to choose", INK, 26)),
             table([["<b>Single vision</b>", "One prescription across the whole lens, for distance or reading", "$140"],
                    ["<b>Progressive</b>", "Near and far in one lens, with a smooth change in between", "$240"],
                    ["<b>Non-prescription</b>", "Blue light or a custom tint, no correction", "$140"]],
                   ["LENS", "WHAT IT&#39;S FOR", "FROM"]),
             text(body("<b>Materials:</b> CR39 for everyday wear, Polycarbonate for strength (shatter resistant), Trivex for feather-light comfort, and High Index 1.67 for strong prescriptions. <b>Anti-reflective coating is included on every lens.</b>", INK, "left"))],
            IVORY, (40, 24, 16, 24)),

    # FAQ
    section([text(eyebrow("Your questions") + headline("Prescription FAQ", INK, 26)),
             text(qa("What prescriptions can you make?", "Single vision, readers and progressive. Looking for something truly custom? Reply and tell us, and we&#39;ll work on it with you.")
                  + qa("Do I need my PD?", "Yes. It&#39;s usually on your prescription. If it isn&#39;t, ask your optometrist, or use the virtual try-on on our product pages, which can measure it for you.")
                  + qa("How long does it take?", "Your order ships in 3&ndash;4 business days once we&#39;ve checked your prescription. Complex prescriptions and custom orders can take up to three weeks. We&#39;ll email you if yours will.")
                  + qa("Can I change my order after I place it?", "Not once it&#39;s placed. Your lenses go straight into production with our lab, so double-check your prescription before you check out.")
                  + qa("Can I return or exchange prescription lenses?", f"Prescription (RX) orders are final sale, because your lenses are made just for you. If your order arrives damaged, defective or wrong, email {MAIL} within 48 hours of delivery with your order number and photos, and we&#39;ll work with you on it.")
                  + qa("Can my own optometrist fit lenses in your frames?", "Our frames are Rx-able, so yes. Just ask your optometrist to confirm they&#39;ll work with your prescription."))],
            IVORY, (24, 24, 8, 24)),

    # Working with you
    section([text(eyebrow("Working with you") + headline("Something truly custom?", INK, 26)
                  + body("A tricky prescription, a tint you can&#39;t find anywhere, or you&#39;re just not sure where to start? Hit reply and tell us what you&#39;re after. A real person reads every email.")),
             button("Email us", f"mailto:{EMAIL}")], SAND, (40, 24, 36, 24)),
    ]
    + trust_row(["Ships in 3&ndash;4<br>business days", "20% off frames<br>with RX lenses", "AR coating<br>on every lens"])
    + [section([text(f'<p style="text-align:center;font-family:{SANS};font-size:12px;line-height:1.7;color:{MUTED};margin:0">Questions? Just hit reply. A real person reads every one.<br>'
                     "{{ organization.name }} &middot; {{ organization.full_address }}<br>{% unsubscribe 'Unsubscribe' %}</p>")], IVORY, (28, 24, 40, 24))])

if __name__ == "__main__":
    walk(RX_FAQ)
    req = {"data": {"type": "template", "attributes": {"name": "[DRAFT DnD] SOL KYST | Prescription FAQ + Breast Cancer readers", "editor_type": "SYSTEM_DRAGGABLE",
                                                       "definition": {"body": {"properties": {}, "styles": {"background_color": IVORY, "width": 600}, "sections": RX_FAQ}, "styles": styles(IVORY)}}}}
    out = pathlib.Path("templates/dnd"); out.mkdir(parents=True, exist_ok=True)
    s = json.dumps(req, separators=(",", ":"), ensure_ascii=False)
    (out / "dnd-rx-faq.json").write_text(s)
    print("dnd-rx-faq", len(s))
