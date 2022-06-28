from datetime import datetime
from libs.db import get_bigdata_db
bd_db = get_bigdata_db()

ENT_COLLECTION = "transactions" # env or another config source

def delete_transactions(year: int):
    start = datetime(year, 1, 1, 0, 0, 0, 0)
    end = datetime(year, 12, 31, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}
    bd_db[ENT_COLLECTION].delete_many(query)
