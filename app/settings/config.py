from enum import Enum


class Admin(str, Enum):
    NAME: str = "d.admin.NAME"
    ALIAS: str = "d.admin.ALIAS"
    STREET: str = "d.admin.STREET"
    POSTAL_CODE: str = "d.admin.POSTAL_CODE"
    CITY: str = "d.admin.CITY"
    TELEPHONE: str = "d.admin.TELEPHONE"
    EMAIL: str = "d.admin.EMAIL"
    WEB: str = "d.admin.WEB"

    @staticmethod
    def postal_code_and_city():
        return Admin.POSTAL_CODE + " " + Admin.CITY
    
    @staticmethod
    def address(sep: str = "  |  "):
        p_code_and_city = Admin.postal_code_and_city()
        return Admin.NAME + sep + Admin.STREET + sep + p_code_and_city

    @staticmethod
    def contact(sep: str = "  |  "):
        return Admin.TELEPHONE + sep + Admin.EMAIL + sep + Admin.WEB


class Key(str, Enum):
    DATE: str = "key.DATE"
    ACCOUNT_ID: str = "key.ACCOUNT_ID"
    TRANSACTION_ID: str = "key.TRANSACTION_ID"
    DEFAULT_SALUTATION_SNIPPET: str = "key.DEFAULT_SALUTATION_SNIPPET"
    PAGE_NUMBER: str = "key.PAGE_NUMBER"
