from app.envelope import Envelope


class Letterhead(Envelope):
    lh_is_1st_page_different: bool = False
    lh_logo: str | None = Envelope.const_path().LOGO.value
    lh_logo_xyw: dict[str, int] = dict(x=25, y=5, w=20)
    lh_xy: tuple[int, int] = (50, 10)
    lh_color: tuple[int, int, int] = (140, -1, -1)

    def lh_1_page(self) -> None:
        self.set_text_color(*self.lh_color)
        if self.lh_logo:
            self.image(self.lh_logo, **self.lh_logo_xyw)
        self.set_font(**self.options_font.H1)
        self.set_xy(*self.lh_xy)
        self.cell(0, txt=self.admin.ALIAS)
    
    def lh_n_pages(self) -> None:
        if self.lh_is_1st_page_different:
            raise NotImplementedError()  # TODO lh_n_* Attributes
        return self.lh_1_page()

    def lh_header(self) -> None:
        if self.add_envelope_marks:
            self.envelope_marks()
        # Letterhead Header
        # =================
        if self.page_no() == 1:
            self.lh_1_page()
