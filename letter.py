from app.envelope import Envelope


if __name__ == "__main__":
    envelope = Envelope()
    envelope.add_page()
    envelope.envelope_marks()
    envelope.output('output/envelope.pdf')
