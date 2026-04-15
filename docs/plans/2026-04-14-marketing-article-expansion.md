# Marketing Article Expansion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Turn all eight shipped App Store product pages into substantial Traditional Chinese marketing articles while keeping support pages clearly separate and utilitarian.

**Architecture:** Keep the shared app metadata and product-page layout in place, but add rich per-app Markdown bodies under `content/apps/`. Extend the URL matrix and support coverage to include `stonestory`, because this request now treats the product set as eight published/store-facing apps.

**Tech Stack:** Hugo, Markdown content pages, existing app data YAML, existing screenshots, Blowfish custom section layouts.

---

### Task 1: Add the eighth app to the site structure

**Files:**
- Modify: `data/app_url_matrix.yaml`
- Create: `content/apps/stonestory.md`
- Create: `content/support/stonestory.md`
- Modify: `marketing_url.md`

**Step 1: Add `stonestory` to the app URL mapping**

Include store URL, marketing URL, privacy URL, support URL, icon path, product copy, and article links.

**Step 2: Add the product page shell**

Create `content/apps/stonestory.md` with the same route pattern as the other apps.

**Step 3: Add the support page shell**

Create `content/support/stonestory.md` with the same route pattern as the other support pages.

**Step 4: Add `stonestory` to the URL matrix**

Update `marketing_url.md` so the document reflects the full eight-app scope for this task.

### Task 2: Write the seven existing product pages as real marketing articles

**Files:**
- Modify:
  - `content/apps/python-dimensions.md`
  - `content/apps/kana-juku.md`
  - `content/apps/english-n-plus-1.md`
  - `content/apps/gantt-planet.md`
  - `content/apps/auditory-companion.md`
  - `content/apps/atomic-presence.md`
  - `content/apps/sown-echoes.md`

**Step 1: Add a non-generic opening section**

Each article should open with audience, problem, and product promise.

**Step 2: Add scenario-driven sections**

Explain when and why someone would use the app, not just what features exist.

**Step 3: Add feature interpretation**

Translate the raw feature list into user-facing value, with some texture and product voice.

**Step 4: Add privacy and offline positioning**

For each app, explain why on-device / no-tracking matters in that product context.

**Step 5: Add CTA-oriented closing**

Close each article with a short “who this is for” section and a direct App Store call-to-action.

### Task 3: Write the eighth product page for StoneStory

**Files:**
- Modify: `content/apps/stonestory.md`
- Reference:
  - `/Users/Drops/Data/DigitalAssets/apps/stone-story.yaml`
  - `content/posts/stonestory_fate.md`
  - `content/posts/stonestory_thermodynamics.md`

**Step 1: Write the positioning section**

Frame StoneStory as an AI-driven classical literature simulation product, not just a research toy.

**Step 2: Add scenario and feature sections**

Explain who would use it, what “simulation” means in practice, and why on-device execution matters.

**Step 3: Add links to the two existing deep-dive essays**

Use them as supporting longform references instead of duplicating all theory inside the marketing page.

### Task 4: Keep support pages distinct from market pages

**Files:**
- Verify / lightly adjust:
  - `content/support/*.md`

**Step 1: Keep support copy short**

Support pages should not become alternate product essays.

**Step 2: Ensure support pages answer operational questions**

Contact, what to include in bug reports, and links to product/privacy.

### Task 5: Verify the result locally

**Files:**
- Verify only

**Step 1: Run a Hugo build**

Run: `hugo`

Expected: exit code `0`.

**Step 2: Spot-check rendered pages**

Check at least:

- `public/apps/gantt-planet/index.html`
- `public/apps/stonestory/index.html`
- `public/support/stonestory/index.html`

**Step 3: Confirm all eight product pages exist**

Run: `find public/apps -maxdepth 2 -name index.html | sort`

Expected: eight app pages plus the apps index.
