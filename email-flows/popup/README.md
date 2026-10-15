# Sign-up pop-up (draft)

Klaviyo form **Tvws8E**, "[DRAFT] SOL KYST pop-up - 15% first pair". It's still a draft and isn't published.

- **Step 1:** logo, "Hey wide face babe", "15% off your first pair", an email field, then **GET MY 15%**. Sign-ups go to the **Newsletter list (YxzPdw)**, which triggers the welcome flow WXaimu. A "No thanks" link closes the pop-up.
- **Step 2:** "You're in." with the code `kystfortheveryfirsttime` (click to copy), then **SHOP WITH 15% OFF**. That button links to `/discount/kystfortheveryfirsttime?redirect=/collections/all`, so the code is applied automatically.
- **Teaser:** a cocoa tab at the bottom left, "15% off your first pair", shown after someone closes the pop-up.
- **Targeting:** desktop and mobile. It shows after 6 seconds and 30% scroll, only to visitors who aren't identified and haven't submitted before, then hides for 5 days after a close or submit.
- **Styling:** ivory #FAF9F6, cocoa #3B2C27, Georgia italic headlines, square corners, and the same lifestyle image as the current pop-up. The side image shows on desktop only.

## Before publishing
- The live pop-up **Txvgns** ("Newsletter sign up - Beige") sends emails to **SMS Subscribers (US6MRa)**, which triggers no flow. Pause it when this one goes live, or both will show.
- YxzPdw is double opt-in, so the welcome flow starts once someone clicks the confirm link.

Preview: `popup-preview.png` (the photo is a placeholder because the CDN is blocked locally).
