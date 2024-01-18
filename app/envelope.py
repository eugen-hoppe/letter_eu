from fpdf import FPDF

from app.constants import Mark


class Envelope(FPDF):
    def envelope_marks(self):
        """
        Adds hole mark (HM) and folding marks (FM1 + FM2) to template
        """
        self.line(Mark.LEFT, Mark.FOLD_Y1, Mark.FOLD_X, Mark.FOLD_Y1)  # FM1
        self.line(Mark.LEFT, Mark.HOLE_Y, Mark.HOLE_X, Mark.HOLE_Y)  # HM
        self.line(Mark.LEFT, Mark.FOLD_Y2, Mark.FOLD_X, Mark.FOLD_Y2)  # FM2
