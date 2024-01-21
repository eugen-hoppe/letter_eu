from dataclasses import dataclass, field

from api.constants import AccountContext, TransactionContext


@dataclass
class Account:
    id: str  # count accounts ?
    name: str
    address_line_2: str
    street: str
    postal_code: str
    city: str
    transactions: list["Transaction"] = field(default=list)
    context: AccountContext = AccountContext.ADMINISTRATION

    def address(self) -> list[str]:
        p_code_and_city = self.postal_code + " " + self.city
        return [self.name, self.address_line_2, self.street, p_code_and_city]


@dataclass
class Transaction:
    subject: str
    id: str  # timestamp as default value?
    salutation: str | None = None
    context: TransactionContext = TransactionContext.REQUEST
