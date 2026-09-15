# Student Support & Safety

- Source: https://admissions.umd.edu/student/student-support
- Retrieved: 2026-09-03
- Output: `pages/student-life/student-support.html`
- Parent: `Student Life`

## Component plan

- Dark `umd-element-hero-minimal` for the interior-page title, using the supplied transparent `images/shared/interior-hero-pattern.png` artwork shared across the four interior pages.
- `umd-element-breadcrumb` matching the Student Life hierarchy; no left navigation.
- A centered `umd-layout-space-horizontal-normal` content container (1280px maximum with responsive side padding), with long-form rich text capped at 800px and aligned left. Headings and two-column sections use the full container width. Existing phone gutters, spacing, and stacking are preserved.
- Standard rich text for the page introduction.
- Alternating two-column rich-text sections for Academics, Wellness and Safety. Each heading stays in the same column as its text with a rule directly below it, and every image uses the same shorter 4:3 landscape aspect ratio.
- An 800px rich-text block aligned left for the longer Transportation & Parking copy and links.
- An Admissions `umd-element-banner-promo` constrained to the same design-system content container. Its stay-in-touch sentence includes inline links to the mailing list and Connect page, with one “Join the List” primary CTA.

## Design check

The three image-led topics use the existing responsive two-column editorial pattern and stack in reading order on mobile. Their headings remain grouped with their copy and outside the rich-text typography scope, with each standard rich-text rule directly below its heading. A shared 4:3 crop reduces desktop image height by one-third compared with the former 8:9 crop, balancing the photos with the adjacent text. Mobile retains its existing 4:3 crop. The desktop Safety photo is framed toward the top to retain the emergency call box and camera. Transportation & Parking uses an 800px reading width because it contains the longest descriptions and the most links. All visible source copy, links and image alt text are preserved. The new page replaces the old external Student Support & Safety link in shared navigation and on the Student Life landing page.

## Integration notes

Uses the upstream component pin and shared chrome, the shared hero pattern, and a parent-page hero eyebrow. The breadcrumb and body use the same normal-width container. The reviewed 800px rich-text measure is intentional. Existing divider placement is retained from the reviewed prototype.
