# Frederick Douglass Scholarship

- Source page: https://admissions.umd.edu/tuition/frederick-douglass-scholarship
- Page role: Tuition & Aid interior page
- Hero: `umd-element-hero-minimal` with `data-theme="dark"` and the supplied transparent `images/shared/interior-hero-pattern.png` artwork shared across the four interior pages
- Source image: `images/shared/frederick-douglass-statue.jpg`
- Copy source: reconstructed source capture in `tmp/source.html` on 2026-09-02
  after the live CMS returned a Cloudflare challenge
- Closing banner promo: shared four-page interior treatment, placed inside the 800px content column, with mailing-list and Connect inline links plus one “Join the List” CTA

## Layout treatment

Use the standard interior-page shell: breadcrumb, a three-level Tuition & Aid
`umd-element-nav-slider`, and an 800px editorial content column. The active
slider panel is `Transfer Merit Scholarships`, with `Frederick Douglass
Scholarship` as its selected child rather than a Tuition & Aid sibling.
Preserve the source hierarchy as an introductory figure and text block followed
by `Eligibility` and `How to Apply` rich-text sections. Lists remain semantic
and retain their nested supporting items.

The opening scholarship summary is a bold standard-size paragraph in the
rich-text block directly above the Frederick Douglass image. It uses the
`.fds-intro-copy` hook to pin the visible type weight to 700 and is not a
section-intro component.
