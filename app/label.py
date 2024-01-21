from app.letterhead import Letterhead


class Label(Letterhead):
    lb_xy_sender: tuple[int, int] = (25, 50)
    lb_color_sender: tuple[int, int, int] = (80, -1, -1)
    lb_xy_recipient: tuple[int, int] = (25, 60)
    lb_color_recipient: tuple[int, int, int] = (0, -1, -1)
    account_address: list[str] = []

    def lb_sender(self):
        self.set_text_color(*self.lb_color_sender)
        self.set_xy(*self.lb_xy_sender)
        self.set_font(**self.options_font.P5)
        self.multi_cell(
            w=80,
            h=5,
            txt=self.admin.address()
        )

    def lb_recipient(self):
        self.set_text_color(*self.lb_color_recipient)
        self.set_xy(*self.lb_xy_recipient)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            80,
            5, 
            txt="\n".join(self.account_address)
        ) 

    def lb_header(self):
        self.lh_header()
        # Label Header
        # ============
        self.lb_sender()
        self.lb_recipient()
