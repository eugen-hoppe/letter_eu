from app import envelope, letterhead, label, info, subject, content


if __name__ == "__main__":
    example_pdfs, examle_id = {}, 6

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

    tb_data = [
        ("d.tb_column[0]", "d.tb_column[..]", "d.tb_column[n]"),
        ("d.tb_row[0][0]", "d.tb_row[0][..]", "d.tb_row[0][n]"),
        ("d.tb_row[..][0]", "d.tb_row[..][..]", "d.tb_row[..][n]"),
        ("d.tb_row[n][0]", "d.tb_row[n][..]", "d.tb_row[n][n]"),
    ]

    if examle_id == 6:
        example_pdfs[examle_id] = "content.pdf"
        doc = content.Content()
        doc.account_address = label_recipient_address
        doc.sb_acccount_id = "d.sb_account_id"
        doc.sb_transaction_id = "d.sb_transaction_id"
        doc.sb_title = "d.sb_title"
        doc.signature = [
            "signature.address() | signature.contact()",
            "signature.legal()",
            "signature.disclaimer()",
        ]
        doc.add_page()
        doc.cnt_text(["content line 1", "", "content line 3"], y_add=10)
        doc.cnt_table(tb_data)
        doc.cnt_text(["content line 4", "content ... " * 25 , "content line n"])

    doc.output(doc.const_path().PDF + str(examle_id) + "_" + example_pdfs[examle_id])
