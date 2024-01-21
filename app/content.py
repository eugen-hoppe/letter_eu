from app.signature import Signature


class Content(Signature):
    content_xy: tuple[int, int] = (25, 130)
    content_line_height: int = 5
    tb_width: int = 160
    tb_coll_widths: tuple[int, ...] | None = None

    def n_page_y_shift(self, add: int = 0, shift_n_page: int = 20):
        y_shift = self.content_xy[1]
        if self.page_no() != 1:
            y_shift = shift_n_page
        self.content_xy = (self.content_xy[0], y_shift + add)

    def cnt_text(self, text: list[str], y_add: int = 5):
        self.set_text_color(*self.content_color)
        self.content_xy = (self.content_xy[0], self.content_xy[1] + y_add)
        self.set_xy(*self.content_xy)
        self.set_font(**self.options_font.P1)
        self.multi_cell(w=160, h=self.content_line_height, txt="\n".join(text))
        self.n_page_y_shift(len(text) * self.content_line_height)

    def cnt_table(self, tb: list[tuple[str, ...]], y_add: int = 5):
        self.set_text_color(*self.content_color)
        tb_kwargs = {
            "line_height": self.content_line_height,
            "borders_layout": "NONE",
            "width": self.tb_width
        }
        if self.tb_coll_widths is not None:
            tb_kwargs["col_widths"] = self.tb_coll_widths
        self.n_page_y_shift(y_add)
        self.set_xy(*self.content_xy)
        if len(tb):
            with self.table(**tb_kwargs) as table:
                for data_row in tb:
                    row = table.row()
                    for cell in data_row:
                        row.cell(cell)
        table_shift = len(tb) * self.content_line_height
        self.n_page_y_shift(table_shift)
