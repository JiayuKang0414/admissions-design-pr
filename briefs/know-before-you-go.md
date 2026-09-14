# Know Before You Go — Layout B reference page

**Output:** `pages/know-before-you-go.html`
**Source:** https://admissions.umd.edu/page/know-before-you-go
**Built:** 2026-09-14

This page exists twice over: it is a recreation of a real live page, and it is
the **reference implementation of interior Layout B** (no left nav) described in
`CLAUDE.md` § Interior page layouts. `pages/tuition/frederick-douglass-scholarship.html`
is the Layout A (with left nav) reference.

## Why it sits at the top of `pages/`

Layout B is for pages with no meaningful sibling set. This one has none: the live
URL is `/page/know-before-you-go` (not under a section), and its breadcrumb runs
Home → Know Before You Go directly. So it is written at `pages/know-before-you-go.html`,
depth 1, alongside `pages/index.html`, rather than inventing a `pages/visit/`
directory with no `index.html` to justify it.

Two consequences, both correct and both verified:

- No drawer slide carries `data-active` — `scripts/_chrome.py` finds no section
  ref for this path, so the mobile drawer opens at its top level.
- Being depth 1 rather than depth 2, it exercises a different `{{ROOT}}`
  expansion than every other hand-written interior page. `build-chrome.py`
  handled it with no special-casing.

## Component mapping

| Live page | This page |
|---|---|
| `h1.headline-one-san-serif` on a plain white band | `umd-element-hero-minimal data-theme="dark"` + chevron pattern, eyebrow `Visit UMD` |
| `umd-breadcrumb` | `umd-element-breadcrumb`, own `-normal` lock |
| `.rich-text.intro` (lede) | `umd-element-section-intro`, text-only — no headline slot |
| `.rich-text.intro` (What to Do) | `.umd-text-rich-advanced` (DS caps its `<p>` at 960px) |
| `hr.thick` + `h2.headline-three-san-serif` | `hr.umd-text-divider` + `h2.umd-sans-extralarge-bold.text-black` (32px desktop / 22px mobile) |
| 3 × `umd-card` (accommodation) | 3 × `umd-element-card` in `umd-layout-grid-gap-three` |
| `h2.headline-four-san-serif` sub-heads | `h3.umd-sans-larger-bold.text-black`, paired in a 2-column grid |
| `a.call-to-action-block` | `umd-element-call-to-action data-display="secondary"` |
| 2 × `umd-image-caption` (campus maps) | 2 × `umd-element-media-inline` in `umd-layout-grid-gap-two` |
| `umd-admissions-resources` (2 items) | 2 × `umd-element-card-icon` (light) in `umd-layout-grid-gap-two` |
| contact + sign-off paragraphs | `umd-element-banner-promo data-theme="dark"` |
| `.footer-cta` | `umd-element-banner-promo` (default gold, sitewide page closer) |

**Resources are icon cards**, matching the Resources treatment on
`pages/academics/index.html` — but the light variant, so no `data-theme` and the
red-chevron `icon-link.svg` rather than the dark page's `icon-link-dark.svg`.

The accommodation cards are standard cards, not text-only overlay link cards:
they carry supporting copy, which is the condition `LAYOUT-PATTERNS.md` § Link
Cards Grid gives for choosing `umd-element-card`. They use
`data-visual-bordered="true"` and `data-visual-image-aligned="true"` so three
differently-proportioned source photos crop to one ratio. Both must be the
literal string `"true"` — a bare attribute is inert (`registry-cards.json`).

**The two campus maps are stacked, not paired** — `umd-layout-grid-gap-stacked`
(1fr, 40px gap at ≥1024px). Side by side they rendered 556px wide and the lot
numbers and building inventory were unreadable; stacked they take the full
1152px content box.

## What to Do is a zig-zag, image right

`LAYOUT-PATTERNS.md` § *Light background — two-column image + text*:
`umd-layout-grid-gap-two` with the text column first and
`figure.umd-layout-alignment-block-stacked` second. Left column is headline →
`<hr>` → body; right column is
`GreaterCollegePark_09182025_DS_7980_1920x1080.webp` (1920×1080, 252KB static
WebP — under both optimization thresholds, untouched).

Measured at 1440px: grid 1152 at x=137, text column 556 at x=137, figure 556 at
x=733, image 556×313, both columns 313px tall. Mobile stacks to one 327px column.

**The headline sits OUTSIDE `.umd-text-rich-advanced`** — a `umd-sans-*` size
collapses to 18px inside that block (RULES §18), so an `h2` moved inside would
silently lose its 32px.

**Every rule on this page sits ABOVE its heading as `hr.umd-text-divider`.** The
zig-zag pattern in LAYOUT-PATTERNS.md puts a bare `<hr>` *inside* the rich-text
block and needs a page rule to give it a border (the inlined critical CSS leaves
`<hr>` borderless, so the UA's inset ~2px grey shows through). Using the DS's own
`umd-text-divider` instead — already 1px solid #000 with 24px below — means that
page rule is unnecessary, and the page comment says so rather than leaving dead
CSS behind.

⚠️ **The "What to Do" rule is 556px, not 1152px**, because it sits inside the
zig-zag's left column. `Where to Stay` and `Resources` open with a full-width
rule. Within the section it reads consistently — it is parallel with the
column-width rules above Self-Guided Tour and Transportation & Parking — but the
three section heads are not identical across the page. Worth a look.

## Sub-topics are paired columns

Self-Guided Tour and Transportation & Parking sit side by side in
`umd-layout-grid-gap-two` rather than stacking — 556px each at x=137 / x=733,
stacking to one 327px column at mobile. Each carries its own `hr.umd-text-divider`
above its heading. Headings are `umd-sans-larger-bold`, which renders 22px/700 at
desktop against 18px/400 body.

**At mobile `umd-sans-larger-bold` drops to 18px** — the same size as the body
copy, so the sub-heads are distinguished by weight alone. That is how the class
behaves by design, not a bug, but it is the reason these are `h3`s under a 32px
`h2` rather than a third distinct size.

## Contact and sign-off: black banner promo

The "Have questions about your visit?" and "Safe travels" lines are a
`umd-element-banner-promo data-theme="dark"` rather than two more paragraphs.
`headline` and `text` are both required slots (`registry-alerts.json`), so the
question becomes the headline and the contact line plus sign-off become the text.

It carries a **Visitor Center** CTA in `slot="actions"`, `data-display="primary"`
plus `data-theme="dark"` — theme does not cascade across a component boundary
(RULES §14), so the dark attribute has to be repeated on the CTA. It renders
170×44, `rgb(226,24,51)` on white text, inside the component's own
`.banner-promo-actions` wrapper. The inline "Visitor Center" link was removed
from the body copy when the CTA was added — two links to the same URL in one
small banner is noise; the `mailto:` link stays.

**The component handles the whole dark treatment itself — no page CSS.** Measured
in its shadow root: `.banner-promo-container` paints `rgb(0,0,0)`; the headline
takes `umd-sans-extralarge-dark` (white, 32px, uppercase); the copy takes
`umd-text-rich-simple-dark` (white); and **both inline links render white with a
white 1px gradient underline**, which is what RULES §34 asks for. This is the
usual dark-theme trap — a link that stays black and disappears — and this
component does not have it.

The page closer below is the same component in its default gold, so the two read
as a pair rather than a repeat.

⚠️ **Reading order:** the sign-off ("Safe travels, and we look forward to seeing
you on campus!") now lands *before* the two campus maps, because that is the
order the live page uses. Closing the section with the banner instead — maps
first, banner last — would read more naturally. Left as-is pending a call.

## The lede is a text-only section intro

The opening paragraph is `umd-element-section-intro` with a `text` slot and **no
`headline` slot** — the `<h1>` is already in the hero, so a headline here would
repeat it. RULES §11 picks the small variant over `-wide` because the lock is
`-normal`.

It carries `include-separator`, which draws the red accent line above the text —
verified to work with no headline present: a `::before` on
`.intro-default-container`, 2px × 64px, `rgb(226, 24, 51)`, with 80px of top
padding to clear it.

It renders 22px / 700 / #000, centered, held in a **992px lock** (`.kbyg-lock-992`)
— x=217, w=992 inside the 1152px content box, which is what makes it read as a
lede rather than a first paragraph. The lock is a bare `max-width` and **not**
`.umd-layout-space-horizontal-small`: that class carries its own 64px of side
padding, which would compound with the `-normal` lock it already sits inside and
pull the intro in to 864px. **No page CSS is involved**: the registry's
CAUTION that headline-less text renders at a flat 18px/400 was verified at
v1.18.12 and is stale at the 2.0.0 this project pins. See OVERRIDES.md
§ `umd-element-section-intro` headline-less.

## Reading measure: none, on purpose

An earlier draft of this page carried a page-level `max-width: 720px` on its copy
blocks. That was wrong and has been removed. `element.min.css` already ships

```css
:is(.umd-text-rich-advanced,.umd-rich-text) p,  /* + ul, ol, pre, blockquote */
{ max-width: 960px; }
```

and **that rule sets `max-width` and nothing else — no auto margins** — so the
copy caps at 960px *in place*, flush to the left edge of the lock, rather than
centring within it. Verified on the built page: every rich-text `<p>` computes
`max-width: 960px`, `margin-left/right: 0`, and renders 960px wide at the same
x as the headings and dividers above it.

A narrower page-level cap only fights the design system. Layout A's 800px
`#umd-shell-content` cap is a *column width for the sidebar layout*, not a
measure to copy into Layout B.

## Page-level CSS

### `.kbyg-top-space { margin-top: 48px }`

`umd-layout-space-vertical-interior-child` is **margin-bottom only** (32px,
margin-top 0). It spaces an `<h2>` away from the content it introduces, but gives
nothing to an element that *follows* a block of copy — so the two sub-headings
and the campus-map CTA collapsed onto the paragraph above them and read as part
of it. There is no `mt-*` utility to reach for: `mt-md` / `mt-lg` / `mt-xl` all
compute to 0 in this bundle set.

### `.kbyg-lock-992`

A bare `max-width: 992px` + auto margins for the section intro — see above for
why not `-horizontal-small`.

### Three zig-zag rules, copied from LAYOUT-PATTERNS.md

`min-width: 0` on the grid children (otherwise the image's min-content forces its
track to the intrinsic 1920px and unbalances the columns), `width: 100%; height:
auto` on the figure image, and the 1px black `<hr>`.

## Images

Downloaded rather than hotlinked, per project convention. The CDN signs every
transform URL, so **only the sizes the live page itself requests are obtainable** —
an unsigned request for the original returns 401.

| File | Source size | Note |
|---|---|---|
| `hotel-at-umd.jpg` | 1920×1080, 341KB | fine |
| `cambria-hotel.jpg` | 259×194, 16KB | ⚠️ low-res |
| `marriott-conference-center.jpg` | 204×116, 8KB | ⚠️ low-res |
| `campus-map-page-1.jpg` | 4000×2589, 1334KB → 2000×1294, 540KB | downscaled |
| `campus-map-page-2.jpg` | 4000×2637, 1493KB → 2000×1318, 599KB | downscaled |

**The two low-res hotel photos are a content-supply gap, not a build defect.**
The live site serves them at 259×194 and 204×116 and will not sign a larger
transform, so they render soft in a 363px card. `data-visual-image-aligned`
crops them to the row ratio, which hides most of it, but a real build of this
page needs proper assets from the client. Do not "fix" this by upscaling or by
substituting unrelated stock photography of different buildings.

The two campus maps were over the project's optimization threshold (>1MB and
4000px wide) and were resaved at 2000px / q82 progressive, which keeps them
legible when opened while halving the weight.

## Verified (1440×900 desktop unless noted)

- Breadcrumb lock and content lock both x=80, w=1280 — aligned, `max-width: 1280px`,
  `padding: 64px`, content box 1152px.
- No `#umd-shell-sidebar-container`, no `.umd-layout-space-columns-left`, no
  `-larger` lock anywhere on the page.
- All three section `h2`s compute 32px / 700 at desktop, 22px at mobile.
- Section intro: `.kbyg-lock-992` and the component host both x=217 w=992;
  accent line present as a 2px × 64px `#e21833` `::before`.
- Zig-zag: text 556 at x=137, figure 556 at x=733, both 313px tall.
- Sub-topic columns: 556 at x=137 and x=733, both 214px tall; `h3`s 22px/700.
- Dark banner promo: upgraded, container background `rgb(0,0,0)`, headline and
  body white, the inline link white with a white gradient underline, and the
  Visitor Center CTA 170×44 red-on-white.
- Section spacing: `umd-layout-space-vertical-interior` resolves to **80px at
  desktop, 56px at mobile**. Measured gaps at 1440px — column pair → map CTA
  80px, map CTA → black banner 80px, black banner → maps 80px.
- Interactive Campus Map CTA is `data-display="primary"`.
- Five `hr.umd-text-divider`: 1152px above Where to Stay and Resources, 556px
  above What to Do, Self-Guided Tour and Transportation & Parking.
- Accommodation row: 3 × 363px, all three 547px tall. Resources icon cards:
  2 × 556px, both upgraded, `data-theme` absent (light).
- Maps stacked: both x=137, w=1152 (full content box).
- Every rich-text `<p>`: `max-width: 960px`, `margin-left/right: 0`, rendered
  960px at the same x as the headings above it — capped in place, not centred.
- Sub-headings compute `margin-top: 48px`.
- All 9 custom element types upgraded (shadow roots present), no broken images,
  horizontal overflow 0.
- Nav logo shadow `max-width: 320px` (the shared chrome injection).
- Mobile (375px): single 327px column at 24px padding, everything stacked,
  horizontal overflow 0.
- `build-chrome.py --check` → 0/25 pages would change.
- Console: the two `process is not defined` errors from the CDN bundle, byte-for-byte
  the same as on `frederick-douglass-scholarship.html`. Pre-existing, not introduced here.
