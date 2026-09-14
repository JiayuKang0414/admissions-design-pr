# Find Your Community — Layout B page

**Output:** `pages/student-life/find-community.html`
**Source:** https://admissions.umd.edu/student/find-community
**Built:** 2026-09-14

Built on the interior-layout rules in `CLAUDE.md` § Interior page layouts.
It lives under `pages/student-life/` because the live URL is
`/student/find-community`, and it uses **Layout B — no left nav**, because the
source page has none.

## It was built wrong the first time

The first build gave this page a `umd-element-nav-slider` sidebar and the
`-larger` lock, on the reasoning that `student-life` has a sibling set in the
drawer and so "is a Layout A section". **The source page has no left nav** —
its `main` contains no `nav` or `aside`, just a single centred 954px column
(checked directly: `main.querySelectorAll('nav, aside, [class*=sidebar]')`
returns empty at 1440px).

CLAUDE.md's rule was the cause, not a slip: it said to use Layout A whenever
a page sits in a section with "a real sibling set worth navigating" and named
`student-life`. That rule has been rewritten — the layout is a per-page
decision made by the source design, and the drawer group in
`shared/header.html` is about the *mobile* nav and implies nothing about a
desktop sidebar.

## The nav now points at this page

`shared/header.html` had "Find Your Community" pointing at
`https://admissions.umd.edu/student/find-community` in both the desktop dropdown
and the mobile drawer. Both were repointed to
`{{ROOT}}pages/student-life/find-community.html`, which is what lets
`scripts/_chrome.py` stamp `data-selected` on the drawer link for this page —
without it the drawer opens on the right slide but highlights nothing.

That is a `shared/` edit, so `build-chrome.py` rewrote all 26 pages. The only
change on the other 25 is that one href.

## The headline the live page hides

The live page renders its `<h1>` as `.sr-only` and repeats the title as an
`<h2>` at the top of the content column. This page puts the title in the
standard interior hero — `umd-element-hero-minimal data-theme="dark"`, chevron
pattern, eyebrow `Student Life` — and drops the duplicate `<h2>`. One visible
title, one level-one heading.

## The five community blocks: zig-zag columns

The live page floats a 477px image alternately right and left with copy
wrapping beside it. This page uses the zig-zag two-column pattern instead
(`LAYOUT-PATTERNS.md` § *Light background — two-column image + text*): a text
column and a `figure.umd-layout-alignment-block-stacked`, 556px each at 1440px,
alternating which side the image lands on.

Each headline sits OUTSIDE `.umd-text-rich-advanced` — a `umd-sans-*` size
collapses to 18px inside that block (RULES §18).

**The alternation is done with `order`, not by swapping the markup**, which is
what the pattern doc says to do. See OVERRIDES.md § Zig-zag alternation: below
650px the grid collapses to one column, and figure-first markup then stacks the
photo above its own heading. Text stays first in the DOM on all five blocks;
`.fc-media-first > figure { order: -1 }` at 650px+ does the visual swap.

Verified at 1440px — DOM order `div | figure` on all five; visual order
`div|figure`, `figure|div`, `div|figure`, `figure|div`, `figure|div`; columns
556px, equal heights per row. At 375px every block stacks `div then figure`.

The fifth block (Alumni Association) is image-left like the fourth rather than
continuing the alternation. That matches the live page, and the card section
sitting between them resets the rhythm visually.

## Component mapping

| Live page | This page |
|---|---|
| `h1.sr-only` + `h2` repeat | `umd-element-hero-minimal`, eyebrow `Student Life` |
| `umd-breadcrumb` | `umd-element-breadcrumb`, own `-normal` lock |
| *(no left nav)* | *(none — Layout B)* |
| 5 × floated `umd-image-caption` + copy | 5 × zig-zag `umd-layout-grid-gap-two` + `figure` |
| 2 × `umd-card` (OMSE, MICA) | 2 × `umd-element-card` in `umd-layout-grid-gap-two` |
| `umd-admissions-resources` (1 item) | 1 × `umd-element-card-icon` (light, red chevron) |
| `.footer-cta` | `umd-element-banner-promo` (default gold page closer) |

The OMSE and MICA cards carry supporting copy, so standard cards rather than
text-only overlay link cards (`LAYOUT-PATTERNS.md` § Link Cards Grid). Neither
has a source image, so no image slot. The live page gives both the category
"Multicultural & Faith Programs"; that became the section `h2` instead of a
repeated eyebrow on each card.

## Images

Downloaded rather than hotlinked. All five are under both optimization
thresholds (<1MB, <4000px), so none were resaved.

| File | Size |
|---|---|
| `find-community/do-good-students-chatting.jpg` | 688×456, 29KB |
| `find-community/international-students-walking.jpg` | 688×456, 65KB |
| `find-community/veteran-services-dining.jpg` | 800×530, 67KB |
| `find-community/alumni-cup.jpg` | 954×500, 92KB |
| `shared/frederick-douglass-statue.jpg` | 1454×931, 219KB |

**The statue photo was already in the repo.** The copy downloaded for this page
was byte-identical (md5 `6d6a6555…`) to the one the Frederick Douglass
Scholarship page had been using at `images/tuition/frederick-douglass-statue.jpg`.
Rather than commit 219KB twice, it moved to `images/shared/` and both pages now
reference it there. Referencing it across section folders
(`../tuition/…` from `student-life/`) was the alternative and was rejected: it
would have left a silent coupling where reorganising the tuition page's images
breaks this one.

## Verified

- Layout B geometry at 1440px: `-normal` lock 1280px wide, content box 1152px.
  No `#umd-shell-sidebar-container`, no `.umd-layout-space-columns-left`, no
  `umd-element-media-inline`, no `-larger` lock in the markup.
- Zig-zag columns 556px each, equal heights per row; alternation by `order`
  with a constant `div | figure` DOM order.
- Drawer: `data-active` on the `student-life` group and `data-selected` on this
  page's link in the shared drawer.
- Type: section `h2`s 32px, body 18px/400.
- Cards 2-up, equal heights. The lone Resources icon card renders 556px at
  x=137 — same track as the OMSE card above it. No broken images. Horizontal
  overflow 0.
- Mobile (375px): everything stacks to 327px, every block leads with its
  heading, overflow 0.
- `build-chrome.py --check` → 0/26.
- Console: the two `process is not defined` errors from the CDN bundle, same as
  every other page in the project.

## The lone Resources card stays on the 2-up grid

The live page has exactly one resource, and a single `umd-element-card-icon`
left to itself stretches the full 1152px content box — airy and out of step with
the two-up card row above it. It is wrapped in `umd-layout-grid-gap-two` instead.
That class is `repeat(2, 1fr)` at 650px+, so a lone child occupies the first
track and the second stays empty: the card renders 556px at x=137, the same
column width and left edge as the OMSE card above it. A second resource would
drop into place with no markup change.
