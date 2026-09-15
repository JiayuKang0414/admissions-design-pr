# Cost of Attendance

- Source page: https://admissions.umd.edu/tuition/cost-of-attendance
- Table design references: Figma file `cnHS6mxwVqK7E8ebkejTcC`, cost table node
  `5950:1492` and zebra-stripe example node `5968:787`
- Page role: Tuition & Aid interior page
- Hero: `umd-element-hero-minimal` with `data-theme="dark"` and the supplied transparent `images/shared/interior-hero-pattern.png` artwork shared across the four interior pages
- Closing banner promo: shared four-page interior treatment, placed inside the 800px content column, with mailing-list and Connect inline links plus one “Join the List” CTA
- Copy source: verbatim from the live source page captured on 2026-09-02

## Table treatment

Render this treatment with the project-owned `scripts.rich_text` table function
and shared `styles/rich-text-table.css`; do not duplicate its CSS in the page.

Use the Figma table system: black 71px header with 16px padding and 18px bold
white header text; 64px body rows with 16px padding on all sides; 16px body
text; explicitly left-aligned second and third columns; 1px row dividers;
alternating white and gray-lightest (`#fafafa`) body rows; and a bold total
row. Parentheticals in the two cost-column headers stay on their own second
lines. All explanatory footnotes below the table use 14px text and the
rich-text bulleted-list style.
