from app.info import Info


class Subject(Info):
    sb_xy_title: tuple[int, int] = (25, 105)
    sb_title: str = ""
    sb_context_fields_color: tuple[int, int, int] = (100, -1, -1)
    sb_y_recipient_context_fields: int = 115
    sb_acccount_id: str = ""
    sb_transaction_id: str = ""
    sb_xy_salutation: tuple[int, int] = (25, 125)
    sb_salutation: str | None = None
    content_color: tuple[int, int, int] = (0, -1, -1)

    def sb_subject(self):
        self.set_xy(*self.sb_xy_title)
        self.set_font(**self.options_font.H3)
        self.multi_cell(
            w=160,  # TODO param?
            h=8,  # TODO param?
            txt=self.sb_title
        )

    def sb_context_account(self):
        self.set_text_color(*self.sb_context_fields_color)
        self.set_xy(25, self.sb_y_recipient_context_fields)
        self.set_font(**self.options_font.P2)
        self.multi_cell(
            w=80,  # TODO param?
            h=5,  # TODO param?
            txt=self.key.ACCOUNT_ID + ": " + self.sb_acccount_id
        )  # TODO method for account_id key value pair OR account context module
    
    def sb_context_transaction(self):
        self.set_text_color(*self.sb_context_fields_color)
        self.set_xy(125, self.sb_y_recipient_context_fields)
        self.set_font(**self.options_font.P2)
        self.multi_cell(
            w=80,  # TODO param?
            h=5,  # TODO param?
            txt=self.key.TRANSACTION_ID + ": " + self.sb_transaction_id
        )  # TODO method for transaction_id key value pair OR transaction context module
    
    def sb_context_salutation(self):
        if self.sb_salutation is None:
            self.sb_salutation = self.key.DEFAULT_SALUTATION_SNIPPET
        self.set_text_color(*self.content_color)
        self.set_xy(*self.sb_xy_salutation)
        self.set_font(**self.options_font.P1)
        self.multi_cell(
            w=160,  # TODO param?
            h=5,  # TODO param?
            txt=self.sb_salutation
        )
    
    def sb_header(self):
        self.info_header()
        # Subjetct Header
        # ===============
        self.sb_subject()
        self.sb_context_account()
        self.sb_context_transaction()
        self.sb_context_salutation()
