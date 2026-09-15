"""Reusable Admissions rich-text HTML patterns."""

from __future__ import annotations

from collections.abc import Sequence
from html import escape


RICH_TEXT_TABLE_STYLESHEET = "styles/rich-text-table.css"


def rich_text_table_header(
    label: str,
    *,
    second_line: str | None = None,
    screen_reader_only: bool = False,
) -> str:
    """Build safe header content for :func:`render_rich_text_table`."""

    safe_label = escape(label)
    if screen_reader_only:
        return f'<span class="sr-only">{safe_label}</span>'
    if second_line is None:
        return safe_label
    return (
        f"{safe_label} "
        '<span class="umd-text-rich-table-heading-parenthetical">'
        f"{escape(second_line)}</span>"
    )


def render_rich_text_table(
    *,
    caption: str,
    headers_html: Sequence[str],
    rows_html: Sequence[Sequence[str]],
    region_label: str | None = None,
    footnotes_html: Sequence[str] = (),
    total_row_indices: Sequence[int] = (),
    row_headers: bool = True,
) -> str:
    """Render the reusable responsive rich-text table pattern.

    ``caption`` and ``region_label`` are escaped plain text. Values in
    ``headers_html``, ``rows_html``, and ``footnotes_html`` are trusted HTML
    fragments so page-builder content can retain links, emphasis, and ``sup``
    markers. Do not pass untrusted user input to those arguments.
    """

    headers = tuple(headers_html)
    rows = tuple(tuple(row) for row in rows_html)
    footnotes = tuple(footnotes_html)
    total_rows = frozenset(total_row_indices)
    if len(headers) < 2:
        raise ValueError("rich-text tables require at least two columns")
    for index, row in enumerate(rows, start=1):
        if len(row) != len(headers):
            raise ValueError(
                f"row {index} has {len(row)} cells; expected {len(headers)}"
            )
    for index in total_rows:
        if index < 0 or index >= len(rows):
            raise ValueError(
                f"total row index {index} is outside the {len(rows)} rendered rows"
            )

    safe_caption = escape(caption)
    safe_region_label = escape(region_label or caption, quote=True)
    lines = [
        '<div class="umd-text-rich-table-scroll" tabindex="0" role="region" '
        f'aria-label="{safe_region_label}">',
        '  <table class="umd-text-rich-table">',
        f'    <caption class="sr-only">{safe_caption}</caption>',
        "    <thead>",
        "      <tr>",
    ]
    lines.extend(f'        <th scope="col">{header}</th>' for header in headers)
    lines.extend(["      </tr>", "    </thead>", "    <tbody>"])

    for index, row in enumerate(rows):
        row_class = ' class="umd-text-rich-table-total"' if index in total_rows else ""
        lines.append(f"      <tr{row_class}>")
        if row_headers:
            lines.append(f'        <th scope="row">{row[0]}</th>')
            lines.extend(f"        <td>{cell}</td>" for cell in row[1:])
        else:
            lines.extend(f"        <td>{cell}</td>" for cell in row)
        lines.append("      </tr>")

    lines.extend(["    </tbody>", "  </table>", "</div>"])
    if footnotes:
        lines.extend(
            [
                "",
                '<div class="umd-text-rich-advanced umd-text-rich-table-footnotes">',
                "  <ul>",
            ]
        )
        lines.extend(f"    <li>{footnote}</li>" for footnote in footnotes)
        lines.extend(["  </ul>", "</div>"])

    return "\n".join(lines)
