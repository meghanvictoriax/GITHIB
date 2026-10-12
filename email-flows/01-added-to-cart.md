# Flow 1: Added to Cart (pre-checkout)

**Trigger:** Added to Cart
**Flow filters:** Placed Order = 0 since flow start · Checkout Started = 0 since flow start (the live "Abandoned Cart" flow takes over from there) · not in this flow in the last 14 days

## The strategy

Someone who adds a pair and leaves *before* checkout usually isn't worried about price yet. They're worried about **fit**. Every wide-face shopper has a drawer full of frames that pinched, slid or left red marks. So this flow sells certainty, not a coupon.

**No discount here on purpose.** Your live checkout flow already ends with "Final offer miss playing hard to get 😆". Discounting earlier just trains people to wait for the code.

---

## Email 1: 1 hour after add to cart · "The fit check"

**Subject A:** Not sure about the size? 🤭
**Subject B:** Before you buy {{ event.Name|default:'your pair' }}…
**Preview:** A 30-second test with a pair you already own

> Hey {{ first_name|default:'babe' }},
>
> You left **{{ event.Name|default:'a pair' }}** in your cart, and we'd bet it's not the style you're unsure about. It's the fit.
>
> Fair. If you've got a wider face, you've probably spent years buying sunnies that pinch your temples by lunchtime. So let's take the guessing out of it.
>
> **The 30-second fit check:**
> Grab the pair of sunglasses you wear most and measure straight across the front, hinge to hinge.
>
> | If yours measure… | …and they feel | Try |
> |---|---|---|
> | ~135mm | perfect | **Mini** (135mm) |
> | ~135–140mm | a little snug | **Midi** (145mm) |
> | ~140mm+ | tight at the temples | **Wide** (158mm) |
> | anything | you want *big* | **Oversized** (145–150mm, deeper lens) |
>
> Still torn? **Reply with a selfie** (straight on, hair back) and we'll tell you your size. A real person answers every one.
>
> And if they still don't feel right when they arrive? **Exchanges are free for 45 days**, with no restocking fee. *(Petite sizes are final sale, so if you're going Petite, send the selfie first.)*
>
> **[ Back to my cart → ]**
>
> Let's get you Kyst,
> SOL KYST

*Build note: use a dynamic block showing the cart item and the size they picked. If the event includes the variant, add a line like "You picked **{{ variant }}**, which should suit you if…".*

---

## Email 2: 1 day later · "What $175–$220 actually buys"

**Subject A:** Why our sunnies cost more than the ones at the drugstore
**Subject B:** {{ event.Name|default:'Your pair' }} is still here ✨
**Preview:** (and why they'll outlast every pair you've owned)

> {{ first_name|default:'Hi' }},
>
> Real talk: SOL KYST isn't the cheapest pair you'll find. Here's where the money goes.
>
> **Acetate, not plastic.** It's the material used in premium frames. It's warmer and heavier in the hand, and it can be adjusted so it actually fits *your* face.
>
> **Polarized lenses + UV400.** They cut glare and block 100% of UVA/UVB.
>
> **Sized for you, not the "average" face.** "Standard" sunglasses come in one size, around 140mm wide. Ours go up to 158mm. That 18mm is the difference between a headache by noon and forgetting you're wearing them.
>
> **The box.** Hard protective case, microfibre cloth and our sliding gift box. (It's giving "treat yourself," and it's a very good gift if you're buying for someone else.)
>
> **Zero risk on the fit.** Free exchanges for 45 days, no restocking fee. In Canada you can drop a return at a ReturnBear location with no box and no label.
>
> **Free shipping over $150,** and orders to Canada and the US over $150 ship duty-free. No surprise fees at the door.
>
> One good pair that fits beats three that sit in a drawer.
>
> [Dynamic cart block]
>
> **[ Finish what you started → ]**
>
> SOL KYST
>
> *P.S. **{{ top_seller|default:'KIN' }}** is our #1 pair this year. If you're between styles, start there.*

---

### Sources
- 140mm "standard" one-size claim: SOL KYST's own sizing copy.
- Exchange, return, shipping and duty details: the store's Refund and Shipping policies (pulled from Shopify).
- KIN as the #1 pair: Shopify net sales, last 365 days.
