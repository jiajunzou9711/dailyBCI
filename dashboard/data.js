// DailyBCI 双平台数据看板 · 持久化数据文件（严格 JSON，同时是合法 JS）
// 由 dashboard/merge_data.py 生成与更新；手工编辑时请保持键全部双引号、无尾逗号。
// 口径纪律：缺失/未报告一律为 null，绝不填 0；百分比以「百分数数值」存储（如 15.5 表示 15.5%）。
window.DASHBOARD_DATA = {
  "meta": {
    "generated_at": "2026-08-06",
    "notes": "首份快照转写自 output/2026-08-06-weekly-dashboard.html（6 篇，采集日 2026-08-06）。小红书观看<100 无笔记诊断；公众号 07-30 未群发、07-31/08-01 平台未报告完读率与时长。",
    "review": {
      "good": [
        "封面点击率稳定在 10-17%，6 篇里 5 篇超同类中位。",
        "内容丰富度全超 90%，收藏率高，「值得存」立住了。",
        "存在可复制的高流量模板：08-01 神经数据分析 曝光 2,593 / 涨粉 8 / 互动率 16.2%。"
      ],
      "bad": [
        "涨粉转化偏低，看的人多、关注的人少。",
        "观看时长方差大（4.6s~49s），开头 3 秒留不住人。",
        "抽象方法论选题流量塌方：08-05 曝光 289，其余 5 篇都在 1,000+。"
      ],
      "next": [
        "标题模板固定为「具体现象/结果 + 数字」：小红书曝光 ≥ 1,500，公众号打开率 ≥ 3%。",
        "首屏 3 秒给结论：小红书首图第一行放大结论，公众号导语第一句给结果。",
        "给关注一个理由：尾卡与摘要统一加「日更 BCI 日报」钩子。"
      ]
    }
  },
  "accounts": [
    {
      "date": "2026-08-06",
      "xhs_followers": 381,
      "xhs_followers_7d": 40,
      "wx_users": 1683,
      "wx_users_1d": 25
    }
  ],
  "posts": [
    {
      "slug": "2026-08-05-tus-lgn",
      "publish_date": "2026-08-05",
      "title_xhs": "实验设计三层拆解",
      "title_wx": "三层对照",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 289,
            "views": 88,
            "ctr": 10.4,
            "avg_watch_s": 14.9,
            "engage_rate": 5.7,
            "followers_gain": 0,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": null,
              "watch_pct": null,
              "engage_pct": null,
              "gain_pct": null
            },
            "reported": true
          },
          "wx": {
            "send_uv": 1675,
            "read_uv": 21,
            "open_rate": 1.3,
            "finish_rate": 85.7,
            "avg_read_s": 28,
            "share_uv": 1,
            "collect_uv": null,
            "follow_after_read": 0,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": true,
            "channel": null,
            "reported": true
          }
        }
      ]
    },
    {
      "slug": "2026-08-04-mesoscope",
      "publish_date": "2026-08-04",
      "title_xhs": "双光子活体成像",
      "title_wx": "双光子成像＋光遗传",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 1550,
            "views": 204,
            "ctr": 13.3,
            "avg_watch_s": 19.3,
            "engage_rate": 11.3,
            "followers_gain": 1,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": 37,
              "watch_pct": 66,
              "engage_pct": 75,
              "gain_pct": 7
            },
            "reported": true
          },
          "wx": {
            "send_uv": 1670,
            "read_uv": 54,
            "open_rate": 3.2,
            "finish_rate": 98.1,
            "avg_read_s": 43,
            "share_uv": 3,
            "collect_uv": null,
            "follow_after_read": 1,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": true,
            "channel": null,
            "reported": true
          }
        }
      ]
    },
    {
      "slug": "2026-08-03-generalizable-speech",
      "publish_date": "2026-08-03",
      "title_xhs": "脑机接口语言解码",
      "title_wx": "脑机接口语言解码",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 2156,
            "views": 346,
            "ctr": 15.8,
            "avg_watch_s": 49,
            "engage_rate": 9.5,
            "followers_gain": 2,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": 33,
              "watch_pct": 94,
              "engage_pct": 80,
              "gain_pct": 10
            },
            "reported": true
          },
          "wx": {
            "send_uv": 1657,
            "read_uv": 100,
            "open_rate": 6,
            "finish_rate": 94,
            "avg_read_s": 38,
            "share_uv": 9,
            "collect_uv": null,
            "follow_after_read": 1,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": true,
            "channel": null,
            "reported": true
          }
        }
      ]
    },
    {
      "slug": "2026-08-01-dlag",
      "publish_date": "2026-08-01",
      "title_xhs": "神经数据分析",
      "title_wx": "神经数据分析",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 2593,
            "views": 402,
            "ctr": 15.5,
            "avg_watch_s": 14.1,
            "engage_rate": 16.2,
            "followers_gain": 8,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": 31,
              "watch_pct": 56,
              "engage_pct": 91,
              "gain_pct": 40
            },
            "reported": true
          },
          "wx": {
            "send_uv": 1638,
            "read_uv": 186,
            "open_rate": 11.4,
            "finish_rate": null,
            "avg_read_s": null,
            "share_uv": 24,
            "collect_uv": null,
            "follow_after_read": 0,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": true,
            "channel": null,
            "reported": true
          }
        }
      ]
    },
    {
      "slug": "2026-07-31-identifiability",
      "publish_date": "2026-07-31",
      "title_xhs": "电生理数据分析",
      "title_wx": "电生理数据分析",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 1043,
            "views": 128,
            "ctr": 12,
            "avg_watch_s": 4.6,
            "engage_rate": 8.6,
            "followers_gain": 0,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": 15,
              "watch_pct": 10,
              "engage_pct": 42,
              "gain_pct": 0
            },
            "reported": true
          },
          "wx": {
            "send_uv": 1628,
            "read_uv": 51,
            "open_rate": 3.1,
            "finish_rate": null,
            "avg_read_s": null,
            "share_uv": 3,
            "collect_uv": null,
            "follow_after_read": 0,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": true,
            "channel": null,
            "reported": true
          }
        }
      ]
    },
    {
      "slug": "2026-07-30-quadbase",
      "publish_date": "2026-07-30",
      "title_xhs": "脑区之间的联系",
      "title_wx": "脑区之间的联系",
      "metrics": [
        {
          "date": "2026-08-06",
          "xhs": {
            "exposure": 2615,
            "views": 457,
            "ctr": 17,
            "avg_watch_s": 17.6,
            "engage_rate": 10.9,
            "followers_gain": 1,
            "likes": null,
            "comments": null,
            "collects": null,
            "shares": null,
            "richness_pct": null,
            "diag": {
              "ctr_pct": 41,
              "watch_pct": 64,
              "engage_pct": 86,
              "gain_pct": 7
            },
            "reported": true
          },
          "wx": {
            "send_uv": null,
            "read_uv": 189,
            "open_rate": null,
            "finish_rate": 96.3,
            "avg_read_s": 52,
            "share_uv": 20,
            "collect_uv": null,
            "follow_after_read": 10,
            "like_cnt": null,
            "comment_cnt": null,
            "zaikan_cnt": null,
            "is_group_send": false,
            "channel": null,
            "reported": true
          }
        }
      ]
    }
  ]
};
