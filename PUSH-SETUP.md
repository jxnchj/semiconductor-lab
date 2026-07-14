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

## 备注

- `.gitignore` 已排除：`.DS_Store`、`_to_delete/`（本地废弃物）、`knowledge-delivery-log.md`（本地投递日志）。想让它们进仓库就删掉对应行。
- 脚本报错时：终端里 `cd ~/Claude/Projects/Semiconductor-learning && git status` 看原因。
- 备用通道：Chrome file_upload 全自动上传（见 TRACK2-HANDOFF §8），本地脚本不可用时 Claude 可代跑。
