# Flow 3: Back in Stock

**Trigger:** Klaviyo Back in Stock (build from **Flows → Create → Back in Stock** so the inventory delay is wired correctly)

## The strategy

People who click "notify me" have already decided. They don't need convincing, they need **speed** and **their size**. Sizes sell through unevenly (Mini and Wide go first on most styles), so the urgency here is real, not manufactured.

Keep both emails short. The product image does the selling.

---

## Email 1: The moment it's back

**Subject A:** It's back: {{ event.ProductName }}
**Subject B:** You asked us to tell you first. {{ event.ProductName }} is back.
**Preview:** Sizes go fast, so check yours

> {{ first_name|default:'Hey' }},
>
> **{{ event.ProductName }}** just restocked, and you're hearing about it before anyone else.
>
> [Large product image → {{ event.URL }}]
>
> Heads up: restocks don't sell out evenly. The most popular sizes go first, so if you know yours, don't sit on this one.
>
> **[ Grab my size → ]**
>
> Not sure which size? Mini 135mm · Midi 145mm · Wide 158mm. Measure a pair you own hinge to hinge and go one up if they pinch. Guess wrong? Exchanges are free for 45 days.
>
> SOL KYST

---

## Email 2: 24 hours later, only if they haven't purchased

**Filter:** Placed Order = 0 since flow start

**Subject A:** Sizes are moving on {{ event.ProductName }}
**Subject B:** Don't make us send the "sold out" email 😩
**Preview:** Quick heads up before it's gone again

> {{ first_name|default:'Hi' }}, quick one.
>
> **{{ event.ProductName }}** is selling through faster than last time. If you still want it, now's the moment.
>
> **[ Shop {{ event.ProductName }} → ]**
>
> SOL KYST
