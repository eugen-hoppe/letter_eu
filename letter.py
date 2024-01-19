from app import envelope, letterhead, label, info, subject


if __name__ == "__main__":
    example_pdfs, examle_id = {}, 5

    if examle_id == 1:
        example_pdfs[examle_id] = "envelope.pdf"
        doc = envelope.Envelope()
        doc.add_page()
        doc.envelope_marks()

    if examle_id == 2:
        example_pdfs[examle_id] = "letterhead.pdf"
        doc = letterhead.Letterhead()
        doc.add_page()
        doc.lh_header()

    label_recipient_address = [
        "d.account_address.name",
        "d.account_address.address_line_2",
        "d.account_address.street",
        "d.account_address.postal_code_and_city",
    ]

    if examle_id == 3:
        example_pdfs[examle_id] = "label.pdf"
        doc = label.Label()
        doc.account_address = label_recipient_address
        doc.add_page()
        doc.lb_header()

    if examle_id == 4:
        example_pdfs[examle_id] = "info.pdf"
        doc = info.Info()
        doc.account_address = label_recipient_address
        doc.add_page()
        doc.info_header()

    if examle_id == 5:
        example_pdfs[examle_id] = "subject.pdf"
        doc = subject.Subject()
        doc.account_address = label_recipient_address
        doc.sb_acccount_id = "d.sb_account_id"
        doc.sb_transaction_id = "d.sb_transaction_id"
        doc.sb_title = "d.sb_title"
        doc.add_page()
        doc.sb_header()

    doc.output(doc.const_path().PDF + str(examle_id) + "_" + example_pdfs[examle_id])
