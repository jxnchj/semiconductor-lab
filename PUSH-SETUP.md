# 一次性设置：本地 git 推送通道（约 5 分钟）

> **背景（2026-07-14 定稿）**：Cowork 沙箱连 GitHub 一律被代理 403，且安全规则不允许 Claude 经手 token——所以推送改到**你本机**：一次性把项目文件夹接上仓库历史，以后每次发布＝**双击 `push.command`**。凭据存 macOS 钥匙串，只输一次。Claude 只改文件、不碰 `.git`（铁律不变）。

## 一次性设置

**第 1 步**：打开「终端 Terminal」，逐行粘贴执行：

```bash
cd ~/Claude/Projects/Semiconductor-learning
git init -b main
git remote add origin https://github.com/jxnchj/semiconductor-lab.git
git fetch origin
git reset origin/main
chmod +x push.command
```

（`git reset origin/main` 只是把远程提交历史"接上"，**不改动你本地任何文件**；之后 `git status` 里显示的就是待推送的本地改动。）

**第 2 步**：在访达里双击 `push.command`（首次若被系统拦：右键 → 打开 → 打开）。

**第 3 步**：首次推送会在终端里要凭据：
- Username：`jxnchj`
- Password：贴一枚 **fine-grained token**（GitHub → Settings → Developer settings → Fine-grained tokens → Generate：Repository access 只选 `semiconductor-lab`，权限勾 **Contents: Read and write** 即可——Pages 部署是推送后自动触发的；有效期建议 1 年）

钥匙串会记住凭据，**以后双击即推、不再输入**。

## 以后每次发布

Claude 改完文件说"已就绪" → 你双击 `push.command` → 回车（或输一句提交说明）→ 完成。约 5 秒，Pages 1–2 分钟后生效。

## 给任意 session 的发布提示词（复制即用）

> 前提：该会话已挂载本项目文件夹（~/Claude/Projects/Semiconductor-learning）。

```
本项目发布走「本机一键脚本」通道（详见项目根目录 PUSH-SETUP.md、PROJECT-HANDOFF §8），按此流程处理：
1. 你只改文件、不碰 git：绝不在挂载目录运行任何 git 命令（包括 git status），绝不 rm（废弃物 mv 进 _to_delete/）。
2. 若本次改过正本 HTML（principles/index.html 或 atlas.html）而尚未做校验（标签配平/JS/重名 id）+ 真机渲染逐帧核对（铁律④，Chrome 注入法），先补做再谈发布。
3. 就绪后向我报告"已就绪"，并列出本次改动的文件清单。
4. 我在本机双击 push.command 推送。提醒我：脚本会先列改动清单——须与你报告的一致；若出现意外的 D（删除）条目，先停下来问你查明再回车（历史教训：.nojekyll 差点被误删）。
5. 我说"推完了"后，你用浏览器到 https://jxnchj.github.io/semiconductor-lab/ 抽验本次改动（Pages 约 1–2 分钟生效），确认后把发布结果（commit 号）回写进 PROJECT-HANDOFF 基线与项目记忆。
6. 本机脚本不可用时的备用通道：Chrome file_upload 全自动，流程见 TRACK2-HANDOFF §8。
```

## 复用到其他项目

方案通用（脚本用 `$(dirname $0)` 自适应目录）。每个新项目只需三件一次性事：
1. GitHub 上先有仓库（新建或已有均可）；
2. 把新仓库加进 fine-grained token 的 Repository access（token 按仓库授权；钥匙串里 github.com 凭据全仓库共用，无需重输）；
3. 在新项目文件夹跑一遍 6 行接管命令（全新空仓库可跳过 fetch/reset；默认分支非 main 则替换分支名）。

在新项目的 Claude 会话里粘贴"通用建立提示词"即可让它把脚本/.gitignore/设置文档一次建好（提示词全文见本次会话记录 2026-07-14，或直接把本文件和 push.command 拷给它照抄，要求：Claude 不碰 git、只建文件、做隐私扫描、提醒 token 授权与 D 条目风险）。

## 备注

- `.gitignore` 已排除：`.DS_Store`、`_to_delete/`（本地废弃物）、`knowledge-delivery-log.md`（本地投递日志）。想让它们进仓库就删掉对应行。
- 脚本报错时：终端里 `cd ~/Claude/Projects/Semiconductor-learning && git status` 看原因。
- 备用通道：Chrome file_upload 全自动上传（见 TRACK2-HANDOFF §8），本地脚本不可用时 Claude 可代跑。
