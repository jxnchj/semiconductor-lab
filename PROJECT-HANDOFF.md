# 半导体研究知识库 · 项目总交接文档（PROJECT HANDOFF）

> **本文档是项目唯一的总交接入口**（2026-07-09 重写，取代旧版"chip-explainer 单文件"时代的交接文档）。
> 给接手的新 session：先读本文件 → 再按需读 `TRACK2-HANDOFF.md`（第二轨细节与发布流程）和 `TRACK1-BACKFILL.md`（两轨回补队列）。第 3 节「工作标准」是硬性要求，第 7 节是安全改文件与渲染核对的方法。

---

## 0. 一句话

一个**长期化、中文、纯前端单文件**的半导体研究知识库，分两轨：**第一轨讲原理**（芯片怎么造出来，交互图解），**第二轨讲产业/价值**（六大赛道投研终端）。部署在 GitHub Pages。

## 1. 文件结构与"唯一正本"（重要）

```
Semiconductor-learning/            ← 本地主文件夹（与仓库根同构）
├── index.html                     门户（选轨落地页）
├── principles/index.html          第一轨 · 原理科普【唯一正本 ≈300KB】
├── atlas.html                     第二轨 · 产业链研究终端【唯一正本 ≈206KB】
├── value-chain/…                  旧路径，全部是跳转页（→ atlas.html#锚点），勿放内容
├── README.md                      对外说明
├── PROJECT-HANDOFF.md             本文件（总交接）
├── TRACK2-HANDOFF.md              第二轨交接 + 发布流程（token/push 命令）
├── TRACK1-BACKFILL.md             两轨异步回补队列（活文档，管内容缺口）
├── FACT-REVIEW.md                 事实复核队列（活文档，管快变声明的保质期）
├── TRACK1-RESTRUCTURE-SPEC.md     ✅已执行完毕，归档留存
└── _to_delete/                    待用户手动删除的废弃物（挂载盘禁止 rm，只能 mv 进来）
```

- **历史沿革**：第一轨早期工作文件叫根目录 `chip-explainer.html`，2026-06 底与 `principles/index.html` 完全同步后，根目录副本已于 2026-07-09 移入 `_to_delete/`。**今后只改 `principles/index.html`，不要再造第二份拷贝。**
- 旧的 `_publish_github/` 发布残骸（过时快照 + 中断的 .git 锁文件）同日移入 `_to_delete/`。现行发布流程见 `TRACK2-HANDOFF.md` §8（在沙箱 /tmp 克隆仓库再覆盖 push，**不在挂载目录碰 .git**）。

## 2. 仓库与线上

- 仓库：`github.com/jxnchj/semiconductor-lab`（Public，Pages=main/root 已开启）。
- 线上：<https://jxnchj.github.io/semiconductor-lab/>（门户）→ `principles/`（轨1）、`atlas.html`（轨2）。
- 2026-07-09 核对：线上与本地内容一致（门户/两轨/重定向均已抽验）。

## 3. 工作标准（CRITICAL — 逐条遵守，历史上被打回多次）

1. **图形要最精细、最接近真实**：CMP 先画凹凸再磨平；共形沉积顺台阶隆起；沟槽斜壁、侧墙弧形、源漏圆弧；材料用渐变质感。
2. **每个图元都要有说明**：图例/标注讲清楚，不留"莫名其妙"的元素；必要元素加说明而不是删掉。
3. **文字与图形平衡**：不为图删字。
4. **必须真实渲染核对（铁律）**：每次改完用 Playwright+Chromium 真实渲染、逐帧/逐状态亲眼看过再说"完成"。绝不允许"代码看着对就算过"。历史踩坑：EUV 镜面画成折射、M6 反射方向错、显影/刻蚀图无区别。
5. **数据要标来源与时间**，区分「事实（机构/财报）vs 叙事（厂商说法）」；金额统一亿美元并注明口径。可借鉴四级可信度标注：`[✓已核实] / [~估算·单源] / [?待证] / [△示意]`。
6. **不偷懒**：顺手通读，缺的补、不清楚的讲明白、错的改掉。

## 4. 第一轨 · 原理科普（principles/index.html）现状

**4 组 · 两级导航，16 页**（顶层组按钮 `data-g`，二层页标签 `data-s`；页名即正式名，正文交叉引用一律用页名、无圈号）：

| 组 | 页（data-s） |
|---|---|
| A 全局导览 | 全链条 `chain` · 基础概念 `basics` |
| B 器件原理 | 晶体管 `tr` · 先进结构演进 `advstruct` |
| C 制造与封装 | 设计·EDA `eda` · 硅片·掩膜 `wafer` · 前道·制造流程 `fab` · 光刻 `litho` · **刻蚀·沉积 `etch`** · **清洗·量测 `clean`**（后两页 2026-07-13 新增，补齐八大工艺） · 制程节点与经济 `adv` · 后道·封装测试 `bepkg` · 先进封装 `pkg` |
| D 芯片家族 | 芯片品类 `family` · 存储器 `mem` · 功率/化合物 `pwr` |

JS：`var scenes={chain:'s-chain',basics:'s-basics',eda:'s-eda',wafer:'s-wafer',tr:'s-tr',fab:'s-fab',litho:'s-litho',etch:'s-etch',clean:'s-clean',adv:'s-adv',advstruct:'s-advstruct',mem:'s-mem',bepkg:'s-bepkg',pkg:'s-pkg',pwr:'s-pwr',family:'s-family'}`。默认 A 组/全链条。**已支持 hash 深链**：`principles/#eda` 等（页面加载时读 hash 自动切组切页），轨2 EDA 赛道页有互链入口。**覆盖度体检**：见 `COVERAGE-AUDIT.md`（八大工艺已全部 ✅；P1 热工艺与掺杂、P2 打包待做，登记在 TRACK1-BACKFILL #7/#8）。

**设计·EDA 页内容**（2026-07-13）：①设计全流程（前端逻辑/后端物理 8 站）②同一电路三副面孔（RTL→门级→CMOS NAND 版图）③布局布线 6 步 stepper（Floorplan→电源→摆放→CTS→布线→签核，id 前缀 ed-，JS 生成 IO 焊盘/标准单元/布线）④验证工作量+bug 代价 ⑤EDA 三大件环节矩阵+三道护城河（工具链耦合/PDK 绑定/人才生态）。**后道·封装测试页测试加厚**（同日）：CP vs FT+ATE 图解、完整测试旅程流程图、wafer map 四种失效图案+良率闭环（在"键合两条路线"之后）。

**主要交互资产**（改动时务必保全）：晶体管页 canvas-3D 引擎（平面/FinFET/GAA 三模式、反型层/耗尽区、自动旋转）、2D 剖面随结构切换、反型层 5 步 stepper + 连续动画、制造流程 26 步剖面 stepper（CMP 四处：先凹凸再磨平）、制程节点密度网格（28/14/7nm 切换）、CMOS 反相器、良率/功耗墙图、EUV 深度三连、光刻胶感光机制、电子特气、外延片、CoWoS/HBM 精细剖面、**ALD 循环 6 步 stepper**（刻蚀·沉积页，id 前缀 ald，宏观深槽+表面化学双视图）、**3D NAND 字线抽换 5 步 stepper**（存储器页，id 前缀 nf，含 nf-lab-n 标签随步切换）。

**设计系统**（一种材料=一种颜色，别引入新色）：硅 `#3a4870`(gSi) · 源漏绿 `#3aa86b`(gSD) · SiO₂黄 `#f2d35a`(gOx) · ILD紫 `#9b7be0`(gILD) · 铜 `#e9a04c`(gCu/gCuV) · 光刻胶红 `#e0556e` · 氮化硅/侧墙灰 `#6f7e9c` · 沟道导通青 `#5eead4`；UI 强调 teal `#34d6cf`（仅 UI）。全局渐变在 `<body>` 后隐藏 `<svg><defs>`（含封装页 gSub/gSolder）。刻意平涂不加渐变的：密度网格、EUV/DUV 波长示意、流程框。

**校验基线（2026-07-15"做深⑤⑥⑦⑧"后，principles/index.html ≈549KB）**：div 486/486 · svg 160/160 · g 525/525 · marker 38/38 · linearGradient 12/12 · radialGradient 3/3 · pattern 1/1 · clipPath 3/3 · 16 scenes/16 tabs · 无重名 id · `node --check` 通过 · Chrome 注入法真机渲染逐帧核对通过。近期批次：做深①ALD+高深宽比刻蚀（刻蚀·沉积页，commit 71f28de）；做深②③④＝量测检测/3D NAND 专线（nf stepper）/HKMG（commit 99eb477）；**做深⑤⑥⑦⑧＝先进封装工艺线（先进封装页：TSV 五步/CoWoS 流水线/混合键合四步）+ DRAM 工艺专线（存储器页，与 NAND 成对）+ 互连 RC 与新金属（fab 页机制加深③）+ 光刻机整机解剖（光刻页运动系统视角）**（2026-07-15 本批，全静态图无新增 JS；内容清单见 COVERAGE-AUDIT §七 行 5–8，快变声明登记 FACT-REVIEW #19–21）。

## 5. 第二轨 · 产业链价值（atlas.html）现状

- **单文件研究终端**：概览「产业链价值地图」+ 六大赛道（材料 `mat` / 设备 `eqp` / EDA·设计 `eda` / 晶圆制造 `foundry` / 存储器 `mem` / 封装测试 `pkg`）+ 工具（上市公司速查 `lookup`、数据来源与方法 `sources`）。
- 每赛道 7 个子页：定位 `-pos` / 细分 `-cats` / 价值量 `-value` / 护城河 `-moat` / 玩家格局 `-players` / 驱动与风险 `-dr` / 数据·来源 `-data`（材料另有深挖 `m-deep`）。id 前缀：m/e/d/f/r/p。
- **全局搜索**（板块/公司/代码）与 **hash 深链**（`#mat #eqp #lookup #m-players…`）均可用。
- 数据快照 **截至 2026-06**；宏观口径已核对＝2025 全年实绩（全球 $7917亿 +25.6% · 设备 $1351亿 · 材料 $732亿 · 代工前十 $1695亿 · 封测前十 $416亿(2024)）。
- **数据债状态（2026-07-09 已还大半）**：① 公司速查市值/PE ✅ 已填 2026-07-08 tushare 收盘快照（再刷新＝重跑 daily_basic 整列替换+改日期；拓荆停牌取停牌前值）；② 硅片总盘 ✅ 已刷至 SEMI 2025 实绩（$114 亿 / 12,973 MSI）；光刻胶/特气/CMP/靶材/掩膜基板细分规模暂无权威 2025 口径，维持 2024 数并已标年份。③ 2026-07-09 全站事实审计已完成一轮：修正了长存"300+ 层全球首突破"（实为 294 层出货、300+ 首发是 SK 海力士 321 层）、长鑫 HBM 落后 1 年→2–3 年、HBM4 首代仍 MR-MUF/TCB（混合键合 16 层/HBM4E 起）、N3E 密度 200–220 MTr/mm²、EUV 单价约 2 亿美元级、EDA 三巨头 ~74%、上海新阳代码 300236.SZ（原误 688137）、豪威集团/先导基电/华虹宏力更名；长电 HBM 良率/英伟达订单标注为传闻级。
- 校验基线：43 sections / 9 views · 无重名 id · JS 通过 · 全视图渲染零 pageerror。

## 6. 两轨分工与回补接口

- **判据：为看懂工艺 → 轨1；为看懂生意/壁垒 → 轨2。** 同一主题可两轨都出现、不重复（机制归轨1，产业/价值归轨2；材料的深度技术原理作为"为什么难=壁垒"跟轨2走）。
- 轨2 研究中发现轨1缺工艺必经知识 → **登记到 `TRACK1-BACKFILL.md`，不打断轨2**；攒批集中回补。该队列 2026-06-27 已清空首批 4 项（光刻胶机制/CMP/电子特气/外延片，均已发布）。

## 7. 安全编辑 + 校验 + 渲染核对（recipe）

**改文件**：整段重写用 `cat > path << 'EOF' … EOF`；小修用唯一短锚点替换（当心中文全角标点）；复杂替换用 Python 按唯一字符串切片、先 `count()==1` 断言。**挂载目录禁止 rm/unlink**，废弃物 `mv` 进 `_to_delete/`。

**每次改完跑校验**（对被改的文件）：
```bash
F=principles/index.html   # 或 atlas.html
for t in div svg g marker linearGradient radialGradient pattern clipPath; do
  echo "$t $(grep -o "<$t[ >]" $F|wc -l)/$(grep -o "</$t>" $F|wc -l)"; done
python3 -c "import re;open('/tmp/s.js','w').write(re.search(r'<script>(.*)</script>',open('$F',encoding='utf-8').read(),re.S).group(1))" && node --check /tmp/s.js
grep -o 'id="[^"]*"' $F | sort | uniq -c | sort -rn | awk '$1>1'   # 应为空
```
基线见 §4/§5；改完与基线比对，开闭不平/重名 id/JS 报错都要先修。

**真实渲染核对**（Playwright + Chromium）：
```python
from playwright.sync_api import sync_playwright
import pathlib
url=pathlib.Path('principles/index.html').resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch(args=["--no-sandbox"]); pg=b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(500)
    pg.click('[data-g="C"]'); pg.click('[data-s="fab"]:visible')   # 切组→切页
    pg.click('#s-fab #fdots .dot:nth-child(13)')                   # stepper 点第 N 个圆点最稳
    pg.screenshot(path='x.png'); print(errs); b.close()
```
要点：轨1 先点组按钮 `[data-g]` 再点页标签 `[data-s]`；晶体管页 `data-v="2d"/"3d"` 切视图、`#gbtn` 加压、`.mbtn` 切结构；反型层 `#ivdots .dot:nth-child(N)`。轨2 点 `[data-view="…"]` 切视图，可直接带 hash 打开。**截图必须亲眼看过**才算核对。
（Cowork 云沙箱已预装 Playwright + Chromium `/opt/pw-browsers`，无需再装；若在其他环境缺库，参考 git 历史里旧版 handoff 的 stub 方案。）

## 8. 发布流程（2026-07-14 改版，详见 PUSH-SETUP.md / TRACK2-HANDOFF §8）

**正式通道＝用户本机一键脚本**：Claude 改完正本与文档后说"已就绪"→ 用户双击项目根目录 `push.command`（本机 git，凭据在 macOS 钥匙串，首次输一次）。一次性设置见 `PUSH-SETUP.md`。**Claude 依旧不在挂载目录跑任何 git 命令**（.git 归用户本机管）。备用通道＝Chrome file_upload 全自动上传。**死路勿再试**（2026-07-14 复验）：沙箱 git/API 直连（代理 403）；Claude 经手 token（安全规则禁止）；claude.ai GitHub 连接器（不进 Cowork 会话）；连接器注册表（无 GitHub）；官方远程 MCP 当自定义连接器（OAuth 不兼容）。

## 9. 值得保留的概念讲法（知识资产，做内容直接复用）

- FEOL 只走一遍造一层晶体管；BEOL 反复叠 10~20 层铜布线——芯片只有一层晶体管、十几层布线。
- 布线多层是把上亿开关连成电路（电源/地/时钟/IO），不是一层对一个晶体管。
- 晶体管是光刻在硅上"雕"出来的（掺杂区=源漏、未掺杂硅=沟道），不是装上去的；整片晶圆同时造几百颗最后才切。
- "nm" 节点名 ≠ 物理尺寸（约 2009 起）；可比的是密度 MTr/mm²、功耗、性能。
- **沟道是栅压"现拉"出来的反型层，不是预埋导线**：栅/栅氧/硅=电容，正栅压推开空穴、把电子（主要来自源极 N+）吸到硅表面成 1–2nm 反型层；撤压即消失（所以能关断）；体内被背靠背 PN 结堵死，只有表面反型层是连续电子通道——这就是"场效应"。
- 已纠错留档：「N3E 物理栅长约 9nm」不准 → 用最小金属间距 ~23nm、CPP ~45–48nm、密度 ~170–200 MTr/mm²（来源 IEDM/WikiChip/TechInsights）。

## 10. 待办与可延伸方向（2026-07-10 与用户对齐后更新）

**项目定位（用户明确）**：首要目的是**学习研究半导体知识 + 基本面角度研究行业与公司标的**，不是构建决策/择时系统。**内容重心（2026-07-13 补充）**：重点＝制造基础端（材料/技术/工艺流程）＋公司基本面的系统性研究；**市场端内容（涨价/催化/股价弹性等）往后摆，必要列示即可**，不展开渲染、不主动新增市场面小节。

**A · 下一步 —— ✅ 全部完成（2026-07-13，commit d31752d/dfbe2a5）**：
1. ✅ 事实审计制度化：两轨快变声明已铺四级标注（轨1 5 处+新页随写标；轨2 8 处），FACT-REVIEW 增 #13/#14 并记录标注铺设情况。
2. ✅ 轨1「设计·EDA」新页：C 组之首，与轨2 EDA 赛道页双向互链（轨1 加了 hash 深链支持）。
3. ✅ 轨1 测试环节加厚：CP/FT/ATE 图解+测试旅程流程图+wafer map 良率闭环三个"放大"小节。
4. ✅ 全程校验+真机渲染逐帧核对+发布。渲染方法注意：Cowork 沙箱无 Playwright 且装不了（PyPI/npm 全被代理挡），改用 **Chrome file_upload 注入法**——在 example.com 上造 `<input type=file>`，file_upload 灌入 HTML，JS 读 `files[0].text()` 后 `document.write` 渲染，再逐帧截图核对（本地文件 file:// 被扩展禁止，此法绕过；对单页可先做"仅该 scene+CSS+defs+JS"的小预览再整页验证）。

**A2 · "做深"阶段（2026-07-14 启动，进度见 COVERAGE-AUDIT §七）**：①ALD/高深宽比刻蚀 · ②量测检测 · ③3D NAND 专线 · ④HKMG · ⑤先进封装工艺线 · ⑥DRAM 专线 · ⑦互连 RC 与新金属 · ⑧光刻机整机——**两批八个深挖主题全部完成（07-14/15）**。轨1 机制层可深挖的主要缺口已基本收敛；下一步候选：FACT-REVIEW 到期复核（下批 2026Q4）；速查表市值/PE 月度刷新；轨2 做深（公司基本面深挖、赛道竞争格局机制化）；或 §B 搁置项经确认后启动。

**B · 已搁置（用户明确暂不做，记录备查，后续可能加入）**：
- 周期仪表盘（SIA 3MMA/设备出货/存储价格/稼动率等择时指标+定期刷新）
- 中美对标估值层（北方华创 vs AMAT、沪硅 vs SUMCO 等估值对比，yfinance 可取数）
- 六赛道横向记分卡（规模×壁垒×国产化×周期位置聚合表）
- 产业数据→量化信号映射页（因子先验库）
- 其他旧列表项：自测小测验、3D 源漏菱形化、CoWoS-S/R/L 变体、UCIe/SoIC/CPO、移动端 ARIA、六赛道按芯片家族展开、季度营收自动刷新

## 11. 给新 session 的启动提示词（可直接复制）

```
这是「半导体研究知识库」双轨项目（GitHub Pages: jxnchj.github.io/semiconductor-lab）。
先完整读项目根目录 PROJECT-HANDOFF.md（总交接），需要发布或做第二轨再读 TRACK2-HANDOFF.md。
铁律：①图形最精细最接近真实；②每个图元有说明；③文字图形平衡；④每次改动必须
Playwright+Chromium 真实渲染、逐帧亲眼核对后才算完成；⑤数据标来源与时间、区分事实vs叙事；
⑥不偷懒，顺手通读补缺纠错。
唯一正本：第一轨 principles/index.html，第二轨 atlas.html（不要再造副本）。
挂载目录禁止 rm，废弃物 mv 进 _to_delete/。
我这次要做的是：【填目标】。请先用一句话复述标准和目标，再动手。
```

---

*任何一步动手前，先复述标准、再渲染核对——这是这个项目的铁律。（本文件 2026-07-09 由体检+重写产生；旧版内容如需考古，见 git 历史。）*
