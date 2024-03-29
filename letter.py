from app import envelope, letterhead, label, info, subject, content


if __name__ == "__main__":
    example_pdfs, examle_id = {}, 7

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
            doc.admin.address(),
            doc.admin.contact(),
        ]
        doc.add_page()
        doc.cnt_text(["content line 1", "", "content line 3"], y_add=10)
        doc.cnt_table(tb_data)
        doc.cnt_text(["content line 4", "content ... " * 25 , "content line n"])

    if examle_id == 7:
        example_pdfs[examle_id] = "example.pdf"
        doc = content.Content()
        doc.account_address = [
            "Beispiel & Muster GmbH",
            "z.Hd. John Doe",
            "Milchstraße 404",
            "04040 Berlin"
        ]
        doc.sb_acccount_id = "8514731393628"
        doc.sb_transaction_id = "08.01.2024"
        doc.sb_title = "Projekt 404"
        doc.signature = [
            doc.admin.address() + "  |  " +  doc.admin.contact(),
        ]
        doc.add_page()
        text_1 = "das Projekt 404 konnte nicht gefunden werden, "
        text_1 += "da es ein um ein Beispiel handelt. " 
        text_1 += "Sollte es um kein Beipiel handeln, dann teilen Sie mir bitte das mit."
        text_2 = "Vielen Dank im Voraus"

        doc.cnt_text(
            [text_1, "", text_2],
            y_add=10
        )
        doc.cnt_text(
            ["Mit freundlichen Grüßen", " ", doc.admin.NAME],
            y_add=15
        )

    doc.output(doc.const_path().PDF + str(examle_id) + "_" + example_pdfs[examle_id])
