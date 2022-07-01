import calendar

from datetime import datetime
from pymongo.cursor import Cursor
from libs.db import get_bigdata_db

bd_db = get_bigdata_db()

COLLECTION_NAME = "transactions"

def get_transactions(year: int, month: int) -> Cursor:
    last_day = calendar.monthrange(year, month)[1]
    start = datetime(year, month, 1, 0, 0, 0, 0)
    end = datetime(year, month, last_day, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}
    
    res = bd_db[COLLECTION_NAME].find(query)
    return res
