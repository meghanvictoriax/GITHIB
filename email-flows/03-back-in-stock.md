# Flow 3: Back in Stock

**Trigger:** Subscribed to Back in Stock (Klaviyo's built-in Back in Stock trigger)
**Setup note:** In Klaviyo, the cleanest way to build this is **Flows → Create → Back in Stock template**. That handles the inventory delay for you. Paste the copy below into that template's emails.
**Flow filters:**
- Can receive email marketing (back-in-stock notices go to non-subscribers too, so turn on "transactional" only if legal/compliance approves)

**Goal:** Turn "notify me" sign-ups into sales the moment a pair is restocked.

---

## Email 1: Immediately when the item is back

**Subject:** IT'S BACK! 🙌 {{ event.ProductName|default:'Your pair' }} just restocked
**Preview text:** Grab it before it disappears again

**Body:**

{{ first_name|default:'Hey' }}! You asked, we listened 🎉

**{{ event.ProductName|default:'The pair you had your eye on' }}** is back in stock, and you're one of the first to know.

[Product image + price block, linking to {{ event.URL }}]

Last time it sold out fast, so don't wait too long on this one!

**[ Get Mine Now → ]**

xo,
The SOL KYST Crew

---

## Email 2: Wait 1 day (only if they haven't purchased)

**Flow filter on this email:** Placed Order zero times since starting this flow

**Subject:** Going, going… 👀
**Preview text:** Your restocked pair is moving fast

**Body:**

Hi {{ first_name|default:'friend' }},

Just a friendly heads up: **{{ event.ProductName|default:'your pair' }}** is flying off the shelves again.

Designed for wide faces, comfy all day, and back for a limited time. 😎

**[ Shop Before It's Gone → ]**

The SOL KYST Crew
