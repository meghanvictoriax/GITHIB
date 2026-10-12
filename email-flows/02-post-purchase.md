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

**From:** [Founder first name] at SOL KYST
**Subject A:** you did it
**Subject B:** A real thank-you (not a robot one)
**Preview:** and one quick question for you

> Hey {{ first_name|default:'there' }},
>
> I'm [Founder first name]. I started SOL KYST because I have a wide face, and I was tired of being told to "just size up" by brands that didn't make a size up.
>
> So when someone like you takes a chance on a small Canadian brand instead of the big names, I notice. Thank you, genuinely.
>
> Your order is being packed in Hamilton now. You'll get tracking the second it ships.
>
> **One quick question:** what finally made you buy? Was it a friend, a TikTok, the sizing, the Barbie collab, something else? Just hit reply. I read every answer, and it honestly shapes what we make next.
>
> [Founder first name]
> Founder, SOL KYST

*Why plain text: it lands in Primary instead of Promotions, and the replies boost your sender reputation. The question also gives you free attribution data.*

## Email 1B: Immediately · repeat customer

**Subject:** Back for another pair? We're blushing 🤭
**Preview:** Your order's being packed right now

> {{ first_name|default:'Hey' }}, you came back!
>
> There's nothing better for a small brand than a repeat customer. It means the first pair actually fit, and that's the whole point of what we do.
>
> Your order's being packed now and tracking is on its way.
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
> - **Sliding down your nose?** The arms can be gently warmed and bent inward. Most optical shops will do it for free in about 2 minutes.
> - **Still tight at the temples after 3 days?** Reply to this email. We'll sort it out with you, and you won't be stuck with a pair that doesn't fit.
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
> **If you went classic → have some fun:** Barbie™ x Sol Kyst Sweet Heart, the peachy-pink heart frames that sold out the first time.
> **And for the screen hours:** Integrity Blue Light RX, the same wide fit as a blue-light frame. You can put your prescription in it (ask your optometrist to confirm).
>
> [Product block: same-size recommendations]
>
> **[ Shop in my size → ]**
>
> SOL KYST

### Variant B (bought Blue Light / RX)

**Subject:** Now do it for the sun ☀️
**Preview:** Same fit you love, polarized

> Same face, same size, same comfort, now polarized with UV400 for outside.
> [Product block: best sellers in their size]
> **[ Find my sunnies → ]**

---

### Needs from you
- Founder first name + a one-line origin story (Email 1A is written as a placeholder version, so edit it to the real story).
- Confirm you're comfortable with "we'll sort it out" in Email 2. Swap in the actual exchange policy if you have one.
- Check whether "Sweet Heart sold out the first time" is true. If not, cut it.
