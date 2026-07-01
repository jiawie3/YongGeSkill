# Diagnostic Protocol

Use this file whenever the user asks whether to open, save, transfer, close, join, or take over a food business.

## First Classification

Ask one classification question if unclear:

```text
你现在是哪种情况：还没签、已签没开、已开亏钱、想接盘、想加盟、想扩店、合同退款纠纷？
```

Then follow the matching branch.

## Branch A: Already Open And Losing Money

Ask for these facts. If the user gives only one loss number, do not diagnose yet.

Required:

- 城市、商圈、具体位置：学校/商场/社区/办公/景区/街边/夜市/外卖店。
- 品类、是否加盟、店铺面积、营业时段。
- 开业多久，总投入，剩余现金，是否负债。
- 月租金+物业，人工人数和工资，水电燃气，平台/软件/贷款等固定支出。
- 日均流水，最好/最差日流水，客单价，日单量。
- 毛利率或食材成本率；堂食/外卖占比；平台抽佣、包装、满减。
- 每月亏损是否包含老板工资。
- 竞品、门头可见度、进店动线、停车/外摆/排队条件。

Default rescue sequence:

1. Calculate true monthly loss and break-even daily revenue.
2. Decide whether the gap is operational or structural.
3. If daily revenue is less than 50% of break-even after 60-90 days and the site has no obvious repair lever, prefer stop-loss.
4. If revenue is near break-even but cost structure is bad, test cost cuts, category simplification, hours, signage, group buying/takeaway structure, and gross-margin repair.
5. If losses are caused by franchise supply price, platform fees, low margin, or rent, do not rely on "more effort" alone.

## Branch B: Planned Opening

Ask:

- 你准备用自己的闲钱、家庭现金流，还是借钱/贷款？
- 之前有没有在这个品类干过？干了多久？
- 为什么选这个品类：会做、看别人赚钱、自己爱吃、总部推荐、朋友劝？
- 店址在哪，租金多少，转让费多少，面积多少，周边竞品是谁？
- 总预算怎么拆：加盟费、装修、设备、首批物料、押金、房租、人工、流动资金。
- 预计日流水、客单价、日单量、毛利率从哪里来？
- 最坏情况下连续亏 6 个月，家里能不能承受？
- 租赁、押金、转让费、证照、油烟/消防、合伙规则是否已经核清？

Default recommendation:

- Borrowed money + no category experience + franchise pitch + high rent = default no.
- Owner has worked in the category, site has real demand, rent is controllable, and break-even is reachable = allow small test before heavy investment.
- For a first store, prefer low fixed cost, low transfer fee, clear复购, and a model the owner can personally operate.
- If lease, permits, transfer price, or partner rules are unclear, read `pre-signing-risk-checks.md` and pause signing before judging the business idea.

## Branch C: Franchise Due Diligence

Ask:

- 品牌名、总部公司全称、招商联系人、合同主体。
- 加盟费、保证金、管理费、设备费、装修费、首批物料、强制进货比例。
- 是否已经签合同或付款；付款到哪个主体；有没有发票/收据。
- 总部是否有直营店；直营店地址；是否允许实地查账。
- 选址是谁选；亏损总部承担什么责任；退出和退款条款。

Then read `franchise-due-diligence.md` and browse current public sources.

## Branch D: Takeover Or Transfer

Ask:

- 原店为什么转让，开了多久，真实月流水和流水凭证。
- 转让费、剩余租期、房东是否同意重签、能否办证。
- 设备能不能用，装修是否适配你的品类。
- 原店日客流、复购、差评、平台账号能否转。
- 接盘后是否还要追加装修、换设备、换菜单。
- 油烟、消防、燃气/电量、外摆、招牌、二房东授权和转租条款是否满足你的品类。

Default logic:

- Do not buy someone else's problem.
- Treat transfer fee as dead cost.
- If the old store could not make money with the same site and same人群, require a clear new reason why you can.
- Read `pre-signing-risk-checks.md` before advising on any transfer fee or takeover package.

## Branch E: Site Selection

Ask:

- 这个点位谁经过，为什么停，为什么买，什么时候买。
- 如果用户有照片/视频/地图截图，先读 `visual-site-analysis.md`，按门头、左右邻店、对面、动线、地图 POI 和位置可信度做视觉问诊。
- 早中晚各 30 分钟真实人流观察，不要只看地图热力。
- 周边 300 米竞品：价格、排队、复购、营业时间。
- 房租占预估流水比例；是否有外摆、停车、门头、油烟、证照限制。
- 店铺是不是在顾客动线死角：二楼、背街、商场冷区、学校门外反向动线。
- 房东链条、租赁期限、付款周期、押金、转租、装修限制和能否办证。

Default logic:

- Location can kill努力.
- If顾客进不来 or看不见, marketing cannot fully fix it.
- A "便宜租金" often buys的是没有需求 or没有动线.

## Branch H: Lease, License, Transfer Fee, Or Partnership

Use when the user asks "这个铺能不能签/要不要接/转让费贵不贵/能不能合伙/证照怎么办".

First read `pre-signing-risk-checks.md`, then ask:

- 现在交了多少钱，下一步要交多少钱，哪一步会变成不可逆投入。
- 合同主体、房东链条、租赁期限、押金、付款周期、转租/提前退租条款。
- 品类是否能办营业执照、食品许可/备案、油烟、消防、燃气/电量、外摆和招牌。
- 转让费如何拆分，是否有 6-12 个月完整后台和支付流水。
- 合伙人各自投钱、出力、工资、分红、亏损上限、经营权和退出规则。

Default logic:

- 没核清房东、证照、转让费和合伙规则前，不签、不装修、不买设备。
- 小定金阶段是最好止损窗口；不要为了追回小钱进入大投入。
- 合伙不是凑钱，必须能补能力、能定权责、能退出。

## Branch G: Visual Site Or Map Screenshot

Use when the user uploads storefront photos, surrounding street photos, a 360-degree sweep, a map screenshot, or a map pin.

First read `visual-site-analysis.md`, then:

- Extract visible facts and state confidence.
- If exact location is not readable, ask for city + address/pin/map link.
- If a map screenshot gives a verifiable location and current POIs matter, browse public/map sources before claiming current surroundings.
- Do not replace financial diagnosis with visual judgment; still ask for rent, area, category, expected/current sales, gross margin, and labor.
- Give a site-risk conclusion only after separating visible evidence from assumptions.

## Branch F: Expansion

Ask:

- First store has been profitable for how many months after owner salary?
- Profit is from system or from owner亲力亲为?
- Can product, staff training, procurement, quality, and cash control be copied?
- Will the second store cannibalize the first?
- Is expansion funded by profit or debt?

Default logic:

- One store刚赚钱 is not a system.
- Do not expand to solve焦虑.
- Expand only after the first store can survive without the owner standing there every day.

## If The User Refuses Numbers

Say:

```text
不算账我没法给你勇哥式判断。餐饮不是凭感觉救的。你先把租金、人工、日流水、毛利率、剩余现金这五个数给我。
```
