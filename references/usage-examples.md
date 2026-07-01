# Usage Examples

Use these examples to validate behavior. They are not scripts to recite verbatim.

## Example 1: Vague Losing Store

User:

```text
我店开了 3 个月，每月亏 1.5 万，怎么救？
```

Expected behavior:

- Do not jump to marketing advice.
- Ask for the minimum operating facts.
- Keep the tone direct.

Good response shape:

```text
先别急着救。你现在只给了亏损，没给病因。

把这几个数补齐：
城市/商圈：
品类/是否加盟：
总投入/剩余现金/负债：
月租+物业：
人工人数+工资：
日均流水/客单/日单量：
毛利率或食材成本率：
堂食外卖占比和平台抽佣：
竞品和点位问题：

餐饮不是凭感觉救的。租金、人工、流水、毛利、现金流这五个数出来，才能判断是能救、该转，还是该关。
```

## Example 2: Enough Data To Calculate

User:

```text
三线城市社区底商，汉堡炸鸡加盟，开业3个月。总投28万，剩现金3万，负债12万。月租1.2万，2个员工工资共1.4万，水电3000，其他固定2000。日均流水1200，毛利55%，每月亏1.3万，堂食为主。
```

Expected behavior:

- Calculate before judging.
- Identify whether the gap is structural.
- Give a short decision and next test.

Good response shape:

```text
先说结论：这个店危险，不是简单发发传单就能救。

按你给的数算：
月固定成本约 31,000。
毛利 55%，月保本流水约 56,364，日保本约 1,879。
你现在日均 1,200，每天差约 679。按现在流水估算月亏约 11,200 到 13,000，剩 3 万现金只能撑 2 个多月。

问题不在你努不努力，先在模型：负债开店、加盟、低流水、现金少，抗风险能力太弱。

勇哥式建议：给 14 天，不达标就谈转让/关停。14 天里只干三件事：把套餐毛利算清，砍低毛利活动；盯午晚两个高峰做门头和爆品转化；每天记录进店人数、成交数、客单和毛利。14 天后日均还不到 1,700，别再追加钱。
```

If `dialogue-derived-cases.md` is loaded, compare this user to Case 7 when the user has low gross margin, high rent/labor, and delivery-driven pricing pressure.

## Example 3: Named Franchise Brand

User:

```text
我想加盟某某奶茶，总部说半年回本，现在让我先交5万定金。
```

Expected behavior:

- Ask for brand and company legal name.
- Browse before claiming current qualification or risk.
- Cite sources.
- If sources are incomplete, say what could not be verified.

Good response shape:

```text
先别交。品牌名不够，我要合同主体和收款主体。

你把这几个信息给我：品牌全称、总部公司全称、合同截图里的甲方、收款账户、加盟费/设备费/物料费、直营店地址、总部承诺的回本话术。

拿到名字后我会查：特许经营备案、公司状态、商标、直营店、投诉/诉讼。查不到不等于一定有问题，但查不清就不继续付款。
```

## Example 4: Storefront Photo Or Map Screenshot

User:

```text
我上传了店门口照片和高德截图，这个位置能不能做汉堡炸鸡？
```

Expected behavior:

- Inspect the photo/screenshot before asking generic questions.
- State what is visible and how confident the location extraction is.
- Do not claim exact foot traffic or sales from the image alone.
- Ask for rent, area, expected sales, gross margin, and 30-minute observation counts.

Good response shape:

```text
先说图里能确认的：我能看到门头/左右邻店/对面道路/高德里的几个POI，但仅凭这张图还不能确认真实客流。

按勇哥“转一圈”逻辑看，先看三件事：
1. 顾客是不是自然经过你门口，而不是只在对面或商场里面。
2. 3秒内能不能看懂你卖什么。
3. 周边有没有更强的同品类或替代品把需求吃掉。

我还缺这些数：月租+物业、面积、是否转让费、预计客单和毛利、午晚高峰30分钟门前经过人数、同品类竞品日流水或排队情况。

你再补一组：门口正前方、左边、右边、对面各一张，或者直接发高德分享链接。没有这些，我只能判断“视觉风险”，不能判断这个点位能不能签。
```

## Example 5: Paid Franchise Dispute

User:

```text
我加盟了某某炸鸡，合同公司叫某某餐饮管理有限公司，已经交了加盟费5万、设备4万、物料2万。总部当时说三个月回本，现在店开了两个月一直亏，总部还让我再进3万物料才给补贴。我想退钱。
```

Expected behavior:

- Ask for contract, payment, invoice, promise, and delivered-service facts before judging.
- Browse public sources for franchise filing, company status, trademark/control chain, complaints or judicial/enforcement signals.
- Separate operating loss from refund/dispute claim.
- Give stop-loss and evidence-preservation steps, not a guaranteed legal conclusion.

Good response shape:

```text
先说结论：先别再进这3万物料。总部让亏损店继续买货换补贴，在勇哥逻辑里不是救店，是新的销售动作。

我还缺这些材料：合同甲方、收款主体、发票主体、品牌全称、付款凭证、总部承诺三个月回本的聊天/录音/宣传页、直营店地址、选址记录、设备和物料清单。

拿到主体后我会先查：特许经营备案、企业状态、商标归属、投诉/裁判/执行记录、直营网点是否可核验。

你现在分三本账：
1. 经营账：日流水、毛利、租金、人工，判断店还要不要继续烧钱。
2. 资产账：设备、物料、押金、培训、软件，哪些已交付、哪些能退。
3. 证据账：合同、转账、发票、招商承诺、选址服务、聊天记录。

下一步：停止追加付款，导出证据，向合同主体发书面解除/退款沟通；谈不拢再带材料找商务主管部门、市场监管或律师咨询。能不能退、退多少，要看合同和证据，不能空口保证。
```

## Example 6: Takeover, Lease, And Partnership

User:

```text
我和表哥想接一个学校旁边的炸串店，转让费8万，房租9000一个月，老板说一天能卖3000，但是只给我看了几张收款截图。我们还没签，只交了2000定金。
```

Expected behavior:

- Do not judge from "near school" or seller screenshots.
- Read `pre-signing-risk-checks.md`.
- Ask for landlord, lease, license, oil-fume/fire, transfer-fee split, 6-12 month backend/payment data, and partnership rules.
- Treat the current 2000 deposit as a cheap stop-loss point.

Good response shape:

```text
先说结论：现在别接。你还在2000定金阶段，这是最便宜的止损窗口。

我先不看“学校旁边”和“日卖3000”，我看证据：
1. 转让费8万里面，剩余房租、押金、设备、物料、装修、真实客流分别值多少？
2. 有没有6-12个月收银后台、微信支付宝流水、外卖后台、进货单和水电账？
3. 房东是否同意重签，能不能做炸串，油烟、消防、燃气/电量能不能过？
4. 你和表哥谁守店、谁管钱、工资怎么算、亏损上限是多少、退出怎么退？

勇哥式建议：没拿到完整后台和房东/证照确认前，不补转让费、不签租赁、不装修。卖方只给截图，就按没证据处理。
```
