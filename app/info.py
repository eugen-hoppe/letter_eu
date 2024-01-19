from app.label import Label



class Info(Label):
    lb_xy_info: tuple[int, int] = (125, 50)
    
    def information(self):
        self.set_xy(*self.lb_xy_info)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=80,
            h=5,
            txt=self.conf_account().address(sep="\n")
        )
    
    def info_header(self):
        self.lb_header()
        self.information()
