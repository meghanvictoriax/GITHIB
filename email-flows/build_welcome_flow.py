"""Welcome flow emails 2-6 (email 1 is build_welcome.py).
Cadence from Mave & Chez (offer -> interactive test ~6h later -> founder story + reviews ~4h after that),
then KENT's structure for days 2-6 (ours-vs-theirs chart, curated "start here" picks, code reminder in every email).

Run:  python3 build_welcome_flow.py templates
"""
import pathlib, sys
from build_welcome import (SITE, CODE, DEN, COCOA, IVORY, LINEN, INK, MUTED, SERIF, SANS, IMG, PRODUCTS, T0,
                           link, button, headline, body, eyebrow, image, product_cell)

PHOTO = {
    "white_frames": IMG + "2FC71376-684A-4BDB-8131-C095955273B5.jpg?v=1791669973&width=1200",
    "couch": IMG + "instagram-image-83b01a3d-ba54-4cee-bb2f-d7ccf89344fb.jpg?v=1791738004&width=1200",
    "friends": IMG + "29E27CC0-0043-4BE6-A87E-9F89926B69DC.jpg?v=1789161927&width=1200",
}
FN = "{{ first_name|default:'' }}"


def topbar():
    return (f'<tr><td style="background:{COCOA};padding:11px 16px;text-align:center"><a href="{link()}" '
            f'style="font:600 10px/1.5 {SANS};letter-spacing:2px;text-transform:uppercase;color:{IVORY};text-decoration:none">'
            f'15% off your first pair &middot; tap to apply</a></td></tr>')


def logo():
    return (f'<tr><td style="padding:24px 20px 20px;text-align:center"><a href="{SITE}" '
            f'style="font:700 18px/1 {SANS};letter-spacing:8px;color:{INK};text-decoration:none">SOL KYST</a></td></tr>')


def section(inner, pad="40px 48px 28px"):
    return f'<tr><td class="pad" style="padding:{pad}">{inner}</td></tr>'


def code_box():
    return (f'<table width="100%" {T0} style="margin:8px 0 0"><tr><td style="border:1px dashed {COCOA};padding:16px;text-align:center">'
            f'<p style="margin:0 0 4px;font:600 10px/1.4 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">Your code</p>'
            f'<p style="margin:0;font:600 14px/1.4 {SANS};letter-spacing:2px;color:{INK}">{CODE.upper()}</p></td></tr></table>')


def footer():
    cell = (f'style="padding:16px 8px;text-align:center;font:600 10px/1.5 {SANS};letter-spacing:2px;'
            f'text-transform:uppercase;color:{MUTED}"')
    return (f'<tr><td style="padding:40px 20px 0"><table width="100%" {T0} style="border-top:1px solid {LINEN};border-bottom:1px solid {LINEN}"><tr>'
            f'<td {cell}>Free exchanges<br>45 days</td><td {cell}>Free shipping<br>over $150</td><td {cell}>As seen on<br>Dragons&#39; Den</td>'
            f'</tr></table></td></tr>'
            f'<tr><td style="padding:28px 30px 40px;text-align:center;font:400 12px/1.7 {SANS};color:{MUTED}">'
            f'Questions? Just hit reply. A real person reads every one.<br>'
            '{{ organization.name }} &middot; {{ organization.full_address }}<br>{% unsubscribe \'Unsubscribe\' %}</td></tr>')


def page(preheader, rows):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>SOL KYST</title><style>body{{margin:0;padding:0;background:{IVORY}}}'
            f'@media (max-width:480px){{.pad{{padding-left:22px!important;padding-right:22px!important}}.pcell{{padding:0 6px 20px!important}}'
            f'.cmp td{{padding:12px 8px!important;font-size:13px!important}}}}</style></head>'
            f'<body style="margin:0;background:{IVORY}"><div style="display:none;max-height:0;overflow:hidden">{preheader}</div>'
            f'<table width="100%" {T0} style="background:{IVORY}"><tr><td align="center">'
            f'<table width="600" {T0} style="width:100%;max-width:600px;background:{IVORY}">'
            f'{topbar()}{logo()}{rows}{footer()}</table></td></tr></table></body></html>')


# ---------- Email 4 (+1 day): ours vs theirs (KENT email 1) ----------
def comparison():
    rows = [
        ("Sizes", "Mini 135 &middot; Midi 145 &middot; Wide 158mm", "One size, about 140mm"),
        ("Fit", "Room for cheekbones and temples", "Pinches by lunch"),
        ("Frame", "Acetate, adjustable to your face", "Often thin plastic"),
        ("Lenses", "Polarized &middot; UV400", "Hit or miss"),
        ("Designed by", "A wide-face makeup artist", "An &ldquo;average&rdquo; face chart"),
        ("Wrong fit?", "Free exchanges for 45 days", "Back in the drawer"),
    ]
    head = (f'<tr><td style="padding:14px 10px;border-bottom:1px solid {LINEN}"></td>'
            f'<td style="padding:14px 10px;background:{COCOA};font:600 11px/1.4 {SANS};letter-spacing:2px;color:{IVORY};text-align:center">SOL KYST</td>'
            f'<td style="padding:14px 10px;border-bottom:1px solid {LINEN};font:600 11px/1.4 {SANS};letter-spacing:2px;color:{MUTED};text-align:center">STANDARD</td></tr>')
    body_rows = "".join(
        f'<tr><td style="padding:14px 10px;border-bottom:1px solid {LINEN};font:600 11px/1.4 {SANS};letter-spacing:1px;text-transform:uppercase;color:{MUTED}">{k}</td>'
        f'<td style="padding:14px 10px;border-bottom:1px solid {LINEN};background:#F4EEE8;font:400 14px/1.45 {SANS};color:{INK};text-align:center">{a}</td>'
        f'<td style="padding:14px 10px;border-bottom:1px solid {LINEN};font:italic 14px/1.45 {SERIF};color:{MUTED};text-align:center">{b}</td></tr>'
        for k, a, b in rows)
    return f'<table width="100%" {T0} class="cmp" style="margin:8px 0 28px">{head}{body_rows}</table>'


E4 = page("Standard frames come in one size. You don't.",
    f'<tr><td>{image(PHOTO["white_frames"], link("/collections/all"), "SOL KYST white frames")}</td></tr>'
    + section(eyebrow("Ours vs. theirs") + headline("Built for your face.<br>Not the average one.")
              + body("Most sunglasses are designed around one &ldquo;standard&rdquo; face. If yours is wider, you&#39;ve felt it: the squeeze at the temples, the red marks, the pair that slides down. Here&#39;s what&#39;s different about ours.")
              + comparison()
              + button("Claim my 15% off", link("/collections/all"), COCOA, COCOA)))

# ---------- Email 2 (+6h): the 30-second test (Mave & Chez "bend test") + fit guarantee ----------
def fit_table():
    rows = [("~135mm", "feel perfect", "Mini 135"), ("~135&ndash;140mm", "feel a little snug", "Midi 145"),
            ("~140mm+", "pinch at the temples", "Wide 158"), ("Any size", "and you want big", "Oversized")]
    return (f'<table width="100%" {T0} class="cmp" style="margin:4px 0 24px">'
            f'<tr><td style="padding:12px 10px;background:{COCOA};font:600 10px/1.4 {SANS};letter-spacing:2px;color:{IVORY}">YOURS MEASURE</td>'
            f'<td style="padding:12px 10px;background:{COCOA};font:600 10px/1.4 {SANS};letter-spacing:2px;color:{IVORY}">AND</td>'
            f'<td style="padding:12px 10px;background:{COCOA};font:600 10px/1.4 {SANS};letter-spacing:2px;color:{IVORY}">TRY</td></tr>'
            + "".join(f'<tr><td style="padding:13px 10px;border-bottom:1px solid {LINEN};font:400 14px/1.4 {SANS};color:{INK}">{a}</td>'
                      f'<td style="padding:13px 10px;border-bottom:1px solid {LINEN};font:italic 14px/1.4 {SERIF};color:{MUTED}">{b}</td>'
                      f'<td style="padding:13px 10px;border-bottom:1px solid {LINEN};font:600 14px/1.4 {SANS};color:{INK}">{c}</td></tr>'
                      for a, b, c in rows) + '</table>')


def step(n, text):
    return (f'<tr><td width="44" valign="top" style="padding:0 0 14px;font:italic 26px/1 {SERIF};color:{COCOA}">{n}</td>'
            f'<td style="padding:4px 0 14px;font:400 16px/1.55 {SANS};color:{INK}">{text}</td></tr>')


def quote(text, name, product):
    return (f'<tr><td style="padding:0 0 26px;text-align:center">'
            f'<p style="margin:0 0 8px;font:14px/1 {SANS};letter-spacing:3px;color:{COCOA}">&#9733;&#9733;&#9733;&#9733;&#9733;</p>'
            f'<p style="margin:0 0 10px;font:italic 19px/1.45 {SERIF};color:{INK}">&ldquo;{text}&rdquo;</p>'
            f'<p style="margin:0;font:600 10px/1.4 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">{name} &middot; {product}</p></td></tr>')


E2 = page("Grab the pair you wore today. Bet we know how this ends.",
    section(eyebrow("The 30-second test") + headline("Do your sunglasses<br>actually fit?")
            + body("Grab the pair you wore today. There&#39;s a quick test that shows whether they really fit your face, or just feel fine for the first ten minutes.")
            + f'<table width="100%" {T0} style="margin:8px 0 12px">'
            + step("1", "Grab the sunglasses you wear most.")
            + step("2", "Measure straight across the front, hinge to hinge.")
            + step("3", "Match it below.") + '</table>'
            + fit_table()
            + body("Pinching at 140mm? That&#39;s not your face. That&#39;s the frame. <b>Still torn? Reply with a selfie</b> (straight on, hair back) and we&#39;ll tell you your size.")
            + button("Shop in my size", link("/collections/all"), COCOA, COCOA), "40px 48px 36px")
    + f'<tr><td>{image(PHOTO["couch"], link("/collections/all"), "Trying on SOL KYST at home")}</td></tr>'
    + section(eyebrow("Our fit promise") + headline("Not in love?<br>No sweat.")
              + body("Wear them for a few days. If the fit isn&#39;t right, <b>exchanges are free for 45 days</b>, with no restocking fee. In Canada, drop them at any ReturnBear location. No box, no label.")
              + f'<table width="100%" {T0} style="margin:8px 0 0">'
              + quote("I had ordered the wide pair initially and felt they were too big so I exchanged them for a midi and they fit perfectly. The exchange process was painless and very easy.", "Jennifer K.", "Integrity")
              + '</table>'
              + f'<p style="margin:0 0 20px;font:italic 13px/1.5 {SERIF};color:{MUTED};text-align:center">Petite, clearance and RX orders are final sale, so send us a selfie first if you&#39;re unsure.</p>'
              + code_box(), "40px 48px 12px"))


# ---------- Email 3 (+4h): founder story + reviews (Mave & Chez "Why we built these") ----------
E3 = page("Why I started SOL KYST, and your 15% is still here.",
    f'<tr><td>{image(PHOTO["friends"], link("/pages/about"), "SOL KYST")}</td></tr>'
    + section(eyebrow("A note from Meghan") + headline("The pair I<br>couldn&#39;t find.")
              + body("Hi, it&#39;s Meghan. I&#39;m the founder of SOL KYST, and I want to tell you why this brand exists, because honestly, it&#39;s a little personal.")
              + body("I&#39;ve been a makeup artist for years, so I spend a lot of time looking at faces. And for just as long, I couldn&#39;t find a single pair of sunglasses that fit mine. I have a wide face. Every pair pinched my temples, left red marks by lunch and looked a size too small. I genuinely thought something was wrong with my face.")
              + body("Turns out it was the frames. Almost everything out there comes in one size, about 140mm, and if that&#39;s not you, well, good luck.")
              + body("So I designed the pair I couldn&#39;t find, in three widths: <b>Mini 135, Midi 145 and Wide 158mm</b>. I posted a pre-order video and it brought in <b>$10,000 in 24 hours</b>. My heart was so full. That&#39;s when I knew it wasn&#39;t just me.")
              + body("Then we walked into CBC&#39;s Dragons&#39; Den, and two Dragons wanted to partner with us. I still kind of can&#39;t believe I get to type that sentence.")
              + body("So if you&#39;ve ever tried on pair after pair and walked out with nothing, this one&#39;s for you. Your face was never the problem.")
              + f'<p style="margin:8px 0 26px;font:italic 18px/1.4 {SERIF};color:{INK};text-align:center">Love, Meghan<br><span style="font:600 10px/1.4 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">Founder, SOL KYST</span></p>'
              + button("Watch our episode", DEN, COCOA, COCOA)
              + f'<p style="margin:18px 0 0;text-align:center"><a href="{SITE}/pages/about" style="font:600 11px/1 {SANS};letter-spacing:2px;text-transform:uppercase;color:{COCOA}">Read the full story &rarr;</a></p>', "40px 48px 12px")
    + f'<tr><td class="pad" style="background:{COCOA};padding:30px 40px 32px;text-align:center">'
      + eyebrow("Don&#39;t forget", LINEN) + headline("Your 15% off is still waiting.", IVORY, 26)
      + button("Claim my 15% off", link("/collections/all"), IVORY, IVORY)
      + f'<p style="margin:16px 0 0;font:600 11px/1.5 {SANS};letter-spacing:2px;text-transform:uppercase;color:{LINEN}">Code: {CODE.upper()}</p></td></tr>'
    + section(eyebrow("Wide faces who made the switch") + headline("Finally, a pair that fits.", INK, 28)
              + f'<table width="100%" {T0} style="margin:12px 0 4px">'
              + quote("This is the first pair of glasses I&#39;ve owned that doesn&#39;t give me a headache or leave marks on my face. They fit my wiiiide face PERFECTLY!", "Melina T.", "Integrity")
              + quote("I always thought my round face shape was why all sunglasses looked slightly off, but I just needed wider sunglasses!", "Mary H.", "Monarch")
              + quote("With my very wide face, even the widest frames looked incredibly awkward and dorky. Enter the MONARCH!!", "Midori P.", "Monarch")
              + '</table>' + button("Find my pair", link("/collections/all"), COCOA, COCOA), "44px 48px 12px"))

# ---------- Email 5 (+2 days): start here (KENT "the trio / the work week") ----------
def pick(label, name, sub, img, path):
    return (f'<tr><td style="padding:0 0 28px"><table width="100%" {T0}><tr>'
            f'<td width="46%" valign="middle"><a href="{link(path)}"><img src="{img}" width="250" alt="{name}" '
            f'style="display:block;width:100%;height:auto;border:0;background:#F4EEE8"></a></td>'
            f'<td width="54%" valign="middle" style="padding-left:22px">'
            f'<p style="margin:0 0 6px;font:600 10px/1.4 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">{label}</p>'
            f'<p style="margin:0 0 8px;font:italic 26px/1.1 {SERIF};color:{INK}">{name}</p>'
            f'<p style="margin:0 0 12px;font:400 14px/1.5 {SANS};color:{INK}">{sub}</p>'
            f'<a href="{link(path)}" style="font:600 11px/1 {SANS};letter-spacing:2px;text-transform:uppercase;color:{COCOA}">Shop &rarr;</a>'
            f'</td></tr></table></td></tr>')


P = {name: (img, path) for name, _, img, path in PRODUCTS}
E5 = page("Four pairs, four moods. Start with one.",
    f'<tr><td>{image(PHOTO["friends"], link("/collections/all"), "Friends in SOL KYST")}</td></tr>'
    + section(eyebrow("Start here") + headline("Not sure where<br>to start?")
              + body("These are the pairs most people start with. Pick the one that feels most like you.")
              + f'<table width="100%" {T0} style="margin:20px 0 4px">'
              + pick("The everyday", "Integrity", "The sleek black rectangle. Goes with everything you own.", *P["INTEGRITY"])
              + pick("The classic", "Monarch", "The tortoise rectangle. Warm, polished, easy.", *P["MONARCH"])
              + pick("The statement", "Hangover", "Big, dark and forgiving. For the days you want to disappear.", *P["HANGOVER"])
              + pick("The fun one", "Sweet Heart", "Barbie&trade; x Sol Kyst. Peachy-pink hearts and our #2 style this year.", *P["SWEET HEART"])
              + '</table>' + button("Claim my 15% off", link("/collections/all"), COCOA, COCOA), "40px 40px 28px")
    + f'<tr><td style="background:#F4EEE8;padding:40px 48px;text-align:center" class="pad">'
      + eyebrow("What you get") + headline("Every pair comes with", INK, 26)
      + body("A hard protective case, a microfibre cloth and our sliding gift box. Free shipping over $150, and orders to Canada and the US over $150 ship duty-free.")
      + f'<p style="margin:8px 0 0;font:italic 15px/1.5 {SERIF};color:{MUTED}">The brand two Dragons wanted in on. <a href="{DEN}" style="color:{COCOA}">Watch the episode</a></p>'
      + '</td></tr>')

# ---------- Email 6: personal note from Meghan (voice: VOICE.md) (plain, KENT-style "feedback? send us your thoughts") ----------
E6 = ('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SOL KYST</title>'
      '<style>body{margin:0;background:#fff}td,p{font-family:Arial,sans-serif;font-size:15px;line-height:1.6;color:#222}p{margin:0 0 16px}a{color:#3B2C27}</style></head>'
      '<body><div style="display:none;max-height:0;overflow:hidden">Your 15% is still here. And a quick question.</div>'
      f'<table width="100%" {T0}><tr><td style="padding:24px 20px"><table width="560" {T0} style="width:100%;max-width:560px"><tr><td>'
      f'<p>Hi {FN},</p>'
      '<p>It&#39;s Meghan again. Quick one, I promise.</p>'
      '<p>I&#39;ll be honest, I&#39;m not great at the salesy stuff. I&#39;d rather just talk to you.</p>'
      '<p>If you&#39;ve been eyeing a pair but something&#39;s holding you back, I&#39;d genuinely love to know what it is. The size? The price? Not sure what&#39;ll suit your face? <b>Just hit reply and tell me.</b> I read these, and I&#39;ll help you figure it out, even if the answer is that we&#39;re not the right fit for you.</p>'
      '<p>Or send me a selfie (straight on, hair back) and I&#39;ll tell you your size. That&#39;s honestly one of my favourite parts of this job.</p>'
      f'<p>Your 15% off is still here whenever you&#39;re ready: <a href="{link("/collections/all")}"><b>{CODE.upper()}</b></a> (it applies automatically when you tap).</p>'
      '<p>Let&#39;s get you Kyst,<br>Meghan<br>Founder, SOL KYST</p>'
      '<p>P.S. Running a small company means wearing a lot of hats. Reading your emails is my favourite one.</p>'
      '<p style="margin-top:40px;font-size:11px;color:#999">{{ organization.name }} &middot; {{ organization.full_address }} &middot; {% unsubscribe \'Unsubscribe\' %}</p>'
      '</td></tr></table></td></tr></table></body></html>')

EMAILS = {
    "welcome-2-the-test": E2,
    "welcome-3-founder-story": E3,
    "welcome-4-ours-vs-theirs": E4,
    "welcome-5-start-here": E5,
    "welcome-6-meghan": E6,
}

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "templates")
    for name, html in EMAILS.items():
        (out / f"{name}.html").write_text(html)
        print(name, len(html))
