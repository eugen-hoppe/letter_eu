from app.subject import Subject


class Signature(Subject):
    signature: list[str] = []
    signature_color: tuple[int, int, int] = (100, -1, -1)

    def footer(self) -> None:
        self.set_text_color(*self.signature_color)
        self.set_y(-15)
        self.set_font(**self.options_font.P3)
        self.multi_cell(0, 3, "\n".join(self.signature), align='C')
        self.set_y(-8)
        self.cell(
            0, 10, self.key.PAGE_NUMBER + " " + str(self.page_no()), align='C'
        )
