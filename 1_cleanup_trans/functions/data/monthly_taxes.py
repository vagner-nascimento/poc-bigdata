from libs.db import get_bigdata_db
bd_db = get_bigdata_db()

COLLECTION_NAME = "trans_monthly_taxes"

def delete_monthly_taxes(year: int) -> None:
    query = { "_id.year": year }
    bd_db[COLLECTION_NAME].delete_many(query)
