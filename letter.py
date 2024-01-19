from app import envelope, letterhead, label, info


if __name__ == "__main__":
    example_pdfs, examle_id = {}, 4

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
        "d.lb_recipient_address.name",
        "d.lb_recipient_address.second_address_line",
        "d.lb_recipient_address.street",
        "d.lb_recipient_address.postal_code_and_city",
    ]

    if examle_id == 3:
        example_pdfs[examle_id] = "label.pdf"
        doc = label.Label()
        doc.lb_recipient_address = label_recipient_address
        doc.add_page()
        doc.lb_header()

    if examle_id == 4:
        example_pdfs[examle_id] = "info.pdf"
        doc = info.Info()
        doc.lb_recipient_address = label_recipient_address
        doc.add_page()
        doc.info_header()

    doc.output(doc.const_path().PDF + str(examle_id) + "_" + example_pdfs[examle_id])
