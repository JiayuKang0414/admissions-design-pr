import unittest

from scripts.rich_text import render_rich_text_table, rich_text_table_header


class RichTextTableTests(unittest.TestCase):
    def test_renders_accessible_table_and_footnotes(self):
        output = render_rich_text_table(
            caption="Costs & fees",
            headers_html=(
                rich_text_table_header("Cost category", screen_reader_only=True),
                rich_text_table_header("Residents", second_line="(In-State)"),
            ),
            rows_html=(("Tuition<sup>1</sup>", "$12,008"),),
            footnotes_html=("<em>Estimated amount.</em>",),
            total_row_indices=(0,),
        )

        self.assertIn("Costs &amp; fees", output)
        self.assertIn('aria-label="Costs &amp; fees"', output)
        self.assertIn('<th scope="row">Tuition<sup>1</sup></th>', output)
        self.assertIn("umd-text-rich-table-heading-parenthetical", output)
        self.assertIn("umd-text-rich-table-footnotes", output)
        self.assertIn('class="umd-text-rich-table-total"', output)

    def test_rejects_rows_with_the_wrong_cell_count(self):
        with self.assertRaisesRegex(ValueError, "expected 2"):
            render_rich_text_table(
                caption="Costs",
                headers_html=("Category", "Amount"),
                rows_html=(("Tuition",),),
            )

    def test_rejects_total_row_index_outside_rendered_rows(self):
        with self.assertRaisesRegex(ValueError, "outside the 1 rendered rows"):
            render_rich_text_table(
                caption="Costs",
                headers_html=("Category", "Amount"),
                rows_html=(("Tuition", "$12,008"),),
                total_row_indices=(1,),
            )

    def test_can_render_rows_as_equal_data_cells(self):
        output = render_rich_text_table(
            caption="Countries",
            headers_html=("Column one", "Column two"),
            rows_html=(("Antigua", "Ghana"),),
            row_headers=False,
        )

        self.assertIn("<td>Antigua</td>", output)
        self.assertNotIn('scope="row"', output)


if __name__ == "__main__":
    unittest.main()
