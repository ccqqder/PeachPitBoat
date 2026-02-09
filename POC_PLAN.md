# POC Plan: 核舟 Hugo Site on GitHub Pages

**Goal:** Get a working Hugo site live at `https://ccqqder.github.io/OliverPitBoat/` with PaperMod theme, one sample blog post (前赤壁賦), and basic site structure.

---

## Step 1: Install Hugo via winget

```bash
winget install Hugo.Hugo.Extended
```
Verify with `hugo version`.

## Step 2: Initialize Hugo site in current directory

Since we already have files (PRD.md, SPEC.md, etc.), we'll use `hugo new site . --force` to scaffold Hugo structure around existing files.

## Step 3: Add PaperMod theme as git submodule

```bash
git init
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

## Step 4: Create `hugo.toml` config

- baseURL = `https://ccqqder.github.io/OliverPitBoat/`
- theme = PaperMod
- languageCode = zh-tw
- defaultTheme = auto (dark mode follows system)
- Menu: Home, Apps, Blog, About

## Step 5: Create sample blog post from `sample_article.txt`

Create `content/posts/red-cliff.md` with:
- Title: 前赤壁賦
- Author: 蘇軾
- Category: "The Observatory"
- Content: the full text from sample_article.txt

## Step 6: Create minimal About page

Create `content/about.md` — a brief placeholder manifesto.

## Step 7: Create Apps matrix page

Create `content/apps/_index.md` with placeholder app cards.
Create `static/api/apps.json` with sample data.

## Step 8: Create GitHub Actions workflow

Create `.github/workflows/hugo.yaml` for auto-deploy to gh-pages.

## Step 9: Create GitHub repo & push

```bash
gh repo create OliverPitBoat --public --source=. --push
```

## Step 10: Configure GitHub Pages

Set Pages source to GitHub Actions (or gh-pages branch) via `gh` CLI.

## Step 11: Verify

Confirm site is live at `https://ccqqder.github.io/OliverPitBoat/`.

---

## What's NOT in POC (deferred to later phases)

- Giscus comments integration
- Custom domain
- App Store real links
- Real app icons
- SEO optimization
- Waitlist/email forms
- Easter eggs / 404 page
