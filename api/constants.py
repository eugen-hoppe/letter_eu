from enum import IntEnum, auto


class AccountContext(IntEnum):
    ADMINISTRATION = auto()
    OPERATION = auto()
    ACCOUNTING = auto()
    EXAMPLE = auto()
    # ...
    SCHEMA = auto()


class TransactionContext(IntEnum):
    REQUEST = auto()
    RESPONSE = auto()
    INVOICE = auto()
    DRAFT = auto()
    # ...
    SCHEMA = auto()
