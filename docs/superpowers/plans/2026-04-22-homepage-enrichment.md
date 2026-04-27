# Homepage Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the identical-to-posts homepage with a three-section layout: pinned featured articles → app showcase grid → recent posts.

**Architecture:** Override `layouts/partials/home/profile.html` (Hugo root overrides theme) to insert two new partials between the bio header and the existing `recent-articles/main.html`. Featured posts are configured via `params.toml`; apps are sourced from Hugo's `content/apps/` pages. No changes to the Blowfish theme directory.

**Tech Stack:** Hugo Extended v0.155.2, Blowfish theme (Tailwind CSS), Hugo i18n, Go templates.

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Modify | `config/_default/params.toml` | Add `featuredPosts` list under `[homepage]` |
| Create | `i18n/zh-TW.yaml` | Section heading strings for zh-TW |
| Create | `i18n/en.yaml` | Section heading strings for en |
| Create | `i18n/ja.yaml` | Section heading strings for ja |
| Create | `layouts/partials/home/featured-articles.html` | Render pinned posts by slug |
| Create | `layouts/partials/home/app-showcase.html` | Render app icon grid |
| Modify | `layouts/partials/home/profile.html` | Wire featured + apps + recent into bio page |

---

### Task 1: Add featuredPosts config

**Files:**
- Modify: `config/_default/params.toml`

- [ ] **Step 1: Add featuredPosts under [homepage]**

In `config/_default/params.toml`, replace the existing `[homepage]` block with:

```toml
[homepage]
  layout = "profile"
  showRecent = true
  showRecentItems = 5
  showMoreLink = true
  showMoreLinkDest = "/posts/"
  cardView = false
  featuredPosts = ["stonestory_thermodynamics", "gantt-planet-intro"]
```

- [ ] **Step 2: Verify Hugo parses it without error**

```bash
hugo config | grep featuredPosts
```

Expected: line containing `featuredposts: [stonestory_thermodynamics gantt-planet-intro]`

---

### Task 2: Create i18n string files

**Files:**
- Create: `i18n/zh-TW.yaml`
- Create: `i18n/en.yaml`
- Create: `i18n/ja.yaml`

Hugo merges root-level `i18n/` with theme i18n — no theme files are touched.

- [ ] **Step 1: Create `i18n/zh-TW.yaml`**

```yaml
homepage_featured:
  other: 精選文章
homepage_apps:
  other: 應用程式
homepage_apps_more:
  other: 查看全部
```

- [ ] **Step 2: Create `i18n/en.yaml`**

```yaml
homepage_featured:
  other: Featured
homepage_apps:
  other: Apps
homepage_apps_more:
  other: View all
```

- [ ] **Step 3: Create `i18n/ja.yaml`**

```yaml
homepage_featured:
  other: 厳選記事
homepage_apps:
  other: アプリ
homepage_apps_more:
  other: すべて見る
```

- [ ] **Step 4: Verify strings resolve**

```bash
hugo server -D --port 1314 &
# then kill it — just checking for template errors in the build output
```

Expected: no `i18n` key-not-found warnings.

---

### Task 3: Create featured-articles partial

**Files:**
- Create: `layouts/partials/home/featured-articles.html`

Reads `site.Params.homepage.featuredPosts`, looks up each page by path, delegates rendering to the existing `article-link/simple.html` partial (which handles feature images, titles, summaries).

- [ ] **Step 1: Create `layouts/partials/home/featured-articles.html`**

```html
{{ with site.Params.homepage.featuredPosts }}
<section class="mt-8">
  <h2 class="mb-6 text-2xl font-extrabold">{{ i18n "homepage_featured" }}</h2>
  <div class="space-y-10 w-full">
    {{ range . }}
      {{ $page := site.GetPage (printf "posts/%s" .) }}
      {{ with $page }}
        {{ partial "article-link/simple.html" . }}
      {{ end }}
    {{ end }}
  </div>
</section>
{{ end }}
```

- [ ] **Step 2: Smoke-check template compiles**

```bash
hugo build --templateMetrics 2>&1 | grep -i error
```

Expected: no errors.

---

### Task 4: Create app-showcase partial

**Files:**
- Create: `layouts/partials/home/app-showcase.html`

Sources app pages from `content/apps/` (Type = "apps"), excludes `_index` pages. Icon path is constructed from `app_slug` front matter matching the pattern in `static/images/apps/`.

- [ ] **Step 1: Create `layouts/partials/home/app-showcase.html`**

```html
{{ $apps := where (where site.RegularPages "Type" "apps") "Params.app_slug" "!=" nil }}
{{ with $apps }}
<section class="mt-10">
  <div class="flex items-baseline justify-between mb-6">
    <h2 class="text-2xl font-extrabold">{{ i18n "homepage_apps" }}</h2>
    <a href="{{ "/apps/" | relLangURL }}"
       class="text-sm font-medium text-primary-600 dark:text-primary-400 hover:underline">
      {{ i18n "homepage_apps_more" }} →
    </a>
  </div>
  <div class="not-prose grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
    {{ range . }}
      {{ $iconURL := printf "/images/apps/%s.png" .Params.app_slug | absURL }}
      <a href="{{ .RelPermalink }}"
         class="group flex flex-col items-center text-center p-3 rounded-xl
                hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors">
        <img src="{{ $iconURL }}"
             alt="{{ .Title }}"
             loading="lazy"
             class="w-16 h-16 rounded-2xl mb-2 shadow-sm">
        <span class="text-sm font-semibold text-neutral-800 dark:text-neutral leading-tight">
          {{ .Title }}
        </span>
        {{ with .Params.summary }}
          <span class="text-xs text-neutral-500 dark:text-neutral-400 mt-1 line-clamp-2 leading-snug">
            {{ . }}
          </span>
        {{ end }}
      </a>
    {{ end }}
  </div>
</section>
{{ end }}
```

- [ ] **Step 2: Verify Hugo builds without error**

```bash
hugo build --templateMetrics 2>&1 | grep -i error
```

Expected: no errors.

---

### Task 5: Override profile.html

**Files:**
- Modify: `layouts/partials/home/profile.html`

Copy the theme's profile.html verbatim (already present from the current override at `layouts/partials/home/profile.html`) and insert the two new section partials between the bio `<section>` and the existing `recent-articles` call.

- [ ] **Step 1: Replace `layouts/partials/home/profile.html`**

Full file content (theme bio block preserved exactly, two partials added):

```html
{{ $disableImageOptimization := .Site.Params.disableImageOptimization | default false }}
<article
  class="{{ if not .Site.Params.homepage.showRecent }}
    h-full
  {{ end }} flex flex-col items-center justify-center text-center">
  <header class="relative px-1 py-1 flex flex-col items-center mb-3">
    {{ with .Site.Params.Author.image }}
      {{ $authorImage := "" }}
      {{ if or (strings.HasPrefix . "http:") (strings.HasPrefix . "https:") }}
        {{ $authorImage = resources.GetRemote . }}
      {{ else }}
        {{ $authorImage = resources.Get . }}
      {{ end }}
      {{ if $authorImage }}
        {{ $final := $authorImage }}
        {{ $squareImage := $authorImage }}
        {{ if not (or $disableImageOptimization (eq $authorImage.MediaType.SubType "svg")) }}
          {{ $final = $authorImage.Fill (print "288x288 q" ( $.Site.Params.Author.imagequality | default "96" )) }}
          {{ $shortSide := int (math.Min $authorImage.Width $authorImage.Height) }}
          {{ $squareImage = $authorImage.Crop (printf "%dx%d" $shortSide $shortSide ) }}
        {{ end }}
        <img
          class="mb-2 h-36 w-36 rounded-full"
          width="144"
          height="144"
          alt="{{ $.Site.Params.Author.name | default `Author` }}"
          src="{{ $final.RelPermalink }}"
          data-zoom-src="{{ $squareImage.RelPermalink }}">
      {{ end }}
    {{ end }}
    <h1 class="text-4xl font-extrabold">
      {{ .Site.Params.Author.name | default .Site.Title }}
    </h1>
    {{ with .Site.Params.Author.headline }}
      <h2 class="text-xl text-neutral-500 dark:text-neutral-400">
        {{ . | markdownify }}
      </h2>
    {{ end }}
    <div class="mt-1 text-2xl">
      {{ partialCached "author-links.html" . }}
    </div>
  </header>
  <section class="prose dark:prose-invert w-full">{{ .Content }}</section>
</article>

{{ partial "home/featured-articles.html" . }}
{{ partial "home/app-showcase.html" . }}

<section>
  {{ partial "recent-articles/main.html" . }}
</section>
```

- [ ] **Step 2: Start dev server and check homepage**

```bash
hugo server -D
```

Open `http://localhost:1313/PeachPitBoat/` and verify:
- Bio section renders (avatar, name, headline)
- "精選文章" heading appears with two article cards (stonestory_thermodynamics, gantt-planet-intro) with feature images
- "應用程式" heading appears with 8 app icons in a grid
- "查看全部 →" link points to `/PeachPitBoat/apps/`
- "最近的文章" section appears at bottom with 5 posts

- [ ] **Step 3: Check English route**

Open `http://localhost:1313/PeachPitBoat/en/` and verify headings are in English ("Featured", "Apps", "View all").

- [ ] **Step 4: Check Japanese route**

Open `http://localhost:1313/PeachPitBoat/ja/` and verify headings are in Japanese.

---

### Task 6: Commit

- [ ] **Step 1: Commit all changes**

```bash
git add config/_default/params.toml \
        i18n/zh-TW.yaml i18n/en.yaml i18n/ja.yaml \
        layouts/partials/home/featured-articles.html \
        layouts/partials/home/app-showcase.html \
        layouts/partials/home/profile.html
git commit -m "feat(homepage): add featured articles + app showcase sections"
```
