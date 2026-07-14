#!/bin/zsh
# 半导体知识库 · 一键推送（在你本机运行；凭据走 macOS 钥匙串，Claude 不经手）
# 首次使用前先按 PUSH-SETUP.md 完成一次性设置。

cd "$(dirname "$0")" || exit 1

if [ ! -d .git ]; then
  echo "⚠️  本目录还不是 git 仓库——请先按 PUSH-SETUP.md 完成一次性设置。"
  printf "按回车退出..."; read -r REPLY; exit 1
fi

echo "== 本地改动 =="
git status -s

if [ -z "$(git status --porcelain)" ]; then
  echo "✅ 没有改动，无需推送。"
  printf "按回车退出..."; read -r REPLY; exit 0
fi

DEFMSG="update $(date '+%Y-%m-%d %H:%M')"
printf "提交说明（直接回车＝%s）：" "$DEFMSG"
read -r MSG
[ -z "$MSG" ] && MSG="$DEFMSG"

git add -A
git commit -m "$MSG"

if git push origin main; then
  echo ""
  echo "✅ 已推送。GitHub Pages 约 1–2 分钟后生效："
  echo "   https://jxnchj.github.io/semiconductor-lab/"
else
  echo ""
  echo "❌ 推送失败——看上方报错。常见原因：首次未输凭据（用户名 jxnchj、密码贴 fine-grained token）、token 过期、网络。"
fi
printf "按回车关闭..."; read -r REPLY
