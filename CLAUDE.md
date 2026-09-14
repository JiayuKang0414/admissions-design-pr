# Claude Code — Admissions Design

This is the **Admissions design project**. It builds on the design-system page builder (vendored as a submodule at `page-builder/`).

## Where to find things

| What | Location |
|---|---|
| Slash commands | `page-builder/.claude/commands/*.md` |
| Layout/spacing/component rules | `page-builder/RULES.md` |
| Component slots & attributes | `page-builder/registry/` |
| Critical CSS (canonical) | `page-builder/styles/critical.css` |
| Skeleton + inlined CSS | `page-builder/TEMPLATE.html` |
| Layout HTML patterns | `page-builder/LAYOUT-PATTERNS.md` |
| Generic page-builder overrides | `page-builder/OVERRIDES.md` |
| **Admissions-specific overrides** | `OVERRIDES.md` (this repo) |

The page-builder's own `CLAUDE.md` (`page-builder/CLAUDE.md`) defines the canonical rules — read it. This file layers admissions-specific guidance on top.

## Output paths

Pages are organised by site section, one directory per section, with the section's
landing page as `index.html` so `/pages/<section>/` serves it:

```
pages/
├── index.html                               site home (stays at the top)
├── know-before-you-go.html                  section-less interior page (Layout B)
├── academics/
│   ├── index.html                           Academics landing
│   ├── programs.html
│   ├── colleges-schools.html
│   └── interest-<slug>.html
├── student-life/index.html
├── how-to-apply/
│   ├── index.html
│   ├── freshman-applicants.html
│   └── transfer-applicants.html
├── personas/
│   └── prospective-students.html            audience landing pages
├── admission-representatives/
│   ├── index.html                           the 24-person directory
│   ├── search.html                          same directory, filterable (CMS person-index pattern)
│   └── <first-last>.html                    one profile page per rep
├── tuition/index.html
└── calendar/index.html
```

`personas/` and `admission-representatives/` have no `data-child-ref` group in
`shared/header.html`, so their pages open the mobile drawer at the top level
rather than on a section — correct until the section earns a nav item.

- New admissions pages → `pages/<section>/<page-name>.html`; a new section starts with its own `index.html`
- New admissions images → `images/academics/`, `images/admissions/`, `images/calendar/`, or a new `images/<page>/` folder per page
- Briefs / source notes → `briefs/<page-name>.md`

### Depth: never hard-code `../`

Pages sit at two different depths (`pages/index.html` vs
`pages/academics/programs.html`), so a fixed `../` prefix is wrong on half of
them. Anything shared across pages — `shared/header.html`, `shared/footer.html`,
and the image paths in `briefs/*-data.json` — writes its paths **repo-root-relative
behind a `{{ROOT}}` token**:

```html
<img src="{{ROOT}}images/logos/admissions-logo.svg" />
<a href="{{ROOT}}pages/academics/programs.html">All Programs</a>
```

`scripts/_chrome.py` expands `{{ROOT}}` to the right number of `../` for the page
being written (`depth_of(path)` → 1 for `pages/index.html`, 2 for anything in
a section folder). Generated pages resolve any remaining tokens from their data
just before writing. A page that moves between directories is then a path change
and nothing else.

Inside a single page's own body, ordinary relative paths are fine — they just have
to match that page's depth (`../../images/...` from a section folder).

Do **not** write to `examples/` or `test/` — test/qa fixtures live in the page-builder repo, and demo/example pages live in the separate `page-builder-examples` repo, not here.

## Image paths

- **Admissions-owned** (logos, page-specific photography): `../images/...`
- **Shared library** (large/small/medium campus, people, events, default): `../page-builder/images/large/...` etc.
- **Sitewide chrome art** (art reused across pages rather than owned by one): `images/shared/` — currently just `interior-hero-pattern.png`, the interior hero graphic

When `images-index.json` is needed, read `page-builder/images/images-index.json`.

### Image optimization scope

When shrinking oversized images (the `/optimize-images` skill or ad-hoc), only touch **static** JPG/PNG/WebP. **GIFs, animated WebPs, and video files are out of scope** — don't resave or report on them (resampling breaks animation, and they need dedicated tooling). Exclude `.gif` and video extensions from scans, and check `n_frames > 1` on any WebP before touching it. This rule is also baked into `~/.claude/commands/optimize-images.md`.

## Interior page layouts

Every interior page (anything that is not a section landing page) uses **one of
exactly two layouts**. They share the same hero and breadcrumb; they differ only
in whether the left nav is present and, consequently, which horizontal lock the
content area sits in.

Reference pages:

| Layout | Reference |
|---|---|
| A — with left nav | [`pages/tuition/frederick-douglass-scholarship.html`](pages/tuition/frederick-douglass-scholarship.html) |
| B — no left nav | [`pages/know-before-you-go.html`](pages/know-before-you-go.html) — recreates `https://admissions.umd.edu/page/know-before-you-go` |

### The shared hero — same on both layouts

Interior pages do **not** get a photographic hero. They get the minimal hero,
dark, with the UMD chevron pattern in the image slot and the **parent page's
name in the eyebrow**:

```html
<section>
  <umd-element-hero-minimal data-theme="dark">
    <p slot="eyebrow">Tuition &amp; Aid</p>
    <h1 slot="headline">Frederick Douglass Scholarship</h1>
    <img slot="image" src="{{ROOT}}images/shared/interior-hero-pattern.png" alt="" />
  </umd-element-hero-minimal>
</section>
```

- **The graphic is `images/shared/interior-hero-pattern.png`** (2602×1022 PNG).
  It is sitewide chrome for interior pages, not page art, which is why it lives
  in `images/shared/` and not in a per-page folder. *(It was
  `images/tuition/ff-pattern-hero.png` until 2026-09-14 — that path is dead.)*
- **`alt=""` is required.** The pattern is decoration; an empty alt keeps it out
  of the accessibility tree so the `<h1>` is the first thing announced.
- **The eyebrow is the parent page**, i.e. the section landing page the
  breadcrumb's last link points at — `Tuition & Aid` for a page under
  `pages/tuition/`, `How to Apply` for one under `pages/how-to-apply/`. It is
  not a category, a tagline, or the page's own name.
- `data-theme="dark"` is not optional. The pattern graphic is drawn for the
  dark panel and has no contrast on the light or maryland themes.

### Layout A — with left nav

`umd-layout-space-horizontal-larger` (1600px max-width, 64px side padding at
≥1200px) wrapping `umd-layout-space-columns-left`: a 242px `umd-element-nav-slider`
sidebar plus the content column, which is capped at 800px for reading measure.

```html
<!-- breadcrumb: its own lock, matching the content lock -->
<div class="umd-layout-space-horizontal-larger umd-layout-space-vertical-interior">
  <umd-element-breadcrumb>…</umd-element-breadcrumb>
</div>

<div class="umd-layout-space-horizontal-larger">
  <div class="umd-layout-space-columns-left">
    <div id="umd-shell-sidebar-container">
      <umd-element-nav-slider>…</umd-element-nav-slider>
    </div>
    <div id="umd-shell-content" class="max-w-[800px]">
      <section class="umd-layout-space-vertical-interior">…</section>
    </div>
  </div>
</div>
```

Measured at a 1280px viewport: lock 1280 → columns 1152 → sidebar 242 at x=64,
content 790 at x=426.

**The sidebar is page content, not shared chrome.** It mirrors the matching
`data-child-ref` group in `shared/header.html`, but `scripts/_chrome.py` does
not stamp it — write its `data-active` / `data-selected` by hand.

Use layout A when the page belongs to a section that has a real sibling set worth
navigating (`tuition`, `how-to-apply`, `academics`, `student-life`).

### Layout B — no left nav

Same hero, same breadcrumb, **no sidebar and no `umd-layout-space-columns-left`**.
The content area uses a different lock:

> **`umd-layout-space-horizontal-normal`** (1280px max-width, 64px side padding
> at ≥1200px → content box caps at 1152px).

```html
<div class="umd-layout-space-horizontal-normal umd-layout-space-vertical-interior">
  <umd-element-breadcrumb>…</umd-element-breadcrumb>
</div>

<div class="umd-layout-space-horizontal-normal">
  <section class="umd-layout-space-vertical-interior">…</section>
</div>
```

Use layout B for one-off pages with no meaningful sibling set — the standalone
informational page that hangs off the site rather than off a section.

**A section-less page is written at the top of `pages/`, not in a directory of
its own** — `pages/know-before-you-go.html`, alongside `pages/index.html`. Don't
invent a section folder with no `index.html` to justify it. `_chrome.py` then
finds no section ref for the path and the mobile drawer opens at its top level,
which is correct.

**Do not use `-larger` here.** Without the 242px sidebar absorbing the left edge,
a 1600px lock puts content at a width nothing else on the site sits at, and the
breadcrumb and body copy stop lining up with the rest of the page stack.

**Four things that follow from the narrower lock and the missing sidebar:**

1. **Section intros: `umd-element-section-intro`, not `-wide`.** RULES §11 picks
   the variant from the lock, not the page — `-wide` over `-normal` spans
   further than the content beneath it.
2. **The `-larger` CSS augmentation does not apply.** Both `critical.css` §3 and
   the per-page §3 block set `position: relative; container-type: inline-size;
   isolation: isolate` on `.umd-layout-space-horizontal-larger` **only**. A
   watermark or a `@container`-driven component inside a `-normal` lock has no
   containing block or query container. Add the same three properties to the
   `-normal` rule on that page if you need either.
3. **Rich text needs no page-level measure — the DS already caps it.**
   `element.min.css` ships

   ```css
   :is(.umd-text-rich-advanced,.umd-rich-text) p,  /* + ul, ol, pre, blockquote */
   { max-width: 960px; }
   ```

   and that rule sets `max-width` and **nothing else — no auto margins** — so
   copy caps at 960px **in place**, flush to the left edge of the lock, while
   the card grids and media still use the full 1152px content box. Do not add a
   narrower page-level cap: it only fights the design system. (Layout A's 800px
   `#umd-shell-content` cap is a *column* width for the sidebar layout, not a
   measure to copy into Layout B.)
4. **`umd-layout-space-vertical-interior-child` is margin-BOTTOM only** (32px,
   margin-top 0). It spaces an `<h2>` away from the content it introduces, but
   gives nothing to an element that *follows* a block of copy — a sub-heading or
   a CTA row set after rich text collapses onto the paragraph above it and reads
   as part of it. There is no `mt-*` utility to reach for: `mt-md` / `mt-lg` /
   `mt-xl` all compute to 0 in this bundle set, so this needs a page-level rule.
   Layout A hides the problem because its sections are shorter and divider-led.

### What is the same on both

- The `noindex` meta pair, the shared header/footer regions, and the access gate
  — all spliced by `scripts/build-chrome.py`, identical on every page.
- `umd-layout-space-vertical-interior` on each `<section>` — interior pages use
  the `*-interior` spacing scale. `umd-layout-vertical-landing` is landing-page
  only.
- The breadcrumb's lock always matches the content lock. Don't mix `-larger`
  breadcrumb with `-normal` content.
- The closing `umd-element-banner-promo` "stay connected" block, per the
  sitewide page-closer convention.

## Shared chrome and reference pages

Every page within a single design project must use the **same site header, navigation, logo, and footer**. Pages in this project should look like a coherent site — they should not invent their own chrome, nav items, or logo treatment.

### The chrome lives in `shared/` — never copy it between pages

| File | What it holds |
|---|---|
| `shared/header.html` | Header stack: `umd-element-navigation-utility` + `umd-element-navigation-header` with the project nav items and logo |
| `shared/footer.html` | `umd-element-footer data-display="visual"` |
| `shared/chrome.css` | CSS companions the chrome markup depends on (see below) |
| `shared/chrome-scripts.html` | Chrome-driven shadow injections (nav-header logo width) |
| `shared/gate.html` | Prototype access gate — head-only `<style>` + `<script>`; blanks the page until a reviewer signs in |

**Edit `shared/`, then run the inliner:**

```bash
python3 scripts/build-chrome.py          # splices shared/ into every page under pages/ (recursively)
python3 scripts/build-chrome.py --check  # exits non-zero if any page is stale (CI-friendly)
```

Each region sits between `SHARED:<key>:START` / `:END` markers in the page. **Do not hand-edit anything between those markers** — the next run overwrites it. On a page that has no markers yet, the script finds the existing chrome by content and wraps it, so adding a new page needs no special setup.

The generated pages (`scripts/build-programs.py`, `scripts/build-colleges-schools.py`, `scripts/build-interest.py`, `scripts/build-calendar.py`, `scripts/build-representatives.py`) emit the *same* blocks via `scripts/_chrome.py`, so running any of them converges on identical bytes — there is no ordering dependency between them.

### Generated pages

| Script | Emits | Data |
|---|---|---|
| `build-programs.py` | `pages/academics/programs.html` | `briefs/programs-data.json` |
| `build-colleges-schools.py` | `pages/academics/colleges-schools.html` | `briefs/colleges-schools-data.json` |
| `build-interest.py [slug]` | `pages/academics/interest-<slug>.html` | `briefs/interests-data.json` + the two above |
| `build-calendar.py` | `pages/calendar/index.html` | `briefs/calendar-data.json` |
| `build-representatives.py [slug]` | `pages/admission-representatives/index.html`, `search.html`, + `<slug>.html` | `briefs/representatives-data.json` |

`build-interest.py` derives the majors grid from the `interests` facet already present on every program in `programs-data.json`, so a new interest page is a data edit (one block in `briefs/interests-data.json`), not a code edit. Run with no argument to rebuild every slug.

`build-representatives.py` works the same way: `representatives-data.json` holds all 24 reps, and the ones carrying `"page": true` get a profile page. Adding the rest is a data edit — flip the flag and re-run. Run with a slug to rebuild one rep without touching the landing page.

**Every region in `shared/` must be emitted by every generator.** `_chrome.keys()` is the list, and `build-programs.py` / `build-calendar.py` assert that their template has a slot for each key — so adding a region to `_chrome.py` breaks those builds until they are wired, which is deliberate. The access gate learned this the hard way: it was originally spliced in by hand, and the next run of `build-programs.py` and `build-calendar.py` silently dropped it, leaving both pages ungated on `main` until it became a proper region (2026-08-31).

Only the content between the header and footer is page-specific.

### ⚠️ Why the CSS and scripts live with the markup

**`page-builder/TEMPLATE.html` does not contain every rule the chrome needs.** Before the extraction these rules sat in a page-specific `<style>` block while the markup was copied from a sibling page — so building a `<head>` from TEMPLATE while copying markup from a page silently dropped them. No console error, no layout break, just unstyled chrome. That happened twice.

| Rule | Why TEMPLATE isn't enough |
|---|---|
| `umd-element-navigation-header div[slot="utility-navigation"] a` | `critical.css` §11's BASE layer styles `.umd-shell-utility-item a`, which never matches this project's plain `<a>` children — they render browser-default blue and underlined without it. Must load **after** the critical block to win at equal specificity. |
| `umd-element-scroll-top[data-layout-fixed="true"]` | Pins to `right:24px; bottom:24px`; the DS default is `right:40px; bottom:10vh`. Opt-in per page, but styled from `shared/` wherever used. |
| `.umd-nav-promo` | The nav dropdown promos. `slot="dropdown-callout"` is projected through a real `<slot>`, so the promo stays in the **light DOM** — the nav-item's shadow CSS cannot reach it, and a bare `<a>` there gets no colour from `critical.css` and renders default blue. Same root cause as the utility-nav row above. |

**Chrome vs. page-level shadow injections.** Only injections driven by the *chrome* belong in `shared/chrome-scripts.html` — currently just the nav-header logo width. The pathway aspect-ratio, banner-promo stacked-actions, call-to-action and card-overlay injections are driven by **page content** and stay in the page that uses them. Don't move them to `shared/`; a page with no `umd-element-pathway` should not carry the pathway injection.

### The mobile drawer is contextual — and its refs are directory names

`umd-element-navigation-header` renders the hamburger **only** when
`slot="primary-slide-links"` is present (`drawer.CreateElement()` returns `null`
otherwise and the header silently collapses to logo-only on mobile — that is how
this project shipped without one). The DS appends the button to the logo column
with no media query, so the hamburger is **persistent at every width**, beside
the desktop nav, as on umd.edu.

All three drawer slots (`primary-slide-links`, `primary-slide-secondary-links`,
`children-slides`) must be **direct children** of the header element — the
component collects them with `:scope > [slot]` — and are **cloned into the shadow
root**, so page CSS cannot style them. Every link's text needs its own `<span>`
or the selected-state underline has nothing to draw on.

The drawer opens on the section the reader is already in. That comes from two DS
attributes which `scripts/_chrome.py` stamps per page while hrefs are still
`{{ROOT}}`-relative:

| Attribute | Where | Effect |
|---|---|---|
| `data-active` | the `children-slides` group for the page's section | drawer opens on that slide, with a Back button to the top level |
| `data-selected` | any drawer link pointing at the page itself | gold underline on the current page |

**The `data-child-ref` / `data-parent-ref` values ARE the section directory names
under `pages/`** (`academics`, `student-life`, `how-to-apply`, `tuition`) — that
coupling is what lets the stamping work without a lookup table. Rename a section
directory and its drawer refs have to follow. A page in no section
(`pages/index.html`) or in a section with no drawer group
(`pages/calendar/`) matches nothing and the drawer opens at its top level, which
is correct.

Because the chrome is now rendered per page rather than per depth,
`_chrome.block(key, page)` / `payload(key, page)` take the **output page path**,
not a depth — `depth_of()` is derived from it.

**When verifying:** assert utility-nav `gap: 24px` **at ≥1024px** — the DS hides the utility slot below desktop, so it measures 0×0 at tablet width and a narrow viewport masks the bug entirely. Also check `umd-element-scroll-top` computes `right/bottom: 24px` and that the nav logo's shadow `max-width` is `320px`. For the drawer, assert the hamburger computes `display: flex` **at desktop too** (it is meant to be persistent) and that the slide carrying `data-active` matches the page's section.

### Projects that don't yet have a reference page

Not every design project will start with an existing `shared/` chrome. In that case, the **first page built establishes it** — make the header/nav/logo/footer choices intentionally, extract them into `shared/` straight away, and treat that as authoritative for every subsequent page in the project.

### The chrome is project-scoped

`shared/` lives in this repo only — never copy this project's chrome into the `page-builder/` submodule, and never assume a different design project (e.g. a future `engineering-design` repo) will share these specific nav items, logos, or footer image. The submodule provides the components; each design project owns its own chrome composition.

That scoping is why `shared/chrome.css` is not upstreamed: the flat-`<a>` utility-nav treatment is *this project's* composition choice, not a design-system default. The one genuinely generic bug it exposed — `critical.css` §11 zeroing the slot gap unconditionally — was fixed upstream instead (`design-system-page-builder` `be3ea6c`).

## Search indexing — every page is `noindex`

Every page under `pages/` carries, immediately after the viewport meta:

```html
<meta name="robots" content="noindex, nofollow">
<meta name="googlebot" content="noindex, nofollow">
```

These are prototypes; none of them should surface in search results.

**A `robots.txt` would not work here.** It is only fetched from the *host* root,
and a GitHub Pages project site is served from `/<repo>/` — a `robots.txt`
committed to this repo never gets read. The meta is the mechanism that actually
applies. The `googlebot` line is a deliberate belt-and-braces duplicate, matching
the treatment on the page-builder's own preview harness.

`page-builder/TEMPLATE.html` does **not** carry the meta (indexing is a project
decision, not a design-system one), so a new hand-written page has to add it.
The generated pages get it from `_chrome.with_robots(head)`, which the four
`build-*.py` scripts apply to the TEMPLATE-derived head — a rebuild cannot drop
it. The helper is idempotent and asserts if TEMPLATE ever loses its viewport
meta anchor.

## Logos

| Slot | Path |
|---|---|
| Header (`umd-element-navigation-header` `slot="logo"`) | `../images/logos/admissions-logo.svg` |
| Footer (`umd-element-footer` `slot="logo"`) | `../images/logos/footer-logo.svg` |
| Fallback (header onerror) | `../images/logos/primary-logo-dark.svg` |

Always include the `onerror` runtime fallback for hotlink-protected URLs (see page-builder/CLAUDE.md).

## Verifying pages in the preview pane

When checking admissions pages in the in-app Browser pane (`mcp__Claude_Browser__*`) against the `admissions-static` dev server, watch for these known quirks:

- **Viewport desync.** A *fresh* tab reports the correct `window.innerWidth` on first measure, but after `location.reload()` or re-`navigate` on the same tab it often sticks at `0` (or a stale width like `375`). When `innerWidth` is `0`, all media queries fail and computed styles read as base/mobile values — this is **not** a CSS bug. Fix: open a fresh tab (and close old ones — there's an ~8-tab cap).
- **Blank screenshots.** `computer{action:screenshot}` frequently returns a blank light-gray image even when the DOM/CSS engine is healthy. Rely on DOM/computed-style assertions via `javascript_tool` for verification, not screenshots.
- **Stale cache.** Navigating to a just-edited page can serve a cached copy. Confirm with `curl` that the dev server serves the change, then navigate with a cache-buster query (`?v=2`) to force a fresh load.

Practical verification recipe: assert on computed styles (9 CSS bundles loaded, `customElements.get(...)` registered, utility-nav gap `24px`, no horizontal overflow) via `javascript_tool` in a fresh tab, rather than trusting screenshots or a reused tab.

## Source of truth hierarchy (admissions)

1. Slash commands in `page-builder/.claude/commands/*.md`
2. `page-builder/RULES.md`
3. `page-builder/registry/`
4. `page-builder/styles/critical.css`
5. `OVERRIDES.md` (this repo) — admissions-specific shadow injections and class overrides
6. `page-builder/OVERRIDES.md` — generic shadow injections (visit-card, banner-promo, etc.)
