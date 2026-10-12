import re, html, pathlib, sys
T = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
KIN_IMG = "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/IMG-6013.jpg?v=1773266986"
AG_IMG = "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/ImaybesadbutatleastIhavegoodhair_4x5in_4x4in.png?v=1767207299"
CTX_ATC = {"Product Name":"KIN","URL":"https://www.solkyst.ca/products/kin-sunglasses-for-wide-face-wide-fit-frames","ImageURL":KIN_IMG,"Variant Name":"Wide"}
CTX_BIS = {"ProductName":"AFTER GLOW","URL":"https://www.solkyst.ca/products/hangover-chic","ImageURL":AG_IMG}

def render(src, ev):
    src = re.sub(r"\{% if event\.ImageURL %\}(.*?)\{% endif %\}", lambda m: m.group(1) if ev.get("ImageURL") else "", src, flags=re.S)
    src = src.replace("{% unsubscribe 'Unsubscribe' %}", '<a href="#">Unsubscribe</a>')
    def var(m):
        expr = m.group(1).strip(); parts = expr.split("|"); base = parts[0].strip(); val = None
        if base == "first_name": val = "Jess"
        elif base == "organization.name": val = "SOL KYST"
        elif base == "organization.full_address": val = "Hamilton, Ontario, Canada"
        elif base.startswith("event."): val = ev.get(base[6:])
        for f in parts[1:]:
            f = f.strip()
            if f.startswith("lookup:"): val = ev.get(f[8:-1])
            elif f.startswith("default:") and not val: val = f[9:-1]
        return val or ""
    return re.sub(r"\{\{(.*?)\}\}", var, src)

FLOWS = [
 ("Added to Cart", "Starts when someone adds to cart but doesn't reach checkout. No discount, because your live checkout flow already closes with one.", [
   ("atc1-fit-check", "1 hour after add to cart", "SOL KYST", "Not sure about the size? 🤭", "A 30-second test with a pair you already own", CTX_ATC),
   ("atc2-value", "+1 day", "SOL KYST", "Why our sunnies cost more than the ones at the drugstore", "(and why they'll outlast every pair you've owned)", CTX_ATC)]),
 ("Post-Purchase", "Starts on Placed Order. First-time buyers get the founder email and repeat buyers get 1B; both then get emails 2 and 3.", [
   ("pp1a-founder", "Immediately · first order", "Meghan at SOL KYST", "you did it", "and one quick question for you", {}),
   ("pp1b-repeat", "Immediately · repeat customer", "SOL KYST", "Back for another pair? We're blushing 🤭", "Your order's being packed right now", {}),
   ("pp2-three-day-rule", "+6 days", "SOL KYST", "Read this before you decide how they fit", "New acetate needs a minute. Here's how to help it along.", {}),
   ("pp3-next-pair", "+14 days", "SOL KYST", "You know your size now. That changes things.", "Your next pair is a 30-second decision", {})]),
 ("Back in Stock", "Starts when someone clicks “notify me” and fires when the item restocks.", [
   ("bis1-its-back", "When the item restocks", "SOL KYST", "It's back: AFTER GLOW", "Sizes go fast, so check yours", CTX_BIS),
   ("bis2-sizes-moving", "+1 day · only if they haven't bought", "SOL KYST", "Sizes are moving on AFTER GLOW", "Quick heads up before it's gone again", CTX_BIS)]),
]
cards = []; nav = []
n = 0
for fname, fdesc, emails in FLOWS:
    fid = fname.lower().replace(" ","-")
    nav.append(f'<a href="#{fid}">{fname}</a>')
    cards.append(f'<section id="{fid}"><h2>{fname}</h2><p class="fd">{fdesc}</p>')
    for key, when, frm, subj, pre, ctx in emails:
        n += 1
        doc = render((T/f"{key}.html").read_text(), ctx)
        cards.append(f'''<article class="em"><div class="meta"><span class="when">{html.escape(when)}</span>
<div class="inbox"><div class="av">{frm[0]}</div><div class="it"><div class="fr">{html.escape(frm)}</div><div class="sj">{html.escape(subj)}</div><div class="pv">{html.escape(pre)}</div></div></div></div>
<div class="frame"><iframe title="{html.escape(subj)}" srcdoc="{html.escape(doc, quote=True)}" loading="lazy" onload="fit(this)"></iframe></div></article>''')
    cards.append('</section>')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SOL KYST Flow Preview</title>
<style>
:root{{--bg:#F4EEE8;--panel:#FFFFFF;--ink:#1A1A1A;--muted:#6B6460;--line:#E6DCD3;--chip:#F6E3D8}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151312;--panel:#201D1B;--ink:#F3EEE9;--muted:#A79F99;--line:#34302D;--chip:#3A2C25}}}}
:root[data-theme="dark"]{{--bg:#151312;--panel:#201D1B;--ink:#F3EEE9;--muted:#A79F99;--line:#34302D;--chip:#3A2C25}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}}
header{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:14px 16px}}
.hw{{max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center}}
h1{{font-size:16px;letter-spacing:4px;margin:0;font-weight:700}}
nav{{display:flex;gap:6px;flex-wrap:wrap}}nav a{{color:var(--ink);text-decoration:none;font-size:13px;padding:5px 11px;border:1px solid var(--line);border-radius:999px}}
.tog{{margin-left:auto;display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}}.tog button{{background:none;border:0;color:var(--ink);padding:6px 12px;font-size:13px;cursor:pointer}}.tog button.on{{background:var(--ink);color:var(--bg)}}
main{{max-width:1180px;margin:0 auto;padding:8px 16px 60px}}
.note{{background:var(--chip);border-radius:12px;padding:12px 16px;margin:18px 0 6px;font-size:14px}}
section{{scroll-margin-top:70px}}h2{{font-size:22px;margin:34px 0 4px}}.fd{{color:var(--muted);margin:0 0 16px}}
.em{{display:grid;grid-template-columns:280px 1fr;gap:18px;align-items:start;margin-bottom:22px}}
.meta{{position:sticky;top:76px}}.when{{display:inline-block;font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:8px}}
.inbox{{display:flex;gap:10px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px}}
.av{{flex:none;width:34px;height:34px;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;font-weight:700}}
.it{{min-width:0}}.fr{{font-weight:700;font-size:14px}}.sj{{font-size:14px}}.pv{{font-size:13px;color:var(--muted)}}
.frame{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:10px;display:flex;justify-content:center;overflow:hidden}}
iframe{{width:100%;max-width:640px;border:0;height:900px;display:block;transition:max-width .2s}}
body.mobile iframe{{max-width:375px}}
@media (max-width:820px){{.em{{grid-template-columns:1fr}}.meta{{position:static}}.tog{{margin-left:0}}}}
</style></head><body>
<header><div class="hw"><h1>SOL KYST</h1><nav>{"".join(nav)}</nav>
<div class="tog" role="group" aria-label="Preview width"><button class="on" onclick="setW(0,this)">Desktop</button><button onclick="setW(1,this)">Mobile</button></div></div></header>
<main><div class="note"><b>{n} draft emails</b> across 3 Klaviyo flows, shown with sample data (Jess · KIN in Wide · AFTER GLOW restock). Everything is in <b>draft</b>, so nothing sends until you turn a flow on.</div>
{"".join(cards)}</main>
<script>
function fit(f){{try{{f.style.height=(f.contentDocument.documentElement.scrollHeight+4)+'px'}}catch(e){{}}}}
function setW(m,b){{document.body.classList.toggle('mobile',!!m);document.querySelectorAll('.tog button').forEach(x=>x.classList.toggle('on',x===b));setTimeout(()=>document.querySelectorAll('iframe').forEach(fit),250)}}
</script></body></html>'''
OUT.write_text(page); print(OUT, len(page))
