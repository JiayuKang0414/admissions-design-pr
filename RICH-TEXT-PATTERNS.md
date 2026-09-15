# Admissions Rich Text Patterns

Project-owned reusable content functions that extend the shared Page Builder
without changing its `page-builder/` submodule.

## Responsive Rich Text Table

Use `scripts.rich_text.render_rich_text_table()` for structured tabular content
inside an Admissions interior page. The function produces a semantic table,
keyboard-focusable horizontal-scroll wrapper, accessible caption and optional
14px rich-text footnotes.

Add the shared stylesheet to the page `<head>`. Adjust the relative path for the
page depth:

```html
<link rel="stylesheet" href="../../styles/rich-text-table.css">
```

Example:

```python
from scripts.rich_text import render_rich_text_table, rich_text_table_header

table_html = render_rich_text_table(
    caption="Estimated cost of attendance",
    region_label="Estimated cost of attendance table",
    headers_html=(
        rich_text_table_header("Cost category", screen_reader_only=True),
        rich_text_table_header("Maryland Residents", second_line="(In-State)"),
        rich_text_table_header("Nonresidents", second_line="(Out-of-State)"),
    ),
    rows_html=(
        ("Tuition<sup>2</sup> &amp; Fees<sup>3</sup>", "$12,008", "$41,974"),
        ("TOTAL EST. COST OF ATTENDANCE", "$32,408", "$62,374"),
    ),
    total_row_indices=(1,),
    footnotes_html=(
        "<em>Footnote copy.</em>",
        '<em>More details are available on the </em><a href="/policy">policy page</a>.',
    ),
)
```

The stylesheet provides the established Cost of Attendance treatment:

- full-width table with a 680px minimum and horizontal overflow on narrow screens;
- black 71px header with white 18px bold text;
- 16px padding on all header and body cells;
- left-aligned columns and tabular numerals;
- 64px body rows, 1px dividers and alternating white / `#fafafa` zebra stripes;
- optional bold total rows selected with `total_row_indices`; and
- semantic bulleted footnotes at 14px with the standard animated link underline.

`headers_html`, `rows_html`, and `footnotes_html` intentionally accept trusted
HTML fragments so authored content can contain links, emphasis and superscript
markers. Never pass user-submitted HTML to those arguments.

By default, the first cell in each row is emitted as a semantic row header.
Pass `row_headers=False` when every column contains equivalent data, such as a
multi-column alphabetical country list.
