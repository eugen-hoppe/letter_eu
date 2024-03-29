from fpdf import FPDF

from app.settings.constants import Mark, Path
from app.settings.options import Font
from app.settings.config import Admin, Key


class Envelope(FPDF):
    add_envelope_marks: bool = True
    options_font: Font = Font
    key: Key = Key
    admin: Admin = Admin

    def envelope_marks(self):
        """
        Adds hole mark (HM) and folding marks (FM1 + FM2) to template
        """
        self.line(Mark.LEFT, Mark.FOLD_Y1, Mark.FOLD_X, Mark.FOLD_Y1)  # FM1
        self.line(Mark.LEFT, Mark.HOLE_Y, Mark.HOLE_X, Mark.HOLE_Y)  # HM
        self.line(Mark.LEFT, Mark.FOLD_Y2, Mark.FOLD_X, Mark.FOLD_Y2)  # FM2

    def today(self, format_: str = "%d.%m.%Y") -> str:
        return self.creation_date.strftime(format_)

    @staticmethod
    def const_path() -> Path:
        return Path
