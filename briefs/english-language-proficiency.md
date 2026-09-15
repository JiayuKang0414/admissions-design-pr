# English Language Proficiency

- Source: https://admissions.umd.edu/apply/english-language-proficiency
- Retrieved: 2026-09-03
- Output: `pages/how-to-apply/english-language-proficiency.html`
- Parent: `How To Apply > International Applicants`

## Component plan

- Dark `umd-element-hero-minimal` using the supplied transparent `images/shared/interior-hero-pattern.png` artwork, shared across the four interior pages.
- `umd-element-breadcrumb` matching the page hierarchy; no left navigation.
- Centered `umd-layout-space-horizontal-normal` content container (1280px maximum with responsive side padding), with long-form rich text capped at 800px and aligned left. Headings, card grids, and two-column sections use the full container width. Existing phone gutters, spacing, and stacking are preserved.
- Existing rich-text styles for all editorial copy and waiver requirements.
- Three text-only light `umd-element-card-overlay` components for the accepted tests, using `umd-layout-grid-gap-three` and `umd-layout-grid-child-fill-height`. The cards form a three-column row at 768px and above and stack on mobile. Each headline links to the test provider; all descriptions, links, and scores remain visible.
- A standalone rich-text section using the standard two-column pattern for the alphabetical English-speaking countries and territories list.
- A Resources section using `umd-layout-grid-gap-two` with one `umd-element-card-icon` for Maryland English Institute, matching the link-icon cards on the Academics page. The linked card heading replaces the separate CTA; both descriptive paragraphs are preserved. One card occupies the left column on desktop, leaving the second column empty, and uses the full width on mobile.
- The shared four-page interior `umd-element-banner-promo`, constrained to the design-system content container, with mailing-list and Connect inline links plus one “Join the List” CTA.

## Design check

The accepted tests use the requested overlay-card component in its text-only color variant, which preserves the full descriptions without the image variant's text truncation. The three cards share a desktop row and stack in source order on mobile; their height follows the content. The country names are a continuous alphabetical list rather than comparative tabular data, so they appear in their own section using the standard responsive two-column rich-text pattern and stack into source order on mobile. The MEI resource uses the standard two-column icon-card grid and explicitly supports a single card without stretching it across both desktop columns. The decorative link icon and linked heading match the Academics page examples. The hero retains the compact dark minimal treatment and uses the supplied FF pattern PNG; the long-form content stays on white for readability.

Visible source copy and links are preserved. Navigation and breadcrumbs are adapted to the prototype's local information architecture.

## Integration notes

Uses the upstream component pin and shared chrome, the shared hero pattern, and a parent-page hero eyebrow. The breadcrumb and body use the same normal-width container. The reviewed 800px rich-text measure is intentional. Existing divider placement is retained from the reviewed prototype.
