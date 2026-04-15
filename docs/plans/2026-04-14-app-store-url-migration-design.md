# App Store URL Migration Design

**Date:** 2026-04-14

**Goal:** Move privacy policy URLs into the `PeachPitBoat` site, create first-party marketing URLs for all shipped apps, and add lightweight support URLs as a nice-to-have so App Store Connect can eventually point to a single domain.

## Scope

Apps in scope are the shipped apps only, using the slug set already established in the legacy legal repo:

- `python-dimensions`
- `kana-juku`
- `english-n-plus-1`
- `gantt-planet`
- `auditory-companion`
- `atomic-presence`
- `sown-echoes`
- `stonestory`

## Chosen Approach

Use a hybrid migration:

- **Privacy pages:** copy the existing legal HTML into this repo with minimal structural change.
- **Marketing pages:** build Hugo pages under `/apps/<slug>/` using app metadata, existing screenshots, and existing posts when available.
- **Support pages:** build lightweight Hugo pages under `/support/<slug>/` with contact, support guidance, and links back to marketing and privacy.

This keeps legal copy stable while still producing first-party product and support URLs inside the current site.

## URL Structure

- `Marketing URL`: `https://ccqqder.github.io/PeachPitBoat/apps/<slug>/`
- `Privacy Policy URL`: `https://ccqqder.github.io/PeachPitBoat/legal/<slug>/privacy/`
- `Support URL`: `https://ccqqder.github.io/PeachPitBoat/support/<slug>/`
- `Terms URL` for `sown-echoes`: `https://ccqqder.github.io/PeachPitBoat/legal/sown-echoes/terms/`

## Source of Truth

Each content type draws from a different source:

- **Legal HTML:** `/Users/Drops/Data/qqder339/qqder339-legal`
- **App metadata and hero assets:** `/Users/Drops/Data/DigitalAssets/apps/*.yaml` and matching `.jpg`
- **In-site screenshots and deep product context:** `content/posts/*`, `static/images/screenshots/*`
- **App Store URL planning note:** `marketing_url.md`

Slug naming follows the existing legal repo, even where DigitalAssets uses a different filename convention such as `english-plus-one`, `meme-lives`, or `stone-story`.

## Data Model

Create a local structured data file in this repo that normalizes:

- slug
- display name
- app store URL
- marketing URL
- privacy URL
- support URL
- terms URL when applicable
- screenshot directory
- icon path
- status

This gives the site one internal mapping layer instead of scattering URL decisions across content files.

## Content Strategy

### Privacy

- Preserve bilingual HTML content.
- Preserve last-updated dates unless a migration-specific adjustment is required.
- Preserve existing legal wording unless a broken link or site path must change.
- Carry shared styling into this repo so the migrated pages remain legible and self-contained.

### Marketing

Each app page should include:

- app name and one-line positioning
- app icon or hero image
- short feature summary pulled from YAML/post copy
- screenshot gallery or selected screenshots
- App Store link
- links to support and privacy

Where a dedicated post already exists, the marketing page can link to that deeper article instead of duplicating all longform copy.

### Support

Each support page should be intentionally minimal:

- support email
- how to report bugs or request help
- expected response scope
- App Store link
- links to marketing and privacy

This is a support URL, not a blog article and not a legal page.

## Site Integration

- Keep the current `/apps/` index page intact unless a small link enhancement is clearly useful.
- Add new content so URLs resolve even without touching top-level navigation.
- Prefer Hugo content pages for marketing/support so the pages inherit site chrome, breadcrumbs, and SEO behavior.
- Keep privacy pages simple and stable, even if they use a separate visual treatment from normal content pages.

## Migration Constraints

- Do not rename slugs away from the current legal repo naming.
- Do not update App Store Connect in this task.
- Do not break existing blog post URLs.
- Do not attempt a full legal copy rewrite during migration.

## Verification

Success means:

- every shipped app has a live `marketing` URL
- every shipped app has a live `privacy` URL inside this repo
- support URLs exist for shipped apps
- `marketing_url.md` becomes a concrete URL matrix rather than a conceptual note
- Hugo build succeeds and generated routes match the intended URL structure
