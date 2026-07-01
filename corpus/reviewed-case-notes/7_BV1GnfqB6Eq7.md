# Case 7: 大学城炸鸡高租低毛利, 每天亏约2200后分租止损

- Source: https://www.bilibili.com/video/BV1GnfqB6Eq7/
- Raw ASR: `../transcripts/7_BV1GnfqB6Eq7.json`
- Machine draft: `../case-notes/7_BV1GnfqB6Eq7.md`
- Review status: reviewed from ASR transcript.
- Reliability: usable for core facts, cost structure, calculation path, and final advice. ASR is rough for some店名、品牌名和口头玩笑; key numbers are repeated enough to be stable: daily sales about 2,500, gross margin below 20%, rent 35,000/month with one month waived, effective school-season business about 8 months, utilities about 5,000/month, labor about 28,000/month, initial investment about 400,000.

## User Facts Extracted

- Case type: 已开店亏损, 自营炸鸡店, not franchise.
- Owner profile: 29岁; 另有自己的事情做, 这个店偏托管状态. 忙时两三天来一次, 不忙时基本每天下午过来.
- Open duration: about 3 months. Owner says previous two months可能亏得没那么多, current month because participating in外卖平台/活动打价, 商家补贴压力更大.
- City/location: 广州大学城一带, 商场一楼/大学商圈. Nearby students include中大、广工等, 对面有宿舍, but商圈大、散、餐饮店多, 人流主要集中在商场正门和部分外街.
- Store size and visibility: 70平方米炸鸡店. 店面/玻璃面较大, but招牌显得小, 识别效率不匹配大面积和高租金.
- Current sales: average about 2,500/day.
- Gross margin: owner says可能不到20%. 勇哥按20%上限粗算, daily gross profit only about 500/day.
- Channel mix: 外卖约一半到六成, 堂食约四到五成. 价格和村子/外面小店差不多, 大学城里卷价格, 再扣外卖费、打包、活动补贴后毛利很低.
- Rent: 35,000/month.春节/过年免一个月, so annual rent about 35,000 x 11 = 385,000.
- Business seasonality: 大学商圈按约8个月有效经营期估算, annual rent spread over 8 months equals about 48,125/month, about 1,604/day.
- Utilities: transcript gives about 5,000/month, one处ASR为5,166; use roughly 5,000-5,166/month, about 167/day.
- Labor: about 28,000/month, counted as about 933/day. Later dialogue implies current labor roughly按4个人口径.
- Initial investment: about 400,000. Rent押二付一约105,000. Hard decoration about 80,000; equipment/decoration口径ASR不完全清晰, owner mentions 11-12万左右. Promotion/代运营 spending already more than 50,000.
- Promotion/outsourcing: 抖音套餐约16,800, 小红书约14,000, 外卖运营约12,000. 外卖代运营/monthly抽点约8%, 抖音主播券/核销类抽点约7%; these are additional burdens beyond simple food cost.
- Transfer fee: current铺位 appears to have no transfer fee. Contract is with mall/property directly, but later是否允许转租/分租 needs和商场谈.
- Nearby benchmark: 一家烧烤店晚上营业, owner estimates around10,000/day and开了多年, but勇哥 says it has about8个人, labor much higher, profit may not be large. Other surrounding刚需店数据 owner掌握不清; some nearby shops have closed.
- User's proposed rescue idea: because店内环境和堂食空间没有充分利用, owner考虑再做一个品类、换品、提高营业额, at least reach breakeven.

## Yongge Question Order

1. First inspect the physical store: 整个大店是否都是他的, 门头/招牌为什么这么小, 炸鸡为什么开这么大.
2. Ask current daily sales, city, store area, then immediately ask gross margin.
3. Ask外卖/堂食占比 and price level, to explain why炸鸡毛利 can fall below20%.
4. Ask rent: monthly or yearly, then identify it as大学商圈 and force the owner to按真实有效经营月份算租金.
5. Ask utilities, staff count/labor cost, then convert rent and labor into daily burden and daily loss.
6. Ask opened how long and whether all three months are the same; connect current worse loss to平台活动/商家补贴.
7. Ask total investment, whether franchise, rent deposit/payment terms, decoration/equipment/promotion spending, and代运营/平台抽点.
8. Ask owner background and how often he comes to the store, identifying semi-absentee operation.
9. When owner proposes adding another product, ask whether he can still carry it, whether the shop can transfer, and inspect the surrounding location, street, school flow, and competitors.
10. Ask what nearby just-demand restaurants sell per day, whether there are truly good businesses on the same street, and compare against the only strong烧烤 benchmark.
11. Ask current plan and possible additional investment, then reverse-calculate breakeven sales for炸鸡,刚需餐, and social/high-ticket categories.
12. Finalize with止损: do not keep changing projects; talk to the mall about splitting the 70 sqm shop into smaller units and subletting/转租 to recover cash flow.

## Calculation Logic

- Current炸鸡 model: 2,500/day sales x below20% margin = less than 500/day gross profit. 勇哥 uses 500/day as generous upper bound.
- Rent seasonality: 35,000/month x 11 paid months = 385,000/year. If大学商圈 effectively only does about8 months of business, rent burden becomes 385,000 / 8 = 48,125/month, about 1,604/day.
- Known fixed burden: effective rent about1,604/day + labor about933/day + utilities about167/day = about2,704/day before promotion amortization, platform代运营抽点, miscellaneous supplies, wastage, and owner time.
- Daily gap: gross profit less than500/day versus fixed burden about2,704/day, so loss is roughly2,200/day. Monthly loss is therefore about66,000, matching勇哥反复强调的6万多/月.
- If rent were naively counted as 35,000/month, daily rent would still be about1,167/day; even without school-season adjustment, gross profit would not cover rent plus labor.
- Current炸鸡 breakeven: fixed burden about2,704/day divided by20% margin = about13,500/day. Transcript gives about13,515/day. Since true margin is below20%, real breakeven would be even higher.
- Hypothetical刚需/社交餐 model: 勇哥 gives about4,900/day breakeven under a higher-margin assumption. This is not low: at 15元学生餐 it means about326-327份/day, roughly150+ orders at lunch and150+ at dinner; at about22元/单 it is still about223单/day.
- Seat/turnover check: if the 70 sqm store has roughly40 seats, 223单/day means lunch and dinner each need multiple table turns. For social/high-ticket food, even at about100-130元/桌, 4,900/day still requires roughly40 tables/day, and would need more marketing and stronger execution.
- Promotion logic: paid抖音、小红书、外卖运营 and percentage commissions are not rescue levers if the base gross margin is already too low. More orders through subsidized channels can increase loss rather than fix it.

## Diagnosis

This is a structural loss case, not a simple marketing problem.

- Category mismatch: 炸鸡 plus heavy外卖 competition is too low-margin for a 70 sqm, high-rent, high-labor storefront.
- Rent mismatch: university traffic looks large, but rent must be absorbed over only about8 effective months, not a full 12-month steady market.
- Location misunderstanding: 人多不等于好商圈. The island/大学城 has many students, but competition is dense, stores are scattered, and the specific position is not necessarily on the strongest meal path.
- Store-size mismatch: large glass/storefront and many seats create fixed cost, but the product and channel mix do not produce enough gross profit per square meter.
- Execution risk: owner is a new entrant in餐饮 and not deeply present in the shop, while any rescue category would require more day-to-day management, product control, and marketing.
- Data gap: owner does not really know nearby刚需店的流水 and uses isolated examples like a long-running烧烤店, but that benchmark has different maturity, staff structure, operating hours, and possibly thin profit.
- Wrong rescue instinct: adding another product or changing category does not solve the rent/labor/traffic math unless the required daily sales, order count, seats, and owner execution can all be proven.

## Recommendation Pattern

- Stop treating the issue as "再做一个品" or "继续投推广". First accept that the current model loses roughly2,000+ every operating day.
- Do not add another品类 inside the same cost structure. For this shop, even a higher-margin刚需/社交品类 has to reach about4,900/day and high turnover, which is unlikely from this position without heavy execution.
- Do not keep throwing money into代运营、抖音、小红书 or平台活动 before the unit economics are fixed.
- Prioritize止损 over经营改造. If the store can be closed or transferred, stopping the daily loss is economically equivalent to earning the amount no longer lost.
- Because there is no transfer fee and the contract is directly with the mall, negotiate with the mall/property about whether the 70 sqm shop can be partitioned into smaller units.
- 勇哥's salvage template: split into 3 smaller spaces, target around16,000/month each, total around48,000/month. Against nominal rent35,000/month, this creates about13,000/month spread; collecting deposits could also recover cash flow. This must depend on contract permission and proper sublease terms.
- When talking to the property, frame it as dividing the space for several family/related operators rather than simply saying the business failed; the useful transferable rule is to obtain permission and reduce/transfer fixed rent burden, not to continue the original restaurant model.
- If partition/sublease is not permitted, the fallback is still to negotiate exit/transfer quickly rather than keep testing new products.

## Reusable Heuristics

- In大学城, annual rent should be spread over real school-season business months. A rent that looks high monthly may become fatal when only8 months produce meaningful revenue.
- Low-margin delivery-heavy categories cannot carry high rent, large area, and full labor. First compare daily gross profit with daily rent, labor, and utilities.
- If daily gross profit cannot cover rent alone or rent plus labor, marketing is not the first answer.
- "人多" is not the same as "can sell enough at this exact point." Check competition density, flow concentration, meal path, nearby store performance, and whether comparable stores are mature outliers.
- Before换品, reverse-calculate required daily sales, then convert it into orders, tables, seats, turnover, and owner hours. If the physical and operational capacity cannot support it, changing品类 is just a new sunk cost.
- For absentee or semi-absentee owners, raise the execution threshold. Categories that look higher-margin often require more active management, not less.
- Promotion companies and platform campaigns must be treated as costs and margin reducers. If the merchant is subsidizing discounts, higher GMV can worsen cash loss.
- When a lease/location is structurally wrong but still attractive to other tenants,分割转租/转让 can be a business rescue path. The goal is fixed-cost transfer and cash recovery, not proving the original food model right.
