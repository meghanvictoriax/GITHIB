import pathlib, sys
OUT = pathlib.Path(sys.argv[1])
SITE = "https://www.solkyst.ca"
INK, MUTED, BG, CARD, SOFT = "#1A1A1A", "#6B6460", "#F4EEE8", "#FFFFFF", "#F6E3D8"
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

CSS = """body{margin:0;padding:0;background:#F4EEE8}
.w{background:#F4EEE8;padding:24px 12px}
.c{width:100%;max-width:600px;background:#fff;border-radius:16px;overflow:hidden}
.c td,.c p,.c a,.c h1{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#1A1A1A}
.logo{padding:28px 40px 20px;text-align:center;border-bottom:1px solid #EFE7E0}
.logo a{font-size:20px;font-weight:700;letter-spacing:7px;text-decoration:none}
.b{padding:36px 40px 8px}
h1{margin:0 0 20px;font-size:28px;line-height:1.2;font-weight:700;letter-spacing:-.3px}
p{margin:0 0 16px;font-size:16px;line-height:1.6}
p.k{margin:24px 0 8px;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#6B6460}
.m{color:#6B6460;font-size:14px}
.btn{margin:28px 0 8px}.btn td{border-radius:999px;background:#1A1A1A}
.btn a{display:inline-block;padding:15px 30px;font-size:15px;font-weight:600;color:#fff;text-decoration:none;border-radius:999px}
.pc{margin:8px 0 4px;background:#F4EEE8;border-radius:12px}.pc td{padding:16px;font-size:16px}
.pc img{display:block;width:120px;height:auto;border-radius:8px}.pc a{text-decoration:none;font-weight:700}
.ft{border:1px solid #EFE7E0;margin:4px 0 8px}.ft td{padding:10px 12px;font-size:14px;border-bottom:1px solid #EFE7E0}
.ft .hd td{background:#F6E3D8;font-weight:700;font-size:12px;letter-spacing:1px;text-transform:uppercase}
.f{padding:28px 40px 36px;text-align:center;font-size:12px;line-height:1.6;color:#6B6460}.f a{color:#6B6460}
.hero img{display:block;width:100%;max-width:600px;height:auto}
@media (max-width:480px){.w{padding:12px 8px!important}.logo{padding:22px 20px 16px!important}.b{padding:28px 20px 4px!important}.f{padding:24px 20px 28px!important}h1{font-size:24px!important}.pc td{padding:12px!important}.pc td.i{width:84px!important}.pc img{width:72px!important}.ft td{padding:8px 6px!important;font-size:13px!important}}"""

T0 = 'role="presentation" cellpadding="0" cellspacing="0" border="0"'
def btn(label, href):
    return f'<table {T0} class="btn"><tr><td><a href="{href}">{label}</a></td></tr></table>'
def p(t, cls=""):
    return f'<p class="{cls}">{t}</p>' if cls else f'<p>{t}</p>'
def h(t): return f'<h1>{t}</h1>'
def h3(t): return f'<p class="k">{t}</p>'
def sign(t="Let&#39;s get you Kyst,<br>SOL KYST"): return p(t)
FOOT = ('<tr><td class="f">Free exchanges for 45 days &middot; Free shipping over $150<br>'
        '{{ organization.name }} &middot; {{ organization.full_address }}<br>{% unsubscribe \'Unsubscribe\' %}</td></tr>')
def page(preheader, inner, top_image=None):
    hero = f'<tr><td class="hero">{top_image}</td></tr>' if top_image else ""
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SOL KYST</title><style>{CSS}</style></head>'
            f'<body><div style="display:none;max-height:0;overflow:hidden">{preheader}</div>'
            f'<table width="100%" {T0} class="w"><tr><td align="center"><table width="600" {T0} class="c">'
            f'<tr><td class="logo"><a href="{SITE}">SOL KYST</a></td></tr>{hero}<tr><td class="b">{inner}</td></tr>{FOOT}'
            '</table></td></tr></table></body></html>')
def plain_page(preheader, inner):
    return ('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SOL KYST</title>'
            '<style>body{margin:0;background:#fff}td,p{font-family:Arial,sans-serif;font-size:15px;line-height:1.6;color:#222}p{margin:0 0 16px}.u{margin-top:40px;font-size:11px;color:#999}.u a{color:#999}</style></head>'
            f'<body><div style="display:none;max-height:0;overflow:hidden">{preheader}</div>'
            f'<table width="100%" {T0}><tr><td style="padding:24px 20px"><table width="560" {T0} style="width:100%;max-width:560px"><tr><td>{inner}'
            '<p class="u">{{ organization.name }} &middot; {{ organization.full_address }} &middot; {% unsubscribe \'Unsubscribe\' %}</p></td></tr></table></td></tr></table></body></html>')
def pp(t): return f'<p>{t}</p>'
def product_card(name, img, url, sub=""):
    im = f'<td width="140" class="i"><a href="{url}"><img src="{img}" width="120" alt="{name}"></a></td>' if img else ""
    sb = f'<br><span class="m">{sub}</span>' if sub else ""
    return f'<table width="100%" {T0} class="pc"><tr>{im}<td><a href="{url}">{name}</a>{sb}</td></tr></table>'
def row(a,b,c, head=False):
    return f'<tr{" class=hd" if head else ""}><td>{a}</td><td>{b}</td><td>{c}</td></tr>'
FIT_TABLE = (f'<table width="100%" {T0} class="ft">' + row("Yours measure","And feel","Try",True)
    + row("~135mm","perfect","<b>Mini</b> 135mm") + row("~135&ndash;140mm","a little snug","<b>Midi</b> 145mm")
    + row("~140mm+","tight at the temples","<b>Wide</b> 158mm") + row("anything","you want <i>big</i>","<b>Oversized</b> 145&ndash;150mm") + '</table>')

ATC_NAME = "{{ event|lookup:'Product Name'|default:'your pair' }}"
ATC_URL = "{{ event.URL|default:'https://www.solkyst.ca/cart' }}"
ATC_CARD = ("{% if event.ImageURL %}" + product_card(ATC_NAME, "{{ event.ImageURL }}", ATC_URL, "{{ event|lookup:'Variant Name'|default:'' }}") + "{% endif %}")
FN = "{{ first_name|default:'babe' }}"

T = {}
T["atc1-fit-check"] = ("SOL KYST | ATC 1 - The fit check", page("A 30-second test with a pair you already own",
    h("Not sure about the size?")
    + p(f"Hey {FN},")
    + p(f"You left <b>{ATC_NAME}</b> in your cart, and we&#39;d bet it&#39;s not the style you&#39;re unsure about. It&#39;s the fit.")
    + ATC_CARD
    + p("Fair. If you&#39;ve got a wider face, you&#39;ve probably spent years buying sunnies that pinch your temples by lunchtime. So let&#39;s take the guessing out of it.")
    + h3("The 30-second fit check")
    + p("Grab the sunglasses you wear most and measure straight across the front, hinge to hinge.")
    + FIT_TABLE
    + p("Still torn? <b>Reply with a selfie</b> (straight on, hair back) and we&#39;ll tell you your size. A real person answers every one.")
    + p("And if they still don&#39;t feel right when they arrive? <b>Exchanges are free for 45 days</b>, with no restocking fee. <span class=\"m\">(Petite sizes are final sale, so if you&#39;re going Petite, send the selfie first.)</span>")
    + btn("Back to my cart &rarr;", ATC_URL) + sign()))

T["atc2-value"] = ("SOL KYST | ATC 2 - What you get", page("(and why they'll outlast every pair you've owned)",
    h("Why our sunnies cost more than the drugstore ones")
    + p(f"{{{{ first_name|default:'Hi' }}}},")
    + p("Real talk: SOL KYST isn&#39;t the cheapest pair you&#39;ll find. Here&#39;s where the money goes.")
    + h3("Acetate, not plastic") + p("The material used in premium frames. It&#39;s warmer and heavier in the hand, and it can be adjusted to fit <i>your</i> face.")
    + h3("Polarized + UV400") + p("Cuts glare and blocks 100% of UVA/UVB.")
    + h3("Sized for you, not the &quot;average&quot; face") + p("&quot;Standard&quot; sunglasses come in one size, around 140mm wide. Ours go up to 158mm. That 18mm is the difference between a headache by noon and forgetting you&#39;re wearing them.")
    + h3("The box") + p("Hard protective case, microfibre cloth and our sliding gift box. It&#39;s giving &quot;treat yourself&quot;, and it makes a very good gift.")
    + h3("Zero risk on the fit") + p("Free exchanges for 45 days, no restocking fee. In Canada, drop returns at any ReturnBear location with no box and no label.")
    + h3("No surprise fees") + p("Free shipping over $150, and orders to Canada and the US over $150 ship duty-free.")
    + p("One good pair that fits beats three that sit in a drawer.")
    + ATC_CARD
    + btn("Finish what you started &rarr;", ATC_URL)
    + p("SOL KYST")
    + p("P.S. <b>KIN</b> is our #1 pair this year. If you&#39;re between styles, start there.", "m")))

T["pp1a-founder"] = ("SOL KYST | PP 1A - Founder thank-you", plain_page("and one quick question for you",
    pp("Hey {{ first_name|default:'there' }},")
    + pp("I&#39;m Meghan, the founder of SOL KYST.")
    + pp("Before this I was a makeup artist. When that work stopped in 2020, I finally did something about a problem I&#39;d had my whole life: I have a wide, cheeky face, and sunglasses just didn&#39;t fit it. So I designed a pair that did. That was the Kyst Eye. We put it up for pre-order in early 2021, and one video brought in over $10,000 in orders in the first 24 hours. Turns out a lot of us had been squeezing into frames made for someone else.")
    + pp("So when someone like you takes a chance on a small Canadian brand instead of the big names, I notice. Thank you, genuinely.")
    + pp("Your order ships from Hamilton within 3&ndash;5 business days, and you&#39;ll get a tracking link the moment it leaves.")
    + pp("<b>One quick question:</b> what finally made you buy? A friend, a TikTok, the sizing, the Barbie collab, something else? Just hit reply. I read every answer, and it honestly shapes what we make next.")
    + pp("Meghan<br>Founder, SOL KYST")))

T["pp1b-repeat"] = ("SOL KYST | PP 1B - Repeat customer", page("Your order's being packed right now",
    h("You came back!")
    + p(f"{{{{ first_name|default:'Hey' }}}},")
    + p("There&#39;s nothing better for a small brand than a repeat customer. It means the first pair actually fit, and that&#39;s the whole point of what we do.")
    + p("Your order ships within 3&ndash;5 business days, and tracking will follow as soon as it does.")
    + p("As a thank-you, you&#39;re first in line for our next drop. We&#39;ll email you before it goes public.")
    + btn("View my order &rarr;", f"{SITE}/account") + sign("xo,<br>SOL KYST")))

T["pp2-three-day-rule"] = ("SOL KYST | PP 2 - The 3-day rule", page("New acetate needs a minute. Here's how to help it along.",
    h("The 3-day rule")
    + p(f"{{{{ first_name|default:'Hi' }}}},")
    + p("Your sunnies should have landed by now. One thing nobody tells you about good frames:")
    + p("<b>Acetate settles.</b> For the first few days, new frames can feel a touch firm behind the ears or snug at the temples. That&#39;s normal. The material relaxes and shapes to you with wear.")
    + p("<b>Give them 3 days of real wear.</b> Then check in with yourself:")
    + h3("Still tight after 3 days?") + p("Swap them for the next size up. <b>Exchanges are free for 45 days after delivery</b>, with no restocking fee. In Canada, drop them at any ReturnBear location with no box and no label.")
    + btn("Start an exchange &rarr;", f"{SITE}/account")
    + h3("Sliding down your nose?") + p("Reply to us first. A quick adjustment at an optical shop usually fixes it, but returns have to come back in their original state, so check with us before anyone bends anything.")
    + h3("Perfect?") + p("Amazing. Keep them in the hard case, clean them only with the microfibre cloth, and take them off with two hands so the hinges stay tight.")
    + sign("SOL KYST")))

P = {
 "integrity": ("INTEGRITY", "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/547973D9-7C97-4ACD-BD1B-C47CF3CCE67F.jpg?v=1767378147", f"{SITE}/products/integrity", "Sleek black rectangle"),
 "monarch": ("MONARCH", "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/Monarch_97e3b29d-5e10-42fe-a0ed-656639bea6ef.png?v=1766799619", f"{SITE}/products/monarch", "The tortoise rectangle"),
 "sweetheart": ("Barbie&trade; x Sol Kyst Sweet Heart", "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/Cut_Out_-_Barbie_-_4.png?v=1784148545", f"{SITE}/products/barbie%E2%84%A2-x-sol-kyst-1970s-superstar-hearts", "Peachy-pink hearts &middot; our #2 seller this year"),
 "kin": ("KIN", "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/IMG-6013.jpg?v=1773266986", f"{SITE}/products/kin-sunglasses-for-wide-face-wide-fit-frames", "Our #1 pair this year"),
}
T["pp3-next-pair"] = ("SOL KYST | PP 3 - You know your size now", page("Your next pair is a 30-second decision",
    h("You know your size now. That changes things.")
    + p(f"{{{{ first_name|default:'Hey' }}}},")
    + p("The hardest part of buying from us is figuring out your size. You&#39;ve done that now.")
    + p("Which means your next pair is easy. <b>Same size, different mood.</b>")
    + h3("Went bold? Try a classic") + product_card(*P["integrity"]) + product_card(*P["monarch"])
    + h3("Went classic? Have some fun") + product_card(*P["sweetheart"]) + product_card(*P["kin"])
    + btn("Shop in my size &rarr;", f"{SITE}/collections/all") + sign("SOL KYST")))

BIS_NAME = "{{ event.ProductName|default:'Your pair' }}"
BIS_URL = "{{ event.URL|default:'https://www.solkyst.ca/collections/all' }}"
BIS_IMG = "{% if event.ImageURL %}<a href=\"" + BIS_URL + "\"><img src=\"{{ event.ImageURL }}\" width=\"600\" alt=\"\" ></a>{% endif %}"
T["bis1-its-back"] = ("SOL KYST | BIS 1 - It's back", page("Sizes go fast, so check yours",
    h(f"It&#39;s back: {BIS_NAME}")
    + p(f"{{{{ first_name|default:'Hey' }}}},")
    + p(f"<b>{BIS_NAME}</b> just restocked, and you&#39;re hearing about it before anyone else.")
    + p("Heads up: restocks don&#39;t sell out evenly. The most popular sizes go first, so if you know yours, don&#39;t sit on this one.")
    + btn("Grab my size &rarr;", BIS_URL)
    + p("Not sure which size? Mini 135mm &middot; Midi 145mm &middot; Wide 158mm. Measure a pair you own hinge to hinge and go one up if they pinch. Guess wrong? Exchanges are free for 45 days.", "m")
    + sign("SOL KYST"), top_image=BIS_IMG))

T["bis2-sizes-moving"] = ("SOL KYST | BIS 2 - Sizes moving", page("Quick heads up before it's gone again",
    h("Sizes are moving")
    + p(f"{{{{ first_name|default:'Hi' }}}}, quick one.")
    + p(f"<b>{BIS_NAME}</b> is selling through faster than last time. If you still want it, now&#39;s the moment.")
    + btn(f"Shop {BIS_NAME} &rarr;", BIS_URL) + sign("SOL KYST"), top_image=BIS_IMG))

OUT.mkdir(parents=True, exist_ok=True)
for k,(name,html) in T.items():
    (OUT/f"{k}.html").write_text(html)
    print(k, len(html), name)
