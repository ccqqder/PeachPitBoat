網站技術規格書 (SPEC.md)
專案名稱: 核舟 (Project Ark) 技術堆疊: Hugo + GitHub Pages + Giscus 版本: 1.0.0 日期: 2026-02-09

1. 系統架構 (System Architecture)
1.1 核心組件
生成引擎 (Generator): Hugo (Extended Version)

原因： Go 語言編寫，單一執行檔，編譯速度極快 (ms 等級)，無 npm/node_modules 相依性地獄 (Dependency Hell)。

託管 (Hosting): GitHub Pages

原因： 免費、HTTPS、整合 Git workflow。

評論系統 (Comments): Giscus

原因： 利用 GitHub Discussions API 儲存留言。無資料庫、無追蹤腳本、載入輕量。

持續整合 (CI/CD): GitHub Actions

原因： Push code 後自動觸發 Hugo Build 並部署到 gh-pages 分支。

1.2 目錄結構 (Directory Structure)
這是標準 Hugo 專案結構，我們將特別加入 static/api 來存放 App 矩陣資料。

Plaintext
my-website/
├── archetypes/        # 內容模板 (預設 Front Matter)
├── content/           # 您的 Markdown 文章
│   ├── posts/         # 部落格文章 (實作/反思)
│   ├── apps/          # 產品頁面 (每個 App 一頁)
│   └── about.md       # 關於我
├── static/            # 靜態資源 (圖片、CNAME、JSON)
│   ├── images/
│   └── api/
│       └── apps.json  # [關鍵] 供 iOS App 抓取的交叉推廣資料
├── themes/            # 下載的主題 (推薦 PaperMod)
├── layouts/           # 自定義 HTML 佈局 (若需修改主題)
├── config.yml         # 網站全域設定 (或 hugo.toml)
└── .github/
    └── workflows/
        └── deploy.yml # CI/CD 自動部署腳本
2. 資料結構定義 (Data Schema)
2.1 產品矩陣資料 (App Matrix JSON)
這是為了讓您的 iOS App 能夠讀取並做交叉推廣 (Cross-Promotion)。

檔案路徑: static/api/apps.json

公開網址: https://yourname.github.io/api/apps.json

JSON
{
  "apps": [
    {
      "id": "com.yourname.ganttplanet",
      "name": "甘特星球",
      "icon_url": "https://yourname.github.io/images/apps/gantt_icon.png",
      "description": "3D 視覺化的專案管理工具，支援離線操作。",
      "store_url": "https://apps.apple.com/app/id123456789",
      "is_promoted": true
    },
    {
      "id": "com.yourname.learnjapanese",
      "name": "安靜日語",
      "icon_url": "https://yourname.github.io/images/apps/jp_icon.png",
      "description": "無干擾的假名記憶卡片。",
      "store_url": "https://apps.apple.com/app/id987654321",
      "is_promoted": true
    }
  ]
}
2.2 文章 Front Matter (Markdown Header)
每篇 .md 文章開頭的定義區塊。

YAML
---
title: "App Store 拒絕了我 3 次：甘特星球的上架血淚史"
date: 2026-02-09T14:00:00+08:00
draft: false
tags: ["iOS Dev", "App Store", "Indie Hacker"]
categories: ["The Workshop"] # 對應 "實作工坊"
description: "關於 Guideline 5.1.1 的攻防戰紀錄..."
cover:
    image: "images/posts/app-review-cover.jpg"
---
3. 實作指南 (Implementation Guide)
3.1 安裝與初始化 (Hugo Setup)
安裝 Hugo (macOS):

Bash
brew install hugo
建立新站點:

Bash
hugo new site memode
cd memode
git init
安裝主題 (推薦 PaperMod):

PaperMod 是目前開發者圈最流行、極簡且支援 Dark Mode 的主題。

Bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
設定 Config: 修改根目錄下的 hugo.toml (或 hugo.yml)：

Ini, TOML
baseURL = 'https://yourname.github.io/'
languageCode = 'zh-tw'
title = '核舟'
theme = 'PaperMod'

[params]
defaultTheme = "auto" # 跟隨系統深色模式
ShowReadingTime = true
ShowShareButtons = true

# 選單設定
[[menu.main]]
identifier = "apps"
name = "Apps"
url = "/apps/"
weight = 10

[[menu.main]]
identifier = "blog"
name = "Blog"
url = "/posts/"
weight = 20
3.2 整合 Giscus 評論系統 (Giscus Setup)
這是您提到的陌生部分，請依序執行：

準備 GitHub Repository:

確保您的網站 Repo 是 Public (公開) 的。

進入 Repo 的 "Settings" -> "General" -> "Features"。

勾選 "Discussions"。

安裝 Giscus App:

前往 Giscus 官網。

點擊安裝 Giscus App 到您的 GitHub 帳號，並選擇該 Repository。

取得設定參數:

回到 Giscus 官網下方，輸入您的 username/repo。

選擇 "Discussion Category" (通常選 "General" 或 "Announcements")。

它會生成一段 <script> 程式碼。不要直接複製 HTML，我們只需要其中的參數。

在 Hugo 中配置 (以 PaperMod 為例):

PaperMod 內建支援 Giscus，不需要改 HTML。

在 hugo.toml 加入以下設定：

Ini, TOML
[params.comments]
host = "https://giscus.app"
id = "R_kgDOLxxxxxx"      # 從 Giscus 官網取得 (Repo ID)
category = "General"
categoryId = "DIC_kwDOLxxxxxx" # 從 Giscus 官網取得 (Category ID)
mapping = "pathname"      # 以文章網址作為討論串標題
strict = "0"
reactionsEnabled = "1"
emitMetadata = "0"
inputPosition = "bottom"
theme = "preferred_color_scheme"
lang = "zh-TW"
loading = "lazy"
repo = "yourname/your-repo"
3.3 部署自動化 (GitHub Actions)
這是為了讓您像 Push code 到 Server 一樣，推送到 GitHub 就自動更新網站。

在專案根目錄建立檔案 .github/workflows/hugo.yaml。

貼上以下內容 (這是 Hugo 官方推薦腳本)：

YAML
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main  # 確保您的主分支名稱是 main 或 master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true  # 抓取主題 submodule
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
GitHub 設定:

Push 代碼到 GitHub。

進入 Repo Settings -> Pages。

將 Source 改為 "gh-pages" branch (這個分支會由 Action 自動建立)。

4. 產品矩陣頁面實作 (The App Matrix Page)
您希望有一個頁面展示所有 App。最簡單的方法是利用 Hugo 的 "Shortcode" 功能，這樣您可以在 Markdown 裡直接呼叫。

建立 Shortcode 模板: 建立檔案 layouts/shortcodes/app-card.html：

HTML
<div class="app-card" style="border: 1px solid #333; padding: 20px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center; gap: 20px;">
    <img src="{{ .Get "icon" }}" alt="{{ .Get "name" }}" style="width: 80px; height: 80px; border-radius: 16px;">
    <div>
        <h3 style="margin: 0;">{{ .Get "name" }}</h3>
        <p style="margin: 5px 0;">{{ .Get "desc" }}</p>
        <a href="{{ .Get "url" }}" target="_blank" style="background: #007AFF; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none; font-size: 0.9em;">Download on App Store</a>
    </div>
</div>
在 Markdown 中使用: 建立 content/apps/_index.md：

Markdown
---
title: "App 矩陣"
layout: "page"
---

這是我目前的 App 產品組合，旨在提供離線、專注的數位體驗。

{{< app-card name="甘特星球" icon="/images/gantt.png" desc="3D 視覺化專案管理" url="#" >}}

{{< app-card name="安靜日語" icon="/images/jp.png" desc="專注的假名學習卡片" url="#" >}}
5. 開發流程總結 (Workflow Summary)
寫文章: hugo new posts/my-new-post.md -> 使用 Markdown 編輯。

更新 App 列表: 編輯 static/api/apps.json (您的 iOS App 會讀取這個) 以及 content/apps/_index.md (網站顯示用)。

本地預覽: 執行 hugo server -D，瀏覽器打開 localhost:1313。

發布:

Bash
git add .
git commit -m "New post: App Store Review"
git push origin main
喝咖啡: 等待 1 分鐘，GitHub Actions 會自動編譯並更新網站。

這套流程完全符合您 Sysadmin 的背景：Config as Code, GitOps, CI/CD, Static Files。