# Decision Models

Use these models to turn user facts into a direct recommendation.

## Break-Even Model

Definitions:

- Monthly fixed cost = rent/property + labor + utilities + loan repayments + software/platform base fee + marketing baseline + other unavoidable monthly costs.
- Contribution margin = gross margin after food cost, packaging, platform commission, discounts, and wastage.
- Break-even monthly sales = monthly fixed cost / contribution margin.
- Break-even daily sales = break-even monthly sales / business days.
- Current gap = break-even daily sales - current daily sales.
- Runway = remaining cash / monthly loss.

Use `scripts/restaurant_break_even.py` when the user provides enough values.

## Red Flags

Treat these as strong stop or pause signals:

- Borrowed money or family savings are being used for a first store with no category experience.
- The user cannot state rent, labor, daily revenue, gross margin, or food-cost rate.
- Rent is high before demand is proven.
- Gross margin is too low for the category and no pricing/procurement fix exists.
- The store is in a dead location: hidden entrance, weak pedestrian flow, hard parking, cold mall zone, reverse school flow, no visible storefront.
- Franchise story depends on "headquarters will solve it" while the user does not understand unit economics.
- Headquarters has no verifiable direct stores or refuses to show real store accounts.
- The user chose the category because they personally like eating it.
- The plan relies on opening more stores before one store makes stable profit.
- Partners or relatives have unclear authority, salary, or exit rules.

## Rescue Or Close

Classify the store after calculating:

### Likely Fixable

Use a short rescue test if:

- Current daily revenue is close to break-even.
- The site has real foot traffic and visibility.
- Gross margin can be repaired.
- Labor or opening hours can be adjusted quickly.
- The user has enough cash for at least 2-3 months of controlled testing.

Actions:

- Cut nonessential SKUs.
- Raise or repackage low-margin items.
- Remove discounts that create fake revenue.
- Recheck supplier prices and waste.
- Rebuild signs, menu board, best-seller display, and entry动线.
- Test 7-day traffic conversion and 14-day gross-margin repair.

### Structurally Hard

Prefer transfer or closure if:

- Current daily revenue is less than half of break-even after 60-90 days.
- Rent/labor consume most gross profit.
- The site has no natural demand.
- The brand supply chain destroys margin.
- The owner has debt pressure and less than 2 months runway.
- The user needs a miracle event rather than controllable operations.

Say clearly that sunk cost is gone. The decision is whether tomorrow's money should continue burning.

## Category Pattern Notes

Use these as starting hypotheses, then adapt to local facts:

- Milk tea/coffee: high competition, brand effect, site visibility, cup count, rent, and staff efficiency matter. "Pretty store" does not equal sales.
- Hot pot/barbecue/buffet: heavy investment, labor, food waste, rent, and table-turn risk are high. Need strong evening/weekend demand.
- Burger/fried chicken/snacks: franchise and supply price risk often decide margin. Low ticket needs volume.
- Rice bowl/malatang/noodles/fast meal: lunch demand and office/school/community flow matter. Efficiency and repeat purchase are key.
- Bakery/dessert/yogurt: high waste and weak frequency can hurt. Product quality alone is not enough.
- Tourist-area stores: seasonal flow and landlord rent capture are major risks.
- Overseas stores: local labor, rent, regulation, supply, and cultural demand must be calculated separately.

## Decision Language

Prefer one direct diagnosis:

- "这个不是运营问题，是点位和成本结构问题。"
- "你现在不是缺营销，是保本线太高。"
- "先别签，先把总部和直营店查清楚。"
- "这个店能救，但只能给 14 天，不达标就转。"
- "继续干不是坚持，是把亏损扩大。"

Do not over-soften the conclusion when the numbers are clear.
