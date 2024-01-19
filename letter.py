from app import envelope, letterhead, label


if __name__ == "__main__":
    example_pdfs, examle_id = {}, 2
    if examle_id == 1:
        example_pdfs[examle_id] = "envelope.pdf"
        doc = envelope.Envelope()
        doc.add_page()
        doc.envelope_marks()
    if examle_id == 2:
        example_pdfs[examle_id] = "letterhead.pdf"
        doc = letterhead.Letterhead()
        doc.lh_title = "d.lh_title"
        doc.add_page()
        doc.lh_header()
    if examle_id == 3:
        print("Start Dev")
    doc.output(doc.const_path().PDF + example_pdfs[examle_id])
