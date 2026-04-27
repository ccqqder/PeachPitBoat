"""Cross-locale i18n audit for the live PeachPitBoat site.

Fetches the homepage of every configured locale, extracts the SEO-critical
metadata that should differ per language (title, description, nav, og:locale,
canonical, hreflang) plus the things that should always be present (og:image),
then runs heuristics that flag the kinds of mistakes humans miss when
manually checking 8 languages: an English-locale title that's still in
Chinese, a stub locale missing menu items, a hreflang set that's lost an
entry, an og:image that 404s.

Usage from project root:
  python tools/audit_i18n.py                  # human-readable report
  python tools/audit_i18n.py --strict         # exit 1 if any locale has issues
  python tools/audit_i18n.py --base-url URL   # audit a different deployment

This is a fast HTTP-only check (no headless browser). It complements
Lighthouse: Lighthouse looks at one page deeply, this looks across 8 locales
shallowly.
"""
from __future__ import annotations
import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Optional

DEFAULT_BASE = "https://ccqqder.github.io/PeachPitBoat"

# Each locale: URL prefix path (relative to base), expected <html lang>,
# title style. `style` drives the title/description CJK heuristic:
#   en   — must NOT contain CJK ideographs or kana
#   ja   — kanji + kana acceptable
#   zh   — CJK ideographs acceptable
# `is_stub` controls the canonical check: stub locales' canonicals should
# strip the language prefix (collapse to EN equivalent).
LOCALES = [
    # (label,      url_prefix,   html_lang, style, is_stub)
    ("en-root",    "/",          "en",      "en",  False),
    ("zh-tw",      "/zh-tw/",    "zh-TW",   "zh",  False),
    ("ja",         "/ja/",       "ja",      "ja",  False),
    ("zh-hans",    "/zh-hans/",  "zh-Hans", "zh",  False),
    ("fr",         "/fr/",       "fr",      "en",  True),
    ("ko",         "/ko/",       "ko",      "en",  True),
    ("vi",         "/vi/",       "vi",      "en",  True),
    ("id",         "/id/",       "id",      "en",  True),
]

# Pages to audit per locale. The path is relative to the locale prefix.
# For a stub-translated page that has its own .md file the canonical should
# self-canonical; for a stub page (isStub: true in front matter, or the
# whole locale is stub) it should canonical to the EN equivalent — that's
# what the canonical heuristic in evaluate() checks.
PAGES = [
    ("home",  ""),
    ("about", "about/"),
    ("posts", "posts/"),
    ("app",   "apps/atomic-presence/"),
]

CJK_RE = re.compile(r"[぀-ヿ一-鿿]")  # hiragana, katakana, CJK
GREEN, YELLOW, RED, RESET = "\033[32m", "\033[33m", "\033[31m", "\033[0m"


@dataclass
class Audit:
    label: str            # locale label, e.g. "fr"
    page: str             # page label, e.g. "home", "about", "app"
    url: str
    expected_html_lang: str
    style: str            # "en" / "ja" / "zh" — controls CJK heuristic
    is_stub: bool         # whole-locale stub flag (see config languages.*.toml)
    locale_prefix: str    # e.g. "/fr/" or "/" for en-root
    html: str = ""
    title: str = ""
    description: str = ""
    html_lang: str = ""
    canonical: str = ""
    og_locale: str = ""
    og_image: str = ""
    nav_anchors: list[str] = field(default_factory=list)
    hreflang_count: int = 0
    issues: list[str] = field(default_factory=list)
    fetch_error: Optional[str] = None
    og_image_status: int = 0
    http_status: int = 0


def _fetch(url: str, timeout: float = 15) -> tuple[int, str]:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # match curl --ssl-no-revoke behavior
    req = urllib.request.Request(url, headers={"User-Agent": "audit-i18n/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""


def _head_status(url: str, timeout: float = 10) -> int:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "audit-i18n/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def _first(pat: str, html: str) -> str:
    m = re.search(pat, html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""


def _internal_anchors(html: str, base_path: str) -> list[str]:
    """Collect deduped internal nav anchor texts.

    Blowfish doesn't always wrap the menu in a <header>, so scan the whole
    document and filter to anchors that point at internal paths and have
    short, visible text. The real-locale homepages should yield 4 anchors
    (home logo + apps + support + privacy); stubs missing a menu file fall
    to 2 (just home + apps card link).
    """
    pairs = re.findall(r"<a [^>]*?href=([^\s>]+)[^>]*>([^<]+)</a>", html)
    seen: set[tuple[str, str]] = set()
    out: list[str] = []
    for href, text in pairs:
        href = href.strip("\"'")
        text = text.strip()
        if not text or text in {"↓", "↑"}:
            continue
        if href.startswith("https://github.com") or "mailto:" in href:
            continue
        if not (
            href.startswith("/PeachPitBoat/")
            or href.startswith("https://ccqqder.github.io/PeachPitBoat/")
        ):
            continue
        key = (href, text)
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
    return out


def collect(audit: Audit) -> Audit:
    try:
        audit.http_status, audit.html = _fetch(audit.url)
    except Exception as e:
        audit.fetch_error = repr(e)
        return audit
    if audit.http_status != 200:
        audit.fetch_error = f"HTTP {audit.http_status}"
        return audit
    h = audit.html
    audit.title = _first(r"<title[^>]*>([^<]+)</title>", h)
    audit.description = _first(r'<meta\s+name=["\']?description["\']?\s+content=["\']([^"\']+)["\']', h)
    audit.html_lang = _first(r"<html[^>]*\blang=([\"']?[a-zA-Z\-]+[\"']?)", h).strip("\"'")
    audit.canonical = _first(r'<link\s+rel=["\']?canonical["\']?\s+href=["\']?([^"\'\s>]+)', h)
    # First og:locale wins — that's our explicit xx_YY override
    audit.og_locale = _first(r'<meta\s+property=["\']og:locale["\']\s+content=["\']([^"\']+)["\']', h)
    audit.og_image = _first(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', h)
    audit.nav_anchors = _internal_anchors(h, audit.url.rstrip("/") + "/")
    audit.hreflang_count = len(re.findall(r"rel=alternate hreflang|rel=\"alternate\" hreflang", h))
    if audit.og_image:
        audit.og_image_status = _head_status(audit.og_image)
    return audit


def evaluate(audits: list[Audit]) -> None:
    """Populate `issues` on each audit by cross-comparing locales.

    `audits` should be the list for ONE page (so nav-parity comparisons stay
    within the same page across locales).
    """
    base_nav = max((len(a.nav_anchors) for a in audits if not a.fetch_error), default=0)
    for a in audits:
        if a.fetch_error:
            a.issues.append(f"FETCH FAILED: {a.fetch_error}")
            continue

        # 1. Title language matches locale style
        if a.style == "en" and CJK_RE.search(a.title or ""):
            a.issues.append(f"title contains CJK in en-style locale: {a.title!r}")

        # 2. Description language matches locale style
        if a.style == "en" and CJK_RE.search(a.description or ""):
            a.issues.append(f"description contains CJK: {a.description[:60]!r}")

        # 3. Nav parity vs the richest locale
        if base_nav and len(a.nav_anchors) < base_nav:
            a.issues.append(
                f"nav has {len(a.nav_anchors)} items, expected {base_nav} "
                f"(missing menu file?): {a.nav_anchors}"
            )

        # 4. Hreflang completeness — should be 8 langs + x-default = 9
        if a.hreflang_count != 9:
            a.issues.append(f"hreflang count {a.hreflang_count} (expected 9)")

        # 5. <html lang> matches expected
        if a.html_lang.lower() != a.expected_html_lang.lower():
            a.issues.append(f"html lang={a.html_lang!r} (expected {a.expected_html_lang!r})")

        # 6. og:image must be reachable
        if not a.og_image:
            a.issues.append("og:image missing")
        elif a.og_image_status != 200:
            a.issues.append(f"og:image returns HTTP {a.og_image_status}: {a.og_image}")

        # 7. og:locale present and looks like xx_YY
        if not a.og_locale:
            a.issues.append("og:locale missing")
        elif not re.match(r"^[a-z]{2}_[A-Z]{2}$", a.og_locale):
            a.issues.append(f"og:locale not in xx_YY form: {a.og_locale!r}")

        # 8. Canonical sanity. Real locales must self-canonical; stub
        # locales may either self-canonical (when the page itself is
        # translated, e.g. /fr/apps/atomic-presence/ which has its own
        # markdown with isStub: false) OR canonical to the EN equivalent
        # (when the page is a stub falling back to English). The audit
        # can't read frontmatter, so for stubs we accept either form and
        # only flag canonicals that don't match either valid target.
        def _norm(u: str) -> str:
            return u.rstrip("/") + "/"

        self_url = _norm(a.url)
        en_url = _norm(
            a.url.replace(a.locale_prefix, "/", 1)
            if a.locale_prefix != "/" else a.url
        )
        canon = _norm(a.canonical) if a.canonical else ""

        if not canon:
            a.issues.append("canonical missing")
        elif a.is_stub:
            if canon not in (self_url, en_url):
                a.issues.append(
                    f"canonical={a.canonical} (expected self={self_url} or EN={en_url})"
                )
        else:
            if canon != self_url:
                a.issues.append(f"canonical={a.canonical} (expected self={self_url})")


def _emit_table(page_label: str, audits: list[Audit], use_color: bool) -> None:
    g, r, x = (GREEN, RED, RESET) if use_color else ("", "", "")
    print(f"\n=== Page: {page_label} ===")
    print(f"{'locale':10} | {'title':36} | nav | hflng | og:locale | og:image |")
    print("-" * 86)
    base_nav = max((len(z.nav_anchors) for z in audits if not z.fetch_error), default=0)
    for a in audits:
        if a.fetch_error:
            print(f"{a.label:10} | {r}{a.fetch_error[:70]}{x}")
            continue
        title_ok = not (a.style == "en" and CJK_RE.search(a.title or ""))
        title_cell = f"{g if title_ok else r}{a.title[:34]:36}{x}"
        nav_ok = len(a.nav_anchors) >= base_nav
        nav_cell = f"{g if nav_ok else r}{len(a.nav_anchors)}{x}  "
        hf_ok = a.hreflang_count == 9
        hf_cell = f"{g if hf_ok else r}{a.hreflang_count}{x}    "
        ogl_ok = bool(re.match(r"^[a-z]{2}_[A-Z]{2}$", a.og_locale or ""))
        ogl_cell = f"{g if ogl_ok else r}{a.og_locale or '-':<7}{x}  "
        ogi_ok = a.og_image_status == 200
        ogi_cell = f"{g if ogi_ok else r}{a.og_image_status or 'no':<3}{x}     "
        print(f"{a.label:10} | {title_cell} | {nav_cell} | {hf_cell} | {ogl_cell} | {ogi_cell} |")


def emit(by_page: dict[str, list[Audit]]) -> None:
    use_color = sys.stdout.isatty()
    g, r, x = (GREEN, RED, RESET) if use_color else ("", "", "")

    for page_label, audits in by_page.items():
        _emit_table(page_label, audits, use_color)

    # Aggregate issues across all (locale × page) combinations.
    all_audits = [a for batch in by_page.values() for a in batch]
    issue_audits = [a for a in all_audits if a.issues]
    total_issues = sum(len(a.issues) for a in all_audits)
    print()
    if total_issues == 0:
        print(f"{g}All checks passed across {len(all_audits)} (locale × page) combinations.{x}")
        return
    print(f"{r}{total_issues} issue(s) across {len(issue_audits)} (locale × page) combination(s):{x}")
    for a in issue_audits:
        print(f"\n  [{a.label} / {a.page}]")
        for issue in a.issues:
            print(f"    - {issue}")


def main() -> int:
    # Windows consoles often default to cp950/cp1252; force UTF-8 so CJK in
    # titles renders correctly in the report.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Cross-locale i18n audit")
    ap.add_argument("--base-url", default=DEFAULT_BASE,
                    help=f"Site base URL (default: {DEFAULT_BASE})")
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 if any locale has issues (for CI)")
    args = ap.parse_args()

    base = args.base_url.rstrip("/")
    by_page: dict[str, list[Audit]] = {}
    for page_label, page_path in PAGES:
        batch: list[Audit] = []
        for lbl, prefix, hlang, style, is_stub in LOCALES:
            url = base + prefix + page_path
            batch.append(Audit(
                label=lbl, page=page_label, url=url,
                expected_html_lang=hlang, style=style,
                is_stub=is_stub, locale_prefix=prefix,
            ))
        by_page[page_label] = batch

    all_audits = [a for batch in by_page.values() for a in batch]
    with ThreadPoolExecutor(max_workers=16) as ex:
        futures = {ex.submit(collect, a): a for a in all_audits}
        for fut in as_completed(futures):
            fut.result()

    for batch in by_page.values():
        evaluate(batch)
    emit(by_page)

    if args.strict and any(a.issues for a in all_audits):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
