# App Store URL Migration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Migrate privacy policy URLs into `PeachPitBoat`, add first-party marketing pages for all shipped apps, and add lightweight support URLs for those same apps.

**Architecture:** Keep privacy content as migrated static HTML mounted under `static/legal/...`, while marketing and support are Hugo content pages driven by one normalized app URL mapping file. Reuse DigitalAssets YAML and in-repo screenshots instead of re-authoring product copy from scratch.

**Tech Stack:** Hugo, Markdown content, static HTML/CSS assets, YAML data files, existing Blowfish theme.

---

### Task 1: Create the normalized app URL mapping

**Files:**
- Create: `data/app_url_matrix.yaml`
- Reference: `/Users/Drops/Data/DigitalAssets/apps/*.yaml`
- Reference: `static/images/screenshots/`

**Step 1: Write the mapping file**

Add one record per shipped app with:

- `slug`
- `name`
- `icon`
- `store_url`
- `marketing_url`
- `privacy_url`
- `support_url`
- `terms_url`
- `screenshot_dir`
- `legacy_legal_source`

Use legal-repo slugs as canonical values.

**Step 2: Verify the mapping format**

Run: `sed -n '1,260p' data/app_url_matrix.yaml`

Expected: eight app entries with complete URL fields and no placeholder `TODO` values.

### Task 2: Import shared legal styling and migrate privacy HTML

**Files:**
- Create: `static/legal/assets/style.css`
- Create: `static/legal/index.html`
- Create: `static/legal/python-dimensions/privacy/index.html`
- Create: `static/legal/kana-juku/privacy/index.html`
- Create: `static/legal/english-n-plus-1/privacy/index.html`
- Create: `static/legal/gantt-planet/privacy/index.html`
- Create: `static/legal/auditory-companion/privacy/index.html`
- Create: `static/legal/atomic-presence/privacy/index.html`
- Create: `static/legal/sown-echoes/privacy/index.html`
- Create: `static/legal/sown-echoes/terms/index.html`
- Create: `static/legal/stonestory/privacy/index.html`
- Reference: `/Users/Drops/Data/qqder339/qqder339-legal/assets/style.css`
- Reference: `/Users/Drops/Data/qqder339/qqder339-legal/index.html`
- Reference: `/Users/Drops/Data/qqder339/qqder339-legal/*/*.html`

**Step 1: Copy the shared stylesheet**

Port the legal CSS into `static/legal/assets/style.css`.

**Step 2: Copy the legal index page**

Port the existing legal index and rewrite relative asset/link paths so they work under `/legal/`.

**Step 3: Copy each privacy page**

Port each privacy HTML file into `static/legal/<slug>/privacy/index.html`.

**Step 4: Copy the single terms page**

Port `sown-echoes/terms.html` into `static/legal/sown-echoes/terms/index.html`.

**Step 5: Rewrite internal links**

Update migrated HTML so:

- stylesheet references use `/PeachPitBoat/legal/assets/style.css`-safe relative paths
- privacy pages can link to marketing and support pages when useful
- the legal index points to the new in-repo paths

**Step 6: Verify migrated routes**

Run: `find static/legal -type f | sort`

Expected: legal asset file, index page, eight privacy routes, and one terms route.

### Task 3: Add reusable app-page partials or data access only if needed

**Files:**
- Modify or Create only if necessary:
  - `layouts/shortcodes/app-card.html`
  - `layouts/partials/`
  - `layouts/_default/`

**Step 1: Inspect whether plain Markdown is enough**

If existing Blowfish `simple` or `single` layout can render the marketing/support pages cleanly, do not add new layouts.

**Step 2: Add a minimal helper only if duplication becomes excessive**

If needed, add one small partial for repeated app meta blocks or screenshot rendering.

**Step 3: Verify no unnecessary layout sprawl**

Run: `find layouts -maxdepth 3 -type f | sort`

Expected: only the minimum extra template surface required by the new pages.

### Task 4: Create marketing pages for shipped apps

**Files:**
- Create:
  - `content/apps/python-dimensions.md`
  - `content/apps/kana-juku.md`
  - `content/apps/english-n-plus-1.md`
  - `content/apps/gantt-planet.md`
  - `content/apps/auditory-companion.md`
  - `content/apps/atomic-presence.md`
  - `content/apps/sown-echoes.md`
  - `content/apps/stonestory.md`
- Reference:
  - `data/app_url_matrix.yaml`
  - `/Users/Drops/Data/DigitalAssets/apps/*.yaml`
  - `content/posts/*.md`
  - `static/images/screenshots/*`

**Step 1: Add front matter for canonical product URLs**

Each file should set:

- `title`
- `layout: simple`
- `url: /apps/<slug>/`
- `summary`

**Step 2: Add concise product copy**

Build each page from available YAML and in-repo post content:

- one-sentence positioning
- short feature bullets
- App Store link
- privacy link
- support link

**Step 3: Add screenshot sections where assets exist**

Embed a small curated set instead of dumping every screenshot.

**Step 4: Link to deeper writing when relevant**

For apps with relevant longform posts, link out to those posts as "Learn more" or equivalent.

**Step 5: Verify marketing URLs exist**

Run: `rg -n '^url: /apps/' content/apps/*.md`

Expected: eight app pages with the intended routes.

### Task 5: Create support pages for shipped apps

**Files:**
- Create:
  - `content/support/_index.md`
  - `content/support/python-dimensions.md`
  - `content/support/kana-juku.md`
  - `content/support/english-n-plus-1.md`
  - `content/support/gantt-planet.md`
  - `content/support/auditory-companion.md`
  - `content/support/atomic-presence.md`
  - `content/support/sown-echoes.md`
  - `content/support/stonestory.md`
- Reference: `data/app_url_matrix.yaml`

**Step 1: Add support section index**

Create a lightweight index page explaining that support pages live here.

**Step 2: Add one support page per shipped app**

Each support page should include:

- contact email
- how to describe a bug report
- what information is useful when contacting support
- links to App Store, marketing, and privacy

**Step 3: Keep these pages intentionally minimal**

Do not add heavy product marketing copy here.

**Step 4: Verify support routes**

Run: `rg -n '^url: /support/' content/support/*.md`

Expected: eight support pages plus one section index.

### Task 6: Replace the URL planning note with a concrete matrix

**Files:**
- Modify: `marketing_url.md`
- Reference: `data/app_url_matrix.yaml`

**Step 1: Rewrite the document**

Keep a short explanation of field purpose, but make the main content a concrete table listing each shipped app and its:

- Marketing URL
- Privacy Policy URL
- Support URL
- Terms URL when applicable

**Step 2: Add a note about slug policy**

Document that canonical slugs follow the legacy legal repo for compatibility.

**Step 3: Verify the matrix**

Run: `sed -n '1,260p' marketing_url.md`

Expected: a copy-pastable URL matrix, not only general guidance.

### Task 7: Build and route verification

**Files:**
- Verify only

**Step 1: Run a Hugo build**

Run: `hugo`

Expected: exit code `0` and generated output with no broken template errors.

**Step 2: Inspect generated routes**

Run:

```bash
find public/apps -maxdepth 2 -name index.html | sort
find public/support -maxdepth 2 -name index.html | sort
find public/legal -maxdepth 4 -name index.html | sort
```

Expected: all shipped app routes exist under `apps`, `support`, and `legal`.

**Step 3: Spot-check cross-links**

Run:

```bash
rg -n '/(apps|support|legal)/' content/support content/apps marketing_url.md static/legal
```

Expected: internal URLs resolve to the new site structure with no remaining `qqder339-legal` URLs in newly authored pages.

### Task 8: Commit the migration cleanly

**Files:**
- Commit all migration files from Tasks 1-6

**Step 1: Review staged changes**

Run: `git diff --stat`

Expected: only migration-related files and no accidental local settings.

**Step 2: Commit**

Run:

```bash
git add data/app_url_matrix.yaml content/apps content/support static/legal marketing_url.md docs/plans/2026-04-14-app-store-url-migration-design.md docs/plans/2026-04-14-app-store-url-migration.md
git commit -m "Migrate App Store URLs into PeachPitBoat"
```

Expected: one clean migration commit.
