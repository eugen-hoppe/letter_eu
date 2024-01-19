from app import envelope, letterhead


class Letter(letterhead.Letterhead):
    def header(self) -> None:
        if self.add_envelope_marks:
            self.envelope_marks()
        if self.page_no() == 1:
            self.lh_1_page()
        else:
            self.lh_n_pages()


if __name__ == "__main__":
    examle_id = 2
    if examle_id == 1:
        doc = envelope.Envelope()
    if examle_id == 2:
        doc = Letter()
        doc.lh_title = "d.lh_title"
    doc.add_page()
    doc.output(doc.const_path().PDF + "letterhead.pdf")
