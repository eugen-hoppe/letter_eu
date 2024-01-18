from app.envelope import Envelope


if __name__ == "__main__":
    doc = Envelope()
    doc.add_page()
    doc.envelope_marks()

    doc.output('output/envelope.pdf')
