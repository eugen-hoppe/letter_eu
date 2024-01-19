from enum import Enum


class Account(str, Enum):
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
        name, street = Account.NAME.value, Account.STREET.value
        return name + sep + street + sep + Account.postal_code_and_city()
