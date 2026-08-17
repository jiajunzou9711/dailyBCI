#!/usr/bin/env python3
"""
merge_data.py — DailyBCI 双平台看板数据合并器（幂等 upsert）。

把「当次抓取」得到的 JSON 片段合并进 dashboard/data.js，写回后保持
`window.DASHBOARD_DATA = {...}` 结构不变。

用法:
    python3 dashboard/merge_data.py --input scrape.json [--output dashboard/data.js]

    scrape.json 结构（与 data.js 内的 posts/accounts 同构，只含本次新增部分）:
    {
      "generated_at": "2026-08-14",
      "accounts": [ { "date": "2026-08-14", "xhs_followers": 390, ... } ],
      "posts": [
        { "slug": "2026-08-13-retinal-closed-loop", "publish_date": "2026-08-13",
          "title_xhs": "...", "title_wx": "...",
          "metrics": [ { "date": "2026-08-14", "xhs": {...}, "wx": {...} } ] }
      ],
      "review": { "good": [...], "bad": [...], "next": [...] }   // 可选，为空则保留原值
    }

合并规则:
  - posts 以 slug 为键;同 slug 的 metrics 以 (slug, date) 为键去重,相同日期覆盖为新值。
  - accounts 以 (date) 为键去重,相同日期覆盖。
  - 缺失字段以 None 表示,绝不用 0 顶替。
  - review 仅在输入显式给出非空 dict 时更新;否则保留原值。
"""

import argparse
import json
import re
import sys

DEFAULT_OUTPUT = "dashboard/data.js"
PREFIX = "window.DASHBOARD_DATA = "
SUFFIX = ";"


def load_current(path: str):
    """从 data.js 读出现有 window.DASHBOARD_DATA 对象。"""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    start = text.find(PREFIX)
    if start < 0:
        raise ValueError(f"{path} 中找不到 {PREFIX!r}")
    body = text[start + len(PREFIX):]
    end = body.rfind(SUFFIX)
    if end >= 0:
        body = body[:end]
    return json.loads(body)


HEADER = (
    "// DailyBCI 双平台数据看板 · 持久化数据文件（严格 JSON，同时是合法 JS）\n"
    "// 由 dashboard/merge_data.py 生成与更新；手工编辑时请保持键全部双引号、无尾逗号。\n"
    "// 口径纪律：缺失/未报告一律为 null，绝不填 0；百分比以「百分数数值」存储（如 15.5 表示 15.5%）。\n"
)


def dump(data) -> str:
    return HEADER + PREFIX + json.dumps(data, ensure_ascii=False, indent=2) + SUFFIX + "\n"


def merge(current: dict, incoming: dict) -> dict:
    out = {
        "meta": dict(current.get("meta", {})),
        "accounts": list(current.get("accounts", [])),
        "posts": list(current.get("posts", [])),
    }
    if "generated_at" in incoming and incoming["generated_at"]:
        out["meta"]["generated_at"] = incoming["generated_at"]

    # accounts: 按 date 去重覆盖
    acc_by_date = {a.get("date"): a for a in out["accounts"]}
    for a in incoming.get("accounts", []) or []:
        if a.get("date"):
            acc_by_date[a["date"]] = a
    out["accounts"] = sorted(acc_by_date.values(), key=lambda x: x.get("date", ""))

    # posts: 按 slug 去重;metrics 按 (slug, date) 去重覆盖
    post_by_slug = {p.get("slug"): p for p in out["posts"]}
    for ip in incoming.get("posts", []) or []:
        slug = ip.get("slug")
        if not slug:
            continue
        if slug not in post_by_slug:
            post_by_slug[slug] = {
                "slug": slug,
                "publish_date": ip.get("publish_date"),
                "title_xhs": ip.get("title_xhs"),
                "title_wx": ip.get("title_wx"),
                "metrics": [],
            }
        p = post_by_slug[slug]
        if ip.get("publish_date"):
            p["publish_date"] = ip["publish_date"]
        if ip.get("title_xhs"):
            p["title_xhs"] = ip["title_xhs"]
        if ip.get("title_wx"):
            p["title_wx"] = ip["title_wx"]
        metric_by_date = {m.get("date"): m for m in p.get("metrics", [])}
        for m in ip.get("metrics", []) or []:
            if m.get("date"):
                metric_by_date[m["date"]] = m
        p["metrics"] = sorted(metric_by_date.values(), key=lambda x: x.get("date", ""))
    out["posts"] = sorted(post_by_slug.values(), key=lambda x: x.get("publish_date", ""), reverse=True)

    # review: 仅当显式给出非空 dict 时更新
    review = incoming.get("review")
    if isinstance(review, dict) and any(review.values()):
        out["meta"]["review"] = review

    return out


def main():
    parser = argparse.ArgumentParser(description="合并每日抓取数据到 data.js")
    parser.add_argument("--input", required=True, help="当次抓取的 JSON 文件路径")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="目标 data.js 路径")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        incoming = json.load(f)

    current = load_current(args.output)
    merged = merge(current, incoming)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(dump(merged))

    print(f"合并完成: posts={len(merged['posts'])} 篇, accounts={len(merged['accounts'])} 条, "
          f"generated_at={merged['meta']['generated_at']}")


if __name__ == "__main__":
    main()
