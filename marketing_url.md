# App Store URLs 建議

這份筆記整理 Apple App Store Connect 內三個常見網站欄位的用途與建議填法：

- `Marketing URL`
- `Support URL`
- `Privacy Policy URL`

重點是三者要分工清楚，不要混成同一頁。

## 1. Marketing URL

### 用途

給還沒下載 App 的使用者看更多產品資訊，屬於產品介紹頁。

### 應該放什麼

- App 的一句定位
- 主要功能與價值
- 產品截圖
- App Store 連結
- 常見問題
- 指向 `Support URL` 與 `Privacy Policy URL` 的連結

### 不建議

- 拿法律頁充當產品頁
- 拿單純聯絡頁充當產品頁
- 只放一篇沒有明確 CTA 的隨筆文章

### 對目前專案的建議

最佳做法是做一個專屬產品頁，例如：

`https://ccqqder.github.io/PeachPitBoat/apps/gantt-planet/`

如果暫時不做專屬 landing page，次佳可先用：

`https://ccqqder.github.io/PeachPitBoat/posts/gantt-planet/`

## 2. Support URL

### 用途

給已下載使用者尋找支援、回報問題、聯絡開發者。

### 應該放什麼

- 支援聯絡方式
- Email
- 常見問題
- 已知問題
- 版本資訊
- 回報 bug 或提供意見的方式
- 指向 `Marketing URL` 與 `Privacy Policy URL` 的連結

### 不建議

- 沒有聯絡方式
- 只有產品介紹，沒有支援資訊
- 只是一篇部落格文章

### 對目前專案的建議

建立專用支援頁，例如：

`https://ccqqder.github.io/PeachPitBoat/support/gantt-planet/`

## 3. Privacy Policy URL

### 用途

這是隱私政策頁，不是產品頁，也不是支援頁。

Apple 要求它連到你公司或開發者的隱私政策，而且所有 App 都必填。

### 應該放什麼

- 是否收集個人資料
- 是否有追蹤
- 是否使用第三方 SDK
- 資料是否上傳伺服器
- 使用者資料如何被使用
- 聯絡方式
- 最後更新日期

### 不建議

- 用一般產品介紹文代替
- 內容過短，看不出隱私承諾
- 沒有更新日期或聯絡方式

### 對目前專案的建議

建立專用隱私頁，例如：

`https://ccqqder.github.io/PeachPitBoat/legal/gantt-planet-privacy/`

## 4. 最佳實務

最好的做法是三個 URL 都放在同一個主網域 `PeachPitBoat` 下，並互相連結：

- `Marketing URL` 連到 `Support URL`、`Privacy Policy URL`
- `Support URL` 連到 `Marketing URL`、`Privacy Policy URL`
- `Privacy Policy URL` 在頁尾連回產品頁

這樣比較符合：

- 使用者理解
- Apple 審核邏輯
- 搜尋引擎抓取與內鏈結構

## 5. 目前建議填法

針對 `甘特星球`，建議如下：

- `Marketing URL`
  - `https://ccqqder.github.io/PeachPitBoat/apps/gantt-planet/`
- `Support URL`
  - `https://ccqqder.github.io/PeachPitBoat/support/gantt-planet/`
- `Privacy Policy URL`
  - `https://ccqqder.github.io/PeachPitBoat/legal/gantt-planet-privacy/`

如果目前尚未建立專屬產品頁，可暫時改為：

- `Marketing URL`
  - `https://ccqqder.github.io/PeachPitBoat/posts/gantt-planet/`

但仍不建議把 `Privacy Policy URL` 指到一般文章。

## 6. 補充

`Marketing URL` 是 Apple App Store Connect 的欄位名稱，不是 Google SEO 的專有名詞。

它本身不是 Google 排名功能，但如果這個網址內容完整、可索引、內鏈合理，會對搜尋可見性有間接幫助。

## 參考

- Apple `Support URL` / `Marketing URL`
  - https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information
- Apple `Privacy Policy URL`
  - https://developer.apple.com/help/app-store-connect/reference/app-information/app-privacy
- Apple App Review Guidelines
  - https://developer.apple.com/app-store/review/guidelines/
