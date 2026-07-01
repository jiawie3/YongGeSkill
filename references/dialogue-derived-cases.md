# Dialogue-Derived Cases

This file contains distilled notes from actual video dialogue transcripts. It should grow over time from `corpus/transcripts/*.json`. Use it ahead of title-only patterns when a user's case resembles one of these notes.

Do not paste full transcripts here. Store raw ASR output in `corpus/transcripts/` and store only facts, questions, calculations, diagnosis, and reusable heuristics here.

## Case 7: 40万开炸鸡, 毛利20%不到, 每月亏约6万

- Source: `BV1GnfqB6Eq7`
- Raw ASR: `corpus/transcripts/7_BV1GnfqB6Eq7.json`
- ASR model: faster-whisper `small`, Chinese, VAD enabled.
- Reliability: usable for business facts and question order, but still needs human review for exact wording.

### User Facts Extracted

- Category: 70-square-meter fried chicken store in Guangzhou.
- Location: university-area business district; business is strongly seasonal because students are present for only part of the year.
- Current average daily revenue: about 2,500.
- Gross margin: owner says under 20%.
- Channel mix: about half dine-in and half delivery; another line suggests delivery may be around 60%.
- Rent: 35,000 per month; rent is paid for 11 months, but the realistic selling season is about 8 months, so 勇哥 annualizes then re-allocates rent across real operating months.
- Water/electricity: about 5,000 per month.
- Labor: about 28,000 per month.
- Investment: about 400,000; no franchise.
- Store status: owner is semi-absent/托管-like, not fully present every day.
- Loss: dialogue repeatedly frames it as roughly 2,000 per day and around 60,000+ per month.

### Yongge Question Order

1. Look at the storefront and ask whether the whole big shop is the user's.
2. Challenge the mismatch between a large store and a small sign/weak visible storefront.
3. Ask current daily revenue.
4. Ask city and shop size.
5. Ask gross margin.
6. Ask dine-in versus delivery share.
7. Ask rent and whether rent is monthly or yearly.
8. Recalculate annual rent against the real student-business season.
9. Ask utilities and labor.
10. Ask total investment and whether it is franchised.
11. Ask where the remaining investment went: rent deposit, decoration, equipment, promotion, delivery/TikTok operations.
12. Ask owner involvement and prior work.

### Calculation Logic

- At 2,500 daily revenue and under 20% gross margin, daily gross profit is only about 500.
- Rent alone is 35,000/month nominal; if 11 months of rent must be covered by about 8 effective student months, the effective monthly rent is about 48,000, or about 1,600 per day.
- Labor adds about 933 per day before utilities and other costs.
- Rent + labor already exceed gross profit by a wide margin, so "more effort" cannot fix the structure.

### Diagnosis

The fatal issue is not one small operational flaw. It is a broken unit model:

- Low gross margin.
- High fixed rent.
- High labor.
- Seasonal student demand.
- Large store and weak storefront efficiency.
- Owner not fully operating the shop personally.

### Recommendation Pattern

The core advice pattern is immediate stop-loss logic:

- If closing the store reduces daily loss by around 2,000, closing is economically equivalent to earning that amount compared with continuing.
- Do not keep adding promotion spend when the basic gross-margin and fixed-cost structure is upside down.
- Recalculate rent against true selling months, not calendar months.

### Reusable Heuristics

- When gross margin is only around 20%, revenue can look busy while the store is still dying.
- A university-area store must calculate revenue over the months students are actually present.
- Convert monthly rent and labor into daily burden; compare it with daily gross profit.
- If daily gross profit cannot even cover rent and labor, the case is structural, not marketing.
- Big shop + small sign + weak owner presence is a dangerous combination.

## Case 10: 90万加盟石锅拌饭, 官网/总部路径不清, 两个月亏6万

- Source: `BV1TWfyBQEVW`
- Raw ASR: `corpus/transcripts/10_BV1TWfyBQEVW.json`
- ASR model: faster-whisper `small`, Chinese, VAD enabled.
- Reliability: usable for business facts, cost split, question order, and contract-risk pattern; exact wording still needs human review.

### User Facts Extracted

- Category: Korean-style stone-pot rice / bibimbap store.
- City: Hangzhou Yuhang.
- Franchise path: user originally wanted to contact another brand, left/used a phone number, then an招商经理 contacted them and pushed a different brand.
- Key uncertainty: whether the user truly found the official headquarters site and phone number; caller relies on hotline/website/招商 explanation.
- Current daily revenue: under 1,000, down from about 3,000 at opening.
- Gross margin: about 50%, so daily gross profit is only about 500 at current revenue.
- Store size: about 124 square meters.
- Rent: about 30,000 per month.
- Labor: three people, roughly 500 per day / about 15,000 per month.
- Utilities: about 5,000 per month.
- Current loss: calculated in dialogue as about 1,100+ per day and more than 30,000 per month; two months lost about 60,000.
- Total investment: more than 900,000.
- Franchise fee: about 158,000.
- Equipment/table/chair package: about 118,786, from headquarters.
- First batch materials: about 150,000.
- Decoration: about 190,000, self-arranged.
- Large amount paid to headquarters: dialogue frames headquarters-related payments as around 400,000+.
- Contract risk: there is a "20 months no payback/store buyback or recovery" style clause, but the recovery amount requires the other party's confirmation and is not an automatic refund.
- Owner intent: wanted a financial investment, with headquarters/store manager handling much of the operation; user did not deeply participate in actual operation.

### Yongge Question Order

1. Ask what store/category and city.
2. Immediately challenge the brand path: did the user actually find the company headquarters and official website?
3. Ask how the招商经理 contacted the user and whether the user may have been diverted from the intended brand.
4. Pause brand debate and ask the operating basics: daily revenue.
5. Ask gross margin.
6. Ask store area.
7. Ask rent.
8. Convert rent to daily burden and compare it to daily revenue/gross profit.
9. Ask labor and utilities.
10. Calculate daily and monthly loss.
11. Ask total investment.
12. Ask why investment is so high: franchise fee, rent/deposit, equipment, furniture, materials, decoration, warehouse, headquarters payments.
13. Ask whether equipment/materials came from headquarters.
14. Review the user's contract/申请/回收条款 and test whether the clause actually protects the user.
15. Ask whether headquarters selected the location and how often they came to the store.
16. Ask why the user believed the team: claimed relation to a successful brand, ex-team story, financial-investment pitch, and outsourced store manager.

### Calculation Logic

- Under 1,000 daily revenue at 50% gross margin gives only about 500 daily gross profit.
- Rent alone is about 1,000 per day.
- Labor adds about 500 per day.
- Utilities add roughly 166 per day.
- Before other fees, the store is already around 1,100+ per day underwater.
- If monthly rent is 30,000 and a "20 months" condition must be survived before any recovery discussion, rent alone can become a huge additional burn; a recovery clause is not meaningful if the store cannot survive that long.

### Diagnosis

This is not merely a bad first-month operation problem. It combines:

- Unclear brand/contact path.
- Heavy franchise and headquarters-related front-loaded payments.
- Oversized store and high rent relative to sales.
- Revenue collapse after opening.
- Owner treated the shop as a passive financial investment.
- Contract protection that sounds comforting but may not be practically enforceable.

### Recommendation Pattern

- Before paying a franchise, verify the official company, site, phone, contract subject, payment subject, direct stores, and whether the brand relationship is real.
- Do not let招商 turn a user's intended brand into another "related" brand without proof.
- Treat "20 months no payback then recovery" clauses as weak unless the recovery amount, trigger, and obligation are concrete and enforceable.
- If current daily gross profit cannot cover rent, labor, and utilities, do not keep funding the store while waiting for headquarters.
- Save contract, payment records,招商承诺, site-selection records, chat logs, and media/report materials before pursuing negotiation or legal consultation.

### Reusable Heuristics

- The moment a user says "我本来想加盟A，后来招商给我推B", enter brand-diversion due diligence.
- A hotline or website shown by招商 is not enough; verify legal entity and official channels independently.
- "总部派店长/代运营" does not remove the owner's cash-flow risk.
- High opening investment plus low current gross profit is a stop-loss case before it is a marketing case.
- A buyback/recovery clause that only works after long survival may be a psychological comfort, not a financial safety net.

## Reviewed Case Index

Use these reviewed notes when a user's situation matches the pattern. Load the linked file for full facts, question order, calculations, diagnosis, and recommendation.

### Case 5: 宝妈负债开中药奶茶, 小学门口三个月亏光

- Full note: `corpus/reviewed-case-notes/5_BV1RKq6BcEWu.md`
- Pattern: official-channel failure + weak养生奶茶 franchise + school-gate demand illusion + borrowed family money.
- Key numbers: half-month revenue under 1,000; monthly sales estimated about 2,000; employee 3,000/month; rent about 20,000/year; utilities about 1,200-1,400/month; total investment about 220,000-230,000, all borrowed.
- Yongge move: reconstruct "wanted known brand but did not find official contact" before discussing operation, then test whether school flow actually buys.
- Recommendation: fire employee, record after-school flow, switch only if real demand supports low-price snacks, and immediately organize evidence for refund/complaint/legal consultation.

### Case 6: 负债加盟杂牌汉堡, 菜单大杂烩, 每天约亏400

- Full note: `corpus/reviewed-case-notes/6_BV1kHZuBGE4E.md`
- Pattern: already opened + franchise + debt + owner cannot calculate margin + menu too broad.
- Key numbers: revenue roughly 1,700/day; rent about 277/day; counted labor about 333/day; utilities about 140/day; transcript frames daily loss around 400.
- Yongge move: stop asking "怎么提升业绩" until product-level gross margin is calculated.
- Recommendation: cut labor, drop the headquarters "everything menu", choose one local just-demand category, calculate each product's true cost, and ask headquarters for refund/fee relief with records.

### Case 8: 想加盟米村被导流, 40万开杂牌拌饭后改为自救

- Full note: `corpus/reviewed-case-notes/8_BV1uJfcBvEiN.md`
- Pattern: intended famous brand + online phone diversion + weak brand + mall-tail location + low-rent family rescue.
- Key numbers: average sales about 1,050/day; gross margin about 50%; rent about 4,583/month; family labor counted about 12,000/month; utilities about 200/day; investment 400,000+; headquarters-side payment about 245,000.
- Yongge move: verify whether the company has real direct stores, then separate rights protection from simplified self-owned operation.
- Recommendation: remove weak brand sign, focus on拌饭 plus simple staples, cut electricity/menu complexity, send解除 notice, and pursue fee/material recovery with evidence.

### Case 11: 大学生助学贷网贷开麻辣烫, 14万亏损后应尽快关转

- Full note: `corpus/reviewed-case-notes/11_BV1ghZYBWEFv.md`
- Pattern: fresh graduate + student loan/online loan + no experience + weak old-mall alley location + stronger nearby competitor.
- Key numbers: sales about 700/day; gross margin about 40%-45%; rent about 2,500/month; counted labor about 12,000/month; utilities about 30/day; daily loss about 200; total investment about 140,000+.
- Yongge move: calculate loss, then shift the core advice from menu repair to life-stage correction.
- Recommendation: close or transfer quickly, cut labor while waiting, go work/study as an应届生, repay debt, and treat the loss as tuition rather than adding another project.

### Case 20: 县城杂牌奶茶夹在霸王蜜雪古茗旁, 30万投入应关转维权

- Full note: `corpus/reviewed-case-notes/20_BV16oZxBpEnb.md`
- Pattern: county-town milk tea + weak brand beside head brands + one-year prepaid rent + no catering experience.
- Key numbers: first-month revenue about 4,000+; average sales about 150/day; 60% margin gives about 90/day gross profit; rent 150,000/year; labor about 200/day; daily loss about 596; investment about 300,000.
- Yongge move: compare weak brand choice with head-brand effect, then calculate whether closing loses less than opening.
- Recommendation: stop operating, list transfer/sublease immediately, recover remaining rent value, preserve evidence, and seek refund/material/legal workflow against headquarters where supported.

### Case 21: 40万加盟铁板烧, 高租金外围街边店, 开业10天月亏4.5万

- Full note: `corpus/reviewed-case-notes/21_BV1MnfgBdE4L.md`
- Pattern: newly opened + high rent + novelty/social category + weak natural flow + headquarters PPT site selection.
- Key numbers: sales often 300-1,000/day; rent about 733/day; 5 staff about 20,000/month after cutting from 11; utilities about 10,000/month; monthly loss about 45,000.
- Yongge move: compare current sales to rent alone, then inspect whether the shop is actually in the mall flow or only near it.
- Recommendation: treat it as structural stop-loss; do not "再坚持" or add promotion unless the natural-flow problem is solved.

### Case 28: 21万接盘商场拌饭店, 月租3万, 月亏约1.9万

- Full note: `corpus/reviewed-case-notes/28_BV1G6ZTBHEws.md`
- Pattern: takeover/transfer + headquarters handoff + weak mall + user under-verifies old data.
- Key numbers: sales about 3,000/day; gross margin about 45%; rent 30,000/month; labor about 25,000/month; utilities about 5,000/month; break-even about 4,400/day; monthly loss about 19,000.
- Yongge move: unpack the transfer price into deposit, rent, stock, and real store value; challenge "material recharge subsidy" as not real rescue.
- Recommendation: transfer during the next high-traffic window while brand/store still has residual value; do not buy more materials.

### Case 479: 60万漂亮饭/生日宴场景店, 9个员工, 月亏约1.5万

- Full note: `corpus/reviewed-case-notes/479_BV1mdDCBhEUy.md`
- Pattern: pretty scene store + oversized space + no repeat-purchase logic + too many cuisines + high labor.
- Key numbers: about 3,000/day sales; 55% gross margin; rent 20,000/month; labor 42,000/month; utilities 5,000/month; daily loss about 582.
- Yongge move: force the owner to choose whether she sells scene/package or runs a normal restaurant.
- Recommendation: pivot to scene/event package sales, remove full kitchen complexity, cut 9 staff down to about 2-3, and focus on short-video/private-domain booking conversion.

### Case 480: 深圳860平自营火锅, 投200万+, 月销70万才保本

- Full note: `corpus/reviewed-case-notes/480_BV16C9LB2Emg.md`
- Pattern: expansion/large store + unproven first-store payback + optimistic margin + weak parking/natural flow.
- Key numbers: 860 sqm; rent about 103,000/month; labor around 180,000/month; fixed costs about 350,000/month; break-even about 700,000/month or 22,000/day; investment over 2 million.
- Yongge move: challenge the gross-margin assumption, first-store proof, parking, and the real reason customers would travel to this shop.
- Recommendation: if reversible, shrink or split the store. If forced to open, track half-year cash burn, paid-traffic cost, repeat rate, table utilization, and prepare for splitting into two projects.

### Case 58: 找不到蜜雪官网被截流, 48万开杂牌奶茶, 月亏约1.7万

- Full note: `corpus/reviewed-case-notes/58_BV1sbzaBcEev.md`
- Pattern: already paid/opened + official-channel failure + headquarters charges + weak site + refund/legal workflow.
- Key numbers: sales often 100-300/day; rent about 8,500/month; current labor about 9,600/month; loss about 573/day; total investment about 480,000; headquarters-side payments about 264,690.
- Yongge move: reconstruct the exact contact path and prove the user never reached the true official brand channel.
- Recommendation: stop operating, send termination notice, preserve evidence, negotiate, complain through regulators if no franchise filing/qualification issue exists, then litigate only after evidence is organized.

### Case 191: 三孩单亲妈妈想负债加盟奶茶, 未付款前被截停

- Full note: `corpus/reviewed-case-notes/191_BV1NNXSBUEdD.md`
- Pattern: planned opening + vulnerable user + short-video project ads + debt-funded milk tea.
- Key numbers: expected investment rising from 100,000 to 200,000+; possible debt about 100,000; rent around 80,000-90,000/year; labor about 9,000/month; break-even about 1,444/day before hidden costs.
- Yongge move: stop the sales funnel first, then calculate. Block project contacts and stop consuming project ads before more "research".
- Recommendation: do not sign or pay; test any old stationery-channel idea without opening a store; avoid milk tea/coffee/hamburger/bakery as first debt-funded project.

### Case 283: 负债开面包店, 供应链毛利低, 街边汽修带位置

- Full note: `corpus/reviewed-case-notes/283_BV12Z5v6nEQi.md`
- Pattern: debt-funded bakery + headquarters supply chain + no stopping flow + "community nearby" illusion.
- Key numbers: sales about 1,250/day; gross margin about 40%; rent 4,500/month; labor about 15,000/month; utilities about 4,500/month; daily loss about 300; investment about 270,000-280,000.
- Yongge move: compare imagined community demand with the actual door-front path and neighboring auto-repair businesses.
- Recommendation: close, negotiate equipment/material/franchise-fee return, and stop debt-funded experimentation.

### Case 287: 宝妈租2万月租面馆, 未正式开业前被劝停

- Full note: `corpus/reviewed-case-notes/287_BV1v6LE6QE3w.md`
- Pattern: planned store + family-convenience site selection + school-adjacent overcount + high first-floor rent.
- Key numbers: rent 20,000/month; area about 95 sqm with only 45 sqm downstairs; labor plan about 22,500/month; utilities about 5,000/month; break-even about 3,166/day.
- Yongge move: separate "I live upstairs/my kids attend school here" from real market demand and competitor share.
- Recommendation: stop decoration and sublease/transfer quickly because no transfer fee was paid and the lease is only days old.

### Case 296: 60万烧烤音乐酒馆, 2个月日销1000, 立即止损

- Full note: `corpus/reviewed-case-notes/296_BV1D2Lz6MEHS.md`
- Pattern: already opened + big decoration + no餐饮经验 + neighbor-queue spillover fantasy.
- Key numbers: sales about 1,000/day; gross margin about 50%; rent about 15,277/month; labor about 21,600/month before owner labor; loss about 1,000/day; investment 600,000+ with 100,000 transfer fee.
- Yongge move: test whether the street has real night-economy flow and whether neighbor traffic belongs to the neighbor's old brand.
- Recommendation: immediate stop-loss, transfer/rent out part of the space, and stop adding concepts.

### Case 307: 老店果切老板想40万扩鲜榨果汁, 人流不等于客流

- Full note: `corpus/reviewed-case-notes/307_BV1akG86uEmT.md`
- Pattern: old profitable store + failed prior branches + partner pressure + unpaid transfer fee + high-rent expansion.
- Key numbers: rent 23,000/month; transfer fee 60,000 not yet paid; agency fee 23,000; labor plan about 22,000/month; utilities about 3,000-4,000/month; total budget about 400,000; break-even roughly 2,285/day at 70% margin before hidden costs.
- Yongge move: make the owner explain why the old store made money, why two branches lost money, and whether visible人流 can become客流 at 20-30 yuan/cup.
- Recommendation: do not pay transfer fee or sign; guard the old store, avoid partner-funded expansion, and validate any future site by real conversion and competitor data.

### Case 308: 广场集装箱炸串月租1.2万, 不能外卖应打包转让

- Full note: `corpus/reviewed-case-notes/308_BV1GaGv6HEc9.md`
- Pattern: mall/plaza container kiosk + high rent density + no delivery permit/conditions + ordinary snack product + transfer-first stop-loss.
- Key numbers: sales about 250/day; actual margin about 50%; rent 12,000/month; labor 6,800/month; utilities about 60/day; daily loss about 560; monthly loss about 16,800-17,000; investment about 160,000.
- Yongge move: reject product-switch fantasies and reframe the "product" as the store package that must be sold.
- Recommendation: package brand/equipment/booth/traffic for transfer, use any rent reduction to improve transferability, and stop adding new categories or equipment.

### Case 329: 封闭职高校内独家奶茶日赚13块, 品牌口碑坏了应重做

- Full note: `corpus/reviewed-case-notes/329_BV1waVh6fELh.md`
- Pattern: closed campus + only one milk-tea slot + weak/local brand bad口碑 + low rent but labor eats profit.
- Key numbers: 3,000 resident students; April 15-30 sales about 7,900, roughly 530/day; gross margin about 40%; rent 100/month plus 15% school commission; labor about 5,000/month; utilities about 900/month; profit about 13/day; takeover about 180,000+.
- Yongge move: identify this as a rare positive captive-demand case and separate real demand from damaged product/brand trust.
- Recommendation: redo signage/products immediately, add permitted summer drinks, submit a stronger student-recognized brand application early, and use summer break for reset if approved.
