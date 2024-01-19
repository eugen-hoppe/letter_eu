from app.subject import Subject
from api.records import id_0


TRANSACTION_ID = 0
records = id_0


if __name__ == "__main__":
    d = Subject()
    d.account_address = records.account.address()
    d.sb_acccount_id = records.account.id
    d.sb_transaction_id = records.account.transactions[TRANSACTION_ID].id
    d.sb_title = records.account.transactions[TRANSACTION_ID].subject
    d.add_page()
    d.sb_header()
    file_name = "id_" + records.__name__.split("_")[-1] + "_" + str(TRANSACTION_ID)
    d.output(d.const_path().PDF + file_name + ".pdf")
