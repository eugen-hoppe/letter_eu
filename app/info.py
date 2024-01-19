from app.label import Label


class Info(Label):
    info_xy_information: tuple[int, int] = (125, 50)
    info_xy_contact: tuple[int, int] = (125, 70)
    
    def information(self):
        self.set_xy(*self.info_xy_information)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,
            h=5,
            txt=self.conf_account().address(sep="\n")
        )
    
    def contact(self):
        self.set_xy(*self.info_xy_contact)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,
            h=5,
            txt=self.conf_account().contact(sep="\n")
        )

    
    def info_header(self):
        self.lb_header()
        self.information()
        self.contact()
