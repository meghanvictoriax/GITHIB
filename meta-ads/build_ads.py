"""Builds ads.md (copy + briefs) and preview.html (feed mockups) for the SOL KYST Meta ad drafts."""
import html, pathlib

CDN = "https://cdn.shopify.com/s/files/1/0444/2089/0784/files/"
IMG = {
    "kin": CDN + "IMG-6013.jpg?v=1773266986",
    "integrity": CDN + "547973D9-7C97-4ACD-BD1B-C47CF3CCE67F.jpg?v=1767378147",
    "monarch": CDN + "Monarch_97e3b29d-5e10-42fe-a0ed-656639bea6ef.png?v=1766799619",
    "sweetheart": CDN + "Cut_Out_-_Barbie_-_4.png?v=1784148545",
    "klip": CDN + "kyst.png?v=1767381811",
    "afterglow": CDN + "ImaybesadbutatleastIhavegoodhair_4x5in_4x4in.png?v=1767207299",
}

GROUPS = [
 ("A", "Prospecting: first-order offer", "Women 25–44, US + Canada. Exclude purchasers (last 2 yrs), women 45+, men. Feed placements only (FB + IG feed, IG Reels). Runs now until 2–3 days before VIP.", [
  dict(id="A1", name="The fit check", fmt="Static 4:5", img="kin",
       overlay="Pinch at the temples?\nYou need a wider frame.",
       primary="If sunglasses have always pinched your temples by lunch, it's not your face. It's the frame.\n\nMost sunglasses come in one size, around 140mm. Ours go up to 158mm, in Mini, Midi, Wide and Oversized, so you finally get a pair that fits.\n\nPolarized, UV400, acetate frames. Free exchanges for 45 days if the size is off.",
       headline="Sunglasses that fit wide faces", desc="Mini · Midi · Wide · Oversized", cta="Shop Now",
       why="Builds on Evergreen Static 6 (your best ad: 23 sales, 2.0 ROAS). Same product-forward static, now leading with the fit problem."),
  dict(id="A2", name="18mm", fmt="Static 4:5 (comparison)", img="integrity",
       overlay="140mm  vs  158mm\nThat 18mm is everything.",
       primary="18mm doesn't sound like much until it's the difference between a headache by noon and forgetting you're wearing them.\n\n\"Standard\" sunglasses stop around 140mm. SOL KYST goes up to 158mm, designed for wide faces first.",
       headline="The 18mm that changes everything", desc="Free shipping over $150", cta="Shop Now",
       why="A simple, scroll-stopping number. Creative: two frames side by side with a ruler line, or one face wearing each."),
  dict(id="A3", name="We're a lil desperate", fmt="Static 4:5 (offer)", img="klip",
       overlay="15% off + a free Kyst Klip\nYour first order only",
       primary="Okay, we upped it to 15% because we're a lil desperate to get you Kyst. 🤭\n\nPlace your first order before [DATE] and you also get our signature Kyst Klip free, plus an invite to our VIP sale, our biggest of the year.\n\nCode [KYST15] at checkout.",
       headline="15% off + a free Kyst Klip", desc="First orders · ends [DATE]", cta="Shop Now",
       why="The new first-order offer. VIP access is the real reason to buy now, and the deadline lands before VIP starts."),
  dict(id="A4", name="Dragons' Den cut, Canada", fmt="Video 9:16 + 4:5, 15–20s", img="kin",
       overlay="[Video] As seen on Dragons' Den",
       primary="The wide-face sunglasses from Dragons' Den. 🕶️\n\nDesigned for faces the big brands forgot. Mini, Midi, Wide and Oversized, polarized, with free exchanges if the size is off.",
       headline="As seen on Dragons' Den", desc="Made for wide faces", cta="Shop Now",
       why="Your Dragons' Den video returned 3.0 ROAS in the US but was barely tested in Canada (Advantage+ Canada spent $174 on a copy of it). Re-cut a shorter version with the first 2 seconds showing the pitch moment. Confirm the Dragons' Den claim before running."),
  dict(id="A5", name="Founder story", fmt="Video 9:16, 30s, Meghan to camera", img="afterglow",
       overlay="[Video] \"I was a makeup artist with a wide face…\"",
       primary="I was a makeup artist with a wide, cheeky face, and sunglasses never fit me. So in 2020 I designed a pair that did.\n\nOne TikTok later, we had a $10,000+ launch day. Turns out a lot of us were squeezing into frames made for someone else. 💛\n\n— Meghan, founder",
       headline="Made for faces like ours", desc="Designed in Hamilton, Ontario", cta="Learn More",
       why="A fresh hook for audiences that are fatigued (Canada frequency is 60). Script: problem (0–5s), what she made (5–15s), try-on in 3 sizes (15–25s), CTA (25–30s)."),
 ]),
 ("B", "Retargeting: visited or added to cart, no purchase", "Site visitors and Add to Cart in the last 30 days, excluding purchasers. Separate ad set so it isn't swallowed by Advantage+.", [
  dict(id="B1", name="Still deciding?", fmt="Carousel (4 cards)", img="sweetheart",
       overlay="Still deciding?\nThe size is the hard part. We've got you.",
       primary="Still thinking about that pair? 👀\n\nNot sure about the size? Reply to any of our emails with a selfie and we'll tell you your fit. And if it's still off, exchanges are free for 45 days.\n\nFirst order? Use [KYST15] for 15% off + a free Kyst Klip before [DATE].",
       headline="Your size, sorted", desc="Free exchanges · 45 days", cta="Shop Now",
       why="Answers the real objection (fit). Carousel cards: KIN, Sweet Heart, Integrity, Monarch (your top sellers)."),
 ]),
 ("C", "VIP: bought in the last 2 years", "Custom audience synced from Klaviyo or Shopify (purchased in the last 730 days). Exclude from all prospecting. Launch the day VIP opens.", [
  dict(id="C1", name="You're on the list", fmt="Static 4:5 + Story 9:16", img="monarch",
       overlay="VIP SALE\nYou're on the list.",
       primary="You're in. 💛\n\nOur VIP sale is our biggest of the year, and it's only open to people who've shopped with us in the last 2 years. That's you.\n\n[VIP OFFER] until [END DATE]. Same size you already know, new mood.",
       headline="VIP access: you're on the list", desc="Ends [END DATE]", cta="Shop Now",
       why="Exclusivity costs nothing and converts well. The \"same size you already know\" line removes the fit worry."),
 ]),
 ("D", "Lapsed: bought more than 2 years ago", "Purchased 731+ days ago, nothing since. Runs until 2–3 days before VIP.", [
  dict(id="D1", name="Get back on the list", fmt="Static 4:5", img="integrity",
       overlay="It's been a minute.\nGet back on the VIP list.",
       primary="It's been a minute! 🥹\n\nOur VIP sale is coming, and it's only for people who've ordered in the last 2 years. Place an order before [DATE] and you're back on the list.\n\nNew since you last shopped: [NEW STYLES].",
       headline="Get back on the VIP list", desc="Order before [DATE]", cta="Shop Now",
       why="Uses the VIP rule as the hook, at no discount cost."),
 ]),
]

out = pathlib.Path(__file__).parent
# Markdown
md = ["# SOL KYST: Meta ad drafts (pre-VIP)", "",
      "Built from the last 90 days of Meta data: women 25–44 bought 70 of 75 orders, feed placements outperform Stories, and the two ads that work are Evergreen Static 6 and the Dragons' Den video. Fill in [BRACKETS] before launch.", ""]
for gid, gname, aud, ads in GROUPS:
    md += [f"## {gid}. {gname}", "", f"**Audience:** {aud}", ""]
    for a in ads:
        md += [f"### {a['id']}: {a['name']}", "",
               f"- **Format:** {a['fmt']}",
               f"- **On-image text:** {a['overlay'].replace(chr(10), ' / ')}",
               f"- **Headline:** {a['headline']}",
               f"- **Description:** {a['desc']}",
               f"- **CTA button:** {a['cta']}",
               f"- **Why:** {a['why']}", "", "**Primary text:**", ""]
        md += ["> " + l if l else ">" for l in a["primary"].split("\n")]
        md.append("")
md += ["## Launch notes", "",
       "- Turn off Instagram Stories in prospecting (0.65 ROAS over the last 90 days).",
       "- Test A1–A5 in one ad set with equal budget for 5–7 days, then move spend to the top two.",
       "- Exclude people who bought in the last 2 years from every prospecting ad set.",
       "- Every [DATE] is the first-order offer deadline: 2–3 days before VIP opens.",
       "- Confirm the Dragons' Den claim (A4) before running.", ""]
(out / "ads.md").write_text("\n".join(md))

# Preview
def card(a):
    lines = html.escape(a["primary"]).replace("\n", "<br>")
    ov = html.escape(a["overlay"]).replace("\n", "<br>")
    return f'''<article class="ad"><div class="tag">{a["id"]} · {html.escape(a["name"])}<span>{html.escape(a["fmt"])}</span></div>
<div class="post"><div class="ph"><div class="av">SK</div><div><b>SOL KYST</b><small>Sponsored</small></div></div>
<p class="pt">{lines}</p>
<div class="media"><img src="{IMG[a["img"]]}" alt="" loading="lazy"><div class="ov">{ov}</div></div>
<div class="foot"><div><small>SOLKYST.CA</small><b>{html.escape(a["headline"])}</b><small>{html.escape(a["desc"])}</small></div><span class="cta">{html.escape(a["cta"])}</span></div></div>
<p class="why"><b>Why:</b> {html.escape(a["why"])}</p></article>'''

secs = "".join(f'<section><h2>{gid}. {html.escape(gn)}</h2><p class="aud">{html.escape(aud)}</p><div class="grid">{"".join(card(a) for a in ads)}</div></section>' for gid, gn, aud, ads in GROUPS)
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Meta Ad Drafts</title>
<style>
:root{{--bg:#F4EEE8;--panel:#fff;--ink:#1A1A1A;--muted:#6B6460;--line:#E6DCD3;--chip:#F6E3D8;--fb:#1877F2}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151312;--panel:#201D1B;--ink:#F3EEE9;--muted:#A79F99;--line:#34302D;--chip:#3A2C25}}}}
:root[data-theme="dark"]{{--bg:#151312;--panel:#201D1B;--ink:#F3EEE9;--muted:#A79F99;--line:#34302D;--chip:#3A2C25}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}}
main{{max-width:1200px;margin:0 auto;padding:20px 16px 60px}}h1{{font-size:24px;margin:8px 0 6px}}.lead{{color:var(--muted);margin:0 0 8px;max-width:760px}}
h2{{font-size:19px;margin:34px 0 4px}}.aud{{color:var(--muted);margin:0 0 14px;font-size:14px;max-width:820px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}}
.tag{{font-size:12px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-bottom:6px;display:flex;justify-content:space-between;gap:8px}}.tag span{{color:var(--muted);font-weight:500;text-transform:none;letter-spacing:0}}
.post{{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
.ph{{display:flex;gap:10px;align-items:center;padding:12px}}.ph b{{display:block;font-size:14px}}.ph small{{color:var(--muted);font-size:12px}}
.av{{width:36px;height:36px;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;font-weight:700;font-size:13px;letter-spacing:1px}}
.pt{{margin:0;padding:0 12px 12px;font-size:14px}}
.media{{position:relative;aspect-ratio:4/5;background:#EFE7E0;overflow:hidden}}.media img{{width:100%;height:100%;object-fit:cover;display:block}}
.ov{{position:absolute;left:0;right:0;bottom:0;padding:18px 16px;background:linear-gradient(transparent,rgba(0,0,0,.65));color:#fff;font-weight:800;font-size:20px;line-height:1.2}}
.foot{{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;background:var(--chip)}}.foot small{{display:block;color:var(--muted);font-size:11px}}.foot b{{display:block;font-size:14px}}
.cta{{flex:none;background:var(--ink);color:var(--bg);font-size:13px;font-weight:600;padding:8px 12px;border-radius:6px}}
.why{{font-size:13px;color:var(--muted);margin:8px 2px 0}}
</style></head><body><main><h1>SOL KYST · Meta ad drafts</h1>
<p class="lead">9 drafts for the run-up to VIP, built from the last 90 days of Meta data. Images are existing product shots standing in for the final creative; the dark text band shows what goes on the image. Fill in [BRACKETS] before launch.</p>
{secs}</main></body></html>'''
(out / "preview.html").write_text(page)
print("ok")
