# Flow 4: Sunset / Unengaged Subscribers

**Trigger:** Segment "Unengaged 120 days" (create this first)

**Segment definition:**
- Can receive email marketing
- AND Opened Email zero times in the last 120 days
- AND Clicked Email zero times in the last 120 days
- AND Placed Order zero times in the last 180 days
- AND Profile created more than 120 days ago

**Goal:** Try once more to re-engage quiet subscribers. If they stay quiet, suppress them to protect deliverability (and the Klaviyo bill).

**Difference from "Winback final":** Winback targets lapsed *customers*. Sunset targets *any* subscriber who has stopped opening.

---

## Email 1: Immediately

**Subject:** Is this goodbye? 🥺
**Preview text:** We miss you, here's 10% off if you're still in

**Body:**

Hey {{ first_name|default:'there' }},

It's been a while and we miss you! 💛

We know inboxes get messy, so let's keep it simple. If you still want sunnies made for wide faces (and the occasional fun email from us), just tap the button below.

As a thank-you for sticking around: **10% off** with code **{{ STAYSUNNY10 }}**.

**[ Yes, Keep Me Subscribed! → ]**
*(links to the site so the click counts as engagement)*

Not feeling it anymore? Totally okay, no hard feelings. You can unsubscribe below.

xo,
The SOL KYST Crew

---

## Email 2: Wait 5 days

**Flow filter on this email:** Opened Email zero times since starting this flow AND Clicked Email zero times since starting this flow

**Subject:** Last call ☀️👋
**Preview text:** We'll stop emailing unless you tell us otherwise

**Body:**

Hi {{ first_name|default:'friend' }},

This is our last email unless you let us know you want to stay.

We'll take you off our list in a few days. You can always come back anytime at solkyst.ca. 😎

**[ Keep Me On The List → ]**

Thank you for being part of the SOL KYST story, even for a little while. 💛

The SOL KYST Crew

---

## Final step: Wait 3 days, then update the profile

**Flow filter:** Opened Email zero times since starting this flow AND Clicked Email zero times since starting this flow

**Action:** Update Profile → set the property `sunset_suppressed = true`. Then suppress these profiles manually in Klaviyo, or exclude `sunset_suppressed = true` from all campaign sends.
