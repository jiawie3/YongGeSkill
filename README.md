# 勇哥餐饮问诊 Skill

一个把“勇哥餐饮”公开视频里的餐饮避坑、算账、选址、加盟尽调、止损决策方法，蒸馏成可复用 Codex Skill 的项目。

如果你见过那种连麦场景：

- “我店开了 3 个月，每月亏 1.5 万，怎么救？”
- “总部说半年回本，让我先交 5 万定金，能不能加盟？”
- “我拍了店门口和高德截图，这个位置能不能做汉堡炸鸡？”
- “转让费 8 万，老板说一天卖 3000，能不能接？”

这个 Skill 就是为这些问题做的。它不会上来讲鸡汤，也不会只模仿口气。它会像一个餐饮问诊系统一样，先追问关键数字，再算保本线、现金流、毛利、租金、人工、点位、加盟主体和合同风险，最后给出直接建议：该救、该转、该关、该别签，还是先查证。

## 这个 Skill 有什么特别

### 1. 不是标题党知识库，而是 504 条公开视频案例蒸馏

本项目围绕公开 Bilibili 视频季资料构建知识库：

- 覆盖 504 条公开案例。
- 本地处理过约 166.9 小时公开视频内容。
- 每条案例都整理成 reviewed case note。
- 知识库不是只看标题，而是把问诊顺序、用户事实、计算逻辑、诊断方式、建议模式和可复用经验拆出来。

GitHub 发布包只保留轻量运行知识库：`corpus/reviewed-case-notes/`。原始音频、原始 ASR transcript、机器初稿和运行日志不上传。

### 2. 真正按餐饮经营问题工作

它重点处理这些场景：

- 亏损门店：月亏、日亏、流水低、现金快烧完。
- 开店前判断：品类、租金、投入、负债、最坏情况。
- 加盟/快招品牌：品牌主体、合同主体、收款主体、特许经营备案、直营店、商标、投诉和纠纷。
- 选址分析：街边、商场、学校、社区、办公、景区、夜市、外卖店。
- 图片/地图问诊：店门口照片、360 度周边照片、高德/百度地图截图。
- 接盘转让：转让费拆分、后台流水、房东、证照、油烟消防、平台账号。
- 合伙/亲戚/夫妻店：出资、工资、分红、亏损上限、经营权和退出机制。
- 扩店：第一家店是不是系统赚钱，还是老板亲力亲为。

### 3. 先算账，再下结论

内置 `scripts/restaurant_break_even.py`，用于快速计算：

- 月固定成本。
- 贡献毛利率。
- 月保本流水。
- 日保本流水。
- 当前利润/亏损。
- 现金还能撑多久。

它的基本逻辑很朴素：餐饮不是凭感觉救的。租金、人工、日流水、毛利率、现金流这几个数没出来，就不能乱给建议。

### 4. 能检索 504 条案例先例

内置 `scripts/search_reviewed_cases.py`，可以按用户情况检索相似案例：

```bash
python scripts/search_reviewed_cases.py "汉堡 加盟 月亏 房租 毛利"
python scripts/search_reviewed_cases.py "接盘 转让费 学校 合伙 房东 证照"
python scripts/search_reviewed_cases.py "奶茶 快招 总部 退款 备案"
```

Skill 使用时会优先从 reviewed case notes 里找相近案例，再结合当前用户给出的数据进行判断。

### 5. 不是娱乐模仿，而是可执行工作流

这个项目不追求“像不像勇哥说话”的表演感，而是蒸馏公开视频里反复出现的解决问题方法：

1. 先分类：开店、亏损、加盟、选址、接盘、纠纷、扩店。
2. 再追问：租金、人工、流水、毛利、投入、负债、点位、合同。
3. 算保本线：看这个模型有没有活路。
4. 找致命约束：是点位、成本、毛利、加盟、能力、合伙，还是沉没成本。
5. 给动作：7 天/14 天/30 天测试，转让，关停，暂停签约，查资质，整理证据。

## 安装方法

把仓库 clone 到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:jiawie3/YongGeSkill.git ~/.codex/skills/yongge-catering-skill
```

如果不用 SSH，也可以用 HTTPS：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jiawie3/YongGeSkill.git ~/.codex/skills/yongge-catering-skill
```

安装后，新开 Codex 会话即可使用：

```text
使用 $yongge-catering-skill 帮我分析：我店开了3个月，每月亏1.5万，怎么救？
```

## 快速使用示例

### 示例 1：亏损门店

```text
使用 $yongge-catering-skill
三线城市社区底商，汉堡炸鸡加盟，开业3个月。总投28万，剩现金3万，负债12万。
月租1.2万，2个员工工资共1.4万，水电3000，其他固定2000。
日均流水1200，毛利55%，每月亏1.3万，堂食为主。这个店怎么救？
```

Skill 会做的事：

- 计算月固定成本、日保本流水、当前亏损、现金 runway。
- 判断是运营问题还是结构问题。
- 给 7/14/30 天止损测试或直接转让/关停条件。

### 示例 2：加盟品牌风险

```text
使用 $yongge-catering-skill
我想加盟某某奶茶，总部说半年回本，现在让我先交5万定金。能不能签？
```

Skill 会先要求你补：

- 品牌全称。
- 总部公司全称。
- 合同甲方。
- 收款主体。
- 加盟费、设备费、物料费。
- 直营店地址。
- 总部承诺截图或聊天记录。

如果涉及具体品牌或公司，Skill 会要求联网查公开信息来源，例如特许经营备案、企业状态、商标、投诉/裁判/执行记录等。

### 示例 3：地图截图/店铺照片

```text
使用 $yongge-catering-skill
我上传了店门口照片和高德地图截图，这个位置能不能做炸鸡汉堡？
```

Skill 会先看图里能确认什么：

- 门头是否 3 秒内看懂。
- 左右邻店、对面、道路、停车、外摆。
- 顾客是否自然经过门口。
- 地图上道路、POI、竞品、学校/社区/商场位置。
- 位置可信度是高、中、低。

然后再让你补租金、面积、预计流水、毛利、午晚高峰 30 分钟观察人数。

### 示例 4：接盘转让

```text
使用 $yongge-catering-skill
我和表哥想接一个学校旁边的炸串店，转让费8万，房租9000一个月。
老板说一天能卖3000，但只给我看了几张收款截图。我们还没签，只交了2000定金。
```

Skill 会按接盘逻辑拆：

- 8 万转让费里剩余房租、押金、设备、物料、装修、真实客流分别值多少。
- 有没有 6-12 个月完整收银后台、支付流水、外卖后台、进货单和水电账。
- 房东是否同意重签，证照、油烟、消防、燃气/电量能不能过。
- 你和表哥谁守店、谁管钱、工资怎么算、亏损上限是多少、退出怎么退。

如果现在只交了 2000 定金，它会优先把你留在“小亏止损窗口”，而不是鼓励你继续砸大钱。

## 项目是怎么制作的

制作流程大致如下：

1. 收集公开视频索引  
   从公开 Bilibili 视频季元数据中提取 504 条案例标题、BV 号、链接和基础信息。

2. 批量获取可分析内容  
   本地运行脚本获取公开视频音频并做 ASR 转写，形成可审计的本地 transcript。

3. 生成机器初稿案例笔记  
   按统一结构抽取每条案例的用户事实、问诊顺序、计算逻辑、诊断和建议。

4. 人工精修 reviewed case notes  
   对 504 条机器初稿进行人工精修，输出到 `corpus/reviewed-case-notes/`。

5. 提炼成 Skill 工作流  
   把重复出现的方法沉淀到 `references/`：

   - `diagnostic-protocol.md`：总问诊流程。
   - `decision-models.md`：保本线、止损、修复、扩店判断。
   - `franchise-due-diligence.md`：加盟/快招品牌尽调。
   - `visual-site-analysis.md`：照片和地图截图选址分析。
   - `pre-signing-risk-checks.md`：租赁、转让费、证照、合伙风险。
   - `usage-examples.md`：典型输入和期望行为。

6. 增加工具脚本  
   用脚本保证检索和算账稳定，而不是每次靠模型临时发挥。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── corpus/
│   └── reviewed-case-notes/
├── references/
│   ├── diagnostic-protocol.md
│   ├── decision-models.md
│   ├── franchise-due-diligence.md
│   ├── visual-site-analysis.md
│   ├── pre-signing-risk-checks.md
│   ├── dialogue-derived-cases.md
│   ├── case-patterns.md
│   ├── usage-examples.md
│   └── source-map.md
└── scripts/
    ├── restaurant_break_even.py
    ├── search_reviewed_cases.py
    ├── corpus_status.py
    ├── run_review_corpus.py
    └── bilibili_corpus_pipeline.py
```

## 发布包包含什么

包含：

- Skill 入口：`SKILL.md`
- Codex UI 元数据：`agents/openai.yaml`
- 运行知识库：`references/`
- 504 条 reviewed case notes：`corpus/reviewed-case-notes/`
- 算账、检索和维护脚本：`scripts/`

不包含：

- 原始音频。
- 原始 ASR transcript JSON。
- 机器初稿 case notes。
- 运行日志、PID、review prompt 缓存。

这样做是为了让仓库保持轻量，同时保留真正用于 Skill 运行的精修知识层。

## 常用脚本

检查 Skill 是否有效：

```bash
python /path/to/quick_validate.py .
```

检索相似案例：

```bash
python scripts/search_reviewed_cases.py "汉堡 加盟 月亏 房租 毛利"
```

计算保本线：

```bash
python scripts/restaurant_break_even.py \
  --daily-sales 1200 \
  --rent 12000 \
  --labor 14000 \
  --utilities 3000 \
  --other-fixed 2000 \
  --gross-margin 55 \
  --cash 30000
```

示例输出：

```text
餐饮保本线测算
- 月固定成本：31,000
- 贡献毛利率：55.0%
- 月保本流水：56,364
- 日保本流水：1,879
- 当前月流水：36,000
- 预估月利润：-11,200
- 距离日保本差额：679
- 现金还能撑：2.7 个月
```

## 适合谁用

- 想开餐饮店，但不知道怎么算账的人。
- 已经开店亏钱，想判断能不能救的人。
- 想加盟某个品牌，担心快招/总部/合同风险的人。
- 准备接盘转让店，怕被流水截图和学校/商场概念带偏的人。
- 想把人物公开视频知识蒸馏成 Skill 的开发者。

## 重要边界

- 这不是勇哥本人，也不是官方账号。
- 本项目基于公开内容做方法蒸馏，不冒充、不中伤、不编造原话。
- 经营建议不能保证赚钱。
- 加盟纠纷建议不能替代正式法律意见。
- 对具体品牌、公司、备案、诉讼、投诉、地图位置等当前信息，使用时应联网核验并引用来源。
- 公开来源可能有缺失、下架、登录限制或验证码限制，查不到不等于事实不存在。

## 一句话总结

这个 Skill 的目标很简单：把“别凭感觉开店，先把账算清楚”的餐饮避坑方法做成可复用工具。能救就给测试路径，不能救就帮你早点止损；能签就先查清楚，查不清就别急着交钱。
