from libs.db import get_bigdata_db
bd_db = get_bigdata_db()

AMOUNT_COLLECTION = "trans_monthly_amount" # env or another config source

def delete_monthly_amount(year: int) -> None:
    query = { "_id.year": year }
    bd_db[AMOUNT_COLLECTION].delete_many(query)
