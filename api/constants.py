from enum import IntEnum, auto


class AccountContext(IntEnum):
    ADMINISTRATION = auto()
    OPERATION = auto()
    ACCOUNTING = auto()
    # ...
    TEST = auto()


class TransactionContext(IntEnum):
    REQUEST = auto()
    RESPONSE = auto()
    INVOICE = auto()
    # ...
    TEST = auto()
