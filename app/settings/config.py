from enum import Enum


class Account(str, Enum):  # TODO RENAME to Admin
    NAME: str = "account.NAME"
    ALIAS: str = "account.ALIAS"
    STREET: str = "account.STREET"
    POSTAL_CODE: str = "account.POSTAL_CODE"
    CITY: str = "account.CITY"
    TELEPHONE: str = "account.TELEPHONE"
    EMAIL: str = "account.EMAIL"
    WEB: str = "acoount.WEB"

    @staticmethod
    def postal_code_and_city():
        return Account.POSTAL_CODE + " " + Account.CITY
    
    @staticmethod
    def address(sep: str = "  |  "):
        p_code_and_city = Account.postal_code_and_city()
        return Account.NAME + sep + Account.STREET + sep + p_code_and_city

    @staticmethod
    def contact(sep: str = "  |  "):
        return Account.TELEPHONE + sep + Account.EMAIL + sep + Account.WEB


class Snippets(str, Enum):
    DATE_KEY: str = "snippets.DATE_KEY"
    ACCOUNT_ID_KEY: str = "snippets.ACCOUNT_ID_KEY"
    TRANSACTION_ID_KEY: str = "snippets.TRANSACTION_ID_KEY"
    DEFAULT_SALUTATION: str = "snippets.SALUTATION"
