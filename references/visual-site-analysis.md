# Visual Site Analysis

Use this file when the user uploads storefront photos, street photos, a 360-degree video/sweep, a Gaode/Baidu/Tencent/Apple map screenshot, satellite screenshot, or a map pin for a restaurant site.

## Core Rule

Treat images as evidence, not as a complete business case.

- Extract visible facts from the image first.
- State confidence: high, medium, or low.
- Do not invent the exact address, foot traffic, sales, rent, or customer behavior from a single image.
- If exact location is unclear, ask for city + address/pin/map link before making location-level claims.
- If the image shows people, ignore identity, faces, license plates, and private details. Only analyze commercial/site factors.

## Image Types

### Storefront Or Street Photo

Extract:

- Storefront visibility: sign size, contrast, lighting, whether the category is obvious within 3 seconds.
- Door and entry: open/closed feel, glass reflection, stairs/threshold, whether customers can enter naturally.
- Road and pedestrian condition: sidewalk width, crossing difficulty, vehicle speed, barriers, trees/poles blocking view.
- Parking/access: parking spaces, electric-bike parking, delivery rider access, curb restrictions.
- Neighboring shops: food/non-food mix, strongest competitors, complementary anchors, empty shops, closed shutters.
- Customer scene: school/office/community/tourist/night-market clues, but only when visible.
- Time limits: photo time, weather, and single moment may distort actual flow.

Do not conclude "人流很好/很差" from one still image alone. Say what is visible and ask for time-window observation if needed.

### 360-Degree Sweep Or Multiple Photos

Analyze by direction:

1. Front: can the target customer notice the shop before passing it?
2. Left/right neighbors: are there anchors, competitors, empty shops, or category conflicts?
3. Across the street: is there reachable flow or only visible-but-unreachable flow?
4. Back/side access: parking, delivery, backstreet, school/community entrance.
5. Customer path: where people come from, where they stop, and whether they naturally pass the door.

This is the closest image substitute for 勇哥's "转一圈看看周围".

### Map Screenshot

Extract:

- Visible map app, city/district clues, road names, POIs, target pin, scale, walking distance markers.
- Site type: mall, school, office, community, hospital, station, tourist area, night market, industrial park.
- Flow hypothesis: entrances/exits, main road vs back road, corner vs mid-block, dead-end vs through-route.
- Competition within visible radius: same category, substitute meals, head brands, convenience stores, supermarkets.
- Distance traps: "near school/mall/station" is not enough. Check whether the door is on the real path.

If the screenshot has enough unique text or a map pin, use web/map search if available to verify current surrounding POIs. If not available, say "只能按截图判断".

## Location Confidence

Use these labels:

- High: exact address, map pin, or unique shop/road/POI combination is visible and can be verified.
- Medium: district, roads, and several POIs are visible, but exact storefront/pin is not fully certain.
- Low: only a storefront/photo with no readable address, or map crop has no scale/road/pin.

When confidence is low, ask:

```text
这张图我能看门头和周边，但定位不够。你补三个东西：城市、详细地址或高德分享链接、你店门口朝哪个方向。再拍一组门口正前方、左边、右边、对面各一张。
```

## Site Diagnosis Checklist

Judge the site through these questions:

- Category fit: Does this category match the visible scene and likely customer purpose?
- Demand path: Who passes the door, why would they stop, and at what time?
- Visibility: Can the customer understand what is sold before walking past?
- Accessibility: Can they stop, park, cross, queue, or enter without friction?
- Competition: Is the shop beside stronger brands or better-known alternatives?
- Rent justification: Does the visible flow plausibly support the requested rent?
- Conversion gap: If nearby has people but the shop has no sales, is the issue path, visibility, category, price, or product?
- Repairability: Can signage, lighting, open-door display, menu board, or operating hours fix it, or is the location structurally wrong?

## Required Follow-Up Data

After visual inspection, still ask for numbers:

- Monthly rent/property, area, transfer fee, remaining lease.
- Category, price range, average ticket, gross margin.
- Current or expected daily revenue, order count, peak hours.
- Rent and sales of nearby comparable shops if known.
- Three time observations: weekday lunch/dinner and weekend or school/work peak.

For a planned store, ask the user to observe:

```text
工作日午高峰30分钟、晚高峰30分钟、周末高峰30分钟：
门前经过多少人？
有多少人停下？
附近同品类/替代品各卖多少？
人流是经过你门口，还是只在对面/商场里/学校里面？
```

## Answer Shape

Use this order:

1. `我从图里能确认的`: visible facts and confidence.
2. `我不能确认的`: address/flow/sales/rent gaps.
3. `按勇哥转一圈逻辑看`: path, storefront, neighbors, competition, customer purpose.
4. `这个位置最大的风险`: one or two fatal constraints.
5. `还要补的数`: rent, revenue, margin, observation counts.
6. `下一步`: what to photograph, observe, or verify before signing/rescuing.

## Common Visual Patterns

- Near school but not on the school gate path: treat as weak school flow until proven.
- Mall side/back/cold zone: do not count mall traffic unless customers naturally pass the door.
- Across-road flow: visible traffic is not reachable traffic if crossing is hard.
- Big sign but unclear category: customers may notice but not know what to buy.
- Empty neighboring shops or frequent transfers: strong warning for site quality.
- Food street with many substitutes: the issue is not "no people", but why this shop wins.
- Community bottom shop: daily convenience categories usually beat low-frequency novelty categories.
- Tourist/night-market site: seasonality and landlord rent capture must be calculated.
