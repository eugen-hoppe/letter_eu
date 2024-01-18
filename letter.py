from app.envelope import Envelope
from app.constants import Font


if __name__ == "__main__":
    doc = Envelope()
    doc.add_page()
    doc.envelope_marks()

    doc.output('output/envelope.pdf')
