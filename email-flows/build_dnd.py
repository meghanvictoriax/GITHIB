"""Drag-and-drop (Klaviyo SYSTEM_DRAGGABLE) versions of welcome emails 1-6.

Same copy and look as the coded templates, rebuilt from Klaviyo blocks so they can be edited in the
drag-and-drop editor. Writes one create-template request body per email to templates/dnd/.

Run:  python3 build_dnd.py
"""
import json, pathlib
from build_welcome import SITE, CODE, DEN, COCOA, IVORY, LINEN, INK, MUTED, IMG, HERO, MID, link
from build_welcome_flow import PHOTO

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"
SAND = "#F4EEE8"
PROD = {
    "INTEGRITY": (IMG + "547973D9-7C97-4ACD-BD1B-C47CF3CCE67F.jpg?v=1767378147&width=600", "/products/integrity"),
    "MONARCH": (IMG + "Monarch_97e3b29d-5e10-42fe-a0ed-656639bea6ef.png?v=1766799619&width=600", "/products/monarch"),
    "HANGOVER": (IMG + "3_14b8037b-4300-4470-aa92-8b5633941ac2.png?v=1766799117&width=600", "/products/hangover"),
    "SWEET HEART": (IMG + "Cut_Out_-_Barbie_-_4.png?v=1784148545&width=600", "/products/barbie%E2%84%A2-x-sol-kyst-1970s-superstar-hearts"),
}
D = {"show_on": "all"}
K = "https://cdn.klaviyomail.com/company/Yh6N8Y/images/"
# Shopify photo -> Klaviyo image library (asset id, url). Drag-and-drop image blocks must use library images.
KIMG = {
    HERO: ("384349022", K + "889fc16f-dcac-49cc-b7a2-73a732a65558.jpeg"),
    MID: ("384349038", K + "50a96475-39a1-4caa-8ca0-32b2bfc80357.jpeg"),
    PHOTO["white_frames"]: ("384349076", K + "02858bdc-c68d-41df-a2b1-42423937fe03.jpeg"),
    PHOTO["couch"]: ("384349159", K + "e4414705-32f0-41b9-af7f-d006491db8ec.jpeg"),
    PHOTO["friends"]: ("384349174", K + "32fb9d73-3398-443d-b274-ec2a6ed536f0.jpeg"),
    PROD["INTEGRITY"][0]: ("384349191", K + "50200e5d-0b08-4086-80ee-0d3fc38bf433.jpeg"),
    PROD["MONARCH"][0]: ("384349203", K + "c5c070e3-cacd-43e9-8f36-af3d8b68f9d8.png"),
    PROD["HANGOVER"][0]: ("384349216", K + "12ea5b07-cd9e-419a-bc2b-f88f16b73057.png"),
    PROD["SWEET HEART"][0]: ("384349233", K + "577d7943-e1d3-4a8c-b6e8-fb779e755cf7.png"),
}


# ---------- blocks ----------
def text(html, pad=(0, 0, 0, 0)):
    t, r, b, l = pad
    return {"content_type": "block", "type": "text", "data": {"content": html, "display_options": D, "styles": {
        "block_padding_top": t, "block_padding_right": r, "block_padding_bottom": b, "block_padding_left": l}}}


def image(src, href, alt, pad=(0, 0, 0, 0)):
    t, r, b, l = pad
    return {"content_type": "block", "type": "image", "data": {
        "properties": {"dynamic": False, "asset_id": KIMG[src][0], "src": KIMG[src][1], "href": href, "alt_text": alt},
        "display_options": D, "styles": {"align": "center", "full_width_mobile": True,
                                         "block_padding_top": t, "block_padding_right": r, "block_padding_bottom": b, "block_padding_left": l}}}


def button(label, href, fg=COCOA, bg=None, pad=(10, 0, 10, 0)):
    t, r, b, l = pad
    return {"content_type": "block", "type": "button", "data": {"content": label, "properties": {"href": href}, "display_options": D, "styles": {
        "background_color": bg or "transparent", "color": fg, "border_color": fg, "border_style": "solid", "border_width": 2, "border_radius": 0,
        "font_family": SANS, "font_size": 13, "font_weight": "600", "letter_spacing": 2, "text_align": "center",
        "inner_padding_top": 14, "inner_padding_bottom": 14, "inner_padding_left": 34, "inner_padding_right": 34,
        "block_padding_top": t, "block_padding_right": r, "block_padding_bottom": b, "block_padding_left": l}}}


def rule():
    return {"content_type": "block", "type": "horizontal_rule", "data": {"display_options": D, "styles": {
        "border_color": LINEN, "border_style": "solid", "border_width": 1, "block_padding_top": 0, "block_padding_bottom": 0,
        "block_padding_left": 20, "block_padding_right": 20}}}


# ---------- text helpers (HTML inside text blocks) ----------
def eyebrow(s, color=MUTED):
    return f'<p style="text-align:center;font-family:{SANS};font-size:11px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{color};margin:0 0 14px">{s}</p>'


def headline(s, color=INK, size=34):
    return f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:{size}px;line-height:1.15;color:{color};margin:0 0 6px">{s}</p>'


def body(s, color=INK, align="center"):
    c = "" if color == INK else f"color:{color};"
    return f'<p style="text-align:{align};{c}margin:0 0 16px">{s}</p>'


def small(s, color=MUTED, italic=False):
    st = f"font-family:{SERIF};font-style:italic" if italic else f"font-family:{SANS}"
    return f'<p style="text-align:center;{st};font-size:13px;line-height:1.6;color:{color};margin:0 0 12px">{s}</p>'


def quote(q, who):
    return (f'<p style="text-align:center;font-family:{SANS};font-size:14px;letter-spacing:3px;color:{COCOA};margin:0 0 8px">&#9733;&#9733;&#9733;&#9733;&#9733;</p>'
            f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:19px;line-height:1.45;color:{INK};margin:0 0 10px">&ldquo;{q}&rdquo;</p>'
            f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:0 0 26px">{who}</p>')


# ---------- sections ----------
def section(blocks, bg=IVORY, pad=(0, 0, 0, 0), cols=None):
    t, r, b, l = pad
    if cols:
        layout = {2: "2-columns-equal-width"}.get(len(cols), "2-columns-equal-width")
        rows = [{"data": {"styles": {"column_layout": layout}}, "columns": [{"blocks": c} for c in cols]}]
    else:
        rows = [{"data": {"styles": {"column_layout": "1-column-full-width"}}, "columns": [{"blocks": blocks}]}]
    return {"content_type": "section", "type": "section", "data": {
        "properties": {}, "display_options": D,
        "styles": {"background_color": bg, "inner_padding_top": t, "inner_padding_right": r, "inner_padding_bottom": b, "inner_padding_left": l,
                   "stack_on_mobile": True}}, "rows": rows}


def topbar():
    return section([text(f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin:0">'
                         f'<a href="{link()}" style="color:{IVORY};text-decoration:none">15% off your first pair &middot; tap to apply</a></p>')], COCOA, (11, 16, 11, 16))


def logo():
    return section([text(f'<p style="text-align:center;font-family:{SANS};font-size:18px;font-weight:700;letter-spacing:8px;margin:0">'
                         f'<a href="{SITE}" style="color:{INK};text-decoration:none">SOL KYST</a></p>')], IVORY, (24, 20, 20, 20))


def trust(third="As seen on<br>Dragons&#39; Den"):
    cell = lambda s: text(f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;line-height:1.5;color:{MUTED};margin:0">{s}</p>', (16, 4, 16, 4))
    return [section([rule()], IVORY, (40, 0, 0, 0)),
            {"content_type": "section", "type": "section", "data": {"properties": {}, "display_options": D, "styles": {"background_color": IVORY, "stack_on_mobile": False}},
             "rows": [{"data": {"styles": {"column_layout": "3-columns-equal-width"}}, "columns": [
                 {"blocks": [cell("Free exchanges<br>45 days")]}, {"blocks": [cell("Free shipping<br>over $150")]}, {"blocks": [cell(third)]}]}]},
            section([rule()], IVORY)]


def footer(line="Questions? Just hit reply. A real person reads every one.", third="As seen on<br>Dragons&#39; Den"):
    return trust(third) + [section([text(
        f'<p style="text-align:center;font-family:{SANS};font-size:12px;line-height:1.7;color:{MUTED};margin:0">{line}<br>'
        "{{ organization.name }} &middot; {{ organization.full_address }}<br>{% unsubscribe 'Unsubscribe' %}</p>")], IVORY, (28, 30, 40, 30))]


def photo(src, alt, path="/collections/all"):
    return section([image(src, link(path), alt)], IVORY)


def code_box():
    return text(f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:0 0 4px;padding-top:16px;border-top:1px dashed {COCOA}">Your code</p>'
                f'<p style="text-align:center;font-family:{SANS};font-size:14px;font-weight:600;letter-spacing:2px;color:{INK};margin:0;padding-bottom:16px;border-bottom:1px dashed {COCOA}">{CODE.upper()}</p>', (8, 0, 0, 0))


def table(rows, head=None, widths=None):
    """A simple HTML table inside a text block (editable in the text editor)."""
    td = f"padding:12px 10px;border-bottom:1px solid {LINEN};font-size:14px;line-height:1.4"
    h = ""
    if head:
        h = "<tr>" + "".join(f'<td style="padding:12px 10px;background:{COCOA};font-size:10px;font-weight:600;letter-spacing:2px;color:{IVORY}">{c}</td>' for c in head) + "</tr>"
    b = "".join("<tr>" + "".join(f'<td style="{td}">{c}</td>' for c in r) + "</tr>" for r in rows)
    return text(f'<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse">{h}{b}</table>', (4, 0, 20, 0))


# ---------- emails ----------
def product_cell(name, sub):
    src, path = PROD[name]
    return [image(src, link(path), name.title(), (0, 6, 0, 6)),
            text(f'<p style="text-align:center;font-family:{SANS};font-size:12px;font-weight:600;letter-spacing:2px;color:{INK};margin:12px 0 2px">{name}</p>'
                 f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:14px;color:{MUTED};margin:0 0 20px">{sub}</p>')]


E1 = ([logo(),
       section([text(eyebrow("Welcome &middot; As seen on CBC&#39;s Dragons&#39; Den", LINEN) + headline("15% off your first pair.", IVORY, 30)),
                button("Claim my 15% off", link(), IVORY),
                text(f'<p style="text-align:center;font-family:{SANS};font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{LINEN};margin:6px 0 0">Code: {CODE.upper()}</p>'
                     f'<p style="text-align:center;font-family:{SANS};font-size:11px;color:{LINEN};margin:2px 0 0">Applies automatically when you tap</p>')], COCOA, (30, 40, 32, 40)),
       photo(HERO, "Close-up in SOL KYST sunglasses"),
       section([text(headline("Your face deserves better.")), button("Claim my 15% off", link("/collections/all"))], IVORY, (44, 48, 12, 48)),
       section([text(body("Most sunglasses come in one size: about 140mm. If you have a wider face, you know how that ends. Pinched temples by lunch, red marks, a drawer full of pairs you don&#39;t wear.")
                     + body("SOL KYST is built around what wide faces actually need. <b>Mini 135, Midi 145 and Wide 158mm.</b> Real acetate, polarized lenses, UV400.")
                     + body("Wrong size? <b>Exchanges are free for 45 days.</b>"))], IVORY, (28, 56, 28, 56)),
       photo(MID, "SOL KYST in the closet"),
       section([text(eyebrow("As seen on CBC&#39;s Dragons&#39; Den") + headline("Two Dragons<br>wanted in.")
                     + body("We walked into the Den with sunglasses built for wide faces, and two Dragons wanted to partner. We walked out with a deal. Not because of the pitch. Because the fit is that good.")),
                button("Watch our episode", DEN),
                text(f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:16px;line-height:1.6;color:{MUTED};margin:18px 0 0">It started with Meghan, a makeup artist with a wide face who designed the pair she couldn&#39;t find. One TikTok later, she had a $10,000+ launch day. <a href="{SITE}/pages/about" style="color:{COCOA}">Read our story</a></p>')],
               IVORY, (48, 52, 36, 52)),
       section([text(eyebrow("Start here"))], IVORY, (8, 32, 0, 32)),
       section(None, IVORY, (0, 26, 0, 26), cols=[product_cell("INTEGRITY", "The sleek black rectangle"), product_cell("MONARCH", "The tortoise rectangle")]),
       section(None, IVORY, (0, 26, 0, 26), cols=[product_cell("HANGOVER", "Big, dark and forgiving"), product_cell("SWEET HEART", "Barbie&trade; x Sol Kyst")]),
       section([button("Shop with 15% off", link("/collections/all"))], IVORY, (0, 32, 8, 32))]
      + footer("Let&#39;s get you Kyst.", "Duty-free CA &amp; US<br>over $150"))

STEP = lambda n, s: f'<p style="font-family:{SANS};font-size:16px;line-height:1.55;color:{INK};margin:0 0 12px"><span style="font-family:{SERIF};font-style:italic;font-size:24px;color:{COCOA};padding-right:16px">{n}</span>{s}</p>'
E2 = ([topbar(), logo(),
       section([text(eyebrow("The 30-second test") + headline("Do your sunglasses<br>actually fit?")
                     + body("Grab the pair you wore today. There&#39;s a quick test that shows whether they really fit your face, or just feel fine for the first ten minutes.")
                     + STEP(1, "Grab the sunglasses you wear most.") + STEP(2, "Measure straight across the front, hinge to hinge.") + STEP(3, "Match it below.")),
                table([["~135mm", "<i>feel perfect</i>", "<b>Mini 135</b>"], ["~135&ndash;140mm", "<i>feel a little snug</i>", "<b>Midi 145</b>"],
                       ["~140mm+", "<i>pinch at the temples</i>", "<b>Wide 158</b>"], ["Any size", "<i>and you want big</i>", "<b>Oversized</b>"]], ["YOURS MEASURE", "AND", "TRY"]),
                text(body("Pinching at 140mm? That&#39;s not your face. That&#39;s the frame. <b>Still torn? Reply with a selfie</b> (straight on, hair back) and we&#39;ll tell you your size.")),
                button("Shop in my size", link("/collections/all"))], IVORY, (40, 48, 36, 48)),
       photo(PHOTO["couch"], "Trying on SOL KYST at home"),
       section([text(eyebrow("Our fit promise") + headline("Not in love?<br>No sweat.")
                     + body("Wear them for a few days. If the fit isn&#39;t right, <b>exchanges are free for 45 days</b>, with no restocking fee. In Canada, drop them at any ReturnBear location. No box, no label.")
                     + quote("I had ordered the wide pair initially and felt they were too big so I exchanged them for a midi and they fit perfectly. The exchange process was painless and very easy.", "Jennifer K. &middot; Integrity")
                     + small("Petite, clearance and RX orders are final sale, so send us a selfie first if you&#39;re unsure.", italic=True)),
                code_box()], IVORY, (40, 48, 12, 48))]
      + footer())

E3_STORY = [
    "Hi, it&#39;s Meghan, the founder of SOL KYST. Let me take you back to summer 2020.",
    "It&#39;s lockdown. Work is shut down, I&#39;m living in downtown Toronto, eating through my savings and wondering what the heck I&#39;m going to do. One day I&#39;m sitting on the beach with my friend, in my cute cover-up and my bathing suit&hellip; and a stupid pair of sunglasses that made me look like John Lennon and Harry Potter had a baby.",
    "And at some point I realized I hadn&#39;t really been listening to her. I was in a full shame spiral about how I looked, and then feeling even worse about that, like, why don&#39;t I care about my friend right now?",
    "You know that feeling. When something&#39;s off with your outfit or you&#39;re feeling insecure, your whole mood is off and you can&#39;t enjoy the spaces you&#39;re in. And realistically? All I needed was a pair of glasses that actually fit me.",
    "They weren&#39;t even abnormally small. I&#39;m just a wide-faced cheeky babe, and sunglasses come in one standard size that has never worked for me.",
    "And right there, the idea washed up on shore: <b>I&#39;m going to make the widest, largest women&#39;s sunglasses on the market.</b>",
    "I&#39;d been a makeup artist for 10+ years, so I sat in front of my mirror with construction paper and scissors and used highlight and contour to cut out a shape that actually flatters a wider face. Many, many paper cut-outs later (and a terrible Canva diagram), that became our Kyst Eye. Same design we use today.",
    "In March 2021 I showed the first black prototype on TikTok, not expecting anything. 120,000 views in a few days and 1,200 sign-ups over one weekend. I threw a website together in three days and had a <b>$10,000+ launch day</b>. Exciting, amazing and really freaking scary, because the inventory was three months away.",
    "Now we&#39;re in three sizes (<b>Mini 135, Midi 145 and Wide 158mm</b>), with 650+ five-star reviews and customers in over 50 countries. And on CBC&#39;s Dragons&#39; Den, two Dragons wanted to partner with us.",
    "Because let&#39;s be real: a bomb pair of sunnies is your armour for the day. You deserve one that fits.",
]
E3 = ([topbar(), logo(), photo(PHOTO["friends"], "SOL KYST", "/pages/about"),
       section([text(eyebrow("A note from Meghan") + headline("The pair I<br>couldn&#39;t find.") + "".join(body(p) for p in E3_STORY)
                     + f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:18px;color:{INK};margin:8px 0 2px">Love, Meghan</p>'
                     + f'<p style="text-align:center;font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:0 0 16px">Founder, SOL KYST</p>'),
                button("Watch our episode", DEN),
                text(f'<p style="text-align:center;font-family:{SANS};font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin:8px 0 0"><a href="{SITE}/pages/about" style="color:{COCOA}">Read the full story &rarr;</a></p>')],
               IVORY, (40, 48, 12, 48)),
       section([text(eyebrow("Don&#39;t forget", LINEN) + headline("Your 15% off is still waiting.", IVORY, 26)), button("Claim my 15% off", link("/collections/all"), IVORY),
                text(f'<p style="text-align:center;font-family:{SANS};font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{LINEN};margin:6px 0 0">Code: {CODE.upper()}</p>')],
               COCOA, (30, 40, 32, 40)),
       section([text(eyebrow("Wide face babes who made the switch") + headline("Finally, a pair that fits.", INK, 28)
                     + quote("This is the first pair of glasses I&#39;ve owned that doesn&#39;t give me a headache or leave marks on my face. They fit my wiiiide face PERFECTLY!", "Melina T. &middot; Integrity")
                     + quote("I always thought my round face shape was why all sunglasses looked slightly off, but I just needed wider sunglasses!", "Mary H. &middot; Monarch")
                     + quote("With my very wide face, even the widest frames looked incredibly awkward and dorky. Enter the MONARCH!!", "Midori P. &middot; Monarch")),
                button("Find my pair", link("/collections/all"))], IVORY, (44, 48, 12, 48))]
      + footer())

CMP = [["SIZES", "Mini 135 &middot; Midi 145 &middot; Wide 158mm", "<i>One size, about 140mm</i>"],
       ["FIT", "Room for cheekbones and temples", "<i>Pinches by lunch</i>"],
       ["FRAME", "Acetate, adjustable to your face", "<i>Often thin plastic</i>"],
       ["LENSES", "Polarized &middot; UV400", "<i>Hit or miss</i>"],
       ["DESIGNED BY", "A wide-face makeup artist", "<i>An &ldquo;average&rdquo; face chart</i>"],
       ["WRONG FIT?", "Free exchanges for 45 days", "<i>Back in the drawer</i>"]]
E4 = ([topbar(), logo(), photo(PHOTO["white_frames"], "SOL KYST white frames"),
       section([text(eyebrow("Ours vs. theirs") + headline("Built for your face.<br>Not the average one.")
                     + body("Most sunglasses are designed around one &ldquo;standard&rdquo; face. If yours is wider, you&#39;ve felt it: the squeeze at the temples, the red marks, the pair that slides down. Here&#39;s what&#39;s different about ours.")),
                table(CMP, ["", "SOL KYST", "STANDARD"]),
                button("Claim my 15% off", link("/collections/all"))], IVORY, (40, 40, 28, 40))]
      + footer())


def pick(label, name, sub):
    src, path = PROD[name.upper()]
    return section(None, IVORY, (0, 40, 24, 40), cols=[
        [image(src, link(path), name)],
        [text(f'<p style="font-family:{SANS};font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{MUTED};margin:24px 0 6px">{label}</p>'
              f'<p style="font-family:{SERIF};font-style:italic;font-size:26px;line-height:1.1;color:{INK};margin:0 0 8px">{name}</p>'
              f'<p style="font-family:{SANS};font-size:14px;line-height:1.5;color:{INK};margin:0 0 12px">{sub}</p>'
              f'<p style="font-family:{SANS};font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin:0"><a href="{link(path)}" style="color:{COCOA}">Shop &rarr;</a></p>', (0, 0, 0, 16))]])


E5 = ([topbar(), logo(), photo(PHOTO["friends"], "Friends in SOL KYST"),
       section([text(eyebrow("Start here") + headline("Not sure where<br>to start?") + body("These are the pairs most people start with. Pick the one that feels most like you."))], IVORY, (40, 40, 16, 40)),
       pick("The everyday", "Integrity", "The sleek black rectangle. Goes with everything you own."),
       pick("The classic", "Monarch", "The tortoise rectangle. Warm, polished, easy."),
       pick("The statement", "Hangover", "Big, dark and forgiving. For the days you want to disappear."),
       pick("The fun one", "Sweet Heart", "Barbie&trade; x Sol Kyst. Peachy-pink hearts and our #2 style this year."),
       section([button("Claim my 15% off", link("/collections/all"))], IVORY, (0, 40, 28, 40)),
       section([text(eyebrow("What you get") + headline("Every pair comes with", INK, 26)
                     + body("A hard protective case, a microfibre cloth and our sliding gift box. Free shipping over $150, and orders to Canada and the US over $150 ship duty-free.")
                     + f'<p style="text-align:center;font-family:{SERIF};font-style:italic;font-size:15px;color:{MUTED};margin:8px 0 0">The brand two Dragons wanted in on. <a href="{DEN}" style="color:{COCOA}">Watch the episode</a></p>')],
               SAND, (40, 48, 40, 48))]
      + footer())

P = lambda s: f'<p style="font-family:Arial,sans-serif;font-size:15px;color:#222222;margin:0 0 16px">{s}</p>'
E6 = [{**section([text(
    P("Hi {{ first_name|default:'' }},") + P("It&#39;s Meghan again. Quick one, I promise.")
    + P("I&#39;ll be honest, I&#39;m not great at the salesy stuff. I&#39;d rather just talk to you.")
    + P("If you&#39;ve been eyeing a pair but something&#39;s holding you back, I&#39;d genuinely love to know what it is. The size? The price? Not sure what&#39;ll suit your face? <b>Just hit reply and tell me.</b> I read these, and I&#39;ll help you figure it out, even if the answer is that we&#39;re not the right fit for you.")
    + P("Or send me a selfie (straight on, hair back) and I&#39;ll tell you your size. That&#39;s honestly one of my favourite parts of this job.")
    + P(f'Your 15% off is still here whenever you&#39;re ready: <a href="{link("/collections/all")}" style="color:{COCOA}"><b>{CODE.upper()}</b></a> (it applies automatically when you tap).')
    + P("Let&#39;s get you Kyst,<br>Meghan<br>Founder, SOL KYST")
    + P("P.S. Running a small company means wearing a lot of hats. Reading your emails is my favourite one.")
    + '<p style="font-family:Arial,sans-serif;font-size:11px;color:#999999;margin:40px 0 0">{{ organization.name }} &middot; {{ organization.full_address }} &middot; {% unsubscribe \'Unsubscribe\' %}</p>',
    (0, 0, 0, 0))], "#FFFFFF", (24, 20, 24, 20))}]

def styles(bg):
  return [
    {"style_type": "base-styles", "properties": {"mobile_optimizations": True}, "styles": {"content_background_color": bg, "margin_top": 0}},
    {"style_type": "text-styles", "styles": {"color": INK, "font_family": SANS, "font_size": 16, "line_height": 1.65}},
    {"style_type": "heading-1-styles", "styles": {"color": INK, "font_family": SERIF, "font_size": 34, "font_style": "italic", "font_weight": "400"}},
    {"style_type": "heading-2-styles", "styles": {"color": INK, "font_family": SERIF, "font_size": 28, "font_style": "italic", "font_weight": "400"}},
    {"style_type": "heading-3-styles", "styles": {"color": INK, "font_family": SERIF, "font_size": 22, "font_style": "italic", "font_weight": "400"}},
    {"style_type": "heading-4-styles", "styles": {"color": MUTED, "font_family": SANS, "font_size": 11, "font_weight": "600", "letter_spacing": 3}},
    {"style_type": "link-styles", "styles": {"color": COCOA, "text_decoration": "underline"}},
    {"style_type": "mobile-styles", "properties": {"mobile_padding_override": False}, "styles": {}},
]

EMAILS = {
    "dnd-welcome-1": ("[DRAFT DnD] SOL KYST | Welcome 1 - Offer + Dragons' Den", E1, IVORY),
    "dnd-welcome-2": ("[DRAFT DnD] SOL KYST | Welcome 2 - The 30-second test", E2, IVORY),
    "dnd-welcome-3": ("[DRAFT DnD] SOL KYST | Welcome 3 - Founder story + reviews", E3, IVORY),
    "dnd-welcome-4": ("[DRAFT DnD] SOL KYST | Welcome 4 - Ours vs theirs", E4, IVORY),
    "dnd-welcome-5": ("[DRAFT DnD] SOL KYST | Welcome 5 - Start here", E5, IVORY),
    "dnd-welcome-6": ("[DRAFT DnD] SOL KYST | Welcome 6 - Note from Meghan", E6, "#FFFFFF"),
}

if __name__ == "__main__":
    out = pathlib.Path("templates/dnd"); out.mkdir(parents=True, exist_ok=True)
    for key, (name, sections, bg) in EMAILS.items():
        req = {"data": {"type": "template", "attributes": {"name": name, "editor_type": "SYSTEM_DRAGGABLE", "definition": {
            "body": {"properties": {}, "styles": {"background_color": bg, "width": 600}, "sections": sections}, "styles": styles(bg)}}}}
        s = json.dumps(req, separators=(",", ":"), ensure_ascii=False)
        (out / f"{key}.json").write_text(s)
        print(key, len(s))
