# Flow 2: Post-Purchase Thank You

**Trigger:** Placed Order
**Flow filters:**
- Has not been in this flow in the last 30 days

**Conditional split after Email 1:** Placed Order **= 1 over all time** (first-time customer) vs **> 1** (repeat customer). Both branches get Emails 2 and 3. Only the Email 1 copy differs (variants below).

**Goal:** Say thank you, cut down on "where's my order" tickets, teach care and fit, and drive a second purchase.

> The existing draft **Review request** flow should handle reviews, so this flow doesn't ask for one.

---

## Email 1: Immediately

### Variant A (first-time customer)

**Subject:** You're officially part of the crew! 🎉
**Preview text:** Thank you so much, seriously

**Body:**

{{ first_name|default:'Hey' }}, THANK YOU! 💛

You just made our whole day. SOL KYST started with one simple idea: sunglasses should fit *every* face, especially the wide ones the big brands forgot about. Your order helps keep that idea alive.

**What happens next:**
1. 📦 We pack your order with love (1–2 business days)
2. 🚚 You get a tracking link as soon as it ships
3. 😎 You put on your new favourite sunnies

Got a question? Just reply to this email. We read every single one.

**[ View My Order → ]**

With so much gratitude,
The SOL KYST Crew

### Variant B (repeat customer)

**Subject:** Back again?! We love you 🥹
**Preview text:** Order #{{ event.OrderId|default:'' }} is in good hands

**Body:**

{{ first_name|default:'Friend' }}, you came back! 🥹

Seriously, repeat customers are the reason we exist. Thank you for trusting us again.

Your order is being packed now, and we'll send tracking the moment it ships.

**[ View My Order → ]**

xo,
The SOL KYST Crew

---

## Email 2: Wait 5 days

**Subject:** How to keep your sunnies looking brand new ✨
**Preview text:** 3 tips that take literally 10 seconds

**Body:**

Hey {{ first_name|default:'there' }}!

Your new pair should be arriving soon (or already on your face 😍). Here's how to keep them looking fresh:

1. **Case it, don't toss it.** Pop them in the case instead of your bag, cupholder or head.
2. **Microfibre only.** Skip your shirt. The cloth in your box is your lenses' BFF.
3. **Two hands on, two hands off.** It keeps the arms from stretching out over time.

**Fit feeling off?** Our sizes (Mini / Midi / Wide / Oversized) are made to fit, so if yours don't feel right, reply and we'll help sort it out.

**[ Read the Fit Guide → ]**

Talk soon,
The SOL KYST Crew

---

## Email 3: Wait 14 days

**Subject:** Your next pair is calling 📞😎
**Preview text:** Because one pair is never enough

**Body:**

Hi {{ first_name|default:'friend' }},

Real talk: most of our crew owns more than one pair. One for everyday, one for vacay, one for "I didn't wash my hair today" energy. 😅

Here are a few picks we think you'll love:

[Product recommendation block: "Recommended for you" or Best Sellers]

Tag us on Instagram **@solkyst** wearing yours. We LOVE seeing our crew out in the wild! 📸

**[ Shop Your Next Pair → ]**

Thanks for being part of this,
The SOL KYST Crew
