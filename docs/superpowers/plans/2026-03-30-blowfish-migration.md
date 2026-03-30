# Blowfish Theme Migration + Braun Style

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate from PaperMod to Blowfish theme with a custom Braun-inspired color scheme and animated profile avatar.

**Architecture:** Replace PaperMod git submodule with Blowfish. Convert single `hugo.toml` to Blowfish's split config directory (`config/_default/`). Create custom Braun color scheme CSS. Generate animated GIF avatar from two PNG frames. Adapt content front matter for Blowfish compatibility.

**Tech Stack:** Hugo Extended, Blowfish theme (git submodule), Python (Pillow for GIF), custom CSS, TinaCMS

---

## File Structure

```
# New files to create
config/_default/hugo.toml           # Core Hugo settings
config/_default/params.toml         # Blowfish theme parameters
config/_default/languages.zh-tw.toml # Chinese language + author profile
config/_default/languages.en.toml   # English language + author profile
config/_default/menus.zh-tw.toml    # Chinese menus
config/_default/menus.en.toml       # English menus
config/_default/markup.toml         # Goldmark / highlight settings
assets/css/schemes/braun.css        # Custom Braun color scheme
assets/css/custom.css               # Additional Braun styling (app-card etc.)
assets/img/author.gif               # Animated avatar GIF

# Files to modify
content/posts/*.md                  # Front matter: ShowReadingTime → showReadingTime, author → authors
content/about.md                    # layout: page → layout: simple
content/apps/_index.md              # layout: page → layout: simple
tina/config.ts                      # Update field names for Blowfish compat

# Files to delete
hugo.toml                           # Replaced by config/_default/ split files

# Submodule changes
themes/PaperMod/                    # Remove
themes/blowfish/                    # Add
```

---

### Task 1: Create Animated GIF Avatar

**Files:**
- Create: `assets/img/author.gif`

- [ ] **Step 1: Generate GIF from two PNG frames using Python**

```bash
"C:\Program Files\Python313\python.exe" -c "
from PIL import Image
import sys

img1 = Image.open(r'C:\Users\14018\Downloads\temp\Gemini_Generated_Image_qu7mlmqu7mlmqu7m.png')
img2 = Image.open(r'C:\Users\14018\Downloads\temp\Gemini_Generated_Image_1pcoom1pcoom1pco.png')

# Resize to 400x400 for web performance
img1 = img1.resize((400, 400), Image.LANCZOS)
img2 = img2.resize((400, 400), Image.LANCZOS)

# Convert to RGBA then P mode for GIF
img1 = img1.convert('RGBA')
img2 = img2.convert('RGBA')

# Save as animated GIF: 1s on frame1, 0.3s on frame2 (drill impact)
img1.save(
    r'C:\Users\14018\Documents\codes\web_desktop\OliverPitBoat\assets\img\author.gif',
    save_all=True,
    append_images=[img2],
    duration=[1000, 300],
    loop=0,
    optimize=True
)
print('GIF created successfully')
"
```

- [ ] **Step 2: Verify GIF exists and is reasonable size**

```bash
ls -la assets/img/author.gif
```

Expected: File exists, size < 500KB

- [ ] **Step 3: Commit**

```bash
git add assets/img/author.gif
git commit -m "Add animated avatar GIF for Blowfish profile"
```

---

### Task 2: Replace Theme Submodule

**Files:**
- Remove: `themes/PaperMod/` (submodule)
- Create: `themes/blowfish/` (submodule)

- [ ] **Step 1: Remove PaperMod submodule**

```bash
git submodule deinit -f themes/PaperMod
git rm -f themes/PaperMod
rm -rf .git/modules/themes/PaperMod
```

- [ ] **Step 2: Add Blowfish submodule**

```bash
git submodule add -b main https://github.com/nunocoracao/blowfish.git themes/blowfish
```

- [ ] **Step 3: Verify submodule is populated**

```bash
ls themes/blowfish/layouts/
```

Expected: Directory listing with `_default/`, `partials/`, `shortcodes/`, etc.

- [ ] **Step 4: Commit**

```bash
git add .gitmodules themes/
git commit -m "Replace PaperMod with Blowfish theme submodule"
```

---

### Task 3: Create Split Config Files

**Files:**
- Delete: `hugo.toml` (root)
- Create: `config/_default/hugo.toml`
- Create: `config/_default/params.toml`
- Create: `config/_default/languages.zh-tw.toml`
- Create: `config/_default/languages.en.toml`
- Create: `config/_default/menus.zh-tw.toml`
- Create: `config/_default/menus.en.toml`
- Create: `config/_default/markup.toml`

- [ ] **Step 1: Create config directory**

```bash
mkdir -p config/_default
```

- [ ] **Step 2: Create `config/_default/hugo.toml`**

```toml
baseURL = "https://ccqqder.github.io/OliverPitBoat/"
theme = "blowfish"
defaultContentLanguage = "zh-tw"
defaultContentLanguageInSubdir = false
enableRobotsTXT = true
hasCJKLanguage = true
enableEmoji = true
summaryLength = 0

[pagination]
  pagerSize = 5

[taxonomies]
  tag = "tags"
  category = "categories"

[sitemap]
  changefreq = "daily"
  filename = "sitemap.xml"
  priority = 0.5

[outputs]
  home = ["HTML", "RSS", "JSON"]
```

- [ ] **Step 3: Create `config/_default/params.toml`**

```toml
colorScheme = "braun"
defaultAppearance = "dark"
autoSwitchAppearance = true
enableSearch = true
enableCodeCopy = true

[header]
  layout = "basic"

[footer]
  showMenu = true
  showCopyright = true
  showThemeAttribution = false
  showAppearanceSwitcher = true
  showScrollToTop = true

[homepage]
  layout = "profile"
  showRecent = true
  showRecentItems = 5
  showMoreLink = true
  showMoreLinkDest = "/posts/"
  cardView = false

[article]
  showDate = true
  showDateUpdated = false
  showAuthor = true
  showBreadcrumbs = true
  showReadingTime = true
  showTableOfContents = true
  showTaxonomies = true
  showWordCount = false
  showZenMode = false

[list]
  showBreadcrumbs = true
  showSummary = true
  groupByYear = true
```

- [ ] **Step 4: Create `config/_default/languages.zh-tw.toml`**

```toml
disabled = false
languageCode = "zh-tw"
languageName = "繁體中文"
weight = 1
title = "核舟"

[params]
  displayName = "繁體中文"
  isoCode = "zh-TW"
  dateFormat = "2006年1月2日"
  description = "核舟 — 興趣使然的開發者將自己做的小玩意丟進海里的記錄"

[params.author]
  name = "Oliver"
  image = "img/author.gif"
  headline = "核舟 — 數位古玩"
  bio = "AI 算力以後會被壟斷嗎？AI能力還會持續突破嗎？不管答案是什麼都要越早使用越好。這裡記錄一個文科背景 Sysadmin 靠 AI 協助開發iOS App。"
  links = [
    { github = "https://github.com/ccqqder" },
    { email = "mailto:qqder339@gmail.com" },
  ]
```

- [ ] **Step 5: Create `config/_default/languages.en.toml`**

```toml
disabled = false
languageCode = "en"
languageName = "English"
weight = 2
title = "The Miniature Boat"

[params]
  displayName = "EN"
  isoCode = "en"
  dateFormat = "2 January 2006"
  description = "The Miniature Boat — A logbook of a hobbyist developer casting digital creations into the vast ocean."

[params.author]
  name = "Oliver"
  image = "img/author.gif"
  headline = "核舟 — The Miniature Boat"
  bio = "Will AI compute be monopolized? Will AI capabilities keep breaking through? Regardless of the answer, the best time to start is now. This is a record of a humanities-background Sysadmin developing iOS apps with the assistance of AI."
  links = [
    { github = "https://github.com/ccqqder" },
    { email = "mailto:qqder339@gmail.com" },
  ]
```

- [ ] **Step 6: Create `config/_default/menus.zh-tw.toml`**

```toml
[[main]]
  name = "首頁"
  pageRef = "/"
  weight = 10

[[main]]
  name = "App 矩陣"
  pageRef = "apps"
  weight = 20

[[main]]
  name = "部落格"
  pageRef = "posts"
  weight = 30

[[main]]
  name = "關於"
  pageRef = "about"
  weight = 40
```

- [ ] **Step 7: Create `config/_default/menus.en.toml`**

```toml
[[main]]
  name = "Home"
  pageRef = "/"
  weight = 10

[[main]]
  name = "Apps"
  pageRef = "apps"
  weight = 20

[[main]]
  name = "Blog"
  pageRef = "posts"
  weight = 30

[[main]]
  name = "About"
  pageRef = "about"
  weight = 40
```

- [ ] **Step 8: Create `config/_default/markup.toml`**

```toml
[goldmark]
  [goldmark.parser]
    wrapStandAloneImageWithinParagraph = false
    [goldmark.parser.attribute]
      block = true
  [goldmark.renderer]
    unsafe = true

[highlight]
  noClasses = false

[tableOfContents]
  startLevel = 2
  endLevel = 4
```

- [ ] **Step 9: Delete root hugo.toml**

```bash
rm hugo.toml
```

- [ ] **Step 10: Verify Hugo can parse config**

```bash
export PATH="$PATH:/c/Users/14018/AppData/Local/Microsoft/WinGet/Links"
hugo config | head -20
```

Expected: Output showing `baseURL`, `theme = blowfish`, no errors.

- [ ] **Step 11: Commit**

```bash
git add config/ hugo.toml
git commit -m "Migrate config from single hugo.toml to Blowfish split config"
```

Note: `git add hugo.toml` stages the deletion.

---

### Task 4: Create Braun Color Scheme

**Files:**
- Create: `assets/css/schemes/braun.css`
- Create: `assets/css/custom.css`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p assets/css/schemes
```

- [ ] **Step 2: Create `assets/css/schemes/braun.css`**

Braun palette mapped to Blowfish's 3-family RGB system:
- **Neutral:** off-white (#F5F5F0) → matte-black (#2B2B2B) scale
- **Primary:** signal orange (#FF6600) scale
- **Secondary:** metal grey (#8B8B85) / aluminium scale

```css
:root {
  /* Neutral: off-white to matte black (Braun chassis) */
  --color-neutral: 245, 245, 240;
  --color-neutral-50: 250, 250, 247;
  --color-neutral-100: 245, 245, 240;
  --color-neutral-200: 232, 232, 224;
  --color-neutral-300: 210, 210, 200;
  --color-neutral-400: 170, 170, 160;
  --color-neutral-500: 139, 139, 133;
  --color-neutral-600: 100, 100, 95;
  --color-neutral-700: 70, 70, 66;
  --color-neutral-800: 43, 43, 43;
  --color-neutral-900: 25, 25, 25;

  /* Primary: signal orange (Braun accent) */
  --color-primary-50: 255, 243, 230;
  --color-primary-100: 255, 224, 194;
  --color-primary-200: 255, 194, 133;
  --color-primary-300: 255, 163, 71;
  --color-primary-400: 255, 133, 31;
  --color-primary-500: 255, 102, 0;
  --color-primary-600: 224, 82, 0;
  --color-primary-700: 179, 66, 0;
  --color-primary-800: 133, 51, 0;
  --color-primary-900: 92, 36, 0;

  /* Secondary: aluminium / metal grey */
  --color-secondary-50: 240, 240, 245;
  --color-secondary-100: 224, 224, 232;
  --color-secondary-200: 200, 200, 210;
  --color-secondary-300: 175, 175, 185;
  --color-secondary-400: 150, 150, 160;
  --color-secondary-500: 120, 120, 130;
  --color-secondary-600: 95, 95, 105;
  --color-secondary-700: 75, 75, 82;
  --color-secondary-800: 55, 55, 60;
  --color-secondary-900: 35, 35, 38;
}
```

- [ ] **Step 3: Create `assets/css/custom.css`** for Braun-specific styling

```css
/* Braun Industrial Minimalism - Custom Overrides */

/* App-card shortcode styling for Braun aesthetic */
.app-card {
  border: 1px solid rgba(var(--color-neutral-300), 1);
  padding: 20px;
  border-radius: 4px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 20px;
  background: rgba(var(--color-neutral-800), 0.3);
  transition: border-color 0.15s ease;
}

.app-card:hover {
  border-color: rgba(var(--color-primary-500), 0.6);
}

.app-card .icon {
  font-size: 3em;
  line-height: 1;
}

.app-card h3 {
  margin: 0;
}

.app-card p {
  margin: 5px 0;
  opacity: 0.8;
}

.app-card .store-btn {
  background: rgba(var(--color-primary-500), 1);
  color: white;
  padding: 6px 14px;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.9em;
  display: inline-block;
  margin-top: 8px;
  transition: background 0.15s ease;
}

.app-card .store-btn:hover {
  background: rgba(var(--color-primary-600), 1);
}
```

- [ ] **Step 4: Commit**

```bash
git add assets/css/
git commit -m "Add custom Braun color scheme and CSS overrides"
```

---

### Task 5: Update App-Card Shortcode for Blowfish

**Files:**
- Modify: `layouts/shortcodes/app-card.html`

- [ ] **Step 1: Update shortcode to use Braun CSS classes**

Replace the entire content of `layouts/shortcodes/app-card.html` with:

```html
<div class="app-card">
    <span class="icon">{{ .Get "icon" }}</span>
    <div>
        <h3>{{ .Get "name" }}</h3>
        <p>{{ .Get "desc" }}</p>
        {{ if ne (.Get "url") "#" }}
        <a href="{{ .Get "url" }}" target="_blank" rel="noopener" class="store-btn">App Store</a>
        {{ end }}
    </div>
</div>
```

- [ ] **Step 2: Commit**

```bash
git add layouts/shortcodes/app-card.html
git commit -m "Update app-card shortcode to use Braun CSS classes"
```

---

### Task 6: Adapt Content Front Matter

**Files:**
- Modify: all `content/posts/*.md` — remove `ShowReadingTime` and `author` (handled globally by Blowfish config)
- Modify: `content/about.md` — remove `layout: page` (Blowfish uses different layout names)
- Modify: `content/apps/_index.md` — remove `layout: page`

- [ ] **Step 1: Remove PaperMod-specific front matter from all posts**

For each post file, remove these lines from front matter:
- `ShowReadingTime: true` (now global in `params.toml` → `[article] showReadingTime = true`)
- `author: "Oliver"` or `author: qqder339@gmail.com` etc. (now in `languages.*.toml` → `[params.author]`)

Files to edit:
- `content/posts/auditory-companion.md` — remove `author` and `ShowReadingTime`
- `content/posts/english-n-plus-1.md` — remove `author` and `ShowReadingTime`
- `content/posts/gantt-planet-intro.md` — remove `author` and `ShowReadingTime`
- `content/posts/gantt-planet.md` — remove `author` and `ShowReadingTime`
- `content/posts/kana_juku_dev_1.md` — remove `author`
- `content/posts/python-dimensions.md` — remove `author` and `ShowReadingTime`
- `content/posts/stonestory_fate.md` — remove `author` and `ShowReadingTime`

- [ ] **Step 2: Update about.md layout**

Change `layout: page` to `layout: simple` in front matter.

- [ ] **Step 3: Update apps/_index.md layout**

Change `layout: page` to `layout: simple` in front matter.

- [ ] **Step 4: Verify no remaining PaperMod-specific front matter**

```bash
grep -r "ShowReadingTime\|ShowShareButtons\|ShowPostNavLinks\|ShowBreadCrumbs\|ShowCodeCopyButtons" content/
```

Expected: No output (no matches).

- [ ] **Step 5: Commit**

```bash
git add content/
git commit -m "Adapt content front matter for Blowfish theme compatibility"
```

---

### Task 7: Update TinaCMS Config

**Files:**
- Modify: `tina/config.ts`

- [ ] **Step 1: Remove `ShowReadingTime` and `author` fields from posts collection**

In `tina/config.ts`, remove these two field objects from the `posts` collection's `fields` array:

```typescript
// REMOVE this field:
{
  type: "string",
  name: "author",
  label: "作者",
},
// REMOVE this field:
{
  type: "boolean",
  name: "ShowReadingTime",
  label: "顯示閱讀時間",
},
```

- [ ] **Step 2: Remove `layout` field from apps and about collections**

In the `apps` collection, remove the `layout` field object.
In the `about` collection, remove the `layout` field object.

- [ ] **Step 3: Commit**

```bash
git add tina/config.ts
git commit -m "Update TinaCMS config for Blowfish theme fields"
```

---

### Task 8: Build Verification and Cleanup

**Files:**
- Verify all existing files work together

- [ ] **Step 1: Run Hugo build**

```bash
export PATH="$PATH:/c/Users/14018/AppData/Local/Microsoft/WinGet/Links"
hugo --minify 2>&1
```

Expected: Build succeeds with no errors. Output shows pages generated.

- [ ] **Step 2: Fix any build errors**

If errors occur, read the error messages and fix the relevant config/content files.

- [ ] **Step 3: Run Hugo dev server and visually verify**

```bash
hugo server -D
```

Open `http://localhost:1313/OliverPitBoat/` in browser. Check:
- Profile layout renders with animated GIF avatar
- Navigation menu works (首頁, App 矩陣, 部落格, 關於)
- Blog posts list correctly
- Individual post pages render (reading time, ToC, tags)
- App 矩陣 page tables and app-card shortcodes display correctly
- Dark/light mode toggle works
- Braun color scheme applied (signal orange accents, off-white/matte-black base)
- Search works

- [ ] **Step 4: Clean up old public/ build artifacts**

```bash
rm -rf public/
hugo --minify
```

- [ ] **Step 5: Final commit and push**

```bash
git add -A
git commit -m "Complete Blowfish theme migration with Braun color scheme"
git push
```
