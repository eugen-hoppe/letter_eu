from app.label import Label


class Info(Label):
    info_xy_information: tuple[int, int] = (125, 50)
    info_xy_contact: tuple[int, int] = (125, 70)
    info_xy_date: tuple[int, int] = (125, 90)
    
    def info_information(self):
        self.set_xy(*self.info_xy_information)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,  # TODO param?
            h=5,  # TODO param?
            txt=self.account.address(sep="\n")
        )
    
    def info_contact(self):
        self.set_xy(*self.info_xy_contact)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,  # TODO param?
            h=5,  # TODO param?
            txt=self.account.contact(sep="\n")
        )
    
    def info_date(self, sep: str = ": "):
        self.set_xy(*self.info_xy_date)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,  # TODO param?
            h=5,  # TODO param?
            txt=self.snipppets.DATE_KEY + sep + self.today()
        )
    
    def info_header(self):
        self.lb_header()
        # Info Header
        # ===========
        self.info_information()
        self.info_contact()
        self.info_date()
