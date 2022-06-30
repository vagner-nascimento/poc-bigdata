from libs.db import get_bigdata_db
bd_db = get_bigdata_db()

TAXES_COLLECTION = "trans_monthly_taxes_amount"

def delete_monthly_taxes(year: int) -> None:
    query = { "_id.year": year }
    bd_db[TAXES_COLLECTION].delete_many(query)
