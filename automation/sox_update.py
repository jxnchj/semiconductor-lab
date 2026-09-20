"""SOX 回撤指标每日自动更新。

注意：本文件是项目内的参考副本（会推送到公开仓库，**严禁写本机绝对路径**）。
实际由定时任务执行的副本位于本机 daimon blueprint/automations/automation_6a52964f-…/assets/automation.py（不入库），
那里保留本机绝对路径属正常；两份副本除路径解析行外内容保持一致。

抓取费城半导体指数 (^SOX) 最新收盘，计算相对历史高点 (ATH) 的回撤，
重写知识库 atlas.html 中 AUTO:SOX-STAT / AUTO:SOX-ROW 标记之间的内容。
失败/数据过期时不改文件，直接抛错让本次运行失败。
"""

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# 路径解析：优先环境变量 SEMILAB_ATLAS；否则按仓库结构推导（本脚本位于 <repo>/automation/）
_repo_default = Path(__file__).resolve().parents[1] / "atlas.html"
ATLAS = Path(os.environ.get("SEMILAB_ATLAS", _repo_default))
KNOWN_ATH = 14634.72          # 2026-06-22 收盘历史高点（C5 来源 6）
KNOWN_ATH_DATE = "2026-06-22"
STALE_DAYS = 7                # 最新交易日距今超过 7 天视为数据过期


def fetch_sox():
    import yfinance as yf
    hist = yf.Ticker("^SOX").history(period="5y", auto_adjust=False)
    if hist is None or hist.empty:
        raise RuntimeError("yfinance 返回空数据：^SOX 抓取失败")
    closes = hist["Close"].dropna()
    last_date = closes.index[-1].date()
    last_close = float(closes.iloc[-1])
    ath = max(KNOWN_ATH, float(closes.max()))
    return last_close, last_date, ath


def fmt_pct(dd):
    """回撤百分比，保留整数；接近 0 时给一位小数。"""
    if abs(dd) < 1:
        return f"{dd:.1f}"
    return f"{dd:.0f}"


def build_blocks(close, d, ath):
    dd = (close / ath - 1.0) * 100.0
    alert = dd <= -30.0
    ds = d.strftime("%Y-%m-%d")
    dshort = d.strftime("%m-%d")
    pct = fmt_pct(dd)

    if dd > -0.05:
        v = "新高"
        state = f"{ds} · 刷新历史高点"
        row = f"{close:,.0f}（{dshort}）· <b>创历史新高</b>（前高 {ath:,.0f}）<sup class=\"s\">6</sup>"
    else:
        v = f"−{fmt_pct(-dd)}<small>%</small>" if dd < 0 else f"{pct}<small>%</small>"
        if alert:
            state = f"{ds} · ⚠ 进入历史熊市带"
        elif dd > -5:
            state = f"{ds} · 接近前高"
        else:
            state = f"{ds} · 回撤进行中"
        row = (f"{close:,.0f}（{dshort}）· 距 ATH <b>{'−' if dd < 0 else ''}{fmt_pct(abs(dd))}%</b>"
               f"<sup class=\"s\">6</sup>")

    stat = (f'<div class="v">{v}</div><div class="l">SOX 当前距 ATH</div>'
            f'<div class="d">{state}</div>')
    return stat, row, dd, alert


def replace_block(text, name, new_inner):
    pat = re.compile(
        r"(<!-- AUTO:" + name + r":START -->).*?(<!-- AUTO:" + name + r":END -->)",
        re.S,
    )
    new_text, n = pat.subn(lambda m: m.group(1) + new_inner + m.group(2), text)
    if n != 1:
        raise RuntimeError(f"标记 AUTO:{name} 在 atlas.html 中匹配到 {n} 处（应为 1），放弃写入")
    return new_text


def run(ctx):
    close, d, ath = fetch_sox()
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    stale = (datetime.now().date() - d) > timedelta(days=STALE_DAYS)
    if stale:
        raise RuntimeError(f"数据过期：最新交易日 {d} 距今超过 {STALE_DAYS} 天，未改动文件")

    stat, row, dd, alert = build_blocks(close, d, ath)

    text = ATLAS.read_text(encoding="utf-8")
    text = replace_block(text, "SOX-STAT", stat)
    text = replace_block(text, "SOX-ROW", row)
    ATLAS.write_text(text, encoding="utf-8")

    summary = (f"SOX {d} 收 {close:,.2f}，距 ATH {ath:,.2f} 回撤 {dd:.1f}%"
               f"{'，⚠ 已进入历史熊市带（>30%）' if alert else ''}；atlas.html 两处读数已更新")
    return {
        "artifact": {
            "summary": summary,
            "close": round(close, 2),
            "asOf": d.isoformat(),
            "ath": round(ath, 2),
            "drawdownPct": round(dd, 2),
            "alert": alert,
            "stale": False,
            "updated": True,
            "fetchedAt": fetched_at,
        }
    }
