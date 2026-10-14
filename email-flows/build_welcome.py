"""Welcome email modelled on the Mave & Chez welcome layout, in SOL KYST's editorial style.

Run:  python3 build_welcome.py templates/welcome-15.html
"""
import pathlib, sys

SITE = "https://www.solkyst.ca"
CODE = "WELCOME15"  # placeholder: create this 15% first-order code in Shopify before going live
DISC = f"{SITE}/discount/{CODE}"
DEN = "https://www.cbc.ca/dragonsden"  # placeholder: swap for the exact SOL KYST episode/pitch link
COCOA, IVORY, LINEN, INK, MUTED = "#3B2C27", "#FAF9F6", "#DFD1C0", "#1E1512", "#6B6460"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"
IMG = "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/"
HERO = IMG + "instagram-image-bfd951e5-a6ff-4337-8afe-0c43091dae24.jpg?v=1791997206&width=1200"
MID = IMG + "08761334-FDD5-4052-AAF3-2AE402CD4769.jpg?v=1791669974&width=1200"
PRODUCTS = [
    ("INTEGRITY", "The sleek black rectangle", IMG + "547973D9-7C97-4ACD-BD1B-C47CF3CCE67F.jpg?v=1767378147&width=600", "/products/integrity"),
    ("MONARCH", "The tortoise rectangle", IMG + "Monarch_97e3b29d-5e10-42fe-a0ed-656639bea6ef.png?v=1766799619&width=600", "/products/monarch"),
    ("HANGOVER", "Big, dark and forgiving", IMG + "3_14b8037b-4300-4470-aa92-8b5633941ac2.png?v=1766799117&width=600", "/products/hangover"),
    ("SWEET HEART", "Barbie&trade; x Sol Kyst", IMG + "Cut_Out_-_Barbie_-_4.png?v=1784148545&width=600", "/products/barbie%E2%84%A2-x-sol-kyst-1970s-superstar-hearts"),
]
T0 = 'role="presentation" cellpadding="0" cellspacing="0" border="0"'

def link(path=""):
    return f"{DISC}?redirect={path}" if path else DISC

def button(label, href, fg, border):
    return (f'<table {T0} align="center" style="margin:0 auto"><tr><td style="border:1.5px solid {border}">'
            f'<a href="{href}" style="display:inline-block;padding:14px 34px;font:600 13px/1 {SANS};letter-spacing:2px;'
            f'text-transform:uppercase;color:{fg};text-decoration:none">{label}</a></td></tr></table>')

def headline(text, color=INK, size=34):
    return (f'<p style="margin:0 0 18px;font:italic 400 {size}px/1.15 {SERIF};color:{color};text-align:center">{text}</p>')

def body(text, color=INK):
    return f'<p style="margin:0 0 16px;font:400 16px/1.65 {SANS};color:{color};text-align:center">{text}</p>'

def eyebrow(text, color=MUTED):
    return (f'<p style="margin:0 0 14px;font:600 11px/1.4 {SANS};letter-spacing:3px;text-transform:uppercase;'
            f'color:{color};text-align:center">{text}</p>')

def image(src, href, alt):
    return f'<a href="{href}"><img src="{src}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0"></a>'

def product_cell(name, sub, img, path):
    return (f'<td class="pcell" width="50%" valign="top" style="padding:0 8px 24px;text-align:center">'
            f'<a href="{link(path)}" style="text-decoration:none"><img src="{img}" width="268" alt="{name}" '
            f'style="display:block;width:100%;height:auto;border:0;background:#F4EEE8">'
            f'<p style="margin:12px 0 2px;font:600 12px/1.4 {SANS};letter-spacing:2px;color:{INK}">{name}</p>'
            f'<p style="margin:0;font:italic 14px/1.4 {SERIF};color:{MUTED}">{sub}</p></a></td>')

grid = "".join(
    f"<tr>{product_cell(*PRODUCTS[i])}{product_cell(*PRODUCTS[i + 1])}</tr>" for i in (0, 2))

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SOL KYST</title><style>
body{{margin:0;padding:0;background:{IVORY}}}
@media (max-width:480px){{.pad{{padding-left:22px!important;padding-right:22px!important}}.pcell{{padding:0 6px 20px!important}}}}
</style></head><body style="margin:0;background:{IVORY}">
<div style="display:none;max-height:0;overflow:hidden">Your 15% off is inside. Sunglasses built for wide faces.</div>
<table width="100%" {T0} style="background:{IVORY}"><tr><td align="center">
<table width="600" {T0} style="width:100%;max-width:600px;background:{IVORY}">

<tr><td style="padding:26px 20px 22px;text-align:center"><a href="{SITE}" style="font:700 18px/1 {SANS};letter-spacing:8px;color:{INK};text-decoration:none">SOL KYST</a></td></tr>

<tr><td class="pad" style="background:{COCOA};padding:30px 40px 32px;text-align:center">
{eyebrow("Welcome &middot; As seen on CBC&#39;s Dragons&#39; Den", LINEN)}
{headline("15% off your first pair.", IVORY, 30)}
{button(f"Use code: {CODE}", link(), IVORY, IVORY)}
</td></tr>

<tr><td>{image(HERO, link("/collections/all"), "Close-up in SOL KYST sunglasses")}</td></tr>

<tr><td class="pad" style="padding:44px 48px 12px">
{headline("Your face deserves better.")}
{button(f"Use code: {CODE}", link("/collections/all"), COCOA, COCOA)}
</td></tr>

<tr><td class="pad" style="padding:28px 56px 28px">
{body("Most sunglasses come in one size: about 140mm. If you have a wider face, you know how that ends. Pinched temples by lunch, red marks, a drawer full of pairs you don&#39;t wear.")}
{body("SOL KYST is built around what wide faces actually need. <b>Mini 135, Midi 145 and Wide 158mm.</b> Real acetate, polarized lenses, UV400.")}
{body("Wrong size? <b>Exchanges are free for 45 days.</b>")}
</td></tr>

<tr><td>{image(MID, link("/collections/all"), "SOL KYST in the closet")}</td></tr>

<tr><td class="pad" style="padding:48px 52px 36px;text-align:center">
{eyebrow("As seen on CBC&#39;s Dragons&#39; Den")}
{headline("Two Dragons<br>wanted in.")}
{body("We walked into the Den with sunglasses built for wide faces, and two Dragons wanted to partner. We walked out with a deal. Not because of the pitch. Because the fit is that good.")}
{button("Watch our episode", DEN, COCOA, COCOA)}
<p style="margin:28px 0 0;font:italic 16px/1.6 {SERIF};color:{MUTED};text-align:center">It started with Meghan, a makeup artist with a wide face who designed the pair she couldn&#39;t find. Her pre-order video brought in $10,000 in 24 hours. <a href="{SITE}/pages/about" style="color:{COCOA}">Read our story</a></p>
</td></tr>

<tr><td class="pad" style="padding:8px 32px 8px">
{eyebrow("Start here")}
<table width="100%" {T0}>{grid}</table>
{button(f"Shop with {CODE}", link("/collections/all"), COCOA, COCOA)}
</td></tr>

<tr><td style="padding:40px 20px 0"><table width="100%" {T0} style="border-top:1px solid {LINEN};border-bottom:1px solid {LINEN}"><tr>
<td style="padding:16px 8px;text-align:center;font:600 10px/1.5 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">Free exchanges<br>45 days</td>
<td style="padding:16px 8px;text-align:center;font:600 10px/1.5 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">Free shipping<br>over $150</td>
<td style="padding:16px 8px;text-align:center;font:600 10px/1.5 {SANS};letter-spacing:2px;text-transform:uppercase;color:{MUTED}">Duty-free CA &amp; US<br>over $150</td>
</tr></table></td></tr>

<tr><td style="padding:28px 30px 40px;text-align:center;font:400 12px/1.7 {SANS};color:{MUTED}">
Let&#39;s get you Kyst.<br>
{{{{ organization.name }}}} &middot; {{{{ organization.full_address }}}}<br>
{{% unsubscribe 'Unsubscribe' %}}
</td></tr>

</table></td></tr></table></body></html>"""

out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "templates/welcome-15.html")
out.write_text(html)
print(out, len(html))
