from app.letterhead import Letterhead


class Label(Letterhead):
    lb_xy_sender: tuple[int, int] = (30, 50)
    lb_sender_address: str = ""
    lb_xy_recipient: tuple[int, int] = (30, 60)
    lb_recipient_address: list[str] = []

    def lb_sender(self):
        self.set_xy(*self.lb_xy_sender)
        self.set_font(**self.options_font.P3)
        self.multi_cell(
            w=80,
            h=5,
            txt=self.lb_sender_address
        )

    def lb_recipient(self):
        self.set_xy(*self.lb_xy_recipient)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            80,
            5, 
            txt="\n".join(self.lb_recipient_address)
        ) 

    def lb_header(self):
        self.lh_header()
        self.lb_sender()
        self.lb_recipient()
