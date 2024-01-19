from api.constants import AccountContext, TransactionContext
from api.models import Account, Transaction


# Account
# =======
account = Account(
    context=AccountContext.EXAMPLE,
    id="40120",
    name="John Doe",
    address_line_2="",
    street="Beispiel Str. 42",
    postal_code="40404",
    city="Berlin",
    transactions=[]
)


# Transactions
# ============
id_0 = Transaction(
    context=TransactionContext.SCHEMA,
    subject="Project X",
    id="2023-04-04",
    salutation="Dear Mr. Doe,"
)
account.transactions.append(id_0)
