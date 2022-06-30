from datetime import datetime
from ctypes import Array

from models.transaction import Transaction
from libs.db import get_tranctions_db, get_bigdata_db

trans_db = get_tranctions_db()
bd_db = get_bigdata_db()

TRANS_COLL = "transactions" # env or another config source

def get_transactions(year: int) -> Array:
    start = datetime(year, 1, 1, 0, 0, 0, 0)
    end = datetime(year, 12, 31, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}
    project = { "payment_id": 1, "amount": 1, "datetime_transaction": 1}
    cur = trans_db[TRANS_COLL].find(query, project)
    
    trans = []
    for res in cur:
        t = Transaction(res["payment_id"], res["amount"], res["datetime_transaction"])
        trans.append(t.__dict__)
    
    return trans

def save_transactions_into_bigdata(trans: Array = []) -> None:
    bd_db[TRANS_COLL].insert_many(trans)
