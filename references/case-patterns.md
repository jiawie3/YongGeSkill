# Case Patterns

This file summarizes recurring patterns from the 504 public Bilibili season titles collected in `bilibili-season-cases.tsv`.

Important: use this only as a discovery index. For actual 勇哥-style reasoning, prefer `dialogue-derived-cases.md` and `corpus/case-notes/` because they are distilled from dialogue transcripts.

## High-Frequency Patterns

- Monthly loss is the dominant story shape: many cases are framed as `月亏X`, `每天亏X`, `亏光`, or `赔光`.
- Franchise risk appears repeatedly: `加盟`, `杂牌`, `总部`, `跑路`, `官网`, `快招` style risk.
- Debt pressure is common: `负债`, `贷款`, and family savings show up as forcing functions.
- Site selection is a repeated cause: `房租`, `位置不行`, `顾客进不来`, `学校旁`, `商场`, `接盘`, `转让`.
- Users often over-trust preference, identity, or confidence: "自己爱吃", "宝妈", "大学生", "教授", "歌手", "夫妻", "亲戚员工".
- Food categories cluster around milk tea, coffee, burger, hot pot, barbecue, fried chicken, rice bowls, buffet, yogurt, skewers, malatang, pizza, chicken cutlet, bakery, noodles, and snacks.

## Pattern To Diagnosis

### Low Data + Big Confidence

Observed in titles such as school-adjacent milk tea, self-liked category, or debt-funded openings.

Diagnosis:

- Ask for numbers immediately.
- Challenge the reason for demand.
- Refuse to judge from confidence.

### Franchise + Weak Brand + High Fee

Observed in many `加盟杂牌` or `总部跑路` titles.

Diagnosis:

- Browse for headquarters, direct stores, filing, trademark, complaints, and contract subject.
- Treat pay-before-verification as dangerous.
- Separate "brand story" from unit economics.

### High Rent + Low Revenue

Observed in titles mentioning rent such as monthly rent 20k/30k or high mall/street costs.

Diagnosis:

- Calculate break-even daily revenue first.
- If current revenue is far below the break-even line, marketing is unlikely to save it.
- Stop adding decoration, equipment, or new categories until rent pressure is solved.

### Low Gross Margin

Observed in titles such as gross margin around 20%.

Diagnosis:

- Food retail cannot survive on revenue alone.
- Recalculate contribution margin after platform, packaging, discounts, and waste.
- If supply chain/franchise procurement locks margin, consider exit.

### Takeover Trap

Observed in `接盘` and transfer-fee cases.

Diagnosis:

- Ask why the previous owner failed.
- Require verifiable revenue records, landlord consent, and license feasibility.
- Treat transfer fee as dead money.

### Sunk-Cost Spiral

Observed in cases where the owner loses one store then adds another investment.

Diagnosis:

- Reset from tomorrow.
- Ask whether further spending changes the structural constraint.
- Prefer controlled test or closure over "再砸一点".

## Case Search Tips

Use `rg` on `references/bilibili-season-cases.tsv`:

```bash
rg "奶茶|咖啡|火锅|加盟|月亏|房租|接盘|负债" references/bilibili-season-cases.tsv
```

When answering, do not cite a title as if it were a transcript. Use titles only to identify recurring public case patterns.
