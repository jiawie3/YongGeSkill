# Franchise Due Diligence

Use this file whenever the user names a franchise brand, headquarters,招商公司, or contract/refund issue.

## Required User Facts

Ask for:

- 品牌名 and headquarters company full legal name.
- Contract subject, payment subject, and invoice/receipt subject.
- Amounts paid: franchise fee, deposit, management fee, equipment, decoration, first materials, training, site-selection fee.
- Whether a contract is signed and whether the store has opened.
- The user's current goal: verify before paying, stop signing, terminate, refund, return materials/equipment, claim damages, keep operating, or close/transfer.
- Whether headquarters promised revenue, site selection, refund, buyback, or exclusive territory.
- Direct-store addresses and whether the user inspected them in person.

## Browse Before Judging

Search current public sources before making a risk call:

1. Commercial franchise filing or official regulator pages for the company/brand. Start with the MOFCOM commercial franchise system: `https://txjy.mofcom.gov.cn/` and, when available, the filing query page `https://txjy.syggs.mofcom.gov.cn/index.do?method=entpsearch`.
2. National Enterprise Credit Information Publicity System or accessible enterprise profiles for registration, abnormal operations, penalties, and shareholders.
3. Trademark pages if the brand ownership is disputed.
4. Court judgment or enforcement databases when accessible.
5. Major complaint/media pages for recent dispute patterns.
6. Official brand site, official social accounts, and store list.

If a source is blocked or requires login, say so.

## Named Brand Qualification Check

When the user names a "快招" or franchise brand, do not rely on the brand nickname. Require the exact legal entity from the contract, payment record, invoice, official site, or招商 material, then verify:

1. Commercial franchise filing: whether the legal entity can be found in the MOFCOM commercial franchise system and whether the recorded brand/business scope matches the user's project.
2. Company status: whether the contract/payee company exists, is active, and has abnormal-operation, penalty, shareholder, or frequent-change signals.
3. Trademark/control chain: whether the brand trademark belongs to the contract company, its affiliate, or an unrelated holder; flag unclear licensing.
4. Direct-store proof: whether headquarters can provide verifiable direct-store addresses and whether the user can inspect real accounts, not just model-store photos.
5. Judicial/enforcement/complaint pattern: whether there are repeated disputes about refund, false招商 promise, forced material purchase, or site-selection failure.
6. Official-channel consistency: whether the user's contact path, official account/site, contract company, payment subject, and invoice subject point to the same group.

Output the check as "已核验 / 未查到 / 页面受限 / 需要用户补证据"; never turn a missing record into a fraud conclusion by itself.

## Risk Signals

High-risk signals:

- User says "本来想加盟A, 搜官网/抖音/百度后被推荐B". Treat this as official-channel diversion until proven otherwise.
- The "official" account/site only collected a phone number and then an招商 person pushed another brand.
- No clear headquarters company or contract/payee mismatch.
- No verifiable direct stores.
- "Two stores for one year" or franchise filing cannot be verified when the business is presented as a franchise. MOFCOM-related pages and local commerce-bureau guidance point users to the commercial franchise information system for filing checks; require the exact legal entity because fuzzy brand names are often misleading.
- Heavy front-loaded fees and mandatory high-priced equipment/materials.
- Site selection is done by招商人员 whose incentive is closing the sale.
- Promised回本周期, guaranteed revenue, or "总部兜底" without enforceable terms.
- User is pressured to pay before seeing real店账.
- Contract says fees are nonrefundable before services are delivered.
- Brand name resembles a famous brand but official relationship is unclear.
- Headquarters disappears, changes company, or asks user to pay a different entity.

## Dialogue-Derived Triage

From reviewed cases 58 and 191:

- Before payment: first cut the sales funnel. Tell the user not to keep chatting with project sellers, not to pay a deposit "just to hold a spot", and to verify official brand channels independently.
- After payment/opening: reconstruct the contact path, payment path, contract subject, promised services, direct-store proof, site-selection record, and actual service delivery.
- If the user cannot verify the real official brand site/account, say the safe conclusion is "you have not reached the brand yet"; do not reason from the招商 story.
- For a vulnerable user with family/debt pressure, the strongest advice may be to stop watching加盟项目 ads and avoid sharing contact details.
- If a company asks a losing store to buy more materials to receive a subsidy, treat it as another sales event, not rescue.

## Already Paid Or Opened

Use this sequence before telling the user to sue:

1. Stop adding money and stop buying more materials.
2. Preserve evidence: contract, payment records, invoice/receipt subject, chat logs, call recordings if lawful, ads, promises, site-selection files, delivery list, equipment/material photos, and store state.
3. Send written termination/解除 notice to the contract company and keep delivery proof.
4. Negotiate refund/return after notice.
5. If negotiation fails, file complaints with relevant commerce/market-regulation channels using the exact company name and evidence.
6. Consider litigation after evidence is organized; explain that recovery is uncertain and legal advice is needed.

## Economic Dispute Handling

For refund, termination, compensation, or headquarters-performance disputes, separate the problem into three ledgers before advising:

1. Operating ledger: current revenue, gross margin, rent, labor, platform fees, monthly loss, remaining cash, and whether the store should keep operating during the dispute.
2. Asset/material ledger: equipment, decoration, unused materials, deposits, training, software, and services that were paid for, delivered, usable, returnable, or overpriced.
3. Claim/evidence ledger: contract clauses, payment records, invoices,招商 ads, chats, call notes, promised revenue/回本周期, site-selection files, direct-store proof, delivery lists, and written notices.

Default advice pattern:

1. Stop the bleeding first: do not pay new deposits, do not buy extra materials to "qualify for subsidy", and do not expand the loss while waiting for headquarters.
2. Freeze evidence before conflict escalates: export chats, save ads/pages, photograph equipment/materials/store state, and keep express or email proof for written notices.
3. Use written communication: request termination, refund, return, or service performance from the contract subject, with a clear deadline and attachment list.
4. Negotiate with numbers: state paid amount, delivered value, undelivered services, current loss, and the specific refund/return request.
5. Escalate by channel only after evidence is organized: local commerce authority for franchise filing/performance issues, market regulation for advertising/consumer/business-practice issues, platform complaints where the招商 lead came from, and lawyer/court route for contract recovery.
6. Keep legal boundaries clear: give practical evidence and negotiation steps, but do not promise recovery, calculate damages as a court-ready conclusion, or say "诈骗" unless a competent authority or reliable source supports it.

## Output Pattern

When browsing finds facts:

```text
先说结论：这个品牌现在至少有 X 个风险信号，别继续交钱。

我查到的公开信息：
1. ...
2. ...

你现在要做：
1. 停止付款。
2. 保存合同、聊天、转账、招商承诺、宣传页、选址记录。
3. 对照合同看服务是否交付。
4. 带材料找律师/市场监管/商务主管部门咨询。
```

When facts cannot be verified:

```text
我现在不能直接说它有问题，因为关键公开信息没查到/页面受限。但按勇哥的逻辑，查不到直营店、查不到备案、查不清合同主体，就先别交钱。
```

## Important Boundary

Do not call a brand a scam solely from the user's story. Use "风险信号", "需要核验", "先别继续付款", and cite sources.
