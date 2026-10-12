# Flow 1: Added to Cart Abandonment

**Trigger:** Added to Cart
**Flow filters:**
- Placed Order zero times since starting this flow
- Checkout Started zero times since starting this flow (the existing "Abandoned Cart" flow handles those people)
- Has not been in this flow in the last 14 days

**Goal:** Catch shoppers who added a pair to their cart but never reached checkout.

---

## Email 1: Wait 2 hours

**Subject:** Your sunnies are waiting 😎
**Preview text:** We saved your cart, no pressure (ok, a little pressure)

**Body:**

Hey {{ first_name|default:'there' }}!

You left something good behind 👀

Your cart is safe and sound, but sunnies this cute don't tend to stick around. Every SOL KYST pair is designed for **wide faces first**, so no more frames pinching your temples or sliding off your nose.

[Dynamic cart block: product image, name, size, price]

**[ Back to My Cart → ]**

Questions about sizing? Just hit reply. A real human (hi!) will help you find your fit.

xo,
The SOL KYST Crew

---

## Email 2: Wait 1 day

**Subject:** Still thinking it over? Here's 10% off 💛
**Preview text:** A little nudge to help you say yes

**Body:**

Hi {{ first_name|default:'friend' }},

We get it, finding *the* pair is a big deal. So here's a little something to make it easier:

### 10% OFF your order
Code: **{{ CART10 }}** (expires in 48 hours)

**Why wide-face babes love us:**
- 🕶️ Sized for real faces: Mini, Midi, Wide & Oversized
- ✨ Comfy all day, no headaches, no pinching
- 💛 Designed in Hamilton, Ontario

[Dynamic cart block]

**[ Claim My 10% → ]**

Thank you for being here!
The SOL KYST Crew
