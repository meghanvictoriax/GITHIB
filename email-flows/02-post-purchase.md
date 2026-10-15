# Flow 2: Post-Purchase

**Trigger:** Placed Order
**Flow filter:** not in this flow in the last 30 days
**Split before Email 1:** Placed Order = 1 all time (first order) → 1A · otherwise → 1B

## The strategy

The job after purchase isn't "thanks + more products." It's:
1. **Make them feel good about the decision** (fewer cancellations, more word of mouth).
2. **Stop fit returns before they happen.** New acetate frames need a few days to settle, and nobody tells people that.
3. **Sell the second pair at the moment it's easiest.** They now know their size, which is the hardest part of buying from you. Use that.

The review ask stays in your existing "Review request" flow.

---

## Email 1A: Immediately · first-time customer · *plain-text, from a person*

**From:** Meghan at SOL KYST
**Subject A:** you did it
**Subject B:** A real thank-you (not a robot one)
**Preview:** and one quick question for you

> Hey {{ first_name|default:'there' }},
>
> I'm Meghan, the founder of SOL KYST.
>
> Before this I was a makeup artist. When that work stopped in 2020, I finally did something about a problem I'd had my whole life: I have a wide, cheeky face, and sunglasses just didn't fit it. So I designed a pair that did. That was the Kyst Eye. In March 2021 I showed it on TikTok, and a few days later we had a $10,000+ launch day. Turns out a lot of us had been squeezing into frames made for someone else.
>
> So when someone like you takes a chance on a small Canadian brand instead of the big names, I notice. Thank you, genuinely.
>
> Your order ships from Hamilton within 3–5 business days, and you'll get a tracking link the moment it leaves.
>
> **One quick question:** what finally made you buy? Was it a friend, a TikTok, the sizing, the Barbie collab, something else? Just hit reply. I read every answer, and it honestly shapes what we make next.
>
> Meghan
> Founder, SOL KYST

*Why plain text: it lands in Primary instead of Promotions, and the replies boost your sender reputation. The question also gives you free attribution data.*

## Email 1B: Immediately · repeat customer

**Subject:** Back for another pair? We're blushing 🤭
**Preview:** Your order's being packed right now

> {{ first_name|default:'Hey' }}, you came back!
>
> There's nothing better for a small brand than a repeat customer. It means the first pair actually fit, and that's the whole point of what we do.
>
> Your order ships within 3–5 business days, and tracking will follow as soon as it does.
>
> As a thank-you, you're first in line for our next drop. We'll email you before it goes public.
>
> **[ View my order → ]**
>
> SOL KYST

---

## Email 2: 6 days later (or trigger off "Delivered Shipment" if your fulfilment data is reliable) · "The 3-day rule"

**Subject A:** Read this before you decide how they fit
**Subject B:** The 3-day rule for new frames
**Preview:** New acetate needs a minute. Here's how to help it along.

> {{ first_name|default:'Hi' }},
>
> Your sunnies should have landed by now. One thing nobody tells you about good frames:
>
> **Acetate settles.** For the first few days, new frames can feel a touch firm behind the ears or snug at the temples. That's normal. The material relaxes and shapes to you with wear.
>
> **Give them 3 days of real wear.** Then check in with yourself:
> - **Still tight at the temples after 3 days?** Swap them for the next size up. **Exchanges are free for 45 days after delivery**, with no restocking fee. In Canada, drop them at any ReturnBear location with no box and no label. [ Start an exchange → ]
> - **Sliding down your nose?** Reply to us first. A quick adjustment at an optical shop usually fixes it, but returns have to come back in their original state, so check with us before anyone bends anything.
> - **Perfect?** Amazing. Keep them in the hard case, clean them only with the microfibre cloth, and take them off with two hands so the hinges stay tight.
>
> SOL KYST

*This is a returns-prevention email. Expect fewer "they're too tight" tickets on day 1–2.*

---

## Email 3: 14 days after Email 2 · "You already did the hard part"

**Conditional split:** ordered a Blue Light / RX frame? → Variant B. Otherwise → Variant A.

### Variant A (bought sunglasses)

**Subject A:** You know your size now. That changes things.
**Subject B:** The hard part's done 😎
**Preview:** Your next pair is a 30-second decision

> {{ first_name|default:'Hey' }},
>
> The hardest part of buying from us is figuring out your size. You've done that now.
>
> Which means your next pair is easy. Same size, different mood.
>
> **If you went bold → try a classic:** Integrity (sleek black rectangle) or Monarch (the tortoise version).
> **If you went classic → have some fun:** Barbie™ x Sol Kyst Sweet Heart, the peachy-pink heart frames that are our #2 seller this year.
>
> [Product block: same-size recommendations]
>
> **[ Shop in my size → ]**
>
> SOL KYST

### Variant B (bought Blue Light / RX)

*Not built in Klaviyo yet. Integrity Blue Light RX isn't an active product right now, so build this branch only if it comes back.*

**Subject:** Now do it for the sun ☀️
**Preview:** Same fit you love, polarized

> Same face, same size, same comfort, now polarized with UV400 for outside.
> [Product block: best sellers in their size]
> **[ Find my sunnies → ]**

---

### Sources
- Founder story: public brand coverage (see ../BRAND.md: makeup artist → 2020 → TikTok March 2021 → $10,000+ launch day). Meghan, edit it so it sounds like you.
- Ship time, exchange window and ReturnBear details: the store's Shipping and Refund policies.
- Sweet Heart as the #2 seller: Shopify net sales, last 365 days.
- Note: RX and Petite orders are final sale, so the 3-day-rule exchange line doesn't apply to them. Add a conditional split, or a line excluding them, before going live.
