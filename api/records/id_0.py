from api.constants import AccountContext, TransactionContext
from api.models import Account, Transaction


# Account
# =======
account = Account(
    context=AccountContext.SCHEMA,
    id="d.accounts[0].id",
    name="d.accounts[0].name",
    address_line_2="d.accounts[0].address_line_2",
    street="d.accounts[0].street",
    postal_code="d.accounts[0].postal_code",
    city="d.accounts[0].city",
    transactions=[]
)


# Transactions
# ============
id_0 = Transaction(
    context=TransactionContext.SCHEMA,
    subject="d.accounts[0].transactions[0].subject",
    id="d.accounts[0].transactions[0].id",
    salutation="d.accounts[0].transactions[0].salutation"
)
account.transactions.append(id_0)
