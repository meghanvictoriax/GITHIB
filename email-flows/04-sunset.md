# Flow 4: Sunset (people who've stopped opening)

**Trigger:** Segment "Unengaged 120d". Build it first:
- Can receive email marketing
- Opened Email = 0 in last 120 days AND Clicked Email = 0 in last 120 days
- Placed Order = 0 in last 180 days
- Profile created > 120 days ago

**How this differs from "Winback final":** winback chases lapsed *buyers*. Sunset cleans up *anyone* who has gone quiet, to protect inbox placement for everyone else.

## The strategy

Stop begging. A short, honest "should we stop?" email beats another promo with a bigger discount. The people who still care will click, and the rest *should* leave, because every dead address drags down whether your launches land in the inbox. Offer a lighter option ("launches only") so you keep people who are just overwhelmed.

---

## Email 1: Immediately

**Subject A:** Should we stop emailing you?
**Subject B:** Honest question, {{ first_name|default:'friend' }}
**Preview:** No guilt trip, just pick one

> Hey {{ first_name|default:'there' }},
>
> We noticed you haven't opened our emails in a while. Totally fine. Inboxes are a lot.
>
> Rather than keep showing up uninvited, we'd rather just ask. Pick one:
>
> **[ Keep me in the loop ]** → everything: drops, restocks, the occasional deal
> **[ Only new launches ]** → a few emails a year, that's it
> **[ I'm good, unsubscribe me ]**
>
> Whatever you choose, thanks for being part of this for a while. 💛
>
> SOL KYST

*Build note: buttons 1 and 2 link to the site with a UTM tag, and the click counts as engagement. Button 2 should also set the profile property `email_frequency = launches_only` (via preference page or a link-tracked segment). Button 3 is `{% unsubscribe %}`.*

---

## Email 2: 5 days later, only if no opens or clicks since flow start

**Subject A:** We're taking you off the list on {{ weekday }}
**Subject B:** Last one from us ☀️
**Preview:** Unless you'd rather stay

> {{ first_name|default:'Hi' }},
>
> This is our last email. If we don't hear from you, we'll take you off the list in a few days. No hard feelings at all.
>
> If you'd like to stay, one tap does it, and here's 10% off as a thank-you for sticking around: **{{ STAYKYST10 }}**
>
> **[ Keep me on the list → ]**
>
> SOL KYST

---

## After Email 2: wait 3 days

**Filter:** Opened = 0 AND Clicked = 0 since flow start
**Action:** Update profile `sunset_suppressed = true` → suppress these profiles or exclude them from all sends.
