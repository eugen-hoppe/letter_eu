import os

from os.path import join, dirname

from enum import Enum

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Admin(str, Enum):
    NAME: str = os.environ.get("ADMIN_NAME", "d.admin.NAME")
    ALIAS: str = os.environ.get("ADMIN_ALIAS", "d.admin.ALIAS")
    STREET: str = os.environ.get("ADMIN_STREET", "d.admin.STREET")
    POSTAL_CODE: str = os.environ.get("ADMIN_POSTAL_CODE", "d.admin.POSTAL_CODE")
    CITY: str = os.environ.get("ADMIN_CITY", "d.admin.CITY")
    TELEPHONE: str = os.environ.get("ADMIN_TELEPHONE", "d.admin.TELEPHONE")
    EMAIL: str = os.environ.get("ADMIN_EMAIL", "d.admin.EMAIL")
    WEB: str = os.environ.get("ADMIN_WEB", "d.admin.WEB")

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
    DATE: str = os.environ.get("KEY_DATE", "key.DATE")
    ACCOUNT_ID: str = os.environ.get("KEY_ACCOUNT_ID", "key.ACCOUNT_ID")
    TRANSACTION_ID: str = os.environ.get("KEY_TRANSACTION_ID", "key.TRANSACTION_ID")
    PAGE_NUMBER: str = os.environ.get("KEY_PAGE_NUMBER", "key.PAGE_NUMBER")
    DEFAULT_SALUTATION_SNIPPET: str = os.environ.get(
        "KEY_DEFAULT_SALUTATION_SNIPPET", "key.DEFAULT_SALUTATION_SNIPPET"
    )
