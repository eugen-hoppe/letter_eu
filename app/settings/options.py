from enum import Enum, IntEnum


class Family(str, Enum):
    HEADING: str = "Courier"
    TEXT: str = "Helvetica"


class Style(str, Enum):
    ODD: str = ""
    EVEN: str = "B"
    ITALIC: str = "I"


class Size(IntEnum):
    XXL: int = 20
    XL: int = 17
    L: int = 14
    M: int = 10
    S: int = 8
    XS: int = 6
    XXS: int = 5


class Font(dict, Enum):
    H1: dict = dict(family=Family.HEADING, style=Style.ODD, size=Size.XXL)
    H2: dict = dict(family=Family.HEADING, style=Style.EVEN, size=Size.XXL)
    H3: dict = dict(family=Family.HEADING, style=Style.ODD, size=Size.XL)
    H4: dict = dict(family=Family.HEADING, style=Style.EVEN, size=Size.XL)
    H5: dict = dict(family=Family.HEADING, style=Style.ODD, size=Size.M)
    H6: dict = dict(family=Family.HEADING, style=Style.EVEN, size=Size.M)
    P1: dict = dict(family=Family.TEXT, style=Style.ODD, size=Size.M)
    P2: dict = dict(family=Family.TEXT, style=Style.EVEN, size=Size.S)
    P3: dict = dict(family=Family.TEXT, style=Style.ODD, size=Size.XS)
    P4: dict = dict(family=Family.TEXT, style=Style.EVEN, size=Size.XXS)
    PI: dict = dict(family=Family.TEXT, style=Style.ITALIC, size=Size.M)
