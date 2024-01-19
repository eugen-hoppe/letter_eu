from enum import Enum


class Mark(float, Enum):
    LEFT: float = 0.5
    HOLE_X: float = 9.5
    HOLE_Y: float = 145.5
    FOLD_Y1: float = 105.0
    FOLD_Y2: float = 210.0
    FOLD_X: float = 4.5


class Path(str, Enum):
    PDF: str = "output/"
    LOGO: str = "app/settings/logo.png"
