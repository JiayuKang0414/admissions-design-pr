# Student Support & Safety — Layout B page

**Output:** `pages/student-life/student-support.html`
**Source:** https://admissions.umd.edu/student/student-support
**Built:** 2026-09-14

## Layout: B, checked not inferred

Per `CLAUDE.md` § *Which layout — read the source page, don't infer it*, the
source was checked first: `main.querySelectorAll('nav, aside, [class*=sidebar]')`
returns empty at 1440px and the content is a single centred 954px column. **No
left nav → Layout B**, `-normal` lock, no `umd-layout-space-columns-left`.

This is the second `student-life` page in a row to come out Layout B, which is
the point of the corrected rule: the section's drawer group says nothing about
whether a page has a desktop sidebar.

Unlike `find-community.html`, this page has a **visible** `<h1>`
(`headline-one-san-serif`, not `.sr-only`), so the hero is carrying a heading
the source also showed rather than one it hid.

## Structure

| Live page | This page |
|---|---|
| `h1.headline-one-san-serif` | `umd-element-hero-minimal`, eyebrow `Student Life` |
| `umd-breadcrumb` | `umd-element-breadcrumb`, own `-normal` lock |
| `.rich-text.intro` | `umd-element-section-intro include-separator`, in a 992px lock |
| Academics / Wellness / Safety — floated image + list | 3 × zig-zag `umd-layout-grid-gap-two` + `figure` |
| Transportation & Parking — no image | full-width `.umd-text-rich-advanced` |
| *(no Resources section)* | — |
| `.footer-cta` | `umd-element-banner-promo` (default gold page closer) |

The source floats images left / right / left across the first three sections.
That order is preserved, done with `order` rather than by swapping the markup
(OVERRIDES.md § *Zig-zag alternation*) — text stays first in the DOM on all
three, so every block still leads with its heading when the grid collapses at
650px. Verified: stack order `div then figure` on all three at 375px.

**Transportation & Parking is deliberately not a zig-zag block.** The source has
no image for it, and inventing one to keep the rhythm would be fabricating
content. It runs full width; its `p`/`ul` cap themselves at 960px via
`element.min.css`.

## The portrait image needed a uniform crop

Two of the three photos are landscape (1920×1080 and 1200×630); the Safety one
is portrait (600×760). Left at its intrinsic ratio it rendered **704px tall** in
a 556px column against a 313px text column — the block was mostly dead space,
and it broke the rhythm with the 313px and 369px blocks either side.

The zig-zag figure images now carry `aspect-ratio: 16/9` + `object-fit: cover`.
That is a no-op for the two landscape sources and crops only the portrait one,
whose subject — the blue-light emergency pillar — runs the full height of the
frame and survives a centre crop. Same reasoning as the pathway 6:5 cap in
OVERRIDES.md: one ratio across a repeated component.

After: all three images 556×313, ratio 1.778; block heights 313 / 369 / 393.

## Images

Downloaded rather than hotlinked. All three under both optimization thresholds
(<1MB, <4000px), so none were resaved.

| File | Size |
|---|---|
| `academics-engineering-lab.jpg` | 1920×1080, 363KB |
| `wellness-health-center.jpg` | 1200×630, 154KB |
| `safety-blue-light.jpg` | 600×760, 62KB |

**The Safety image needed its `@` URL-encoded.** The CDN path is
`safety@2x.jpg`; requesting it with a literal `@` returns
`{"name":"HashException","status":403,"message":"Invalid security hash"}`.
`safety%402x.jpg` with the same signature returns 200. Worth knowing for any
other asset with a `@2x` suffix.

## The nav now points at this page

`shared/header.html` had "Student Support & Safety" pointing at the live site in
both the desktop dropdown and the mobile drawer; both now point at
`{{ROOT}}pages/student-life/student-support.html`, which is what lets
`_chrome.py` stamp `data-selected`. That is a `shared/` edit, so all 27 pages
were rebuilt and the only change on the other 26 is that one href.

## Verified

- Layout B geometry at 1440px: `-normal` lock 1280px wide, no sidebar.
  Section-intro lock 992px at x=217, accent line present.
- Zig-zag: visual order `figure|div`, `div|figure`, `figure|div`; DOM order
  `div|figure` on all three. Images 556×313, ratio 1.778.
- All four section `h2`s 32px.
- Drawer: `data-active` on `student-life`, `data-selected` on this page's link.
- No broken images. Horizontal overflow 0 at 1440px and 375px.
- Mobile: everything stacks to 327px, every block leads with its heading,
  images keep the 16:9 ratio.
- `build-chrome.py --check` → 0/27.
- Console: the two `process is not defined` errors from the CDN bundle, same as
  every other page in the project.

## Duplicated page CSS — worth consolidating

`.ss-lock-992` and `.ss-media-first` are this page's copies of rules already
written as `.kbyg-lock-992` on `know-before-you-go.html` and `.fc-media-first`
on `find-community.html`. The project convention is page-scoped prefixes
(`.fa-*`, `.wta-*`, `.cal-*`), so that is what they are — but both rules are now
on their second page each and will recur on every Layout B page that uses a
section intro or a zig-zag. There is no shared home for page-layout utilities in
this repo (`shared/chrome.css` is specifically for chrome the header/footer
depends on), so promoting them means either a new shared stylesheet here or a
change to `critical.css` in the page-builder submodule. Flagging rather than
deciding.
